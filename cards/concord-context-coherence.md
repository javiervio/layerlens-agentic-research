# When Agent Context Goes Stale: Incoherence in Volatile Agent Context

- authors_or_org: Yingying Liu, Junzhou Fang, Chenxiong Qian
- canonical_url: https://arxiv.org/abs/2610.05281
- discovered_url: inbox/arxiv/LATEST.md (2026-W42 harvest)
- discovered_via: feed
- doi_or_arxiv_id: 2610.05281v2
- version: v2
- published_at: 2026-10-04 (updated 2026-10-06)
- retrieved_at: 2026-10-19
- source_type: paper
- access_scope: abstract (verbatim, directly read via arXiv harvester inbox)
- sections_read: abstract only
- topics: context engineering, stale observations, agent runtimes

## Claims from this source
- C-0064: Agents ground reasoning in tool observations (e.g. file contents) whose underlying sources can later be modified by users, other agents, or external tools, while the model retains only the stale content in context, with existing runtimes providing little support for notifying the model that a previously observed fact has gone stale — causing reuse of outdated observations and incorrect claims about current state. Concord is a context-coherence framework that links each observation to its source, detects source changes, and applies configurable policies (update, annotate, suppress) before reuse; it is runtime- and resource-agnostic. On ConcordBench (constructed so previously-observed file contents become stale after subsequent edits), across three frontier models Concord produced answers consistent with the restored workspace state in all evaluated cases, matching the oracle recovery count, while using 46.4% fewer tokens than the strongest non-oracle baseline.
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; ConcordBench is a constructed benchmark built specifically for this failure mode, not an in-the-wild incidence rate; three models evaluated
  - relationship to existing claims: new — first claim in this knowledge base specifically on *stale context invalidation* as a named failure mode, distinct from C-0004's general context-engineering guidance (compaction/note-taking/sub-agents) and from I-0009's misleading-error-message framing. Dedup: checked against I-0009 (distinct — that is about error-message actionability post-failure; this is about tool-observation staleness mid-task, before any failure occurs) and T-06 (adjacent but distinct — T-06 is about environment *state* lifecycle from the system's side; this is about the *agent's belief* about that state going stale, a legibility problem on the agent's own side of the boundary).

## LayerLens relevance
- open question(s) touched: #2 (attribution — "the agent acted on stale information" is a nameable, distinct failure category from both agent error and environment error); #7 (recovery). Directly relevant to LayerLens's own mutable/replayable environments: if an environment's state can change mid-run (a teammate's concurrent write, a scheduled mutation, a branch/fork), an agent's own context could go stale in exactly this way — worth a design check on whether LayerLens's environments ever invalidate or re-serve updated state to an agent mid-task.
