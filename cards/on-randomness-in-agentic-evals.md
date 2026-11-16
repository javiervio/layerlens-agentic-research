# On Randomness in Agentic Evals

- authors_or_org: KTH (reported; not independently confirmed)
- canonical_url: https://arxiv.org/abs/2602.07150 (as reported; not independently opened — arxiv.org blocked, not in this week's inbox)
- discovered_url: WebSearch, this run's deliberate T-01 contradicting-evidence slice
- discovered_via: search
- doi_or_arxiv_id: arXiv:2602.07150 (as reported)
- version: unknown
- published_at: date unknown (secondary sources place it around 2026-02, "arXiv 2026")
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: incomplete access (WebSearch secondary summary only; no primary text opened)
- sections_read: none directly; summarized via WebSearch result
- topics: reliability, pass@1 variance, run-to-run noise

## Claims from this source
- C-0151: Reportedly, running ~60,000 trajectories on SWE-bench found single-run pass@1 estimates vary by 2.2 to 6.0 percentage points depending on which run is selected, with standard deviations exceeding 1.5 percentage points even at temperature 0; the authors reportedly argue this makes single-run evaluations statistically unsound and recommend multiple runs plus pass^k-style metrics.
  - locator: WebSearch summary only
  - evidence_label: incomplete access
  - limitations: secondary summary only; arXiv id, exact scale, and institutional affiliation (KTH) are as reported by the search summary and not independently verified; this run's own deliberate contradicting-evidence search (per PROTOCOL.md's 20%-budget allowance) found no counter-evidence to T-01, only this further corroboration — a pattern now observed across at least four consecutive runs.
  - relationship to existing claims: if confirmed, a large-scale (60,000-trajectory) fifth-plus independent family for T-01, consistent in direction and rough magnitude with C-0019 (Identical Runs) and this run's C-0137/C-0138.

## LayerLens relevance
- open question(s) touched: #5 (reliability vs one lucky pass). Recorded at incomplete-access confidence; worth a primary-source check (via the arXiv inbox or a reachable mirror) in a future run before citing the specific percentage-point figures externally.
