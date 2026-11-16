# The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record

- authors_or_org: Vivek Acharya
- canonical_url: https://arxiv.org/abs/2611.06989
- discovered_url: inbox/arxiv/2026-W46.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.06989v1
- version: v1
- published_at: 2026-11-04
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: cost accounting, comparability, attribution, FinOps

## Claims from this source
- C-0145: Enterprises running business transactions through multi-agent AI systems cannot answer "what did this order/claim/case cost in AI?" from billing data alone, because providers never see enterprise transaction boundaries and billing is settlement-grain (aggregated by SKU/period) even under FOCUS (the FinOps Open Cost and Usage Specification). The authors propose the Two-Ledger Model: a settlement ledger (FOCUS-conformant billing) joined to an attribution ledger (invocation-grain usage on OpenTelemetry GenAI telemetry) via a layered correlation spine (trace context, A2A/MCP metadata, business-key correlation, probabilistic matching), each record carrying a recorded method and confidence; a versioned rate card prices usage near-real-time, and period reconciliation flags the unexplained residual as "shadow AI." In a simulation with known ground truth, the spine sustained cost coverage above 99% as trace propagation fell to zero, the reconciliation residual recovered planted unmetered spend within 0.24 percentage points while flagging provider billing errors, and mid-flight gating cut p99 transaction cost by up to 61% at a 2-4% false-pause rate.
  - locator: abstract, verbatim
  - evidence_label: proposal / interpretation (a cost-accounting architecture, validated on a simulation with known ground truth, not production data)
  - limitations: abstract only; simulation-based validation, not a real multi-tenant deployment; single-author paper.
  - relationship to existing claims: new evidence for I-0004 (comparability guardrails / always show a tradeoff axis): a concrete, standardization-oriented mechanism for the cost side specifically, complementary to C-0106's (HarnessMM) finding that harness-internal engineering makes cost a moving target even holding model/harness name fixed — this paper proposes a traceability and confidence-scoring mechanism for exactly that problem, one layer up (business-transaction, not just harness-run).

## LayerLens relevance
- open question(s) touched: #1 (comparability) — a cost ledger with per-record confidence and a flagged "residual" is a candidate reference design if LayerLens's own cost/credits reporting (billing/ledger, already shipped per LAYERLENS_CONTEXT) is ever extended to per-task or per-environment cost attribution.
