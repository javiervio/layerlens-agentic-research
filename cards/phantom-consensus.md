# Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making

- authors_or_org: Disha Sheshanarayana, Rajat Subhra Pal, Manjira Sinha, Tirthankar Dasgupta
- canonical_url: https://arxiv.org/abs/2611.08971
- discovered_url: inbox/arxiv/2026-W46.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.08971v1
- version: v1
- published_at: 2026-11-06
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: multi-agent integrity, consensus, pluralistic ignorance, attribution

## Claims from this source
- C-0129: LLMs shift their public decisions after observing ambiguous social signals while reporting inaccurate estimates of what other agents privately judged, even when the group's recorded private judgments do not actually support the apparent consensus ("phantom consensus," a pluralistic-ignorance-style pattern). On PHANTOM-Bench, across nine closed- and open-weight models, ambiguous public signals degrade decision quality; public accuracy drops by as much as 47.8 percentage points, and collective-rationality failures reach 47.3% in the most susceptible setting. Revealing the agents' recorded private decisions (transparency) repairs many failures without revealing the gold label, though recovery varies by model.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; nine models, one benchmark (PHANTOM-Bench); mechanism of "ambiguous social signal" not detailed in the abstract.
  - relationship to existing claims: new, strong independent evidence family for T-08 (multi-agent emergent integrity failures): visible agreement can misrepresent actual private judgments, extending the pattern T-08 already tracks (collusion, evasive coordination, laundered bias) to apparent-consensus-that-isn't.

## LayerLens relevance
- open question(s) touched: #13 (multi-agent scope — if LayerLens ever grades multi-agent systems, "did the agents actually agree, or only appear to" is a distinct, measurable failure mode a per-agent grader would not catch); #2 (attribution, adjacent — this is a different flavor of "the visible record understates the truth" than C-0080's Believed-but-Not-Said).
