# HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup

- authors_or_org: Xiang Li, Siyu Lu, Federica Sarro, Claire Le Goues, He Ye
- canonical_url: https://arxiv.org/abs/2611.18443v1
- discovered_url: inbox/arxiv/LATEST.md (cs.SE, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.18443v1
- version: v1
- published_at: 2026-11-13
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: environment lifecycle, checkpointing, coding agents, environment setup

## Claims from this source
- C-0160: Existing coding-agent environment-setup agents control recovery at either single-command granularity (too local to remove polluted state) or whole-script granularity (too coarse to preserve useful progress). HerAgent introduces "semantic setup blocks," one abstraction used for execution, validation, checkpointing, repair, and rollback. Against six prior agents on four environment-setup datasets, HerAgent improves setup success in every comparison, with the largest gains on Installamatic-Bench (52.0% to 85.0%) and SetupBench (46.3% to 70.4%), while cutting setup cost by up to 94.5%.
  - locator: abstract
  - evidence_label: bounded empirical
  - limitations: abstract only; specific to the environment-setup phase (installing dependencies, configuring a runnable environment) rather than task-execution-time checkpointing, a narrower scope than most of T-06's other evidence.
  - relationship to existing claims: a new T-06/I-0007 family, but at a different point in the lifecycle than most prior evidence (Crab, DeltaBox, DSec) — those checkpoint a running task; HerAgent checkpoints the setup phase that precedes any task running at all, a distinction worth preserving in I-0007's framing of "what state persists, when."

## LayerLens relevance
- open question(s) touched: #3 (deterministic replayability), #7 (recovery — a setup-phase-specific checkpoint granularity)
- general: LayerLens's own environments are minted deterministically with no setup phase of this kind (no dependency installation), so this is more relevant to understanding the competitive/research landscape's checkpoint granularity vocabulary ("semantic setup blocks") than to a direct product gap.
