# Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries

- authors_or_org: Junchi Liao
- canonical_url: https://arxiv.org/abs/2610.23362v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.AI)
- discovered_via: feed
- doi_or_arxiv_id: 2610.23362v1
- version: v1
- published_at: 2026-10-16
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED per standing pattern; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: monitor validity, safety evidence pipelines, agent oversight infrastructure

## Claims from this source
- C-0068: Runtime safety/policy monitors can have "evidence-path failures": a detector correctly recognizes a policy-relevant signal (e.g. a regex match on leaked content), but the framework's own plumbing strands that evidence before it reaches the enforcement decision point, so the system behaves as if nothing was detected even though recognition occurred. Using "canary contracts" (known payloads placed on a changed evidence surface) applied to public framework repair histories, the author confirms 18 such evidence-path failures across 11 LLM/agent safety project groups and 4 implementation ecosystems: 9 are repairs of an established enforcement boundary, 8 are new-surface policy-coverage gaps, 1 is boundary-only. 14 of 18 reach real enforcement consequences (7 native action outcomes, 6 configured enforcement boundaries, 1 synthetic-consumer consequence).
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; single author; "public framework repairs" as the data source means this samples bugs that were found and fixed, not an unbiased incidence rate; the taxonomy (carrier/adapter/authority/surface families) is the author's own framework, not independently validated.
  - relationship to existing claims: new angle for T-02 and T-03 — distinct from "the benchmark score can be gamed" (C-0001/C-0006) and from "a clean monitor readout coexists with reward hacking" (C-0045/Near-Zero Monitor Readout): this is about evidence that *was* correctly recognized by a detector but never reached the decision point that was supposed to act on it. A failure mode one level more specific than "monitor is wrong" — "monitor was right, and it didn't matter."

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — this is itself a new attribution category: "the evidence existed, the enforcement decision never saw it," distinct from agent error or environment error), #11 (reviewer surface — a Riley-persona reviewer trusting a compliance signal needs to know the evidence actually reached the point that was supposed to act on it, not just that a detector fired somewhere upstream).
