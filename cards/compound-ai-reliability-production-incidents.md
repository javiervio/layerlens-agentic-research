# Compound AI System Reliability: A Failure Taxonomy and Resilience Pattern Catalog from 150 Production Incidents

- authors_or_org: Rudrendu Kumar Paul, Sourav Nandy
- canonical_url: https://arxiv.org/abs/2610.02503v1
- discovered_url: inbox/arxiv/LATEST.md (2026-W41 harvest, cs.DC)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2610.02503v1
- version: v1
- published_at: 2026-10-01
- retrieved_at: 2026-10-12
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the harvested inbox; arxiv.org itself not reachable this run)
- sections_read: abstract
- topics: reliability, failure taxonomy, production incidents, resilience patterns

## Claims from this source
- C-0042: Analysis of 150 real production incident reports (open-source compound-AI projects plus anonymized enterprise deployments) yields a taxonomy of 23 failure modes in 5 categories: retrieval, generation, tool, orchestration, and integration failures. Controlled fault-injection experiments measure resilience patterns: circuit breakers reduce cascade propagation by 89%, output quality gates catch 73% of silent degradation before user impact, and component isolation reduces blast radius by 64%. Systems using 3+ of the catalog's patterns cut mean-time-to-recovery by 71% versus unstructured monitoring baselines.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly; grounded in real incident reports, not only benchmark audits)
  - limitations: abstract only; incident corpus composition (how many open-source vs. enterprise, which systems) not detailed; fault-injection "controlled experiments" methodology not seen.
  - relationship to existing claims: a new, distinct evidence family for T-03 (failure attribution emerging as the practical debugging unit) — the first grounded in real production incidents rather than benchmark/trace audits (C-0001, C-0006, C-0015, C-0017 are all benchmark- or research-trace-based). The 5-category/23-mode taxonomy is a genuinely different attribution scheme (component-boundary failures: retrieval/generation/tool/orchestration/integration) than the agent-vs-environment-vs-grader split LayerLens's own trust wall draws, worth comparing rather than assuming overlap.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — a production-grounded taxonomy to compare LayerLens's own attribution categories against), #9 (comparison/trajectory diff, adjacent). Not tied to a new idea/feature row this run (dedup discipline): strengthens I-0003/F-0002 as corroborating evidence that attribution-by-category is a real, measured practitioner need, not only a research framing.
