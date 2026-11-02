# When Agents Fail: Model or Harness--Who's to Blame?

- authors_or_org: Shao Zhang, Hangfan Zhang, Yuanyuan Shi, Hao Li, Min-Le Su, Kangcong Li, et al.
- canonical_url: https://arxiv.org/abs/2610.32483
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.CL)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.32483v1
- version: v1
- published_at: 2026-10-23
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox; arxiv.org itself unreachable this session)
- sections_read: abstract
- topics: harness/model attribution, benchmark comparability, agent evaluation methodology

## Claims from this source
- C-0093: The paper's title states its thesis directly: agentic benchmark performance reflects the *joint* behavior of model and harness, so harnesses must be evaluated through their interaction with models, not assumed neutral. The authors propose five measures — **Valid Completion Rate (VCR)**, **Model-Harness Fit**, **Cross-Model Fit**, **Interaction Residuals** (pairing-specific strengths/weaknesses hidden by component-level summaries), and **Token Load** — and evaluate four general-purpose harnesses (OpenCode, Codex CLI, Pi CLI, DeepAgents) against four core models plus two native model-harness systems, across six benchmarks (context management, tool use, long-context planning, multimodal interaction, artifact handoff): **111 evaluation settings, 52,168 trajectories**. Key finding: **"harness rankings vary across models and benchmarks"**, and "similar task scores can accompany distinct execution profiles" — a harness that wins on task score can still differ sharply in how it got there (completion reliability, token cost).
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; specific VCR/Fit numbers per harness-model pair not seen; four harnesses and four models, not a census.
  - relationship to existing claims: **independently corroborates and extends C-0044 ("Finding the Right Fit")** — a different author group, a much larger trajectory count (52,168 vs. C-0044's scale), and a more complete measurement framework (five named metrics vs. two headline numbers) for the same underlying finding that harness is a first-class, non-ignorable confound. Strengthens T-01 and I-0004's build caution.

## LayerLens relevance
- open question(s) touched: #1 (comparability), #9 (comparison as the signature surface).
- This is the single largest-scale, most methodologically complete confirmation yet that any LayerLens comparison view must pin harness identity as a first-class dimension (I-0004's existing build caution from C-0044), not just model and version — now backed by two independent, large-N studies rather than one.
