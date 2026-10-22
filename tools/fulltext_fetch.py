#!/usr/bin/env python3
"""
Full-text fetcher. Runs on a GitHub Actions runner (full internet) to pull the
whole body of the top candidate papers (ranked by tools/discovery_harvest.py)
plus anything a human dropped in inbox/manual_links.txt, and commit them to
inbox/fulltext/ so the cloud research routine (which cannot reach arxiv.org)
reads real full text from its own checkout instead of only an abstract.

Full text comes from ar5iv or arXiv-HTML (both render the paper body); the PDF
is recorded as a link-only fallback (no stdlib PDF parser, so we never parse it).
Stdlib only (urllib + re + json).
"""

import html as _html
import json
import os
import re
import time
import urllib.request

UA = "layerlens-fulltext-fetcher/1.0 (+research)"
MIN_HTML_CHARS = 500          # below this, treat the HTML fetch as a miss
FULLTEXT_CAP = 6              # most full bodies fetched per run (commit-size bound)
MAX_BODY_CHARS = 50000       # per-paper body cap stored in the inbox
MANIFEST_PATH = "inbox/_candidates/LATEST.json"
MANUAL_LINKS_PATH = "inbox/manual_links.txt"
_ARXIV_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")


def arxiv_id_from(s):
    """Extract a bare arXiv id (no version suffix) from an id or URL, else None."""
    if not s:
        return None
    m = _ARXIV_RE.search(s)
    return m.group(1) if m else None


def fulltext_urls(arxiv_id):
    """Ordered (source_label, url) attempts: ar5iv, arXiv-HTML, then PDF link."""
    return [
        ("ar5iv", f"https://ar5iv.labs.arxiv.org/abs/{arxiv_id}"),
        ("arxiv-html", f"https://arxiv.org/html/{arxiv_id}"),
        ("pdf-link", f"https://arxiv.org/pdf/{arxiv_id}"),
    ]


