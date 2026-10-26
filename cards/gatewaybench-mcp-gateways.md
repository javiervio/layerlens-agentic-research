# GatewayBench: Unified Capability and Security Evaluation Platform for MCP Gateways

- authors_or_org: Yitian Zheng, Zhaorun Chen, Haoyu Li, Bo Li
- canonical_url: https://arxiv.org/abs/2610.23449v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.AI)
- discovered_via: feed
- doi_or_arxiv_id: 2610.23449v1
- version: v1
- published_at: 2026-10-16
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: MCP gateways, tool-surface evaluation, comparability confounds

## Claims from this source
- C-0071: GatewayBench is the first systematic benchmark for MCP gateways (the middleware layer that aggregates, governs, and shapes the tool surface an agent sees), comprising 524 tasks across six domains plus a pool of 11,118 real-world tools from 251 authentic MCP servers, with task-irrelevant tools deliberately injected to emulate large-scale deployments. Across seven widely deployed MCP gateways and diverse agent configurations (benign and adversarial tasks), gateway design produced substantial differences in task completion, tool-use efficiency, and resilience to attacks, and — notably — these effects interact strongly with the underlying model and agent harness, not just the gateway in isolation.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; seven gateways is not exhaustive of the category; "interacts strongly with model and harness" is reported qualitatively in the abstract, without the specific numbers.
  - relationship to existing claims: a new confound alongside C-0044 (harness reverses rankings) and C-0066 (the full protocol+framework+model stack is a confound) — this adds the MCP gateway layer specifically as a further comparability variable. Strengthens T-01 and I-0004's build caution (a comparison view must pin gateway/tool-surface configuration too, not only harness and model).

## LayerLens relevance
- open question(s) touched: #1 (comparability), general scope (tools and protocols / MCP). GatewayBench's injected-irrelevant-tools design is also a concrete methodology LayerLens could borrow for stress-testing its own tool surfaces at scale (relevant to I-0009's tool-surface theme).
