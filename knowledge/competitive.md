# Competitive learning

What other teams are doing, framed so it feeds LayerLens design decisions. The agent updates this per `AGENT_RUNBOOK.md`. Never infer a missing capability from silence; absence of evidence is not evidence of absence.

---

### BenchJack (research project, UC Berkeley/related authors) - Benchmarks are exploitable by default, and auditing is currently reactive, not built-in

- **Documented problem**: Agent benchmarks are supposed to measure capability, but 8 of 8 audited (SWE-bench Verified, SWE-bench Pro, Terminal-Bench, WebArena, FieldWorkArena, OSWorld, GAIA, CAR-bench) were exploitable via weak isolation between agent and evaluator, accessible ground truth, RCE, judge prompt-injection, or weak scoring logic — 6 of 8 hit ~98-100% scores without genuine task-solving.
- **Their solution**: A red-team scanner (static analysis + AI-driven reconnaissance + proof-of-concept exploit generation) that audits an existing benchmark's implementation after the fact and reports findings by vulnerability class (V1-V8) and severity.
- **Known limits**: Reactive (audits benchmarks that already exist and are already in use); PoC exploits are not automatically re-verified; single-user tool, no parallelism; authors note high refusal rates from one of their two supported agent backends on security-flavored prompts.
- **Result reported**: All 8 audited benchmarks exploitable; a claimed iterative-patching pipeline reduced hackable-task ratio from ~100% to <10% on 4 "well-designed" benchmarks — this second number is **unconfirmed** (search-snippet only, not independently opened).
- **Availability**: Open source scanner (GitHub), paper on arXiv (2605.12673, not independently read this run — see run log).
- **Our users' need**: Devon/Evan/Mina personas need to trust that a passing score means the agent actually did the work, and that a failing score is attributable to something real. Riley (compliance) needs "mechanical grading, nothing self-scored" to actually hold under adversarial conditions, not just in the happy path.
- **LayerLens alternative (hypothesis, pending validation)**: LayerLens's trust wall (seed/knobs never served to an agent-facing key) is a structural, day-one mitigation of BenchJack's V1 (no isolation) and V2 (ground truth accessible) classes, rather than a bolt-on audit after the benchmark is already deployed. Whether it also closes V4 (judge prompt-injection) depends on how Judges/Scorers are sandboxed from agent output — not yet verified against BenchJack's own taxonomy.
- **How to validate**: Have someone other than the environment's author attempt each of BenchJack's 8 vulnerability classes against a real LayerLens environment/task, and document which are structurally impossible (by the trust wall's design) versus merely undocumented/discouraged. A result showing several classes are only "discouraged, not prevented" would be the finding that changes our confidence in the differentiator.
- **Action**: investigate (this run surfaces the checklist; validating it against our own product needs someone with environment access, which this research agent does not have).
- **Evidence links and dates**: canonical: https://github.com/benchjack/benchjack (README), paper arXiv:2605.12673 (not opened); discovered via WebSearch 2026-09-25; published May 2026; read 2026-09-25.

---

### IOV Labs (independent researcher) - LLM judges favor their own model family, even blind and even without self-recognition

- **Documented problem**: In a pilot (4 models, 2 vendor families, 1,152 blind pairwise judgments), every judge rated its own family's answers above a neutral consensus baseline (mean SPI +0.14), and this held even for models that could not reliably tell which response was their own.
- **Their solution**: A measurement methodology (Self-Preference Index = own-family win rate minus leave-one-out consensus of other judges) that isolates bias from genuine quality differences; no mitigation is proposed in what was read, only measurement.
- **Known limits**: Author states pilot scale explicitly — 24 prompts, 2 families, small consensus baseline, open-ended (not verifiable/ground-truth) tasks, length-win-rate confound.
- **Result reported**: Mean SPI +0.14; GPT-4o highest at +0.21; Claude Sonnet 4.6 and Claude Haiku 4.5 both +0.14; only Claude Sonnet 4.6 above-chance at self-recognition.
- **Availability**: Public GitHub repo, methodology and results open; no product, this is a research artifact.
- **Our users' need**: Alex (analyst/model comparison) and Riley (compliance) need to know when a Judge verdict might be quietly biased toward or against a given agent — particularly if the Judge and the agent-under-test share a model family/vendor.
- **LayerLens alternative (hypothesis, pending validation)**: LayerLens already separates Graders (deterministic) from Judges (rubric-tuned) from Scorers (LLM rubric 0-5) and keeps Graders load-bearing. The open gap: does the UI ever surface *which* judge model is being used relative to the agent under test, and flag same-family pairings as a risk? Not yet known.
- **How to validate**: Pick one existing eval where the Judge model and the agent-under-test share a vendor/family; re-run the same task/outputs with a cross-family judge; compare verdicts. A meaningful divergence would justify a same-family warning in the product; no divergence would be evidence to deprioritize this.
- **Action**: investigate.
- **Evidence links and dates**: canonical: https://github.com/hankimis/self-preference; discovered via WebSearch 2026-09-25; date unknown (repo undated); read 2026-09-25.

---

### Sierra Research (tau2-bench) - Honest, dated precedent for "this version's scores don't compare to that version's"

- **Documented problem**: A grading bug in one domain (`banking_knowledge`) was silently zeroing rewards for agent behavior that was actually policy-correct; fixing it necessarily changed what "correct" meant for every score in that domain.
- **Their solution**: Ship the fix as a version bump (v1.0.1), and state directly in the release notes that scores from before and after are not comparable, plus report the direction and rough magnitude of the shift (upward only, up to ~9 points) so users aren't left guessing.
- **Known limits**: This is a single, self-reported instance; we don't know how often this class of bug occurs across tau2-bench's history or across other benchmarks generally (absence of evidence elsewhere is not evidence of absence).
- **Result reported**: No pass-to-fail flips; up to ~9-point score increase depending on model, after the fix.
- **Availability**: Generally available — open source, versioned releases on GitHub.
- **Our users' need**: Taylor (QA/regression) and engineering/product leaders need to know, at a glance, whether two runs being compared ran against the same environment/task/grading version — this is open question #1, verbatim.
- **LayerLens alternative (hypothesis, pending validation)**: LayerLens's "immutable environment, task, and prompt versions; runs stamped with the versions they ran against; the grid refuses to average across mismatched versions" (differentiator #5) is designed to make this kind of silent incomparability structurally impossible rather than something a maintainer has to remember to announce.
- **How to validate**: Simulate a grading-logic change in a LayerLens environment (bump a grader) and confirm the product (a) versions it, (b) refuses to blend pre/post scores in the same view, and (c) can show a human-readable "what changed and which way" summary comparable to what sierra-research wrote by hand.
- **Action**: adopt (as a validation of an already-stated differentiator, not a new idea) — worth using as the concrete external example when explaining the "On record" pillar to a non-technical stakeholder.
- **Evidence links and dates**: canonical: https://github.com/sierra-research/tau2-bench/releases; discovered via WebSearch 2026-09-25 (tau2-bench is also a seed source in our own SOURCES.md); v1.0.1 dated 2026-07-22; read 2026-09-25.

---

### Microsoft Research (Magentic-UI) - Named vocabulary for human-in-the-loop control, worth comparing mechanics against

- **Documented problem**: Fully autonomous agents are fallible and pose safety/security risk; the stated alternative is human-in-the-loop collaborative control.
- **Their solution**: An open-source multi-agent web interface (MCP-extensible) built around named interaction mechanisms: co-planning, co-tasking, multi-tasking, action guards (safety checkpoints), and long-term memory.
- **Known limits**: Only the publication landing page was read this run, not the technical report or repo internals — so we cannot yet say how "action guards" concretely surface to a user, or whether confirmations name specific consequences.
- **Result reported**: None captured this run (qualitative framing only, no evaluation numbers read).
- **Availability**: Open source (per general knowledge of the project; not independently confirmed via a repo read this run).
- **Our users' need**: Open question #6 (human control and recovery) and #2 (failure attribution as "a routed next action") — both ask, in effect, what Magentic-UI's "action guards" claim to already do.
- **LayerLens alternative (hypothesis, pending validation)**: Unknown yet whether Magentic-UI's action guards name specific consequences before a confirmation (open question #6 asks exactly this). Needs a deeper read before any comparison claim is made.
- **How to validate**: Next run (or a manual session with product access), read the Magentic-UI technical report/repo directly and check its action-guard UI against open question #6's specific phrasing ("Do confirmations show specific consequences?").
- **Action**: investigate (deeper read needed before any adopt/explore/do-nothing call).
- **Evidence links and dates**: canonical: https://www.microsoft.com/en-us/research/publication/magentic-ui/; discovered via our own SOURCES.md seed list; date unknown; read 2026-09-25 (page summary only).

---

### Prime Intellect - Verifiable-reward RL training infrastructure; unclear yet whether it competes with or merely parallels LayerLens Environments

- **Documented problem**: Agentic RL training needs environments with fast, verifiable reward signals (binary/scalar, no learned reward model) to keep GRPO/RLOO-style training's rollout throughput from becoming the bottleneck.
- **Their solution**: prime-rl (async RL training framework, scales to 1000+ GPUs) integrates natively with the Verifiers library (a real, active GitHub project: 4,700+ stars, 683 forks, 2,378 commits) and an "Environments Hub" for sourcing task environments, including SWE and agentic benchmarks.
- **Known limits**: We could not reach primeintellect.ai or docs.primeintellect.ai this run (blocked by session network policy), so claims about the Hub's own scale (a search summary mentioned "2,500+ environments") and its exact verification mechanics are **unconfirmed** — only the GitHub repo descriptions were independently read.
- **Result reported**: n/a (infrastructure claims, not benchmark results).
- **Availability**: Open source (prime-rl, verifiers repos); Environments Hub itself not independently confirmed as open or hosted-only this run.
- **Our users' need**: n/a directly — Prime Intellect's stated use case is training-time RL rollouts, not post-hoc agent evaluation/readiness, which is LayerLens's Environments pillar. This may make it a parallel infrastructure play rather than a direct competitor, but that needs confirming.
- **LayerLens alternative (hypothesis, pending validation)**: Unclear yet whether Prime Intellect environments are ever used for *evaluation* the way LayerLens's are (versioned, graded, attributed) as opposed to purely for *training* rollouts. This distinction should be resolved before treating Prime Intellect as a competitive comparison point rather than an adjacent infrastructure reference.
- **How to validate**: A future run should open primeintellect.ai/docs directly (network permitting) and check specifically whether the Hub supports the same evaluation/attribution/versioning workflow LayerLens does, or whether it's purely a training-data/rollout source.
- **Action**: investigate.
- **Evidence links and dates**: canonical: https://github.com/PrimeIntellect-ai/prime-rl, https://github.com/PrimeIntellect-ai/verifiers; discovered via WebSearch 2026-09-25 (Prime Intellect is a seed "team to watch" in SOURCES.md); read 2026-09-25.

---

### E2B - Sandbox infrastructure; session-lifecycle claims could not be verified this run

- **Documented problem**: Long-running or multi-session agents need sandbox state to persist or resume across a conversation without re-provisioning.
- **Their solution**: Per the GitHub repo description, E2B is "open-source infrastructure that allows you to run AI-generated code in secure isolated sandboxes in the cloud," with JS/Python SDKs.
- **Known limits**: Specific session-limit numbers (a 1-hour cap on a free/Hobby tier, 24 hours on a paid/Pro tier) appeared only in third-party blog posts (Blaxel, bex.co) surfaced by WebSearch — **both domains were blocked by this session's network egress policy**, so these specific numbers were not independently verified and should be treated as unconfirmed pending a run where those sources (or E2B's own docs at e2b.dev, also blocked this run) are reachable.
- **Result reported**: n/a — no independently-read result this run.
- **Availability**: Open source core; hosted product tiers referenced by third parties but not confirmed directly.
- **Our users' need**: n/a until the lifecycle claims are confirmed.
- **LayerLens alternative (hypothesis, pending validation)**: n/a this run.
- **How to validate**: Next run, retry e2b.dev/docs and the two blocked blog domains; if still blocked, ask Javier whether a saved/authorized link exists per PROTOCOL.md's "links Javier saved" allowance.
- **Action**: do nothing (this run) — insufficient independently-verified evidence to act on.
- **Evidence links and dates**: canonical (confirmed reachable): https://github.com/e2b-dev/E2B; unconfirmed secondary sources (blocked, not opened): blaxel.ai/blog/e2b-session-limit, bex.co/blog/2026/09/11/e2b-sandbox-time-limits; discovered via WebSearch 2026-09-25.
