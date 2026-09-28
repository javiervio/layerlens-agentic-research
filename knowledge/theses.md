# Field theses

The system's living point of view: five to nine statements about where agentic environments are going, each earned by evidence, never by vibes. This is the instrument that turns months of findings into a worldview and makes cross-time comparison possible.

Rules:
- A thesis requires at least **two independent evidence families** (different authors/orgs, not the same experiment). Single-source candidates wait in the nursery below.
- Every weekly run updates direction arrows during the corroboration pass; the monthly synthesis re-reads the whole file top-down.
- Direction: **strengthening** (new supporting evidence this period), **stable** (no movement), **weakening** (counter-evidence arrived), **broken** (falsified; keep the corpse, it teaches).
- Every thesis names what would falsify it. A thesis nobody could refute is positioning, not knowledge.
- Counter-evidence is recorded with the same care as support. Deleting counter-evidence is falsifying the record.

---

## T-01: Reliability is overtaking raw capability as the differentiating axis of agent evaluation

- **Direction**: strengthening (as of 2026-09-29)
- **Statement**: The field is shifting from "which agent scores higher" to "which agent behaves the same way twice." Capability gains are no longer producing reliability gains, and credible actors are reallocating toward reliability.
- **Evidence timeline**:
  - 2026-02-18: "Towards a Science of AI Agent Reliability" (Princeton, ICML 2026): 12 reliability metrics; verbatim finding "overall reliability shows minimal improvement over time, despite 24 months of model releases" [C-0008]
  - 2026-07-01: HAL (Princeton PLI) archived its cost-aware leaderboard harness, maintainers stating they are "focusing our current work on agent reliability" [C-0009]
  - 2026-07-22: tau2-bench v1.0.1 declared pre/post scores non-comparable after a grading fix, a reliability-of-meaning failure in a widely used benchmark [C-0003]
- **Counter-evidence**: none recorded yet.
- **Falsifier**: competitor evaluation products and major leaderboards keep winning adoption on single-number accuracy through 2027; reliability metrics fail to appear in any shipped product.
- **Stratix implication**: pass^k-style readouts and variance-across-attempts (F-0001) are aligned with where the field is going, not a niche bet; deterministic free minting makes k-repeat testing economically ours to own.

## T-02: Trust in agent benchmarks is collapsing, and verification-by-construction is becoming a purchasable property

- **Direction**: strengthening (as of 2026-09-29)
- **Statement**: Independent audits keep showing that benchmark scores can be achieved without the measured capability. As this becomes common knowledge, "our scores cannot be gamed, by construction" turns from an engineering nicety into a thing buyers ask for.
- **Evidence timeline**:
  - 2026-05: BenchJack: 8/8 audited major benchmarks exploitable; 6 reach ~98-100% without solving tasks [C-0001]
  - 2026-07-22: tau2-bench grading-bug incident (scores wrong for months, silently) [C-0003]
  - 2026-07-24: HackDetect: independent method, 15 benchmarks, exposures/reward hacking in ~67% of audited trace families [C-0006]
- **Counter-evidence**: none recorded yet.
- **Falsifier**: the audited benchmarks get patched and re-audited clean, and no buyer behavior shifts toward verifiable evaluation by mid-2027.
- **Stratix implication**: the trust wall and "On record" are answers to a documented, worsening failure mode, timing ammunition for positioning (two independent audits citable today), and F-0002 (attribution surfaced) is how the guarantee becomes visible.

## T-03: Failure attribution (agent vs environment vs grader) is emerging as the practical unit of agent debugging

- **Direction**: stable, early (as of 2026-09-29)
- **Statement**: Raw traces are too low-level and single scores too high-level; the useful middle is "whose fault was this," and tools are converging on it from different directions.
- **Evidence timeline**:
  - 2026-05: BenchJack's vulnerability taxonomy is, in effect, an attribution scheme for invalid scores (agent exploited evaluator vs evaluator leaked) [C-0001]
  - 2026-05-27: FeasiGen distinguishes agent failure from task-infeasibility (the environment's fault), and measures agents' inability to tell [C-0007]
  - 2026-07-24: HackDetect's audit assigns each inflated score to a named exposure route [C-0006]
- **Counter-evidence**: none recorded yet; note this thesis rests partly on interpretation (these works do attribution without naming it a category).
- **Falsifier**: debugging tools consolidate on trace-level observability without attribution categories, and users prove fine with it.
- **Stratix implication**: env-vs-agent attribution is already shipped backend truth; T-03 says the market is walking toward it. F-0002 makes it legible before someone else names the category.

## T-04: Oversight tooling answers "when to ask permission" but not "what to show when asking" — consequence legibility is white space

- **Direction**: stable, early (as of 2026-09-29)
- **Statement**: Approval mechanisms (tiers, guards, gates) are maturing fast, but what the confirmation actually communicates (the specific consequence of the pending action) is unexamined, including by the leaders.
- **Evidence timeline**:
  - 2026-09-25/28: Magentic-UI ships a three-tier approval policy; its docs, read directly, do not describe what a confirmation shows [C-0005, C-0011]
  - 2026-09-28: this run's search across the oversight literature found no shipped mitigation or published pattern for consequence-preview confirmations (absence of findings, recorded honestly, not proof of absence)
- **Counter-evidence**: none recorded yet; evidence base is thin and partly negative-space, treat accordingly.
- **Falsifier**: a major agent product ships consequence-naming confirmations, or HCI literature surfaces that already solved this.
- **Stratix implication**: F-0006 is a candidate innovation lane (not a fast follow of anyone); for a product whose story is legible verification, an illegible confirmation is off-thesis.

---

## Thesis nursery (single evidence family; not yet theses)

- **N-01: Multi-agent architectures are being adopted as a reliability mechanism, not just a capability one.** FeasiGen's planner-executor pair cut false-continues ~10x [C-0007]. Needs a second independent family.
- **N-02: LLM judges carry structural biases that will push evaluation back toward deterministic grading.** One pilot on self-preference [C-0002]. Needs corroboration at scale.
- **N-03: Agent environments/sandboxes have become an industrial-scale layer that frontier labs build in-house, while the verification layer on top remains unbuilt by them.** DeepSeek's DSec runs ~3M sandboxes/day for RL training yet does no verification, generation, or answer keys [C-0012]. Strong single source; needs a second independent family (another lab or vendor publishing environment infra at scale) to promote. Strategic implication if it holds: environments are the center of gravity, and the verification instrument on top is open ground, LayerLens's lane.
