# Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents

- authors_or_org: Liang Cheng, Mingsheng Cai, Jiuming Jiang, Luo Mai — University of Edinburgh (Large-Scale Machine Learning Systems Group)
- canonical_url: https://arxiv.org/abs/2605.28532
- discovered_url: WebSearch "task feasibility awareness agent benchmark arxiv 2026"
- discovered_via: search (this exact paper was flagged as high-priority pending from the 2026-09-25 run log, which found it inaccessible last week too)
- doi_or_arxiv_id: arXiv:2605.28532
- version: not confirmed
- published_at: 2026-05-27 (per aggregated search text)
- retrieved_at: 2026-09-28
- source_type: paper
- access_scope: abstract only, and second-hand — arxiv.org (abs/html/pdf) was EGRESS_BLOCKED again this run, as was pith.science's mirror page. No GitHub repo for the FeasiGen pipeline was found via search. Everything below is WebSearch's generated summary across several listing pages, not text opened directly.
- sections_read: none directly. Flagged **incomplete access (search summary only)**.
- topics: task feasibility, infeasible-task detection, tool-using agents, multi-agent architectures

## Claims from this source

- C-0007: The paper proposes FeasiGen, a pipeline that builds infeasible tool-use tasks by identifying tools that successful runs consistently require and then masking them out, with reported human verification of >94% infeasibility-annotation accuracy. Across nine evaluated models (spanning GPT, DeepSeek, Qwen, and LLaMA families), false continue rate (proceeding on a task that is actually infeasible, instead of recognizing and stopping) reportedly ranged 23.5%-73.9% for single-agent setups, and multi-agent architectures reportedly cut the average false continue rate from 54.6% to 17.5%.
  - locator: none — search-summary only.
  - evidence_label: incomplete access
  - limitations: no primary text opened; specific model list, task domains, and exact experimental conditions (how "multi-agent" was configured) are unverified. The >94% infeasibility-annotation figure is itself a claim about the benchmark's own construction quality, not about agent behavior, and is also unverified beyond the search summary.
  - relationship to existing claims: new — this is the first claim in our knowledge base that speaks directly to LayerLens open question #4 (task feasibility). No prior claim to compare against.

## LayerLens relevance

- **Open question #4 (Task feasibility)** — directly on point. If the reported numbers hold up, they would suggest: (a) most current models are bad at recognizing an infeasible task rather than confabulating a wrong answer or endless retry loop, and (b) an orchestrator/verifier layer (multiple agents, or an explicit feasibility check) measurably helps. For LayerLens's own question — "how does a person author a solvable scenario and see why one is not solvable" — this paper is really about the mirror-image problem (agents recognizing infeasibility at run time, not authors avoiding it at design time), so even a full read would only partially answer our open question; still the closest match found so far.
- Action for next run: this is now the second run in a row this exact paper was flagged high-priority and could not be opened. If arxiv.org remains blocked a third week running, consider asking Javier directly whether he can share a saved PDF or alternate link per PROTOCOL.md's "links Javier saved" allowance, since search-summary-only is reaching its limit of usefulness here.
