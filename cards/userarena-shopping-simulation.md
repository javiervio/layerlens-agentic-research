# UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents

- authors_or_org: Jujia Zhao, Jiakai Tang, Jing Yu, et al. (incl. Suzan Verberne, Zhaochun Ren)
- canonical_url: https://arxiv.org/abs/2610.30932
- discovered_url: inbox/discovery/LATEST.md (hf-daily, 41 upvotes, 2026-W44) then inbox/fulltext/
- discovered_via: feed (discovery harvester, HF Daily Papers upvote signal)
- doi_or_arxiv_id: arXiv:2610.30932
- version: v1
- published_at: 2026-10-22
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (see the fulltext-harvester note in cards/are-gaia2-meta-environments.md)
- sections_read: abstract (verbatim)
- topics: user simulation, synthetic data validation, offline evaluation against production outcomes

## Claims from this source
- C-0091: UserArena is a real-world e-commerce interactive benchmark (64,729 session trajectories, 11,010 users, 566,102 items, 13 action types) pairing real trajectories with an interactive simulated environment, that **supports offline validation of a simulator against outcomes from a controlled production A/B test** — a five-level evaluation spanning output validity, local decisions, sequential behavior, personalization, and outcomes. The authors' own method (On-Policy Trajectory Distillation, using trajectory-level intent as dense teacher targets on student rollouts) "most closely reproduces the production policy effect in offline simulation" among evaluated simulators.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; single domain (e-commerce/shopping); "most closely reproduces" is a relative, not absolute, fidelity claim; the actual A/B comparison numbers not seen.
  - relationship to existing claims: new — first claim in this knowledge base on validating a user/world simulator's fidelity against a real, independent production outcome (as opposed to validating against another benchmark or a static dataset).

## LayerLens relevance
- open question(s) touched: #6 (synthetic data legibility — "preview a full trace before spending, trace it back to generation and validation"); feeds **I-0008** (establish ground truth for a user-built or prod-imported world), which was previously the weakest idea in the backlog (L0, internally-derived, no external corroboration).
- UserArena's "offline validation against production A/B" pattern is a concrete, external precedent for exactly the validation method I-0008's own "how to validate" section calls for in the abstract ("an actual user asking to grade against their own imported world") — this is the first external research evidence that such validation is a real, published methodology, not just a hoped-for workflow. Strengthens I-0008 from "internally derived" to having one external source.
