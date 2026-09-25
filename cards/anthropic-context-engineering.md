# Effective Context Engineering for AI Agents

- authors_or_org: Anthropic (engineering blog)
- canonical_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- discovered_url: WebSearch "agent memory context engineering long-horizon lessons learned postmortem" (candidate list) then fetched directly
- discovered_via: search
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2025-09-29 (per fetched page)
- retrieved_at: 2026-09-25
- source_type: post (vendor engineering blog, practitioner guidance)
- access_scope: full text
- sections_read: whole article per WebFetch summary (context engineering vs. prompt engineering, "context rot," compaction, structured note-taking, sub-agent architectures, just-in-time retrieval)
- topics: context engineering, agent memory, long-horizon agents

## Claims from this source

- C-0004: Anthropic frames "context engineering" (curating the optimal set of tokens across an inference run) as distinct from prompt engineering, names a "context rot" phenomenon (models degrade as context grows), and recommends three techniques for long tasks: compaction (summarize + restart with compressed context), structured note-taking (agent maintains external memory files), and sub-agent architectures (specialized agents do focused work and return condensed summaries to an orchestrator), plus retrieving data "just-in-time" rather than loading it all upfront.
  - locator: whole article (see WebFetch summary; original article not re-quoted line-by-line here)
  - evidence_label: proposal / interpretation (practitioner guidance from one vendor, not a controlled study with measured results)
  - limitations: no benchmark numbers attached to the recommendations in what was retrieved; this is Anthropic's own product/engineering guidance, so should be read as informed opinion, not independent research.
  - relationship to existing claims: new

## LayerLens relevance

- Published 2025-09-29 — **this is a foundational piece from about a year before this run, not new work**; flagged in the brief as background rather than "what's new this week." Recheck cadence: foundational concepts, 180 days (already past due — treat as still broadly valid practitioner guidance, not urgent to re-verify).
- General relevance to the "context and tools" slice of scope (15% budget) and to open question #6 (human control and recovery) via structured note-taking / sub-agent summarization as inspectable intermediate state — worth a future run cross-referencing this against a study with actual measured results (e.g., the "context budget mismatch, 98.3% failure" finding surfaced in this run's search results but not independently opened — see run log pending list).
