# Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs

- authors_or_org: Xiaobo Chen, Genliang Zhu, Ziyuan Wang, Chu Wang
- canonical_url: https://arxiv.org/abs/2611.07483
- discovered_url: inbox/arxiv/2026-W46.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.07483v1
- version: v1
- published_at: 2026-11-05
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: multi-agent handoffs, signed manifests, provenance, trust boundary

## Claims from this source
- C-0135: When enterprise agents split a request across subagents and merge results, each handoff can summarize away, alter, or ignore a requirement. A preregistered study on synthetic, exactly-scorable tasks compared free-text, structured-JSON, and signed requirement-manifest handoffs (orchestrator extracts each requirement as a verbatim quote plus a checkable predicate, HMAC-SHA256-signs the manifest, deterministic code verifies the merger's decision). With Qwen3-8B (1,440 trajectories, five threats), signed manifests cut unsafe commits under attack from 69.4% to 9.0% (60.4pp) with no loss of conformant commits vs. structured handoffs; an unsigned manifest committed violations in 79% of mutated runs vs. none for the signed one. A deterministic verifier caught 78.7% of violating decisions vs. 59.0% for an LLM checker, with 7% vs. 50% false alarms. An oracle manifest removed all remaining unsafe commits, meaning the residual risk comes from extraction errors made *before* signing — confirmed by a preregistered pre-signing injection attack, where one adversarial line raised signed-manifest violations from 14.6% to 37.5% (Qwen3-8B), 11.1% to 63.9% (gpt-oss-20b), and 8.3% to 75.0% (GPT-5.6-luna): the signature then authenticated the corrupted manifest. "Signing protects requirements in transit, not at extraction; the extraction step is the trust boundary."
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly; preregistered design stated)
  - limitations: abstract only; synthetic, exactly-scorable tasks; one open-weight model as the main subject plus two others in the injection test.
  - relationship to existing claims: directly extends I-0013 (memory/retrieved-content provenance and authority) with a second, distinct mechanism (signed requirement manifests for inter-agent handoffs, vs. C-0123/C-0124's memory-authorship attack/defense pair) and names the same lesson as C-0131 (Signed, Sealed, Leaked) from the opposite direction: here signing defeats in-transit tampering well, but the pre-signing extraction step remains the real trust boundary — "signed but not safe" is a recurring pattern this week.

## LayerLens relevance
- open question(s) touched: #7 (human control), #2 (attribution — extraction-time corruption vs. transit-time tampering is a useful attribution split for any future multi-agent or multi-step handoff LayerLens ever grades); general (memory/provenance). Strengthens I-0013.
