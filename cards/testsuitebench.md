# TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications

- authors_or_org: Kazuki Egashira, Niels Mündler-Sasahara, Mark Niklas Müller, Martin Vechev
- canonical_url: https://arxiv.org/abs/2610.13065
- discovered_url: inbox/arxiv/LATEST.md (2026-W42 harvest)
- discovered_via: feed
- doi_or_arxiv_id: 2610.13065v1
- version: v1
- published_at: 2026-10-09
- retrieved_at: 2026-10-19
- source_type: paper
- access_scope: abstract (verbatim, directly read via arXiv harvester inbox)
- sections_read: abstract only
- topics: verification-suite quality, mutation testing, test generation

## Claims from this source
- C-0062: TestSuiteBench (165 open-source applications, each with a structured spec, reference implementation, reference test suite, and ~74 mutants per app on average, 73% killed by exactly one reference test and on average only 0.2% of remaining tests) finds even frontier coding agents generate weak test suites from specifications: mutation scores below 60%, despite suites being largely valid (88% of generated tests pass on the reference implementation). Generated suites often lack relevant input combinations and are smaller than reference suites. Implementations generated for the same specifications pass 82% of reference tests. The authors frame this as "agents can build software they cannot verify."
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; 165 applications is substantial but still a specific corpus, not a census; mutation-score threshold (60%) is the authors' own bar
  - relationship to existing claims: a new, structurally distinct family for T-02 alongside C-0046 (Discriminating Fixture Coverage) — both show verification/test-suite quality is itself a gap, not just benchmark scoring logic; this one is specifically about *agent-generated* test suites (a product-shaped capability gap, not an audit of pre-existing human-made suites like C-0046).

## LayerLens relevance
- open question(s) touched: #2 (attribution — a test suite that passes its own author's implementation while missing real defect classes is a verification-side failure, not necessarily an agent-side one); general (candidates for LayerLens's own benchmark-authoring/generation flows — "generate a benchmark from documents" should itself be checked against this gap before being trusted as ground truth).
