# Between Spoilers and Guesswork: Avoiding Over-Specification in Coding Benchmarks

- authors_or_org: Yuanzhe Liu, Bastian Lipka, Avraham Shinnar, Jatin Ganhotra, Yao Ma, Martin Hirzel
- canonical_url: https://arxiv.org/abs/2610.22760v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.SE)
- discovered_via: feed
- doi_or_arxiv_id: 2610.22760v1
- version: v1
- published_at: 2026-10-16
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: benchmark task specification, ground-truth leakage, task feasibility

## Claims from this source
- C-0072: Repository-level coding benchmarks can fail in two opposite directions: under-specification causes "guesswork" (solutions must invent missing information, or resort to contamination/reward hacking), while over-specification causes "spoilers" (solutions can bypass the harder steps a benchmark was meant to measure, shortening its useful adoption life). The authors show that several widely-used benchmarks that added hints to fix under-specification (SWE-bench Pro, FEA-bench, Doc2Feat-bench, Multi-SWE-bench) did so by deriving hints from ground truth, which leaks into the task statement and causes over-specification in some cases. They experiment with specification levels to find a middle ground and will release hints the community can use to get more reliable signal from these benchmarks.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; coding benchmarks specifically; "will release hints" means the proposed fix was not yet independently verified in what was read.
  - relationship to existing claims: a new, specific instance of ground-truth leakage into the task statement itself (distinct from C-0001/BenchJack's V2, "ground truth accessible at runtime" to the *solver* during execution — here the leak is baked into the task description that's shown to the solver from the start). Also directly names the "guesswork vs spoilers" tension that FeasiGen's (C-0007) feasibility work sits adjacent to: under-specification creates false infeasibility/ambiguity, over-specification creates a false sense that a hard benchmark has been "solved."

## LayerLens relevance
- open question(s) touched: #4 (task feasibility — the under/over-specification framing is a sharper vocabulary for exactly this question), #2 (attribution — a benchmark that leaks ground truth into its own task statement is a self-inflicted V2-style vulnerability, relevant when LayerLens's own benchmark-authoring flows, upload/auto-generate-from-docs, add hints or context to a task). Directly testable: does LayerLens's own task-authoring ever add hints that leak the answer key's structure into the visible task statement?
