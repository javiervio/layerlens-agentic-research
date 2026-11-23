# Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents

- authors_or_org: (authors not captured in discovery-harvest entry; code at github.com/ZJU-REAL/decision-agents)
- canonical_url: https://arxiv.org/abs/2611.17167
- discovered_url: inbox/discovery/LATEST.md (hf-daily, 2026-W47, 36 upvotes)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.17167
- version: v1 (unconfirmed)
- published_at: date unknown (surfaced 2026-W47)
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the discovery inbox)
- sections_read: abstract
- topics: decision models, judges, reinforcement learning, reward signal design

## Claims from this source
- C-0171: Decision models (typed outputs: a choice among caller-defined options, with a probability per option) have mostly been studied as actors, judged by how well they act. Comparing three decision models and three general LLMs as actors and judges on ALFWorld, and using JEV as a teacher (reward signal) on ALFWorld and WebShop: as actors, all six models are pulled away from a subgoal that must come first by an easier one; as judges seeing the whole trajectory, the same models correctly credit the steps toward that subgoal, and asking "did this action help" (rather than "will the task succeed") separates useful from useless actions; as a teacher, JEV raises a Qwen2.5-1.5B policy trained with GRPO from 72.8% to 82.9% success on ALFWorld and from 56.8% to 71.4% on WebShop. The authors conclude a poor actor can still teach well, because judging an action after the episode ends reveals consequences that acting must anticipate.
  - locator: abstract
  - evidence_label: bounded empirical
  - limitations: abstract only; small model scale for the "teacher" experiment (1.5B policy); whether the pattern holds for frontier-scale policies is untested in what was read.
  - relationship to existing claims: a genuinely new angle for I-0010/T-05's decision-model cluster — the same model class (Jev/JEV) already tracked for judge confidence-escalation is shown here to have a second, distinct use (reward-shaping teacher) separate from the judging-for-a-verdict use case this knowledge base has focused on.

## LayerLens relevance
- open question(s) touched: #2 (attribution — "did this action help" is a step-level credit-assignment question, close in spirit to LayerLens's own attribution-as-a-location ambition)
- general: adjacent to I-0010; relevant mainly as a widening of the decision-model design space (judge, actor, teacher) LayerLens should be aware of if it ever trains or tunes a policy against its own graders.
