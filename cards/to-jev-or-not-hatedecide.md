# To Jev or Not? Evaluating the Accuracy and Efficiency of Structured Decision Models for Hate-Speech Moderation

- authors_or_org: Demetris Paschalides, George Pallis, Marios D. Dikaiakos
- canonical_url: https://arxiv.org/abs/2610.03324v1
- discovered_url: inbox/arxiv/LATEST.md (2026-W41 harvest, cs.CL)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2610.03324v1
- version: v1
- published_at: 2026-10-02
- retrieved_at: 2026-10-12
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the harvested inbox; arxiv.org itself not reachable this run)
- sections_read: abstract
- topics: structured decision models, LLM judges, content moderation, confidence/escalation

## Claims from this source
- C-0049: HATEDECIDE evaluates six structured-decision-model configurations (the Jev/"System One" category: typed answers, no free text) on four hate-speech datasets against specialized moderation, zero-shot, commercial, and supervised baselines. Commercial LLMs significantly outperformed all decision models on only one of four datasets. Supplying a dataset's definition changed up to 28% of predictions without consistently improving classification; decomposing the question into multiple sub-questions significantly improved performance in only 20% of comparisons. On a diagnostic set, the best hosted decision model came within 1.6 macro-F1 points of the best commercial LLM at ~97% lower inference cost.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly; an independent academic evaluation, not from TypeSafe AI or a Jev-affiliated team)
  - limitations: abstract only; hate-speech moderation is one task domain, not necessarily representative of decision-model performance on evaluation/judging tasks generally; "six decision-model configurations" not individually named in the abstract.
  - relationship to existing claims: the second independent, non-Jev-affiliated source for the decision-model/"System One" category (after C-0032/C-0033, both from the Jev research/reference-implementation lineage) — the specific second source I-0010's own maturity note called for to reach L1. The result is a genuine complication, not pure corroboration: definitions and decomposition (two of the category's selling points) do NOT reliably help here, though cost-efficiency (97% cheaper, within 1.6 F1 points) replicates. Treat I-0010 as corroborated on "decision models are a real, competitive, much-cheaper alternative" but not yet on "explicit criteria/decomposition improve quality," which this paper's own task found unreliable.

## LayerLens relevance
- open question(s) touched: #2 (attribution/judge trust). Promotes I-0010 from L0 toward L1 (now backed by evidence from more than one lineage: Jev's own research group plus an independent academic group, plus — see C-0052 this run — a frontier lab's own competing product). The complication (decomposition/definitions not reliably helping) is a genuine build caution: if LayerLens ever exposes a decision-model-style Judge/Scorer, decomposing a rubric into more sub-questions is not automatically better and should be validated per-task, not assumed.
