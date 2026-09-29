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
    # Evaluation / observability competitors (grounded in LayerLens moat + persona docs, plus obvious peers).
    ("Galileo", "https://galileo.ai/blog", []),                       # sitemap
    ("Comet / Opik", "https://www.comet.com/blog", ["https://www.comet.com/blog/feed"]),
    ("Databricks", "https://www.databricks.com/blog", ["https://www.databricks.com/rss.xml"]),
    ("Patronus AI", "https://www.patronus.ai/blog", []),              # sitemap
    ("Humanloop", "https://humanloop.com/blog", []),                  # sitemap
    ("Confident AI (DeepEval)", "https://www.confident-ai.com/blog", []),  # sitemap
    ("Langfuse", "https://langfuse.com/blog", ["https://langfuse.com/rss.xml"]),  # likely WebSearch-only
    ("Vals AI", "https://www.vals.ai", []),                           # no blog path; WebSearch-only, kept on radar
    # Environment / sandbox infrastructure peers (flagship-adjacent).
    ("Daytona", "https://www.daytona.io/blog", ["https://www.daytona.io/rss.xml"]),
    ("Runloop", "https://www.runloop.ai/blog", []),                   # sitemap
]
MAX_PER_SOURCE = 6
WINDOW_DAYS = 120  # competitors post slowly; keep a wide window so the inbox is not empty
ATOM = "{http://www.w3.org/2005/Atom}"
UA = "layerlens-competitor-harvester/1.0 (+research)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


def origin_of(url):
    m = re.match(r"(https?://[^/]+)", url)
    return m.group(1) if m else url


def fetch_title(url):
    """Best-effort readable title from a page; fall back to a slug from the URL."""
    try:
        html = fetch(url).decode("utf-8", "ignore")
        m = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)', html, re.I) \
            or re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
        if m:
            t = re.sub(r"\s+", " ", m.group(1)).strip()
            for sep in (" | ", " · ", " — ", " - "):
                if sep in t:
                    t = t.split(sep)[0].strip()
            if t:
                return t
    except Exception:
        pass
    slug = url.rstrip("/").rsplit("/", 1)[-1].replace("-", " ").replace("_", " ")
    return slug[:120] or url


def sitemap_items(home):
    """Feedless fallback: pull recent /blog/ and /changelog/ post URLs from sitemap.xml."""
    base = origin_of(home)
    try:
        raw = fetch(base + "/sitemap.xml")
        root = ET.fromstring(raw)
    except Exception:
        return []
    def locs_lastmods(r):
        out = []
        for u in r.iter():
            if u.tag.endswith("}url") or u.tag == "url":
                loc = lm = None
                for c in u:
                    if c.tag.endswith("}loc"): loc = (c.text or "").strip()
                    if c.tag.endswith("}lastmod"): lm = (c.text or "").strip()[:10]
                if loc: out.append((loc, lm or ""))
        return out
    entries = []
    if root.tag.endswith("sitemapindex"):
        subs = [c.text.strip() for u in root.iter() for c in u if c.tag.endswith("}loc") and c.text]
        for s in subs[:8]:
            if not any(k in s.lower() for k in ("blog", "post", "changelog", "page", "sitemap")):
                continue
            try:
                entries += locs_lastmods(ET.fromstring(fetch(s)))
            except Exception:
                pass
            time.sleep(1)
    else:
        entries = locs_lastmods(root)
    posts = [(l, lm) for (l, lm) in entries
             if ("/blog/" in l or "/changelog/" in l) and not l.rstrip("/").endswith(("/blog", "/changelog"))]
    # newest first by lastmod (blank sorts last)
    posts.sort(key=lambda x: x[1] or "0000", reverse=True)
    seen, out = set(), []
    for loc, lm in posts:
        if loc in seen:
            continue
        seen.add(loc)
        out.append({"title": fetch_title(loc), "link": loc, "date": lm or "unknown", "summary": ""})
        time.sleep(1)
        if len(out) >= MAX_PER_SOURCE:
            break
    return out


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
        if not got:  # feedless fallback: sitemap
            got = sitemap_items(home)
            if got:
                used = origin_of(home) + "/sitemap.xml (sitemap fallback; titles fetched per page)"
        if got:
            coverage.append(f"- {name}: {len(got)} posts via {used}")
            blocks.append(f"## {name}\nSource: {used} | Home: {home}\n")
            for p in got:
                summ = ("\n" + p["summary"]) if p.get("summary") else ""
                blocks.append(f"### {p['title']}\n- date: {p['date'] or 'unknown'}\n- link: {p['link']}\n{summ}")
        else:
            coverage.append(f"- {name}: NO FEED OR SITEMAP FOUND (cover via WebSearch; home {home})")
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
