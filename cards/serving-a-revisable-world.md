# Serving a Revisable World: Versioned Execution for Interruptible Agents

- authors_or_org: Yanxin Zhang, Rahul Sharma, Nitin Vegesna, Zheyu Fu, Chang Liu, Trivikram Krishnamurthy
- canonical_url: https://arxiv.org/abs/2610.01160v1
- discovered_url: inbox/arxiv/LATEST.md (2026-W41 harvest, cs.DC)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2610.01160v1
- version: v1
- published_at: 2026-10-01
- retrieved_at: 2026-10-12
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the harvested inbox; arxiv.org itself not reachable this run)
- sections_read: abstract
- topics: environment lifecycle, interruption/revision, versioned execution, LLM serving

## Claims from this source
- C-0041: `\retire` is an LLM-serving control-plane redesign around "versioned execution": requests own scheduling/memory resources, but execution *versions* own "authority" (the permission to publish output or install state). On revision, `\retire` first revokes the obsolete version's authority, bounds its remaining execution, and certifies which completed prefix (e.g. KV state) its successor can inherit, rather than treating a revision as abort-then-restart. Implemented in vLLM; reduces revision-to-successor time-to-first-token by a median 17.1% in controlled paired experiments, and a replay of recorded real coding-agent interruption arrivals emitted no obsolete output while every final version kept progressing through repeated revisions.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly; first-party systems implementation in vLLM)
  - limitations: abstract only; "controlled paired experiments" not detailed; serving-layer (inference infra) scope, not an environment/tool-state scope the way DSec/Crab/Planarian are.
  - relationship to existing claims: twelfth independent family for thesis T-06, but at a different layer than the rest of the cluster (inference serving, not sandbox/tool state) — a fourth distinct angle (after infra scale, RL training, agent-runtime recovery) showing the same revoke/preserve/branch shape recurring even inside the model-serving stack itself. "Authority" (who may publish/install state) is a precise vocabulary addition relevant to I-0007's governance-layer build caution (C-0034).

## LayerLens relevance
- open question(s) touched: #3 (replayability), #7 (recovery — specifically mid-task revision when a user changes instructions). The authority/certified-prefix framing is a concrete pattern for how a LayerLens checkpoint/branch feature could state, legibly, exactly what is and is not inherited across a revision.
