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

**2026-09-28 update — the mechanism, read directly**: Action guards are a three-tier, per-agent tool-approval policy (`auto_approve`, `require_approval_untrusted` [default], `require_approval_all`), configured via YAML per agent (orchestrator or web_surfer). Source: raw.githubusercontent.com/microsoft/magentic-ui/main/docs/configuration.md, read in full 2026-09-28. This answers "how does a human set the agent's caution level" but the docs as read do not say whether a confirmation names the specific consequence of the pending action (open question #7's exact phrasing) — recorded as undocumented-in-what-we-read, not as absent. See `cards/magentic-ui.md` (C-0011) for the full claim.

---

### Braintrust — comparison and sandboxing claims are directionally relevant but still unread (two runs in a row blocked)

- **Documented problem**: Comparing two eval runs meaningfully requires more than a single score delta; and running untrusted agent code inside an eval pipeline risks leaking platform credentials to that code.
- **Their solution**: Reportedly, an "Experiments" comparison view showing score breakdowns, regression detection, and output diffs "at the test case level" side by side; and a "Harbor" sandboxed-eval mode that keeps the Braintrust API key in the host process, out of reach of code running inside the task container.
- **Known limits**: We do not know, because www.braintrust.dev has been EGRESS_BLOCKED two runs running (2026-09-25 and 2026-09-28), whether the "output diff" is step/trajectory-level or only a final-answer diff, or what Harbor's sandboxing actually enforces versus merely intends.
- **Result reported**: n/a — no independently-read result.
- **Availability**: Generally available (commercial eval platform); Harbor described as an "integration," exact availability tier unconfirmed.
- **Our users' need**: Devon and Evan (open questions #1 comparability, #9 comparison as signature surface) need to know whether a competitor's "diff" view already operates at the step level LayerLens's v3 "unified DAG diff for comparing trajectories" direction is aiming for — if so, that's a bar to clear, not a novel bet.
- **LayerLens alternative (hypothesis, pending validation)**: Unknown whether Braintrust's diff is trajectory-level; until confirmed, treat the v3 "DAG diff" direction as neither validated nor invalidated by this competitor.
- **How to validate**: Next run, retry www.braintrust.dev directly; if blocked a third time, ask Javier whether he has a saved/authorized link per PROTOCOL.md, since this vendor is explicitly named in SOURCES.md and remains the least-verified entry on our "teams to watch" list.
- **Action**: investigate (blocked twice; escalate priority for a saved link if blocked again).
- **Evidence links and dates**: canonical: https://www.braintrust.dev/foundations/comparing-experiments, https://www.braintrust.dev/blog/harbor-agent-evals, https://www.braintrust.dev/docs/platform/experiments; discovered via WebSearch 2026-09-28 (and 2026-09-25); read 2026-09-28 (search summary only, both runs).

---

### Princeton PLI (HAL / Holistic Agent Leaderboard) — cost-blind leaderboards are uninformative; the same lab has now pivoted from comparability to reliability

- **Documented problem**: Agent benchmark leaderboards historically rank by accuracy alone, which the authors argue is uninformative for a real adoption decision — "what does it mean if an agent has 1% higher accuracy but is 10x more expensive?"
- **Their solution**: HAL, a standardized harness across 9+ benchmarks (SWE-bench Verified/Mini, USACO, AppWorld, CORE-bench, tau-bench, SciCode variants, AssistantBench, ScienceAgentBench, CollaborativeAgentBench) that tracks cost by default and visualizes results as a cost-accuracy Pareto frontier instead of a single rank.
- **Known limits**: The project is now archived (2026-07-01); the maintainers' own README states they've moved on to agent-reliability work instead (see the reliability-paper card/claim, C-0008) — meaning the Pareto-leaderboard approach was apparently not the team's final answer to comparability, or at least not where they chose to keep investing.
- **Result reported**: A secondary (unverified) summary reported "100x cost differentials for 1% accuracy gains" and "less than one-third of models on the Pareto frontier for any given benchmark" — flagged incomplete access, not confirmed against the README itself.
- **Availability**: Was generally available (open source, GitHub); archived and no longer accepting submissions as of 2026-07-01.
- **Our users' need**: Taylor (the accountable lead, open question #10 "the readiness report") and Devon/Evan (open questions #1, #9) need comparisons that show tradeoffs, not just a rank — exactly HAL's stated design goal.
- **LayerLens alternative (hypothesis, pending validation)**: LayerLens's model-comparison and Insights/Evidence surfaces should be checked against HAL's specific framing: does LayerLens ever present a single "winner" without a cost or reliability axis alongside it? If so, HAL's own archival-and-pivot (choosing to stop investing in the pure-comparability framing) is a mild caution that comparability alone may not be the most differentiating axis for LayerLens either — reliability (open question #5) may deserve equal design weight.
- **How to validate**: Have someone with product access check LayerLens's own comparison views (model head-to-head, Optimize) for whether cost and reliability are shown by default alongside accuracy/pass rate, the way HAL's README argues they should be.
- **Action**: explore alternative (adopt the "always show cost/reliability alongside accuracy" framing as a design check, not necessarily HAL's specific harness or Pareto visualization).
- **Evidence links and dates**: canonical: https://github.com/princeton-pli/hal-harness (README read in full, directly, 2026-09-28); companion paper reportedly arXiv:2510.11977 (not independently read); discovered via WebSearch 2026-09-28 (following a GitHub search for the reliability paper's authors); read 2026-09-28.

---

### Arize — observability-to-evaluation framing, not yet differentiated from generic competitors (rotation coverage only)

- **Documented problem**: Teams need to move from "something looks wrong in this trace" (observability) to "did this pass or fail against a criterion" (evaluation) without re-deriving the pipeline each time.
- **Their solution**: Per search-summary descriptions only, Arize frames this as tracing + evals + monitoring, with deterministic checks for objective criteria and LLM judges for semantic ones, plus an "Agent-as-a-Judge" pattern for dynamically exploring a trace across multiple steps.
- **Known limits**: This run only surfaced generic marketing/blog-style content (arize.com/resources, arize.com/blog); no product docs, pricing, or a specific worked example were opened. This is meaningfully thinner coverage than this run's Braintrust or HAL entries.
- **Result reported**: n/a.
- **Availability**: Generally available (commercial observability/eval platform, per general knowledge; not independently confirmed this run).
- **Our users' need**: n/a until differentiated further — currently indistinguishable from generic "LLM observability platform" positioning.
- **LayerLens alternative (hypothesis, pending validation)**: none yet — insufficient evidence to state a difference in behavior.
- **How to validate**: Next run, open a specific Arize docs page (not a blog/resources listing) and look for one concrete, checkable mechanic (e.g., how "Agent-as-a-Judge" actually decides what to explore) rather than framing language.
- **Action**: do nothing this run (rotation coverage only — SOURCES.md flagged Arize as untouched since inception; this run's search budget did not stretch to a deep read).
- **Evidence links and dates**: canonical: https://arize.com/resources/, https://arize.com/blog/best-ai-observability-tools-for-autonomous-agents-in-2026/; discovered via WebSearch 2026-09-28; read 2026-09-28 (search summary only).

---

### Browserbase — latency/reliability numbers found only via third-party comparison sites, not Browserbase's own docs (rotation coverage only)

- **Documented problem**: Teams running browser-using agents need to know cold-start latency, session success rate, and stealth quality before committing to a provider.
- **Their solution**: Unknown from what was read this run — no Browserbase-authored page was opened, only third-party comparison content.
- **Known limits**: The only numbers found ("browserbench averages, January 2026, 5,000 runs per provider," Browserbase reportedly at 40-50% success rate with higher latency than some competitors) came from third-party review/comparison sites (aimultiple.com-style aggregators), not from Browserbase's own docs or a neutral, named benchmark methodology page. Per PROTOCOL.md's rule 4 ("a vendor announcement is not proof") and general evidence discipline, a competitor-comparison number from an uncredited third-party site is weaker than a vendor announcement, not stronger — treat as **anecdotal signal**, not bounded empirical evidence.
- **Result reported**: Unconfirmed third-party numbers only; not repeated here as fact.
- **Availability**: Generally available (commercial managed browser infrastructure).
- **Our users' need**: Marginal for LayerLens today — LayerLens's shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail, Google Calendar) are API/record-based, not browser-driven, so Browserbase-style latency is adjacent infrastructure rather than a direct comparison point unless LayerLens adds a browser-driven system type.
- **LayerLens alternative (hypothesis, pending validation)**: n/a — no clear product overlap established this run.
- **How to validate**: Only worth deeper investigation if/when LayerLens's roadmap adds a browser-interaction system type; until then, low priority.
- **Action**: do nothing (rotation coverage only; weak evidence and unclear product overlap).
- **Evidence links and dates**: discovered via WebSearch 2026-09-28 ("Browserbase agent browser automation latency benchmark developer experience 2026"); no canonical first-party source opened; read 2026-09-28 (third-party search summaries only).

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
