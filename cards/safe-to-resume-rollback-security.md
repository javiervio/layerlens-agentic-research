# Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback

- authors_or_org: Guanlong Wu, Dahui Li, Ke Jiang, Jianyu Niu, Cong Wang, Yinqian Zhang
- canonical_url: https://arxiv.org/abs/2608.29381
- discovered_url: WebSearch (following up the DeltaBox/T-06 checkpoint-rollback cluster)
- discovered_via: search
- doi_or_arxiv_id: arXiv:2608.29381
- version: v1
- published_at: 2026-08-29
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: incomplete access (arxiv.org EGRESS_BLOCKED this run; description assembled from consistent WebSearch summaries, treated as secondary, not primary text)
- sections_read: none directly; search-summary only
- topics: environment lifecycle, checkpoint/rollback security, agent runtime recovery

## Claims from this source
- C-0026: The paper presents what it calls the first systematic security study of checkpoint/rollback (C/R) in agent systems. Core finding: "correct rollback does not imply secure recovery" — a checkpoint can be faithfully restored (state-correct) yet resume an execution whose states, assumptions, and external effects never coexisted in any valid history, because the world outside the sandbox (other services, other agents, real external effects) kept moving while the checkpoint was frozen. Introduces "execution continuity" as a named security requirement distinct from state-correctness, and characterizes a design space of existing C/R mechanisms and their recovery boundaries/state dependencies.
  - locator: WebSearch summaries of the abstract (arxiv.org/abs, /html, /pdf all listed but blocked directly).
  - evidence_label: incomplete access (secondary summary only; no primary text, no concrete attack numbers or case studies confirmed).
  - limitations: no primary text read; no quantitative results captured (e.g., how many systems tested, how often continuity breaks in practice); single paper, and part of an apparently active sub-cluster (also found: ACRFence, "When Can Agents Safely Checkpoint, Fork, Restore, and Merge?", "Recoverability as a System Primitive" — none of these individually confirmed or read this run, recorded here only for future-run follow-up).
  - relationship to existing claims: **counter-evidence / risk complication to thesis T-06** (environment-lifecycle checkpoint/rollback/fork convergence, C-0012/C-0020/C-0023/C-0025). Where those sources treat checkpoint/rollback as a maturing, near-commodity capability, this paper argues the security dimension of that capability is largely unexamined and can silently fail even when the mechanism works "correctly" in the narrow state-restoration sense.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — a checkpoint/branch feature is exactly the kind of thing this paper cautions about), #3 (deterministic replayability — replay must also preserve *validity* of the history, not just state).
- Direct build caution for I-0007/F-0007: if LayerLens ever ships a checkpoint/branch affordance on an environment with remote system-type state (Salesforce, Linear, Stripe, etc.), "did the restore actually happen" is necessary but not sufficient — whether the resumed execution's assumptions about the outside world (e.g., a Stripe webhook that fired during the frozen window) still hold needs its own design answer, not just correct state duplication.
