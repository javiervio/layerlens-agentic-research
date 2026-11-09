# Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems

- authors_or_org: Xiaoyang Wang, Tianrui Wang, Christopher C. Yang
- canonical_url: https://arxiv.org/abs/2610.38215v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.MA harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.38215v1
- version: v1
- published_at: 2026-10-28
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: multi-agent fairness, verifier/audit integrity, attribution

## Claims from this source
- C-0122: Across a full factorial of five model families and four aggregation topologies on 120 real MIMIC-IV emergency cases under counterfactual demographic swaps, no configuration neutralized a racial disparity (all 20 cells gave Black patients more acute triage in the direction of their agents' independent answers). Every model has a topology that amplifies its own baseline gap, but which topology varies by model, so no design is reliably safe or reliably amplifying — the disparity relocates, it is never removed. Late-stage fixes (fairness instructions, demographic masking) left the gap untouched; per-agent self-debiasing widened it, because the bias is already encoded in each agent's ordinary clinical numbers before aggregation. The one intervention that worked: making counterfactual versions visible inside the system and pooling them through deliberation — a "diverse-perspective ensemble" cut the gap 67-94% where all five perspectives pool at every round, with no retraining or architectural change; the one topology that never pools them is the one it cannot reliably repair.
  - locator: abstract (verbatim)
  - evidence_label: bounded empirical (a full-factorial controlled study on real clinical data with counterfactual demographic swaps, a strong experimental design)
  - limitations: abstract only; clinical/MIMIC-IV domain specifically (racial-bias-in-triage), not yet shown to generalize to other bias classes or non-clinical multi-agent tasks.
  - relationship to existing claims: a fourth, structurally distinct addition to nursery thesis N-04 this run — this is about *bias* surviving and relocating through multi-agent deliberation (not collusion or contract failure), and makes a sharp, general-sounding claim with direct product relevance: "per-model, per-output, per-version audits... can certify the parts but never the committed decision." This is a genuinely new caution for any system (including LayerLens's own Graders/Judges/Scorers, if ever composed into a multi-agent voting/consensus pattern) that treats agreement among independently-correct-looking components as evidence of a fair or correct committed outcome.

## LayerLens relevance
- open question(s) touched: #13 (multi-agent scope — the strongest single piece of evidence yet that "does the verification model extend to grading multi-agent systems" is not a hypothetical question: single-component audits can certify the parts and still miss the committed decision), #2 (attribution — "disparity laundering" is a candidate name for a failure category no part-level grader would catch)
