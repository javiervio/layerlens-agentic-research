# ToolBottleneckBench: Measuring Tool-Agent Performance under Controlled Pressures and Fixed Harness Budgets

- authors_or_org: Zichuan Xu, Yuyang Dong, Makoto Onizuka, Chuan Xiao
- canonical_url: https://arxiv.org/abs/2610.21098v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.SE)
- discovered_via: feed
- doi_or_arxiv_id: 2610.21098v1
- version: v1
- published_at: 2026-10-15
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: harness budget confounds, tool-agent benchmarking, T-01/I-0004

## Claims from this source
- C-0073: ToolBottleneckBench measures tool-agent performance under controlled pressures (registered tool catalog size, visible tool menu, certified workflow, encoding of returned records) at fixed harness budgets, using synthetic enterprise tasks and an exact grader that records the first unmet obligation and which harness limit (if any) ended a failed episode. Across 21 model/harness configurations, only the visible tool menu produced a large model-level penalty, and that penalty tracked truncation at the completion cap — raising the cap sixteenfold removed most of the penalty. Most failures ended at a harness limit rather than a model reasoning failure, and the failure record identified the assigned pressure no more reliably than a simple count of tool calls. Only two repairs beat every configuration switch, and neither improved model behavior itself — both changed which tools reached the model or who issued the calls.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; synthetic enterprise tasks, not real-world tool catalogs; 21 configurations, not exhaustive.
  - relationship to existing claims: extends C-0044 (Finding the Right Fit: harness reverses model rankings) with a specific, actionable mechanism — harness *budget* (completion cap, visible tool menu size) drives much of what looks like a model capability gap, and the paper's own recommendation ("report pressure effects with the harness budgets under which they were measured") is a direct instance of PROTOCOL.md's own comparability rule.

## LayerLens relevance
- open question(s) touched: #1 (comparability). Strengthens I-0004's build caution: a LayerLens comparison view should pin and surface harness budget parameters (tool menu size, completion caps), not only harness/scaffold identity, since this paper shows budget alone can look like a capability difference.
