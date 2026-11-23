# Recalibrating a Typed-Decision Model in an Afternoon: A Hands-On Recipe for Laya's Confidence Scores

- authors_or_org: Mohammed Nayeem Khan, Aliyas Ahmad Misri
- canonical_url: https://arxiv.org/abs/2611.16499v1
- discovered_url: inbox/arxiv/LATEST.md (cs.SE, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.16499v1
- version: v1
- published_at: 2026-11-12
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: decision models, calibration, judge confidence

## Claims from this source
- C-0163: A typed-decision model (like TypeSafe AI's Jev/Laya) returns a per-option probability that code compares to a threshold to answer, abstain, or escalate. On 1,065 synthetic, LLM-labelled items, the released "Laya" checkpoint has a pooled ECE of 0.073 but a bucket-macro ECE (averaged over buckets grouped by question type and option count) of 0.143 — the 12-option bucket is over-confident by +0.22 and the 3-5-option bucket under-confident by 0.05, canceling out in the pooled number. A single global temperature makes pooled ECE worse (0.173); a cross-fitted temperature per bucket brings macro-ECE to 0.073-0.089; after recalibration, a gate aimed at 10% error answers 46.3% of items (10.5% wrong) versus 6.9% on the original published confidences.
  - locator: abstract
  - evidence_label: bounded empirical
  - limitations: abstract only; a single named checkpoint (Laya); synthetic, LLM-labelled evaluation items, not real production decisions.
  - relationship to existing claims: a concrete, quantified build caution for I-0010 (confidence-aware judge verdicts) — a pooled/aggregate confidence calibration metric can hide large per-bucket miscalibration in exactly the kind of decision-model pattern I-0010 proposes exposing, and naive global recalibration can make things worse. Directly extends the T-05 industry-response thread (Jev/TypeSafe AI, HATEDECIDE, OpenAI Decisions, Comet's independent test) with a hands-on calibration audit of the category's own flagship product.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — a judge's exposed confidence number needs per-category, not just aggregate, calibration checking)
- general: if LayerLens ever exposes a Judge/Scorer's own confidence (I-0010), this paper's bucket-macro-ECE method is a candidate validation check before trusting that confidence number at face value.
