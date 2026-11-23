# Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning

- authors_or_org: Gustavo Pinto
- canonical_url: https://arxiv.org/abs/2611.17304v1
- discovered_url: inbox/arxiv/LATEST.md (cs.SE, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.17304v1
- version: v1
- published_at: 2026-11-12
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: production debugging, tool access, attribution, field study

## Claims from this source
- C-0164: A field observation of Claude Code diagnosing eight real database incidents in a production message-dispatch engine finds that in every incident whose root cause depended on runtime concurrency, the agent announced a cause, shipped a fix, and later walked it back, each wrong guess costing a deploy-and-observe cycle. Mapping each incident to what the agent lacked finds access to production state (live lock views, untruncated deadlock reports, read-only execution, explicit environment context) was the most pervasive bottleneck — present in all five concurrency-dependent incidents, alone in one and combined with a reasoning error in four. The three incidents not depending on concurrency needed nothing beyond what the agent already had; the agent's wrong hypotheses were consistent with the evidence it could see, not fabrications. The paper argues the next step for production-debugging agents is a forensics layer supplying the access the agent lacks.
  - locator: abstract
  - evidence_label: anecdotal signal (a single field observation, eight incidents, one production system)
  - limitations: abstract only; small N (eight incidents in one system); no comparison condition (an agent given the missing access was not tested in what was read).
  - relationship to existing claims: a new, concrete real-world instance for I-0009 (agent-actionable error/recovery guidance) with a distinct emphasis — the gap here is observational access (what the agent can see), not recovery-instruction wording (C-0018) or interface drift (C-0078). Worth naming as its own sub-category within I-0009: an "access gap," separate from a "guidance gap."

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — "access gap vs. reasoning error" is a finer attribution split than agent-vs-environment alone), #7 (recovery)
- general: LayerLens's own shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail) are real API/record-based systems where an agent's visible tool surface may likewise omit state a human debugger would reach for — worth a design-review note alongside I-0009's existing audit plan.
