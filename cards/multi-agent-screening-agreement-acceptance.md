# Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You

- authors_or_org: Benjamin Chang, Dell Zhang
- canonical_url: https://arxiv.org/abs/2611.12705v1
- discovered_url: inbox/arxiv/LATEST.md (cs.MA, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.12705v1
- version: v1
- published_at: 2026-11-09
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: judges, agreement, formal bounds, recall estimation

## Claims from this source
- C-0176: When AI agents screen items for a costly human assessor (agentic search, e-discovery, paper review), only what passes screening gets judged, so recall is structurally hard to pin down. The paper formally characterizes what each kind of evidence can and cannot establish, even with unlimited data: agreement among agents shows they concur, never that they are right, however many agents agree; acceptance by the human assessor gives precision but only a lower bound on recall; knowing which agents found which relevant items gives an upper bound on recall if agents' finds are not negatively correlated, and caps what one more agent can add if agents are interchangeable. Without further assumptions, recall can only be pinned down (to any chosen accuracy) by judging a random sample of the items that were NOT passed, and the needed sample size does not grow with the number of agents.
  - locator: abstract
  - evidence_label: proposal (a formal/theoretical result, not an empirical study)
  - limitations: abstract only; a theoretical contribution — no empirical validation on a real screening deployment described.
  - relationship to existing claims: a formal, generalizable extension of T-05's "agreement is not verification" line (C-0016, C-0133/Copies Are Not Confirmations) — this paper proves the limit precisely: agreement, however measured, never bounds correctness, and the only way to estimate what was missed is to sample the rejected set, not the accepted one.

## LayerLens relevance
- open question(s) touched: #2 (attribution — relevant to any LayerLens feature that would infer agent/judge reliability from inter-judge agreement alone)
- general: a caution worth keeping alongside I-0005/I-0010 — if LayerLens ever reports agreement between multiple judges/graders as a reliability signal, this paper is a reminder that agreement never establishes correctness, only a sample of what was rejected can.
