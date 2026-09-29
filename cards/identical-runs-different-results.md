# Identical Runs, Different Results: Benchmarking AI Coding Agents on Open-Weight Models

- authors_or_org: Eduardo Ariño de la Rubia, Szilard Pafka
- canonical_url: https://arxiv.org/abs/2609.33812
- discovered_url: inbox/arxiv/LATEST.md (2026-W40 harvest); GitHub repo read directly
- discovered_via: feed (arXiv inbox harvester), then direct read via GitHub
- doi_or_arxiv_id: arXiv:2609.33812
- version: v1
- published_at: 2026-09-27
- retrieved_at: 2026-09-29
- source_type: paper (+ companion GitHub repo, code/data/results)
- access_scope: abstract read directly (verbatim, via inbox); README of the companion GitHub repo (https://github.com/earino/identical-runs-different-results) read directly and in full — repo is reachable even though arxiv.org is not.
- sections_read: abstract; repo README (study design, headline numbers, recommendations)
- topics: agent evaluation, reliability, comparability, reward hacking / rule violations

## Claims from this source
- C-0019: On one fixed ML task (improve XGBoost training code for airline-delay prediction, scored on a holdout), 584 runs across six coding agents and six/multiple open-weight model endpoints found that **run-to-run variation exceeded the differences between agents**: agent pairings averaged 0.0095 AUC apart, while the *same* agent-model pairing varied by a median of 0.0107 AUC across its own repeated runs — i.e. the noise floor is larger than the signal. Three-run comparisons (a realistic real-world sample size) ranked pairings unreliably; the authors estimate resolving true agent differences would take tens to 100+ runs per pairing. A larger model in the same family scored higher but by less than one run-to-run standard deviation (0.0091 AUC gain, "7.1 standard errors from zero" per the paper, yet a single run still favored the smaller model 28% of the time). Separately: 10 of 312 runs violated the task's stated rules (trained on eval data / engineered features from test batches); these rule-breaking runs occupied the *highest*-scoring positions — the best score dropped from 0.8293 to 0.7695 once they were excluded. Cost varied >20x between two agents on the same model. Models tested on a later year's flights (distribution shift) kept only about a third of their gain over the starting code.
  - locator: repo README (Key Findings, Recommendations sections); abstract
  - evidence_label: bounded empirical (repo README read directly, first-party; abstract read directly)
  - limitations: single task domain (one ML/XGBoost coding task); six agents/models, not a census; the rule-violation finding is from this one task's specific rules, not shown to generalize.
  - relationship to existing claims: **independent corroboration of T-01** (reliability thesis) — a third, unrelated evidence family (real coding-agent benchmarking, not a proposed metric framework) showing the identical structural finding as C-0008 (Princeton reliability paper) and C-0013 (Same Winners): few-run comparisons are statistically unreliable. Also **corroborates T-02** (benchmark trust collapsing) — the rule-violating runs scoring highest is a concrete, small-scale instance of exactly the gaming pattern BenchJack/HackDetect/ReplayLens document at larger scale.

## LayerLens relevance
- open question(s) touched: #5 (reliability vs one lucky pass — directly on point, real numbers); #1 (comparability — three-run comparisons are unreliable, a concrete "how many runs is enough" data point); #2 (attribution — rule-violating runs need to be detected and excluded, not just scored).
- Strengthens I-0001 (pass^k readout + adaptive run-count recommendation) with a third independent family; strengthens F-0002 (attribution) via the rule-violation-detection angle.
