# OpenAI Decisions API — a frontier lab ships the Jev-pattern as a first-class product

- authors_or_org: OpenAI
- canonical_url: unconfirmed exact page (OpenAI's own announcement not independently opened this run; openai.com is EGRESS_BLOCKED in this sandbox, newly confirmed)
- discovered_url: via WebSearch, cross-referenced against inbox/reference/LATEST.md's Latent Space entry ("Why Dwarkesh is Wrong about Computer Use + How OpenAI shipped its Jev competitor in 1 Week", https://www.latent.space/p/devday-2026, 2026-09-30) and the competitor-inbox's Langfuse entry noting OpenAI gpt-6-luna decision-model evaluators
- discovered_via: feed (reference/competitor inboxes, titles) then search
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: announced around OpenAI DevDay 2026 (~2026-09-30 per Latent Space); public beta opened to all developers 2026-10-06 per one secondary source
- retrieved_at: 2026-10-12
- source_type: post (vendor product launch, read via multiple secondary/aggregator summaries; sources disagree on exact timeline and pricing)
- access_scope: incomplete access (several independent secondary summaries agree on the core mechanism; pricing and exact launch-status details conflict across sources and are flagged as unconfirmed)
- sections_read: n/a (secondary summaries only)
- topics: structured decision models, LLM judges, confidence/typed verdicts, competitive landscape

## Claims from this source
- C-0052: OpenAI's Decisions API (a dedicated `/v1/decisions` endpoint, powered by GPT-6 Luna) takes a developer-defined question plus a fixed set of allowed answers and returns a selection (predicate / choice / score) instead of generated text — the same "System One," typed-decision category TypeSafe AI's Jev opened in September 2026 (C-0032/C-0033). OpenAI states roughly 150ms latency versus ~1.6s for a standard Luna call (no independent latency benchmark published per the sources found). Sources disagree on launch status (limited preview vs. public beta opened to all developers on 2026-10-06) and on pricing (one source: $0.10/M input tokens, no output-token charge, versus Jev's reported $0.042/M — more than 2x Jev's rate; another source says no pricing had been published as of 2026-09-30). One difference from Jev: the Decisions API accepts image input, which Jev does not yet support. Langfuse has already shipped evaluators for gpt-6-luna decision-model calls, working alongside existing TypeSafe Jev support.
  - locator: multiple independent secondary summaries (firecrawl.dev, dealroom.ai, langfuse.com changelog, and others), cross-checked for consistency; genuine disagreement flagged rather than resolved
  - evidence_label: incomplete access (no OpenAI primary source opened; the event itself — a major lab launching a directly competing product in the same category within about three weeks of the category's own debut — is corroborated across multiple independent outlets even though pricing/timeline specifics are not)
  - limitations: no primary source; conflicting secondary reports on launch status and pricing, explicitly not resolved here; independent latency/accuracy benchmarks for the Decisions API were not found by any source searched.
  - relationship to existing claims: the single strongest validation yet of thesis T-05's "industry response" sub-thread and idea I-0010 (confidence-aware/decision-model judges) — not a research paper or a second startup, but a frontier model lab (OpenAI) shipping the same typed-decision pattern as a core API product within weeks of the category's debut, independently of TypeSafe AI. Together with C-0049 (an independent academic evaluation of the category, HATEDECIDE) this gives I-0010 evidence from three independent lineages (Jev's own group, an unrelated academic group, and a competing frontier lab), which is enough to promote I-0010 from L0 to L1 this run.

## LayerLens relevance
- open question(s) touched: #2 (attribution/judge trust). This is the clearest evidence yet that "typed, narrow, confidence-bearing decision models as a judge primitive" is becoming industry-standard infrastructure, not a single vendor's bet — raises the priority case for I-0010/F-0010 (though maturity promotion, not a build decision, is what this run can respon­sibly do). A genuinely competitive dynamic (OpenAI undercutting or matching Jev's pricing) also means the category's unit economics may keep shifting quickly; worth rechecking soon (see recheck date).
