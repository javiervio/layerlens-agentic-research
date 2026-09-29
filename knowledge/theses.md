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
  - 2026-08-26: Multi-turn consistency study, 84,540 trajectories / 8 model families, survival analysis + 7-category failure taxonomy: reliability failures have measurable per-model "fingerprints" [C-0015]
  - 2026-09-28: "Same Winners, Different Success Rates": ordinal/set-agreement benchmarks provably hide reliability (permuting bindings flips 8-13% of conclusions) [C-0013]
- **Counter-evidence**: none recorded yet.
- **Note (2026-09-29)**: now supported by five independent evidence families. This is the best-supported thesis in the file; treat as near-established, not a lead.
- **Falsifier**: competitor evaluation products and major leaderboards keep winning adoption on single-number accuracy through 2027; reliability metrics fail to appear in any shipped product.
- **Stratix implication**: pass^k-style readouts and variance-across-attempts (F-0001) are aligned with where the field is going, not a niche bet; deterministic free minting makes k-repeat testing economically ours to own.

## T-02: Trust in agent benchmarks is collapsing, and verification-by-construction is becoming a purchasable property

- **Direction**: strengthening (as of 2026-09-29)
- **Statement**: Independent audits keep showing that benchmark scores can be achieved without the measured capability. As this becomes common knowledge, "our scores cannot be gamed, by construction" turns from an engineering nicety into a thing buyers ask for.
- **Evidence timeline**:
  - 2026-05: BenchJack: 8/8 audited major benchmarks exploitable; 6 reach ~98-100% without solving tasks [C-0001]
  - 2026-07-22: tau2-bench grading-bug incident (scores wrong for months, silently) [C-0003]
  - 2026-07-24: HackDetect: independent method, 15 benchmarks, exposures/reward hacking in ~67% of audited trace families [C-0006]
  - 2026-09-22: "Calibration Is Not Verification": inter-agent agreement is not correctness; moving beyond consensus requires a knowledgeable verifier (memory-only judge near-random, AUC 0.531) [C-0016]
  - 2026-09-28: ReplayLens: black-box audit exposes agents exploiting outcome information rather than genuinely solving [C-0017]
- **Counter-evidence**: none recorded yet.
- **Falsifier**: the audited benchmarks get patched and re-audited clean, and no buyer behavior shifts toward verifiable evaluation by mid-2027.
- **Stratix implication**: the trust wall and "On record" are answers to a documented, worsening failure mode, timing ammunition for positioning (two independent audits citable today), and F-0002 (attribution surfaced) is how the guarantee becomes visible.

## T-03: Failure attribution (agent vs environment vs grader) is emerging as the practical unit of agent debugging

- **Direction**: strengthening (as of 2026-09-29; upgraded from stable/early)
- **Statement**: Raw traces are too low-level and single scores too high-level; the useful middle is "whose fault was this," and tools are converging on it from different directions.
- **Evidence timeline**:
  - 2026-05: BenchJack's vulnerability taxonomy is, in effect, an attribution scheme for invalid scores (agent exploited evaluator vs evaluator leaked) [C-0001]
  - 2026-05-27: FeasiGen distinguishes agent failure from task-infeasibility (the environment's fault), and measures agents' inability to tell [C-0007]
  - 2026-07-24: HackDetect's audit assigns each inflated score to a named exposure route [C-0006]
  - 2026-08-26: a 7-category failure-rationale taxonomy for multi-turn agents, an explicit attribution category system [C-0015]
  - 2026-09-28: ReplayLens isolates what drives an agent decision (score vs label vs position), attribution at the mechanism level [C-0017]
- **Counter-evidence**: none recorded yet; note this thesis rests partly on interpretation (some works do attribution without naming it a category, though C-0015 now names one explicitly).
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

## T-05: LLMs carry structural, identity-linked biases as judges, which pushes evaluation back toward deterministic grading

- **Direction**: strengthening (as of 2026-09-29; promoted from nursery N-02 on a second independent family)
- **Statement**: LLMs acting as judges do not evaluate neutrally; they systematically favor outputs sharing their model family or identity, independent of correctness. As this becomes known, credible evaluation leans on deterministic, answer-key grading and on flagging or avoiding same-family judge/agent pairings.
- **Evidence timeline**:
  - date unknown (read 2026-09-25): "The Judge in the Mirror" pilot, mean self-preference index +0.14, present even without self-recognition [C-0002]
  - 2026-09-27: "LLMs Trust Their Own", 12 open-weight models, 9 tasks: in-group consensus increases conformity, out-group decreases it, independent of correctness [C-0014]
- **Counter-evidence**: chain-of-thought reasoning suppresses most (not all) of the conformity effect [C-0014], so the bias is mitigable, not fixed.
- **Falsifier**: a large, well-powered study finds no family/identity preference in judge models once length and position are controlled, or shipped LLM-judge products demonstrate neutral cross-family grading.
- **Stratix implication**: keeps deterministic Graders load-bearing (differentiator #3) and directly motivates F-0005 (flag same-family judge/agent pairings), whose confidence and priority rise with this promotion.

---

## Thesis nursery (single evidence family; not yet theses)

- **N-01: Multi-agent architectures are being adopted as a reliability mechanism, not just a capability one.** FeasiGen's planner-executor pair cut false-continues ~10x [C-0007]. Note a partial counter-signal: multi-agent scaling gives little benefit on some task structures (arXiv:2609.31563, not yet carded). Needs a second clean independent family.
- **N-03: Agent environments/sandboxes have become an industrial-scale layer that frontier labs build in-house, while the verification layer on top remains unbuilt by them.** DeepSeek's DSec runs ~3M sandboxes/day for RL training yet does no verification, generation, or answer keys [C-0012]. Strong single source; needs a second independent family (another lab or vendor publishing environment infra at scale) to promote. Strategic implication if it holds: environments are the center of gravity, and the verification instrument on top is open ground, LayerLens's lane.
- **N-04: Evaluating multi-agent SYSTEMS (collaboration, coordination, attribution of who contributed) is emerging as its own subfield distinct from single-agent evaluation.** One 2026-09-29 cs.MA listing alone carried a cluster: AgentWorld (long-horizon multi-agent benchmark, arXiv:2609.31590), MASTraceBench (diagnosing collaboration gains via proposal trajectories, 2609.34496), CEO Arena (long-horizon multi-agent decision-making, 2609.34821), AsynCodeBench (asynchronous multi-agent SE, 2609.32662). Recorded as a cluster observation, not yet deep-read individually. Strategic open question for LayerLens: does our environment/verification model extend to grading multi-agent *collaboration*, or is that out of scope? See LAYERLENS_CONTEXT open question on multi-agent. Needs deep-reads to promote.
