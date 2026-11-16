# Hard Issue, Weak Model, or Bad Run? Rethinking Failure Prediction for Coding Agents

- authors_or_org: Xingyue Shi, Wesley K. G. Assunção
- canonical_url: https://arxiv.org/abs/2611.08285
- discovered_url: inbox/arxiv/2026-W46.md (cs.SE)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.08285v1
- version: v1
- published_at: 2026-11-05
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox; arxiv.org itself unreachable this run)
- sections_read: abstract
- topics: attribution, reliability, run-to-run variance, failure prediction

## Claims from this source
- C-0127: On public SWE-bench Verified trajectories (one attempt per model per issue), two run-independent factors dominate trajectory-based failure predictors: issue difficulty (a reference score computed without looking at the run reaches 0.92 AUROC vs ~0.62 for trajectory predictors) and model ability (knowing which model ran predicts failure better than the predictors do). Beyond difficulty and ability, what a predictor gains from reading the trajectory is statistically equivalent to zero. Model-switching gains (vs. an any-model oracle) are no larger than random run-to-run variation alone produces, and per-issue switching gains nothing on held-out runs; a repeated-run pilot shows the same model often solves an issue in some runs and fails it in others, so retrying has real room to repair "bad run" failures specifically, but current predictors cannot tell a bad run apart from a hard issue or a weak model.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; single benchmark (SWE-bench Verified); "repeated-run pilot" scale not stated in the abstract.
  - relationship to existing claims: directly corroborates and sharpens T-03's attribution framing (agent vs environment vs grader -> here, issue/task vs model vs run) and T-01 (run-to-run variance); independent third angle alongside C-0019/C-0070.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — this paper's own "hard issue, weak model, or bad run?" three-way split is close to LayerLens's agent/environment/grader split, applied specifically to the run-vs-ability-vs-difficulty axis), #5 (reliability vs one lucky pass).
