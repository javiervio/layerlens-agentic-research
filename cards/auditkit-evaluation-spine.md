# AuditKIT: A Unified Evaluation Spine for Benchmarking, Judging, and Comparing Large Language Models and Agentic Systems

- authors_or_org: Shreeyans Arora, Utsav Avaiya, Zera Lyngkhoi, Hem Gosalia, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu et al.
- canonical_url: https://arxiv.org/abs/2610.22511v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.SE)
- discovered_via: feed
- doi_or_arxiv_id: 2610.22511v1
- version: v1
- published_at: 2026-10-15
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: unified evaluation design, grader/judge separation, missing-evidence handling

## Claims from this source
- C-0074: AuditKIT is a source-available evaluation library that records benchmark accuracy, judge-based assessment, runtime performance, tool-use behavior, and retrieval quality in one result representation, with direction-aware metric contracts and configuration fingerprints. For agents specifically, it provides turn-aware tool-call matching, separates parallel from sequential execution, and — notably — distinguishes verified task outcomes from trajectory-level diagnostics, marking missing or unobservable evidence as "unscored" rather than counting it as a failure. Seven case studies (model comparison, serving runtimes, retrieval, tool calling, interoperability) show that answer extraction, runtime behavior, and metric selection choices change evaluation outcomes.
  - locator: abstract, verbatim
  - evidence_label: documented capability (first-party design description, read via abstract)
  - limitations: abstract only; "source-available" status and governance/maintainer identity not established; no independent verification of the seven case-study results.
  - relationship to existing claims: an independently-arrived-at design pattern that parallels LayerLens's own shipped choices — separating a verified/deterministic outcome from a trajectory-level diagnostic rhymes with LayerLens's Grader/Judge split, and marking missing evidence "unscored, not failure" rhymes with "the agent's own claims are stored beside verdicts, never used as evidence" (independently validated again, as C-0022/Failure-Transparent Agents already did). Worth watching as a possible open-source convergence point, not yet confirmed as a commercial competitor.

## LayerLens relevance
- open question(s) touched: #1 (comparability), #2 (attribution). A second independent confirmation (after C-0022) that "mark the ambiguous case honestly instead of silently scoring it as pass or fail" is becoming a recognized good practice in the field, not a LayerLens-specific design choice.
