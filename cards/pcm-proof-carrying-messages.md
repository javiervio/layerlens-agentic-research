# PCM: A Proof-Carrying Message Protocol for Verifiable Multi-Agent Communication

- authors_or_org: Bravish Ghosh
- canonical_url: https://arxiv.org/abs/2610.39109v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.MA harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.39109v1
- version: v1
- published_at: 2026-10-29
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: attestation, reviewer surface, cryptographic verification, multi-agent trust

## Claims from this source
- C-0117: Proof-Carrying Messages (PCM) is a protocol in which each inter-agent claim ("the tests passed," "a person approved this refund") carries evidence: records from an append-only Merkle log the agent cannot write, with inclusion proofs signed by an attesting signer the agent cannot control. Receivers verify offline and give each claim a three-valued result (proven/unproven/failed); a claim resting only on the agent's own report is never proven; authority travels as grant chains rooted in a recorded human approval that can only narrow. On a pre-specified benchmark of 926 messages (712 containing lies across 16 classes), PCM accepted only 10 lies (1.4%, 95% CI 0.8-2.6%, all stale-evidence cases), versus plain A2A accepting all 712 and models of six deployed protocols (A2A with signed Agent Cards, uAgents, RFC 9421, SCITT, AP2, Verifiable Intent) accepting 504-712; two independent verifiers agreed on all 926 verdicts at about 1ms verification time.
  - locator: abstract (verbatim)
  - evidence_label: bounded empirical (a concrete protocol with a formal security property proof plus a quantified benchmark against six named deployed protocols)
  - limitations: abstract only (the security proofs, benchmark construction, and the 16 lie classes themselves not read in detail); single-author paper; benchmark is "pre-specified" by the authors, not independently adversarially red-teamed by a third party.
  - relationship to existing claims: **second independent evidence family for nursery thesis N-05** (cryptographic/proof-based verification as an alternative to re-execution/trust-based verification) alongside Microsoft Research's Magnetar (C-0085, ZK proofs for general computation) — PCM applies the same structurally-different-from-re-execution idea specifically to *inter-agent claims*, not general computation, making it a closer match to open question #11 (the reviewer surface) than Magnetar was. Promotes N-05 to a full thesis per theses.md's own two-independent-evidence-family rule.

## LayerLens relevance
- open question(s) touched: #11 (reviewer surface — "accept a claim without trusting the claimant" is PCM's exact framing), #3 (deterministic replayability — offline-verifiable proofs, ~1ms verification)
