# Automated full-text reading and discovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let the weekly research engine automatically find trendy agentic-environment papers and read their full text, instead of depending on someone pasting links and a manual deep-read session.

**Architecture:** New GitHub Actions harvester steps (full internet) pull a trend-radar candidate set from HF Daily Papers, OpenAlex, and wider arXiv queries, then fetch the full body of the top-ranked candidates via ar5iv / arXiv-HTML and commit them to new `inbox/` folders. The cloud routine (which cannot reach arxiv.org/huggingface.co) reads those committed files from its own checkout. A plain `inbox/manual_links.txt` is the fallback intake for off-radar or off-arXiv sources. Pure logic (relevance scoring, ranking, HTML-to-text, rendering) is unit-tested; `main()` does live I/O.

**Tech Stack:** Python 3.12 stdlib only (`urllib`, `xml.etree`, `json`, `re`) so the runner needs no `pip install`, matching the existing harvesters. `pytest` for tests (dev-only, not needed on the runner).

**Spec:** `PROPOSAL-lensy-delivery.md`, "Part B: automated discovery and full-text reading" (verified against AgentMercury arXiv 2608.20634 and live endpoints).

## Global Constraints

- Stdlib only in every `tools/*.py` harvester. No new runtime dependency on the runner.
- No PDF text parsing (no stdlib parser). PDF is a recorded-link fallback only; HTML (ar5iv / arXiv-HTML) is the real full-text path.
- Never delete or rewrite existing inbox content from another harvester; only add new `inbox/discovery/` and `inbox/fulltext/` trees and a `inbox/manual_links.txt`.
- Keep commit size bounded: cap full-text fetches per run and truncate each stored body (exact values below).
- Match the existing harvester house style: module docstring explaining it runs on a runner with full internet, `UA` header on every request, polite inter-request `time.sleep`, print a one-line summary at the end.
- Nothing commits to the live Monday workflow until Javier has reviewed locally (per session protocol).

## Review Focus

- **arXiv id with version suffix** (`2608.20634v1`) vs bare (`2608.20634`): both must dedupe to one paper and both must build a working ar5iv/HTML URL. Covered in Task 2.
- **A candidate that is not on arXiv** (a `breken.ai` URL in `manual_links.txt`): must be fetched generically and stored, never crash the arXiv path. Covered in Task 4.
- **A full-text fetch that fails all sources** (ar5iv down, HTML 404, only PDF): must record the canonical link + "full text unavailable (HTML), PDF link only" and continue, never abort the run. Covered in Task 2 / Task 4.
- **Empty or malformed upstream response** (HF/OpenAlex returns `{}` or non-JSON, arXiv returns an error Atom): the candidate source yields zero candidates and the run continues on the others. Covered in Task 3.
- **Zero candidates overall** (nothing matched this week): writes a valid "no candidates this run" index, does not write empty files that look like a successful large harvest. Covered in Task 3 / Task 4.

---

### Task 1: Shared env-relevance module

**Files:**
- Create: `tools/envkeywords.py`
- Modify: `tools/arxiv_harvest.py:25-33,70-72` (import the shared keywords instead of a local copy; behavior unchanged)
- Test: `tests/test_envkeywords.py`

**Interfaces:**
- Produces: `KEYWORDS: list[str]`; `matched_terms(text: str) -> list[str]` (lowercased substring hits, deduped, order-preserving); `relevance_score(text: str) -> int` (count of distinct matched terms).

- [ ] **Step 1: Write the failing test**

```python
from tools.envkeywords import matched_terms, relevance_score, KEYWORDS

def test_matches_are_distinct_and_lowercased():
    t = "A Multi-Agent sandbox ENVIRONMENT for agentic evaluation"
    terms = matched_terms(t)
    assert "environment" in terms and "sandbox" in terms and "multi-agent" in terms
    assert len(terms) == len(set(terms))

def test_score_counts_distinct_terms():
    assert relevance_score("world model world model") == 1  # one distinct term
    assert relevance_score("no relevant words here") == 0

def test_keywords_cover_core_env_vocab():
    for k in ("agent", "environment", "sandbox", "benchmark", "synthetic"):
        assert k in KEYWORDS
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_envkeywords.py -v`
Expected: FAIL (module not found)

- [ ] **Step 3: Implement `tools/envkeywords.py`**

Move the existing `KEYWORDS` list verbatim from `arxiv_harvest.py`. `matched_terms` lowercases the input once and returns `[k for k in KEYWORDS if k in hay]` with order preserved and no duplicates (KEYWORDS has none). `relevance_score` returns `len(matched_terms(text))`.

