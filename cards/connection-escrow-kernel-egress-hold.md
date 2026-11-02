# Connection Escrow: Holding AI-Agent Pod Egress in the Kernel Until an Isolated Verifier Rules

- authors_or_org: Ashok Subbabhatta Gopalakrishna
- canonical_url: https://arxiv.org/abs/2610.26501
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.OS)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.26501v1
- version: v1
- published_at: 2026-10-19
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox)
- sections_read: abstract
- topics: kernel-level isolation, egress control, trust-wall precedent, adversarial robustness of controls

## Claims from this source
- C-0102: Names the general problem directly: "controls placed between the agent and its tools are bypassed by a child process or a direct socket, and their approval is not tied to the connection the kernel later opens." **Connection escrow** parks every outbound TCP connection from a supervised pod inside the kernel's `connect()` path, before any packet exists, via a 98-instruction eBPF program on the pod's cgroup; a node interceptor attributes the held socket to process/executable digest/cgroup/pod identity, and a verifier in a **separate container with its own key** must return a signed verdict naming that exact socket cookie and destination before release — an expired or forged or late verdict is refused. A 36-check adversarial suite (real cgroups) passed on the eBPF hold point: forged/rebound/replayed/expired/late verdicts refused; child-process and renamed-binary bypasses failed; even the agent's own attempt to reach the verifier is itself escrowed. On a Kubernetes cluster, 600 connections from six pods were gated; the hold adds **4.5ms median per released connection** (24us of which is policy). A further extension gates on TLS-encrypted request *content* without terminating TLS, via an eBPF uprobe at the TLS-library boundary.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only), notable for an unusually thorough adversarial test suite described directly in the abstract
  - limitations: abstract only; single author; the 36-check suite's specific attack classes beyond the four named (forgery, replay, bypass-by-children, renamed binaries) not individually itemized here.
  - relationship to existing claims: **a close structural analogue to LayerLens's own trust wall**, but enforced at the kernel/egress layer rather than at the data-serving layer — this paper's core worry (a control that is "not tied to the connection the kernel later opens" can be bypassed) is precisely the "declared isolation is not verified isolation" lesson T-02 already draws from Prime Intellect's inference-layer sandbox escape (C-0051) and NVIDIA's platform (C-0050), now given a concrete, adversarially-tested countermeasure design rather than only a named vulnerability class.

## LayerLens relevance
- open question(s) touched: #2 (attribution), #11 (the reviewer surface — a verdict signed by an isolated verifier, checkable independent of the agent, is a strong instance of "accept a claim without trusting the claimant").
- Directly relevant to the trust-wall design-review checklist T-06/I-0007 already recommend ("verify LayerLens's own environments cannot be escaped via a similar inference-layer side-channel"): this paper supplies a concrete, adversarially-validated *pattern* (kernel-level hold-until-verdict, bound to the exact socket identity) rather than just another named escape. Worth flagging alongside C-0051/C-0050 as a candidate reference design if LayerLens's own trust wall is ever audited against side-channel bypass.
