# ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents

- authors_or_org: Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique, Lars Henning Klein, Akhil Arora, Ashvin Goel, et al.
- canonical_url: https://arxiv.org/abs/2610.28093v2
- discovered_url: inbox/arxiv/2026-W45.md (cs.OS harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.28093v2
- version: v2
- published_at: 2026-10-20 (v2: 2026-10-25)
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: agent memory, trust wall, provenance/authority, OS-style protection

## Claims from this source
- C-0124: ClawMMU is a protection layer that labels every piece of an agent's long-term memory (much of which comes from web pages and tool results) with its owner, scope, origin, and authority, then checks these labels whenever content enters the model's context, is written to storage, returns from storage, or drives a tool call. Its central rule: information may rise in authority, but authority never lifts itself. Because checks depend on *where content came from*, not *what it says*, memory attacks become classical protection faults the harness stops even when the model itself is fooled.
  - locator: abstract (verbatim)
  - evidence_label: proposal or interpretation (a protection-layer design proposal; the abstract does not report an evaluation against named attacks or a benchmark)
  - limitations: abstract only; no reported quantitative evaluation in what was read (unlike its companion Ring-0/AaOS paper, which does report experiments) — treat as a design proposal pending a fuller read of its evaluation section.
  - relationship to existing claims: the direct structural countermeasure to the Role Grounding Attack (C-0123, same inbox) — "authority never lifts itself" is precisely the invariant RGA's misattribution exploit violates. Also extends Ring-0/AaOS's (C-0113) broader OS-protections-missing-from-agents argument into a specific, implementable mechanism for the memory subsystem.

## LayerLens relevance
- open question(s) touched: #7 (human control), general scope area "context and memory" per PROTOCOL.md; relevant background for the trust-wall cluster (T-02) even though LayerLens's own system types are not today a long-horizon cross-session memory product
