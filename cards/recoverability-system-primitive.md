# Recoverability as a System Primitive for Long-Horizon AI Agents

- authors_or_org: Zhihui Zhang and one other author (full author list not confirmed — only "Zhihui Zhang and 1 other author" surfaced in the search summary)
- canonical_url: https://arxiv.org/abs/2609.13672
- discovered_url: WebSearch, following up the pending "rollback-security cluster" noted in the 2026-09-29 pass-2 run log (ACRFence, "When Can Agents Safely Checkpoint, Fork, Restore, and Merge?", "Recoverability as a System Primitive")
- discovered_via: search
- doi_or_arxiv_id: arXiv:2609.13672
- version: v1
- published_at: 2026-09 (exact day not confirmed)
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: incomplete access (arxiv.org EGRESS_BLOCKED to both /abs and /html; no companion GitHub repo found via search; WebSearch summary only)
- sections_read: none directly; summary only
- topics: agent recovery, checkpoint governance, long-horizon agents, environment lifecycle

## Claims from this source
- C-0034: Proposes "recoverability" as a distinct system primitive from mere state-restoration: the system must explicitly select a *supported* starting point and a *permitted* recovery action (or explicitly withhold automatic continuation), rather than silently resuming from any technically-restorable checkpoint. The reference design (Recoverability Primitive Runtime, RPR) separates an Evidence/Policy layer, a Governance layer, and an Enactment/Audit layer, and the audit trail records restoration fidelity, adherence to the governing decision, and the final task outcome as separate pieces of evidence. States that accurate restoration and a successful completion can together conceal a disallowed starting point.
  - locator: WebSearch summary only, no primary-text locator available.
  - evidence_label: incomplete access.
  - limitations: no primary text; no quantitative results, benchmark, or worked example captured; single paper; author list not fully confirmed.
  - relationship to existing claims: **directly answers the gap C-0026 ("Safe to Resume?") named** — where C-0026 argues state-correct rollback does not imply secure/valid resumption, this paper proposes a governance-layer mechanism (an explicit, auditable "is this recovery action permitted" decision, separate from "did the restore work technically") as exactly that missing second question. Treat as a proposed answer to a named risk, not yet independently validated — strengthens T-06 with a design-pattern response, distinct from (not a duplicate of) the five prior mechanism-existence families.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery), #3 (deterministic replayability as a surface). Directly sharpens I-0007/F-0007's build caution from C-0026: "legible" should mean showing not just *that* a checkpoint/branch happened but *which governing rule permitted it*, as a distinct, inspectable piece of evidence alongside the restore itself.
