# Towards a Science of AI Agent Reliability

- authors_or_org: Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan (Princeton)
- canonical_url: https://arxiv.org/abs/2602.16666
- discovered_url: WebSearch (2026-09-28 scheduled run)
- discovered_via: search
- doi_or_arxiv_id: arXiv:2602.16666
- version: v1 2026-02-18; v3 2026-06-02
- published_at: 2026-02-18
- retrieved_at: 2026-09-29 (manual deep-read, local session with full web access)
- source_type: paper
- access_scope: abstract read directly + HTML body sections (metrics, benchmarks, models, findings, limitations); full experimental tables not exhaustively read
- sections_read: abstract, metrics/dimensions, evaluation setup, headline finding, limitations
- topics: agent evaluation, reliability, consistency, non-determinism, pass@k vs pass^k
- venue: ICML 2026

## Claims from this source
- C-0008: 12 reliability metrics across 4 dimensions; capability gains have not produced reliability gains.
  - locator: abstract + metrics section + findings
  - Four dimensions and their metrics (directly read): **Consistency** (outcome, trajectory-distributional, trajectory-sequential, resource), **Robustness** (fault, environment, prompt), **Predictability** (calibration, AUROC/discrimination, Brier), **Safety** (compliance, harm severity).
  - Evaluated 15 models (OpenAI GPT-4 Turbo/4o-mini/o1/GPT-5.2/GPT-5.5, Google Gemini 2.5 Flash/Pro, 3.1 Pro, 3.5 Flash, Anthropic Claude 3/3.5 Haiku, Sonnet 4, Opus 4.5/4.7) across 2 benchmarks: GAIA (165 validation tasks) and tau-bench (26 verified customer-service tasks).
  - Headline finding (verbatim from body): "Overall reliability shows minimal improvement over time, despite 24 months of model releases."
  - evidence_label: bounded empirical (directly read; numbers from abstract + body, not re-derived from raw tables)
  - limitations (stated): two benchmarks cover a narrow task slice; single scaffold per benchmark; LLM-based safety judging is itself a reliability concern; metric decomposition is subjective; temperature 0 may overestimate achievable reliability.
  - relationship to existing claims: same lab as C-0009 (HAL); consistent with HAL's stated pivot to reliability.

## Note on pass@k vs pass^k
The paper uses the pass@k / pass^k (pass-hat-k) terminology within its consistency dimension. The crisp definitions used in this week's brief (pass@k = at least one of k succeeds; pass^k = all k succeed) are the field-standard definitions and are consistent with the paper's usage; the paper's own formal definition was not quoted verbatim in the sections read.

## LayerLens relevance
- Open question #5 (reliability versus one lucky pass), nearly verbatim. Also #9 (comparison surface) via the consistency/predictability metrics.
