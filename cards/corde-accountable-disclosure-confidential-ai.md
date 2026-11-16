# Enforcing Accountable Disclosure in Confidential AI

- authors_or_org: Shumpei Shiina, Haruka Takahashi, Kento Sasaki, Takuya Hayashi, Tsubasa Takahashi
- canonical_url: https://arxiv.org/abs/2611.05971
- discovered_url: inbox/arxiv/2026-W46.md (cs.OS)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.05971v1
- version: v1
- published_at: 2026-11-04
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: confidential computing, attestation, accountable disclosure, tamper-evident log

## Claims from this source
- C-0141: Confidential AI (via CPU/GPU confidential computing) lets LLMs process prompts without exposing them to providers/operators, but agents often need to send prompt-derived information to external services, and providers may need limited disclosure for safety monitoring/failure diagnosis. CORDE is a system for confidential VMs implementing "Confine or Declare": user-derived data is confined by default, but when it must leave the CVM it must first be "declared" — its exact contents, recipient, and stated reason recorded in a user-accessible, tamper-evident declaration log, via per-user information-flow control in Rust combined with a TEE-based ledger and remote attestation. On an NVIDIA H100, declaration-before-disclosure added about 0.5% to task latency on the AppWorld agent benchmark.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly; system evaluated on one named benchmark)
  - limitations: abstract only; overhead measured on AppWorld specifically; TEE/confidential-computing-dependent, a different hardware/trust model than LayerLens's own system types.
  - relationship to existing claims: strengthens T-02/T-09's attestation cluster with a low-overhead, concrete mechanism directly naming what I-0014 asks for ("a reviewer checks the evidence chain, not a badge") — here the declaration log *is* the evidence chain, tamper-evident and user-accessible by construction, distinct from PCM's (C-0117) proof-carrying-message approach and Magnetar's (C-0085) ZK-proof approach: a third, complementary mechanism (confine-or-declare logging) for the same reviewer-trust goal.

## LayerLens relevance
- open question(s) touched: #11 (the reviewer surface) — directly. Strengthens I-0014.
