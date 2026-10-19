# A Baseline Assessment for the Agentic Web Technology Stack

- authors_or_org: Vagner Figueredo de Santana, Diogo Cortiz
- canonical_url: https://arxiv.org/abs/2610.13703
- discovered_url: inbox/arxiv/LATEST.md (2026-W42 harvest)
- discovered_via: feed
- doi_or_arxiv_id: 2610.13703v1
- version: v1
- published_at: 2026-10-09
- retrieved_at: 2026-10-19
- source_type: paper
- access_scope: abstract (verbatim, directly read via arXiv harvester inbox)
- sections_read: abstract only
- topics: MCP/agent protocols, frameworks, comparability

## Claims from this source
- C-0066: MASTIF (Multi-Agent System TestIng Framework) benchmarks a baseline Agentic Web technology stack — 3 LLMs, 3 protocols, and 4 agent implementation frameworks — against 300 Mind2Web benchmark tasks. Selecting a task-specific technology stack (protocol + framework + model combination) can produce gains in task completion rate, efficiency score, and social-value stability, and reductions in verbosity and time to complete tasks, versus a non-task-specific stack choice.
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; 3x3x4 combinations is a baseline assessment, not exhaustive; specific numeric deltas not given in the abstract
  - relationship to existing claims: corroborates and extends C-0044 ("Finding the Right Fit," harness reverses model rankings) — that paper showed harness as a confound for a given model; this paper shows the full agentic-web technology stack (protocol choice + framework choice, not just harness/scaffold) is similarly a confound for task outcomes, widening the set of variables a fair comparison must pin down.

## LayerLens relevance
- open question(s) touched: #1 (comparability), #9 (comparison as signature surface). Strengthens I-0004's build caution: a comparison view's "pin harness/scaffold" requirement (from C-0044) should extend to the full technology stack (protocol, framework, model) where LayerLens's own environments interact with an agent via MCP or similar protocols.
