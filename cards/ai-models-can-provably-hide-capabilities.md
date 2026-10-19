# AI Models Can Provably Hide Arbitrary Capabilities

- authors_or_org: Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, Christian Schroeder de Witt
- canonical_url: https://arxiv.org/abs/2610.13928
- discovered_url: inbox/arxiv/LATEST.md (2026-W42 harvest)
- discovered_via: feed
- doi_or_arxiv_id: 2610.13928v1
- version: v1
- published_at: 2026-10-09
- retrieved_at: 2026-10-19
- source_type: paper
- access_scope: abstract (verbatim, directly read via arXiv harvester inbox)
- sections_read: abstract only
- topics: capability evaluation, elicitation, cryptographic backdoors, verification limits

## Claims from this source
- C-0063: Capability evaluations assume a hidden capability can be elicited if present. This paper constructs backdoor attacks embedding encrypted neural networks inside host model weights, decrypting and executing only on a secret trigger ("digital lockers"), extending prior string-hiding work to arbitrary hidden computations. Implemented as a proof of concept (PyTorch, a chemical-reaction-prediction proxy task for CBRN-relevant capability), the hidden circuits resist elicitation via fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training, under stated cryptographic assumptions, even with full weight access.
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly; proof-of-concept + cryptographic argument, not an observed in-the-wild case)
  - limitations: abstract only; a proxy task (chemical reaction prediction), not a real CBRN capability; "resists elicitation" demonstrated against the four named methods only, not an exhaustive defense survey
  - relationship to existing claims: a structurally new angle for T-02 — prior evidence (BenchJack, HackDetect, Unearned Passes, Near-Zero Monitor Readout) shows verification is *empirically* gameable or blind in practice; this paper argues a *provable, cryptographic* limit exists on elicitation-based audits in principle, i.e. even a perfect, well-resourced audit process can be structurally defeated, not just an under-resourced one. This sharpens T-02's framing from "verification is often gamed" to "verification-by-elicitation has a hard ceiling," which is a stronger and more durable caution.

## LayerLens relevance
- open question(s) touched: #2 (attribution/trust); general positioning — this is a caution against *any* elicitation-only verification strategy (does the agent behave correctly when asked/tested), which reinforces why LayerLens's deterministic, answer-key-based Graders (grading actual outcomes against ground truth, not asking the model to self-report or demonstrate on demand) are a structurally different and more defensible verification class than elicitation-style capability probes. Not directly actionable for a product feature, but a positioning-relevant finding worth citing when explaining why "graded by outcome" beats "graded by self-demonstration."
