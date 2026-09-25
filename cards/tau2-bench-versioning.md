# tau2-bench — release history and the v1.0.1 grading-fix / comparability notice

- authors_or_org: Sierra Research (sierra-research)
- canonical_url: https://github.com/sierra-research/tau2-bench
- discovered_url: WebSearch "tau-bench tau2-bench simulated user domain policy agent benchmark update"
- discovered_via: search (this is also a named reference benchmark in our own SOURCES.md, so this doubles as the periodic "verify each reference benchmark" check)
- doi_or_arxiv_id: origin paper arXiv:2506.07982 (τ2-Bench) and arXiv:2406.12045 (τ-bench); this card covers the maintained repo/releases, not the original papers
- version: v1.0.1 (latest patch at retrieval), τ³-bench 1.0.0 (latest minor), see below for full history read
- published_at: v1.0.1 dated 2026-07-22; τ³-bench 1.0.0 dated 2026-03-18 (per GitHub Releases page)
- retrieved_at: 2026-09-25
- source_type: docs (GitHub repo README + Releases page, primary/maintainer-authored)
- access_scope: full text — README.md (via raw.githubusercontent.com) and the Releases page, both read directly
- sections_read: README (What It Is, domains, evaluation modes, CLI), Releases (v1.0.1, τ³-bench 1.0.0, v0.2.0, v0.1.3)
- topics: run comparability, benchmark versioning, grading correctness, simulated users, domain policy

## Claims from this source

- C-0003: In release v1.0.1 (2026-07-22), sierra-research fixed grading bugs in the `banking_knowledge` domain that had been systematically zeroing rewards for cautious, policy-correct agent behavior (plus fixes to database-hash comparison, numeric argument normalization, unrealizable golden trajectories in tasks 077-086, transaction sort order, contradictory knowledge-base docs, and one task's expected refund amount). The release notes state explicitly: results generated with older versions are **not comparable** with >= 1.0.1, and that every score changed only upward (no simulation flipped pass-to-fail), moving by up to ~9 points depending on model.
  - locator: GitHub Releases page, "τ-Bench 1.0.1 — Banking Knowledge Grading Fixes"
  - evidence_label: documented capability (the maintainers' own release notes — a primary, first-party source)
  - limitations: single benchmark instance; does not establish how common this failure mode is across other benchmarks; we did not independently verify the underlying scoring code, only the maintainers' stated summary.
  - relationship to existing claims: new
- C-0003b: τ³-bench 1.0.0 (2026-03-18) added voice full-duplex evaluation (7 realtime providers), a new `banking_knowledge` domain (97 tasks, 698 policy documents, 12 configurable retrieval strategies from BM25 to agentic sandboxed-shell search), and 75+ task-quality fixes across airline/retail domains.
  - locator: GitHub Releases page, "τ³-Bench 1.0.0"
  - evidence_label: documented capability
  - limitations: n/a — direct release notes
  - relationship to existing claims: new

## LayerLens relevance

- Open question #1 (Comparability) and #4 (what "repeat a run" means): this is a concrete, dated, named-version existence proof of exactly the problem LayerLens's "immutable environment/task/prompt versions, grid refuses to average across mismatched versions" differentiator (#5, "On record") is designed to prevent — a widely-cited, actively maintained benchmark had to explicitly warn its own users not to compare scores across a patch version, because a grading bug had been silently changing what "correct" meant. Worth citing as the headline example when explaining to a non-technical stakeholder why version-pinning results matters.
- Also useful precedent for how to *communicate* a breaking grading change honestly: sierra-research reported the direction and magnitude of the score shift (upward only, up to ~9 points) rather than just declaring "don't compare" — a pattern LayerLens's own release/versioning communication could borrow from.
