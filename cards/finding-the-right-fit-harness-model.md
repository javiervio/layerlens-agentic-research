# Finding the Right Fit: Model-Harness Interactions across Agent Tasks

- authors_or_org: Yixuan Li, Yiyun Zhou, Yao Long Teng, Fuchao Yang, Yanchen Deng, Zhiyi Lyu et al.
- canonical_url: https://arxiv.org/abs/2610.00917v1
- discovered_url: inbox/arxiv/LATEST.md (2026-W41 harvest, cs.SE), companion repo via search
- discovered_via: feed (arXiv inbox harvester), then citation (companion GitHub repo)
- doi_or_arxiv_id: arXiv:2610.00917v1
- version: v1
- published_at: 2026-10-01
- retrieved_at: 2026-10-12
- source_type: paper
- access_scope: abstract read directly via inbox, plus companion GitHub repo README (github.com/liyix/finding-the-right-fit) read directly and in full
- sections_read: abstract; repo README (harnesses, models, benchmarks, headline numbers)
- topics: comparability, model-harness interaction, agent evaluation methodology

## Claims from this source
- C-0044: Evaluating 66 configurations (5 models x harnesses incl. native pairings) across TUA-Bench, ALE-CLI, and Terminal-Bench 4 (6,204 scored trajectories total), model rankings reverse depending on harness. On Terminal-Bench 4, Claude Opus 5 beats GPT-6 Astra by 7.9 points under OpenHands (57.1 vs 49.2) but trails it by 30.1 points under the "PI" harness (30.2 vs 60.3). For 4 of 5 models the best harness changes across benchmarks; a model's own vendor harness is not reliably its best (Claude's native harness wins on TUA-Bench/ALE-CLI but OpenHands wins on Terminal-Bench 4 for Claude). Higher cost does not reliably buy a higher score: GPT-6 Astra scores higher under PI ($4.66/task) than under openJiuwen ($11.07/task) on Terminal-Bench 4. Kimi K3 is the one model whose best harness (openJiuwen) holds across all three benchmarks.
  - locator: repo README, directly read; headline numbers cross-checked against the abstract
  - evidence_label: bounded empirical (companion repo directly read; full result tables in the paper itself not opened, arxiv.org blocked)
  - limitations: three benchmarks, five models, six harnesses — not a census; "PI" harness's exact mechanics not detailed in what was read.
  - relationship to existing claims: a strong, directly-read new family for open question #1 (comparability) and T-01 — the single most concrete demonstration yet in this knowledge base that a model ranking is not a property of the model alone; harness is a comparably large confound, which PROTOCOL.md's own evidence-discipline rule 7 already names in principle ("check model, tools, scaffold are comparable before ranking") but this gives it hard numbers.

## LayerLens relevance
- open question(s) touched: #1 (comparability), #9 (comparison as signature surface). Directly strengthens I-0004/F-0003 (always show a tradeoff axis / comparability guardrails): a model-only leaderboard is actively misleading when harness varies, which argues LayerLens's own model-comparison views should surface (or pin) the harness/scaffold as a first-class, not incidental, dimension of any comparison.
