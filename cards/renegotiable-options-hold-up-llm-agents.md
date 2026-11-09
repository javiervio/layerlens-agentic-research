# Renegotiable Options Fail to Prevent Hold-Up Between Two Profit-Maximizing Frontier LLM Agents

- authors_or_org: Junwei Yao, Zike Yang, Yongxi Zhou, Yanxian Chen, Jianan Liu, Jiaxi Wen, et al.
- canonical_url: https://arxiv.org/abs/2610.40961v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.MA harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.40961v1
- version: v1
- published_at: 2026-10-29
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: multi-agent trust/negotiation, contract design, game theory

## Claims from this source
- C-0119: In the hold-up problem (a seller can adapt a unit to a buyer at a cost before price is set, so a foreseeing seller does not adapt), a "renegotiable option" contract raised human investment from 41.5% to 67.2% of pairs in a prior human lab experiment (Hoppe and Schmitz) even though game theory predicts the option should fail once the buyer can let it lapse and offer its own price. The authors had Claude Opus 5.5 and GPT-6.1 Sol, each told to maximize its own side's profit, play the same one-shot game under four contract regimes plus a reference-price control. The agents matched game theory, not the human result: under the renegotiable option no seller adapted, under an option that structurally rules out renegotiation every seller did. Removing the explicit profit-maximization instruction left investment unchanged. Changing payoffs so the buyer would exercise the option regardless of adaptation, no seller adapted (agents did not reflexively adapt whenever an option existed or its price covered the cost).
  - locator: abstract (verbatim)
  - evidence_label: bounded empirical (a controlled, two-model, multi-regime experiment directly replicating a named human-subjects study's design)
  - limitations: abstract only; one-shot (not repeated) play; two models tested; the "profit-maximization instruction" ablation and payoff-restructuring checks are useful robustness checks but still a small number of named contract regimes.
  - relationship to existing claims: a concrete, controlled demonstration that a contract mechanism empirically validated to work *between humans* does not transfer to profit-maximizing LLM agents, because the agents reason closer to the game-theoretic prediction than humans do — directly relevant to nursery thesis N-04 (multi-agent trust/coordination as its own subfield) and a genuinely new angle (contract design, not collusion or bias) within it.

## LayerLens relevance
- open question(s) touched: #13 (multi-agent scope — if LayerLens ever evaluates multi-agent negotiation/contracting scenarios, human-validated mechanism designs cannot be assumed to carry over to agent-vs-agent play without re-testing)
