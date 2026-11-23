# Can You Trust Your Finance Agent? Drift, Diagnosis and Auditable Intervention on One Shipped Financial Research Agent

- authors_or_org: Cosimo Galeone, Anna Ettorre, Ginevra Mariani, Minsu Park, Giuseppe Ettorre, Daniele Ligorio
- canonical_url: https://arxiv.org/abs/2611.17939v1
- discovered_url: inbox/arxiv/LATEST.md (cs.CL, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.17939v1
- version: v1
- published_at: 2026-11-13
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: reliability, attribution, judges, optimization, third-party audit

## Claims from this source
- C-0156: An independent audit of the untuned reference agent shipped with the Vals Finance Agent Benchmark v2 asks four questions a leaderboard score does not answer. Stability: seven identical runs on 18 questions pass between 105 and 123 of 149 rubric criteria, and cost varies by up to 17%. Attribution: of 20 failed trajectories (three runs, nine held-out questions) classified by which layer's owner would remedy them under a taxonomy frozen in advance, 13 trace to the agent's instructions, 3 to its tools, 4 to the model, and none to its data. Diagnosis trust: four blind readers from three model families, given only the traces, name the same fault as the paper's own LLM analyzer in 94% of cases — the same rate at which the readers agree with each other (93%). Change trust: an optimization loop that reads traces, makes one targeted change per round, and keeps it only if it clears a fixed threshold reaches, under a cost objective, 0.34x the baseline cost on held-out questions (95% CI [0.22, 0.58]) at accuracy within noise; under an accuracy objective it gains 14 points on development questions and 1.5 on held-out ones.
  - locator: abstract
  - evidence_label: bounded empirical (a third party auditing a real, shipped agent, not the agent's own vendor)
  - limitations: abstract only; "one shipped financial research agent" — a single system, not a cross-vendor study; exact rubric-criteria definitions and the held-out optimization gap (14 vs 1.5 points) suggest some overfitting to development questions, not fully characterized in the abstract.
  - relationship to existing claims: a strong new, real-production-adjacent independent evidence family for T-01 (run-to-run variance: 105-123/149 across seven identical runs) and T-03 (an attribution taxonomy with a named owner per layer, instructions/tools/model/data, closely paralleling LayerLens's own agent/environment/grader split); the 94% blind-reader agreement with the paper's own LLM analyzer is a rare, directly-measured calibration point for "can a diagnosis be trusted," relevant to I-0010.

## LayerLens relevance
- open question(s) touched: #1 (comparability — 17% cost variance across identical runs), #2 (failure attribution — a frozen, four-layer ownership taxonomy, independently validated at 94% against blind human readers), #5 (reliability — run-to-run pass-rate range on a real shipped agent), #9 (comparison)
- general: a rare third-party audit of a real, already-shipped agent (not a research prototype or a vendor's own benchmark) is exactly the kind of independent-verification precedent LayerLens's own "structural neutrality" positioning should be compared against; also relevant to the existing Vals AI competitive.md entry (the audited benchmark is Vals Finance Agent Benchmark v2).
