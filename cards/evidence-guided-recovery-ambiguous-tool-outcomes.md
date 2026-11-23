# Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial Execution

- authors_or_org: (authors not captured in discovery-harvest entry; see canonical URL)
- canonical_url: https://arxiv.org/abs/2610.41453
- discovered_url: inbox/discovery/LATEST.md (hf-daily, 2026-W47, 4 upvotes)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.41453
- version: v1 (unconfirmed)
- published_at: date unknown (surfaced 2026-W47)
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the discovery inbox)
- sections_read: abstract
- topics: recovery, retry, environment lifecycle, evidence-based planning

## Claims from this source
- C-0170: Tool timeouts leave agents facing ambiguous outcomes and partial execution (an action may have failed, committed, or remained in flight while later steps already completed). This paper formulates evidence-guided task recovery over approved obligations, provider capabilities, and states compatible with public evidence, using a shared admissibility check (key expiry, authorization timing, dependencies, residual effects) and a terminal certificate that separates actual goal satisfaction from publicly-supported safe completion. In a finite 37-assignment study, planning and three active controls each certify 28 completions; a preregistered, assignment-held-out comparison across 58 paired units in 19 task families finds planning advice certifies 30 completions versus 9 for evidence prompting (36.2 percentage points, exact family sign-flip p=0.0078), using 272 proposals versus 399; all 116 trajectories pass independent replay.
  - locator: abstract
  - evidence_label: bounded empirical
  - limitations: abstract only; small N (37, 58 units); "two local model bundles" in the comparison, generalization to frontier models not described in what was read.
  - relationship to existing claims: a direct, mechanistically distinct extension of C-0100 ("Permission to Retry")'s four-obligation decomposition — this paper's "terminal certificate separating goal satisfaction from safe completion" is a sharper, formally-tested version of exactly the distinction C-0100 named but did not fully operationalize.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — a remote-write retry/recovery feature needs to distinguish "did the task actually succeed" from "is it safe to call this done")
- general: strengthens I-0007's remote-state retry/recovery hypothesis with a second, independently-tested formalization of the obligation-decomposition idea C-0100 introduced.
