# Progress on provable inference for large language models

- authors_or_org: Anthropic
- canonical_url: https://www.anthropic.com/research/provable-inference
- discovered_url: inbox/reference/2026-W46.md (Anthropic sitemap)
- discovered_via: feed
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-11-09
- retrieved_at: 2026-11-16
- source_type: post
- access_scope: full text (WebFetch; anthropic.com reliably reachable per SOURCES.md)
- sections_read: full post
- topics: cryptographic verification, zkSNARK, attestation, reviewer trust

## Claims from this source
- C-0148: Anthropic's "provable inference" (PI) lets a user with limited compute and no information about a model's weights verify that a response came from a specific, committed set of weights, via a zkSNARK (not re-execution). Offline, the prover publishes a short commitment ("fingerprint") pinning one exact weight set while keeping it hidden; online, for each request the prover produces a proof asserting the committed model produced the given output tokens; anyone holding the commitment, prompt, and reply can check the proof without the weights, with limited compute. The protocol is proven complete, sound, and zero-knowledge (revealing nothing about weights/intermediate values, including which experts ran in a MoE model), succinct, and software-only (no trusted hardware), with stated post-quantum security; completeness/soundness/zero-knowledge are formally proven in Lean. On FlashProve/Llama 4 Maverick (400B MoE, 4-bit weights, one H100 + 24 CPU cores): offline commitment ~39 minutes covering ~16M requests; online proving ~223s for a batch of 24 requests (~110 tokens/sec); each proof ~18.78MB for 1,024-token windows; verification ~17s on 24 threads; overhead vs. vLLM is ~72-94x (roughly two orders of magnitude), versus a cited prior system (VerInf) at ~0.02 tokens/sec. Stated limitations: the fast C++ verifier carries no formal guarantee (though it agreed with the Lean verifier on tests run); the proof covers an exact integer model and greedy decoding only (floating-point/sampled outputs may diverge, and the method does not cover adversarially designed prompts); architecture is not hidden; timing side-channels during proof generation are out of scope; context is capped at 1,024 tokens, far below real chat/frontier windows; proving is post-hoc/batched, adding delay; explicitly "a research prototype." Code, protocol spec, Lean proofs, and a technical report released under Apache 2.0.
  - locator: full post (WebFetch summary, key figures and quotes preserved)
  - evidence_label: documented capability (first-party, directly read) for the design and benchmark figures; the formal-verification claims are stated as proven in Lean but the fast implementation's correspondence to the proof is explicitly not guaranteed.
  - limitations: a frontier lab's own research prototype, not a shipped product; ~80x inference overhead and a 1,024-token cap make it far from production-ready for typical agent contexts; greedy-decoding-only restricts applicability to real-world sampled generation.
  - relationship to existing claims: a major new, third independent family for T-09 (cryptographic/proof-carrying verification as a structurally different alternative to re-execution-based trust), alongside Microsoft Research's Magnetar (C-0085, general computation) and PCM (C-0117, inter-agent claims) — notably the first of the three from a frontier AI lab itself, not an academic security group, and the first with a full formal (Lean-verified) proof of its own protocol properties.

## LayerLens relevance
- open question(s) touched: #11 (the reviewer surface) — directly: Anthropic's own framing ("a user... without any information about the weights to verify") is close to open Q#11's exact phrasing (a reviewer accepting a claim without trusting the claimant). Strengthens I-0014 and T-09. The ~80x overhead and short-context limitation are a concrete calibration point for how far cryptographic verification is from being practical for a product like LayerLens today — worth citing as evidence this approach is promising but not yet buildable at agent-context scale.
