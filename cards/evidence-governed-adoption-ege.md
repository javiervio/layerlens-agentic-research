# Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents

- authors_or_org: Subodh Lonkar
- canonical_url: https://arxiv.org/abs/2611.16378v1
- discovered_url: inbox/arxiv/LATEST.md (cs.MA, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.16378v1
- version: v1
- published_at: 2026-11-12
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: self-modification, governance, statistical adoption testing, trust

## Claims from this source
- C-0167: Autonomous agents that modify their own prompts, memories, tools, workflows, or policies face a governance gap: a plausible modification is not necessarily suitable for persistent adoption, because candidate selection is adaptive, evaluators may be imperfect, and local gains can hide degradation against an earlier baseline. Evidence-Governed Evolution (EGE) separates candidate generation from confirmatory adoption, evaluates frozen candidates on fresh paired audits, requires meaningful improvement on a prespecified primary objective, protects declared capabilities via reference-relative non-inferiority tests, and applies governance constraints before bounded canary deployment. The paper establishes an evaluator-calibrated simultaneous lower-bound construction for a countable sequence of adaptively generated candidates (combining candidate-wise Hoeffding bounds with calibration samples comparing the operational evaluator against a prespecified reference), formalizes reference replacement via bridge tests, derives a cumulative degradation bound along a versioned reference lineage, and gives an audit-planning condition relating effect-size margin, sample sizes, and acceptance probability.
  - locator: abstract
  - evidence_label: proposal (a formal statistical framework, illustrated by a Monte Carlo stress test; not evaluated on a real deployed agent in what was read)
  - limitations: abstract only; a Monte Carlo illustration is not the same as a real-world validation; the framework's practical overhead (how many fresh paired audits are needed) is not stated.
  - relationship to existing claims: extends T-02's "benchmark maintenance is ongoing, not one-time" (C-0021) and "claims stored beside verdicts, never used as evidence" (C-0022) into the self-modification setting specifically — a formal statistical answer to "when should a self-generated change actually be trusted and kept."

## LayerLens relevance
- open question(s) touched: #5 (reliability — "local gains can hide degradation against an earlier baseline" is directly relevant to any LayerLens-hosted optimizer loop), general (the optimizer already gates promotion on holdout-gained-positive/lost-zero; this paper's versioned-reference-lineage and cumulative-degradation-bound framing is a candidate rigor upgrade to compare against)
- general: relevant to LayerLens's own prompt optimizer (per-round, tuning/holdout split, gated promotion) — EGE's formal non-inferiority testing is a stricter standard worth comparing the existing gate against.
