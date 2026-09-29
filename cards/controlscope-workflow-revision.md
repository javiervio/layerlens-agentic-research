# ControlScope: Workflow Revision and Reliability in LLM Agents

- authors_or_org: Jingjie Ning, Xueqi Li, Yibo Kong, Dongting Li
- canonical_url: https://arxiv.org/abs/2609.34313
- discovered_url: inbox/arxiv/LATEST.md (2026-W40 harvest, cs.SE)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2609.34313
- version: v1
- published_at: 2026-09-28
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: abstract only, read directly and verbatim via the arXiv inbox harvester
- sections_read: abstract
- topics: human/agent recovery, workflow revision granularity, environment lifecycle

## Claims from this source
- C-0030: ControlScope studies how much of a running agent workflow should be revised when something goes wrong, comparing three repair granularities from the same public execution state: KEEP (continue the generated code as-is), ARG (edit only the next tool call's data arguments), and FULL (replace the unfinished workflow entirely). Framed as "nested permissions" that separate the repairs available to a reviewer from the actions an agent actually selects. Evaluated across filesystem tasks, ALFWorld, and AppWorld. Reported results are mixed and granular rather than a single "FULL always wins" story: on 20 filesystem tasks, FULL completed 15-16 vs. 13 for KEEP under one review-draw setup, but 10-13 vs. 13 under a different (fast-draw) setup; on ALFWorld, KEEP/ARG/FULL scored 85/86/87 on one task cohort and 134/134/127 on another; on a 585-instance AppWorld panel, differences between granularities were small. A "five-call protection" scheme saved 19.4% of logged model output at the cost of one success across 20 fresh runs. Frozen replays showed cases where a viable agent-written fix was interrupted by a later, unnecessary revision.
  - locator: abstract, verbatim.
  - evidence_label: bounded empirical (abstract read directly).
  - limitations: abstract only; results are heterogeneous across task suites and draw conditions (not a clean monotonic finding), and the authors' own numbers show granularity choice can help, hurt, or barely matter depending on setup — treat as an early, mixed-results paper, not a settled recommendation for "how much to revise."
  - relationship to existing claims: new — first claim specifically on *repair granularity* (how much of a workflow to revise) as opposed to *whether* to allow rollback/checkpoint at all (T-06's cluster). Distinct evidence for I-0007 (recovery persona: not just "can you branch/checkpoint" but "how much should a human or agent be allowed to change when recovering").

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — this is a concrete taxonomy of repair scope: continue / edit-argument / replace-workflow), #6 (adjacent — synthetic-task legibility touches similar mid-run editing questions).
- Strengthens I-0007/F-0007 with a new angle: environment lifecycle legibility isn't only about checkpoint/branch existing, it's also about what granularity of revision a person or agent should be offered when something breaks — a design menu (continue / tweak the next step / start the remaining workflow over), not a binary.
