# Copies Are Not Confirmations: How News Duplication Fools LLM Judges and Continual Learners

- authors_or_org: Abdelkader Metales, Miriam Grabenheinrich, Aicha Metales
- canonical_url: https://arxiv.org/abs/2611.09203
- discovered_url: inbox/arxiv/2026-W46.md (cs.CL)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.09203v1
- version: v1
- published_at: 2026-11-06
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: judge bias, consensus-is-cheap, provenance, corroboration

## Claims from this source
- C-0133: LLM judges and continual learners often treat duplicate reports of the same claim (wire-copy, syndicated, press-release) as independent confirmations. In 200,000 CC-News articles, a MinHash detector linked 18.9% to a near-copy from another outlet (precision 0.97), but caught 0% of LLM-generated rewrites of the same claim. Shown three identical reprints instead of one report, two of four tested judges (Llama 3.2 3B, phi4 14B) raised the share of lies they accepted from 0.06 to 0.71 and 0.21 to 0.90 respectively, ignoring an explicit note that the reports shared one source; Gemini 2.5 Flash already believed a single report, while Gemini 2.5 Pro followed provenance notes correctly. Showing a judge one report per detected chain (continual-learning setting) cut copied-lie acceptance by 0.10-0.24pp at a mean cost of at most 4.2pp of accepted truths. A rewrite-detection test (named-entity absence vs. an earlier look-alike) separated LLM rewrites from independent reports at AUC 0.98-0.99 and cut reworded-copy lies accepted from 0.67 to 0.20. The authors conclude counting reports/chains alone is not a reliable defence, the effect of provenance information is judge-dependent, and colluding sources remain an open problem.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; news-domain dataset (CC-News), not an agent-environment benchmark; four judge models.
  - relationship to existing claims: a new, concrete evidence family for T-05/T-02: directly corroborates C-0016's "agreement is not verification" (Calibration Is Not Verification) and T-05's judge-bias thesis with a specific, measurable mechanism — repeated identical sources inflate a judge's apparent confidence even when told the sources are not independent.

## LayerLens relevance
- open question(s) touched: #2 (attribution — a judge treating N copies of one claim as N independent confirmations is a nameable, testable failure mode distinct from same-family bias); general (evaluation/judges scope). Relevant if any LayerLens Judge/Scorer ever aggregates multiple pieces of retrieved evidence toward one verdict.
