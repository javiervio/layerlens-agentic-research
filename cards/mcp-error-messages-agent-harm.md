# MCP Error Messages Written for Developers Hurt the Most Capable Agents Most

- authors_or_org: Xiaonan Xu, Wenjing Wu
- canonical_url: https://arxiv.org/abs/2609.35381
- discovered_url: inbox/arxiv/LATEST.md (2026-W40 harvest)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2609.35381
- version: v1
- published_at: 2026-09-28
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: abstract only (verbatim, directly read via inbox harvester; arxiv.org itself blocked this run, no reachable GitHub mirror found)
- sections_read: abstract
- topics: tools and protocols (MCP), failure attribution, human/agent interaction

## Claims from this source
- C-0018: In 150 widely-used MCP servers, 949 of 3,001 error messages tell the calling agent what to do next, and half of those steps depend on something the server cannot see about the caller (e.g. "run a command," "edit a configuration," "open a web page"). Tested on five OpenAI models acting only through MCP tools: on expired credentials, a terminal-command-shaped step left 45% of tasks recovered, and the score lost by following it grew from 18 points (GPT-5.5) to 69 points (GPT-6 Astra) — i.e. more capable models followed the bad, human-oriented instruction *more* faithfully, not less. On rate limits, a bare "wait and retry" (no named call) left only 6% recovered. Two remedies tested: naming an actual server tool in the error step raised recovery to 84% (credentials) and 88% (rate limits); deleting the step via a one-sentence pre-read prompt raised credential recovery to 82%.
  - locator: abstract, full text
  - evidence_label: bounded empirical (abstract read directly; full paper not opened)
  - limitations: abstract only; five OpenAI models via Berkeley Function Calling Leaderboard tasks, not independently verified breadth; mechanism for "more capable = more harmed" not explained in what was read (plausibly: better instruction-following makes a model more likely to literally follow a human-oriented step it cannot actually execute).
  - relationship to existing claims: new — first claim in our scope-slice on MCP/tool error-message design specifically; connects to open question #2 (attribution) and #7 (recovery) at the tool-interface layer, and to the new counterintuitive pattern named in C-0021 below (capability amplifies rather than dampens interface/eval-surface harm).

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — a misleading error message is itself a distinct, nameable failure class, not "agent error"), #7 (human control and recovery — an agent given a bad recovery step needs the environment to help it, not mislead it).
- Direct product tie: LayerLens's own shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail) wrap real APIs with real, human-authored error messages — this paper's failure mode is not hypothetical for us, it is a concrete property of the exact system types we ship. See new idea I-0009.
