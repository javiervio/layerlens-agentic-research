# Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains

- authors_or_org: Yichiet Aun, Mohammed A. Alhartomi, Jing Jie Tan, Waqas Nadeem, Adeb Salh, Shankar Karuppayah et al.
- canonical_url: https://arxiv.org/abs/2611.06585
- discovered_url: inbox/arxiv/2026-W46.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.06585v1
- version: v1
- published_at: 2026-11-04
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: MCP, trust wall, isolation, germline execution, signed-but-not-safe

## Claims from this source
- C-0131: A signed/authenticated MCP tool can still conceal malicious code that performs its advertised function while leaking confidential information to a policy-allowed destination; Meta's MCPGuard-Dynamic (a state-of-the-art runtime defence) blocked a direct exfiltration attempt but failed to prevent this disguised attack in every trial. The authors propose "germline execution": each tool invocation runs in an ephemeral copy forked from a data-free "germline" process, each copy receiving only the information authorised for its destination, so even if malicious code executes, what it can disclose is bounded by the data available to its copy — proven as "sink noninterference" under stated confinement assumptions. Across 153 attack runs, germline execution detected zero unauthorised disclosures vs. 5.9-74.5% of runs under baseline defences/an ablation; invocations served by a single copy completed in 10-49ms, 2-28x faster than restarting the tool for every call.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; proof relies on stated assumptions about copy confinement and a data-free germline process; a single demonstrated attack construction, not a census of signed-tool threats.
  - relationship to existing claims: new, concrete evidence that authenticity/signing is not the same property as behavioral safety ("signed but not safe") — a sharper, MCP-specific instance of the "declared isolation is not verified isolation" lesson T-02 already tracks (Prime Intellect's inference-layer escape, Connection Escrow, Tracekit Box). Also structurally close to the trust wall (bound what a process can see, not just what it is allowed to do) and to T-09's proof-based verification cluster in spirit, though this is isolation-by-construction rather than cryptographic proof.

## LayerLens relevance
- open question(s) touched: #2 (attribution), #11-adjacent (trust beyond a signature/badge); general (tools and protocols scope — MCP named explicitly in SOURCES.md search vocabulary). Directly useful design-review language: a signed or verified status is not proof of safe behavior, matches LAYERLENS_CONTEXT's own "trust wall" differentiator precisely (bound what a process can see).
