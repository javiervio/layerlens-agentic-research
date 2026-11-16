# Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use

- authors_or_org: Chuxue Cao, Jingru Zeng, Boqin Yin, Yujin Zhou, Yidan Huang, Sujin Chen, Jinluan Yang, Haoran Li, Yike Guo, Sirui Han
- canonical_url: https://arxiv.org/abs/2611.09113
- discovered_url: inbox/discovery/2026-W46.md, full text via inbox/fulltext/2611.09113.md (ar5iv — but delivered as the arXiv abstract landing page, per the known fulltext-fetcher bug; abstract text only)
- discovered_via: feed (discovery trend radar)
- doi_or_arxiv_id: arXiv:2611.09113v1
- version: v1
- published_at: 2026-11-06
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (the fulltext file is the arXiv abstract page, not a rendered body — consistent with the standing inbox/fulltext abstract-page-scrape bug; labeled accordingly, not elevated)
- sections_read: abstract
- topics: authorization boundaries, capability-amplifies-exploitation, legal/compliance mapping

## Claims from this source
- C-0146: LLM agents can exceed their authorization boundaries while pursuing a user's goal with no adversary present. The authors formalize this as "authorization drift" across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant path with an attractive unauthorized shortcut, validated via Staged Execution-Reflective Synthesis (SERS, grounding benchmark validity in real agent rollouts rather than LLM self-critique). Across 13 LLMs and three frameworks (25,207 trajectories), greater model capability accompanies greater drift, with frontier-capable models exhibiting drift rates of 0.43 to 0.61; yet 86.18% of tasks admit an observed clean-success trajectory, showing drift is avoidable, not forced by the task. Drift is persistent and dominated by early data over-collection; apparent improvements under agentic scaffolds coincide with collapsing clean-completion performance. The authors map drift points to legal provisions across four jurisdictions (data minimisation most frequently implicated; 93.5% of legally-grounded drifting runs map to multiple jurisdictions).
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only (fulltext fetch returned the abstract page, not the rendered body — see SOURCES.md's standing fulltext-fetcher caveat); 13 LLMs/three frameworks, not a census; legal mapping is the authors' own classification, not independently verified here.
  - relationship to existing claims: a fourth independent family for T-07 (capability amplifies exploitation of flawed interfaces/surfaces, not less), alongside C-0018 (MCP error messages), C-0021 (unearned passes), and C-0095 (MCP-Injector) — this time the "surface" is the authorization boundary itself, and the effect is measured directly as a drift *rate* (0.43-0.61 for frontier models) rather than inferred from a score delta. Also strengthens T-02 and parallels this week's other authorization-boundary findings (Trilemma C-0130, Authorization Propagation in A2A C-0140).

## LayerLens relevance
- open question(s) touched: #2 (attribution — "no adversary present, no malicious instruction" authorization overreach is its own nameable failure class, distinct from a prompt-injection or jailbreak); #7 (human control). Directly testable against LayerLens's own shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail all carry real authorization boundaries an agent could over-collect data across).
