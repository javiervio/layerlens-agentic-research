# MIRIX-2.0: Multi-Agent Memory System

- authors_or_org: (authors not captured in discovery-harvest entry; see canonical URL)
- canonical_url: https://arxiv.org/abs/2611.12068
- discovered_url: inbox/discovery/LATEST.md (hf-daily, 2026-W47, 18 upvotes)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.12068
- version: v1 (unconfirmed)
- published_at: date unknown (surfaced 2026-W47)
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the discovery inbox)
- sections_read: abstract
- topics: memory architecture, provenance, multi-agent systems

## Claims from this source
- C-0169: MIRIX-2.0, a multi-agent memory system, is reported as the most accurate of compared systems on four of five QA benchmarks (91.4% LoCoMo, 72.6% LongMemEval-S, leading the strongest baseline by 14.3 points there), and reaches the highest mean success among compared memory methods on ALFWorld/WebShop procedural-memory tasks and 49.2% on MetaClaw-Bench (vs. 44.0% for MetaClaw's own skill library). Architecturally, six typed memory agents keep complete records as the system of record, and a "provenance hypergraph" indexes episodic and semantic records with n-ary frames that cite their originating rows; retrieval runs under explicit budgets so the evidence a question inspects does not grow with history; an "AutoDream" process merges duplicate anchors outside the write path without rewriting any record and distills task sessions into reusable skills.
  - locator: abstract
  - evidence_label: bounded empirical
  - limitations: abstract only; author/institution not captured by the discovery harvester's entry; benchmark comparison set and exact baselines not fully specified in what was read.
  - relationship to existing claims: a strong, shipped/open-system-shaped corroboration for I-0013 (track provenance and authority on memory) — "a provenance hypergraph... that cite their rows" is close to a working implementation of exactly the record-level authorship tracking I-0013's hypothesis calls for, at the architecture level rather than as an attack/defense study.

## LayerLens relevance
- open question(s) touched: #7 (human control), general (context and memory — I-0013)
- general: a candidate reference architecture if LayerLens ever builds cross-session memory for an agent-under-test or system type: citing originating rows for every memory frame is the mechanism I-0013 already argues for.
