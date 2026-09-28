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

---

### C-0005: Magentic-UI is an open-source human-in-the-loop multi-agent web interface built around named interaction mechanisms including action guards

- **Statement**: Magentic-UI (Microsoft Research) is an open-source, MCP-extensible, multi-agent web interface for web browsing, code execution, and file manipulation, designed around human-in-the-loop collaborative control rather than full autonomy, via named mechanisms: co-planning, co-tasking, multi-tasking, action guards (safety checkpoints), and long-term memory.
- **Source(s)**: [Magentic-UI publication page](https://www.microsoft.com/en-us/research/publication/magentic-ui/), Microsoft Research, date unknown, read scope: page summary only (2026-09-25). Extended 2026-09-28: see C-0011 for a direct read of the actual tool-approval mechanism.
- **Discovered via**: citation (our own SOURCES.md seed list).
- **Evidence label**: documented capability (first-party description) for the existence and named mechanisms; proposal for the framing that human-in-the-loop is "a promising path forward."
- **Limits**: only a landing-page summary was read for the general framing; no evaluation data captured. (Note: this claim ID was created via `cards/magentic-ui.md` on 2026-09-25 but not backfilled into this file until the 2026-09-28 run — a bookkeeping gap now closed; see `knowledge/changelog.md`.)
- **Relates to**: extended by C-0011 (concrete tool-approval mechanism, read directly 2026-09-28).
- **LayerLens relevance**: Open questions #2 (failure attribution) and #6/#7 (human control and recovery, confirmations naming specific consequences).
- **Confidence**: Moderate for the general framing (first-party, but summary-level); see C-0011 for higher-confidence specifics.
- **Recheck after**: 2026-12-24 (~90 days).

---

### C-0006: An independent benchmark-exploitability audit (different methodology, largely non-overlapping benchmark set) reportedly reaches a compatible conclusion to BenchJack, but is not yet independently read

- **Statement**: A paper titled "Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI" reportedly audited 2,385 traces across 15 agent benchmarks (via a method called HackDetect) and found exposure/reward-hacking evidence in 67.0% of "Frontier Science" traces and 66.7% of "AutoLab" traces, with score inflation ("Mislead gap") of 0.45-1.00 in paired comparisons.
- **Source(s)**: arXiv:2607.22368, authors not confirmed, date unconfirmed (~2026-07-24 per aggregated search text), read scope: **none directly** — arxiv.org and a mirror (pith.science) were both blocked; this is search-summary only.
- **Discovered via**: search.
- **Evidence label**: incomplete access.
- **Limits**: This is the weakest-confidence claim in this file. No primary text, not even an abstract, was opened. Numbers come from WebSearch's own aggregation across secondary listing pages. Treat as a lead, not a corroboration, until directly read.
- **Relates to**: plausibly extends/corroborates C-0001 (BenchJack) — different method, different (non-overlapping named) benchmarks, same general phenomenon — but this upgrade from "plausible" to "confirmed" requires a direct read that has not happened in two attempts (this run and implicitly available since May per publication date).
- **LayerLens relevance**: Open question #2 (failure attribution); same territory as C-0001's support for the "trust wall" differentiator.
- **Confidence**: Low — search-summary only, cannot rule out misattribution or aggregation error in the numbers themselves.
- **Recheck after**: 2026-10-12 (short — this should be retried again next run before the normal 30-day cycle, since it's a discovery-only lead, not a settled claim).

---

### C-0007: Current models show weak infeasible-task detection; multi-agent setups reportedly help substantially (not yet independently read)

- **Statement**: A paper proposing "FeasiGen" (a pipeline that builds infeasible tool-use tasks by masking tools that successful runs consistently require) reportedly found false continue rates (proceeding despite infeasibility) of 23.5%-73.9% across nine single-agent models, and that multi-agent architectures cut the average false continue rate from 54.6% to 17.5%.
- **Source(s)**: [FeasiGen paper](https://arxiv.org/abs/2605.28532), Liang Cheng, Mingsheng Cai, Jiuming Jiang, Luo Mai (University of Edinburgh), 2026-05-27, read scope: **none directly** — search-summary only; arxiv.org blocked again this run (second run in a row this exact paper could not be opened).
- **Discovered via**: search (flagged high-priority pending from the 2026-09-25 run).
- **Evidence label**: incomplete access.
- **Limits**: no primary text opened; cannot confirm task domains, exact multi-agent configuration, or the >94% infeasibility-annotation-accuracy claim about the benchmark's own construction.
- **Relates to**: none yet — first claim on this exact topic in our knowledge base.
- **LayerLens relevance**: Open question #4 (task feasibility) — directly on point, though note the paper is about agents recognizing infeasibility at run time, which is the mirror image of LayerLens's question of authors constructing solvable scenarios at design time.
- **Confidence**: Low — search-summary only; author names and affiliation are confirmed (a rare case where WebSearch surfaced them explicitly), which is a mild positive signal for genuineness, but does not substitute for reading the methodology.
- **Recheck after**: 2026-10-12 (short — retry before normal cycle; two consecutive runs unable to open a directly-relevant paper is itself worth escalating).

---

### C-0008: A proposed reliability-science framework distinguishes pass@k (capability) from pass^k (reliability) and reportedly finds capability gains have not translated into reliability gains (not yet independently read)

- **Statement**: "Towards a Science of AI Agent Reliability" (Rabanser, Kapoor, Kirgis, Liu, Utpala, Narayanan — Princeton, ICML 2026 poster) proposes twelve metrics across four dimensions (consistency, robustness, predictability, safety), distinguishes pass@k (at least one success in k attempts) from pass^k (all k attempts succeed), and reportedly evaluated 15 models across two benchmarks (K=5 repeats, J=5 paraphrases, p_fault=0.2 fault injection), finding only small reliability improvements despite capability gains.
- **Source(s)**: arXiv:2602.16666, read scope: **none directly** — arxiv.org, alphaxiv.org, and huggingface.co/papers all blocked this run; a reported companion GitHub repo's URL could not be located via search.
- **Discovered via**: search (via the deliberate contradicting-evidence search slice on non-determinism in agent evaluation).
- **Evidence label**: incomplete access.
- **Limits**: no primary text opened; specific metrics, benchmarks, and models unconfirmed. Author reputation (same lab as HAL, ICML acceptance) is noted as a mild confidence factor but explicitly not treated as evidence.
- **Relates to**: connects to C-0009 (HAL) — same lab, and HAL's own README states the team "are focusing our current work on agent reliability," which is consistent with (though does not independently confirm) this paper being that follow-on work.
- **LayerLens relevance**: Open question #5, nearly verbatim ("how do we express variation across attempts — reliability versus one lucky pass"). The single best-matched open question of this run, despite the weak access.
- **Confidence**: Low on the numbers (search-summary only); moderate that the general framing (pass@k vs pass^k as a real, useful distinction) is sound, since this distinction is corroborated independently by other sources found this run (e.g. a CORE-bench reference to "pass^k... chance that all k task trials are successful").
- **Recheck after**: 2026-10-12 (short — high-value paper, retry before normal cycle).

---

### C-0009: Cost-blind agent leaderboards produce uninformative comparisons; a Pareto-frontier, cost-controlled evaluation approach is a directly-verified alternative design

- **Statement**: HAL (Holistic Agent Leaderboard), a Princeton PLI project, is a standardized agent-evaluation harness spanning 9+ benchmarks that reports cost alongside accuracy by default and frames comparison as a cost-accuracy Pareto frontier rather than a single ranked number, explicitly to answer "what does it mean if an agent has 1% higher accuracy but is 10x more expensive?" The project is now archived (as of 2026-07-01), with the maintainers stating they are "focusing our current work on agent reliability" instead.
- **Source(s)**: [hal-harness README](https://github.com/princeton-pli/hal-harness), Princeton PLI, retrieved 2026-09-28, read scope: **full text, read directly** (github.com is reachable in this session, unlike arxiv/alphaxiv/huggingface). Companion paper reportedly arXiv:2510.11977 (ICLR 2026), not independently read.
- **Discovered via**: search, then citation (via the agent-eval / Pareto-curves repo, same authors).
- **Evidence label**: documented capability (primary source, directly read) for the design, rationale, and archival statement. The specific "100x cost differentials for 1% accuracy gains" and "less than one-third of models on the Pareto frontier" figures are evidence label incomplete access (only from a secondary WebSearch summary, not the README text itself).
- **Limits**: README describes design intent, not the underlying visualization math or a worked example; this run did not verify the harness against real output.
- **Relates to**: connects to C-0008 (reliability paper) — same lab, explicit stated pivot from comparability to reliability work.
- **LayerLens relevance**: Open questions #1 (comparability) and #9 (comparison as the signature surface). Directly supports the design principle that "better" must specify a tradeoff dimension, not just a rank — matches PROTOCOL.md's own evidence-discipline language almost exactly.
- **Confidence**: High for the design/rationale/archival facts (directly read, first-party, unambiguous). Low for the specific cost-differential numbers (secondary summary only).
- **Recheck after**: 2027-03-24 (foundational design pattern, ~180 days) for the design claim; 2026-10-12 for the unconfirmed numbers.

---

### C-0010: Braintrust reportedly offers side-by-side experiment comparison with test-case-level output diffs, and a sandboxed-eval mode that keeps platform credentials out of agent-reachable code (not yet independently read)

- **Statement**: Braintrust's "Experiments" are immutable comparable snapshots; the comparison view reportedly shows score breakdowns, regression detection, and output diffs "at the test case level" between two experiments. Separately, Braintrust's "Harbor" sandboxed-eval integration reportedly keeps the platform API key "in the host process" so "agent code running in the sandbox cannot read it."
- **Source(s)**: braintrust.dev docs/blog pages (comparing-experiments, harbor-agent-evals, platform/experiments), read scope: **none directly** — www.braintrust.dev blocked again this run (second run in a row); search-summary only.
- **Discovered via**: search (Braintrust is a named "team to watch" in SOURCES.md).
- **Evidence label**: incomplete access.
- **Limits**: cannot confirm whether "output diff" is trajectory/step-level or only final-output level (directly relevant to open question #9); cannot confirm the actual isolation guarantees of Harbor's sandboxing beyond one summarized sentence.
- **Relates to**: adjacent to C-0001/C-0006 (agent/evaluator isolation as a recognized problem class) — Harbor's credential-isolation pattern rhymes with LayerLens's "trust wall," though it protects a different asset (API key vs. seed/knobs) — treat as a parallel pattern, not the same mechanism, until confirmed.
- **LayerLens relevance**: Open questions #1, #9 (comparability, trajectory diff as signature surface); general (trust boundary pattern).
- **Confidence**: Low — search-summary only, two runs in a row blocked from this vendor's own docs.
- **Recheck after**: 2026-10-12 (short — retry; this vendor has now been search-summary-only twice).

---

### C-0011: Magentic-UI's "action guards" are concretely a three-tier, per-agent tool-approval policy; whether confirmations show specific consequences is undocumented in what was read

- **Statement**: Magentic-UI implements action guards as a configurable tool-approval policy with three settings — `auto_approve` (no checks, eval/trusted only), `require_approval_untrusted` (default: prompts before untrusted tool calls, auto-approves read-only calls), `require_approval_all` (every tool call confirmed) — configurable per-agent (orchestrator or web_surfer) via YAML.
- **Source(s)**: [magentic-ui configuration.md](https://raw.githubusercontent.com/microsoft/magentic-ui/main/docs/configuration.md), Microsoft, retrieved 2026-09-28, read scope: full text, read directly (github/raw.githubusercontent reachable).
- **Discovered via**: citation (following up C-0005 from the prior run).
- **Evidence label**: documented capability (first-party docs, directly read).
- **Limits**: as read, the docs do not state what a confirmation dialog displays, whether it names the specific consequence of the pending action, or the scope/persistence of an approval. This is recorded as "not described in what we read" per PROTOCOL.md rule 5, not as a claim the feature is absent — a further `docs/limitations.md` was referenced but not fetched this run.
- **Relates to**: extends C-0005 (replaces vague "action guards" framing with the concrete mechanism).
- **LayerLens relevance**: Open questions #6/#7 (human control and recovery — "do confirmations show specific consequences?"). A concrete, comparable design to benchmark LayerLens's own confirmation UI against.
- **Confidence**: High for the three-tier mechanism itself (directly read, unambiguous). No confidence either way on the consequence-preview question — explicitly unresolved.
- **Recheck after**: 2026-12-24 (~90 days).
