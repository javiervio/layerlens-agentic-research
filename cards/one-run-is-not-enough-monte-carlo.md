# One Run Is Not Enough: A Monte Carlo Protocol for Evaluating LLM Reliability on Data Science Tasks

- authors_or_org: Wenqi Ni, Ozan Evkaya, Miguel de Carvalho
- canonical_url: https://arxiv.org/abs/2611.09729
- discovered_url: inbox/arxiv/2026-W46.md (cs.LG)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.09729v1
- version: v1
- published_at: 2026-11-06
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: reliability, run-to-run variance, pass^k, data science benchmark

## Claims from this source
- C-0137: Assessing LLM reliability on data science tasks requires examining both response quality and consistency across repeated runs, task types, and difficulty levels. DS-QA (100 data science/statistics questions, 16 datasets, 3 difficulty levels, drawn from UK university courses) is evaluated with a three-layer framework (general response properties, coarse-grained metrics, task-specific metrics) using a Monte Carlo protocol of 100 repeated runs per OpenAI model. Results reveal substantial response variability for data-visualization and supervised-learning tasks, particularly at medium/hard difficulty, with verbosity also correlating with token cost (a 0.1 increase in word verbosity ratio corresponds to ~0.013 more token verbosity ratio).
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; one domain (data science/statistics), OpenAI models only; "substantial variability" not given a single headline number in the abstract.
  - relationship to existing claims: a new, directly-named-"one run is not enough" independent family for T-01/I-0001, methodologically similar to C-0019 (Identical Runs) and C-0070 (equivalence-testing/run-count formula) but in a new domain (data science tasks) with the largest per-item repeat count yet seen in this cluster (100 runs/question).

## LayerLens relevance
- open question(s) touched: #5 (reliability vs one lucky pass), directly. Strengthens I-0001/F-0001.
