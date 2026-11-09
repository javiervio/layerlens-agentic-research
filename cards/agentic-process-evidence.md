# Agentic process evidence

- authors_or_org: Yuval Kainan, Carmit Hershman
- canonical_url: https://arxiv.org/abs/2610.40071v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.SE harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.40071v1
- version: v1
- published_at: 2026-10-29
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: attestation, provenance, reviewer surface, supply-chain/governance

## Claims from this source
- C-0118: The authors argue every governance framework, audit trail, and compliance control in the software development life cycle (SDLC) assumes a human made the decision, an assumption that no longer holds once AI agents autonomously create PRs, select dependencies, refactor code, interpret test failures, and execute infrastructure changes — and that git's own log shows what changed, never what model/tools/accountability chain produced it. They introduce Agentic Process Evidence (APE): a signed, tamper-evident, machine-readable attestation of agentic processes linking sessions to outcomes, built on the in-toto attestation framework, enabling policy-as-code control with human-in-the-loop only where needed.
  - locator: abstract (verbatim)
  - evidence_label: proposal or interpretation (a position/design paper proposing a governance framework, not a validated system with reported results)
  - limitations: abstract only; no reported deployment, benchmark, or adoption numbers in what was read — this is an argued design proposal, not yet demonstrated at scale.
  - relationship to existing claims: a position-level articulation of the same gap PCM (C-0117) and Soei (C-0116) both address with working systems — "you can't hold an ephemeral process accountable" and "the git log was designed for human commits" name exactly why attestation/provenance is becoming a named category rather than a niche concern, adding a third, independent voice to the same cluster (a design-proposal perspective, distinct from PCM's cryptographic-protocol and Soei's production-observability approaches).

## LayerLens relevance
- open question(s) touched: #11 (reviewer surface — attestation is API-only today per LAYERLENS_CONTEXT; this is a third source naming the same gap from a governance/compliance angle rather than a technical-mechanism angle)
