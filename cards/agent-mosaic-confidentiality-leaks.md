# Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems

- authors_or_org: Daniel Ruiz, Luca Luceri, Emilio Ferrara
- canonical_url: https://arxiv.org/abs/2610.30418
- discovered_url: inbox/discovery/LATEST.md (hf-daily, 23 upvotes, 2026-W44) then inbox/fulltext/
- discovered_via: feed (discovery harvester)
- doi_or_arxiv_id: arXiv:2610.30418
- version: v1
- published_at: 2026-10-21
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (see the fulltext-harvester note in cards/are-gaia2-meta-environments.md)
- sections_read: abstract (verbatim)
- topics: confidentiality, information aggregation risk, agentic environment design, mixed-clearance data

## Claims from this source
- C-0092: Agents that retrieve from multiple individually-permitted documents can "disclose a sensitive conclusion assembled from them" even though no single document was sensitive — a "mosaic effect." Across 30 synthetic cybersecurity/medical/military scenarios (10,800 answers from 3 LLM agents in simulation, 1,440 answers from live agents in two open-source harnesses), the best model (GPT-5.6-Sol) disclosed forbidden composites in **7.08% of answers in simulation (worse in live harnesses)**, even under benign, single-document-answerable queries. Adding visible classification headers and explicit aggregation rules reduced but did not eliminate disclosure: **32.37% of simulated answers still leaked the composite despite these safeguards**. Refusals did not reliably protect confidentiality either — "significant refusals reveal the prohibited conclusion regardless."
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; synthetic scenarios (30 examples), not real enterprise data; two open-source harnesses tested live, not a broad census; the exact classification-header/aggregation-rule mitigation design not described.
  - relationship to existing claims: new — first claim in this knowledge base specifically on cross-document information-aggregation leakage within one agent session, distinct from TUPLE-Bench's (C-0069) confidence-field leakage (a different leak channel: aggregated inference vs. a judge's own output fields) and from the credential-isolation cluster (T-02, Braintrust/Modal/E2B/LayerLens trust wall, which protects secrets/credentials, not inferable conclusions from permitted documents).

## LayerLens relevance
- open question(s) touched: none existing maps cleanly; this is a genuinely new pain point.
- **New idea candidate**: LayerLens mints environments populated with real or synthetic records (Salesforce, Gmail, SEC EDGAR, Stripe) that plausibly carry mixed sensitivity even within one tenant (e.g., an email thread mentioning a deal plus a separate record naming a customer's medical or financial detail). An agent operating across several of an environment's own system types could, in principle, assemble a disclosure neither document alone would authorize — the same mosaic mechanism, inside a LayerLens environment rather than a document-retrieval RAG system. Dedup: checked against I-0009 (tool/error-surface guidance — distinct, this is about information aggregation, not tool-call recovery), I-0006 (consequence-naming confirmations — distinct, this is about what an agent is allowed to *conclude and say*, not a pending write action), and the general trust-wall/credential-isolation cluster (T-02 — distinct, that protects secrets/seeds from the agent; this is about the agent's own legitimate access to multiple records combining into something none of them individually discloses). Distinct enough from all existing ideas to merit a new L0 entry (see ideas/backlog.md I-0012).