def _default_fetcher(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def html_to_text(html):
    """Strip scripts/styles/tags to readable text and collapse whitespace."""
    if html is None:
        return ""
    if isinstance(html, bytes):
        html = html.decode("utf-8", "ignore")
    html = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", html, flags=re.I | re.S)
    html = re.sub(r"<[^>]+>", " ", html)
    html = _html.unescape(html)
    return re.sub(r"\s+", " ", html).strip()


def fetch_fulltext(arxiv_id, fetcher=None):
    """
    Try each HTML source in order; return {source,url,text} on the first body
    long enough to be real. If every HTML source fails, return the PDF link with
    text=None so the caller records the canonical link without claiming a body.
    """
    fetcher = fetcher or _default_fetcher
    urls = fulltext_urls(arxiv_id)
    pdf_label, pdf_url = urls[-1]
    for label, url in urls[:-1]:
        try:
            text = html_to_text(fetcher(url))
        except Exception:  # noqa: BLE001 - a blocked/failed source is not fatal
            continue
        if len(text) >= MIN_HTML_CHARS:
            return {"source": label, "url": url, "text": text}
    return {"source": "pdf-link-only", "url": pdf_url, "text": None}


def render_fulltext_md(meta, body, max_chars):
    """Render one paper: header block, then the (truncated) body or a PDF note."""
    authors = ", ".join(meta.get("authors") or []) or "authors unknown"
    lines = [
        f"## {meta.get('title', 'Untitled')}",
        f"- link: {meta.get('link', '')}",
        f"- authors: {authors}",
        f"- signal: {meta.get('signal', 'n/a')}",
        f"- full text via: {body.get('source')} ({body.get('url')})",
        "",
    ]
    text = body.get("text")
    if text is None:
        lines.append(
            "Full text unavailable as HTML (ar5iv/arXiv-HTML did not render); "
            f"PDF link only: {body.get('url')}"
        )
    else:
        if len(text) > max_chars:
            text = text[:max_chars] + " ... [truncated]"
        lines.append(text)
    return "\n".join(lines)


# --- Intake + orchestration (runs on the GitHub Actions runner) ---------------

def parse_manual_links(text):
    """One arXiv id or URL per non-comment, non-blank line -> target dicts."""
    out = []
    for line in (text or "").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        out.append({
            "id": arxiv_id_from(line),
            "arxiv_id": arxiv_id_from(line),
            "url": line,
            "title": "(manual intake)",
            "signal": "manual",
            "source": "manual",
        })
    return out


def load_candidates(path=MANIFEST_PATH):
    """Read the discovery manifest; a missing/broken file yields []."""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except Exception:  # noqa: BLE001
        return []


def _target_key(t):
    return (t.get("arxiv_id") or arxiv_id_from(t.get("url") or t.get("link") or "")
            or t.get("id") or t.get("url") or t.get("link"))


def select_targets(manifest, manual, cap):
    """Manual links first (always fetched), then top manifest candidates, deduped+capped."""
    selected, seen = [], set()
    for t in list(manual) + list(manifest):
        key = _target_key(t)
        if key in seen:
            continue
        seen.add(key)
        selected.append(t)
        if len(selected) >= cap:
            break
    return selected


def _slug(s):
    return re.sub(r"[^A-Za-z0-9._-]", "_", s or "item")[:80]


def _fetch_target(t, fetcher=None):
    """Return (key, meta, body) for one target, arXiv or generic web URL."""
    fetcher = fetcher or _default_fetcher
    arxiv_id = t.get("arxiv_id") or arxiv_id_from(t.get("url") or t.get("link") or t.get("id") or "")
    meta = {
        "title": t.get("title") or "Untitled",
        "authors": t.get("authors") or [],
        "signal": t.get("signal", "n/a"),
    }
    if arxiv_id:
        meta["link"] = f"https://arxiv.org/abs/{arxiv_id}"
        return arxiv_id, meta, fetch_fulltext(arxiv_id, fetcher)
    url = t.get("url") or t.get("link") or ""
    meta["link"] = url
    try:
        text = html_to_text(fetcher(url))
        body = {"source": "web", "url": url, "text": text or None}
    except Exception:  # noqa: BLE001 - a blocked source is recorded, not fatal
        body = {"source": "web-unavailable", "url": url, "text": None}
    return _slug(url), meta, body


def main():
    manifest = load_candidates()
    manual_text = ""
    if os.path.exists(MANUAL_LINKS_PATH):
        with open(MANUAL_LINKS_PATH, encoding="utf-8") as f:
            manual_text = f.read()
    targets = select_targets(manifest, parse_manual_links(manual_text), FULLTEXT_CAP)

    os.makedirs("inbox/fulltext", exist_ok=True)
    index = []
    for t in targets:
        key, meta, body = _fetch_target(t)
        md = render_fulltext_md(meta, body, MAX_BODY_CHARS)
        with open(f"inbox/fulltext/{_slug(key)}.md", "w", encoding="utf-8") as f:
            f.write(md)
        got = "full text" if body.get("text") else "link only"
        index.append(f"- {meta['title']} ({got} via {body['source']}): {meta['link']} "
                     f"-> inbox/fulltext/{_slug(key)}.md")
        time.sleep(2)  # polite gap between full-text fetches

    header = [
        "# Full text fetched this run",
        "",
        "Whole-body text of the top discovery candidates plus any inbox/manual_links.txt "
        "entries, pulled on a runner so the cloud routine reads them directly (no fetch). "
        "Each bullet links to the stored file; 'link only' means HTML did not render and "
        "only the PDF link was recorded.",
        "",
    ]
    body_lines = index if index else ["No full text fetched this run (no candidates or manual links)."]
    with open("inbox/fulltext/LATEST.md", "w", encoding="utf-8") as f:
        f.write("\n".join(header + body_lines) + "\n")
    print(f"Full text: {len(index)} documents written to inbox/fulltext/.")


if __name__ == "__main__":
    main()
