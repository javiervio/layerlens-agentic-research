# LayerLens context

This is what makes the research ours. The agent reads this every run and ties findings back to it. **Javier: correct anything wrong or stale. Treat unverified items as unknown, never as fact.**

<!-- CONTEXT_REVIEWED: 2026-09-29 --> **Context reviewed: 2026-09-29.** Bump this date (and the marker comment) whenever you confirm or correct this file. The weekly health check flags it if it goes stale (~60 days), because every "apply to LayerLens" hypothesis rests on this file being current.

**Source of truth is v1, the shipped product.** This file separates three things and labels every section:
- **[V1]** what exists today, the shipped reality and the source of truth.
- **[PUBLIC]** the live public site positioning (current).
- **[V3 DIRECTION]** a design direction being explored and **not implemented yet.** Useful as intent for how we might design, never as a description of the current product.
- **[AUDIENCE]** personas and jobs, valid as reference regardless of version.
- **[OPEN]** an active design question the research should target.

## What LayerLens is [PUBLIC]

LayerLens is the **Agent Readiness Platform**. Tagline: **"Your business is your benchmark."** The pitch: test agents against the work your business actually requires, the systems your agents use, the situations they need to handle, and the outcomes your business requires, then use the evidence to guide the next change.

It is **one platform with three connected pillars**, short form **"Evaluate. Simulate. Generate.":**
1. **Environments** (flagship): give the agent somewhere to work; test it with the tools and records the task needs.
2. **Evaluations**: check the agent's outputs and actions against your requirements. No environment required.
3. **Synthetic Data**: test situations your current data leaves out. Ground truth included.

**"Flagship" does not mean "environment-first."** The three pillars carry equal weight; Evaluations has the strongest genuine usage today; the environment pillar is a deliberate expansion bet with no observed audience yet.

The load-bearing idea: **where a failure happens is everything.** Every verdict points either to the agent or to the environment.

Status: pre-launch, small real footprint (around twenty signups in the first 90 days, no user interviews yet). Naming: the public brand is **LayerLens**; **Stratix** is the internal name of the application. The current, shipped, canonical product is **v1**.

## What Environments is today [V1, shipped, source of truth]

Public framing of the flagship pillar: "Test agents with the tools and records they need." The user chooses the systems and starting records, runs the task and inspects the actions, and reviews what changed. Every value is labelled **recorded** (real data) or **filled in with the answer key** (synthetic). Available system types today: **Salesforce, Linear, SEC EDGAR, Stripe, Gmail** (Google Calendar also exists in code), more on the way.

