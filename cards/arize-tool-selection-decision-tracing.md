# Arize: Agent tool selection — the tool your agent almost called

- authors_or_org: Nancy Chauhan, Arize AI
- canonical_url: https://arize.com/blog/ai-agent-tool-selection-decision-tracing/
- discovered_url: inbox/competitors/LATEST.md (Arize feed, 2026-W44)
- discovered_via: feed (competitor harvester) then search
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-10-19
- retrieved_at: 2026-11-02
- source_type: post
- access_scope: incomplete access (WebSearch summary; arize.com remains EGRESS_BLOCKED, consistent with every prior run since 2026-09-28)
- sections_read: n/a (search summary only)
- topics: decision tracing, tool-selection fallback thresholds, judge/grading of tool choice

## Claims from this source
- C-0109: Arize's Phoenix platform added "decision tracing" with a new DECISION span kind, recording a probability for every tool option the model rejected, not just the one it picked. The post demonstrates a fallback design: a confidence-gated router (threshold 0.7) where below-threshold decisions defer to the chat model's own tool choice, and at/above-threshold decisions use the dedicated decision model's pick. Reported comparison on "first tool matched our label": chat-model-alone 78%, always-enforced decision-model 95%, gated (threshold) version 91%. The always-enforced version's failure mode: forced onto the router's pick, the chat model sometimes could not complete a step (one named example repeated three times: "Let me look up your orders first" and stopped). Tool choices were graded with an LLM judge plus human annotation, written onto the decision span.
  - locator: WebSearch summary of the Arize blog post
  - evidence_label: incomplete access (vendor's own post, read via search summary only, not opened directly)
  - limitations: the exact method for choosing the 0.7 threshold not captured; vendor's own benchmark on its own tool/task, not independently verified; a single worked example.
  - relationship to existing claims: a direct extension of last run's Arize/Harbor+Phoenix tool-description finding (C-0086) — same underlying capability area (tool selection/routing instrumentation) but a different mechanism (confidence-gated routing vs. tool-description editing) — and a concrete, numbers-bearing instance of the TypeSafe/Jev-style "decision model + escalation on low confidence" pattern (T-05/I-0010) applied specifically to *tool selection* rather than judging an output.

## LayerLens relevance
- open question(s) touched: #2 (attribution — a logged "the tool your agent almost called" is a legible near-miss record, directly relevant to I-0009's goal of distinguishing tool-surface problems from model reasoning problems).
- Strengthens **I-0009** (now with Arize's tool-selection-confidence instrumentation as a fourth, more product-shaped reference pattern alongside C-0018, C-0078, C-0097) and **I-0010** (a concrete confidence-gated-escalation instance applied to tool routing, not just judging — widening the pattern's observed scope beyond the Jev/decision-model cluster).
