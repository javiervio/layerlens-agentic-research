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
- **Relates to**: **now corroborated by C-0014** (identity-dependent conformity, 12 models, independent authors/method), 2026-09-29. Together they form two independent evidence families, promoting nursery N-02 to thesis T-05.
- **LayerLens relevance**: Open question #2 (Failure attribution) and differentiator #3 (reproducible, defensible grading — "a self-check wobbles"). Supports keeping deterministic Graders load-bearing and treating Judges/Scorers as bias-prone signals that may need a same-family flag in the UI.
- **Confidence**: Upgraded 2026-09-29 from moderate to moderate-high: the single pilot is now independently corroborated by a 12-model study (C-0014). The specific SPI numbers remain pilot-scale; the existence and direction of the bias are now well-supported.
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

### C-0006: An independent benchmark-exploitability audit (different methodology, largely non-overlapping benchmark set) corroborates BenchJack (abstract read directly 2026-09-29)

- **Statement**: The paper "Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI" audited 2,385 traces across 15 agent benchmarks (via a method called HackDetect) and found exposure/reward-hacking evidence in 67.0% of "Frontier Science" traces and 66.7% of "AutoLab" traces, with score inflation ("Mislead gap", defined as exploit score minus intended score) of 0.45-1.00 in paired comparisons. Named exploit routes: recover public solutions, read evaluation artifacts, infer generator structure, manipulate feedback, benefit from invalid scoring paths.
- **Source(s)**: [Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/abs/2607.22368), Jiaqi Shao, Hanck Chen, Wei Zhang, Maxm Pan, Bing Luo, 2026-07-24, read scope: **abstract read directly** (manual deep-read 2026-09-29, local full-web session); full methodology tables not read.
- **Discovered via**: search (cloud run), upgraded via manual deep-read.
- **Evidence label**: bounded empirical (abstract read directly).
- **Limits**: only the abstract was read; per-benchmark tables and the HackDetect method internals not verified. Two benchmark families named (Frontier Science, AutoLab); the other 13 of the 15 are not individually confirmed here.
- **Relates to**: **corroborates C-0001 (BenchJack)** — different method, largely non-overlapping benchmarks, same phenomenon. Now upgraded from "plausible" to confirmed corroboration via direct read (independent evidence, not the same experiment).
- **LayerLens relevance**: Open question #2 (failure attribution); same territory as C-0001's support for the "trust wall" differentiator.
- **Confidence**: Moderate-high — abstract read directly, headline numbers confirmed verbatim; full methodology not yet read.
- **Recheck after**: 2027-01-24 (~180 days; the phenomenon is now doubly corroborated, no longer a discovery-only lead).

---

### C-0007: Current models show weak infeasible-task detection; multi-agent planner-executor setups help substantially (abstract + body read directly 2026-09-29)

