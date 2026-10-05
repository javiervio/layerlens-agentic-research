# Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes

- authors_or_org: Tianyuan Wu, Chaokun Chang, Lunxi Cao, Wei Gao, Wei Wang (2026); affiliated with the "open-agent-infra" project.
- canonical_url: https://arxiv.org/abs/2604.28138
- discovered_url: WebSearch ("Crab semantics-aware checkpoint restore agent sandbox github terminal-bench"), following up the T-06 cluster's pending items.
- discovered_via: search, then GitHub (companion repo).
- doi_or_arxiv_id: arXiv:2604.28138
- version: v1 (paper); repo at HEAD, 2026
- published_at: 2026 (exact date not independently confirmed; arxiv.org itself blocked)
- retrieved_at: 2026-10-05
- source_type: paper (read via companion repo)
- access_scope: full text — README read directly and in full (github.com/ChaokunChang/crab is reachable; arxiv.org itself is EGRESS_BLOCKED, so the paper's own text was not read, only the repo's description of it, which quotes the same reported numbers)
- sections_read: full README (problem framing, mechanism, evaluation results, limitations, license/attribution)
- topics: environment lifecycle, checkpoint/restore, sandbox infrastructure, agent-OS semantic gap

## Claims from this source
- C-0037: Crab is a semantics-aware checkpoint/restore runtime for agent sandboxes that closes an "agent-OS semantic gap" (the agent framework sees model turns and tool calls but not their OS effects; the OS sees process/file activity but not which agent turn it belongs to or whether it matters for recovery). A three-layer system — Coordinator (turn-boundary detection, async checkpointing during LLM wait time), Inspector (eBPF-based observer picking checkpoint granularity: none / filesystem-only / process-only / full), C/R Engine (runc + CRIU + ZFS backends) — observes OS-visible effects per turn rather than trusting the agent's own account of what changed.
  - locator: README sections "Problem", "Core Mechanism", "Evaluation".
  - evidence_label: bounded empirical (companion repo read directly; underlying arXiv text itself not read).
  - limitations: v0 preview, Ubuntu 24.04/26.04 on x86-64 only; requires a root-owned single-user daemon; host bind mounts excluded from the snapshot boundary; **explicitly cannot undo external side effects (GitHub pushes, API calls, database writes)** — this is a stated, not incidental, scope limit; rollback is manual only in this release (an automatic agent-facing rollback tool is described as planned, not shipped).
  - relationship to existing claims: **eighth independent family for thesis T-06** (environment lifecycle convergence), and so far the strongest quantitatively (directly read, concrete numbers, real agents/benchmarks) of the "local sandbox state" branch of that cluster. Its own stated limitation (cannot undo external side effects) is an unprompted, first-party confirmation of exactly the gap "Safe to Resume?" (C-0026) and ACRFence (C-0038, this same run) argue is unresolved — Crab solves the local-state recovery problem well and explicitly declines to touch the remote/external-state problem.
- Reported results (quoted from the README, which states these come from the companion arXiv paper 2604.28138): evaluated using Claude Code, iFlow CLI, and SWE-agent against Terminal-Bench and SWE-Bench workloads. Recovery correctness improved from 8% (chat-only baseline) / 28-42% (chat+filesystem baseline) to 100% (Crab) on Terminal-Bench. 87% of agent turns were classified as needing no checkpoint at all (eliminating that recovery work entirely). Execution overhead stayed within 1.9% of a fault-free, checkpoint-free baseline under dense co-location. Exposing rollback as an agent-callable tool gave a 29% wall-clock reduction and 36% rollback-token reduction; branched RL rollouts reduced redundant tokens 40.0-64.2% via intermediate-state reuse.
  - locator: README "Evaluation Scope" and "Reported Performance Metrics".
  - evidence_label: bounded empirical (first-party repo, numbers stated as from the paper; the underlying paper's tables themselves were not independently read).
  - limitations: single project's self-reported benchmarks; "100%" recovery correctness is specifically against the baselines compared (chat-only, chat+filesystem), not an absolute claim of flawless recovery under all conditions; RL-rollout and rollback-as-tool numbers come from presumably different experimental setups than the headline Terminal-Bench figure, not all directly comparable to one another.
  - relationship to existing claims: strengthens T-06 (same cluster as C-0012 DSec, C-0020 Planarian, C-0023 CRR, C-0025 AgentRewind, C-0028 E2B, C-0030 ControlScope, C-0034 Recoverability-Primitive).

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery), #3 (deterministic replayability as a surface).
- Directly sharpens I-0007/F-0007's hypothesis: the "local sandbox state" part of environment lifecycle legibility (what changed, when to checkpoint, how to roll back) is now a demonstrated, quantified, near-solved engineering problem across multiple independent teams (Crab, DeltaBox, DSec). The part that remains hard, unsolved, and exactly LayerLens's own shape (Salesforce, Linear, SEC EDGAR, Stripe, Gmail — all remote, external-system state) is the part Crab explicitly excludes and ACRFence (C-0038) shows is actively exploitable.
