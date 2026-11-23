# Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation

- authors_or_org: Disha Sheshanarayana, Sai Linisha Reddy Goli
- canonical_url: https://arxiv.org/abs/2611.18471v1
- discovered_url: inbox/arxiv/LATEST.md (cs.AI, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.18471v1
- version: v1
- published_at: 2026-11-13
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: verification, attribution, agent evaluation, harness

## Claims from this source
- C-0155: LLM-based verifiers judging agent executions are typically evaluated under one representation of the trajectory, but deployed systems expose the same execution through composed tools, delegation boundaries, or compacted histories. A new test, "Verification Transport," measures whether a verifier's judgment stays correct across native, abstracted, and restored views of the same frozen execution (task, trajectory, outcome, ground truth, criterion, and verifier held fixed). Across four agent-evaluation benchmarks, seven verifier backbones, four verification protocols, and three abstraction boundaries, transport failure reaches about 31% under macro abstraction and delegation. Verification protocols fail differently: direct verification more often produces an outright incorrect verdict, while evidence-grounded and deliberative protocols tend to abstain under limited observability.
  - locator: abstract
  - evidence_label: bounded empirical
  - limitations: abstract only; exact benchmark/backbone names, what "macro abstraction" concretely changes, and whether abstention is scored as a distinct outcome from "wrong" are not visible from the abstract alone.
  - relationship to existing claims: extends T-03 (attribution) and T-05 (judge reliability) with a new, more specific failure mode — a verifier's correctness is not stable under exactly the kind of representation changes (delegation, compaction) that real agent harnesses already use.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — a verdict computed over a compacted/delegated trace view may not be the same verdict a full trace would earn), #9 (comparison — two "passing" verdicts may rest on different observability of the same execution)
- general: directly relevant to LayerLens's own Judges/Scorers, which read traces that may themselves be compacted or delegated (sub-agent calls) before a verdict is reached — this paper's abstain-vs-err distinction between verification protocols is a concrete design choice LayerLens's own Judge architecture should be checked against.