- [ ] **Step 4: Refactor `arxiv_harvest.py` to import the shared list**

Replace the local `KEYWORDS` block with `from tools.envkeywords import KEYWORDS` (or a path-safe import matching how the file is run as `python tools/arxiv_harvest.py`; add the minimal `sys.path` shim if needed). `relevant(p)` keeps using `any(k in hay for k in KEYWORDS)`. No behavior change.

- [ ] **Step 5: Run tests + a smoke import of the harvester**

Run: `python3 -m pytest tests/test_envkeywords.py -v && python3 -c "import tools.arxiv_harvest"`
Expected: tests PASS, import clean.

- [ ] **Step 6: Commit**

```bash
git add tools/envkeywords.py tools/arxiv_harvest.py tests/test_envkeywords.py
git commit -m "refactor: shared env-relevance keywords module"
```

---

### Task 2: Full-text fetch core (pure functions)

**Files:**
- Create: `tools/fulltext_fetch.py` (pure functions only in this task; `main()` lands in Task 4)
- Test: `tests/test_fulltext_fetch.py`, `tests/fixtures/ar5iv_sample.html`

**Interfaces:**
- Produces:
  - `arxiv_id_from(s: str) -> str | None` — accepts a bare id, a versioned id, or any arxiv.org/ar5iv URL; returns the id WITHOUT version suffix, else `None`.
  - `fulltext_urls(arxiv_id: str) -> list[tuple[str, str]]` — ordered `(source_label, url)` to try: ar5iv, arXiv-HTML, then the PDF link.
  - `html_to_text(html: str) -> str` — strip scripts/styles/tags to readable text, collapse whitespace.
  - `fetch_fulltext(arxiv_id, fetcher) -> dict` — tries `fulltext_urls` in order using the injected `fetcher(url)->bytes`; returns `{"source", "url", "text"}` on first HTML hit, or `{"source": "pdf-link-only", "url": <pdf>, "text": None}` if only the PDF remains / all HTML fails.
  - `render_fulltext_md(meta: dict, body: dict, max_chars: int) -> str` — one paper's markdown: title, authors, canonical link, signals, source-read line, then the (truncated) body or the unavailable note.

- [ ] **Step 1: Write the failing tests**

```python
from tools.fulltext_fetch import (
    arxiv_id_from, fulltext_urls, html_to_text, fetch_fulltext, render_fulltext_md)

def test_arxiv_id_strips_version_and_parses_urls():
    assert arxiv_id_from("2608.20634v1") == "2608.20634"
    assert arxiv_id_from("2608.20634") == "2608.20634"
    assert arxiv_id_from("https://arxiv.org/html/2608.20634v1") == "2608.20634"
    assert arxiv_id_from("https://ar5iv.labs.arxiv.org/abs/2608.20634") == "2608.20634"
    assert arxiv_id_from("https://breken.ai/post") is None

def test_fulltext_urls_order_ar5iv_html_pdf():
    labels = [lbl for lbl, _ in fulltext_urls("2608.20634")]
    assert labels[0] == "ar5iv" and "pdf" in labels[-1]

def test_html_to_text_strips_markup_and_scripts():
    html = "<html><head><style>x{}</style></head><body><p>Hello</p><script>bad()</script> world</body></html>"
    txt = html_to_text(html)
    assert "Hello" in txt and "world" in txt
    assert "bad()" not in txt and "<p>" not in txt

def test_fetch_fulltext_uses_first_html_source():
    sample = open("tests/fixtures/ar5iv_sample.html", "rb").read()
    got = fetch_fulltext("2608.20634", fetcher=lambda url: sample)
    assert got["source"] == "ar5iv" and "AgentMercury" in got["text"]

def test_fetch_fulltext_falls_back_to_pdf_link_when_html_fails():
    def boom(url):
        raise OSError("blocked")
    got = fetch_fulltext("2608.20634", fetcher=boom)
    assert got["source"] == "pdf-link-only" and got["text"] is None and "pdf" in got["url"]

def test_render_truncates_body():
    md = render_fulltext_md(
        {"title": "T", "authors": ["A"], "link": "L", "signal": "upvotes 9"},
        {"source": "ar5iv", "url": "U", "text": "x" * 100},
        max_chars=10)
    assert "truncated" in md.lower() and md.count("x") <= 10
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_fulltext_fetch.py -v`
Expected: FAIL (module not found). Create `tests/fixtures/ar5iv_sample.html` as a small HTML doc containing the string `AgentMercury` in a `<p>` plus a `<script>` and `<style>` to prove stripping.

