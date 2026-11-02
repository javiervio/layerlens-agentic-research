# HarnessMM: Recursive Self-Improvement for Harness Token Efficiency

- authors_or_org: not stated in what was read
- canonical_url: https://arxiv.org/abs/2610.32813
- discovered_url: inbox/discovery/LATEST.md (arxiv recency, 2026-W44)
- discovered_via: feed (discovery harvester)
- doi_or_arxiv_id: arXiv:2610.32813
- version: v1 (assumed)
- published_at: date unknown (discovery harvest gave no explicit date for this entry)
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the discovery inbox)
- sections_read: abstract
- topics: harness token efficiency, decision reuse, cost as a comparability dimension

## Claims from this source
- C-0106: HarnessMM ("Harness Minus Minus") observes that agent harnesses "repeatedly invoke reasoning after tool feedback, even when an earlier call has already fixed the next action," and introduces guarded decision reuse: a controller at the model-tool boundary stores "Executable Decision Graphs" (exact actions, literal arguments, causal dependencies, public guards) and reuses them from observed receipts instead of re-invoking the model, falling back to the original model call for new semantic decisions or unsupported evidence. On HumanEval, preserves Codex success at 90.82% while cutting tokens/task from 66.72k to 47.02k (-29.54%); on a "DeepSeek Harness," success *rises* (71.43% -> 85.71%) while tokens/task fall from 96.28k to 11.62k (-87.93%).
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; author affiliation unknown; two harness/model pairings only; "success rises" alongside large token savings on one of the two is a striking, not yet independently corroborated, result.
  - relationship to existing claims: a cost-focused instance of the T-01 harness cluster — rather than showing harness choice reverses rankings (C-0044, C-0093), this shows harness-internal *engineering* (decision reuse) can change the cost side of the cost-accuracy tradeoff substantially without hurting (and here, apparently helping) accuracy.

## LayerLens relevance
- open question(s) touched: #1 (comparability — a comparison view should account for how much of a harness's token cost is reasoning-reuse-avoidable overhead, a dimension existing build cautions on I-0004 did not yet name).
- Minor direct relevance (an optimization technique for harness builders, not an evaluation-product finding) but worth keeping as a further data point that cost is a live, moving target when comparing agent-harness pairings, reinforcing I-0004's "always show a tradeoff axis" hypothesis.
