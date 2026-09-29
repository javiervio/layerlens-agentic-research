# jev-harness: a typed-decision, receipt-producing review pattern built on Jev

- authors_or_org: TypeSafeAI (GitHub org "TypeSafeAI"; repo self-describes as "a custom coding harness for TypeSafe AI's Jev" — read as a first-party or closely-affiliated reference implementation, not independently confirmed as TypeSafe AI's own official repo; treat authorship/affiliation as unconfirmed)
- canonical_url: https://github.com/TypeSafeAI/jev-harness
- discovered_url: WebSearch ("TypeSafe AI Jev github")
- discovered_via: search
- doi_or_arxiv_id: n/a
- version: pinned model `jev-1.13.0` per the README
- published_at: date unknown
- retrieved_at: 2026-09-29
- source_type: docs (GitHub README, read directly — github.com is reachable in this session)
- access_scope: full text (README)
- sections_read: all (pattern, four questions, receipt contents, decision primitives, performance-data caveats, limitations)
- topics: LLM-as-judge alternatives, typed decisions, audit trails, agent tool-call review, receipts/provenance

## Claims from this source
- C-0033: A "typed decision + receipt" pattern is emerging as a way to gate LLM-proposed actions: a generative LLM proposes an action, a narrow decision-only model (Jev) answers a small number of predefined yes/no questions with a probability and confidence, deterministic code applies a fixed decision table (not the model) to produce a verdict, and every step is recorded in a structured "receipt" (model version, latency, exact answers, validation/execution status) for offline audit.
  - locator: README sections "The Core Pattern," "The Four Questions," "Receipt Contents," "Decision Primitives."
  - evidence_label: proposal / interpretation for the pattern's general value (this is a reference implementation, not a controlled study); documented capability for what the harness concretely does and records.
  - limitations: the repo's own benchmark numbers (25-fixture and 20-fixture tests) are explicitly labeled "synthetic offline results, not calibration" and "a run is not a benchmark" — do not treat as evidence of real-world accuracy. The harness itself never applies patches, executes code, or grants permission; host software must still validate, execute, authorize, sandbox, and store durably. A "bound receipt"'s SHA-256 digest is explicitly "not a signature" (no cryptographic non-repudiation).
  - relationship to existing claims: new — complements C-0032 (the academic confidence-cascade paper) with a concrete product-pattern instance of the same "narrow, typed, confidence-bearing decision + human/code authorization + audit trail" idea, from the applied/engineering side rather than the benchmark side.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution), #7 (human control and recovery — "even a favorable Jev verdict requires explicit host approval before any action" is a directly comparable pattern to LayerLens's own confirmation/approval questions, open Q#6/#7); general (the "receipt" concept rhymes closely with LayerLens's own "on record"/verdict-with-evidence house vocabulary, worth noting as an independent external validation of that framing, not a novel idea to adopt wholesale).
- Feeds new idea I-0010 (see `ideas/backlog.md`) alongside C-0032.
