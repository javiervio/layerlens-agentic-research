# Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents

- authors_or_org: Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
- canonical_url: https://arxiv.org/abs/2611.14320v1
- discovered_url: inbox/arxiv/LATEST.md (cs.MA, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.14320v1
- version: v1
- published_at: 2026-11-10
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: memory, provenance, self-verification, agent reliability

## Claims from this source
- C-0168: External memory lets agents distill past trajectories into lessons for new tasks, but can cause "memory-induced degradation" — failing a task the agent would have solved without memory — typically because a lesson is incorrect, or is misapplied/misread, since lessons are inferred from trajectories labeled only success/failure and are usually given to the agent without the trajectories they came from, leaving no way to check them. WikiTrace stores each lesson linked to a summary of why its source trajectory succeeded or failed and to the raw trajectory itself; on a new task the agent starts from all insights and, when one lacks detail, conflicts with another, or comes from a failed task, descends through its links with terminal tools to fill in detail or correct the insight before acting, validated on five agentic benchmarks.
  - locator: abstract
  - evidence_label: bounded empirical
  - limitations: abstract only; exact benchmark names/numbers not visible in what was read.
  - relationship to existing claims: a third independent mechanism for I-0011/I-0013 (alongside Concord's source-change detection and AMV-Guard's action-conditioned verification) — this one lets the agent itself check a memory item against its evidentiary trail rather than only flagging staleness or gating by action consequence.

## LayerLens relevance
- open question(s) touched: #7 (human control — a memory system that can be descended into its evidence is a legibility pattern, not just a staleness flag), general (context and memory)
- general: strengthens I-0011's hypothesis that a staleness/trust flag on memory should be traceable back to its originating trajectory, not just a binary flag.
