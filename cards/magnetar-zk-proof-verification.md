# Proof-based general-purpose computing with Magnetar

- authors_or_org: Microsoft Research
- canonical_url: https://www.microsoft.com/en-us/research/blog/proof-based-general-purpose-computing-with-magnetar/ (companion paper: https://eprint.iacr.org/2026/2423)
- discovered_url: inbox/reference/2026-W43.md (Microsoft Research section, via microsoft.com/en-us/research/feed)
- discovered_via: feed
- doi_or_arxiv_id: IACR ePrint 2026/2423
- version: n/a
- published_at: 2026-10-15
- retrieved_at: 2026-10-26
- source_type: post (first-party Microsoft Research blog; microsoft.com has historically been reliably reachable in this sandbox, but this run used WebSearch rather than a direct WebFetch — not independently re-confirmed reachable this run)
- access_scope: incomplete access (WebSearch summary of the Microsoft Research post and third-party summaries of the IACR paper; neither opened directly this run)
- sections_read: WebSearch summary only
- topics: zero-knowledge proofs, verification without re-execution, attestation

## Claims from this source
- C-0085: Magnetar is a zero-knowledge proof system for general-purpose programs (written in Rust, Go, or C) that lets a verifier check a program's output correctness "without rerunning the program, without trusting whoever ran it, and without needing data on which the program was run," per Microsoft's own blog framing. Per the IACR paper, Magnetar runs 10-39x faster on average than prior comparable proof systems, avoids circuit-friendly algebraic hashes (e.g. Poseidon) and elliptic-curve/lattice assumptions, and reports, at 120 bits of provable security on a consumer laptop (M4 Max), proofs of about 600 KiB that verify in 10-12ms. With zero-knowledge enabled, proofs can keep private inputs hidden from the verifier.
  - locator: WebSearch summary of the Microsoft Research blog post and the IACR ePrint paper abstract
  - evidence_label: incomplete access (neither the blog post nor the paper independently opened this run; the 10-39x and benchmark figures are the authors' own reported numbers, not independently reproduced)
  - limitations: a general-purpose cryptographic verification system, not built for or evaluated on agentic environments/evaluation specifically; the link to agent evaluation here is this run's own inference, not a claim the source itself makes.
  - relationship to existing claims: new — first claim in this knowledge base on cryptographic/ZK-proof-based verification as a category. Distinct in kind from every mechanism T-02/T-06 has tracked so far (deterministic re-grading, trace-level attribution, checkpoint/rollback, audit scanners): those all either re-execute, re-derive, or compare against a stored answer key; a ZK proof instead lets a verifier trust a *computation's own proof of correctness* without needing to see the private inputs or re-run anything. Seeded as nursery thesis N-05 (single source) rather than folded into an existing thesis, since the mechanism family is genuinely new to this knowledge base.

## LayerLens relevance
- open question(s) touched: #3 (deterministic replayability as a surface — ZK proofs are a different answer to a similar need: both let someone else trust a result without re-deriving it themselves, but LayerLens's approach is "replay and compare," while this is "verify a cryptographic proof of correct execution"), #11 (the reviewer surface — Riley needs to accept a claim without trusting the claimant; a ZK-proof-style guarantee is a structurally stronger version of that same need, though far more expensive/specialized to build than LayerLens's current replay-based approach). Good "one concept to understand better" candidate: worth a plain-language explanation of how this differs from LayerLens's own verification model.
