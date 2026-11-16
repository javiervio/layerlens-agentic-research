# More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty

- authors_or_org: Burkay Tunçtürk, Koorosh Aslansefat, Yiannis Papadopoulos, Bao Nguyen
- canonical_url: https://arxiv.org/abs/2611.07140
- discovered_url: inbox/arxiv/2026-W46.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.07140v1
- version: v1
- published_at: 2026-11-04
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: multi-agent reliability, Bayesian reliability modeling, combining rules

## Claims from this source
- C-0143: Teams building multi-agent LLM systems often assume more agents mean more reliability, but the usual evidence (average benchmark accuracy) ignores the input mix a deployed system meets and the rule merging the agents' answers. Building on HIP-LLM (a hierarchical imprecise-probability assessment of single LLMs), the authors propose a framework combining it with a Bayesian network of the system's failure logic, where agent failure-probability intervals propagate through a network in which the combining rule itself can fail, producing a "reliability envelope" showing which evidence limits it. In a pipeline extracting regulated chemical-hazard statements, majority voting over three models protected against the weakest model but did not clearly exceed the best one, and a voter failing on 5% of demands would largely erase its advantage over the middle model. "More agents yield a more defensible reliability claim, not automatically a more reliable system."
  - locator: abstract, verbatim
  - evidence_label: proposal / interpretation (a reliability-modeling framework) with bounded empirical illustration (one pipeline).
  - limitations: abstract only; one applied pipeline (chemical-hazard extraction); the combining-rule failure mode is modeled, not independently measured across many real systems.
  - relationship to existing claims: a new, directly relevant nuance for T-01/T-08: voting/consensus across multiple agents is not a free reliability upgrade, and the mechanism combining their answers is itself a point of failure that must be accounted for — complements C-0016 (agreement is not verification) from a reliability-engineering rather than epistemic angle.

## LayerLens relevance
- open question(s) touched: #5 (reliability), #13 (multi-agent scope, if LayerLens ever evaluates ensembles/voting agents rather than a single agent against an environment).
