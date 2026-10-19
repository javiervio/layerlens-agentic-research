# Environments experience: ideas and hypotheses backlog

The durable place where research turns into product ideas for the LayerLens Environments experience. Unlike a weekly brief (ephemeral) or a competitive entry (about someone else), an idea here **accumulates evidence over time** and moves up a maturity ladder until Javier decides what to build.

The system proposes and gathers evidence. It never builds, files tickets, or decides. Javier decides, and promotes ready ideas to Linear/Figma himself.

Ideas with a product-shaped hypothesis also get a row in `features/matrix.csv` (F-xxxx), the ranked sheet where Impact, Effort, evidence-derived Confidence, and Priority live. This file is the deep-traceability layer behind that sheet.

## Maturity ladder

- **L0 Nascent**: one source, or a bare idea. Interesting, not actionable.
- **L1 Developing**: multiple independent sources, OR one strong source plus a clear user outcome and a validation plan.
- **L2 Ready to spec**: a real problem, a named persona, a user outcome stated as "better for whom, by how much," at least one open design question it answers, and a concrete way to validate. This is where Javier promotes it out of the repo.
- **L3 Decided**: build / park / drop, with Javier's reason and date.

Rule: **a single mention never reaches L2.** One paper is a lead, not a mandate.

## How an idea earns its place (schema)

Each entry records: the problem/pain point, the persona, the user outcome (time to diagnose, comprehension, correction, recovery, reliability, effort, cost), the linked open design question(s) from `LAYERLENS_CONTEXT.md`, accumulating evidence (claim IDs + links), a testable hypothesis, how to validate, and maturity + last update.

## Prioritization view (maturity first, then evidence count)

| ID | Idea | Open Q | Maturity | Evidence | Primary user outcome |
|---|---|---|---|---|---|
| I-0003 | Attribution as a location, every attribution a door | #2 | L1 | 8 | Faster, correct failure diagnosis |
| I-0004 | Comparability guardrails + always show a tradeoff axis | #1, #9 | L1 | 3 | No false comparisons; no accuracy-only ranking |
| I-0001 | Reliability-aware run counts + a pass^k readout | #5 | L1 (evidence-complete, blocked only on product check) | 5 | Capability vs reliability made visible; runs spent where they matter |
| I-0007 | Environment lifecycle legibility + checkpoint/branch a run | #7 | L1 | 12 | Understand and control environment state and lifetime |
| I-0002 | "Why is this not solvable" feasibility explanation | #4 | L0 | 1 | Authors design solvable tasks faster |
| I-0005 | Flag same-family judge/agent pairings | #2 | L1 | 2 | Judge verdicts trusted appropriately |
| I-0006 | Confirmations that name the specific consequence | #7 | L0 | 2 | Approve with understanding, not blindly |
| I-0009 | Agent-actionable error/recovery guidance in tool surfaces | #2, #7 | L0 | 1 | Agents recover from real failures instead of following misleading human-oriented steps |
| I-0010 | Confidence-aware judge verdicts, with escalation on low confidence | #2 | L1 | 6 | Judge verdicts trusted appropriately, without a false reassurance from mere re-run consistency |
| I-0011 | Detect and surface stale environment observations mid-task | #2, #7 | L0 | 1 | Agents (and users) don't act on outdated facts the environment has since changed |

---

## I-0001: Reliability-aware run counts and a pass^k readout

- **Problem / pain point**: A single pass or accuracy number hides whether an agent behaves the same way twice. A user can ship an agent that "passed" once and then fails unpredictably in production.
- **Persona**: Evan (evaluation owner), Taylor (accountable lead, shares the readiness report).
- **User outcome**: users can separate capability (can it ever succeed) from reliability (does it succeed every time), and spend runs where reliability matters instead of running everything once or everything many times.
- **Open design question(s)**: #5 (reliability versus one lucky pass), with #1/#9 (comparison).
- **Evidence** (accumulating):
  - C-0008, "Towards a Science of AI Agent Reliability" (Princeton, ICML 2026): pass@k vs pass^k, 12 reliability metrics across 4 dimensions, finding minimal reliability gains despite capability gains. https://arxiv.org/abs/2602.16666
  - C-0013, "Same Winners, Different Success Rates": ordinal/set-agreement benchmarks provably hide reliability. https://arxiv.org/abs/2609.34215
  - C-0019, "Identical Runs, Different Results": 584 real coding-agent runs — run-to-run variance (median 0.0107 AUC) exceeds agent-to-agent difference (mean 0.0095 AUC); three-run comparisons rank pairings unreliably; a third, independent, real-world evidence family. https://arxiv.org/abs/2609.33812
  - C-0053, ThinkingBox (incomplete access, dates/numbers disputed across sources): reportedly a ~40-point gap between pass@1 (65.36%) and pass^20 (25.25%) on a 507-task stateful business-workflow benchmark — a vivid number if confirmed, pending a primary-source check. (not yet confirmed)
