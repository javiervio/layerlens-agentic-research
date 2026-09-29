#!/usr/bin/env python3
"""
Reference-sources harvester. Runs on a GitHub Actions runner (full internet) to
pull high-signal, non-competitor sources the cloud research sandbox can't reach:
frontier-lab research/engineering blogs and a few genuinely high-signal analysts.
Writes recent posts to inbox/reference/ for the weekly routine to read in full.

Curated on purpose (signal over volume). Feeds first, then a sitemap fallback for
feedless sites. Anything with neither is logged "cover via WebSearch." Stdlib only.
"""

import time, urllib.request, datetime, os, re
from xml.etree import ElementTree as ET

# name -> (home, [candidate feed URLs]). Empty feed list => go straight to sitemap fallback.
SOURCES = [
    # Frontier lab research / engineering blogs
    ("OpenAI", "https://openai.com/news/", ["https://openai.com/blog/rss.xml"]),
    ("Google DeepMind", "https://deepmind.google/discover/blog/", ["https://deepmind.google/blog/rss.xml"]),
    ("Google Research", "https://research.google/blog/", ["https://research.google/blog/rss/"]),
    ("Microsoft Research", "https://www.microsoft.com/en-us/research/blog/", ["https://www.microsoft.com/en-us/research/feed/"]),
    ("Hugging Face", "https://huggingface.co/blog", ["https://huggingface.co/blog/feed.xml"]),
    ("Anthropic", "https://www.anthropic.com/news", []),   # sitemap fallback (news/research/engineering)
    ("Meta AI", "https://ai.meta.com/blog/", []),          # sitemap fallback
    # High-signal analysts (agent / eval focused, not hype)
    ("Interconnects (Nathan Lambert)", "https://www.interconnects.ai/", ["https://www.interconnects.ai/feed"]),
    ("Import AI (Jack Clark)", "https://importai.substack.com/", ["https://importai.substack.com/feed"]),
    ("Simon Willison", "https://simonwillison.net/", ["https://simonwillison.net/atom/everything/"]),
    ("Latent Space", "https://www.latent.space/", ["https://www.latent.space/feed"]),
]
MAX_PER_SOURCE = 6
POST_SEGMENTS = ("/blog/", "/news/", "/research/", "/discover/blog/", "/engineering/", "/posts/", "/p/", "/changelog/")
ATOM = "{http://www.w3.org/2005/Atom}"
UA = "layerlens-reference-harvester/1.0 (+research)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


def origin_of(url):
    m = re.match(r"(https?://[^/]+)", url)
    return m.group(1) if m else url


def parse_feed(raw):
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return []
    items = []
    for it in root.findall(".//item"):
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        date = (it.findtext("pubDate") or "").strip()[:16]
        desc = re.sub("<[^>]+>", "", (it.findtext("description") or "")).strip()
        if title:
            items.append({"title": title, "link": link, "date": date, "summary": desc[:500]})
    if items:
        return items
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


def fetch_title(url):
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
    base = origin_of(home)
    try:
        root = ET.fromstring(fetch(base + "/sitemap.xml"))
    except Exception:
        return []
    def locs(r):
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
            if not any(k in s.lower() for k in ("blog", "post", "news", "research", "sitemap")):
                continue
            try:
                entries += locs(ET.fromstring(fetch(s)))
            except Exception:
                pass
            time.sleep(1)
    else:
        entries = locs(root)
    posts = [(l, lm) for (l, lm) in entries
             if any(seg in l for seg in POST_SEGMENTS)
             and not l.rstrip("/").endswith(("/blog", "/news", "/research", "/changelog"))]
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


def main():
    today = datetime.date.today()
    y, w, _ = today.isocalendar()
    week_tag = f"{y}-W{w:02d}"
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
        if not got:
            got = sitemap_items(home)
            if got:
                used = origin_of(home) + "/sitemap.xml (sitemap fallback)"
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
        f"# Reference-sources harvest {week_tag} (fetched {today.isoformat()})",
        "",
        "Recent posts from frontier-lab blogs and high-signal analysts, pulled from their "
        "feeds/sitemaps by a GitHub Actions runner (the cloud research sandbox cannot reach "
        "most of these directly). Read alongside inbox/arxiv/ and inbox/competitors/. Curated "
        "for signal, not volume; sources with no feed are listed for WebSearch coverage.",
        "",
        "## Coverage this run",
    ] + coverage + [""] + blocks

    os.makedirs("inbox/reference", exist_ok=True)
    content = "\n".join(lines)
    with open(f"inbox/reference/{week_tag}.md", "w", encoding="utf-8") as f:
        f.write(content)
    with open("inbox/reference/LATEST.md", "w", encoding="utf-8") as f:
        f.write(content)
    reached = sum(1 for c in coverage if "NO FEED" not in c)
    print(f"Reference harvest: {reached}/{len(SOURCES)} sources resolved. Wrote inbox/reference/{week_tag}.md")


if __name__ == "__main__":
    main()
