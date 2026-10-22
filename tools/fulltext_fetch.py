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
import re
import urllib.request

UA = "layerlens-fulltext-fetcher/1.0 (+research)"
MIN_HTML_CHARS = 500          # below this, treat the HTML fetch as a miss
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
