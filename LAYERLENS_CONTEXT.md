# LayerLens context

This is what makes the research ours. The agent reads this every run and ties findings back to it. Seeded by Claude from the canonical LayerLens docs as of September 2026. **Javier: correct anything wrong or stale. Treat unverified items as unknown, never as fact.**

Status marker: [SEEDED] = drafted by Claude from internal docs, pending Javier's confirmation. [CONFIRMED] = Javier verified. [OPEN] = an active design question the research should target.

## What LayerLens is [SEEDED]

LayerLens builds verification infrastructure for AI. Stratix is the flagship evaluation platform: the independent proof layer that turns AI claims into verifiable evidence. Status: pre-launch, small real enterprise footprint (order of tens of active users on core actions as of September 2026).

The moat is verification made legible: environment-versus-agent attribution, a leak-gated optimization loop, and attested receipts. The backend already builds this; the experience is where the differentiation is still being invested.

## What Environments is [SEEDED]

Environments are simulated API services (called twins or worlds) that an agent is evaluated against. Key properties:

- A world is minted deterministically from a type, a seed, knobs, and a cast. No model call is needed to mint it, so iterating a world costs nothing.
- Every tool call is computed from the world at request time. Every answer an agent can be graded on is in the answer key by construction, written in the same act as the data.
- The trust wall: the seed and knobs are never served to an agent-facing key, so an agent can never compute its own grade.
- World types shipped: SEC EDGAR, Stripe, Gmail, Salesforce, Linear, Google Calendar. Some support writes on live state.
- Graders: answer, actions, judge, state. The agent's own claims are stored beside verdicts but never used as evidence.
- The optimizer: a structured prompt artifact per (environment, student model), improved over rounds. It uses 70/30 tuning/holdout slices, only ever sees tuning failures, gates every candidate for answer leakage on the composed prompt, and promotes only when holdout gained is positive and lost is zero.
- Attribution: leave-one-out analysis of what each prompt addition contributed.

The information architecture is three surfaces: **Build** (Overview, Environment, Chat), **Train** (Tasks, Runs, Optimize), **Prove** (Insights/Evidence, Assets), with Activity as history. An environment detail replaces the global sidebar with its own rail.

## The differentiators to preserve [SEEDED]

1. **Env-versus-agent attribution.** Four honest buckets per failed attempt (agent missed it, environment could not answer, agent stopped early, cannot attribute), derived from the transcript, never from the agent's claim.
2. **The leak-gated optimizer.** A governed, gated prompt-improvement loop in a UI. Nobody else is known to ship this.
3. **Provenance and receipts.** Immutable environment, task, and prompt versions; runs stamped with the versions they ran against; the grid refuses to average across mismatched versions; cost measured from real usage, never estimated.
4. **Deterministic free minting.** Worlds mint with no model call; the answer key is written with the data.
5. **Prompt-diff mechanics.** Sentences as lines, word-level highlight, every change carrying its reason and its gained/lost tasks (partially shipped).
6. **The cast and composites.** "These are the same companies" as a checked fact across services, so cross-service questions stay honest.

## Who uses it [SEEDED]

Primary (P0) users relevant to Environments:
- **Devon**, AI/ML developer and agent builder: builds reliable agents, debugs, iterates fast, evaluates in CI/CD.
- **Evan**, ML evaluation specialist: designs evals, builds custom scorers and judges, cares about reproducibility.
- **Mina**, AI observability analyst: monitors production agents, evaluates production traces.

Also relevant: Taylor (QA/testing, regression gates), Alex (analyst, model comparison), Riley (compliance, attestation and evidence export). Design rule: light mode is non-negotiable; several personas are non-engineering.

The Environments user, concretely, is the person who builds or configures a world, authors or generates tasks, runs agents against it, reads the optimizer rounds, and reviews the proof. Success is: they can tell whether a failure was the agent's or the environment's, whether two runs are comparable, and what to fix next.

## Open design questions the research should target [OPEN]

These are live, unresolved decisions from the current design program. When a finding speaks to one of these, say so explicitly.

1. **Comparability.** How does a person judge whether two runs are comparable when the environment, data, tools, model, or evaluator changed? How do we show the versions a result ran against?
2. **Failure attribution in the UI.** Does the interface clearly separate an infrastructure failure from a policy failure from a reasoning failure from an evaluation failure? Is every attribution chip a routed next action ("diagnosis as a door")?
3. **Task feasibility.** How does a person author a solvable scenario and see *why* one is not solvable?
4. **What "repeat a run" means.** A new model call does not guarantee the same trajectory. How do we express variation across attempts (reliability versus one lucky pass)?
5. **Synthetic data legibility.** How does a person inspect a generated task or world and trace it back to how it was generated and validated?
6. **Human control and recovery.** What can a person inspect, interrupt, correct, and resume without rebuilding the whole task? Do confirmations show specific consequences?
7. **How much prompt structure to surface** on Optimize (five sections plus history versus promoted lines only).
8. **The auto-loop** ("Improve until" up front versus manual rounds first).
9. **Tools-first versus data-first** ordering on the Environment page.
10. **Environment-first platform reframe** (open, larger direction question).

## What NOT to assume [SEEDED]

- The public product page describes agentic evaluations broadly. It does not describe the internal Environments architecture. Do not infer roadmap from it.
- Do not treat any competitor comparison as settled. Verify current state before claiming a gap.
- Version naming inside LayerLens is contested; do not lean on it. Describe capabilities, not version labels.
