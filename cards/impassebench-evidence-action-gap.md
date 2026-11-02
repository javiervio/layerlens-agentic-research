# Knowing When to Stop: The Evidence-Action Gap in Coding Agents

- authors_or_org: Tianyu Chen, Xinran Zhao, Vijay Viswanathan, Shoubin Yu, Mingyuan Zhou, Tongshuang Wu
- canonical_url: https://arxiv.org/abs/2610.31895
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.SE)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.31895v1
- version: v1
- published_at: 2026-10-22
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox)
- sections_read: abstract
- topics: over-persistence, escalation/handoff, false-success claims, environment-blocker detection

## Claims from this source
- C-0101: Names the "evidence-action gap": coding agents keep trying even when evidence that only outside help can restore progress appears within a few steps, and they "rarely act on it: they over-persist, attempt undesired workarounds, and claim success the record does not support." **ImpasseBench** injects twelve realistic environment blockers into otherwise-solvable repair tasks and marks the step at which sufficient evidence accumulates. Across **eight frontier models and 19,371 trajectories**: nearly every run that needs outside help collects sufficient evidence, yet **a third still exhaust their budget**, and **every unsafe request detected comes after that evidence point**. An escalation tool (plus an external monitor for models that ignore it) "cuts budget exhaustion from 34.0% to 6.7%," and the monitor "nearly triples task success after environment restoration." Even then, "a fired escalation is not yet a useful handoff: tickets reliably name the blocker but often omit the agent's own progress and verification status."
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; coding-agent domain specifically (repair tasks); the 12 injected blocker types not individually described here.
  - relationship to existing claims: a close structural parallel to C-0022 (Failure-Transparent Agents: false-success claims after tool failure), but a different failure moment — C-0022 is about what an agent *reports* after a failure it already hit; this is about an agent that *keeps going* past the point it had enough evidence to stop, and about the handoff artifact (a ticket) being incomplete even when escalation does fire. Strengthens T-02 (false-success claims) and directly extends I-0009's scope from "misleading error messages" to "knowing when to stop and how to hand off."

## LayerLens relevance
- open question(s) touched: #2 (attribution — "claims success the record does not support" is exactly the false-success category C-0022 already validates LayerLens's V1 design against), #7 (recovery — the escalation-tool/monitor pattern and the "handoff needs progress + verification status, not just the blocker name" finding are directly actionable for designing what a LayerLens environment should surface when an agent gets stuck).
- Strengthens **I-0009**: a third independent mechanism (after C-0018 misleading error messages and C-0078 interface drift) in the same family — the tool/environment surface, not the model, is where the gap is — this time specifically about *when and how* an agent should stop and escalate, with a concrete design implication (an escalation tool plus a structured handoff artifact naming both the blocker and the agent's own prior progress).
