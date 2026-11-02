# Who Verifies the Tools? How Warped Formatters Mislead Agents and Their Verifiers

- authors_or_org: William Jeffries
- canonical_url: https://arxiv.org/abs/2610.32110
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.SE)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.32110v1
- version: v1
- published_at: 2026-10-23
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox)
- sections_read: abstract
- topics: tool output formatting, verifier gaming, production incident, attribution

## Claims from this source
- C-0097: A **real production RAG research system** (used by the Pilsudski Institute in New York) had tool output formatters that technically computed correct results but, in their printed text, omitted search limits, result caps, or identifier namespaces — "each tool did its job correctly, but its output omitted" key context. This misled both the agent (which gave wrong/incomplete answers) and verifiers checking the agent's work. Testing two formatter versions (one with the omissions, one with all details stated) on the same agent/verifier setup: **in one test, verifiers went from accepting incorrect answers 90/90 times to rejecting them 90/90 times**, solely from the formatter wording change. A control confirmed verifiers could catch the errors once given the missing facts. The author's audit prompt, run against two well-known open-source agentic systems (OpenClaw and Hermes), found warped formatters in both; a fix was opened as a PR for OpenClaw and already merged.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical — notably, a **real production incident with a named real-world system**, not a constructed benchmark; this is one of the higher-confidence sources this run given it documents an actual deployed failure plus an actual remediation.
  - limitations: abstract only; single author, single production system plus two open-source test subjects; the "90/90" figures are from one specific test condition, not necessarily representative of all failure types tested (the paper says "three of the four failure types" saw substantial drops, implying the fourth did not, or less so).
  - relationship to existing claims: **a real-world instance of exactly the pattern T-02/T-03 track (gaming/verification trust collapse)**, but from the opposite direction of most of this knowledge base's audit papers: here the gap isn't exploited adversarially, it's an unintentional, structural formatting defect that fools both agent and verifier simultaneously — closely parallel to C-0018 (MCP error messages misleading agents) but extended to verifiers, not just agents, and grounded in a real deployed system rather than a constructed study.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — a misleading tool-output *format*, distinct from a misleading tool-output *error message*, is its own nameable failure class), #11 (reviewer surface — a verifier accepting a wrong answer because of formatting, not logic, is exactly the kind of thing a reviewer needs to be protected from).
- Directly strengthens **I-0009** (a second real-world, non-benchmark instance of "the tool/interface surface itself, not the model's reasoning, is where the gap is," after C-0078's interface-drift finding) — and introduces a build caution specific to LayerLens's own graders: if a Judge grader reads tool-call *output text* rather than the underlying structured state, a formatting defect in a system type's own tool surface could fool the Judge the same way it fooled this paper's verifiers. Worth a design-review note alongside the trust-wall checklist.
