# Calibration Is Not Verification: Falsifiability-Aware Conformal Routing for Mixture-of-Agents

- authors_or_org: Nada Rahali, Zijia Wang, Zhisong Liu
- canonical_url: https://arxiv.org/abs/2609.25959
- discovered_via: cs.MA recent listing (Javier request)
- doi_or_arxiv_id: arXiv:2609.25959
- published_at: 2026-09-22
- retrieved_at: 2026-09-29 (manual deep-read, full web session)
- source_type: paper
- access_scope: abstract + summary read directly
- topics: verification vs consensus, factuality, multi-agent agreement, LLM judges

## Claims
- C-0016: Inter-agent agreement is not evidence of correctness; heterogeneous agents can jointly repeat an unsupported claim. Their conformal filter (C-MoA) roughly doubled retained-claim precision on long-form (0.41 to 0.75) but was near-chance on short-form where "consensus is cheap"; moving beyond consensus required a knowledgeable verifier (a memory-only judge scored AUC 0.531, near random).
  - evidence_label: bounded empirical (directly read)
  - relationship: strengthens T-02 (verification-by-construction, not consensus) and differentiator #3 (a self-check/consensus "wobbles"; a real verifier is needed). Research validation of the LayerLens verification thesis.
## LayerLens relevance
- Positioning + differentiator #3; general "agreement is not verification" ammunition and a caution against consensus/LLM-judge-only grading.
