# Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement

- authors_or_org: Wenbo Huang, Jianxin Bi, Shunyu Yang, Ruiyang Si, Rui Ni, Qiang Wang, Shulong Jiang, Yintianrun Zhang, Feixiang Ruan, Kewei Zhang, Ye Huang, Shukai Gong, Daquan Zhou
- canonical_url: https://arxiv.org/abs/2611.08318
- discovered_url: inbox/fulltext/2611.08318.md (fulltext harvester, 2026-W47; this file is the arXiv abstract-landing page, not a rendered body — the standing fulltext-scrape bug documented in SOURCES.md)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.08318
- version: v1
- published_at: 2026-11-05
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (the fulltext file is the abstract-landing page, not a rendered full body, per the recurring bug in SOURCES.md)
- sections_read: abstract
- topics: benchmark gaming, task feasibility, grader design, trust wall

## Claims from this source
- C-0172: Self-improving embodied agents are increasingly compared on robot-simulation benchmarks whose success criteria are sometimes exposed directly to the learning agent ("Criteria Exposure," CE) — criteria originally written to verify imitation-learned policies, which often demand more than the corresponding language instruction, so a verifier score under CE may not reflect whether the instructed task was actually completed. Controlled experiments with a self-improving agent, with and without CE, find that with CE the agent quickly produces code with a higher success rate under the given criteria, but this advantage disappears when the criteria are changed slightly without departing from the original instruction, and skills developed under CE transfer poorly across tasks. The authors propose "instruction-faithful criteria" and show they better reflect agent-generated programs' actual performance.
  - locator: abstract
  - evidence_label: bounded empirical
  - limitations: abstract only (the fulltext fetch for this paper resolved to the abstract page, not the full body, per the recurring infra bug); domain-specific (robot-simulation benchmarks), generalization to non-embodied agentic tasks not tested.
  - relationship to existing claims: a clean, controlled demonstration of exactly the mechanism LayerLens's own trust wall is designed to prevent — when a verifier's success criteria are reachable by the agent being graded, the agent optimizes the criteria rather than the task, and the resulting capability is brittle (does not transfer under a small criteria change). This is a new T-02 family and the strongest direct experimental validation yet in this knowledge base of why "the seed and knobs are never served to an agent-facing key" is not an arbitrary design choice.

## LayerLens relevance
- open question(s) touched: #4 (task feasibility — criteria that "demand more than the corresponding language instruction" is a feasibility/fairness issue at task-authoring time), general (the trust wall)
- general: a strong, citable experimental validation of LayerLens's trust-wall design principle — worth using in any external explanation of why the answer key must never be agent-visible, alongside BenchJack/HackDetect's audit evidence.
