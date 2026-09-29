# Planarian: Managing Agent State with Statepoints

- authors_or_org: Jinnan Guo, Hao Mark Chen, Kapil Vaswani, Andrew Paverd, Peter Pietzuch
- canonical_url: https://arxiv.org/abs/2609.35366
- discovered_url: inbox/arxiv/LATEST.md (2026-W40 harvest)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2609.35366
- version: v1
- published_at: 2026-09-28
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: abstract only (verbatim, directly read via inbox harvester; arxiv.org blocked, no independent GitHub mirror found this run)
- sections_read: abstract
- topics: environment lifecycle, sandbox infrastructure, human control and recovery

## Claims from this source
- C-0020: Planarian is an agent runtime that introduces "agent statepoints" — consistent, restorable point-in-time versions of BOTH local (file/process) and remote (external service) environment state — exposed via three primitives: **snapshot** (capture local state via incremental process/filesystem snapshotting, plus recorded compensating actions for remote state), **rollback** (restore local checkpoint + replay compensating actions to undo remote changes), and **fork** (branch multiple isolated explorations from one statepoint). Reported results: enables agents to undo mistakes and explore alternatives in parallel, improving task quality by up to 15x; lets users recover from erroneous actions with only 3% overhead.
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly; full paper/methodology not opened)
  - limitations: abstract only — no benchmark/task details, no info on what "task quality" metric means or which tasks the 15x figure applies to; single source.
  - relationship to existing claims: **independent corroboration of nursery N-03** (environment lifecycle/checkpoint infra as an industrial pattern) — a different team (Imperial College / Microsoft-affiliated authors, distinct from DeepSeek's DSec, C-0012) converging on the same snapshot/rollback/fork primitive, and explicitly extending it to *remote* (not just local sandbox) state via compensating actions, which DSec's abstract did not address. This is the second independent family N-03 needed; see thesis promotion in changelog.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — snapshot/rollback/fork is a concrete, named mechanism for "what can a person inspect, interrupt, correct, and resume without rebuilding the whole task"); #3 (deterministic replayability as a surface).
- Directly strengthens I-0007 (environment lifecycle legibility + checkpoint/branch a run) to a second independent source, and is arguably the closest external match yet to LayerLens's own deterministic-minting + replay story, now generalized to *remote* system state (our Salesforce/Linear/Stripe/etc. system types are exactly this "remote state" case).
