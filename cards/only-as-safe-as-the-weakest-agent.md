# Only as Safe as the Weakest Agent: A Break That Appears Only When the System Is Multi-Agent

- authors_or_org: Keegan Wang, Anantika Mannby
- canonical_url: https://arxiv.org/abs/2611.17520v1
- discovered_url: inbox/arxiv/LATEST.md (cs.MA, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.17520v1
- version: v1
- published_at: 2026-11-12
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: multi-agent systems, delegation, capability and safety, harness

## Claims from this source
- C-0158: Attacks long patched against frontier models used in isolation can break the same, unmodified models when they operate as multi-agent systems (demonstrated on Claude Code, Codex, and a reference harness, all with their own unmodified sub-agent mechanisms), via forged records planted in a file store the system searches. When a strong orchestrator model searches the store itself, harmful revisions are committed in almost zero of over 1,000 trials. But when that same orchestrator delegates the search to a cheaper sub-agent — which is what these harnesses are built to do — the same models on the same facts fail on 20/180, 44/180, 75/180, and 553/900 trials (across four tested configurations). The system's safety lands near the weak reader's level, not the strong orchestrator's, even though the orchestrator itself is unchanged; simulations over 18 models show the same effect in the delegation chain.
  - locator: abstract
  - evidence_label: bounded empirical (demonstrated on real, unmodified production harnesses: Claude Code, Codex, plus a reference harness)
  - limitations: abstract only; the forged-record attack is one specific vector (a planted file-store record), not a general claim about all delegation patterns; exact per-model breakdown of the four fail-rate numbers not visible from the abstract.
  - relationship to existing claims: a sharp, directly-demonstrated extension of T-07 (capability does not self-correct for bad interface/environment design) into multi-agent delegation specifically, and a new T-08 family — the first in this cluster demonstrated on real, unmodified, widely-used production harnesses (Claude Code, Codex) rather than only constructed research games.

## LayerLens relevance
- open question(s) touched: #13 (multi-agent scope — a concrete, production-harness-demonstrated reason why a multi-agent system's safety is not simply "as safe as its strongest model"), #2 (attribution — a failure here would misleadingly implicate "the model" when the actual cause is a delegation-pattern design choice)
- general: directly sharpens T-07's Stratix implication (well-designed environments matter more, not less, as capability rises) with a concrete delegation-specific instance; relevant if LayerLens's own agent-under-test harnesses are ever audited for sub-agent delegation patterns.
