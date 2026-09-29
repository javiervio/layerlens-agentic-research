# Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias

- authors_or_org: Justin D. Norman, Michael U. Rivera, D. Alex Hughes
- canonical_url: https://arxiv.org/abs/2606.19544
- discovered_url: WebSearch (this run's deliberate contradicting-evidence slice, searching for counter-evidence to T-05)
- discovered_via: search
- doi_or_arxiv_id: arXiv:2606.19544
- version: v1
- published_at: 2026-06-17
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: incomplete access (arxiv.org EGRESS_BLOCKED this run; description assembled from consistent WebSearch summaries citing specific numbers, treated as secondary, not primary text; authors state code/data release is deferred to publication, so no companion repo was available to upgrade this)
- sections_read: none directly; search-summary only
- topics: LLM-as-judge, evaluation reliability, judge bias, agreement metrics

## Claims from this source
- C-0027: A systematic, large-scale evaluation of 21 LLM-as-judge models from 9 providers across three benchmarks (MT-Bench, JudgeBench, RewardBench), tested under three protocols (agreement, consistency, bias audit) over 118 runs and approximately 541,000 individual judgments. Headline findings (as reported by search summaries, consistent across sources): raw percent-agreement overstates chance-corrected discrimination (vs. Cohen's kappa) by 33-41 percentage points across the 21 models; high test-retest reliability (kappa >= 0.95 for some judges) coexists with severe position bias (>0.10) in some of the same, production-deployed judges — i.e., "the most reproducible judges [are] among the least valid."
  - locator: WebSearch summaries of the abstract; the same 33-41pp figure and >=0.95/>0.10 pairing appeared consistently across independent search result snippets, increasing confidence the summary is accurate even without primary-text confirmation.
  - evidence_label: incomplete access (secondary summary only, but from a large, well-specified systematic study, not a single anecdote).
  - limitations: no primary text read; cannot independently verify per-benchmark breakdowns or exact model list; single paper, though it is itself a large-N systematic study rather than a small pilot.
  - relationship to existing claims: **independent corroboration of thesis T-05** (LLM judges carry structural, identity/behavior-linked bias) — a third, much larger-scale family alongside C-0002 (self-preference pilot, 4 models) and C-0014 (identity conformity, 12 models). Distinct emphasis: this paper is about *general* reliability/validity/position-bias, not specifically same-model-family favoritism, so it strengthens T-05's broader claim ("LLM judges do not evaluate neutrally") without being additional evidence specifically for I-0005/F-0005's narrower same-family-flag hypothesis.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — a Judge verdict's own reliability needs a visible confidence signal), differentiator #3 (reproducible, defensible grading).
- The "most reproducible judges are the least valid" framing is a strong, quotable caution against treating a Judge's *consistency* across re-runs as a proxy for its *correctness* — directly relevant to any LayerLens UI that might show a Judge's stability as reassurance.
