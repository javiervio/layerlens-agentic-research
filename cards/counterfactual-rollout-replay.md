# Counterfactual Rollout Replay: Forkable Environments as Free Process Rewards for Software Engineering Agents

- authors_or_org: Yuanhao Li, Hongbo Wang, Xuhong Chen, Yiming Cao, Xunzhu Tang
- canonical_url: https://arxiv.org/abs/2609.33875
- discovered_url: inbox/arxiv/LATEST.md (2026-W40 harvest)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2609.33875
- version: v1
- published_at: 2026-09-27
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: abstract only (verbatim, directly read via inbox harvester; arxiv.org blocked this run)
- sections_read: abstract
- topics: environment lifecycle (fork/restore), RL training infrastructure

## Claims from this source
- C-0023: Counterfactual Rollout Replay (CRR) uses "forkable executable environments" — restore a saved state, sample an alternative action, roll the branch forward — to get step-level return contrasts for training, without human process labels or a learned reward model. With a 14B policy, CRR improved pass@1 on SWE-bench Verified/Live/rebench; on SWE-bench Verified an equal-wall-clock comparison gave 41.7% vs 36.7% for extended outcome-only GRPO (a 5.0-point gain, fork overhead included). Authors' own stated limit: only applies where state restoration is affordable and reliable; stochastic continuations and expensive/imperfect replay remain limitations.
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; training-time use case (RL), not directly a product/UX finding; single source for this specific application.
  - relationship to existing claims: a third independent instance of the fork/restore/branch environment-state primitive (alongside C-0012 DSec and C-0020 Planarian), this time from an RL-training angle rather than infra or agent-runtime — further corroborates thesis promotion (see T-06 in changelog).

## LayerLens relevance
- open question(s) touched: general (environment lifecycle); adjacent to open question #5 (variation across attempts) since counterfactual branching is itself a structured way to probe run-to-run variance at a specific decision point, not just the whole trajectory.
- Feeds I-0007 (environment lifecycle legibility + checkpoint/branch a run) as a third convergent source, from yet another distinct angle (training reward shaping) than DSec (infra scale) or Planarian (agent runtime/UX).
