# ReplayLens: Auditing Agents' Use of Outcomes

- authors_or_org: Dong Xu, Zhangfan Yang, Jiantao Wu, Shipeng Zhang, Zexuan Zhu, Jiangqiang Li, Jun Zhang, Junkai Ji
- canonical_url: https://arxiv.org/abs/2609.34177
- discovered_via: cs.MA recent listing (Javier request)
- doi_or_arxiv_id: arXiv:2609.34177
- published_at: 2026-09-28
- retrieved_at: 2026-09-29 (manual deep-read, full web session)
- source_type: paper
- access_scope: abstract read directly
- topics: outcome auditing, attribution, memory, benchmark validity

## Claims
- C-0017: A black-box audit (change one relationship in stored history at a time) reveals what actually drives an agent's reuse of logged experience: swapping outcome scores changes decisions while moving intact action-score pairs does not, separating score-dependence from order-sensitivity, and exposing cases where agents exploit outcome information rather than genuinely solving the task.
  - evidence_label: bounded empirical (directly read)
  - relationship: strengthens T-02 (agents game/exploit rather than solve) and T-03 (attribution: what drives a decision). Same lab as C-0013.
## LayerLens relevance
- Open Q #2 (attribution); supports F-0002 (attribution as location) and the trust-wall story (an agent exploiting outcome info is exactly what the trust wall blocks).
