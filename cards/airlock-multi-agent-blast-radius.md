# Airlock: Bounding the Multi-Agent Blast Radius via Selective Online Containment

- authors_or_org: Zhonghao Zhan, Javad Forough, Yefan Zhang, Krinos Li, Xiao Ma, Hamed Haddadi
- canonical_url: https://arxiv.org/abs/2611.06727
- discovered_url: inbox/arxiv/2026-W46.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.06727v1
- version: v1
- published_at: 2026-11-04
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: multi-agent containment, provenance, blast radius, lifecycle/rollback

## Claims from this source
- C-0132: When multi-agent systems act on the external world, one agent's faulty output can spread to other tasks before detection, creating a system-wide "blast radius." Existing multi-agent controls either cancel only the faulty source (missing downstream consumers) or halt/roll back the entire workflow (discarding healthy work). Airlock is a multi-agent runtime/guardrail with a tree-structured runtime (EdgeCitadel) that narrows permissions vertically from parent to child agents, plus an append-only provenance DAG recording cross-agent data consumption; on an alert it traces forward to isolate tainted executions/pending actions and backward to narrow root causes, with a default full-quarantine tier and an "assured optimized cut" tier (fence-then-prune) that minimizes collateral disruption under a deadline. Across 1,832 testbed runs, 161 physical smart-home runs, and 24,266 simulation records, Airlock blocked all post-alert faulty actuations with zero post-convergence leaks; native A2A/LangGraph controls contained at most 33.3% of faults or retained at most 16% of work without redo, while Airlock retained +68 to +96 percentage points more healthy work (its optimized cut tier retaining +46pp more than full quarantine under dense spread).
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; comparison baselines are "native controls in A2A and LangGraph," not every possible containment design; code released (github.com/EdgeCitadelTeam/EdgeCitadel) but not independently run this week.
  - relationship to existing claims: strengthens T-02 (trust-wall/containment cluster) and T-06/I-0007 (environment lifecycle: selective rollback that preserves healthy work is a sharper, more surgical version of the "quarantine vs. undo everything" tradeoff ACRFence/Recoverability-as-Primitive already raise) and T-08 (multi-agent blast-radius containment specifically).

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — selective containment that keeps healthy work is directly relevant to any future checkpoint/branch/retry feature, I-0007); #13 (multi-agent scope). A concrete reference design for "undo only what needs undoing" rather than all-or-nothing rollback.
