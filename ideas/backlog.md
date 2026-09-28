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
| I-0003 | Attribution as a location, every attribution a door | #2 | L1 | 2 | Faster, correct failure diagnosis |
| I-0004 | Comparability guardrails + always show a tradeoff axis | #1, #9 | L1 | 2 | No false comparisons; no accuracy-only ranking |
| I-0001 | Reliability-aware run counts + a pass^k readout | #5 | L1 | 1 | Capability vs reliability made visible; runs spent where they matter |
| I-0002 | "Why is this not solvable" feasibility explanation | #4 | L0 | 1 | Authors design solvable tasks faster |
| I-0005 | Flag same-family judge/agent pairings | #2 | L0 | 1 | Judge verdicts trusted appropriately |
| I-0006 | Confirmations that name the specific consequence | #7 | L0 | 1 | Approve with understanding, not blindly |

---

## I-0001: Reliability-aware run counts and a pass^k readout

- **Problem / pain point**: A single pass or accuracy number hides whether an agent behaves the same way twice. A user can ship an agent that "passed" once and then fails unpredictably in production.
- **Persona**: Evan (evaluation owner), Taylor (accountable lead, shares the readiness report).
- **User outcome**: users can separate capability (can it ever succeed) from reliability (does it succeed every time), and spend runs where reliability matters instead of running everything once or everything many times.
- **Open design question(s)**: #5 (reliability versus one lucky pass), with #1/#9 (comparison).
- **Evidence** (accumulating):
  - C-0008, "Towards a Science of AI Agent Reliability" (Princeton, ICML 2026): pass@k vs pass^k, 12 reliability metrics across 4 dimensions, finding minimal reliability gains despite capability gains. https://arxiv.org/abs/2602.16666
- **Hypothesis** (Javier's, refined): LayerLens holds the task, the grader type, and, because minting is deterministic and free, can cheaply observe run-to-run variance. So it can (a) surface **pass^k as a first-class reliability readout** beside accuracy, and (b) **recommend how many attempts k** a task warrants, single-shot where an answer-key grader on a stable task suffices, multiple where variance is detected or reliability is the question. The adaptive form ("reliability not yet established, run N more" vs "stable across k, stop") is stronger than a static task-type lookup, because variance is empirical.
- **Differentiator angle**: re-running is near-free here (deterministic free minting), so k-repeat reliability testing is economically viable in a way a paid or stateful competitor setup may not be. This makes the feature moat-aligned, not generic.
- **How to validate**: (1) the design exercise, sketch the readout (2026-W40 brief); (2) product check, do Runs/Insights show reliability by default today (open Q#5); (3) user test, show two runs with equal accuracy but different pass^k and see whether users pick the reliable one and can explain why.
- **Maturity**: L1 developing (one strong source + clear outcome + validation plan). To reach L2: a second independent source on measured run-to-run variance, plus the product check result.
- **Last update**: 2026-09-29.

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
- **Hypothesis**: surface attribution as a location on the trace (where it broke) with a routed next action, not a log line, and make the trust wall's guarantees visible so a passing score is legibly not gameable.
- **How to validate**: product check on the current attribution UI (open Q#2); design the trace-location surface; test whether users correctly assign blame faster.
- **Maturity**: L1 developing (two independent corroborating sources + the core differentiator). To reach L2: the product-check result and a named user outcome measured against today's UI.
- **Last update**: 2026-09-29.

## I-0004: Comparability guardrails and always show a tradeoff axis

- **Problem / pain point**: comparing runs or models on one accuracy number hides version mismatches and cost/reliability tradeoffs. A 1-point accuracy edge can hide a 10x cost difference.
- **Persona**: Taylor (accountable lead), Alex (analyst), Evan.
- **User outcome**: users compare only comparable runs, and never rank on accuracy alone.
- **Open design question(s)**: #1 (comparability), #9 (comparison as the signature surface).
- **Evidence**:
  - C-0003, tau2-bench v1.0.1: maintainers had to declare scores non-comparable across a grading-fix version. https://github.com/sierra-research/tau2-bench/releases
  - C-0009, HAL (Princeton): cost-aware Pareto-frontier comparison, archived to pursue reliability. https://github.com/princeton-pli/hal-harness
- **Hypothesis**: LayerLens's immutable versions already block averaging across mismatches; extend that to always show at least one tradeoff axis (cost or reliability) next to the primary score, HAL-style, rather than a single winner.
- **How to validate**: product check, do comparison views show cost/reliability by default today (open Q#1); prototype a Pareto-style comparison.
- **Maturity**: L1 developing (two sources). To reach L2: the product-check result and a validation plan for the tradeoff view.
- **Last update**: 2026-09-29.

## I-0005: Flag same-family judge/agent pairings

- **Problem / pain point**: an AI judge quietly favors its own model family, biasing verdicts, with no visible signal.
- **Persona**: Evan, Alex, Riley.
- **User outcome**: judge verdicts trusted appropriately; bias surfaced, not hidden.
- **Open design question(s)**: #2 (attribution), differentiator #3 (reproducible, defensible grading).
- **Evidence**:
  - C-0002, "The Judge in the Mirror" (pilot): mean self-preference index +0.14, present even without self-recognition. https://github.com/hankimis/self-preference
- **Hypothesis**: when a Judge model shares a vendor/family with the agent under test, flag it and suggest a cross-family judge or a deterministic Grader.
- **How to validate**: cross-family re-judge test (2026-W39 brief).
- **Maturity**: L0 nascent (single pilot). To reach L1: corroborating evidence beyond one pilot, or a strong outcome + validation confirmed.
- **Last update**: 2026-09-29.

## I-0006: Confirmations that name the specific consequence

- **Problem / pain point**: approve/deny confirmations gate risky actions but do not inform the decision.
- **Persona**: Devon, Riley.
- **User outcome**: users approve with understanding of what will change, not blindly.
- **Open design question(s)**: #7 (confirmations showing specific consequences).
- **Evidence**:
  - C-0005 / C-0011, Magentic-UI: a three-tier tool-approval policy exists, but whether the confirmation names the specific consequence is undocumented in what was read. https://github.com/microsoft/magentic-ui
- **Hypothesis**: for actions that write to an environment, the confirmation names the specific record or field that will change, not a generic "are you sure?"
- **How to validate**: product check on the current confirmation UI (open Q#7); design a consequence-preview confirmation.
- **Maturity**: L0 nascent (one source). To reach L1: a second source on consequence-preview confirmations, or a validated outcome.
- **Last update**: 2026-09-29.
