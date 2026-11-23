# Where Autonomy Belongs: A Separation of Powers for Agentic Program Evolution

- authors_or_org: Zhengyang Ai, Tong Liu, Jingxian Tang, Xiaobing Du, Tao Xiao, Fengshi Zhang et al.
- canonical_url: https://arxiv.org/abs/2611.15309v1
- discovered_url: inbox/arxiv/LATEST.md (cs.MA, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.15309v1
- version: v1
- published_at: 2026-11-11
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: attribution, judge independence, program evolution, architecture

## Claims from this source
- C-0162: LLM-driven program evolution rests on three decisions — govern (directs search from accumulated evidence), propose (constructs the next candidate), and judge (settles validity and fitness). Existing systems split into controller-centric (strong govern, weak propose) or agent-centric (one coding agent takes over both govern and propose) designs; neither protects judge's independent authority, which the authors argue is why "benchmark reliability suffers." EvoTrias is a separation-of-powers architecture giving each decision exactly one owner — Structured Governance, Open Proposal, and Protected Judgment behind a private evaluator — exchanging only typed contracts, with runtime hooks reinforcing the boundaries; it can run as a plugin turning an existing coding agent into an evolution system, and sets a new state of the art on mathematical, systems, and algorithm-design benchmarks.
  - locator: abstract
  - evidence_label: bounded empirical / proposal (a named architecture with benchmark results, though the abstract's benchmark-result sentence is truncated)
  - limitations: abstract only; "sets a new state of the art" lacks the specific numbers in what was read.
  - relationship to existing claims: a strong, independent architectural validation of exactly the principle LayerLens's own grader taxonomy already embodies (deterministic Graders kept load-bearing, separate from AI Judges/Scorers) — the authors' explicit argument that judge's authority must never be absorbed into propose or govern is a ready-made, outside articulation of why LayerLens keeps grading mechanically separate from agent reasoning. Feeds I-0003/F-0002 and the trust-wall design logic directly.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — naming judge as a protected, separately-owned authority is close to LayerLens's own agent/environment/grader attribution split, applied here to the evolution-search setting rather than task execution)
- general: a citable, independent articulation of "why judge must be protected, separate authority" — useful for explaining the trust-wall/grader-separation design to a non-technical stakeholder, in the same spirit as tau2-bench's versioning notice.
