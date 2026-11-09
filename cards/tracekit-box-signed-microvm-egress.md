# Tracekit Box: Running AI Agents in Micro-VMs Where Every Way Out Is Decided and Signed

- authors_or_org: Bravish Ghosh
- canonical_url: https://arxiv.org/abs/2610.38458v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.OS harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.38458v1
- version: v1
- published_at: 2026-10-28
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox; arxiv.org itself unreachable)
- sections_read: abstract
- topics: environments, trust wall / isolation, egress control, attestation

## Claims from this source
- C-0112: Tracekit Box is an open-source (MIT, v0) system that runs each agent job in its own Firecracker micro-VM with no network card; every way out (commands, outbound connections, secrets, model calls, the workspace patch) is a host-served "door" over vsock, gated by a signer the agent cannot reach, with names resolved on the host, private/cloud-metadata addresses always refused, secrets swapped in only at the proxy, and changes returned as a signed, per-file patch. All 13 end-to-end checks passed on a real KVM runner; 15 fuzz targets on the trust boundary found 9 findings, all fixed; a 102-record demo run verified offline as a `.tkb` bundle.
  - locator: abstract (verbatim)
  - evidence_label: bounded empirical (single-author system paper, self-reported test/fuzz results, not independently reproduced)
  - limitations: single author; does not yet run Firecracker's jailer; needs a co-located signer; only logs in-VM processes where they cross a door, not fully; self-reported fuzzing/test numbers, not third-party audited.
  - relationship to existing claims: extends T-02 (declared isolation vs verified isolation) with a concrete, open, fail-closed, signed-and-verifiable-offline reference design — closer to LayerLens's own trust-wall shape (a boundary the agent cannot see behind) than prior entries (Connection Escrow/C-0102 is the closest existing analogue; this is a full-VM, not just an egress-hold, design).

## LayerLens relevance
- open question(s) touched: #3 (deterministic replayability — the `.tkb` bundle is an offline-verifiable per-run artifact), #11 (reviewer surface — verification does not require trusting the operator)
