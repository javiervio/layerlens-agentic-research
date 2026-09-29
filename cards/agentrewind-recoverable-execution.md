# AgentRewind: Recoverable Execution for Long-Horizon LLM Agents

- authors_or_org: Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang
- canonical_url: https://arxiv.org/abs/2608.14380
- discovered_url: WebSearch (team-rotation/T-06 follow-up search on checkpoint/rollback cluster)
- discovered_via: search
- doi_or_arxiv_id: arXiv:2608.14380
- version: v1
- published_at: 2026-08-14
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: incomplete access (arxiv.org and mirrors EGRESS_BLOCKED this run; no independently-read primary text found; description assembled from multiple WebSearch summaries of the same paper, treated as secondary)
- sections_read: none directly; search-summary only
- topics: environment lifecycle, checkpoint/rollback, agent runtime recovery, long-horizon agents

## Claims from this source
- C-0025: AgentRewind is a runtime recovery framework that records aligned checkpoints of both an agent's context and its "controlled environment" (the workspace directory tree, tracked via file-level changes), letting an agent roll back to an earlier checkpoint and resume with information from the failed attempt after an error, rather than restarting from scratch. Introduces MettleBench, a benchmark of real-world, multi-requirement long-horizon engineering tasks (checklist-progress scored, not single pass/fail). Reported to improve task success rate and checklist progress across multiple models, execution strategies, and agent harnesses versus compared baselines.
  - locator: WebSearch summaries of the abstract/paper description (arxiv.org, arxiv.org/html, and secondary aggregator pages), consistent across sources.
  - evidence_label: incomplete access (secondary summary only; no primary text opened).
  - limitations: no primary text read; specific benchmark numbers (success-rate deltas) not captured in what was retrieved; single paper.
  - relationship to existing claims: fourth independent family for thesis T-06 (environment-state lifecycle convergence), alongside C-0012 (DSec), C-0020 (Planarian), C-0023 (Counterfactual Rollout Replay) — this one specifically targets agent-runtime *recovery* (closest yet to a product-facing use case for I-0007).

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery), #3 (deterministic replayability).
