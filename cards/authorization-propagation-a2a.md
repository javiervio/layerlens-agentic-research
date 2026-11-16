# Authorization Propagation in Agent2Agent Systems: An Experimental Security Evaluation of Multi-Hop Delegation

- authors_or_org: Gabriele Donno, Kashif Mehmood, Katina Kralevska
- canonical_url: https://arxiv.org/abs/2611.07050
- discovered_url: inbox/arxiv/2026-W46.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.07050v1
- version: v1
- published_at: 2026-11-04
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: A2A protocol, authorization, delegation, multi-hop security

## Claims from this source
- C-0140: Delegated Agent2Agent (A2A) workflows create a security problem when the agent sending a request differs from the principal the authority originated from. Evaluating a layered downstream-verification design in a synthetic four-party healthcare reimbursement workflow (separating current-caller context, transitive authorization evidence, per-hop Ed25519 request authentication, and independent replay state for requests and authorization artifacts), 14 of 15 adversarial conditions were rejected; an isolated delegation-path test exposed the absence of semantic authority attenuation (authority does not narrow as it passes through hops). A separate authorized-intermediary experiment showed a holder of the shared authorization-evidence HMAC key can modify the represented authority and generate valid evidence. Full-configuration median security-processing latency was 5.11ms with a 3.87kB serialized payload.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; one synthetic four-party workflow; a prototype, not a production A2A deployment.
  - relationship to existing claims: new evidence directly on A2A (named in SOURCES.md's own "Integration" search vocabulary alongside MCP/AG-UI), extending I-0013 (provenance/authority tracking) to the specific case of authority attenuating across delegation hops, and corroborating T-02's "signed is not sufficient" pattern this week (C-0131, C-0135): a shared HMAC key holder here can still forge a valid-looking authorization artifact.

## LayerLens relevance
- open question(s) touched: #7 (human control, authority/delegation), general (tools and protocols — A2A). Relevant if LayerLens's own system types or any multi-agent-under-test ever uses A2A-style delegation between agents.
