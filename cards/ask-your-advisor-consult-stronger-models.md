# Ask Your Advisor: Learning When to Consult Stronger Models in Agentic Systems

- authors_or_org: Pascal Sowietzki, Steffen Holter, Yannick Metz, Emil Kasper, Raphael Baur, Mennatallah El-Assady
- canonical_url: https://arxiv.org/abs/2610.13870
- discovered_url: inbox/arxiv/LATEST.md (2026-W42 harvest)
- discovered_via: feed
- doi_or_arxiv_id: 2610.13870v1
- version: v1
- published_at: 2026-10-09
- retrieved_at: 2026-10-19
- source_type: paper
- access_scope: abstract (verbatim, directly read via arXiv harvester inbox)
- sections_read: abstract only
- topics: escalation, consultation, cost-aware agent design, executor-advisor systems

## Claims from this source
- C-0065: ARIA is a meta-controller for executor-advisor agentic systems (a lower-cost executor model that can selectively consult a stronger advisor model) that frames consultation as a sequential resource-allocation problem: it maps execution evidence to a compact state abstraction at workflow contact points and chooses SILENT or CONSULT, with action values learned by Monte Carlo control from cost-penalized outcomes. Across SWE-bench Verified, Terminal-Bench 2.1, and tau2-bench, ARIA recovers 44-81% of the executor-advisor success gap at under half the advisor's cost, beating ten other evaluated conditions (routing, cascading, fixed/prompted consultation, random placement at matched advice volume). A single consultation-price parameter governs the success-cost trade-off without retraining either model.
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; three benchmarks; "compact state abstraction" internals not described
  - relationship to existing claims: generalizes the confidence-gated escalation pattern T-05/I-0010 has tracked for *judging* (Jev's confidence cascade, C-0032/C-0033) to *execution/tool-use* more broadly — a related but distinct application of the same underlying idea (a cheap default path, escalate on low confidence/high stakes). Strengthens the broader pattern without being additional same-scope evidence for I-0010's narrower judge-verdict framing.

## LayerLens relevance
- open question(s) touched: #2 (attribution — a system that explicitly records when and why it escalated is itself a legible decision trail); general (cost/reliability trade-off framing, adjacent to I-0004's tradeoff-axis hypothesis). Not tied to a new idea/feature row this run — recorded as corroborating evidence for the general "cheap default, escalate on uncertainty" pattern underlying I-0010, per dedup discipline.
