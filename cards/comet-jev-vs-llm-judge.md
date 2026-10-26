# Comet/Opik: "Jev vs. LLM-as-a-Judge for AI Evals" — a concrete, independent production comparison

- authors_or_org: Comet (Aswin Thiyagarajan)
- canonical_url: https://www.comet.com/site/blog/jev-model-vs-llm-as-a-judge/
- discovered_url: inbox/competitors/2026-W43.md (Comet / Opik section, via comet.com/blog/feed)
- discovered_via: feed
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-09-29 (per feed); retrieved via WebSearch 2026-10-26
- retrieved_at: 2026-10-26
- source_type: post (vendor blog)
- access_scope: incomplete access (WebSearch summary of the post's opening; full methodology and the 103-disagreement breakdown not retrieved)
- sections_read: WebSearch summary only
- topics: decision-model category (T-05/I-0010), independent empirical comparison

## Claims from this source
- C-0084: On 1,000 real production evaluation turns, Comet ran TypeSafe AI's Jev (a decision-only model returning a probability rather than prose) head-to-head against a gpt-4o-mini LLM-as-a-judge. Jev was roughly 3.5x cheaper and 3.8x faster, and the two agreed on 897 of 1,000 turns (897/1,000 = 89.7% raw agreement), leaving 103 disagreements. Jev's pricing is cited as $0.042 per million tokens read. Comet frames the reusable methodology as "test whether a new [decision] model matches the judge on your own traffic," rather than taking any vendor's benchmark claim at face value.
  - locator: WebSearch summary of comet.com/site/blog/jev-model-vs-llm-as-a-judge
  - evidence_label: incomplete access (full post and the 103-disagreement analysis not independently read; headline numbers are from the post's own opening summary as relayed by search)
  - limitations: a single evaluation vendor's own test (Comet, not an uninvolved academic group); no stated inter-rater reliability or breakdown of which 103 cases disagreed and why; 89.7% raw agreement is not adjusted for chance (c.f. C-0027's caution that raw agreement overstates chance-corrected discrimination by 33-41 points in a different, larger study).
  - relationship to existing claims: this is a fourth independent lineage for T-05/I-0010 (after Jev's own research group, HATEDECIDE's academic test, and OpenAI's competing Decisions API) — notably, the first one run by a different *evaluation infrastructure vendor* testing the claim against its own real production traffic, rather than a research benchmark or the originating company's own materials. The concrete, if partial, agreement number (897/1000) is more specific than this knowledge base's prior decision-model evidence, though it still needs the same chance-correction caution C-0027 already flags for judge-agreement statistics generally.

## LayerLens relevance
- open question(s) touched: #2 (attribution / judge verdict design). Reinforces I-0010's existing pending action (a product check on whether LayerLens's own Judge/Scorer verdicts expose confidence today) rather than changing it — this is corroborating evidence for the category's momentum and cost claims, not new information about whether exposing confidence is itself a good design (that question is untouched by this specific post).
