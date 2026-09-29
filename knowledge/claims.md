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
