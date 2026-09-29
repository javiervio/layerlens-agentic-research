# Same Winners, Different Success Rates: Evaluating How LLM Agents Recover from Failures

- authors_or_org: Dong Xu, Zhangfan Yang, Jiantao Wu, Shipeng Zhang, Zexuan Zhu, Jiangqiang Li, Jun Zhang, Junkai Ji
- canonical_url: https://arxiv.org/abs/2609.34215
- discovered_via: cs.MA recent listing (Javier request)
- doi_or_arxiv_id: arXiv:2609.34215
- published_at: 2026-09-28
- retrieved_at: 2026-09-29 (manual deep-read, full web session)
- source_type: paper
- access_scope: abstract + summary read directly
- topics: reliability, failure recovery, evaluation validity, ordinal measures

## Claims
- C-0013: Checkpoint/"set-agreement" benchmarks (which action wins) can hide real reliability, because different success-probability pairs (e.g. 0.9,0.8 vs 0.2,0.1) yield identical winning-action distributions. On 864 RecoveryBench episodes + 3,456 planning responses, permuting checkpoint-to-action bindings flips 8-13% of cell-level conclusions; agreement and held-out quality can move in opposite directions. Proposes 4 diagnostic metrics (agreement, all-zero fraction, held-out success, pooled success).
  - evidence_label: bounded empirical (directly read)
  - relationship: strengthens T-01 and supports F-0001 (a single/ordinal number hides reliability). Same lab as ReplayLens (C-0017) - treat those two as one lab, distinct phenomena.
## LayerLens relevance
- Open Q #5 (reliability vs one lucky pass); reinforces pass^k/variance readout (F-0001).
