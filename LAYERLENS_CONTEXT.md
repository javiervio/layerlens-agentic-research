# LayerLens context

This is what makes the research ours. The agent reads this every run and ties findings back to it. Seeded by Claude from the canonical LayerLens docs as of September 2026. **Javier: correct anything wrong or stale. Treat unverified items as unknown, never as fact.**

Status marker: [SEEDED] = drafted by Claude from internal docs, pending Javier's confirmation. [CONFIRMED] = Javier verified. [OPEN] = an active design question the research should target.

## What LayerLens is [CONFIRMED: public site, Sep 2026]

LayerLens is the **Agent Readiness Platform**. Tagline: **"Your business is your benchmark."** The pitch: test agents against the work your business actually requires, the systems your agents use, the situations they need to handle, and the outcomes your business requires, then use the evidence to guide the next change.

It is **one platform with three connected pillars**, short form **"Evaluate. Simulate. Generate.":**
1. **Environments** (flagship): give the agent somewhere to work; test it with the tools and records the task needs.
2. **Evaluations**: check the agent's outputs and actions against your requirements. No environment required.
3. **Synthetic Data**: test situations your current data leaves out. Ground truth included.

Use one, or connect all three to keep testing as the agent evolves.

The load-bearing idea, stated on the home page: **where a failure happens is everything.** Every verdict points either to the agent or to the environment. That attribution, plus results you can reproduce and defend ("on record"), is the spine of the product.

Status: pre-launch, small real enterprise footprint (order of tens of active users on core actions as of September 2026). Note on naming: the public brand is **LayerLens**; **Stratix** is the internal name of the application. Describe capabilities, not version labels.

## What Environments is [CONFIRMED public framing + SEEDED internal architecture]

Public framing (the flagship pillar): "Test agents with the tools and records they need." The user chooses the systems and starting records, runs the task and inspects the actions, and reviews what changed in the environment. Every value is labelled either **recorded** (from real data) or **filled in with the answer key** (synthetic, to cover a gap). World types available: **Salesforce, Linear, SEC EDGAR, Stripe, Gmail**, with more on the way.

Internal architecture (deeper truth behind the pillar, from the app):
- A world (also called a twin) is minted **deterministically** from a type, a seed, knobs, and a cast. No model call is needed to mint it, so iterating a world costs nothing.
- Every tool call is computed from the world at request time. Every answer an agent can be graded on is in the answer key by construction, written in the same act as the data.
- **The trust wall**: the seed and knobs are never served to an agent-facing key, so an agent can never compute its own grade.
- The optimizer: a structured prompt artifact per (environment, student model), improved over rounds. It uses 70/30 tuning/holdout slices, only ever sees tuning failures, gates every candidate for answer leakage on the composed prompt, and promotes only when holdout gained is positive and lost is zero.
- Attribution: leave-one-out analysis of what each prompt addition contributed.

The public five-step loop is **Build, Run, Eval, Optimize, On record** (ending in a readiness report). Internally the app groups the same work under a **Build / Train / Prove** rail (Build: Overview, Environment, Chat; Train: Tasks, Runs, Optimize; Prove: Insights/Evidence, Assets; plus Activity).

## The three grader types [CONFIRMED: public site]

Evaluations grade one answer in up to three ways. The example: the agent returned $40, the answer key says $28.
- **Graders** (deterministic, answer-key): mechanical, no model in the loop, identical every run. "A verdict you can reproduce and defend."
- **Judges** (AI judge, your rubric): tuned to your team's review criteria, so it applies your policy rather than a generic one.
- **Scorers** (LLM rubric, 0 to 5): rates dimensions like correctness, groundedness, readability, so you see how good and where it breaks, not just pass/fail.

Bring your own: private and fine-tuned models, benchmarks as CSV or JSON, or auto-generated from your docs. Compare and track: models head to head, and re-run to compare versions.

## The differentiators to preserve

1. **Env-versus-agent attribution** [CONFIRMED, the headline]. Every verdict points to the agent ("the twin served recorded values; the claim did not match") or to the environment ("the working copy refused to make something up; record the field and the test gets stronger"). Derived from the transcript, never from the agent's claim.
2. **Deterministic free minting and the trust wall** [SEEDED]. The answer key is minted from recorded values; iterating a world costs nothing; the seed and knobs are never served.
3. **Reproducible, defensible grading** [CONFIRMED]. Mechanical grading, nothing self-scored; the deterministic grader gives the same verdict every run while a self-check "wobbles."
4. **The leak-gated optimizer** [SEEDED]. A governed, gated prompt-improvement loop in a UI. Nobody else is known to ship this.
5. **Provenance, "On record"** [CONFIRMED + SEEDED]. Every result carries its evidence; immutable environment, task, and prompt versions; runs stamped with the versions they ran against; the grid refuses to average across mismatched versions; cost measured from real usage, never estimated.
6. **The cast and composites** [SEEDED]. "These are the same companies" as a checked fact across services, so cross-service questions stay honest.

## Who uses it [CONFIRMED public framing + SEEDED internal personas]

Public framing, "built for the people on the hook":
- **AI and platform engineers**: grade their own agent, inspect every verdict and its evidence, review the steps behind the result.
- **Engineering and product leaders**: compare agent versions against the tasks and outcomes the business requires; one readiness report to share.
- **Risk and compliance**: review requirements, results, and supporting evidence together; defined terms, stated limitations, mechanical grading, everything on record.

Internal personas behind those groups: Devon (agent builder, P0), Evan (eval specialist, P0), Mina (observability, P0), Taylor (QA/regression), Alex (analyst/model comparison), Riley (compliance). Design rule: light mode is non-negotiable; several personas are non-engineering.

The Environments user, concretely, is the person who assembles a world, authors or generates tasks, runs agents against it, reads the optimizer rounds, and reviews the proof. Success is: they can tell whether a failure was the agent's or the environment's, whether two runs are comparable, and what to fix next.

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
