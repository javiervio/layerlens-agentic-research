# Pdb or Not to Be: Comparing Debugging Interfaces With Pass_X@k

- authors_or_org: Ryan Magnuson, Ellie Kitanidis, Ariel Lee
- canonical_url: https://arxiv.org/abs/2611.08666
- discovered_url: inbox/arxiv/2026-W46.md (cs.SE)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.08666v1
- version: v1
- published_at: 2026-11-05
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: pass@k methodology, run-to-run variance, tool diversity, debugging interfaces

## Claims from this source
- C-0138: Comparing a debugger-only coding agent against a bash-only agent on all 500 SWE-bench Verified instances (two models, three independent runs per architecture x model), the authors introduce pass_X@k, a cross-agent pass@k that gives an unbiased estimator of the probability that at least one of k *different agents* succeeds (as opposed to k repeated attempts by one agent). Although the bash and debugger agents solve partially disjoint subsets of the benchmark in any single pair of runs, pass_X@2 reveals this is largely due to run-to-run variance rather than genuine tool complementarity: across both models, two bash rollouts outperform the combination of one bash and one debugger rollout.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; two models, one benchmark (SWE-bench Verified); three runs per configuration.
  - relationship to existing claims: a build caution and a methodological extension directly relevant to I-0001's own pass^k vocabulary: this paper shows that apparent "complementarity" between two different tools/architectures can itself be a run-to-run-variance illusion unless disentangled with a cross-agent estimator — a sharper, generalized version of the caution C-0024 (reliability@k vs misapplied pass@k) already raised. Strengthens T-01.

## LayerLens relevance
- open question(s) touched: #5 (reliability vs one lucky pass) — directly relevant if LayerLens's own pass^k-style readout (I-0001/F-0001) is ever extended to compare two different agents/configurations rather than one agent's repeated attempts: the same run-to-run-variance confound applies and needs a pass_X@k-style estimator, not a naive subset-union comparison.
