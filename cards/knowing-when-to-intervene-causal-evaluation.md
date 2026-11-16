# Knowing When to Intervene: Causal Evaluation of AI Agents

- authors_or_org: Ayush Sawarni, Wenqian Xing, Tijana Zrnic, Ramesh Johari, Vasilis Syrgkanis
- canonical_url: https://arxiv.org/abs/2611.09792
- discovered_url: inbox/arxiv/2026-W46.md (cs.AI)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.09792v1
- version: v1
- published_at: 2026-11-06
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: human oversight, intervention, causal evaluation, audit prioritization

## Claims from this source
- C-0134: Deciding whether to intervene in an agent's trajectory (verify its current output, steer it, escalate to a human or a costlier model) is fundamentally a causal-inference question — whether the intervention's causal effect on the final outcome is beneficial — made hard by the dynamic setting (impact depends on current context/environment and the agent's future behavior). The authors develop the first methodologically grounded framework for estimating the causal effects of randomized interventions within agent trajectories, using a relatively small dataset of trajectories collected under randomized interventions (verification/screening) to estimate the dynamic causal effect of a rich class of contextual intervention policies; the same structural parameters can build "safety leaderboards" capturing the risk of various agentic actions for audit prioritization. Applied to tau-bench Retail, ToolSandbox, and ImpossibleBench, intervention effects vary substantially across agent actions and states.
  - locator: abstract, verbatim
  - evidence_label: proposal / interpretation (a methodological framework; abstract read directly) with bounded empirical validation on three named benchmarks.
  - limitations: abstract only; "relatively small dataset" scale not quantified in the abstract; benchmarks are tau-bench Retail, ToolSandbox, ImpossibleBench (all already named reference points in SOURCES.md).
  - relationship to existing claims: new; the first source in this knowledge base to frame "when should a human/costlier check step in" as a measurable causal-effect question rather than a design-principle argument (T-04's prior evidence, C-0047/C-0075/C-0100, is scope-contract, survey, or taxonomy-based, not causal-estimation-based). Distinct mechanism, same territory.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — a principled way to decide *when* intervention is worth its cost, not just what a confirmation should show); #2 (attribution — "safety leaderboards" of per-action risk are a candidate input to LayerLens's own attribution/Insights surface). Feeds I-0006 and I-0001 (reliability-aware run allocation is adjacent to intervention-allocation).
