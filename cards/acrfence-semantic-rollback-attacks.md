# ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore

- authors_or_org: Yusheng Zheng, Yiwei Yang, Wei Zhang, Andi Quinn — UC Santa Cruz and University of Connecticut (per secondary coverage; not independently confirmed against the paper itself).
- canonical_url: https://arxiv.org/abs/2603.20625
- discovered_url: WebSearch ("ACRFence semantic rollback attack agent checkpoint restore arxiv"), following up the T-06 counter-evidence cluster flagged pending in the 2026-09-29 run logs.
- discovered_via: search.
- doi_or_arxiv_id: arXiv:2603.20625
- version: v1
- published_at: 2026-05 (per a dated secondary source, eunomia.dev blog dated 2026-05-21; not independently confirmed)
- retrieved_at: 2026-10-05
- source_type: paper
- access_scope: incomplete access — arxiv.org (abs and html) EGRESS_BLOCKED this run; eunomia.dev (a blog covering it) also EGRESS_BLOCKED (newly confirmed this run); no GitHub companion repo found. Record built from two independent WebSearch passes whose summaries agree on specifics (attack names, affected frameworks, PoC details), not from primary text.
- sections_read: none directly; WebSearch summaries only.
- topics: checkpoint/restore security, environment lifecycle, agent-tool interaction

## Claims from this source
- C-0038: ACRFence names and demonstrates "semantic rollback attacks": LLM agent checkpoint-restore mechanisms assume a retried external tool call will be identical to the original, but LLM agents re-synthesize subtly different requests after a restore, so a target service treats the re-generated request as new rather than a legitimate retry. Two attack classes: **Action Replay** (an irreversible action already executed before the checkpoint; after restore, the LLM generates a fresh request id, so the external service commits the action again rather than recognizing a repeat) and **Authority Resurrection** (a one-time approval token is consumed, then a rewind-to-checkpoint brings the agent's local state back to a point before the token was marked consumed, so it appears valid again). Proof-of-concept experiments with Claude Code CLI and Qwen3-32B reportedly confirmed duplicate commits under checkpoint/restore; the underlying assumption failure is described as affecting LangGraph, CrewAI, Google ADK, AutoGen, and other checkpoint-restore-offering frameworks generally, not one implementation. Proposed mitigation (ACRFence) is a framework-agnostic proxy (deployable as, e.g., an MCP proxy) that records irreversible tool effects at the tool boundary and enforces "replay-or-fork" semantics on restoration (i.e., either genuinely replay the exact original effect or fork into a new, clearly-distinct branch, never silently re-execute as if nothing happened).
  - locator: WebSearch summaries (two independent queries, consistent on attack names, PoC frameworks, and mitigation mechanism).
  - evidence_label: incomplete access (no primary text; PoC scope — specific models/frameworks tested — not independently verified beyond what two search passes agree on).
  - limitations: no quantitative attack-success rates or mitigation-overhead numbers captured; author affiliation not independently confirmed; cannot confirm whether the "LangGraph, CrewAI, Google ADK, AutoGen" affected-frameworks list reflects actual tested exploits in each or a general applicability argument.
  - relationship to existing claims: **sharpens, rather than merely echoes, C-0026 ("Safe to Resume?")** — C-0026 argued conceptually that correct rollback does not imply secure recovery; ACRFence supplies two named, concrete attack mechanisms with a stated proof-of-concept on real tooling (Claude Code CLI + Qwen3-32B), moving the risk from "an unresolved concern" to "a demonstrated exploit class," the same maturation pattern BenchJack/HackDetect (C-0001/C-0006) showed for benchmark exploitability. Also the sharpest-yet evidence that Crab's (C-0037, this same run) explicit exclusion of "external side effects" from its recovery guarantee is not a minor footnote but exactly the attack surface this paper targets.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery) directly; #3 (deterministic replayability — a "replay" that silently re-executes an external effect is not actually a safe replay).
- This is the single most concrete, actionable piece of evidence yet for I-0007/F-0007's build caution: if LayerLens ever ships checkpoint/branch over its own remote system types (Salesforce, Stripe, Linear, Gmail, SEC EDGAR), a token/credential or a payment/write action is exactly the kind of irreversible external effect ACRFence names — "replay-or-fork" semantics (never silently re-execute) is a concrete design pattern to evaluate against our own system-type writes, not just an abstract caution.
