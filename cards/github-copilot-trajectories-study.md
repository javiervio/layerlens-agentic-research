# Large-Scale Study of GitHub Copilot Trajectories

- authors_or_org: Izah Sohail, Yerdanat Kurmantayev, May Mahmoud, Sarah Nadi
- canonical_url: https://arxiv.org/abs/2610.32313
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.SE)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.32313v1
- version: v1
- published_at: 2026-10-23
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox)
- sections_read: abstract
- topics: real-world human-agent collaboration, production trajectory data, benchmark-vs-reality gap

## Claims from this source
- C-0096: Studying **7,581 Copilot-authored PRs with publicly accessible session data** (real-world, not benchmark-constructed), the authors find most coding-agent benchmarks (SWE-bench-style) wrongly assume autonomous, single-trajectory operation: **58% of Copilot PRs have no human intervention at all**, and when developers do intervene, collaboration is brief (median 2 human-AI loops). Merged PRs tend to have fewer initial trajectory iterations than unmerged ones. The trajectory immediately following the *first* human intervention shows a significant drop (20.8 fewer iterations, 8.4 fewer minutes) versus the initial trajectory, but *later* interventions show minimal iteration/duration change — most of the work happens in the initial trajectory, and later interventions tend to be small, focused requests.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only, but a large real-production dataset, not a constructed benchmark)
  - limitations: abstract only; Copilot-specific (one vendor's agent and interaction model), may not generalize to other harnesses; "publicly accessible session data" implies a selection bias toward open-source/public PRs.
  - relationship to existing claims: new, real-production family alongside C-0042/C-0043 (production incident taxonomy, enterprise trajectory deviation) — this one is specifically about the *shape* of human-agent collaboration in the wild (how often, how much, when), a gap the paper explicitly states most benchmarks assume away.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — concrete, real numbers on how often and how much humans actually intervene), #12 (are Devon and Evan one person — adjacent: this shows a single human role toggling between hands-off oversight and brief, targeted correction, relevant to who actually drives intervention in practice).
- A useful real-world calibration point for designing LayerLens's own confirmation/intervention UI (I-0006): if most real human-agent collaboration is "mostly autonomous, occasionally a brief focused correction" rather than constant oversight, a consequence-naming confirmation needs to work well for an infrequent, high-leverage interrupt, not assume continuous supervision.
