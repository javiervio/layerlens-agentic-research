# AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation

- authors_or_org: Wentao Shi, Yu Wang, Yuyang Zhao, Yuxin Chen, Fuli Feng, Xueyuan Hao, Xi Su, Qi Gu, Hui Su, Xunliang Cai, Xiangnan He
- canonical_url: https://arxiv.org/abs/2604.18240
- discovered_url: inbox/discovery/2026-W46.md, full text via inbox/fulltext/https___doi.org_10.48550_arxiv.2604.18240.md
- discovered_via: feed (discovery trend radar, full text fetched by tools/fulltext_fetch.py)
- doi_or_arxiv_id: arXiv:2604.18240v1
- version: v1
- published_at: 2026-04-20
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (the fulltext file delivered is the arXiv abstract page, not a rendered body — the standing fulltext-fetcher bug; labeled accordingly)
- sections_read: abstract
- topics: Agent-as-a-Judge, environment-aware evaluation, judge mechanisms

## Claims from this source
- C-0147: As RL training scales agent training, reliably verifying agent behavior in complex environments is increasingly hard; rule-based verifiers and LLM-as-a-Judge models struggle to generalize beyond narrow domains. "Agent-as-a-Judge" addresses this by actively interacting with environments and tools to acquire verifiable evidence, rather than judging from text alone, but its capabilities remain underexplored. AJ-Bench systematically evaluates Agent-as-a-Judge across three domains (search, data systems, graphical user interfaces), comprising 155 tasks and 516 annotated trajectories, assessing judge agents' information acquisition, state verification, and process verification. Experiments show consistent performance gains over LLM-as-a-Judge baselines, while also revealing substantial open challenges in agent-based verification. (ACL 2026 Findings.)
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; three domains, 155 tasks; "consistent performance gains" and "substantial open challenges" not quantified in the abstract.
  - relationship to existing claims: a distinct flavor of judge mechanism from this knowledge base's existing T-05/I-0010 cluster (TypeSafe AI's Jev, OpenAI's Decisions API, etc. are all typed/decision-only judges reading supplied state; AJ-Bench's Agent-as-a-Judge actively interacts with the environment/tools to gather its own evidence before judging) — complementary, not overlapping, since it targets *how* a judge acquires evidence rather than how confidently it reports a verdict.

## LayerLens relevance
- open question(s) touched: #2 (attribution, judges). LayerLens's own Judges already evaluate traces against a rubric; AJ-Bench's "actively interacts with environments/tools to acquire verifiable evidence" is a reference point for whether a future Judge mechanism should be allowed to probe the environment itself rather than only read a submitted trace — worth noting as a design option, not yet a feature hypothesis.
