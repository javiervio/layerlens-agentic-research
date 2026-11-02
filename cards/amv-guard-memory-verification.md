# When Is a Memory Safe Enough to Act On? Action-Conditioned Verification for Long-Lived Agents

- authors_or_org: Yiqi Wang, Yifei Wang, Jiaqi Zhang, Zhangkai Wu, Yiqun Duan, Taotao Cai, et al.
- canonical_url: https://arxiv.org/abs/2610.31446
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.MA)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.31446v1
- version: v1
- published_at: 2026-10-22
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox)
- sections_read: abstract
- topics: stale-memory detection, action-conditioned verification, value-of-information, agent recovery

## Claims from this source
- C-0099: The paper frames whether a remembered fact must be re-checked before acting as **a property of the pending action, not of the memory entry itself** ("the same remembered address can be used unchecked for a routine shipment but should be re-confirmed before a valuable one"). It formalizes this as a sequential-stopping / value-of-information (VOI) problem and builds **AMV-Guard**, a verification gate that extracts the premises a candidate action rests on, calibrates belief about whether each is wrong, and selects checks by bounded VOI. On ToolSandbox, relative to a static verification policy with the same inputs, AMV-Guard **lowers mean verification cost by 33.9% while keeping 100% safe-proceed recall and 0% harmful-gate rate**, and raises "proceed coverage" from 38.83% to 44.17%. A gate-core transfer to AppWorld (carrying over the stopping/VOI logic but not the full pipeline) lowers verification cost by 21.3% at a small cost in safe-proceed recall/task success.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; two benchmark environments (ToolSandbox, AppWorld), not a broad census; "AppWorld transfer" explicitly trades some safety/success for cost, a real tradeoff not fully characterized here.
  - relationship to existing claims: **second independent source and mechanism for I-0011/F-0011** (stale-observation detection), alongside C-0064 (Concord). Distinct mechanism: Concord detects that a *source has changed* and applies update/annotate/suppress policies; AMV-Guard instead asks, for a given pending *action*, which of its memory premises are worth re-verifying given the action's consequence — action-conditioned rather than source-change-conditioned. Together they give I-0011 two genuinely different angles on the same pain point (staleness as a property of the observation's source vs. staleness-worth-checking as a property of the action about to be taken).

## LayerLens relevance
- open question(s) touched: #2 (attribution — staleness/unverified-memory as its own nameable category), #7 (recovery — what should happen once staleness is suspected: this paper's answer is "selectively re-verify, scaled to the action's consequence," a sharper design pattern than Concord's update/annotate/suppress alone).
- **Promotes I-0011/F-0011 from L0 to L1** per the maturity ladder's rule ("multiple independent sources" or "one strong source + outcome + validation plan"): this is now a second, mechanistically distinct source. The VOI framing is additionally a candidate design pattern LayerLens could use directly: scale re-verification effort to what a pending write action would actually do (consistent with LayerLens's own consequence-aware confirmation hypothesis, I-0006) rather than treating all stale observations as equally worth re-checking.