- [ ] **Step 3: Implement the pure functions in `tools/fulltext_fetch.py`**

`arxiv_id_from`: regex for `\d{4}\.\d{4,5}` after optionally splitting a URL path; return match without the `vN` suffix, else `None`. `fulltext_urls`: `[("ar5iv", f"https://ar5iv.labs.arxiv.org/abs/{id}"), ("arxiv-html", f"https://arxiv.org/html/{id}"), ("pdf-link", f"https://arxiv.org/pdf/{id}")]`. `html_to_text`: drop `<script>`/`<style>` blocks, replace tags with spaces, unescape entities, collapse whitespace. `fetch_fulltext`: iterate HTML sources (all but the pdf-link), `fetcher(url)`, on success `html_to_text`, require a minimum length (say > 500 chars) else try next; if none succeed return the pdf-link dict with `text=None`. `render_fulltext_md`: header block + body; if `text` is None emit the unavailable note with the PDF link; if `len(text) > max_chars` slice and append `"... [truncated]"`.

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_fulltext_fetch.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add tools/fulltext_fetch.py tests/test_fulltext_fetch.py tests/fixtures/ar5iv_sample.html
git commit -m "feat: full-text fetch core (ar5iv/html/pdf fallback)"
```

---

### Task 3: Discovery harvester (trend radar)

**Files:**
- Create: `tools/discovery_harvest.py`
- Test: `tests/test_discovery_harvest.py`, `tests/fixtures/hf_daily.json`, `tests/fixtures/openalex.json`

**Interfaces:**
- Consumes: `tools.envkeywords.relevance_score`, `matched_terms`.
- Produces:
  - `hf_candidates(data: list|dict) -> list[dict]` — from HF Daily Papers JSON; each `{id, title, summary, link, signal_kind:"upvotes", signal:int, source:"hf-daily"}`, env-filtered by `relevance_score > 0`.
  - `openalex_candidates(data: dict) -> list[dict]` — from OpenAlex works JSON; `{id, title, summary, link, signal_kind:"citations", signal:int, source:"openalex"}`, env-filtered.
  - `arxiv_query_candidates(xml: bytes) -> list[dict]` — from an arXiv API keyword-search Atom response; `signal_kind:"recency"`.
  - `rank_candidates(cands: list[dict]) -> list[dict]` — dedupe by arxiv id / normalized link, keep the richest signal, sort by `(relevance_score, signal)` desc.
  - `render_discovery_md(ranked: list[dict], week_tag, today) -> str` — the human trend radar (all candidates with signals + matched terms + why-surfaced), valid even when `ranked == []`.
  - `main()` — fetch all three live, rank, write `inbox/discovery/{week_tag}.md` + `inbox/discovery/LATEST.md`, and the machine manifest `inbox/_candidates/LATEST.json` (ranked list, top ~25) for Task 4.

- [ ] **Step 1: Write the failing tests**

```python
import json
from tools.discovery_harvest import (
    hf_candidates, openalex_candidates, rank_candidates, render_discovery_md)

def test_hf_keeps_only_env_relevant_with_upvotes():
    data = json.load(open("tests/fixtures/hf_daily.json"))
    cs = hf_candidates(data)
    assert all(c["source"] == "hf-daily" and c["signal_kind"] == "upvotes" for c in cs)
    assert all(c["signal"] >= 0 for c in cs)
    assert any("environment" in (c["title"]+c["summary"]).lower() or
               "agent" in (c["title"]+c["summary"]).lower() for c in cs)

def test_openalex_maps_citations():
    data = json.load(open("tests/fixtures/openalex.json"))
    cs = openalex_candidates(data)
    assert all(c["signal_kind"] == "citations" for c in cs)

def test_rank_dedupes_by_id_and_sorts():
    a = {"id":"2608.20634","title":"Agent env","summary":"sandbox","link":"x","signal_kind":"upvotes","signal":2,"source":"hf-daily"}
    b = {"id":"2608.20634","title":"Agent env","summary":"sandbox","link":"x","signal_kind":"citations","signal":9,"source":"openalex"}
    c = {"id":"1111.00001","title":"agent","summary":"benchmark","link":"y","signal_kind":"recency","signal":0,"source":"arxiv"}
    ranked = rank_candidates([a,b,c])
    assert len([r for r in ranked if r["id"]=="2608.20634"]) == 1  # deduped
    assert ranked[0]["id"] in {"2608.20634","1111.00001"}  # sorted by relevance then signal

