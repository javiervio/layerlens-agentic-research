# Decision-model category update: Arize's 8-way benchmark, TypeSafe's $870M raise, confirmed OpenAI pricing

- authors_or_org: Arize (benchmark), Bloomberg via multiple outlets (funding), various
- canonical_url: https://arize.com/blog/decision-model-benchmark/ (Arize); funding reported by Bloomberg, relayed via https://www.channelinsider.com/ai/news-typesafe-ai-870-million-funding-jev-model/ and others
- discovered_url: inbox/competitors/LATEST.md (Arize feed title, 2026-W42 harvest), then WebSearch
- discovered_via: feed, then search
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-10-07 (Arize post); 2026-10-09 (Bloomberg funding report)
- retrieved_at: 2026-10-19
- source_type: post
- access_scope: incomplete access (arize.com EGRESS_BLOCKED to direct WebFetch again this run — DNS resolution failure; all detail via WebSearch summaries of the Arize post and of funding-news coverage)
- sections_read: n/a (search-summary only)
- topics: decision-only judge models, category convergence, funding

## Claims from this source
- C-0057: The "decision-only judge model" category (opened by TypeSafe AI's Jev, 2026-09-15) has, within about three weeks, drawn roughly ten entrants per Arize's own count, including OpenAI, Liquid AI (d1), Cloudflare, AWS, and PostHog, plus an open clone ("Kev") on Hugging Face. Arize's own benchmark compares eight decision models for hallucination detection, LLM evaluation, and agent routing, finding the leaders "closely matched on accuracy" but separated on latency, cost, deployment options, and sensitivity to question wording. Liquid reports its d1 model scored a composite 58.9 versus Jev 1.13's 57.9 on a named public leaderboard, Hugging Face's "Decision Index 0.2.1" — Liquid's own claim to be first to beat Jev on that index. A Liquid researcher cautioned on a podcast that "benchmarks for decision models are very new, and right now you cannot really trust them." Separately, Bloomberg reported TypeSafe AI raised ~$870M at a $7.5B valuation (Series A, led by Andreessen Horowitz, with Sequoia and DCVC participating) roughly three weeks after Jev's launch; TypeSafe claims roughly a third of the Fortune 500 use Jev (its lead investor states 25%), with no customers named and weights not released. OpenAI's Decisions API is confirmed to have launched 2026-10-06 at $0.10 per million input tokens, "more than twice" Jev's reported $0.042/M.
  - locator: n/a (WebSearch summaries; no primary page opened)
  - evidence_label: incomplete access for the benchmark/funding specifics (PROTOCOL.md rule 4: a vendor's or investor's own figures are not independently verified); the existence of a dedicated public leaderboard ("Decision Index") is itself a documented-capability-level fact (multiple independent sources describe it consistently)
  - limitations: arize.com itself unreachable this run (consistent EGRESS_BLOCKED pattern); full Arize results table (all eight models, OpenAI/Cloudflare/AWS/PostHog's own scores) not found; TypeSafe's ARR figure referenced in the original search query was not found in any source and should not be treated as reported
  - relationship to existing claims: strengthens T-05 and I-0010/F-0010 substantially beyond the three-lineage framing recorded 2026-10-12 — the category now has (a) a dedicated, named, third-party-hosted leaderboard (evidence the market treats this as a distinct, comparable category, not a one-off feature), (b) a $7.5B valuation confirming serious capital conviction, and (c) confirmed, resolved pricing dynamics (OpenAI at >2x Jev's per-token rate, resolving the pricing-conflict flag from C-0052). This also surfaces a genuine caution worth recording alongside the enthusiasm: a domain expert on the category's own benchmarks says they "cannot really trust" results yet, echoing this knowledge base's own T-05 caution (C-0027, "the most reproducible judges are among the least valid") applied to the newest entrants in the category too.

## LayerLens relevance
- open question(s) touched: #2 (attribution/judge trust). I-0010's "the category is moving fast, a product check is increasingly time-sensitive" framing is strengthened further: with a dedicated public leaderboard and multiple frontier-scale entrants (OpenAI, AWS, Cloudflare) now in this space, waiting to check whether LayerLens's own Judge/Scorer verdicts could use a confidence-aware, decision-model-style mechanism carries a growing opportunity cost relative to competitors who may adopt one of these off-the-shelf.
