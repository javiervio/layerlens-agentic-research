#!/usr/bin/env python3
"""
arXiv harvester. Runs on a GitHub Actions runner (full internet), fetches recent
papers in our categories from the arXiv API, filters to agentic-environment
relevance, and writes them into inbox/arxiv/ so the cloud research routine (which
cannot reach arxiv.org) can read real abstracts and links from its own checkout.

Stdlib only (urllib + xml.etree), so no pip install on the runner.
"""

import time
import urllib.request
import urllib.parse
import datetime
import re
import os
from xml.etree import ElementTree as ET

CATEGORIES = ["cs.MA", "cs.AI", "cs.CL", "cs.HC", "cs.LG", "cs.DC", "cs.OS", "cs.SE"]
MAX_PER_CAT = 40
WINDOW_DAYS = 9  # slight overlap so nothing published late is missed
API = "http://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"

# Lightweight relevance filter (substring match on title+abstract, lowercased).
KEYWORDS = [
    "agent", "agentic", "environment", "sandbox", "tool use", "tool-use",
    "tool-calling", "tool calling", "evaluation", "benchmark", "reward hacking",
    "verifier", "verification", "trajectory", "synthetic", "simulation",
    "multi-agent", "multiagent", "orchestration", "mcp", "human-in-the-loop",
    "oversight", "reliability", "reproducib", "world model", "task feasibility",
    "rollout", "self-improve", "optimizer", "llm judge", "llm-as-a-judge",
]


def fetch_category(cat):
    q = urllib.parse.urlencode({
        "search_query": f"cat:{cat}",
        "start": 0,
        "max_results": MAX_PER_CAT,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"{API}?{q}"
    req = urllib.request.Request(url, headers={"User-Agent": "layerlens-arxiv-harvester/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def parse_entries(xml_bytes, cat):
    root = ET.fromstring(xml_bytes)
    out = []
    for e in root.findall(f"{ATOM}entry"):
        abs_url = (e.findtext(f"{ATOM}id") or "").strip()
        arxiv_id = abs_url.rsplit("/", 1)[-1]
        title = " ".join((e.findtext(f"{ATOM}title") or "").split())
        summary = " ".join((e.findtext(f"{ATOM}summary") or "").split())
        published = (e.findtext(f"{ATOM}published") or "")[:10]
        updated = (e.findtext(f"{ATOM}updated") or "")[:10]
        authors = [a.findtext(f"{ATOM}name") for a in e.findall(f"{ATOM}author")]
        out.append({
            "id": arxiv_id, "abs_url": abs_url.replace("http://", "https://"),
            "title": title, "summary": summary,
            "published": published, "updated": updated,
            "authors": [a for a in authors if a], "primary_cat": cat,
        })
    return out


def relevant(p):
    hay = (p["title"] + " " + p["summary"]).lower()
    return any(k in hay for k in KEYWORDS)


def within_window(p, cutoff):
    d = p["updated"] or p["published"]
    try:
        return datetime.date.fromisoformat(d) >= cutoff
    except ValueError:
        return True  # keep if unparseable rather than silently drop


def main():
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=WINDOW_DAYS)
    iso_year, iso_week, _ = today.isocalendar()
    week_tag = f"{iso_year}-W{iso_week:02d}"

    seen, papers = set(), []
    for cat in CATEGORIES:
        try:
            entries = parse_entries(fetch_category(cat), cat)
        except Exception as ex:  # noqa: BLE001
            print(f"WARN {cat}: {ex}")
            time.sleep(3)
            continue
        for p in entries:
            if p["id"] in seen:
                continue
            if not within_window(p, cutoff):
                continue
            if not relevant(p):
                continue
            seen.add(p["id"])
            papers.append(p)
        time.sleep(3)  # arXiv API asks for a 3s gap between requests

    papers.sort(key=lambda p: (p["updated"] or p["published"]), reverse=True)

    lines = [
        f"# arXiv harvest {week_tag} (fetched {today.isoformat()})",
        "",
        f"{len(papers)} relevant papers across {', '.join(CATEGORIES)}, filtered to the "
        f"last {WINDOW_DAYS} days by an agentic-environment keyword set. Abstracts are "
        "verbatim from the arXiv API. Links preserved. The routine reads this from its "
        "own checkout, so no arxiv.org fetch is needed at run time. Full text for a "
        "specific paper: hand it to a local deep-read session.",
        "",
    ]
    for p in papers:
        auth = ", ".join(p["authors"][:6]) + (" et al." if len(p["authors"]) > 6 else "")
        lines += [
            f"## {p['title']}",
            f"- arxiv_id: {p['id']} · primary surfaced via: {p['primary_cat']}",
            f"- authors: {auth}",
            f"- published: {p['published']} · updated: {p['updated']}",
            f"- link: {p['abs_url']}",
            "",
            f"{p['summary']}",
            "",
        ]

    os.makedirs("inbox/arxiv", exist_ok=True)
    week_path = f"inbox/arxiv/{week_tag}.md"
    content = "\n".join(lines)
    with open(week_path, "w", encoding="utf-8") as f:
        f.write(content)
    with open("inbox/arxiv/LATEST.md", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {len(papers)} papers to {week_path} and LATEST.md")


if __name__ == "__main__":
    main()
