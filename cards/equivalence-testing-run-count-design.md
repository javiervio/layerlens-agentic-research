# Equivalence testing and run-count design for stochastic machine-learning experiments

- authors_or_org: Dmytro Knopov, Nadiya Shvai
- canonical_url: https://arxiv.org/abs/2610.23700v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.LG)
- discovered_via: feed
- doi_or_arxiv_id: 2610.23700v1
- version: v1
- published_at: 2026-10-16
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: run-count design, statistical equivalence testing, T-01/I-0001

## Claims from this source
- C-0070: Claims that two ML methods "perform equally well" often rest on a non-significant difference between two or three runs, which is underpowered, not evidence of equivalence. The authors develop a protocol (two one-sided tests, TOST, equivalent to a confidence interval inside a pre-specified margin) built on a two-level (seed x item) variance model separating between-run dispersion from item-level noise, plus a closed-form formula converting a chosen equivalence margin and target power into the number of runs per method needed. On a 270-cell simulation grid and non-Gaussian seed distributions, the formula held within its design range, from five runs per method upward. Re-analyzing four published runs of a joint energy-based model, certifying equivalence at two runs per method succeeds with only about 3% probability given the variance actually observed in those runs, while certifying a 0.01 AUROC margin at 80% power needs twelve runs even under exact equality. A thousand-seed CIFAR-10 zoo and MultiBERTs check the formula against real seed-variability laws (within 0.05 in range) and resolve comparisons that two or three runs leave undecided. A two-stage design (small pilot, then apply the formula using an upper confidence bound on the pilot's variance, not its point estimate) substantially reduces undersizing.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly) — a methodological/statistical contribution, not an agent-benchmark finding per se, but directly actionable for one.
  - limitations: abstract only; developed and validated on ML training-method comparisons (AUROC-style per-run metrics), not agent task success specifically; the field's worked examples are a JEM and CIFAR-10/MultiBERTs zoos, not agentic-environment benchmarks — the formula's applicability to agent pass/fail metrics is a reasonable but unconfirmed extension.
  - relationship to existing claims: directly strengthens T-01 and gives I-0001 (reliability-aware run counts / pass^k readout) something it previously lacked: a concrete, principled formula for "how many runs are enough," rather than just evidence that too-few runs mislead (C-0019, C-0013, C-0058). This is a candidate mechanism LayerLens could use to recommend k, not just display variance after the fact.

## LayerLens relevance
- open question(s) touched: #5 (what "repeat a run" means — directly on point: this gives a formula, not just a caution), #1 (comparability — equivalence testing is exactly "are these two runs/configs comparable," formalized).
