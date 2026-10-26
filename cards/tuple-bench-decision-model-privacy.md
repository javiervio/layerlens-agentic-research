# TUPLE-Bench: Evaluating and Mitigating Privacy-Utility Trade-offs in Typed Decision Models

- authors_or_org: Yiqu Yang, Qiaoyuan Zheng, Yang Tian, Yu Fan, Elliott Ash
- canonical_url: https://arxiv.org/abs/2610.23668v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.AI)
- discovered_via: feed
- doi_or_arxiv_id: 2610.23668v1
- version: v1
- published_at: 2026-10-16
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: typed decision models, judge confidence exposure, privacy leakage, T-05/I-0010

## Claims from this source
- C-0069: Typed decision models (the "Jev"-style category: a narrow, typed verdict plus a probability/confidence field) can leak withheld information through those auxiliary fields even when the model is instructed not to reveal it. Across nine models on paired synthetic cases where a recipient should learn only a coarse category, not its fine-grained cause, 91.88%-99.93% of responses revealed the withheld cause through direct selection or residual scores, and even when the cause was excluded from the candidate set entirely, full outputs (confidence + per-candidate probabilities) still enabled 62.85%-75.35% recovery on held-out cases versus 51.04%-57.64% using only the selected category (50% chance baseline). Full outputs reduced downstream cost in all 27 model-task comparisons, but confidence fields specifically increased leakage without a consistent cost benefit. The authors propose workflow-constrained privacy quantization (WCPQ) to reduce leakage while preserving downstream workflow behavior/cost.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; synthetic paired cases, not a real-world deployment; nine models, not a census; the leakage finding is about a *cause* being inferable from auxiliary fields, a different property from the "confidence is miscalibrated" caution T-05 already carries.
  - relationship to existing claims: a genuine, concrete build caution for I-0010/F-0010 (confidence-aware judge verdicts): the idea's hypothesis is to expose a Judge's own confidence/probability fields in the UI; this paper shows those exact fields (confidence, residual scores) are a documented channel for leaking information the system was trying to withhold. Distinct from C-0049/HATEDECIDE (which questions whether explicit criteria/decomposition improve *accuracy*) — this is about *information leakage*, a different risk dimension on the same feature idea.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution / judge verdict design). Directly actionable: if LayerLens ever exposes a Judge's or Scorer's raw confidence/probability alongside a verdict (I-0010's hypothesis), it should audit whether those fields let a recipient infer something the verdict was supposed to keep coarse (e.g. a specific policy violation reason that should stay generalized for a given viewer's permission level).
