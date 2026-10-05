# BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure

- authors_or_org: not independently confirmed this run (search-summary only).
- canonical_url: https://arxiv.org/abs/2609.11028
- discovered_url: WebSearch ("arxiv agent evaluation reliability reward hacking October 2026"), then a targeted follow-up search.
- discovered_via: search.
- doi_or_arxiv_id: arXiv:2609.11028
- version: v1
- published_at: 2026-09-10 (per search result metadata)
- retrieved_at: 2026-10-05
- source_type: paper
- access_scope: incomplete access — arxiv.org (abs and html) EGRESS_BLOCKED this run; no GitHub companion repo found (a third-party aggregator, awesomepapers.io, indexes the paper and a derived "trajectories" dataset page, but that domain was not fetched and is not treated as primary).
- sections_read: none directly; WebSearch summary only.
- topics: benchmark/evaluation integrity, reward hacking, agent-evaluator isolation

## Claims from this source
- C-0039: BenchShield is a model-backed instrumentation layer for LLM-agent evaluation infrastructure, positioned as detection-at-the-infrastructure-level rather than a benchmark replacement: it instruments infrastructure points (mounts, host-accepted effects, outcome-input construction, reward provenance, released logs/feedback) to reconstruct what it calls the "reward-relevant trajectory" — the path by which authority and information actually moved during an evaluation run — on the reasoning that transcripts/tool-call logs alone omit exactly these infrastructure-level facts. The team built a human-labeled corpus of 456 adjudicated trajectories drawn from more than 31,000 public agent runs across three benchmarks.
  - locator: WebSearch summary of the abstract/intro.
  - evidence_label: incomplete access.
  - limitations: no primary text; the 456/31,000 figures and the "three benchmarks" are as reported by search summary, not independently verified; no accuracy/precision numbers for the detector itself were captured; author identity/affiliation unconfirmed.
  - relationship to existing claims: a new, independent family for **thesis T-02** (benchmark/evaluator trust collapsing, verification-by-construction becoming purchasable) — distinct in kind from the prior audits (BenchJack C-0001, HackDetect C-0006 audit existing benchmarks after the fact; BenchShield instead proposes instrumenting the infrastructure itself to make the reward-relevant trajectory legible going forward, closer in spirit to LayerLens's own "trust wall built in from the start" framing than to a reactive audit tool).

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — "reward-relevant trajectory" is itself an attribution concept, naming where authority/information moved, not just whether the final score was high).
- Not tied to a new idea/feature row this run (per dedup discipline) — folded into I-0003/F-0002's evidence list as a further, structurally different (instrumentation vs. post-hoc audit) confirmation that the market is converging on "make gaming visible by construction," which is the same principle behind LayerLens's trust wall and attribution surface.
