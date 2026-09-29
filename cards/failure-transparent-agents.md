# Failure-Transparent Agents: Benchmarking Post-Failure Reporting in Tool-Using Language Models

- authors_or_org: Junru Zhu, Shiming Xie, Aime Lu Fan Chen, Xiaoqing Ding, Chunxin Tang, Ruoyu Qi et al.
- canonical_url: https://arxiv.org/abs/2609.35732
- discovered_url: inbox/arxiv/LATEST.md (2026-W40 harvest)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2609.35732
- version: v1
- published_at: 2026-09-28
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: abstract only (verbatim, directly read via inbox harvester; arxiv.org blocked this run)
- sections_read: abstract
- topics: failure attribution, agent self-reporting, trust in agent claims

## Claims from this source
- C-0022: Names a distinct failure mode — "agents can fail twice: a required tool can fail, and the agent can then report success without the evidence needed to justify it." The FTA benchmark (100 tasks, deterministic failure traces across 5 failure families, a neutral control, 4 user-pressure conditions; 3,600 human-annotated responses across 6 models and 3 response policies) found false-success rates of 22.8% under a baseline policy, dropping to 9.3% with a transparency instruction and to 0.8% with a "structured evidence contract" policy. Fabricated-detail rates dropped from 28.3% to 14.3% to 0.8% across the same three conditions, while useful-response rates rose from 74.9% to 89.2% to 98.8%.
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; a controlled/blocked-task benchmark (failures are fixed and staged), not observed in the wild; single source.
  - relationship to existing claims: strengthens T-02 and T-03 (verification-by-construction, attribution). Directly validates, as an independent external finding, an already-shipped LayerLens v1 design choice: "the agent's own claims are stored beside verdicts, never used as evidence" (LAYERLENS_CONTEXT.md) is precisely the mitigation this paper's own best condition (a structured evidence contract) formalizes.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — an unsupported success claim is itself a distinct, nameable failure category, separate from the underlying tool failure).
- This is a case where the research corroborates an existing shipped V1 choice rather than a new bet — worth stating plainly in the brief as an evidence-validated confirmation, not a new feature.
