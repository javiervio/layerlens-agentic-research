# HAL: The Holistic Agent Leaderboard (hal-harness)

- authors_or_org: Princeton PLI lab (Princeton Language and Intelligence); related prior work by Sayash Kapoor, Benedikt Stroebl, and Arvind Narayanan
- canonical_url: https://github.com/princeton-pli/hal-harness
- discovered_url: WebSearch "Holistic Agent Leaderboard HAL Princeton github Pareto cost accuracy" (followed from a GitHub search for the reliability paper's authors)
- discovered_via: search, then citation (agent-eval repo below led to this one)
- doi_or_arxiv_id: companion paper reportedly arXiv:2510.11977 ("Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation," accepted ICLR 2026 per search results — not independently confirmed)
- version: repository archived as of 2026-07-01 (stated in the README itself)
- published_at: not confirmed for the paper; repo predates its 2026-07-01 archival
- retrieved_at: 2026-09-28
- source_type: docs (GitHub README, primary source, fetched directly via WebFetch — reachable, unlike arxiv/alphaxiv/huggingface)
- access_scope: full text — the README was fetched and read directly, not via search summary.
- sections_read: overview / what HAL is, cost-controlled evaluation rationale, supported benchmarks list, reproducibility and versioning (execution isolation, run continuity, trace encryption), agent-trace access, stated limitations, archival notice.
- topics: agent evaluation, comparability, cost-controlled evaluation, Pareto frontier, benchmark leaderboards, reproducibility

## Claims from this source

- C-0009: HAL is a standardized agent-evaluation harness spanning 9+ benchmarks (SWE-bench Verified/Mini, USACO, AppWorld, CORE-bench, tau-bench, three SciCode variants, AssistantBench, ScienceAgentBench, CollaborativeAgentBench) that reports cost alongside accuracy by default and visualizes results as a cost-accuracy Pareto frontier rather than a single ranked number. Per the README's own framing: "Benchmark evaluations tend to ignore costs, leading to uninformative evaluations for downstream developers," posing the question "What does it mean if an agent has 1% higher accuracy on a benchmark but is 10x more expensive?" A related WebSearch summary (not independently verified against the README itself) reported "100x cost differentials for 1% accuracy gains" and "less than one-third of tested models typically achieving optimal cost-accuracy trade-offs for any given benchmark."
  - locator: README sections "What HAL Is" and cost-controlled evaluation description (directly fetched)
  - evidence_label: documented capability (primary source, full README read directly) for the design and rationale; the specific "100x" and "less than one-third" figures are evidence_label: incomplete access (only from a secondary WebSearch summary, not the README text itself, and not the underlying paper).
  - limitations: the README describes intent and design ("cost-controlled by default," Pareto framing) without walking through the actual visualization mechanics or math in the text that was returned; reproducibility mechanics (execution isolation via conda/Docker/Azure, `--run_id`/`--continue_run`, automatic trace encryption "to avoid benchmark contamination") are documented but this run did not verify them against real output.
  - relationship to existing claims: new. Connects thematically to C-0008 (reliability paper) — see below.
- C-0009b: As of 2026-07-01 the repository is archived with the maintainers' own stated reason: "HAL leaderboard results are no longer being updated through this harness. We are focusing our current work on agent reliability." The same two named individuals (Kapoor, Narayanan) behind HAL are also authors on the "Towards a Science of AI Agent Reliability" paper (see ai-agent-reliability-science card, C-0008).
  - locator: README archival notice (directly fetched)
  - evidence_label: documented capability (first-party, unambiguous statement)
  - limitations: this establishes that one specific lab shifted its own stated focus from leaderboard/comparability work to reliability work; it does not establish this as a field-wide trend from a single data point.
  - relationship to existing claims: connects to C-0008 — same lab, sequential projects, explicit stated pivot from "which agent is better" to "does this agent behave the same way twice."

## LayerLens relevance

- **Open question #1 (Comparability)** and **#9 (Comparison as the signature surface)**: HAL's core argument — a single accuracy number without cost, and without acknowledging that "better" depends on the tradeoff you care about, is close to useless for a real decision — is a strong, directly-read (not just discovered) precedent for LayerLens's own differentiator language ("Different must name a difference in behavior. Better must say better for whom and by how much.", PROTOCOL.md). Worth citing this project by name when explaining why LayerLens's comparison views should default to showing tradeoffs (cost, time, reliability) rather than a single leaderboard rank.
- The archival-and-pivot fact (C-0009b) is this week's clearest example of PROTOCOL.md's "connection between research and competitive" pattern: a credible, well-resourced academic group tried to solve comparability first, then explicitly moved on to reliability — suggesting the field currently sees "does it work the same way twice" (open question #5) as the harder, more current problem than "which agent is better" (open question #1). That is itself a signal worth Javier's attention regardless of the still-unread reliability paper's specific numbers.
