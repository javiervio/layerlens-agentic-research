# Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing

- authors_or_org: Oktie Hassanzadeh, Dharmashankar Subramanian
- canonical_url: https://arxiv.org/abs/2610.13823
- discovered_url: inbox/arxiv/LATEST.md (2026-W42 harvest)
- discovered_via: feed
- doi_or_arxiv_id: 2610.13823v1
- version: v1
- published_at: 2026-10-09
- retrieved_at: 2026-10-19
- source_type: paper
- access_scope: abstract (verbatim, directly read via arXiv harvester inbox)
- sections_read: abstract only
- topics: reliability, run-to-run variance, benchmark validity, LLM-as-judge/semantic query engines

## Claims from this source
- C-0058: Re-executing the text/tabular workloads of three semantic-query benchmarks (SemBench, LRO-Bench, UDA-Bench) through their own harnesses, logging 1.2M model calls, finds 0.07%-10.2% (up to 24.0% on one task) of per-row outputs change across five re-runs at temperature 0; plans amplify row-level changes exponentially into answer-level changes (a few percent of extracted values change on UDA-Bench, but ~two-thirds of answers do); reanalyzing SemBench's own published executions finds 21% of text results change quality between executions, including on engines whose plans are deterministic; 16 of 28 LRO-Bench implementation-recommendation tests are not settled by the benchmark's own executions.
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; three specific benchmark harnesses, not a general census; "changing rows are rows on which models disagree with each other" is a correlational observation, not a causal mechanism
  - relationship to existing claims: independent corroboration of T-01 (reliability over capability) — a fourth/fifth-scale, very large (1.2M calls) real-system family, notable for reanalyzing a benchmark's *own already-published* results and finding they don't hold up to re-execution, which is a sharper and more damning instance of the pattern C-0019 ("Identical Runs, Different Results") established for coding-agent benchmarking.

## LayerLens relevance
- open question(s) touched: #5 (reliability vs. one lucky pass), #1 (comparability — "several per-query system comparisons... are not settled by the executions the benchmarks run")