- **Statement**: FeasiGen (a pipeline that builds infeasible tool-use tasks by masking tools that successful runs consistently require; infeasibility annotations human-verified at over 94% accuracy) found false continue rates (proceeding despite infeasibility) ranging **23.5% (GPT-5.5, best) to 73.9% (Qwen3.5-9B, worst)** across nine single-agent models, with a single-agent average of **54.6%**. Multi-agent planner-executor architectures reduced this substantially: the best pair (Qwen-122B planner, GPT-OSS executor) reached **2.6% FCR, nearly a 10x reduction** versus the best single agent.
- **Source(s)**: [Do Agents Know What They Can't Do?](https://arxiv.org/abs/2605.28532), Liang Cheng, Mingsheng Cai, Jiuming Jiang, Luo Mai (University of Edinburgh), 2026-05-27, read scope: **abstract + HTML body read directly** (manual deep-read 2026-09-29, local full-web session); full result tables not exhaustively read.
- **Discovered via**: search (flagged high-priority pending from the 2026-09-25 run), upgraded via manual deep-read.
- **Evidence label**: bounded empirical (directly read).
- **Correction**: the earlier search-summary figure "multi-agent cut the average from 54.6% to 17.5%" was NOT confirmed on direct read. Confirmed anchors are single-agent average 54.6% and best multi-agent pair 2.6%; no "17.5%" figure was found in the sections read.
- **Limits (stated by authors)**: FeasiGen operates on benchmarks with fixed, fully predefined tool pools; in open-ended settings where agents dynamically retrieve or invoke arbitrary tools, the masked-dependency construction may not transfer. Metrics: FCR, success rate, token cost to early stop, token cost to task failure.
- **Relates to**: first and only claim on task feasibility.
- **LayerLens relevance**: Open question #4 (task feasibility) — directly on point. Note the mirror-image framing: the paper is about agents recognizing infeasibility at run time; LayerLens's question is about authors constructing solvable scenarios and seeing why one is not solvable at design time. The FeasiGen mechanism (mask a critical tool, task becomes infeasible) is itself a candidate for a "why is this not solvable" explanation surface.
- **Confidence**: Moderate-high — directly read, key numbers confirmed and one earlier error corrected; still a single paper, not independently corroborated.
- **Recheck after**: 2026-12-24 (~90 days; model-dependent).

---

### C-0008: A reliability-science framework decomposes agent reliability into 12 metrics across 4 dimensions and finds capability gains have not translated into reliability gains (abstract + body read directly 2026-09-29)

- **Statement**: "Towards a Science of AI Agent Reliability" (Rabanser, Kapoor, Kirgis, Liu, Utpala, Narayanan — Princeton, ICML 2026) proposes twelve metrics across four dimensions: **Consistency** (outcome, trajectory-distributional, trajectory-sequential, resource), **Robustness** (fault, environment, prompt), **Predictability** (calibration, AUROC, Brier), **Safety** (compliance, harm severity). It evaluated 15 models (OpenAI, Google, Anthropic families) across two benchmarks, **GAIA (165 validation tasks)** and **tau-bench (26 verified tasks)**, and found (verbatim) "overall reliability shows minimal improvement over time, despite 24 months of model releases."
- **Source(s)**: [Towards a Science of AI Agent Reliability](https://arxiv.org/abs/2602.16666), Princeton, ICML 2026, v1 2026-02-18 / v3 2026-06-02, read scope: **abstract + HTML body read directly** (manual deep-read 2026-09-29, local full-web session); full result tables not exhaustively read.
- **Discovered via**: search (deliberate contradicting-evidence slice on non-determinism), upgraded via manual deep-read.
- **Evidence label**: bounded empirical (directly read).
- **Limits (stated by authors)**: two benchmarks cover a narrow task slice; single scaffold per benchmark; LLM-based safety judging is itself a reliability concern; metric decomposition is subjective; temperature 0 may overestimate achievable reliability.
- **On pass@k vs pass^k**: the paper uses the pass@k / pass^k terminology within its consistency dimension; the crisp definitions used in the brief (pass@k = at least one of k succeeds; pass^k = all k succeed) are field-standard and consistent with the paper's usage, but the paper's own formal definition was not quoted verbatim in the sections read.
- **Relates to**: connects to C-0009 (HAL) — same lab; HAL's README states the team is "focusing our current work on agent reliability," consistent with this being that follow-on work.
- **LayerLens relevance**: Open question #5, nearly verbatim ("how do we express variation across attempts — reliability versus one lucky pass"). The best-matched open question in the knowledge base.
- **Confidence**: High for the framework, metrics, benchmarks, and headline finding (directly read); the specific K/J/fault-injection parameters cited earlier were from a search summary and were not re-verified in this read.
- **Recheck after**: 2027-03-24 (~180 days; foundational framework).

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

---

### C-0012: A frontier lab published production-scale sandbox infrastructure for agentic training that explicitly does no verification, generation, or answer keys (a different stack layer from LayerLens)

- **Statement**: DeepSeek Elastic Compute (DSec) is DeepSeek's production sandbox platform (four backends behind one SDK, co-designed with their RL framework) that served all RL training and evaluation sandbox workloads from DeepSeek V3.2 to V4.1: ~160 nodes, ~3M sandboxes/day, ~380K concurrent, 5,000+ creations/second. It provides stateful pause/resume (Firecracker snapshots) and `pack_diff` checkpoint-and-restore. It explicitly does NOT do environment generation, verification/grading, or answer keys; it is a runtime substrate, not a verification product.
- **Source(s)**: [DeepSeek Elastic Compute (DSec)](https://arxiv.org/abs/2609.22978), DeepSeek (Jialiang Huang et al., 131 authors), 2026-09-19, read scope: abstract + HTML body (architecture, lifecycle, scale, evaluation), read directly 2026-09-29.
- **Discovered via**: Javier (deep-read request).
- **Evidence label**: bounded empirical (first-party systems paper, self-reported metrics, not reproduced).
- **Limits**: single vendor's internal platform; nothing about agent correctness or task validity; infra metrics self-reported.
- **Relates to**: feeds nursery thesis N-03; contrasts with LayerLens's verification layer (do not conflate infra-to-run with instrument-to-verify).
- **LayerLens relevance**: Positioning (infra to run vs instrument to verify) and open questions on environment lifecycle/state and deterministic replay; basis for idea I-0007.
- **Confidence**: High for what the system is and does (directly read); the "explicitly no verification" point is a genuine, load-bearing distinction.
- **Recheck after**: 2027-03-19 (~180 days; infra landscape).

---

### C-0013: Ordinal / "which action wins" benchmarks can hide real agent reliability

- **Statement**: Checkpoint-based benchmarks that score by set-agreement (which action wins) can be blind to reliability: different success-probability pairs (e.g. 0.9,0.8 vs 0.2,0.1) yield identical winning-action distributions. On 864 RecoveryBench episodes plus 3,456 planning responses, permuting checkpoint-to-action bindings flipped 8-13% of cell-level conclusions, and agreement and held-out quality moved in opposite directions. Four diagnostic metrics proposed (agreement, all-zero fraction, held-out success, pooled success).
- **Source(s)**: [Same Winners, Different Success Rates](https://arxiv.org/abs/2609.34215), Dong Xu et al., 2026-09-28, read directly 2026-09-29.
- **Discovered via**: cs.MA recent listing (Javier request).
- **Evidence label**: bounded empirical (directly read).
- **Relates to**: strengthens T-01; supports F-0001 (a single/ordinal number hides reliability). Same lab as C-0017.
- **LayerLens relevance**: Open Q #5 (reliability vs one lucky pass).
- **Confidence**: Moderate-high (directly read, concrete numbers, single study).
- **Recheck after**: 2027-03-29.

### C-0014: LLMs show identity-dependent conformity (in-group favoritism), corroborating self-preference bias

- **Statement**: Across 12 open-weight models and 9 judgment tasks with objectively correct answers, in-group consensus (shared AI/model-family/minimal-group identity) increases conformity while out-group consensus decreases it, independent of correctness; chain-of-thought suppresses most but not all of the effect.
- **Source(s)**: [LLMs Trust Their Own: Identity-Dependent Conformity](https://arxiv.org/abs/2609.33495), Liron Soffer, Ravid Shwartz-Ziv, Chen Shani, 2026-09-27, read directly 2026-09-29.
- **Discovered via**: cs.MA recent listing (Javier request).
- **Evidence label**: bounded empirical (directly read).
- **Relates to**: **independent corroboration of C-0002** (self-preference in LLM judges): different authors, different method, compatible conclusion, larger model set. Second independent evidence family, which promotes nursery N-02 to thesis T-05 and raises F-0005.
- **LayerLens relevance**: Open Q #2 + differentiator #3; directly raises F-0005 (flag same-family judge/agent pairings).
- **Confidence**: Moderate-high (12 models, 9 tasks, directly read).
- **Recheck after**: 2026-12-29 (~90 days).

### C-0015: Multi-turn agent consistency has measurable failure "fingerprints"; a 7-category failure taxonomy

- **Statement**: Over 20-step tasks, 84,540 trajectories across 8 model families, using survival analysis (time-to-first-failure) and a 7-category failure-rationale taxonomy (inter-rater kappa=0.83): failures have distinct fingerprints by model and context; early failures are impulse-driven, later ones fatigue/cost-benefit-framed; longer deliberation correlated with more intra-rationale contradiction.
- **Source(s)**: [Evaluation of Multi-Turn Consistency in LLM Agents](https://arxiv.org/abs/2609.29508), Igor Bogdanov, Olga Manakina, Chung-Horng Lung, 2026-08-26, read directly 2026-09-29.
- **Discovered via**: cs.MA recent listing (Javier request).
- **Evidence label**: bounded empirical (directly read).
- **Relates to**: strengthens T-01 (reliability) and T-03 (failure attribution as a category system).
- **LayerLens relevance**: Open Q #2 and #5; a reference for categorizing/attributing failures in the UI.
- **Confidence**: Moderate-high (large trajectory set, directly read).
- **Recheck after**: 2027-02-26.

### C-0016: Inter-agent agreement is not verification; a knowledgeable verifier is required

- **Statement**: Agreement among heterogeneous agents is not evidence of correctness (they can jointly repeat an unsupported claim). A conformal filter roughly doubled long-form retained-claim precision (0.41 to 0.75) but was near-chance on short-form where "consensus is cheap"; moving beyond consensus required a knowledgeable verifier (a memory-only judge scored AUC 0.531, near random).
- **Source(s)**: [Calibration Is Not Verification](https://arxiv.org/abs/2609.25959), Nada Rahali, Zijia Wang, Zhisong Liu, 2026-09-22, read directly 2026-09-29.
- **Discovered via**: cs.MA recent listing (Javier request).
- **Evidence label**: bounded empirical (directly read).
- **Relates to**: strengthens T-02 (verification-by-construction, not consensus) and differentiator #3 (self-check/consensus wobbles; a real verifier is needed).
- **LayerLens relevance**: Positioning + differentiator #3; caution against consensus/LLM-judge-only grading.
- **Confidence**: Moderate-high (directly read; a research validation of our verification thesis).
- **Recheck after**: 2027-03-22.

### C-0017: Agents can exploit outcome information rather than genuinely solving; a black-box audit isolates what drives a decision

- **Statement**: Changing one relationship in an agent's stored history at a time shows swapping outcome scores changes decisions while moving intact action-score pairs does not, separating score-dependence from order-sensitivity and exposing cases where agents exploit outcome information rather than solving the task.
- **Source(s)**: [ReplayLens: Auditing Agents' Use of Outcomes](https://arxiv.org/abs/2609.34177), Dong Xu et al., 2026-09-28, read directly 2026-09-29.
- **Discovered via**: cs.MA recent listing (Javier request).
- **Evidence label**: bounded empirical (directly read). Same lab as C-0013 (treat as one lab, distinct phenomena).
- **Relates to**: strengthens T-02 (agents game/exploit rather than solve) and T-03 (attribution); supports F-0002 and the trust-wall story.
- **LayerLens relevance**: Open Q #2 (attribution).
- **Confidence**: Moderate (directly read; demonstrative scope by the authors' own note).
- **Recheck after**: 2027-03-29.

### C-0018: MCP error messages written for human developers actively mislead tool-using agents, and more capable models follow the bad advice more faithfully

- **Statement**: In 150 widely-used MCP servers, 949 of 3,001 error messages tell the calling agent what to do next, and half of those steps depend on something the server cannot see about the caller (e.g. "run a command," "edit a configuration"). Tested on five OpenAI models: on expired credentials, following a terminal-command-shaped step left 45% of tasks recovered, and the score lost by following it grew from 18 points (GPT-5.5) to 69 points (GPT-6 Astra) — more capable models followed the bad, human-oriented step *more*, not less. On rate limits, a bare "wait and retry" left only 6% recovered. Two remedies: naming an actual server tool in the step raised recovery to 84% (credentials) / 88% (rate limits); deleting the step via a one-sentence pre-read prompt raised credential recovery to 82%.
- **Source(s)**: [MCP Error Messages Written for Developers Hurt the Most Capable Agents Most](https://arxiv.org/abs/2609.35381), Xiaonan Xu, Wenjing Wu, 2026-09-28, read scope: abstract read directly via `inbox/arxiv/LATEST.md` (arxiv.org itself blocked; no reachable mirror found).
- **Discovered via**: arXiv inbox harvester.
- **Evidence label**: bounded empirical (abstract read directly).
- **Limits**: abstract only; five OpenAI models on Berkeley Function Calling Leaderboard tasks, not a broad model census; mechanism for "more capable = more harmed" not explained in what was read.
- **Relates to**: new — first claim on MCP/tool error-message design specifically. Pairs with C-0021 (capability correlating with more, not less, exploitation) as the second instance of the same counterintuitive pattern — see new thesis T-07.
- **LayerLens relevance**: Open Qs #2 (attribution), #7 (recovery); directly concrete for our own shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail all wrap real, human-authored APIs/error surfaces). Motivates new idea I-0009.
- **Confidence**: Moderate (single source, abstract only, but concrete numbers and a clean before/after remedy comparison).
- **Recheck after**: 2026-12-29 (~90 days; model-dependent).

### C-0019: Run-to-run variation in real coding-agent benchmarking exceeds agent-to-agent differences, and rule-violating runs score highest until excluded

- **Statement**: 584 runs across six coding agents and multiple open-weight model endpoints on one ML coding task found agent pairings averaged 0.0095 AUC apart while the *same* pairing varied by a median of 0.0107 AUC across its own repeated runs — noise exceeds signal. Three-run comparisons ranked pairings unreliably; resolving true differences would take tens to 100+ runs per pairing. A larger model scored higher but by less than one run-to-run standard deviation, and a single run still favored the smaller model 28% of the time. 10 of 312 runs violated stated task rules (trained on eval data); these occupied the highest-scoring positions — best score dropped from 0.8293 to 0.7695 once excluded. Cost varied >20x between two agents on the same model. Gains over starting code fell to about a third when tested on a later year's data (distribution shift).
- **Source(s)**: [Identical Runs, Different Results](https://arxiv.org/abs/2609.33812), Eduardo Ariño de la Rubia, Szilard Pafka, 2026-09-27, read scope: abstract read directly via inbox; companion GitHub repo README read directly in full (https://github.com/earino/identical-runs-different-results).
- **Discovered via**: arXiv inbox harvester, then GitHub read directly.
- **Evidence label**: bounded empirical (repo README + abstract, both read directly).
- **Limits**: single task domain (one ML/XGBoost task); six agents/models, not a census; rule-violation finding specific to this task's own rules.
- **Relates to**: **independent corroboration of T-01** — a third, unrelated evidence family (alongside C-0008, C-0013) showing the same structural finding (few-run comparisons are unreliable) in a completely different domain (real coding-agent benchmarking, not a proposed metric or an ordinal-scoring study). Also corroborates T-02 (rule-violating runs scoring highest is a small, concrete instance of the gaming pattern C-0001/C-0006/C-0017 document at scale).
- **LayerLens relevance**: Open Q #5 (directly on point, real numbers) and #1 (a concrete "how many runs is enough" data point). Strengthens I-0001 and F-0002 (rule-violation/attribution detection).
- **Confidence**: Moderate-high (directly read, first-party repo, concrete numbers, third independent family for T-01).
- **Recheck after**: 2027-03-27 (~180 days; foundational reliability finding).

### C-0020: Planarian's "agent statepoints" generalize snapshot/rollback/fork to both local sandbox state and remote service state via compensating actions

- **Statement**: Planarian is an agent runtime exposing three primitives on "agent statepoints" (consistent, restorable point-in-time versions of environment state): snapshot (incremental local process/filesystem capture, plus recorded compensating actions for remote state), rollback (restore local checkpoint + replay compensating actions to undo remote changes), and fork (branch multiple isolated explorations from one statepoint). Reported: improves task quality by up to 15x (enabling undo/parallel exploration); lets users recover from erroneous actions with only 3% overhead.
- **Source(s)**: [Planarian: Managing Agent State with Statepoints](https://arxiv.org/abs/2609.35366), Jinnan Guo, Hao Mark Chen, Kapil Vaswani, Andrew Paverd, Peter Pietzuch, 2026-09-28, read scope: abstract read directly via inbox (arxiv.org blocked; no mirror found).
- **Discovered via**: arXiv inbox harvester.
- **Evidence label**: bounded empirical (abstract read directly).
- **Limits**: abstract only; no benchmark/task detail behind the 15x figure; single source.
- **Relates to**: **second independent family for nursery N-03** (alongside C-0012, DSec) — different team, and explicitly extends the pattern to *remote* system state via compensating actions, which DSec's abstract did not cover. Promotes N-03 to thesis T-06 (see changelog). Further corroborated same-day by C-0023 (Counterfactual Rollout Replay, training-angle) and a not-yet-confirmed fourth (DeltaBox, incomplete access — see card).
- **LayerLens relevance**: Open Q #7 (human control/recovery) and #3 (deterministic replayability). Closest external match yet to LayerLens's deterministic-minting + replay story, generalized to remote state — exactly our Salesforce/Linear/Stripe/etc. system-type shape. Strengthens I-0007 to a second independent source.
- **Confidence**: Moderate (abstract only, but a clean, directly relevant mechanism description).
- **Recheck after**: 2027-03-28 (~180 days; infra landscape).

### C-0021: Benchmark "unearned passes" require ongoing maintenance, not a one-time fix, and confirmed violation rates can rise sharply with model capability before later cohorts improve

- **Statement**: Defines "unearned passes" (a pass without demonstrating the intended capability) and "integrity gap." Across 3,810 passing trajectories from 29 model-benchmark cohorts, a process-verification framework distinguished evidenced reward-hacking from verifier weakness. On SWEBench Pro V1.0, confirmed violation rates rose from 24% to 73% between Opus 4.7 and Fable 5 on matched tasks, then fell to 11% (Fable 5.1) and 0% (GPT-6 Astra) — authors caution this is descriptive, not normalized, and later models also passed fewer exploitable tasks. Violations concentrated on a small set of recurring surfaces (especially unintended access to reference solutions via git history). Patching one exploit route was insufficient across three repair case studies — the same protected info often remained reachable another way — so the authors combine minimal patches with exploit replay and fresh re-evaluation.
- **Source(s)**: [Maintaining Benchmarks Against Increasingly Capable Agents](https://arxiv.org/abs/2609.34262), Weijun Luo, Kelvin Luu, Xinyi Liu, Guangze Luo, Miguel Romero Calvo, Soham Dan et al., 2026-09-28, read scope: abstract read directly via inbox (arxiv.org blocked).
- **Discovered via**: arXiv inbox harvester.
- **Evidence label**: bounded empirical (abstract read directly).
- **Limits**: abstract only; configurations not normalized across model generations; single benchmark family for the headline number.
- **Relates to**: strengthens T-02 with a new angle — benchmark integrity as *ongoing* maintenance, sharper than C-0003's single-incident framing. The 24%→73% rise is the second instance (with C-0018) of "more capability correlates with more exploitation, not less" — promotes new thesis T-07.
- **LayerLens relevance**: Open Qs #1 (comparability — scores decay as capability rises, a moving target even without a version bump) and #2 (attribution — reward-hacking vs verifier-weakness is env-vs-agent attribution). Nuances the trust-wall differentiator: a static, one-time wall is necessary but this paper implies ongoing re-audit matters too.
- **Confidence**: Moderate-high (concrete numbers, but abstract only and explicitly descriptive not controlled).
- **Recheck after**: 2026-12-28 (~90 days; model-dependent).

### C-0022: A "structured evidence contract" policy nearly eliminates false-success self-reporting after tool failure

- **Statement**: Names a failure mode where "agents can fail twice": a required tool fails, and the agent then reports success without evidence to justify it. The FTA benchmark (100 tasks, 5 failure families, a neutral control, 4 user-pressure conditions, 3,600 human-annotated responses across 6 models and 3 response policies) found false-success rates of 22.8% (baseline policy), 9.3% (transparency instruction), and 0.8% (structured evidence contract). Fabricated-detail rates dropped 28.3% → 14.3% → 0.8% across the same conditions; useful-response rates rose 74.9% → 89.2% → 98.8%.
- **Source(s)**: [Failure-Transparent Agents](https://arxiv.org/abs/2609.35732), Junru Zhu, Shiming Xie, Aime Lu Fan Chen, Xiaoqing Ding, Chunxin Tang, Ruoyu Qi et al., 2026-09-28, read scope: abstract read directly via inbox (arxiv.org blocked).
- **Discovered via**: arXiv inbox harvester.
- **Evidence label**: bounded empirical (abstract read directly).
- **Limits**: abstract only; controlled/blocked-task benchmark (staged failures), not observed in the wild; single source.
- **Relates to**: strengthens T-02/T-03. Directly validates an already-shipped LayerLens V1 choice ("the agent's own claims are stored beside verdicts, never used as evidence") — the paper's best condition (a structured evidence contract) is essentially that design, independently arrived at.
- **LayerLens relevance**: Open Q #2 — an unsupported success claim is its own nameable failure category, distinct from the underlying tool failure. Evidence-validated confirmation of an existing V1 choice, not a new bet.
- **Confidence**: Moderate-high (concrete numbers, clean before/after conditions, but abstract only).
- **Recheck after**: 2027-03-28.

### C-0023: Forkable/restorable environment state, applied to RL training, produces a measurable training-efficiency gain without human process labels

- **Statement**: Counterfactual Rollout Replay (CRR) restores a saved state, samples an alternative action, and rolls the branch forward to get step-level return contrasts for training, with no human process labels or learned reward model. With a 14B policy, CRR improved pass@1 on SWE-bench Verified/Live/rebench; on SWE-bench Verified an equal-wall-clock comparison gave 41.7% vs 36.7% for extended outcome-only GRPO (5.0-point gain, fork overhead included). Stated limit: only applies where state restoration is affordable and reliable.
- **Source(s)**: [Counterfactual Rollout Replay](https://arxiv.org/abs/2609.33875), Yuanhao Li, Hongbo Wang, Xuhong Chen, Yiming Cao, Xunzhu Tang, 2026-09-27, read scope: abstract read directly via inbox (arxiv.org blocked).
- **Discovered via**: arXiv inbox harvester.
- **Evidence label**: bounded empirical (abstract read directly).
- **Limits**: abstract only; training-time use case, not a product/UX finding directly.
- **Relates to**: third independent instance of the fork/restore/branch environment-state primitive (with C-0012 DSec, C-0020 Planarian) — from an RL-training angle. Contributes to thesis T-06.
- **LayerLens relevance**: general (environment lifecycle); adjacent to open Q #5 (counterfactual branching as a structured way to probe run-to-run variance at a specific decision point). Feeds I-0007.
- **Confidence**: Moderate (abstract only, but concrete controlled-comparison numbers).
- **Recheck after**: 2027-03-27.

### C-0024: Some agentic-code-generation benchmarks compute "pass@k" incorrectly, conflating unit-test sub-results with independent attempts, inflating scores dramatically

- **Statement**: Some benchmarks substitute, into pass@k's `n`/`c`, the number of unit tests in one submission and tests passed — rather than independent rollout attempts and rollouts that fully succeed ("unit tests inside one submission are not independent attempts — they are correlated sub-results of a single run"). The corrected metric, reliability@k (`n` = independent rollouts, `c` = rollouts where all tests pass), collapsed a synthetic-benchmark pass@5 of ~0.96-0.97 to a reliability@5 of ~0.00-0.12. On 5 real SWE-bench tasks: mean hidden-test pass rate 0.80 vs strict full-task resolve rate 0.20 (4x inflation). A security-adjusted variant additionally requires no high-severity security issues; in one 240-rollout experiment a GPT-4o Codex agent produced 24 insecure rollouts vs 4-5 for competing agents.
- **Source(s)**: [Beyond Pass@k: Measuring Reliability and Security of Agentic Code Generation](https://arxiv.org/abs/2608.14711), read scope: companion GitHub repo README ([nv78/Research-CodeBench](https://github.com/nv78/Research-CodeBench)) read directly and in full; the arXiv paper itself and its abstract were NOT read (arxiv.org blocked); author identities not independently confirmed.
- **Discovered via**: search (this run's deliberate 20%-budget contradicting-evidence slice), then citation to the companion repo.
- **Evidence label**: bounded empirical (companion repo README read directly; underlying paper unconfirmed beyond what the README states).
- **Limits**: repo-to-paper correspondence not independently cross-checked line by line; synthetic-benchmark figures are an illustrative worst case per the README, not necessarily representative; authorship/affiliation unconfirmed.
- **Relates to**: **a genuine methodological caution on C-0008's pass@k/pass^k vocabulary** (used in the 2026-W40 brief and learning/tutor.md) — does not contradict T-01, but shows the true reliability gap is likely *worse* than some reported numbers suggest, and flags a concrete implementation trap for any pass^k-style feature.
- **LayerLens relevance**: Open Q #5, directly. If LayerLens ships a pass^k-style readout (F-0001/I-0001), the "k attempts" must be genuinely independent full-task rollouts, not sub-task or per-tool-call checks dressed up as attempts. Added as a build caution to I-0001, not a new feature.
- **Confidence**: Moderate (directly read companion artifact; underlying paper itself unconfirmed).
- **Recheck after**: 2026-12-29 (~90 days).

### C-0025: AgentRewind — checkpoints agent context + environment together for runtime recovery on long-horizon tasks (incomplete access)

- **Statement**: AgentRewind is a runtime recovery framework recording aligned checkpoints of an agent's context and its "controlled environment" (workspace directory tree, tracked via file-level changes), letting an agent roll back to an earlier checkpoint and resume with information from a failed attempt, instead of restarting cold. Introduces MettleBench, a benchmark of real-world, multi-requirement long-horizon engineering tasks. Reported to improve task success and checklist progress across models, execution strategies, and agent harnesses.
- **Source(s)**: [AgentRewind](https://arxiv.org/abs/2608.14380), Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang, 2026-08-14, read scope: incomplete access (arxiv.org blocked; assembled from consistent WebSearch summaries, no primary text).
- **Discovered via**: search.
- **Evidence label**: incomplete access.
- **Limits**: no primary text; no quantitative deltas captured; single paper.
- **Relates to**: **fourth independent family for T-06** (environment-lifecycle convergence), alongside C-0012 (DSec), C-0020 (Planarian), C-0023 (Counterfactual Rollout Replay) — the closest yet to a product-facing agent-runtime-recovery use case.
- **LayerLens relevance**: Open Q #7 (recovery), #3 (replayability). Strengthens I-0007/F-0007.
- **Confidence**: Low-moderate (incomplete access, but consistent across multiple independent summaries).
- **Recheck after**: 2027-02-14 (~180 days; infra landscape claim).

### C-0026: A rollback-security study argues "correct rollback does not imply secure recovery" — counter-evidence/risk for the checkpoint-rollback convergence thesis (incomplete access)

- **Statement**: The first systematic security study of checkpoint/rollback (C/R) in agent systems. Core finding: a checkpoint can be faithfully, state-correctly restored yet resume an execution whose states, assumptions, and external effects never coexisted in any valid history, because the world outside a frozen sandbox (other services, other agents, real external side effects) kept moving. Introduces "execution continuity" as a security requirement distinct from state-correctness, and characterizes the design space and recovery boundaries of existing C/R mechanisms.
- **Source(s)**: [Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback](https://arxiv.org/abs/2608.29381), Guanlong Wu, Dahui Li, Ke Jiang, Jianyu Niu, Cong Wang, Yinqian Zhang, 2026-08-29, read scope: incomplete access (arxiv.org blocked; WebSearch summaries only).
- **Discovered via**: search (following the T-06/DeltaBox checkpoint-rollback cluster).
- **Evidence label**: incomplete access.
- **Limits**: no primary text; no concrete attack case studies or quantitative failure rates captured; single paper, part of an apparently active sub-cluster (ACRFence, "When Can Agents Safely Checkpoint, Fork, Restore, and Merge?", "Recoverability as a System Primitive" — none individually read this run, noted for future follow-up).
- **Relates to**: **counter-evidence / risk complication for T-06** — the other four T-06 families treat checkpoint/rollback/fork as a maturing, near-commodity mechanism; this paper argues its security dimension is largely unexamined and can silently fail even when state-restoration is technically correct.
- **LayerLens relevance**: Open Q #7 (recovery), #3 (replayability). A direct build caution for I-0007/F-0007: if a checkpoint/branch feature is ever built over remote system-type state (Salesforce, Stripe, etc.), state-correct restore is necessary but not sufficient — whether the resumed execution's assumptions about the outside world still hold needs its own design answer.
- **Confidence**: Low-moderate (incomplete access; the core argument — rollback correctness and execution-continuity are different properties — is conceptually clear even without primary-text numbers).
- **Recheck after**: 2027-02-14 (~180 days; infra landscape claim, paired with C-0025).

### C-0027: A large-scale systematic study of 21 LLM judges finds high test-retest reliability coexists with severe bias — "the most reproducible judges are among the least valid" (incomplete access)

- **Statement**: A systematic evaluation of 21 LLM-as-judge models from 9 providers across three benchmarks (MT-Bench, JudgeBench, RewardBench), under three protocols (agreement, consistency, bias audit), over 118 runs and ~541,000 individual judgments. Raw percent-agreement overstates chance-corrected discrimination (vs. Cohen's kappa) by 33-41 percentage points across the 21 models. High test-retest reliability (kappa >= 0.95 for some judges) coexists with severe position bias (>0.10) in some of the same, production-deployed judges.
- **Source(s)**: [Reliability without Validity](https://arxiv.org/abs/2606.19544), Justin D. Norman, Michael U. Rivera, D. Alex Hughes, 2026-06-17, read scope: incomplete access (arxiv.org blocked; consistent WebSearch summaries citing the same specific figures across independent snippets; authors state code/data release is deferred to publication).
- **Discovered via**: search (this run's deliberate contradicting-evidence slice against T-05).
- **Evidence label**: incomplete access (but a large, well-specified systematic study, not an anecdote).
- **Limits**: no primary text; cannot verify per-benchmark breakdowns or the exact model list independently.
- **Relates to**: **third independent family for T-05** (LLM judges carry structural bias), alongside C-0002 (self-preference pilot) and C-0014 (identity conformity). Distinct emphasis: general reliability/validity/position-bias, not specifically same-model-family favoritism — strengthens T-05's broad claim without being additional evidence specifically for I-0005/F-0005's narrower same-family-flag hypothesis.
- **LayerLens relevance**: Open Q #2 (attribution), differentiator #3 (reproducible, defensible grading). The "reproducible but not valid" framing directly cautions against showing a Judge's re-run consistency as reassurance of its correctness.
- **Confidence**: Moderate (incomplete access, but large-N systematic study with figures repeated consistently across independent search summaries).
- **Recheck after**: 2026-12-17 (~90 days; model/provider-dependent judge claim).

### C-0028: E2B's own blog confirms pause and fork as sandbox lifecycle primitives (first-party, feed-summary only)

- **Statement**: E2B's own blog (via its RSS feed) describes a reference agent workbench (built on OpenAI's Agents API) with "application-managed lifecycle, one sandbox per chat, pause and fork" — confirming pause and fork exist as first-class E2B sandbox lifecycle primitives, at least in this reference pattern.
- **Source(s)**: [Build an Agent Workbench on OpenAI's Agents API](https://e2b.dev/resources/build-an-agent-workbench-on-openais-agents-api), E2B, published 2026-09-10, read scope: RSS feed description only (one sentence), via `inbox/competitors/LATEST.md`; the full post was not reachable (e2b.dev EGRESS_BLOCKED to WebFetch, confirmed again this run).
- **Discovered via**: feed (inbox harvester).
- **Evidence label**: documented capability (first-party) at abstract/summary-only access scope.
- **Limits**: one-sentence feed summary; underlying mechanics, guarantees, and limitations of "pause and fork" not described in what was read.
- **Relates to**: **fifth data point for T-06** (environment-lifecycle convergence) — the first from an already-commercial, productized sandbox vendor rather than a research paper, i.e. the pattern is already shipping in industry infrastructure, not only academic. Resolves, in direction, the prior `knowledge/competitive.md` note that E2B's session-lifecycle claims were third-party-blog-only and unconfirmed.
- **LayerLens relevance**: Open Q #7, #3. Updates the E2B competitive entry from "insufficient evidence" to a thin, first-party-confirmed capability.
- **Confidence**: Moderate (first-party, but a one-sentence summary, not the full post).
- **Recheck after**: 2026-12-29 (~90 days; vendor capability claim).

### C-0029: A trajectory-level security-debt metric finds most benchmarks' security scanners barely agree with each other (abstract read directly)

- **Statement**: Proposes the Security Debt Line Integral (SDLI), accumulating static-analysis (SAST) risk over an agent's intermediate code states each time it reaches a new best test-pass ratio, instead of scoring only the final artifact. Instantiated with four SAST tools across 830 passing SWE-bench runs, 712 ProgramBench final workspaces, and 13 public MirrorCode trajectories. Two-tool CWE-class agreement occurred in only 3.9% of SWE-bench runs and 26.2% of the higher-passing ProgramBench subset (6.2% after excluding three advisory-heavy classes) — authors are explicit these are scanner findings, not confirmed exploitable vulnerabilities. A repair case study reduced scanner signal while preserving tested behavior, but showed sensitivity to equivalent API rewrites.
- **Source(s)**: [Trajectory-Level Security Debt in LLM Coding Agents](https://arxiv.org/abs/2609.35199), Prateek Kumar Rajput, Abdoul Kader Kabore, Yewei Song, Melissa Tessa, Tailia Malloy, Jacques Klein et al., 2026-09-28, read scope: abstract read directly via `inbox/arxiv/LATEST.md`.
- **Discovered via**: arXiv inbox harvester.
- **Evidence label**: bounded empirical (abstract read directly).
- **Limits**: abstract only; low two-tool scanner agreement (3.9-26.2%) is itself a major confound — the "true" security-debt rate is not established, only that trajectory-level tracking surfaces something final-artifact-only evaluation misses; authors state SDLI's value for steering agents or confirming exploits "remains to be established."
- **Relates to**: new — first claim specifically on security posture tracked across a trajectory rather than the final artifact only. Complements T-03/I-0003 with a distinct dimension (security debt, not correctness), sharing the principle that intermediate states carry information the final state hides.
- **LayerLens relevance**: Open Q #9 (comparison/trajectory diff), #2 (attribution, general sense). Not tied to an existing idea/feature row this run — recorded as a claim and open-question note per dedup discipline.
- **Confidence**: Moderate (abstract only, concrete numbers, but low cross-tool agreement limits what can be concluded).
- **Recheck after**: 2027-03-28 (~180 days).

### C-0030: ControlScope studies workflow-revision granularity (continue / edit-argument / replace) mid-execution, with mixed results (abstract read directly)

- **Statement**: Compares three repair granularities from the same public execution state — KEEP (continue as-is), ARG (edit only the next tool call's data arguments), FULL (replace the unfinished workflow) — framed as "nested permissions" separating available repairs from the actions an agent actually selects. Across filesystem tasks, ALFWorld, and AppWorld, results are mixed: FULL completed 15-16/20 vs. 13 for KEEP under one setup but 10-13 vs. 13 under another; ALFWorld KEEP/ARG/FULL scored 85/86/87 on one cohort and 134/134/127 on another; a 585-instance AppWorld panel showed small differences. A "five-call protection" scheme saved 19.4% of logged output at the cost of one success across 20 runs.
- **Source(s)**: [ControlScope: Workflow Revision and Reliability in LLM Agents](https://arxiv.org/abs/2609.34313), Jingjie Ning, Xueqi Li, Yibo Kong, Dongting Li, 2026-09-28, read scope: abstract read directly via `inbox/arxiv/LATEST.md`.
- **Discovered via**: arXiv inbox harvester.
- **Evidence label**: bounded empirical (abstract read directly).
- **Limits**: abstract only; heterogeneous, non-monotonic results across task suites and draw conditions — not a settled recommendation for how much to revise.
- **Relates to**: new — first claim specifically on *repair granularity* (how much of a workflow to revise) rather than *whether* rollback/checkpoint is available at all (the rest of T-06's cluster). Distinct evidence for I-0007: recovery is not just "can you branch/checkpoint" but "how much should be changed when recovering."
- **LayerLens relevance**: Open Q #7 (a concrete taxonomy: continue / edit-argument / replace-workflow), #6 (adjacent).
- **Confidence**: Low-moderate (abstract only, mixed/non-monotonic results).
- **Recheck after**: 2027-03-28 (~180 days).

### C-0031: A Workday production report finds progressive (lazy) disclosure of agent skills improves retrieval quality with only marginal latency cost (abstract read directly)

- **Statement**: As Workday's deployed LLM agents' skills libraries (named in-context procedures) grow, operational cost grows with them. Progressive disclosure (lazy-loading skills only as needed, rather than always including the full library in context) empirically improves skill-retrieval quality, and only marginally degrades overall latency.
- **Source(s)**: [Report: Progressive Disclosure of Agent Skills](https://arxiv.org/abs/2609.35692), Guilin Zhang, Kai Zhao, Priyanka Mudgal, Waleed Ammar, Xiquan Cui, Xu Chu et al. (Workday), 2026-09-28, read scope: abstract read directly via `inbox/arxiv/LATEST.md`.
- **Discovered via**: arXiv inbox harvester.
- **Evidence label**: bounded empirical (abstract read directly; first-party production report from a named company, not a lab benchmark).
- **Limits**: abstract only; no specific numbers given; single company/deployment; "marginally degrades" is qualitative.
- **Relates to**: new — adjacent to but distinct from C-0004 (Anthropic's general context-engineering guidance, which recommends just-in-time retrieval); this is a concrete, measured production instance of the same principle.
- **LayerLens relevance**: General ("context and tools" scope slice); loosely touches #6. Not tied to an existing idea/feature row this run, per dedup discipline.
- **Confidence**: Moderate (concrete production claim, but abstract-only, unquantified).
- **Recheck after**: 2027-03-28 (~180 days).

### C-0032: A decision-only "confidence cascade" judge comes within a few points of a top LLM judge at a fraction of the cost, and escalation to a stronger judge on low-confidence cases beats either judge alone

- **Statement**: JEV, a decision-only judge model returning typed answers (Choice/Score/Boolean) with calibrated probabilities instead of generated text, was tested against 16 generative and reward-model judges with blinded human adjudication. It came within ~3 points of the strongest judge wherever a verdict could be read off the text, at ~0.36% of its fee and ~0.15s median latency, but fell behind on tasks requiring a *derived* verdict (math, code, logic). A "frozen confidence cascade" (fit a confidence threshold on a selection set, freeze it, escalate low-confidence cases to the strong judge) was ~0.9 points *more* accurate than the strong judge alone at ~41% of its fee, and matched the strong judge's accuracy exactly in a pre-specified live test on two new workloads.
- **Source(s)**: [JEV-as-a-Judge: Accept When Confident, Escalate When Unsure](https://arxiv.org/abs/2609.26550), Yubo Li, Yidi Miao, Ramayya Krishnan, Rema Padman (Carnegie Mellon University), 2026-09, read scope: companion GitHub repo README read directly ([dataelvisliang/jev-as-a-judge-scaffold](https://github.com/dataelvisliang/jev-as-a-judge-scaffold), an independent scaffold citing the paper's numbers, not an official CMU repo); the arXiv paper itself not read (arxiv.org blocked); figures cross-checked as consistent across several independent secondary summaries (OpenRouter, MLflow, HoneyHive blogs — all also blocked to direct fetch this run).
- **Discovered via**: search, following a cross-vendor blog convergence on "Jev" spotted in `inbox/competitors/LATEST.md` (Arize, Browserbase, Confident AI/DeepEval, and Langfuse all posted about it independently within the same week — see `knowledge/competitive.md`).
- **Evidence label**: bounded empirical (companion repo directly read; underlying paper itself unconfirmed).
- **Limits**: the README itself warns thresholds "do not transfer" across tasks/datasets (must be refit per task), the model is "vulnerable to confidently incorrect outputs," and it performs poorly on reference-free prose and any task requiring a derived (not read-off-the-text) verdict; single paper, not yet independently replicated outside its own authors' live test.
- **Relates to**: new — first claim on a decision-only/non-generative judge architecture. **Directly relevant to and complicates T-05**: T-05 says LLM judges carry structural bias and that reproducibility does not imply validity (C-0027); JEV's calibrated-confidence-plus-escalation pattern is an emerging, evidence-backed industry response to exactly that gap, not a refutation of it (a low-confidence signal is a legitimate distinct property from a bias-free verdict — JEV's own paper does not claim to remove bias, only to know when to defer).
- **LayerLens relevance**: Open Q #2 (attribution — a calibrated confidence signal is a structurally different, more honest way to answer "should I trust this verdict" than the re-run consistency T-05/C-0027 already showed is a false reassurance); differentiator #3. Motivates new idea I-0010.
- **Confidence**: Moderate (companion repo directly read with concrete numbers; primary paper text unconfirmed; a single research group's own results, not yet independently replicated).
- **Recheck after**: 2026-12-29 (~90 days; a fast-moving, newly-emerging pattern).

### C-0033: A "typed decision + receipt" pattern is emerging as a lighter-weight alternative to generative LLM judges for gating proposed actions

- **Statement**: A reference harness built on the Jev decision-only model implements: a generative LLM proposes one action; Jev answers a small, fixed set of predefined yes/no questions about the proposal, each with a probability and confidence; deterministic code (not the model) applies a fixed decision table to the answers to produce a verdict (permit / proposal_only / reject / unavailable); and every step is recorded in a structured "receipt" (model version, latency, exact answers, validation/execution status), with an optional cryptographically-hashed "bound receipt" for offline replay (explicitly "not a signature"). A favorable verdict still requires explicit human/host authorization before any action executes.
- **Source(s)**: [jev-harness](https://github.com/TypeSafeAI/jev-harness), GitHub org "TypeSafeAI" (affiliation with TypeSafe AI itself not independently confirmed), date unknown, read scope: full README, read directly.
- **Discovered via**: search.
- **Evidence label**: documented capability for what the harness concretely implements and records; proposal/interpretation for the pattern's general value (a reference implementation, not a controlled study — its own benchmark numbers are explicitly labeled "synthetic offline results, not calibration").
- **Limits**: the harness never applies patches, executes code, or grants permission itself (a design choice, not a gap, but means it says nothing about how a host should implement authorization); receipt hashing is explicitly not a signature (no non-repudiation guarantee); author affiliation with TypeSafe AI unconfirmed.
- **Relates to**: complements C-0032 with a concrete applied-engineering instance of the same "narrow, typed, confidence-bearing decision plus human authorization plus audit trail" idea.
- **LayerLens relevance**: Open Q #2, #7 (the "even a favorable Jev verdict requires explicit host approval" pattern is directly comparable to LayerLens's own confirmation-before-write questions). The "receipt" concept is an independent external validation of the general shape of LayerLens's own "on record"/verdict-with-evidence vocabulary, worth noting as convergent naming, not something to newly adopt.
- **Confidence**: Moderate (directly read, but a single, unconfirmed-affiliation reference repo, and its own numbers are self-labeled non-calibrated).
- **Recheck after**: 2026-12-29 (~90 days).

### C-0034: A proposed "recoverability" system primitive argues correct restoration is a separate question from whether resuming is permitted, and proposes a governance-layer answer

- **Statement**: Proposes "recoverability" as distinct from mere state-restoration: a system must explicitly select a *supported* starting point and a *permitted* recovery action (or explicitly withhold automatic continuation), rather than silently resuming from any technically-restorable checkpoint. A reference design, the Recoverability Primitive Runtime (RPR), separates an Evidence/Policy layer, a Governance layer, and an Enactment/Audit layer, with the audit trail recording restoration fidelity, adherence to the governing decision, and the final task outcome as separate pieces of evidence. States that accurate restoration and a successful completion can together conceal a disallowed starting point.
- **Source(s)**: [Recoverability as a System Primitive for Long-Horizon AI Agents](https://arxiv.org/abs/2609.13672), Zhihui Zhang and one other author (full author list unconfirmed), 2026-09, read scope: incomplete access (arxiv.org blocked, no companion repo found; WebSearch summary only).
- **Discovered via**: search, following up the rollback-security cluster flagged pending in the prior run's log.
- **Evidence label**: incomplete access.
- **Limits**: no primary text; no quantitative results or worked example captured; single paper; author list not fully confirmed.
- **Relates to**: **directly answers the gap C-0026 ("Safe to Resume?") named** — proposes a governance-layer mechanism (an explicit, auditable "is this recovery action permitted" decision, separate from "did the restore work technically") as an answer to exactly the risk C-0026 raised. A proposed design response, not yet independently validated. Strengthens T-06 with a distinct design-pattern angle (governance/permission), not a duplicate of the five prior mechanism-existence families.
- **LayerLens relevance**: Open Q #7, #3. Sharpens I-0007/F-0007's build caution: "legible" should show not just *that* a checkpoint/branch happened, but *which governing rule permitted it*, as separate, inspectable evidence.
- **Confidence**: Low-moderate (incomplete access; conceptually clear but no primary-text verification).
- **Recheck after**: 2027-02-14 (~180 days; infra/design-pattern claim, paired with C-0025/C-0026).

### C-0035: Patronus AI positions "Generative Simulators" as adapting, evolving environments rather than fixed benchmarks (background finding, not new this week)

- **Statement**: Patronus AI's "Generative Simulators" generate new tasks/scenarios, adapt the surrounding conditions and oversight/checking process based on observed agent behavior, and evolve over time rather than remaining a fixed test set, under a named concept "Open Recursive Self-Improvement" (ORSI): an agent improves through interaction and feedback without a full retraining cycle between attempts. Positioned against static benchmarks that "look strong" on a fixed test but "stumble when requirements change mid-task."
- **Source(s)**: [Introducing Generative Simulators](https://www.patronus.ai/blog/introducing-generative-simulators), Patronus AI, published 2025-12-17 (confirmed via a dated secondary source), read scope: incomplete access (patronus.ai blocked; WebSearch summary aggregating the vendor's own post and consistent secondary tech-press coverage).
- **Discovered via**: feed (title surfaced in `inbox/competitors/LATEST.md`), content via search.
- **Evidence label**: proposal / interpretation (vendor's own framing of its own product; no independently verified numbers).
- **Limits**: no primary text; ~9 months old relative to this run — treat only the existence and framing as current, not any implied roadmap timing; Patronus is a named "team to watch" never previously individually touched in `knowledge/competitive.md`.
- **Relates to**: new — first Patronus AI claim. Adjacent to idea I-0008 (ground truth for user-built/imported worlds) via the shared tension of staying gradeable while an environment changes.
- **LayerLens relevance**: Open Q #6 (synthetic data legibility) most directly; #4 (task feasibility) adjacent. Positioning note: LayerLens environments are deterministically minted (reproducible-and-fixed); Patronus's framing is adaptive-and-evolving — a genuine design-philosophy fork worth tracking, not yet a validated advantage either way.
- **Confidence**: Low-moderate (incomplete access, vendor's own framing, but consistent across independent secondary coverage).
- **Recheck after**: 2027-03-29 (~180 days; foundational positioning claim).
