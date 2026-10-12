# ContractWarden and Agent-Warden: kernel-level damage boundaries and provenance tracking for LLM agents

- authors_or_org: Dongxu Cui, Zhichao Gu, Ping Zheng, Wenshuai Xi, Simeng Han, Yong Liao (ContractWarden adds Wenshuai Xi); overlapping author team, same research group
- canonical_url: ContractWarden https://arxiv.org/abs/2609.38248v1 ; Agent-Warden https://arxiv.org/abs/2609.38245v1
- discovered_url: inbox/arxiv/LATEST.md (2026-W41 harvest, cs.OS)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2609.38248v1 (ContractWarden); arXiv:2609.38245v1 (Agent-Warden)
- version: v1 (both)
- published_at: 2026-09-29 (both)
- retrieved_at: 2026-10-12
- source_type: paper (two companion papers)
- access_scope: abstract only for both (verbatim, read directly from the harvested inbox; arxiv.org itself not reachable this run)
- sections_read: abstracts
- topics: human-authorized oversight, consequence boundaries, kernel-level enforcement, provenance/attribution

## Claims from this source
- C-0047 (ContractWarden): A Linux reference monitor enforces a human-authorized "damage boundary" without trusting the agent or its own policy suggestions: a model may *propose* a tri-state asset contract (allow / deny / no_egress), but a human makes the final choice; an execution gate binds the contract to a concrete task before untrusted code runs; an eBPF/LSM data plane then enforces file/network decisions and monotonically propagates `no_egress` through child processes, files, pipes, and sockets. All 570 runs across 19 security tests satisfied predefined criteria; median overhead 11.96-12.89% (VM) / 35.79-61.54% (physical), lower than a baseline (frozen ActPlane).
- C-0048 (Agent-Warden): A companion eBPF-based provenance monitor tracks task/file state across process creation, file access, and termination, invisible to application-layer tracing. In a controlled file-mediated propagation scenario it reconstructed a cross-process causal chain *absent from the application-layer trace*. Overhead 0.2-3.5% end-to-end, 0.6-3.7% additional system CPU, on x86-64/ARM64 bare metal.
  - locator: abstracts, verbatim
  - evidence_label: bounded empirical (abstracts read directly)
  - limitations: abstracts only; single research group's own benchmarks; Linux/eBPF-specific (kernel-level approach, not obviously portable to LayerLens's own cloud-hosted, system-type-based architecture which wraps external APIs rather than local OS resources).
  - relationship to existing claims: ContractWarden is a new, concrete design pattern for T-04 (consequence legibility is white space) and open question #7 — distinct from Magentic-UI's three-tier *per-call* approval (C-0011): this is an upfront, task-scoped *contract* a human authorizes once, then kernel-enforced regardless of what the agent later proposes. Agent-Warden is a new, concrete family for open question #2/T-03 (failure attribution) and I-0003 — its headline result (a causal chain invisible at the application/trace layer, recovered only by watching OS-level effects) is a sharp, literal illustration of why trace-only attribution can be incomplete, directly resonant with LayerLens's own "where a failure happens is everything" premise, even though the mechanism (kernel tracing) does not map onto LayerLens's own system-type architecture.

## LayerLens relevance
- open question(s) touched: ContractWarden -> #7 (human control — a contract-based, pre-authorized boundary is a different mechanism from a per-action confirmation; worth comparing against I-0006's consequence-preview hypothesis, which is about per-action framing, not upfront scope contracts). Agent-Warden -> #2 (attribution — attach as evidence to I-0003/F-0002: real attribution signal sometimes requires watching effects below the trace, not just the trace itself, even though LayerLens's own environments are API/record-based rather than OS-level). Neither is a new idea/feature row this run (dedup discipline): both fold into existing I-0003 and I-0006 threads as evidence and design-pattern comparisons.