def test_render_handles_zero_candidates():
    md = render_discovery_md([], "2026-W43", "2026-10-22")
    assert "no candidates" in md.lower()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_discovery_harvest.py -v`
Expected: FAIL. Create `tests/fixtures/hf_daily.json` (a short list shaped like `https://huggingface.co/api/daily_papers`: items with `paper.id`, `paper.title`, `paper.summary`, `paper.upvotes`, at least one env-relevant and one not) and `tests/fixtures/openalex.json` (shaped like `https://api.openalex.org/works`: `results[]` with `id`, `title`/`display_name`, `abstract_inverted_index` or `abstract`, `cited_by_count`, `doi`).

- [ ] **Step 3: Implement `tools/discovery_harvest.py`**

Parsers tolerate both the documented and empty/malformed shapes (wrap each in try/except, return `[]` on failure). HF id: prefer the arXiv id from `paper.id`. OpenAlex abstract may be an inverted index (reconstruct to text) or absent (empty summary, still scoreable on title). `rank_candidates` keys dedup on `arxiv_id_from(link or id) or normalized link`. `main()` uses the shared `fetch` style with `UA`, polite sleeps, writes the two markdown files + `inbox/_candidates/LATEST.json`; prints `Discovery: N candidates (hf H, openalex O, arxiv A)`.

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_discovery_harvest.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add tools/discovery_harvest.py tests/test_discovery_harvest.py tests/fixtures/hf_daily.json tests/fixtures/openalex.json
git commit -m "feat: discovery harvester (HF Daily Papers + OpenAlex + arXiv queries)"
```

---

### Task 4: Wire full-text `main()` + manual-link intake

**Files:**
- Modify: `tools/fulltext_fetch.py` (add `main()` + `parse_manual_links` + `load_candidates`)
- Create: `inbox/manual_links.txt` (committed, with a header comment; the human-editable fallback intake)
- Test: `tests/test_fulltext_main.py`

**Interfaces:**
- Consumes: Task 2 pure functions; the `inbox/_candidates/LATEST.json` manifest from Task 3.
- Produces:
  - `parse_manual_links(text: str) -> list[dict]` — one URL or arXiv id per non-comment, non-blank line; arXiv lines carry their id, others carry the raw URL with `source:"manual"`.
  - `select_targets(manifest: list[dict], manual: list[dict], cap: int) -> list[dict]` — manual links first (always fetched), then top manifest candidates by rank, deduped, truncated to `cap`.
  - `main()` — read manifest + `inbox/manual_links.txt`, `select_targets(cap=FULLTEXT_CAP)`, fetch each (arXiv via `fetch_fulltext`; non-arXiv manual URL via a generic fetch+`html_to_text`), write `inbox/fulltext/<key>.md` and an `inbox/fulltext/LATEST.md` index.

- [ ] **Step 1: Write the failing tests**

```python
from tools.fulltext_fetch import parse_manual_links, select_targets

def test_parse_manual_links_skips_comments_and_blanks():
    text = "# header\n\nhttps://arxiv.org/abs/2608.20634v1\nhttps://breken.ai/x\n"
    got = parse_manual_links(text)
    assert len(got) == 2
    assert got[0]["id"] == "2608.20634"          # arxiv id extracted, version stripped
    assert got[1]["source"] == "manual" and got[1]["url"].startswith("https://breken.ai")

