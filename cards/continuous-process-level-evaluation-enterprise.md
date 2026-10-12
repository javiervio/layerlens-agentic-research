# Continuous Process-Level Evaluation for Evolving Enterprise AI Agent Skills

- authors_or_org: Ngoc Phuoc An Vo, Aarya Doshi, Vadim Sheinin
- canonical_url: https://arxiv.org/abs/2610.01833v1
- discovered_url: inbox/arxiv/LATEST.md (2026-W41 harvest, cs.SE)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2610.01833v1
- version: v1
- published_at: 2026-10-01
- retrieved_at: 2026-10-12
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the harvested inbox; arxiv.org itself not reachable this run)
- sections_read: abstract
- topics: process-level evaluation, trajectory evaluation, enterprise agents, attribution

## Claims from this source
- C-0043: A continuous evaluation framework for enterprise agent skills combines outcome-level and process-level checks (tool selection, arguments, execution order, database integrity) via programmatic checks plus a narrowly-scoped LLM judge. Across 240 trials (two skills, two spec variants, two harnesses, three models): of 175 trials that passed every applicable *final numerical* check, 162 (92.6%, 95% CI 87.7-95.6%) still contained another evaluator-detected deviation; under a broader 7-check final-state definition, 151/164 passing runs (92.1%) still violated a trajectory check. Dependency attribution reduced a mean of 6.34 failed checks per run to 2.65 root causes.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly; first-party enterprise production report, not a public benchmark)
  - limitations: abstract only; single enterprise system (a "Value Aware Resiliency" Business Value Determination skill); authors themselves flag longitudinal validation under real API evolution as future work.
  - relationship to existing claims: a strong new, real-enterprise-deployment family for I-0003/F-0002 and T-03 — directly measures how often a final-output-only check would have missed a real deviation (over 90% of the time in this deployment), the most concrete "why trajectory-level attribution matters" number yet recorded. Also a concrete instance of root-cause reduction (6.34 failed checks -> 2.65 roots via dependency attribution), a method worth comparing against LayerLens's own attribution approach.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — directly on point), #9 (trajectory-level comparison). Strengthens I-0003/F-0002 significantly: this is evidence from a live enterprise deployment, not a research audit or benchmark, that "the final answer passed" and "nothing went wrong along the way" are very different claims — core to LayerLens's own "where a failure happens is everything" premise.
