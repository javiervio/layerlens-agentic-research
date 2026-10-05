# DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback

- authors_or_org: not independently confirmed this run (search-summary only; see limitations)
- canonical_url: https://arxiv.org/abs/2605.22781
- discovered_url: WebSearch, following up on Planarian (2609.35366) to check for a second independent lifecycle-infra source
- discovered_via: search
- doi_or_arxiv_id: arXiv:2605.22781
- version: v1
- published_at: date reported as 2026-05 (not independently confirmed)
- retrieved_at: 2026-09-29 (first surfaced); re-confirmed with richer, consistent detail 2026-10-05
- source_type: paper
- access_scope: incomplete access — arxiv.org (abs and html) both EGRESS_BLOCKED both runs; no reachable GitHub mirror found either run. Search-summary only, but now consistent across three independent WebSearch passes (two runs) on the specific mechanism names and numbers.
- sections_read: none directly; WebSearch summaries only
- topics: environment lifecycle (checkpoint/rollback), sandbox infrastructure

## Claims from this source
- C-0036: DeltaBox proposes an OS-level abstraction ("DeltaState") treating the filesystem and process memory as a transactional, change-based state pair, with two mechanisms: DeltaFS (change-based filesystem checkpoint/rollback — organizes file state into layers, freezes the writable layer and inserts a new one at checkpoint time) and DeltaCR (change-based process-state checkpoint/rollback via incremental dumps, accelerating rollback by `fork()`-ing directly from a frozen template process rather than running a full restore pipeline). Motivated by the observation that consecutive AI-agent checkpoints are highly similar, so only the delta needs capturing. Reportedly achieves millisecond-level checkpoint/rollback (14ms / 5ms respectively) on SWE-bench and RL micro-benchmarks, letting agents explore substantially more nodes under a fixed time budget, versus hundreds of milliseconds to seconds for full-state duplication.
  - locator: WebSearch summaries, consistent across three independent queries spanning two run dates on the mechanism names (DeltaState/DeltaFS/DeltaCR) and the 14ms/5ms figures.
  - evidence_label: incomplete access (promoted from an unassigned pending item to a numbered claim this run, since the mechanism description and numbers have now been stable and consistent across multiple independent search passes, not because primary text was read).
  - limitations: not independently read; numbers and mechanism description remain secondhand; no author/affiliation independently confirmed.
  - relationship to existing claims: **ninth independent family for thesis T-06** (alongside DSec C-0012, Planarian C-0020, CRR C-0023, AgentRewind C-0025, E2B C-0028, ControlScope C-0030, Recoverability-Primitive C-0034, Crab C-0037) — specifically another "local sandbox state" data point (filesystem + process memory), reinforcing that this branch of the cluster is maturing fast and converging on similar change-based/delta techniques independently (DeltaBox's "DeltaState" and Crab's eBPF-based granularity detection solve adjacent problems with different mechanisms).

## LayerLens relevance
- open question(s) touched: general (environment lifecycle), adjacent to #3 (deterministic replayability).
- Still pending for a future run: a direct read (arxiv.org retry, or a newly-published companion repo) to move past incomplete access.
