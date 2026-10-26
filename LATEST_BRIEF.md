# Weekly brief — 2026-W44 (2026-10-26)

A five-minute read. Full traces are in `knowledge/claims.md` (C-0068 through C-0087) and this week's cards in `cards/`.

**Infra note up front**: the arXiv/competitor/reference harvester did not fire at all this week as of this run's start (a full week later than the last three weeks' "fires late" pattern) — see `runs/2026-10-26.md`. This run instead triaged last week's never-processed harvest (fetched 2026-10-19, a few hours after that day's research run had already completed).

## What deserves your attention

1. **A real formula for "how many runs are enough."** A new statistical methodology (TOST-based equivalence testing) converts a chosen margin and target power into a concrete run-count-per-method number — the first source in this knowledge base that answers the question directly, rather than only warning that two or three runs mislead. Re-analyzing four published runs of one model: certifying equivalence at two runs succeeds with only ~3% probability given the actual observed variance. Directly actionable for I-0001's pass^k readout — this gives it a *mechanism*, not just a motivation. [arXiv:2610.23700]. Changed since last week: nothing like this existed in the knowledge base before.
2. **A new, sharper attribution category: "the monitor was right, and it didn't matter."** A study of public safety-framework repair histories confirms 18 cases where a detector correctly recognized policy-relevant evidence (e.g. a regex match on leaked content), but the framework's own plumbing stranded that evidence before it reached the enforcement decision point. This is more specific than "the monitor is wrong" — it names a failure where recognition and consequence silently disconnect. [arXiv:2610.23362]. New this week.
3. **Modal crosses $1B ARR at a $15.75B valuation; E2B drops the word "sandbox."** Modal (sandbox infrastructure) raised $750M at a $15.75B valuation, reportedly tripling usage since May; the same week, E2B published "Sandboxes are dead," repositioning itself as an "agent-driven private cloud" rather than a sandbox vendor. Neither is new *technical* evidence — both are market-scale signals that the sandbox-infrastructure category (which this knowledge base has tracked technically converging for two months) is now commercially mature enough that an established player wants to differentiate beyond raw sandbox mechanics. Changed since last week: a $15.75B valuation and an established vendor's own strategic repositioning are new; the underlying technical convergence (T-06) was already documented.
4. **An independent test of the "Jev" decision-model pattern — and a caution about exposing judge confidence.** A different evaluation vendor (Comet, uninvolved in Jev's creation) ran its own production test: 1,000 real evaluation turns, 89.7% agreement with an LLM judge at ~3.5x lower cost. The same week, a separate paper (TUPLE-Bench) found that across nine models, the exact fields this pattern proposes exposing — confidence, per-candidate scores — leaked a supposedly-withheld piece of information 92-100% of the time. Read together: the cost/speed case for confidence-aware judges keeps strengthening, but "just show the confidence" is not a free design move — it needs its own privacy/leakage audit. [comet.com; arXiv:2610.23668]
5. **Real companies are building the attribution-lifecycle tooling our own differentiators argue for.** Meta's own production root-cause-analysis system ("Diviner") operationalizes a four-stage lifecycle (encode incidents into versioned knowledge, execute with evidence-linked hypotheses, evaluate against responder-reviewed ground truth, adapt only after replay and owner approval) — the most concrete real-world precedent yet for the "attribution as a location, every attribution a door" idea (I-0003), built by a frontier-scale company for its own on-call engineers rather than a product's end users. [arXiv:2610.21281]

## What changed in what we know

| Prior claim/status | New evidence | Current status |
|---|---|---|
| I-0009 (tool-error recovery) rested on one source | SchemaShield-Lite: a second, independent mechanism (post-deployment interface drift) with the same shape of fix | **Promoted L0 -> L1** |
| T-04 (consequence legibility) was "stable, early," design-principle reasoning only | A 239-practitioner, 31-country survey: reviewers already demand more evidence/provenance for AI-authored work today | Upgraded to "strengthening" — the need is felt now, not speculative |
| NVIDIA's platform launch was corrected (2026-10-19) to remove an unsupported causal link to Anthropic's incidents | A different disputed "agents escaped via emergent coordination" incident, forensically recreated, resolves to an ordinary cryptographic-verification-bypass misconfiguration (CVE-2026-65616) | A second instance of the same lesson: don't take press-reported sandbox-escape attribution at face value, in either direction |
| T-01 (reliability over capability) rested on 10 evidence families | This run's deliberate contradicting-evidence search specifically looked for signs the problem is resolved — found none, only a new 23,392-episode study tying decay to task duration | 14 families; search for counter-evidence came up empty, itself a data point |

## One concept to understand better: zero-knowledge proofs as a different kind of "verify without re-running"

Microsoft Research published Magnetar, a system that lets someone check a program's output is correct *without re-running the program and without trusting whoever ran it* — using a cryptographic proof instead of a replay. A proof (a few hundred KB) can be checked in milliseconds, and the private inputs the program ran on can stay hidden from the verifier entirely.

**Where this differs from LayerLens's own approach**: every verification mechanism in this knowledge base so far — our trust wall, deterministic replay, checkpoint/rollback, benchmark audits — works by either re-executing something, comparing against a stored answer key, or inspecting a trace. A ZK proof is a structurally different answer: the *computation itself* carries its own proof of correctness, so nobody needs to see the private data or redo the work to trust the result.

**When it doesn't apply**: this is general-purpose cryptographic computing (Rust/Go/C programs), not built for or evaluated on agent environments at all — the connection to LayerLens is this brief's own inference, not a claim Microsoft makes. It's also far more specialized and expensive to build than "replay and compare." Tie to **open question #11** (the reviewer surface — what would let Riley accept a claim without trusting the claimant?): a ZK-style proof is a structurally stronger version of that same need, worth knowing about even though it's not a near-term build.

## Possible applications to LayerLens

**Tool-description testing as a first-class workflow (open question #2).** Arize published a small, concrete worked example: editing one tool description cut an agent's unnecessary tool calls from 51 to zero and lowered a benchmark's cost by 30%, with correctness unchanged — using a fixed benchmark, repeated runs, and a diff between two configurations. **The gap**: LayerLens already has an analogous workflow for *prompts* (the Optimize loop), but this knowledge base has no evidence LayerLens offers the same iterate-and-measure loop for a system type's own *tool descriptions* specifically — and two papers this run (SchemaShield-Lite, the Android-agent provenance study) both independently found the tool/observation surface, not the model, is where real recovery failures live. **The assumption**: that a measurable, before/after tool-description test would surface real, fixable waste in LayerLens's own shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail) the same way it did for Arize's Codex example. **A small test a designer could run**: pick one existing LayerLens system type, run its current tool descriptions against a fixed task set, count unnecessary tool calls, then try one description edit and re-run — see if the Arize pattern (same correctness, lower cost) replicates on our own surface.

## Ideas that advanced

- **I-0009** (agent-actionable error/recovery guidance): promoted **L0 -> L1** — a second independent source and mechanism (interface drift) now exists alongside the original misleading-error-messages finding.
- I-0001, I-0003, I-0004, I-0010 all gained new evidence (run-count formula; monitor-validity/benchmark-leak/production-RCA/trace-annotation findings; MCP-gateway/harness-budget confounds; an independent production test plus a confidence-leakage caution, respectively) but stay at their existing L1 cap, each still blocked only on a product check someone with LayerLens access would need to run.
- I-0006 gained one adjacent (not identical) source — stays L0.

## Feature ranking moves

- **F-0009** (agent-actionable error/recovery guidance): **L0 -> L1**, confidence 0.3 -> 0.6, priority 0.45 -> 0.90.
- No other feature's maturity or score changed this run (several gained evidence links but remain at their L1 cap pending a product check).

## For you

- **Comprehension question**: In your own words, what's the difference between "LayerLens's trust wall proves a grade wasn't gamed" and "a Magnetar-style proof shows a computation ran correctly"? What does each one let a skeptical third party *not* have to do?
- **Design exercise**: Sketch, for one LayerLens system type you know well, what a "tool-description test" screen might look like — given a fixed task set and two versions of a tool's description, what would you want the screen to show someone deciding whether the new version is actually better (not just different)?

## Coverage and gaps

- Triaged in full (never-before-processed): `inbox/arxiv/2026-W43.md` (192 papers — scanned all titles, read ~22 abstracts in full, carried 14 forward to claims), `inbox/competitors/2026-W43.md` (17 sources), `inbox/reference/2026-W43.md` (11 sources).
- 10 WebSearch calls this run: 6 on competitive follow-ups (Modal, E2B, Arize x2, Comet, Microsoft Research), 1 to pin down a paper found via the contradicting-evidence search, 1 deliberate contradicting-evidence search (found no counter-evidence to T-01), 2 narrowing searches to identify a specific paper.
- `inbox/discovery/` and `inbox/fulltext/` do not exist — wired into the Monday workflow on 2026-10-19 but never actually run via a real scheduled harvest yet (see run log).
- Rotation gap carried forward: Galileo, Patronus's other named products (Glider, SpeedRunBench), LangChain/LangSmith, and Vals AI were seen only at title level in this week's inbox; none individually deep-dived this run.
- Never claim complete coverage of the field from one week's search; this is a sample, not a census.