- **Hypothesis** (Javier's, refined): LayerLens holds the task, the grader type, and, because minting is deterministic and free, can cheaply observe run-to-run variance. So it can (a) surface **pass^k as a first-class reliability readout** beside accuracy, and (b) **recommend how many attempts k** a task warrants, single-shot where an answer-key grader on a stable task suffices, multiple where variance is detected or reliability is the question. The adaptive form ("reliability not yet established, run N more" vs "stable across k, stop") is stronger than a static task-type lookup, because variance is empirical.
- **Build caution (new, 2026-09-29)**: C-0024 ("Beyond Pass@k") shows some benchmarks compute pass@k wrong by conflating unit-test sub-results with independent rollouts, inflating scores by up to ~0.9 absolute in an illustrative case. Whatever "k attempts" LayerLens counts for a pass^k readout must be genuinely independent full-task rollouts, not sub-task or per-tool-call checks. https://arxiv.org/abs/2608.14711 (via companion repo, github.com/nv78/Research-CodeBench)
- **Differentiator angle**: re-running is near-free here (deterministic free minting), so k-repeat reliability testing is economically viable in a way a paid or stateful competitor setup may not be. This makes the feature moat-aligned, not generic.
- **How to validate**: (1) the design exercise, sketch the readout (2026-W40 brief); (2) product check, do Runs/Insights show reliability by default today (open Q#5); (3) user test, show two runs with equal accuracy but different pass^k and see whether users pick the reliable one and can explain why.
- **Maturity**: L1 developing — now backed by three confirmed independent evidence families plus a clear outcome and validation plan, plus one pending (ThinkingBox, unconfirmed). **Evidence-complete**: the only thing standing between this and L2 is item (2), the product check, which needs someone with LayerLens product access; this idea should not need further external corroboration to be spec-ready once that check runs.
- **Last update**: 2026-10-12.

## I-0002: "Why is this not solvable" feasibility explanation at task authoring

- **Problem / pain point**: authors cannot easily tell whether a task is solvable, or why not; separately, agents barrel ahead on infeasible tasks and waste budget.
- **Persona**: Devon (agent engineer), Evan (evaluation owner).
- **User outcome**: authors design solvable scenarios faster and understand infeasibility at design time; evaluations stop wasting budget on impossible tasks.
- **Open design question(s)**: #4 (task feasibility).
- **Evidence**:
  - C-0007, FeasiGen (Edinburgh): masking the critical tools a task needs makes it infeasible; nine models detect infeasibility poorly (false-continue up to 73.9%); multi-agent planner-executor best pair 2.6%. https://arxiv.org/abs/2605.28532
- **Hypothesis**: LayerLens knows the environment's tools and the answer key, so it could compute and show whether a task's required tools and records are present, and explain "not solvable because tool X or record Y is missing," which is FeasiGen's critical-tool masking run in reverse.
- **How to validate**: prototype a feasibility check on an existing environment/task; author user test.
- **Maturity**: L0 nascent (one source). To reach L1: a second source on feasibility at authoring time, or a clear outcome + validation plan confirmed with an author.
- **Last update**: 2026-09-29.

## I-0003: Attribution as a location, and every attribution a door

- **Problem / pain point**: users cannot tell whether a failure is the agent's, the environment's, the grader's, or infrastructure. A number alone does not say, and benchmark scores are frequently inflated by exploiting weak isolation.
- **Persona**: all (Devon, Evan, Riley especially).
- **User outcome**: faster and correct diagnosis; verdicts that can be trusted and defended.
- **Open design question(s)**: #2 (failure attribution). Aligns with the v3 direction's "failures light up in place."
- **Evidence**:
  - C-0001, BenchJack: 8/8 audited benchmarks exploitable via weak agent/evaluator isolation and accessible ground truth. https://github.com/benchjack/benchjack
  - C-0006, HackDetect: independent audit, 2,385 traces across 15 benchmarks, 67% and 66.7% exploit rates. https://arxiv.org/abs/2607.22368
  - C-0021, "Maintaining Benchmarks Against Increasingly Capable Agents": distinguishes evidenced reward-hacking from verifier weakness (env-vs-agent attribution, formalized); benchmark integrity is ongoing maintenance, not one-time. https://arxiv.org/abs/2609.34262
  - C-0022, "Failure-Transparent Agents": a distinct attribution category (unsupported post-failure success claims); a structured evidence contract cut false-success from 22.8% to 0.8%, independently validating LayerLens's existing "claims stored beside verdicts, never used as evidence" design. https://arxiv.org/abs/2609.35732
  - C-0039, BenchShield (incomplete access): instruments evaluation infrastructure prospectively to reconstruct the "reward-relevant trajectory" (how authority/information actually moved), rather than auditing after the fact — a structurally different, closer-to-LayerLens's-own-approach confirmation of the same attribution need; 456 human-adjudicated trajectories from 31,000+ public runs. https://arxiv.org/abs/2609.11028
  - C-0042, a 150-production-incident taxonomy (23 failure modes, 5 component-boundary categories) with measured resilience patterns (circuit breakers cut cascade propagation 89%; 3+ patterns cut MTTR 71%) — the first family grounded in real production incidents rather than benchmark/trace audits. https://arxiv.org/abs/2610.02503v1
  - C-0043, a real enterprise deployment: 92.6% of trials passing every final-output check still had an undetected trajectory deviation; dependency attribution cut 6.34 failed checks/run to 2.65 root causes — the most concrete "why trajectory-level attribution matters" number yet, from production rather than a benchmark. https://arxiv.org/abs/2610.01833v1
  - C-0046, "Discriminating Fixture Coverage": a verification suite can pass the standard "kills known-bad, passes known-good" bar and still certify a mutant and miss real defect classes — a caution directly applicable to LayerLens's own graders, not just the agents they grade. https://arxiv.org/abs/2610.02928v1
  - C-0048, Agent-Warden (abstract read directly): a kernel-level eBPF provenance monitor reconstructed a cross-process causal chain absent from the application-layer trace entirely — a literal illustration that trace-only attribution can miss the real cause. https://arxiv.org/abs/2609.38245v1
  - C-0055, Anthropic's own primary-source account of its cybersecurity incidents (directly read): Anthropic publicly revised its own attribution call, from "harness/operational failure" to "model alignment failure (biased reasoning + recklessness)," as more evidence arrived — a real-world case study that attribution is revisable, not a one-time verdict. https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents
  - C-0062, TestSuiteBench (abstract read directly): frontier coding agents generate weak test suites from specifications (mutation scores under 60%) despite the suites looking valid — "agents can build software they cannot verify," directly relevant to LayerLens's own benchmark-generation flows. https://arxiv.org/abs/2610.13065
  - C-0067, MASCope (abstract read directly): recovers communication topology from multi-agent traces without explicit labels and uses it to diagnose coordination failures (chi^2=409.9 topology-failure association) at ~6% the cost of repeated LLM diagnosis — a concrete method for attribution *within* a multi-agent system. https://arxiv.org/abs/2610.10126
- **Hypothesis**: surface attribution as a location on the trace (where it broke) with a routed next action, not a log line, and make the trust wall's guarantees visible so a passing score is legibly not gameable.
- **How to validate**: product check on the current attribution UI (open Q#2); design the trace-location surface; test whether users correctly assign blame faster.
- **Maturity**: L1 developing — now eleven independent corroborating sources plus the core differentiator, including one (C-0022) that validates a choice already shipped in V1, one (C-0039) whose own approach (prospective instrumentation) is the closest external analogue yet to LayerLens's trust wall, two (C-0042, C-0043) grounded in real production/enterprise deployments, and (new this run) a directly-read real-world case study of attribution being revised in public (C-0055) plus a concrete multi-agent attribution method (C-0067). To reach L2: the product-check result and a named user outcome measured against today's UI.
- **Last update**: 2026-10-19.

## I-0004: Comparability guardrails and always show a tradeoff axis

- **Problem / pain point**: comparing runs or models on one accuracy number hides version mismatches and cost/reliability tradeoffs. A 1-point accuracy edge can hide a 10x cost difference.
- **Persona**: Taylor (accountable lead), Alex (analyst), Evan.
- **User outcome**: users compare only comparable runs, and never rank on accuracy alone.
- **Open design question(s)**: #1 (comparability), #9 (comparison as the signature surface).
- **Evidence**:
  - C-0003, tau2-bench v1.0.1: maintainers had to declare scores non-comparable across a grading-fix version. https://github.com/sierra-research/tau2-bench/releases
  - C-0009, HAL (Princeton): cost-aware Pareto-frontier comparison, archived to pursue reliability. https://github.com/princeton-pli/hal-harness
  - C-0044, "Finding the Right Fit" (directly read via companion repo): model rankings reverse across agent harnesses with hard numbers (Claude beats GPT by 7.9 points under one harness, trails by 30.1 under another, same benchmark); a model's own vendor harness is not reliably its best, and higher cost does not reliably buy a higher score. https://arxiv.org/abs/2610.00917v1
  - C-0066, "A Baseline Assessment for the Agentic Web Technology Stack" (abstract read directly): the full protocol+framework+model stack, not just harness alone, is a confound for task completion rate, efficiency, and verbosity. https://arxiv.org/abs/2610.13703
  - C-0058, "Same Query, Different Answer" (abstract read directly): re-executing published benchmarks at scale (1.2M model calls) finds 21% of a benchmark's own already-published results change quality on re-execution — a comparability caution at the level of "did this score even replicate," prior to any cross-run comparison. https://arxiv.org/abs/2610.13823
- **Hypothesis**: LayerLens's immutable versions already block averaging across mismatches; extend that to always show at least one tradeoff axis (cost or reliability) next to the primary score, HAL-style, rather than a single winner.
- **Build caution (new, 2026-10-12)**: C-0044 shows harness/scaffold is as large a confound as model choice or cost — any comparison view should pin and surface harness identity as a first-class dimension, not treat "model" as the whole story.
- **Build caution (new, 2026-10-19)**: C-0066 extends this to the full technology stack (protocol + framework), and C-0058 is a reminder that even a single, un-compared score may not survive its own re-execution — comparability starts before comparison.
- **How to validate**: product check, do comparison views show cost/reliability by default today (open Q#1); prototype a Pareto-style comparison.
- **Maturity**: L1 developing (five sources). To reach L2: the product-check result and a validation plan for the tradeoff view.
- **Last update**: 2026-10-19.

## I-0005: Flag same-family judge/agent pairings

- **Problem / pain point**: an AI judge quietly favors its own model family, biasing verdicts, with no visible signal.
- **Persona**: Evan, Alex, Riley.
- **User outcome**: judge verdicts trusted appropriately; bias surfaced, not hidden.
- **Open design question(s)**: #2 (attribution), differentiator #3 (reproducible, defensible grading).
- **Evidence** (accumulating):
  - C-0002, "The Judge in the Mirror" (pilot): mean self-preference index +0.14, present even without self-recognition. https://github.com/hankimis/self-preference
  - C-0014, "LLMs Trust Their Own" (12 open-weight models, 9 tasks): in-group consensus increases conformity, out-group decreases it, independent of correctness. https://arxiv.org/abs/2609.33495
  - Backed by thesis T-05 (structural identity-linked judge bias).
- **Hypothesis**: when a Judge model shares a vendor/family with the agent under test, flag it and suggest a cross-family judge or a deterministic Grader.
- **How to validate**: cross-family re-judge test (2026-W39 brief), then a product check on whether the Judge/agent model identities are even surfaced today.
- **Maturity**: **L1 developing (upgraded 2026-09-29** from L0): two independent evidence families now, plus a promoted thesis. To reach L2: the product check result plus a named user outcome.
- **Last update**: 2026-09-29.

## I-0007: Make environment lifecycle legible, and let users checkpoint/branch a run

- **Problem / pain point**: users cannot see, while working in an environment, what state it keeps across a run, when it will stop existing, or cheaply save a checkpoint and branch off to try a variation. Lifecycle is invisible.
- **Persona**: Devon (agent engineer), Evan (evaluation owner).
- **User outcome**: users understand and control an environment's state and lifetime, and can explore variants (reproduce, branch, compare) without rebuilding, which also strengthens reproducibility.
- **Open design question(s)**: env state/lifetime (control and recovery) and deterministic replay as a visible surface.
- **Evidence**:
  - C-0012, DeepSeek DSec: stateful pause/resume via snapshots and `pack_diff` (checkpoint a sandbox, restore as a new one) exist as backend capabilities at industrial scale. https://arxiv.org/abs/2609.22978
  - C-0020, Planarian: "agent statepoints" generalize snapshot/rollback/fork to both local AND remote system state via compensating actions — a different team, and the closest external match yet to LayerLens's own system-type shape (Salesforce/Linear/Stripe as remote state); reports up to 15x task-quality improvement. https://arxiv.org/abs/2609.35366
  - C-0023, Counterfactual Rollout Replay: fork/restore applied to RL training reward-shaping, a third distinct angle (training, not infra or runtime UX). https://arxiv.org/abs/2609.33875
  - C-0025, AgentRewind (incomplete access): checkpoints agent context AND environment state together for runtime recovery on long-horizon tasks; closest yet to a product-facing recovery use case. https://arxiv.org/abs/2608.14380
  - C-0028, E2B (first-party feed summary, incomplete access): E2B's own blog describes "pause and fork" as sandbox lifecycle primitives in a reference workbench — the first industry-productized (not academic) data point. https://e2b.dev/resources/build-an-agent-workbench-on-openais-agents-api
  - C-0030, ControlScope (abstract read directly): a taxonomy of repair granularity (continue / edit-argument / replace-workflow) when recovering a running workflow — legibility also means choosing how much to change, not just whether you can checkpoint. https://arxiv.org/abs/2609.34313
  - C-0034, "Recoverability as a System Primitive" (incomplete access): proposes a governance-layer design that explicitly separates "did the restore work" from "was resuming from here permitted," directly answering the C-0026 gap below. https://arxiv.org/abs/2609.13672
  - C-0036, DeltaBox (incomplete access, promoted from pending 2026-10-05): "DeltaState" abstraction (DeltaFS + DeltaCR), millisecond-level (14ms/5ms) checkpoint/rollback via change-based state capture. https://arxiv.org/abs/2605.22781
  - C-0037, Crab (directly read via companion GitHub repo, 2026-10-05): semantics-aware checkpoint/restore closing the "agent-OS semantic gap"; 100% recovery correctness vs. 8-42% baselines, 87% of turns need no checkpoint, 1.9% overhead — the strongest quantitative local-sandbox-state evidence yet, and explicitly, by its own stated design, cannot undo external side effects. https://arxiv.org/abs/2604.28138
  - C-0038, ACRFence (incomplete access, 2026-10-05): demonstrates two concrete "semantic rollback attacks" (Action Replay, Authority Resurrection) with a stated real-tooling PoC (Claude Code CLI + Qwen3-32B), affecting checkpoint-restore across LangGraph/CrewAI/Google ADK/AutoGen; proposes "replay-or-fork" semantics as a mitigation. https://arxiv.org/abs/2603.20625
  - C-0040, StateFork (abstract read directly, 2026-10-12): generalizes checkpoint/branch to agent *exploration* (not just recovery) for terminal agents; names "observation-equivalent restoration" (future actions must produce the same observations) as branching's correctness condition — precise vocabulary for what any LayerLens checkpoint/branch feature must guarantee. https://arxiv.org/abs/2609.38648v1
  - C-0041, "Serving a Revisable World" (abstract read directly, 2026-10-12): the same revoke/preserve/branch shape recurs inside the LLM-serving layer itself; separates request-level resources from execution-version "authority" (who may publish output/install state), a fourth distinct angle beyond infra scale, RL training, and agent-runtime recovery. https://arxiv.org/abs/2610.01160v1
  - Daytona (reported, incomplete access, 2026-10-12): a second commercial vendor productizing Crab directly (not just citing the research) — "agent-aware snapshots" reportedly cut checkpoints by 87% versus snapshotting every turn while maintaining 100% recovery correctness on a 100-turn Terminal-Bench comparison.
  - C-0056, Databricks Lakebase (reported, incomplete access, 2026-10-19): branches an entire Postgres-compatible database in under a second via copy-on-write storage with per-branch role isolation — the first evidence of fast, cheap branching of a genuinely shared, database-shaped resource, narrowing (not closing) the unsolved remote-state gap. https://www.databricks.com/blog/lakebase-and-agentic-sdlc-branching-databases-coding-agents
  - C-0060, "Returning to Development States" (abstract read directly, 2026-10-19): full sandbox snapshot search for coding agents helps mainly because it captures progress outside the repository (databases, services) — concretely supports the local-vs-remote split from the angle of what's valuable to preserve. https://arxiv.org/abs/2610.13841
- **Build caution (2026-09-29)**: C-0026 ("Safe to Resume?") argues correct, state-accurate rollback does not imply secure recovery — a restored checkpoint can resume an execution whose assumptions about the outside world (other services, other agents, real external effects) never validly coexisted. If LayerLens ever ships checkpoint/branch over remote system-type state (Salesforce, Stripe, etc.), "did the restore work" is not the same question as "is it still safe/valid to resume here" — the second needs its own design answer. https://arxiv.org/abs/2608.29381
- **Build response (2026-09-29 pass 3)**: C-0034 proposes exactly the missing second question as a governance-layer decision, auditable separately from the restore itself. Not yet validated, but sharpens the hypothesis below: legibility should show which rule permitted a checkpoint/branch, not just that it technically worked.
- **Build caution sharpened to a demonstrated exploit class (new, 2026-10-05)**: ACRFence (C-0038) turns C-0026's conceptual risk into two named, concrete attacks on real agent tooling — a token or a payment action replayed or resurrected by a naive rollback is not hypothetical. Crab (C-0037), the strongest local-state mechanism found yet, independently and explicitly confirms the same boundary by stating it cannot undo external side effects at all. **The cluster now has a clean internal split**: local sandbox state (filesystem/process memory) is a maturing, near-commodity engineering problem (Crab, DeltaBox, DSec); remote/external state (a CRM write, a payment, a consumed approval token) is the unsolved, actively-exploitable part — and it is exactly LayerLens's own system-type shape (Salesforce, Linear, SEC EDGAR, Stripe, Gmail).
- **Build caution, a new isolation-gap class (2026-10-12)**: Prime Intellect's own disclosed "universal offline sandbox escape" (C-0051) shows a sandbox's declared network isolation can be bypassed entirely through the model-serving layer's own capabilities (a provider API's server-side file/URL fetch), a side-channel invisible to the sandbox's own policy. NVIDIA's new hardware-level Open Agent Safety Platform (C-0050), launched after reported real "offline-but-not" containment failures at two named labs, reinforces the same lesson at the highest stakes: declared isolation is not verified isolation. Any LayerLens checkpoint/branch/lifecycle feature, and the trust wall generally, needs to account for this layer, not just the environment's own sandbox boundary.
- **Hypothesis (sharpened 2026-10-05)**: the local-sandbox-state capability (snapshot, checkpoint/branch) is proven and commoditizing; LayerLens's opportunity is not to build that infra but to make lifecycle legible and verifiable in the product for exactly the harder, unsolved part — remote system-type state — where "did the restore work" and "is it still safe to resume here" are different questions. Show what state persists, when an environment ends, and offer checkpoint/branch/replay as first-class, attributable actions — naming, per ControlScope's taxonomy, how much a recovery action is allowed to change; per the governance-layer idea (C-0034), which rule permitted it; and per ACRFence's pattern, whether a given restore is a genuine replay or a safe fork rather than a silent, potentially duplicate re-execution of an external effect.
- **Narrowing signal (new, 2026-10-19)**: Databricks' Lakebase (C-0056) shows that where LayerLens's own environment owns the stateful resource (a database, as opposed to a genuinely third-party API like Stripe), cheap copy-on-write branching is already a solved engineering problem elsewhere — worth evaluating directly rather than assuming the whole remote-state branch is equally hard. It still does not address ACRFence's attack class (undoing an already-fired external effect), which remains specific to state LayerLens does not own.
- **Differentiator angle**: DSec makes checkpointing a backend feature; making it a legible, verifiable product surface (deterministic replay you can see and trust) is the LayerLens expression, tied to our replayability moat asset. Planarian's remote-state generalization and ACRFence's attack taxonomy are both especially close to our own product shape (remote, record-based system types), closer than the now-more-crowded local-sandbox-state branch.
- **How to validate**: a designer prototype of a checkpoint/branch/replay affordance on an environment run, specifically exercising a remote-write system type (e.g. Stripe or Salesforce) against ACRFence's two named attack shapes, and a product check on whether any of this is discoverable in today's UI.
- **Maturity**: **L1 developing**: now fourteen independent evidence families (DSec, Planarian, Counterfactual Rollout Replay, AgentRewind, E2B, ControlScope, Recoverability-as-Primitive, DeltaBox, Crab, ACRFence, StateFork, Serving a Revisable World, Databricks Lakebase, Returning to Development States) converging on the same mechanism from research, RL training, agent-runtime recovery, LLM-serving infra, shipping industry infrastructure, a governance-design response, and now a named-attack security study — strengthens thesis T-06 further, with its counter-evidence (Safe to Resume / ACRFence / the Prime Intellect and NVIDIA isolation-gap evidence) now the most concrete and actionable part of the whole cluster for LayerLens specifically. To reach L2: a named user outcome and a validation plan result (the designer prototype, ideally run against the remote-state attack shapes above, and now also the inference-layer side-channel class).
- **Last update**: 2026-10-19.

## I-0008: Establish ground truth for a user-built or prod-imported world

- **Problem / pain point**: the stated goal is a synthetic world users can fully mess with AND that mirrors their real prod, so they can thoroughly test agents. But a world a user hand-edits or imports from prod is realistic yet arrives with no answer key, so "what is correct" is unknown and agents cannot be graded against it deterministically.
- **Persona**: Devon (agent engineer), Evan (evaluation owner).
- **User outcome**: users can bring in (or freely build) their real world and still get trustworthy, gradeable results, keeping realism and verifiability together instead of trading one for the other.
- **Open design question(s)**: task feasibility and synthetic-data legibility (where ground truth comes from and how it is validated).
- **Framing correction (from the 2026-09-29 discussion)**: it is NOT realism vs verifiability. Mutation, branching, and checkpointing are all realistic and verifiable, because grading looks at outcomes (actions/state graders already do this), and a snapshot is just a reproducible starting point. The real constraint is narrow: any state you want to GRADE against must be reproducible and have a knowable correct answer. Minted worlds get the answer key for free; user-built or prod-imported worlds do not, so this idea is about capturing ground truth for the realistic end of that spectrum, and guiding which grader (answer / actions / state / judge) applies where.
- **Evidence**:
  - C-0012, DeepSeek DSec: prompted the statefulness/mutability discussion (stateful, branchable worlds at scale). https://arxiv.org/abs/2609.22978
  - Internal: builds on LayerLens's existing learned-world (connect-source) capability and the actions/state/judge grader types.
- **Hypothesis**: if we give users a way to declare or infer what "correct" means for a world we did not mint, we extend verifiable grading from minted worlds to imported/edited ones, unlocking "bring your real world and still trust the verdict."
- **How to validate**: external corroboration or a direct user-need signal (an actual user asking to grade against their own imported world), plus a prototype of a ground-truth-capture flow.
- **Maturity**: L0 nascent, and honestly weaker than most: internally derived from a conversation, no external research corroboration yet. Needs a real user-need signal or a second source to reach L1.
- **Last update**: 2026-09-29.

## I-0006: Confirmations that name the specific consequence

- **Problem / pain point**: approve/deny confirmations gate risky actions but do not inform the decision.
- **Persona**: Devon, Riley.
- **User outcome**: users approve with understanding of what will change, not blindly.
- **Open design question(s)**: #7 (confirmations showing specific consequences).
- **Evidence**:
  - C-0005 / C-0011, Magentic-UI: a three-tier tool-approval policy exists, but whether the confirmation names the specific consequence is undocumented in what was read. https://github.com/microsoft/magentic-ui
  - C-0047, ContractWarden (abstract read directly): a *different* mechanism — an upfront, task-scoped "damage boundary" contract (allow/deny/no_egress) a human authorizes once, then kernel-enforced regardless of what the agent later proposes, rather than a per-action consequence preview. https://arxiv.org/abs/2609.38248v1
- **Hypothesis**: for actions that write to an environment, the confirmation names the specific record or field that will change, not a generic "are you sure?"
- **Distinction noted (2026-10-12)**: ContractWarden answers "what can the agent ever touch" (scope-level, decided once), not "what will this specific action do" (I-0006's own question, still open per T-04). Both are legitimate human-control patterns; LayerLens may eventually want both, but they are not substitutes for each other.
- **How to validate**: product check on the current confirmation UI (open Q#7); design a consequence-preview confirmation.
- **Maturity**: L0 nascent (two sources, but the second is a different mechanism, not a second data point on the same question). To reach L1: a second source specifically on consequence-preview confirmations, or a validated outcome.
- **Last update**: 2026-10-12.

## I-0009: Agent-actionable error and recovery guidance in tool/environment surfaces

- **Problem / pain point**: Tool and API error messages are written for human developers (run a command, edit a config, open a web page). Agents that read these messages often follow the human-oriented step literally, and fail to recover — and, counterintuitively, more capable models follow the bad step more faithfully, not less.
- **Persona**: Devon (agent engineer, debugging why an agent got stuck on a real system); Evan (evaluation owner, wants failures attributed to the right cause).
- **User outcome**: agents recover from real, tool-level failures inside a LayerLens environment instead of silently following advice they cannot act on; failures get attributed to "misleading tool surface" rather than misfiled as "agent error."
- **Open design question(s)**: #2 (failure attribution — a misleading error message is its own nameable failure class), #7 (recovery).
- **Evidence**:
  - C-0018, "MCP Error Messages Written for Developers Hurt the Most Capable Agents Most": in 150 MCP servers, 949/3,001 error messages give human-oriented next steps; following them left recovery as low as 6% (rate limits) or cost up to 69 points of task score (credentials, GPT-6 Astra); naming an actual tool call in the message raised recovery to 84-88%. https://arxiv.org/abs/2609.35381
  - Connects to new thesis T-07 (capability amplifies, not dampens, exploitation of flawed interfaces) via C-0021.
- **Hypothesis**: LayerLens's own shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail) wrap real APIs with real, human-authored error surfaces — this is not a hypothetical failure mode for us. An environment could audit or annotate its tool error surfaces for agent-actionability (does the message name a call the agent can actually make?), and surface a "misleading tool surface" attribution category distinct from agent error.
- **Dedup**: checked against I-0002 (task feasibility, about design-time solvability) and I-0006 (pre-action confirmation consequences); distinct — this is about run-time recovery guidance after a tool failure, not before-the-fact confirmation or task-level solvability.
- **How to validate**: audit a sample of LayerLens's own system-type error surfaces (Salesforce/Linear/Stripe/etc.) for the same human-oriented-step pattern the paper documents; if found, prototype a tool-call-naming rewrite and measure recovery.
- **Maturity**: L0 nascent (one source, though it connects to a two-family thesis, T-07). To reach L1: a second source specifically on agent-actionable error design, or the internal audit result.
- **Last update**: 2026-09-29.

## I-0010: Confidence-aware judge verdicts, with escalation on low confidence

- **Problem / pain point**: thesis T-05/C-0027 already show that a Judge's own re-run consistency is a false reassurance of correctness ("the most reproducible judges are among the least valid"). Users have no visible signal of when a given Judge verdict is actually uncertain versus confidently wrong.
- **Persona**: Evan (evaluation owner), Riley (reviewer, needs to accept a claim without trusting the claimant).
- **User outcome**: judge verdicts carry a legible confidence signal; low-confidence verdicts are flagged or escalated (to a stronger judge, a deterministic Grader, or a human) instead of being presented with the same face-value authority as a confident one.
- **Open design question(s)**: #2 (failure attribution — is a low-confidence Judge verdict its own nameable category, distinct from a wrong verdict presented as confident?).
- **Evidence** (accumulating):
  - C-0032, "JEV-as-a-Judge": a decision-only judge exposing calibrated confidence, escalating low-confidence cases to a stronger judge, beat either the cheap or the strong judge alone (0.9 points more accurate than the strong judge at 41% of its fee); within ~3 points of a top LLM judge at 0.36% of its fee where a verdict could be read off the text. https://arxiv.org/abs/2609.26550
  - C-0033, jev-harness (typed-decision + receipt pattern): a concrete applied instance of the same idea — narrow typed questions, probability + confidence per answer, a deterministic decision table, and a recorded receipt, with human authorization still required before any action. https://github.com/TypeSafeAI/jev-harness
  - Backed by thesis T-05 (as an emerging industry-response signal, adopted independently by 4+ eval/observability vendors — Arize, Confident AI/DeepEval, Langfuse, Browserbase — within one week).
  - C-0049, HATEDECIDE (abstract read directly, 2026-10-12): an independent academic group (not Jev/TypeSafe-affiliated) tests the decision-model category on hate-speech moderation — replicates the cost-efficiency claim (within 1.6 F1 points of a commercial LLM at ~97% lower cost) but finds supplying explicit criteria and decomposing into sub-questions do NOT reliably improve accuracy, a genuine complication to the optimistic framing. https://arxiv.org/abs/2610.03324v1
  - C-0052, OpenAI Decisions API (incomplete access, 2026-10-12): OpenAI shipped a directly competing typed-decision API (`/v1/decisions`, GPT-6 Luna, ~150ms) within about three weeks of Jev's own debut — a frontier lab entering the exact category independently, the single strongest signal yet that this is becoming standard infrastructure, not one startup's bet. Pricing/launch-status details conflict across secondary sources and are unconfirmed.
  - C-0057, decision-model category update (incomplete access, 2026-10-19): ~10 companies shipped a decision-only model within three weeks of Jev's launch (OpenAI, Liquid, Cloudflare, AWS, PostHog + an open clone); a dedicated public leaderboard ("Decision Index") now exists on Hugging Face; TypeSafe AI raised ~$870M at a $7.5B valuation; OpenAI's pricing confirmed at >2x Jev's rate. A category insider cautions the category's own benchmarks "cannot really be trusted" yet. https://arize.com/blog/decision-model-benchmark/
  - C-0065, "Ask Your Advisor" (abstract read directly, 2026-10-19): a related, broader pattern — confidence-gated escalation to a stronger model, generalized from judging to execution/tool-use, with a meta-controller recovering 44-81% of the success gap at under half the cost. https://arxiv.org/abs/2610.13870
- **Hypothesis**: LayerLens's Judges/Scorers could expose the model's own confidence/probability alongside a verdict (not just pass/fail), and use a confidence threshold to route low-confidence cases to a deterministic Grader, a stronger/different Judge, or a flagged-for-human-review state — turning "the judge wasn't sure" into a visible, actionable signal instead of a silently confident-looking verdict.
- **Build caution (new, 2026-10-12)**: C-0049 shows that *how* a decision model is used matters — explicit criteria and sub-question decomposition are not automatically better and should be validated per task, not assumed as a universal improvement.
- **Build caution (new, 2026-10-19)**: C-0057's category insider quote is a reminder that even this category's own benchmarks are young and not yet trustworthy — don't adopt a specific decision-model vendor on benchmark claims alone.
- **Dedup**: checked against I-0005 (flag same-family judge/agent pairings — a different bias-detection mechanism, about *whose* model the judge is, not how confident it was) and I-0006 (confirmations naming consequences — about human approval of agent actions, not judge verdict trust). Distinct: this is about a judge's own uncertainty as a first-class, visible signal.
- **How to validate**: product check, does LayerLens's Judge verdict UI expose any confidence/probability today, or only a pass/fail label (open Q#2); a design sketch of a confidence-flagged verdict; a small test comparing whether users catch a wrong verdict faster when a low-confidence flag is shown versus not.
- **Maturity**: **L1 developing**: now six evidence points across three independent lineages (Jev's own research group, an unrelated academic group, and a competing frontier lab's own shipped product), with the category's growth (a named leaderboard, $7.5B valuation, ~10 entrants) raising the time-sensitivity of the pending product check without itself changing the maturity level. To reach L2: the product-check result plus a named user outcome and validation plan.
- **Last update**: 2026-10-19.

## I-0011: Detect and surface stale environment observations mid-task

- **Problem / pain point**: an agent grounds its reasoning in a tool observation (e.g. a file's contents, a record's state) whose underlying source can change later in the same task — through a concurrent write, a scheduled mutation, a branch/fork, or another agent's action — while the model retains only the stale content in its context. Existing agent runtimes provide little support for signaling this, so the agent (and a human reviewing the trace) can act on, or trust, outdated facts about current state.
- **Persona**: Devon (agent engineer, debugging a trace where the agent's claims don't match a later system check); Evan (evaluation owner, wants a failure correctly attributed to staleness rather than agent error or environment error).
- **User outcome**: agents (and the people reviewing their traces) correctly distinguish "the agent acted on information that was true when observed, but changed since" from "the agent made an error" or "the environment behaved incorrectly" — a new, legible failure category, with less wasted debugging effort re-deriving why a trace looks inconsistent.
- **Open design question(s)**: #2 (failure attribution — staleness as its own nameable category), #7 (recovery — once staleness is detected, what should happen: re-fetch, annotate, or suppress the stale observation).
- **Evidence**:
  - C-0064, "When Agent Context Goes Stale" (abstract read directly): Concord links each tool observation to its source, detects source changes, and applies configurable policies (update/annotate/suppress) before reuse; on a purpose-built benchmark it matched oracle recovery in all evaluated cases across three frontier models while using 46.4% fewer tokens than the strongest non-oracle baseline. https://arxiv.org/abs/2610.05281
- **Hypothesis**: LayerLens's environments are mutable and can be branched/forked/replayed (a core architectural property); any of those operations could leave a running agent holding stale observations about environment state from before the mutation. A lightweight staleness-detection layer (link each tool response to the environment-state version it was read from; flag or re-serve when that version changes mid-task) would make this failure category visible and attributable, rather than silently confusing a trace.
- **Dedup**: checked against I-0009 (agent-actionable error/recovery guidance — distinct: that is about error messages being misleading post-failure; this is about tool *observations* going stale pre-failure, with no error signal at all) and T-06/I-0007 (adjacent but distinct: T-06 is about environment *state* lifecycle from the system's side; this is about the *agent's belief* about that state going stale, a legibility problem on the agent's side of the same boundary). Distinct because no existing idea addresses observation invalidation specifically.
- **How to validate**: a product check on whether any LayerLens environment mutation (a branch, a concurrent edit, a scheduled change) can occur mid-task today, and if so, whether a running agent's prior tool observations are ever invalidated or re-served; a design sketch of a staleness flag in the trace UI.
- **Maturity**: L0 nascent (one source). To reach L1: a second source on stale-observation detection specifically, or a product-check result confirming the failure mode occurs in a LayerLens environment today.
- **Last update**: 2026-10-19.
