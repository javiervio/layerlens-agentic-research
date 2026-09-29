#!/usr/bin/env python3
"""
Competitor / team harvester. Runs on a GitHub Actions runner (full internet), so
it can reach competitor blogs and changelogs that the cloud research sandbox
cannot. Pulls each source's RSS/Atom feed, takes the most recent posts, and writes
them to inbox/competitors/ for the weekly routine to read from its own checkout.

Feeds only (no HTML scraping): reliable and clean. A source with no discoverable
feed is logged as "no feed found" so the routine knows to cover it via WebSearch
instead, and coverage stays honest. Stdlib only (urllib + xml.etree), no pip.
"""

import time, urllib.request, datetime, os, re
from xml.etree import ElementTree as ET

# name -> list of candidate feed URLs (first that parses wins). Homepage kept for the log.
SOURCES = [
    ("Braintrust", "https://www.braintrust.dev/blog", [
        "https://www.braintrust.dev/blog/rss.xml", "https://www.braintrust.dev/rss.xml",
        "https://www.braintrust.dev/blog/feed.xml", "https://www.braintrust.dev/feed.xml"]),
    ("Arize", "https://arize.com/blog/", [
        "https://arize.com/blog/feed/", "https://arize.com/feed/", "https://arize.com/blog/rss/"]),
    ("E2B", "https://e2b.dev/blog", [
        "https://e2b.dev/blog/rss.xml", "https://e2b.dev/rss.xml", "https://e2b.dev/blog/feed.xml", "https://e2b.dev/index.xml"]),
    ("Browserbase", "https://www.browserbase.com/blog", [
        "https://www.browserbase.com/blog/rss.xml", "https://www.browserbase.com/rss.xml", "https://www.browserbase.com/feed.xml"]),
    ("Modal", "https://modal.com/blog", [
        "https://modal.com/blog/feed", "https://modal.com/blog/rss.xml", "https://modal.com/rss.xml", "https://modal.com/index.xml"]),
    ("Prime Intellect", "https://www.primeintellect.ai/blog", [
        "https://www.primeintellect.ai/blog/rss.xml", "https://www.primeintellect.ai/rss.xml", "https://www.primeintellect.ai/index.xml"]),
    ("LangChain / LangSmith", "https://blog.langchain.com/", [
        "https://blog.langchain.com/rss/", "https://blog.langchain.dev/rss/"]),
]
MAX_PER_SOURCE = 6
WINDOW_DAYS = 120  # competitors post slowly; keep a wide window so the inbox is not empty
ATOM = "{http://www.w3.org/2005/Atom}"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "layerlens-competitor-harvester/1.0 (+research)"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


def parse_feed(raw):
    """Return list of {title, link, date, summary} from RSS or Atom, or [] if unparseable."""
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return []
    items = []
    # RSS: channel/item
    for it in root.findall(".//item"):
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        date = (it.findtext("pubDate") or "").strip()[:16]
        desc = re.sub("<[^>]+>", "", (it.findtext("description") or "")).strip()
        if title:
            items.append({"title": title, "link": link, "date": date, "summary": desc[:500]})
    if items:
        return items
    # Atom: entry
    for e in root.findall(ATOM + "entry"):
        title = " ".join((e.findtext(ATOM + "title") or "").split())
        link = ""
        for l in e.findall(ATOM + "link"):
            if l.get("rel") in (None, "alternate") and l.get("href"):
                link = l.get("href"); break
        date = (e.findtext(ATOM + "updated") or e.findtext(ATOM + "published") or "")[:10]
        summ = re.sub("<[^>]+>", "", (e.findtext(ATOM + "summary") or e.findtext(ATOM + "content") or "")).strip()
        if title:
            items.append({"title": title, "link": link, "date": date, "summary": summ[:500]})
    return items


def main():
    today = datetime.date.today()
    iso_year, iso_week, _ = today.isocalendar()
    week_tag = f"{iso_year}-W{iso_week:02d}"

    blocks, coverage = [], []
    for name, home, feeds in SOURCES:
        got, used = [], None
        for fu in feeds:
            try:
                items = parse_feed(fetch(fu))
            except Exception:
                items = []
            if items:
                got, used = items[:MAX_PER_SOURCE], fu
                break
            time.sleep(1)
        if got:
            coverage.append(f"- {name}: {len(got)} posts via {used}")
            blocks.append(f"## {name}\nFeed: {used} | Home: {home}\n")
            for p in got:
                blocks.append(f"### {p['title']}\n- date: {p['date'] or 'unknown'}\n- link: {p['link']}\n\n{p['summary']}\n")
        else:
            coverage.append(f"- {name}: NO FEED FOUND (cover via WebSearch; home {home})")
        time.sleep(3)

    lines = [
        f"# Competitor / team harvest {week_tag} (fetched {today.isoformat()})",
        "",
        "Recent posts from competitor and reference-team blogs, pulled from their RSS/Atom "
        "feeds by a GitHub Actions runner (the cloud research sandbox cannot reach these "
        "directly). Read this alongside inbox/arxiv/. Sources with no feed are listed so you "
        "cover them via WebSearch and log the gap honestly.",
        "",
        "## Coverage this run",
    ] + coverage + [""] + blocks

    os.makedirs("inbox/competitors", exist_ok=True)
    content = "\n".join(lines)
    with open(f"inbox/competitors/{week_tag}.md", "w", encoding="utf-8") as f:
        f.write(content)
    with open("inbox/competitors/LATEST.md", "w", encoding="utf-8") as f:
        f.write(content)
    reached = sum(1 for c in coverage if "NO FEED" not in c)
    print(f"Competitor harvest: {reached}/{len(SOURCES)} sources had a feed. Wrote inbox/competitors/{week_tag}.md")


if __name__ == "__main__":
    main()
