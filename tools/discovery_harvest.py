#!/usr/bin/env python3
"""
Discovery harvester (trend radar). Runs on a GitHub Actions runner (full
internet) and surfaces trendy agentic-environment papers from three angles the
9-day category scan misses:

  - HF Daily Papers  (curated, trending, carries an upvote signal)
  - OpenAlex         (topic search across all time, carries a citation count)
  - wider arXiv queries (keyword search, not just the latest-in-category feed)

It writes a human trend radar to inbox/discovery/ and a machine manifest to
inbox/_candidates/LATEST.json that tools/fulltext_fetch.py reads to decide which
papers to pull in full. The cloud routine cannot reach these endpoints, so this
pre-fetch on the runner is the whole point. Stdlib only (urllib + json + re).
"""

import datetime
import json
import os
import time
import urllib.parse
import urllib.request
from xml.etree import ElementTree as ET

try:
    from tools.envkeywords import relevance_score, matched_terms
    from tools.fulltext_fetch import arxiv_id_from
except ImportError:  # run as `python tools/discovery_harvest.py`
    from envkeywords import relevance_score, matched_terms
    from fulltext_fetch import arxiv_id_from

UA = "layerlens-discovery-harvester/1.0 (+research)"
HF_API = "https://huggingface.co/api/daily_papers"
OPENALEX_API = "https://api.openalex.org/works"
ARXIV_API = "http://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_QUERIES = [
    "agentic environment", "synthetic environment agent", "agent sandbox",
    "tool use benchmark agent", "multi-agent evaluation",
]
MAX_PER_SOURCE = 30
MANIFEST_TOP = 25


def _fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def _text_of(c):
    return (c.get("title", "") + " " + c.get("summary", "")).strip()


def _arxiv_link(arxiv_id, fallback=""):
    return f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else fallback


def hf_candidates(data):
    """HF Daily Papers JSON -> env-relevant candidates with an upvote signal."""
    out = []
    if not isinstance(data, list):
        return out
    for item in data:
        try:
            paper = item.get("paper", item) or {}
            raw_id = str(paper.get("id", "") or "")
            title = paper.get("title") or item.get("title") or ""
            summary = paper.get("summary") or ""
            if relevance_score(title + " " + summary) == 0:
                continue
            arxiv_id = arxiv_id_from(raw_id)
            out.append({
                "id": arxiv_id or raw_id,
                "arxiv_id": arxiv_id,
                "title": title.strip(),
                "summary": summary.strip(),
                "link": _arxiv_link(arxiv_id, f"https://huggingface.co/papers/{raw_id}"),
                "signal_kind": "upvotes",
                "signal": int(paper.get("upvotes", 0) or 0),
                "source": "hf-daily",
            })
        except Exception:  # noqa: BLE001 - skip a malformed row, keep the rest
            continue
    return out


def _reconstruct_abstract(inverted):
    if not isinstance(inverted, dict):
        return ""
    positions = []
    for word, idxs in inverted.items():
        for i in idxs:
            positions.append((i, word))
    positions.sort()
    return " ".join(w for _, w in positions)


def openalex_candidates(data):
    """OpenAlex works JSON -> env-relevant candidates with a citation signal."""
    out = []
    results = (data or {}).get("results") if isinstance(data, dict) else None
    if not isinstance(results, list):
        return out
    for w in results:
        try:
            title = w.get("title") or w.get("display_name") or ""
            summary = w.get("abstract") or _reconstruct_abstract(
                w.get("abstract_inverted_index"))
            if relevance_score(title + " " + summary) == 0:
                continue
            arxiv_id = (w.get("ids", {}) or {}).get("arxiv") or arxiv_id_from(
                w.get("doi") or "")
            arxiv_id = arxiv_id_from(arxiv_id) if arxiv_id else None
            out.append({
                "id": arxiv_id or w.get("id", ""),
                "arxiv_id": arxiv_id,
                "title": title.strip(),
                "summary": summary.strip(),
                "link": _arxiv_link(arxiv_id, w.get("doi") or w.get("id", "")),
                "signal_kind": "citations",
                "signal": int(w.get("cited_by_count", 0) or 0),
                "source": "openalex",
            })
        except Exception:  # noqa: BLE001
            continue
    return out


def arxiv_query_candidates(xml):
    """arXiv keyword-search Atom response -> env-relevant candidates (recency)."""
    out = []
    try:
        root = ET.fromstring(xml)
    except Exception:  # noqa: BLE001
        return out
    for e in root.findall(f"{ATOM}entry"):
        abs_url = (e.findtext(f"{ATOM}id") or "").strip()
        arxiv_id = arxiv_id_from(abs_url)
        title = " ".join((e.findtext(f"{ATOM}title") or "").split())
        summary = " ".join((e.findtext(f"{ATOM}summary") or "").split())
        if relevance_score(title + " " + summary) == 0:
            continue
        out.append({
            "id": arxiv_id or abs_url,
            "arxiv_id": arxiv_id,
            "title": title,
            "summary": summary,
            "link": _arxiv_link(arxiv_id, abs_url.replace("http://", "https://")),
            "signal_kind": "recency",
            "signal": 0,
            "source": "arxiv",
        })
    return out


