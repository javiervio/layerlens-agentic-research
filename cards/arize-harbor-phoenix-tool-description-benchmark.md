# Arize: "How to test agent tool descriptions with Harbor and Phoenix"

- authors_or_org: Arize AI
- canonical_url: https://arize.com/blog/how-to-test-agent-tool-descriptions-with-harbor-and-phoenix/
- discovered_url: inbox/competitors/2026-W43.md (Arize section, via arize.com/blog/feed)
- discovered_via: feed
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-10-12
- retrieved_at: 2026-10-26
- source_type: post (vendor blog; arize.com EGRESS_BLOCKED per every prior run, read via WebSearch summary)
- access_scope: incomplete access
- sections_read: WebSearch summary only
- topics: tool-surface testing, I-0009, Braintrust/Harbor ecosystem convergence

## Claims from this source
- C-0086: Arize published a concrete, reproducible worked example of testing a tool description's effect on agent behavior: editing one tool description reduced an agent's (Codex's) unnecessary skill loads from 51 to zero and lowered the benchmark run's cost from $11.85 to $8.34, with correctness unchanged on the benchmark. The method ran the same 18 questions three times per agent configuration via Harbor (Braintrust's sandboxed-eval framework, each attempt in a fresh container) with the Phoenix plugin, comparing configurations and inspecting tool calls in Phoenix; the workflow is define tasks/reference answers, validate the verifier, establish a baseline, then compare a revised tool description against the same benchmark.
  - locator: WebSearch summary of arize.com's own walkthrough post
  - evidence_label: incomplete access (vendor's own worked example; not independently reproduced; full task/question set not retrieved)
  - limitations: a single benchmark run (18 questions x 3 repeats per configuration) on one specific tool-description edit; a small, illustrative case study, not a general finding about tool-description effects.
  - relationship to existing claims: a concrete, quantified instance of I-0009's general theme (tool-surface legibility affects agent efficiency, not just correctness) — complements C-0078 (SchemaShield-Lite) by showing the inverse direction: a well-written tool description measurably reduces wasted/unnecessary tool calls and cost, not just prevents drift-induced failures. Also a notable ecosystem-convergence data point: this is Arize's own product (Phoenix) integrating with Braintrust's Harbor framework, a competitor-to-competitor integration this knowledge base had only seen mentioned in passing before (competitive.md's Braintrust entry, 2026-10-05 update).

## LayerLens relevance
- open question(s) touched: #2 (attribution — unnecessary tool-call counts are themselves a legible failure signature), general (tool surfaces). Strengthens I-0009 with a second concrete, numbers-bearing vendor example (after the Arize/Harbor/Phoenix workflow itself, which is also a candidate reference design for how LayerLens might let an author iterate on a system type's own tool descriptions and measure the effect, directly analogous to LayerLens's own "Optimize" tooling for prompts).
