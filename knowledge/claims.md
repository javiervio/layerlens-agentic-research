# Claims

The current state of what we believe about agentic environments. Each claim carries its source, link, date, evidence label, and confidence-with-reasons. The agent updates this every run per `AGENT_RUNBOOK.md`. History is preserved in `changelog.md`; nothing here is deleted silently.

---

### C-0001: Agent benchmarks routinely fail to isolate the agent from the evaluator/ground truth, making them exploitable without genuine task-solving

- **Statement**: An automated red-team audit (BenchJack) of 8 major, widely-used agent benchmarks (SWE-bench Verified, SWE-bench Pro, Terminal-Bench, WebArena, FieldWorkArena, OSWorld, GAIA, CAR-bench; 4,458 tasks total) found all 8 exploitable, with 6 of 8 producing ~98-100% scores via exploits that performed no genuine task-solving. The authors group the exploits into 8 vulnerability classes: no agent/evaluator isolation (V1), ground-truth accessible at runtime (V2), RCE on untrusted input (V3), LLM judges vulnerable to prompt injection (V4), weak string-matching scoring (V5), evaluation edge-case gaps (V6), untrusted code running with evaluator privileges (V7), unnecessary agent permissions (V8).
- **Source(s)**: [BenchJack README](https://github.com/benchjack/benchjack), authors Wang, Li, Mang, Cheung, Sen, Song, arXiv:2605.12673 (May 2026), read scope: README (sections listed), not the arXiv paper itself (arxiv.org unreachable this run).
- **Discovered via**: search.
- **Evidence label**: bounded empirical.
- **Limits**: 8 benchmarks, not a census of the field; audited at a point in time, may since be patched; PoC exploits "not automatically verified against targets" per the authors' own stated limitations; full paper methodology not read directly.
- **Relates to**: none yet (first run).
- **LayerLens relevance**: Open question #2 (Failure attribution in the UI); directly validates the premise behind the "trust wall" differentiator (seed/knobs never served to an agent-facing key) as addressing a documented exploit class (V1, V2), not a hypothetical one.
- **Confidence**: Moderate-high for the existence and prevalence of the problem class (concrete, itemized exploits across named, real benchmarks); low for the claimed follow-up mitigation numbers ("<10% hackable after iterative patching") since that detail was only seen in a search summary, not opened directly — treat that sub-claim as unconfirmed.
- **Recheck after**: 2026-12-24 (capabilities/pricing-adjacent claim about specific benchmarks; ~90 days, since it depends on which benchmark versions were audited).

---

### C-0002: LLM judges show measurable self-preference bias toward their own model family, even under blind judging and even without reliable self-recognition

- **Statement**: In a pilot study, four frontier models across two vendor families (GPT-4o-mini, GPT-4o; Claude Haiku 4.5, Claude Sonnet 4.6) judged 24 open-ended prompts blindly (1,152 pairwise judgments total, both presentation orders tested). Mean Self-Preference Index (a judge's win rate for its own family minus a leave-one-out consensus of other judges) was +0.14 (GPT-4o-mini +0.07, GPT-4o +0.21, Claude Haiku 4.5 +0.14, Claude Sonnet 4.6 +0.14). Only Claude Sonnet 4.6 showed above-chance self-recognition when separately asked to identify authorship; the other three were at chance — i.e. the bias does not require the judge to actually recognize its own output.
- **Source(s)**: ["The Judge in the Mirror"](https://github.com/hankimis/self-preference), Han Kim, IOV Labs, date unknown, read scope: full README.
- **Discovered via**: search.
- **Evidence label**: bounded empirical (author explicitly labels this a pilot).
- **Limits**: pilot scale (24 prompts, 4 models, 2 families, 3-judge consensus baseline); open-ended prompts only, not verifiable/ground-truth tasks; response length correlates with win rate (SPI is designed to control for this, raw scores do not); single independent repo, not peer-reviewed — corroborating academic literature exists (e.g. NeurIPS 2024 self-preference work surfaced in this run's search results) but was not independently opened this run.
- **Relates to**: none yet (first run).
- **LayerLens relevance**: Open question #2 (Failure attribution) and differentiator #3 (reproducible, defensible grading — "a self-check wobbles"). Supports keeping deterministic Graders load-bearing and treating Judges/Scorers as bias-prone signals that may need a same-family flag in the UI.
- **Confidence**: Moderate — internally consistent, transparent about limits, but small sample and unverified authorship/organization track record.
- **Recheck after**: 2026-12-24 (~90 days; model-dependent claim, and newer model versions will need re-testing).

---

### C-0003: An actively maintained, widely-cited agent benchmark had to declare its own scores non-comparable across a patch version because of a grading bug

- **Statement**: tau2-bench release v1.0.1 (2026-07-22) fixed grading bugs in the `banking_knowledge` domain that had been systematically zeroing rewards for cautious, policy-correct agent behavior (plus several related fixes: database-hash comparison, numeric argument normalization, unrealizable golden trajectories in tasks 077-086, transaction sort order, contradictory knowledge-base docs, one task's expected refund amount). The maintainers' release notes state explicitly that results from versions before 1.0.1 are **not comparable** with >= 1.0.1, and that the fix moved every affected score upward only (no pass-to-fail flips), by up to ~9 points depending on model.
- **Source(s)**: [tau2-bench GitHub Releases](https://github.com/sierra-research/tau2-bench/releases), Sierra Research, dated 2026-07-22, read scope: full release notes (primary/maintainer-authored).
- **Discovered via**: search (tau2-bench is also a named reference benchmark in our own `SOURCES.md`; this doubles as this run's periodic verification of that reference).
- **Evidence label**: documented capability (first-party release notes).
- **Limits**: single benchmark instance; does not establish prevalence of this failure mode elsewhere; we read the maintainers' summary of the fix, not the underlying scoring code diff itself.
- **Relates to**: none yet (first run).
- **LayerLens relevance**: Open questions #1 (Comparability) and #4 (what "repeat a run" means); a concrete, dated existence proof for why LayerLens's "immutable environment/task/prompt versions, refuses to average across mismatched versions" differentiator (#5, "On record") solves a real, already-occurring problem. Also a model for honest communication of a breaking grading change (state direction and magnitude of the shift, not just "don't compare").
- **Confidence**: High — first-party release notes, unambiguous statement, no interpretation required.
- **Recheck after**: 2026-10-25 (~30 days; capability/pricing-adjacent, and tau2-bench releases frequently — worth checking for further patches).

---

### C-0004: Practitioner guidance frames context management for long-running agents around three techniques — compaction, structured note-taking, and sub-agent architectures

- **Statement**: Anthropic's engineering guidance distinguishes "context engineering" (curating the optimal token set across an inference run) from prompt engineering, names "context rot" (degradation as context grows), and recommends compaction (summarize + restart with compressed context), structured note-taking (agent-maintained external memory files), and sub-agent architectures (specialized agents return condensed summaries to an orchestrator), plus just-in-time retrieval over upfront loading.
- **Source(s)**: [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), Anthropic, published 2025-09-29, read scope: full text.
- **Discovered via**: search.
- **Evidence label**: proposal / interpretation (vendor practitioner guidance, not a controlled study — no benchmark numbers attached in what was retrieved).
- **Limits**: single-vendor framing; should be corroborated against studies with measured outcomes (a claim about a "98.3% full-summary failure rate" surfaced in this run's search results for a different paper but was not independently opened — see run log, pending).
- **Relates to**: none yet (first run).
- **LayerLens relevance**: General / "context and tools" scope slice; loosely touches open question #6 (human control and recovery) via structured note-taking and sub-agent summaries as inspectable intermediate state.
- **Confidence**: Low-moderate as *new* information — this is foundational, ~1 year old, likely already familiar; flagged in this week's brief as background, not news.
- **Recheck after**: 2027-03-24 (foundational concept, ~180 days).
