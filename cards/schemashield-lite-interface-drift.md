# Robust Function Calling for LLM Agents Under Interface Drift

- authors_or_org: Aniruddha Chattopadhyay, Kanishka Halder, Partha Sarathi Roy
- canonical_url: https://arxiv.org/abs/2610.23342v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.AI)
- discovered_via: feed
- doi_or_arxiv_id: 2610.23342v1
- version: v1
- published_at: 2026-10-16
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: tool interface drift, function-calling robustness, I-0009

## Claims from this source
- C-0078: Tool-augmented LLM agents rely on interface text (tool descriptions, argument schemas, the candidate tool list shown at inference time) that can change after deployment even when the underlying tool semantics stay fixed — "interface drift." The authors' lightweight, training-free repair layer, SchemaShield-Lite (schema validation + candidate-set retry for missing tool names + one-shot constrained repair), raised Qwen3.5-9B's DICE-300 accuracy from 0.717 to 0.813 and BFCL-200 accuracy from 0.580 to 0.805, recovering 19/22 and 33/45 drift-induced failures respectively with no observed repair harms. Ablations show candidate-set drift (especially distractor tools) accounts for most of the damage, more than description/schema-text edits alone; naive retry alone does not explain the gains.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; one base model (Qwen3.5-9B) tested; "no observed repair harms" is the authors' own characterization, not independently audited.
  - relationship to existing claims: a second, independent source on the broader theme I-0009 opened with C-0018 (MCP error messages mislead agents) — both are about the tool-calling interface itself (not the agent's reasoning) being the actual point of failure, and both propose a repair that works by making the tool surface itself more legible/robust rather than by making the model smarter. Different specific mechanism (schema/candidate-list drift after deployment, vs. misleading natural-language error messages at failure time), but the same underlying idea: LayerLens's own shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail) are exactly the kind of real, evolving API surface where both failure modes would occur.

## LayerLens relevance
- open question(s) touched: #2 (attribution — "interface drift" is a nameable failure category distinct from agent error), #7 (recovery). Promotes I-0009 from a single-source to a multi-family idea (see ideas/backlog.md).
