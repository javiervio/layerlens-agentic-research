# DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback

- authors_or_org: not independently confirmed this run (search-summary only; see limitations)
- canonical_url: https://arxiv.org/abs/2605.22781
- discovered_url: WebSearch, following up on Planarian (2609.35366) to check for a second independent lifecycle-infra source
- discovered_via: search
- doi_or_arxiv_id: arXiv:2605.22781
- version: v1
- published_at: date reported as 2026-05 (not independently confirmed)
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: incomplete access — arxiv.org (abs and html) both EGRESS_BLOCKED this run; no reachable GitHub mirror attempted/found. Search-summary only.
- sections_read: none directly; WebSearch summary only
- topics: environment lifecycle (checkpoint/rollback), sandbox infrastructure

## Claims from this source
- Reported (NOT independently confirmed, incomplete access): DeltaBox proposes an OS-level abstraction ("DeltaState") with two mechanisms — DeltaFS (change-based filesystem checkpoint/rollback via layered file states) and DeltaCR (change-based process-state checkpoint/rollback via incremental dumps) — motivated by the observation that consecutive AI-agent checkpoints are highly similar, so only the delta needs duplicating rather than the full state. Reportedly achieves millisecond-level checkpoint/rollback (14ms / 5ms) on SWE-bench and RL micro-benchmarks, versus hundreds of milliseconds to seconds for full-state duplication.
  - locator: WebSearch summary only — no claim ID assigned; not promoted to knowledge/claims.md per PROTOCOL.md (a search snippet only justifies discovery, never a claim on its own).
  - evidence_label: incomplete access.
  - limitations: not independently read; numbers and mechanism description are secondhand.
  - relationship to existing claims: if confirmed by a direct read, this would be a fourth independent source (alongside DSec, Planarian, Counterfactual Rollout Replay) for the environment-lifecycle/checkpoint convergence pattern (T-06). Recorded here for traceability and as a pending item, not used to justify any claim or idea promotion this run.

## LayerLens relevance
- open question(s) touched: general (environment lifecycle), adjacent to #3 (deterministic replayability).
- Pending for a future run: attempt a direct read (arxiv.org retry, or search for a companion repo) to decide whether this becomes a real claim.
