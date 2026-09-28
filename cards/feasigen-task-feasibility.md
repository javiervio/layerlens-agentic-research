# Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents (FeasiGen)

- authors_or_org: Liang Cheng, Mingsheng Cai, Jiuming Jiang, Luo Mai (University of Edinburgh)
- canonical_url: https://arxiv.org/abs/2605.28532
- discovered_url: WebSearch (2026-09-25 and 2026-09-28 scheduled runs)
- discovered_via: search
- doi_or_arxiv_id: arXiv:2605.28532
- version: v1
- published_at: 2026-05-27
- retrieved_at: 2026-09-29 (manual deep-read, local session with full web access)
- source_type: paper
- access_scope: abstract read directly + HTML body (results range, multi-agent numbers, metrics, limitations)
- sections_read: abstract, method (FeasiGen pipeline), metrics, results, limitations
- topics: task feasibility, tool-use agents, early stopping, multi-agent, synthetic task construction

## Claims from this source
- C-0007: Models are weak at recognizing infeasible tasks; multi-agent planner-executor setups help substantially.
  - locator: abstract + results
  - Method: FeasiGen extracts tool-calling traces from successful runs across multiple agent systems, finds the critical tools consistently shared across strategies, and masks them to turn solvable tasks infeasible. Human verification confirms infeasibility annotations at over 94% accuracy.
  - Metrics defined: False Continue Rate (FCR, how often the agent proceeds on an infeasible task), Success Rate on feasible tasks, token cost to early stop, token cost to task failure.
  - Results (directly read): FCR across nine single-agent models ranged **23.5% (GPT-5.5, best) to 73.9% (Qwen3.5-9B, worst)**; single-agent average FCR **54.6%**. Best multi-agent pair (Qwen-122B planner, GPT-OSS executor) reached **2.6% FCR, nearly a 10x reduction** versus the best single agent.
  - **Correction to earlier record**: the 2026-09-25/09-28 search-summary figure of "multi-agent cut average from 54.6% to 17.5%" was NOT confirmed by direct read. The paper's headline multi-agent result is the best pair at 2.6%; a "17.5%" multi-agent average was not found in the sections read. Treat 2.6% (best pair) and 54.6% (single-agent avg) as the confirmed anchors.
  - evidence_label: bounded empirical (directly read)
  - limitations (stated): FeasiGen operates on benchmarks with fixed, fully predefined candidate tool pools; in open-ended settings where agents dynamically retrieve or invoke arbitrary tools, agents may bypass the masked dependencies, so the infeasibility construction may not transfer.
  - relationship to existing claims: first and only claim on task feasibility.

## LayerLens relevance
- Open question #4 (task feasibility). Note the mirror-image framing: this paper is about agents detecting infeasibility at run time; LayerLens's question is about an author constructing a solvable scenario and seeing why one is not solvable at design time. The FeasiGen pipeline (mask a critical tool, task becomes infeasible) is itself a candidate mechanism for a "why is this not solvable" explanation surface.