def test_select_targets_prioritizes_manual_then_caps():
    manifest = [{"id": f"0000.0000{i}", "link": f"l{i}", "rank": i} for i in range(10)]
    manual = [{"id": "2608.20634", "url": "https://arxiv.org/abs/2608.20634"}]
    sel = select_targets(manifest, manual, cap=3)
    assert sel[0]["id"] == "2608.20634"   # manual first
    assert len(sel) == 3                   # capped
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_fulltext_main.py -v`
Expected: FAIL (names not defined).

- [ ] **Step 3: Implement `main()` + helpers; add `inbox/manual_links.txt`**

`FULLTEXT_CAP = 6`, `MAX_BODY_CHARS = 50000`. `parse_manual_links` strips `#`-comment and blank lines; for each line `arxiv_id_from(line)` decides arXiv vs generic. `select_targets` concatenates manual then manifest, dedupes by id/url, slices to `cap`. `main()` is defensive: a missing manifest or missing `manual_links.txt` means an empty list, not a crash; zero targets writes a valid "no full text fetched this run" `LATEST.md`. `inbox/manual_links.txt` ships with a comment block explaining: one arXiv id or URL per line, picked up on the next Monday run, for off-radar or off-arXiv sources.

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_fulltext_main.py -v`
Expected: PASS.

- [ ] **Step 5: Full suite green**

Run: `python3 -m pytest tests/ -v`
Expected: all PASS.

- [ ] **Step 6: Commit**

```bash
git add tools/fulltext_fetch.py tests/test_fulltext_main.py inbox/manual_links.txt
git commit -m "feat: full-text main + manual-link intake fallback"
```

---

### Task 5: Extend the Monday workflow

**Files:**
- Modify: `.github/workflows/arxiv-harvest.yml` (add two run steps + broaden the committed paths)

**Interfaces:**
- Consumes: `tools/discovery_harvest.py`, `tools/fulltext_fetch.py`.

- [ ] **Step 1: Add the harvest steps**

After the existing "Harvest arXiv" step, add "Discover trending papers" (`python tools/discovery_harvest.py`) then "Fetch full text" (`python tools/fulltext_fetch.py`). Order matters: discovery writes the manifest the full-text step reads.

- [ ] **Step 2: Broaden the commit step**

Change `git add inbox/arxiv` to `git add inbox/arxiv inbox/discovery inbox/fulltext inbox/_candidates`. Keep the existing "no changes" guard and commit message pattern.

- [ ] **Step 3: Verify the workflow parses**

Run: `python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/arxiv-harvest.yml')); print('yaml ok')"` (if `yaml` is unavailable, a visual diff review is the fallback).
Expected: `yaml ok`.

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/arxiv-harvest.yml
git commit -m "ci: run discovery + full-text harvest in the Monday workflow"
```

---

### Task 6: Point the routine at the new inboxes

**Files:**
- Modify: `SOURCES.md` (inbox list + the "full text for a specific source" line), `AGENT_RUNBOOK.md:14` (step 1 discover), `tools/arxiv_harvest.py:116-117` (drop the "hand it to a local deep-read session" line)

- [ ] **Step 1: Update `SOURCES.md`**

In the inbox list (lines ~15-20), add `inbox/discovery/LATEST.md` (the trend radar: ranked env-paper candidates with upvote/citation signals) and `inbox/fulltext/LATEST.md` (committed full bodies of the top candidates, read directly, no fetch). Replace the closing "For full text of a specific source, hand it to a local deep-read session." with a line pointing to `inbox/fulltext/` and noting `inbox/manual_links.txt` as the way to request a specific paper or off-arXiv URL for next run.

- [ ] **Step 2: Update `AGENT_RUNBOOK.md` step 1 (Discover)**

Extend "read the THREE inboxes" to include discovery + full-text: the routine now reads full bodies from `inbox/fulltext/` directly (so "open up to two sources deeply" is no longer gated by a blocked fetch for those papers), and uses `inbox/discovery/LATEST.md` as the trend radar. Keep the four-angle combination intact.

- [ ] **Step 3: Fix the stale line in `arxiv_harvest.py`**

Replace the docstring/footer "Full text for a specific paper: hand it to a local deep-read session." with "Full text of the top candidates is fetched automatically into inbox/fulltext/ by tools/fulltext_fetch.py."

- [ ] **Step 4: Verify no stale pointer remains**

Run: `grep -rn "local deep-read session" . --include=*.md --include=*.py`
Expected: no matches (or only historical run logs under `runs/`, which are an immutable record and left as-is).

- [ ] **Step 5: Commit**

```bash
git add SOURCES.md AGENT_RUNBOOK.md tools/arxiv_harvest.py
git commit -m "docs: routine reads inbox/discovery + inbox/fulltext"
```

---

## Local verification before any push (session gate)

Before proposing a PR, run end to end against live endpoints locally (the runner-equivalent) and show Javier the output, since the unit tests deliberately do not hit the network:

```bash
python3 tools/discovery_harvest.py   # writes inbox/discovery + inbox/_candidates
python3 tools/fulltext_fetch.py      # writes inbox/fulltext (should include a real body)
```

Confirm `inbox/fulltext/LATEST.md` lists real papers with real bodies (AgentMercury 2608.20634 is a known-good target to drop in `inbox/manual_links.txt` for the smoke run). Only after Javier reviews locally do we open the PR.
