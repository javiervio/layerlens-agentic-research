# CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments

- authors_or_org: Monojit Banerjee, Zhujun Lan, Defu Cao (repo under github.com/salesforce-misc)
- canonical_url: https://arxiv.org/abs/2610.32004
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.HC)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.32004v1
- version: v1
- published_at: 2026-10-23
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox)
- sections_read: abstract
- topics: stateful enterprise benchmarks, contract-grounded evaluation, CRM/business-process agents

## Claims from this source
- C-0094: CRM-Agent-Bench is an execution-grounded benchmark of **555 stateful, multi-turn CRM tasks across nine business domains and 36 capability tags**, built around a "deployable-agent benchmark should jointly assess four facets: the outcome an agent reaches, the trajectory it takes, its operational viability, and its policy compliance." Each task supplies a **task-specific executable contract** — checks over actions, arguments, order, response, target state, and protected state — and "success is the strict conjunction of the checks declared for that task." Across sixteen evaluated agent systems, strict success spanned **64.32% to 83.60%**, with closely-grouped leading systems diverging sharply in cost and per-domain reliability.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; authored with Salesforce-affiliated contributors (per the GitHub org), so may reflect a particular house style of what "CRM correctness" means; per-domain/per-system breakdowns not seen.
  - relationship to existing claims: new — the closest external benchmark design found yet to LayerLens's own system-type shape (CRM/Salesforce-style stateful, rule-bound, mutable-record environments), and independently arrives at the same "outcome alone is not enough" four-facet framing LayerLens's own graders (answer, actions, judge, state) already implement.

## LayerLens relevance
- open question(s) touched: #1 (comparability — "closely grouped leading systems diverge sharply in cost," echoing HAL's cost-accuracy argument), #2 (attribution — the four-facet contract decomposition is itself an attribution scheme).
- This is an unusually direct external validation of LayerLens's Environments pillar's premise: a credible, Salesforce-adjacent benchmark independently concluded that evaluating a CRM-shaped agent requires checking outcome + trajectory + operational viability + policy compliance together, not outcome alone — effectively re-deriving a version of LayerLens's own answer/actions/judge/state grader taxonomy from a different direction. Worth citing as external corroboration when explaining the "why four grading mechanisms, not one" design choice. Strengthens I-0003 and I-0004.
