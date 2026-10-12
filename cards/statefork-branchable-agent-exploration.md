# StateFork: Branchable Infrastructure for Agent Exploration

- authors_or_org: Jiakai Xu, Tianle Zhou, Georgios Liargkovas, Danielle Gillai, Ruizhe Fu, Patrick Shen et al.
- canonical_url: https://arxiv.org/abs/2609.38648v1
- discovered_url: inbox/arxiv/LATEST.md (2026-W41 harvest, cs.OS)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2609.38648v1
- version: v1
- published_at: 2026-09-29
- retrieved_at: 2026-10-12
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the harvested inbox; arxiv.org itself not reachable this run)
- sections_read: abstract
- topics: environment lifecycle, checkpoint/branch, terminal agents, exploration search

## Claims from this source
- C-0040: StateFork is a control plane separating exploration policy from physical state materialization for terminal-using agents (sessions, commands, snapshots, restores, cleanup over multiple execution substrates); its Waypoint substrate combines filesystem layering, process checkpointing, and a persistent terminal session. On Terminal-Bench, branch-based exploration beats pass@20 at the same visited-node budget, and Waypoint gets 26% higher task accuracy than other execution substrates while exploring up to 70% faster.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; single benchmark (Terminal-Bench); "other execution substrates" not named in the abstract.
  - relationship to existing claims: eleventh independent family for thesis T-06 (environment lifecycle convergence). Distinct conceptual contribution: names "observation-equivalent" restoration as the correctness condition for branching (future actions must produce the same observations after restore), a sharper formal framing than most of T-06's prior mechanism-exists data points.

## LayerLens relevance
- open question(s) touched: #3 (deterministic replayability), #7 (recovery), #8 (living-graph/exploration). "Observation-equivalent" is a useful, precise vocabulary word for what LayerLens's own checkpoint/branch feature (I-0007) would need to guarantee before it could be trusted.
