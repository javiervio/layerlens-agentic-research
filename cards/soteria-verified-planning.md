# Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents

- authors_or_org: Mike He, Ankush Desai, Sharad Malik, Aarti Gupta
- canonical_url: https://arxiv.org/abs/2611.17880v1
- discovered_url: inbox/arxiv/LATEST.md (cs.SE, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.17880v1
- version: v1
- published_at: 2026-11-13
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: formal verification, oversight, runtime enforcement, safety vs utility

## Claims from this source
- C-0161: LLM agents executing multi-step tool calls must satisfy both utility (completing the task) and safety (conforming to policies/constraints), which existing approaches treat as a tradeoff — blocking an unsafe action prevents a violation but can strand the agent with no principled way to recover. Soteria generates a structured plan, formally verifies it against specifications before any tool invocation, and uses the verified plan during execution both to keep the agent on a specification-conformant trajectory and to provide guidance when an unsafe action is blocked. Across multiple tool-use benchmarks, Soteria achieves 1.7x the average task success rate of the best baselines with no policy-specification violations.
  - locator: abstract
  - evidence_label: bounded empirical
  - limitations: abstract only; "multiple benchmarks" not named; the exact guidance Soteria offers when blocking an action (what it tells the agent to try instead) is not described in the abstract.
  - relationship to existing claims: directly answers part of T-04's core gap (oversight tooling answers "when to block" but not "what to do when blocked") with a concrete mechanism — the verified plan itself supplies the alternative. Also a new T-02 family (verification-by-construction applied to planning, not just evaluation) and converges this week with EvoTrias (C-0162) and Microsoft's PDD Kit (C-0176) on formal verification as an emerging layer over agent-generated artifacts.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — "stranded with no principled way to recover" is exactly T-04's framing; Soteria's verified-plan-as-guidance is a candidate mechanism, distinct from naming a specific consequence in a confirmation, but adjacent)
- general: part of this run's three-source convergence on formal/proof-based verification of agent-generated plans and code (Soteria, EvoTrias, PDD Kit) — see new idea I-0015.
