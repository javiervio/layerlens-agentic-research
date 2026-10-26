# Diviner: Agentic RCA with Human-Governed Adaptation for Large-Scale Infrastructure

- authors_or_org: Pradipta Ghosh, Gaurav Mitra, Shripad Nadgowda, Akshil Shah, Junyu Liu, Canturk Isci et al. (Meta)
- canonical_url: https://arxiv.org/abs/2610.21281v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: 2610.21281v1
- version: v1
- published_at: 2026-10-15
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: real production root-cause analysis, attribution, human governance

## Claims from this source
- C-0076: Diviner is a real, production agentic root-cause-analysis (RCA) system operating at Meta, organized around a four-stage reliability lifecycle: Encode (combine reviewed incidents with service-owner expertise into scoped, versioned skills/workflows/typed tools and an incident knowledge graph), Execute (an adaptive Lead plus context-isolated workers apply relevant knowledge to point-in-time evidence and maintain evidence-linked hypotheses), Evaluate (compare saved investigation trajectories against responder-reviewed outcomes, measuring exact cause, useful direction, and "Groundedness"), and Adapt (recurring gaps and on-call feedback drive focused knowledge updates, admitted only after replay, quality checks, and owner approval). The paper explicitly notes generic LLM agents do not solve RCA through tool access alone: they can use stale or mistimed context, interpret failed queries as absent symptoms, report unsupported system state, and overload observability services built for human-paced use.
  - locator: abstract, verbatim
  - evidence_label: documented capability / postmortem-adjacent (first-party description of a real production system, abstract read directly)
  - limitations: abstract only; a single company's internal system, not independently benchmarked against alternatives; "Groundedness" as a metric is not defined in what was read.
  - relationship to existing claims: strengthens T-03 with a rare, real-world (not benchmark-audit) production RCA system from a frontier-scale company, and its "Evaluate" stage (comparing trajectories to responder-reviewed ground truth, explicitly scored for exact cause / useful direction / groundedness) is a concrete, operationalized attribution-evaluation design — close in spirit to what LayerLens's own attribution surface (I-0003) aims to make legible for users, but built for internal on-call engineers rather than product end users. Also independently confirms the "stale or mistimed context" failure mode I-0011/Concord already documents, from a different angle (an RCA agent using stale observability data, not an agent in a mutable test environment).

## LayerLens relevance
- open question(s) touched: #2 (failure attribution), #7 (recovery — Diviner's human-governed "Adapt" stage, where updates are admitted only after replay/quality-check/owner approval, is a concrete precedent for how LayerLens might let an environment or grader evolve safely over time without silently changing what "correct" means, echoing the tau2-bench/C-0003 versioning discipline).
