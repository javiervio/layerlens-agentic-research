# Does a Self-Learning Migration Agent Learn? An Audited Evaluation of Evidence-Graded Experience Memory for Oracle-to-PostgreSQL Migration

- authors_or_org: Oleg Grynets, Vasyl Lyashkevych, Valeriia Oliferuk, Vladyslav Babenko, Danylo Kovalchuk, Dmytro Kostetskyi
- canonical_url: https://arxiv.org/abs/2611.16143v1
- discovered_url: inbox/arxiv/LATEST.md (cs.SE, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.16143v1
- version: v1
- published_at: 2026-11-12
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: memory, leakage, benchmark contamination, methodological audit

## Claims from this source
- C-0166: An audit of an evidence-graded "self-learning" migration agent (Oracle-to-PostgreSQL) across four studies finds that an apparent memory benefit (persistent memory improved reference conformity by 0.015 [0.004, 0.025] over a no-memory baseline) was largely a measurement artifact: 72% of held-out units (264/367) shared a PostgreSQL reference with training data, and on the 103 leak-free units the memory effect fell to 0.002 [-0.008, 0.011]. A model-free nearest-target-copy baseline (no LLM at all) scored 0.222, beating every LLM system (at most 0.163). A reference-grouped split reducing copying found no statistically distinguishable memory effect (0.005 [-0.003, 0.017]) and no policy-adaptation effect. A separate ground-truth evaluation on real PL/SQL units found 10-22% of "PostgreSQL-accepted" units were behaviorally incorrect; a human-gated fix cycle raised demonstrably correct units from 98/216 to 167/224.
  - locator: abstract
  - evidence_label: bounded empirical (a rigorous, multi-study audit with a model-free baseline specifically designed to detect leakage)
  - limitations: abstract only; domain-specific (Oracle-to-PostgreSQL migration); the audit's own corrective splits (reference-grouped) are themselves a methodology to be checked, not an independently-replicated standard.
  - relationship to existing claims: a strong new T-01/T-02 family and a methodological template — "does it learn, or does it copy/leak" is exactly the kind of audit this knowledge base's existing claims (C-0019, C-0058, C-0151) argue is needed before trusting an apparent improvement; the model-free nearest-target-copy baseline beating every LLM system is a sharp, reusable sanity check.

## LayerLens relevance
- open question(s) touched: #5 (reliability — apparent gains from "learning" need a leakage-aware baseline before being trusted), #1 (comparability)
- general: relevant to I-0008 (ground truth for imported/user-built worlds) and to any LayerLens feature that would let an agent "learn" across tasks within an environment — a model-free copy baseline is a cheap sanity check worth recommending before crediting any such feature with a genuine capability gain.
