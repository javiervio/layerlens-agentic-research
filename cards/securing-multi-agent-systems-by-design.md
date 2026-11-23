# Securing Multi-Agent Systems by Design

- authors_or_org: Xilong Wang, Xiaoxing Chen, Neil Gong
- canonical_url: https://arxiv.org/abs/2611.17883v1
- discovered_url: inbox/arxiv/LATEST.md (cs.CL, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.17883v1
- version: v1
- published_at: 2026-11-13
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: multi-agent systems, security, aggregation, attacks and defenses

## Claims from this source
- C-0157: Multi-agent systems that decompose a task into subtasks, delegate to agents, and aggregate responses are vulnerable to Response Manipulation Attacks (ReMA), which iteratively optimize a malicious agent's responses (formulated as untargeted and targeted optimization problems, approximately solved via feedback from a surrogate multi-agent system) to bias the final aggregated solution. A proposed defense, SecMAS, selects the response most consistent with a sufficiently large subset of other agents' responses using semantic similarity, with theoretically established security guarantees against both attack types; evaluations show existing aggregation rules are vulnerable to ReMA while SecMAS defends against all evaluated attacks, including adaptive variants, at utility comparable to existing rules.
  - locator: abstract
  - evidence_label: bounded empirical (a proposed attack and defense pair with stated theoretical guarantees, not yet observed in a real deployed system)
  - limitations: abstract only; "theoretically established security guarantees" depend on assumptions (e.g. how many agents must be honest) not visible from the abstract.
  - relationship to existing claims: a new, concrete attack/defense pair for T-08 (multi-agent emergent integrity failures) — this is a composability-of-trust failure in the aggregation step specifically, a mechanism distinct from the collusion, bias-laundering, and contract-failure mechanisms T-08 already tracks.

## LayerLens relevance
- open question(s) touched: #13 (multi-agent scope — a concrete new failure class, and a named defense, a system-level grader for multi-agent aggregation would need to catch)
- general: if LayerLens's environment/verification model is ever extended to multi-agent systems (open Q#13), SecMAS's "majority consistency, not majority count" aggregation rule is a candidate reference design for a dedicated multi-agent grader.