def _dedup_key(c):
    return c.get("arxiv_id") or arxiv_id_from(c.get("link", "")) or c.get("link") or c.get("id")


def rank_candidates(cands):
    """Dedup by arXiv id / link, keep the richest signal, sort best-first."""
    grouped = {}
    for c in cands:
        key = _dedup_key(c)
        if key not in grouped:
            grouped[key] = dict(c)
            grouped[key]["sources"] = [c["source"]]
        else:
            g = grouped[key]
            if c["source"] not in g["sources"]:
                g["sources"].append(c["source"])
            if c.get("signal", 0) > g.get("signal", 0):
                g["signal"] = c["signal"]
                g["signal_kind"] = c["signal_kind"]
            if relevance_score(_text_of(c)) > relevance_score(_text_of(g)):
                g["title"], g["summary"] = c["title"], c["summary"]
    ranked = sorted(
        grouped.values(),
        key=lambda c: (relevance_score(_text_of(c)), c.get("signal", 0)),
        reverse=True,
    )
    for i, c in enumerate(ranked):
        c["rank"] = i
    return ranked


def render_discovery_md(ranked, week_tag, today):
    lines = [
        f"# Discovery trend radar {week_tag} (fetched {today})",
        "",
        "Trendy agentic-environment papers surfaced from HF Daily Papers (upvotes), "
        "OpenAlex (citations), and wider arXiv keyword queries, ranked by relevance "
        "and signal. The top candidates have their full text pulled into "
        "inbox/fulltext/ by tools/fulltext_fetch.py. Drop a specific paper or URL "
        "into inbox/manual_links.txt to force it in next run.",
        "",
    ]
    if not ranked:
        lines.append("No candidates this run (no env-relevant papers matched).")
        return "\n".join(lines)
    for c in ranked:
        terms = ", ".join(matched_terms(_text_of(c))[:8]) or "none"
        srcs = ", ".join(c.get("sources", [c.get("source", "?")]))
        lines += [
            f"## {c['title']}",
            f"- link: {c['link']}",
            f"- signal: {c['signal_kind']} {c['signal']} | sources: {srcs}",
            f"- matched: {terms}",
            "",
            c.get("summary", ""),
            "",
        ]
    return "\n".join(lines)


def main():
    today = datetime.date.today()
    y, wk, _ = today.isocalendar()
    week_tag = f"{y}-W{wk:02d}"

    hf, oa, ax = [], [], []
    try:
        hf = hf_candidates(json.loads(_fetch(HF_API)))
    except Exception as ex:  # noqa: BLE001
        print(f"WARN hf: {ex}")
    time.sleep(1)
    try:
        oa_url = OPENALEX_API + "?" + urllib.parse.urlencode({
            "search": "agentic environment evaluation",
            "per_page": MAX_PER_SOURCE,
            "sort": "relevance_score:desc",
        })
        oa = openalex_candidates(json.loads(_fetch(oa_url)))
    except Exception as ex:  # noqa: BLE001
        print(f"WARN openalex: {ex}")
    for q in ARXIV_QUERIES:
        try:
            url = ARXIV_API + "?" + urllib.parse.urlencode({
                "search_query": f"all:{q}",
                "start": 0, "max_results": 10,
                "sortBy": "submittedDate", "sortOrder": "descending",
            })
            ax += arxiv_query_candidates(_fetch(url))
        except Exception as ex:  # noqa: BLE001
            print(f"WARN arxiv '{q}': {ex}")
        time.sleep(3)  # arXiv asks for a 3s gap

    ranked = rank_candidates(hf + oa + ax)
    content = render_discovery_md(ranked, week_tag, today.isoformat())

    os.makedirs("inbox/discovery", exist_ok=True)
    os.makedirs("inbox/_candidates", exist_ok=True)
    with open(f"inbox/discovery/{week_tag}.md", "w", encoding="utf-8") as f:
        f.write(content)
    with open("inbox/discovery/LATEST.md", "w", encoding="utf-8") as f:
        f.write(content)
    manifest = [
        {"id": c["id"], "arxiv_id": c.get("arxiv_id"), "title": c["title"],
         "link": c["link"], "rank": c["rank"], "signal_kind": c["signal_kind"],
         "signal": c["signal"], "sources": c.get("sources", [c["source"]])}
        for c in ranked[:MANIFEST_TOP]
    ]
    with open("inbox/_candidates/LATEST.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"Discovery: {len(ranked)} candidates "
          f"(hf {len(hf)}, openalex {len(oa)}, arxiv {len(ax)}). "
          f"Wrote inbox/discovery/{week_tag}.md and manifest ({len(manifest)}).")


if __name__ == "__main__":
    main()
