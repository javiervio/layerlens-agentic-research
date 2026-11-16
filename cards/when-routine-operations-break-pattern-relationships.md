# When Routine Operations Break Architectural Pattern Relationships in LLM Agent Harnesses

- authors_or_org: Boming Xia, Qinghua Lu, Dino Sejdinovic, Liming Zhu
- canonical_url: https://arxiv.org/abs/2611.09088
- discovered_url: inbox/arxiv/2026-W46.md (cs.SE)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.09088v1
- version: v1
- published_at: 2026-11-06
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: harness fragility, guardrails, silent failure, architectural patterns

## Claims from this source
- C-0139: LLM agent harnesses distribute tool mediation, state management, and safety guardrails across native services, independently written plugins, and configuration; routine operations (no code change) can silently change the runtime order or retained state that architectural pattern relationships require. Studying five relationships tied to the Guardrail Enforcement Point, Autonomy Controller, and Blackboard patterns across five released harnesses and fourteen independently written plugins (via "PatternOps," an assessment procedure tracing requirements to the providers/records that realise and decide them), the authors found such operations broke relationships silently: after a plugin was reapplied or an allow rule saved, policy stopped evaluating edits while every plugin stayed active, and a prohibited edit executed. Which alternative allocation held depended on the specific requirement; some preserved required order/state on tested paths while others prevented prohibited effects but missed edits rejected elsewhere.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; five named harnesses and fourteen plugins, not a census; "a prohibited edit executed" is one demonstrated instance, not a measured rate.
  - relationship to existing claims: strengthens T-01 (harness as a first-class, under-engineered artifact — direct extension of C-0113 Ring-0/AaOS's "deployed harnesses miss OS-grade protections" finding, now with a concrete silent-guardrail-failure mechanism) and T-02 (a guardrail silently failing to re-evaluate after a routine config change is a new, concrete instance of "declared isolation is not verified isolation").

## LayerLens relevance
- open question(s) touched: #2 (attribution — a silently-broken guardrail is a distinct failure category from either the agent or the environment misbehaving); #7 (human control — a human approved an "allow rule" believing a guardrail was active). Relevant design-review caution for LayerLens's own trust wall: a routine config/plugin change should not be able to silently stop a protection from being evaluated.