Shipped architecture (read from the app's main branch):
- An environment is minted **deterministically** from a type, a seed, knobs, and a cast. No model call is needed to mint it, so iterating it costs nothing. (In the codebase the minted instance is called a "world" or "twin"; the product term is always **environment**, never "world.")
- Every tool call is computed from the environment at request time. The answer key is written in the same act as the data.
- **The trust wall**: the seed and knobs are never served to an agent-facing key, so an agent cannot compute its own grade.
- Graders shipped: answer, actions, judge, state. The agent's own claims are stored beside verdicts, never used as evidence.
- The optimizer improves a structured prompt artifact per (environment, student model) over rounds: 70/30 tuning/holdout slices, only sees tuning failures, gates every candidate for answer leakage on the composed prompt, promotes only when holdout gained is positive and lost is zero.
- Attribution: leave-one-out analysis of what each prompt addition contributed (backend exists; a confirm UI is a fast-follow).

**The shipped UI today** is a Build / Train / Prove cockpit rail over DS tables and panels (Build: Overview, Environment, Chat; Train: Tasks, Runs, Optimize; Prove: Insights/Evidence, Assets; plus Activity). It is **not** a node graph. Any "living graph" or cinematic-playback language belongs to the v3 direction below, not to what exists.

## The three grading mechanisms [V1 + PUBLIC]

Evaluations grade one answer up to three ways. Public example: agent returned $40, answer key says $28.
- **Graders** (deterministic, answer-key): mechanical, no model in the loop, identical every run. Reproducible and defensible.
- **Judges** (AI judge, your rubric): tuned to your team's criteria; versioned, pass/fail verdicts with criteria, evidence, and confidence, with an optimization loop.
- **Scorers** (LLM rubric, 0 to 5 publicly, 0 to 1 internally): rate dimensions like correctness, groundedness, readability. Internally a Scorer is a reusable LLM-judge prompt used inside benchmark evaluations.

Nuance: publicly these read as three symmetric objects, but internally there are two implemented mechanisms with different lifecycles (a versioned Judge that evaluates traces, versus a reusable unversioned Scorer). Do not assume three parallel objects.

Bring your own: private and fine-tuned models, benchmarks as CSV or JSON, or auto-generated from your docs. Compare and track: models head to head, re-run to compare versions.

## What users can do today [V1 feature backbone]

The shipped v1 capabilities (roughly sixty use cases), which the research should treat as the real product surface:
- **Models**: browse and inspect the catalog with drill-to-evidence; register custom HTTP-endpoint models; adapt non-OpenAI contracts; compare head to head; handle provider and deprecation.
- **Benchmarks**: browse and verify provenance; attach; author by upload; generate from documents; synthetic augmentation; curate answer keys; export JSONL. (Backend "datasets" equals UI "Benchmarks.")
- **Judges and Scorers**: create, version, roll back judges; run single, bulk, or N by M; inspect verdict evidence; human-label; optimize; define reusable scorers.
- **Traces and trace datasets**: ingest via SDK, OTLP, Langfuse, file, or samples; replay and inspect; tag; build reproducible datasets; obtain signed attestation (API-only today).
- **Integrations**: inbound sources plus outbound connectors; event subscriptions; route eval outcomes to chat, PM, incident tools.
- **Billing and credits**: balance and ledger; purchase; per-surface insufficient-credits gating; bring-your-own-key bypass. Credits at 1:1 USD (the term "ECU" is discarded).
- **Keys and permissions**: API, provider, and signing keys; collaborators; org roles owner, admin, viewer; tenant isolation.

## Who uses it [AUDIENCE, ratified persona set]

The ratified set is four; it supersedes an older set of ten (Mina, Alex, Sam, Paige, Iris, Casey and others are archived or folded in). All are proto-personas built on assumptions; real evidence is thin.

- **P-1 Devon, the agent engineer (P0).** Builds and ships an AI agent and wires the pipeline (SDK, CI gates, trace ingestion, keys). Core job: run the agent inside a working copy and see whether a failure points to the agent or the environment before a customer finds it. Default lens: Engineer. Primary for Environments and the trace spine.
- **P-2 Evan, the evaluation owner (P0).** Owns what "good" means: benchmarks, graders, judges, scorers; runs and re-runs; calibrates judges against team labels. Primary for the Evaluations pillar; strongest genuine usage. Success: recommend with proof instead of vibes, reproducible records.
- **P-3 Taylor, the accountable lead (P1).** On the hook for the release; sets the bar, signs off, controls budget and seats, shares the readiness report upward. Champion and economic buyer. Entirely assumption-based, no sales evidence yet.
- **P-4 Riley, the reviewer and risk influencer (P1).** Risk, compliance, audit, or external reviewer who never runs anything; consumes evidence, provenance, attestation. An influencer, not a daily user. Gap: attestation is API-only today, so the product barely has a surface for its own marketed compliance audience.

Segments, not personas: **Readers** (anonymous public consumers) and **Adversarial mode** (red-team jobs run by Devon or Evan). Verdict: two P0 user personas (real but thin), one P1 committee persona (assumed), one P1 influencer.

Design rule in force for v1: **light mode.** (The v3 direction proposes a dark canvas; that conflict is unsettled and belongs to the direction below.)

## v3 design direction: NOT built yet [V3 DIRECTION]

Everything in this section is **aspirational design intent under exploration, not shipped.** It is valuable as a north star for how we might design, and as the set of bets the research can inform. The research must never describe it as the current product.

The mandate: the reimagined experience should be market-breaking, nothing like generic eval SaaS. The proposed experience DNA:
1. Generative, AI-native entry: "describe the environment you want" plus Generate; the blank state is a prompt, not an empty table.
2. The environment as a **living graph**, not a data table.
3. **Trace a task through the environment** with cinematic play, step, and speed playback; failures light up in place, so attribution is a location, not a log line.
4. Inspect in place; the canvas is home, tables are contextual panels.
5. Cockpit phases Build, Train, Prove (this part is already shipped in v1 as the rail).
6. **The Gym**: the optimizer as a room you enter.
7. The record as a crafted artifact, security-printing aesthetic.
8. Dark, cinematic, opinionated.

The proposed rigor principles behind it: every mention is a door; every number is a claim with its evidence one click away; go anywhere and the way back restores everything; drawers are contextual, detail pages are for focus; search accelerates, structure orients; honesty rendered in the UI; feedback is quiet, friction is structural (real workloads run minutes to hours); context persistent, identity never ambiguous.

Per-pillar direction: environments as a living graph; evaluations as a "verification bench" whose signature surface is a unified DAG diff for comparing trajectories; synthetic as a "generative studio" that previews one full trace before you spend; a dark cinematic canvas with a light inspector; lists and admin stay conventional on purpose.

## Why it could be defensible (strategy) [V3 DIRECTION / strategy]

The central question: build something that gets better with usage and that no competitor can copy. Honest caveat in the docs: synthetic environments, receipts, the UX, and the word "independence" are all copyable; only the structure is not. The proposed moat: structural neutrality (pages no incumbent can publish), tamper-evident record seniority (an append-only log started early), a data loop on the answer-key join that does not plateau because every new model empties the matrix, and later network effects. Two named uncopyable assets, both only real if the product surfaces them: env-versus-agent attribution base rates, and deterministic replayability shown on every scorecard (seed, version, hash, reproduce affordance). Most of this is design-in-now intent, not shipped.

## House vocabulary and style [enforced]

- Say **environment**, never "world."
- Say **continuous verification** or **re-runs**, never "monitoring."
- Say **points to**, never "root cause."
- Lead with **verification, proof, receipts, on record**; avoid observability framing.
- No em dashes or en dashes. No ISO dates in anything user-facing (use human dates). No "ECU."

## Open design questions the research should target [OPEN]

When a finding speaks to one of these, say so explicitly. Several concern the v3 direction; that is intended, since the point is to inform those bets with outside evidence.

1. **Comparability.** How does a person judge whether two runs are comparable when the environment, data, tools, model, or evaluator changed, and how do we show the versions a result ran against?
2. **Failure attribution in the UI.** Does the interface clearly separate infrastructure, policy, reasoning, and evaluation failures, and could attribution be shown as a location on a trace rather than a log line?
3. **Deterministic replayability as a surface.** How would seed, version, hash, and a reproduce affordance become visible on every scorecard?
4. **Task feasibility.** How does a person author a solvable scenario and see why one is not solvable?
5. **What "repeat a run" means.** A new model call does not guarantee the same trajectory; how do we express variation across attempts (reliability versus one lucky pass)?
6. **Synthetic data legibility.** How does a person inspect a generated task, preview a full trace before spending, and trace it back to generation and validation?
7. **Human control and recovery.** What can a person inspect, interrupt, correct, and resume without rebuilding the whole task, and do confirmations show specific consequences?
8. **The living-graph idea.** Could a node-graph environment with trace-through playback work for real tasks without becoming a toy? (v3 bet.)
9. **Comparison as the signature surface.** What makes a trajectory diff genuinely legible for comparing two agent versions?
10. **The readiness report.** Who is its actual recipient, and what does "ready under budget" need to show to be trusted and shared upward?
11. **The reviewer surface.** What does a risk or compliance reviewer need to accept a claim without trusting the claimant, given attestation is API-only today?
12. **Are Devon and Evan one person** at target customers, or two? This shapes the whole information architecture.
13. **Multi-agent scope.** Does the environment/verification model extend to grading multi-agent *systems*, collaboration quality, coordination, attribution of which agent contributed, or is LayerLens single-agent-against-environment for now? (Open strategic question raised by the multi-agent-evaluation research wave, thesis N-04; not yet decided.)

## What NOT to assume

- **The v3 direction is not shipped.** v1 is the product. Never describe the living graph, the Gym, cinematic playback, or the dark canvas as things that exist. They are bets.
- **Flagship is not env-first.** Do not over-index on environments at the expense of evaluations and synthetic data.
- The public product page describes the pitch, not the internal architecture or roadmap.
- Do not treat any competitor comparison as settled; verify current state before claiming a gap.
- Grader, Judge, and Scorer are not three symmetric objects internally.
- Spaces and the Learn module are being dropped; do not assume public leaderboard or Spaces surfaces carry forward.
