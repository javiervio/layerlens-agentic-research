# Beyond Pass@k: Measuring Reliability and Security of Agentic Code Generation

- authors_or_org: authors of arXiv:2608.14711 (not independently confirmed by name this run — see limitations)
- canonical_url: https://arxiv.org/abs/2608.14711
- discovered_url: WebSearch, this run's deliberate contradicting-evidence search slice ("agent evaluation reliability skeptic critique pass^k overstated 2026")
- discovered_via: search, then citation to companion GitHub repo (nv78/Research-CodeBench), read directly
- doi_or_arxiv_id: arXiv:2608.14711
- version: not confirmed
- published_at: date reported as 2026-08 (not independently confirmed; arxiv.org itself blocked)
- retrieved_at: 2026-09-29
- source_type: paper (+ companion GitHub repo)
- access_scope: abstract not read directly (arxiv.org and arxiv.org/html both EGRESS_BLOCKED this run); companion GitHub repo README (https://github.com/nv78/Research-CodeBench) read directly and in full.
- sections_read: repo README only (methodological error, corrected metric, headline numbers, security-adjusted variant)
- topics: agent evaluation methodology, reliability metrics, benchmark correctness

## Claims from this source
- C-0024: Some agentic-code-generation benchmarks misapply the pass@k estimator by substituting, into its `n` and `c` variables, the number of unit tests inside one submission and the number of tests passed — rather than the number of *independent rollout attempts* and the number of rollouts that fully succeed. The repo states plainly: "Unit tests inside one submission are not independent attempts — they are correlated sub-results of a single run." The corrected metric, **reliability@k**, uses `n` = independent rollout attempts, `c` = rollouts where all tests pass (binary, full-task success). On a synthetic multi-rollout benchmark, this correction collapsed a broken pass@5 of approximately 0.96-0.97 down to a reliability@5 of approximately 0.00-0.12. On 5 real SWE-bench tasks: mean hidden-test pass rate 0.80 vs strict (full-task) resolve rate 0.20 — a 4x inflation. A further "security-adjusted reliability@k" counts only rollouts that are both correct and free of high-severity security issues; in one experiment (240 rollouts), a GPT-4o Codex agent produced 24 insecure rollouts versus 4-5 for competing agents.
  - locator: GitHub README, directly quoted sections (Methodological Error, Reported Score Inflation, Security-Adjusted Reliability@k)
  - evidence_label: bounded empirical (repo README read directly; the underlying arXiv paper itself not opened, so methodology beyond what the README states is unconfirmed)
  - limitations: the repo is a companion artifact, not verified here as first-party to the exact arXiv paper title (title match found via search, not cross-checked line-by-line); "synthetic multi-rollout benchmark" figures (0.96-0.97 -> 0.00-0.12) are an illustrative worst case per the README, not necessarily representative of all benchmarks; author identities and affiliation not independently confirmed this run.
  - relationship to existing claims: **a genuine methodological caution on C-0008's pass@k/pass^k vocabulary** (used in the 2026-W40 brief and learning/tutor.md) — not a contradiction of the reliability thesis (T-01) itself, but a demonstration that even the metric meant to *measure* reliability is, in some existing benchmark implementations, computed in a way that badly overstates it. This is the deliberate 20%-budget "evidence that could contradict/complicate what we believe" slice for this run, and it complicated rather than refuted: it strengthens T-01 (the true reliability gap is likely worse than reported, not better) while flagging a real implementation trap for any pass^k-style feature LayerLens might build (F-0001/I-0001).

## LayerLens relevance
- open question(s) touched: #5 (reliability vs one lucky pass) — directly. If LayerLens ships a pass^k-style readout (F-0001), this is a concrete warning: the "k attempts" must be genuinely independent rollouts of the *whole task*, not sub-results (e.g. per-tool-call or per-subtask checks) dressed up as attempts.
- Action: add a build-time caution to F-0001/I-0001's hypothesis text, not a new feature row.
