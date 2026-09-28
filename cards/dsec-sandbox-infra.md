# DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale

- authors_or_org: Jialiang Huang and 130 others, DeepSeek
- canonical_url: https://arxiv.org/abs/2609.22978
- discovered_url: shared by Javier (arxiv.org/html/2609.22978v1)
- discovered_via: Javier
- doi_or_arxiv_id: arXiv:2609.22978
- version: v1
- published_at: 2026-09-19
- retrieved_at: 2026-09-29 (manual deep-read, local session with full web access)
- source_type: paper
- access_scope: abstract + HTML body (architecture, lifecycle, scale, evaluation) read directly; full appendices not read
- topics: sandbox infrastructure, agentic training, RL rollout, microVM, snapshot, environment lifecycle, scale

## Claims from this source
- C-0012: A frontier lab has published production-scale sandbox INFRASTRUCTURE for agentic RL training and evaluation, and it explicitly does not do environment generation, verification, or answer keys.
  - locator: abstract, architecture and evaluation sections
  - What it is: DSec is DeepSeek's production sandbox platform exposing four backends (FnCall, container, microVM, full-VM) behind one SDK, co-designed with their RL framework; it served all sandbox workloads for RL training and evaluation from DeepSeek V3.2 to V4.1.
  - Scale (directly read): one unit ~160 nodes (30K cores, ~250 TB DRAM), ~3M sandboxes/day, ~380K concurrent, 5,000+ creations/second, up to 800 microVMs or 3,200 containers per node.
  - Lifecycle and state: create -> prepare -> stateful interaction -> terminate (stop or TTL). microVM pause saves memory+execution state to a snapshot and kills the Firecracker process; resume restores it. `pack_diff` checkpoints a sandbox as an incremental disk snapshot that can be restored as a new sandbox.
  - Performance: on-demand image loading 1.71x faster than eager pull; composable EROFS layers 1.76x faster task completion; 40.2% peak host memory reduction with virtio-pmem; QoS CPU scheduling cut SMT latency inflation from 45.2% to 17.3% under overcommit.
  - Explicitly absent: no automated environment generation, no verification/grading, no answer-key or ground-truth mechanism. It is a runtime substrate, not a verification product.
  - evidence_label: bounded empirical (directly read; a first-party systems paper with its own benchmarks, not independently reproduced)
  - limitations: single vendor's internal platform; infra metrics are self-reported; nothing about agent correctness or task validity.

## Relationship to LayerLens (the important part)
DSec is a DIFFERENT LAYER from LayerLens, not a competitor. DSec runs sandboxes at scale to TRAIN models. LayerLens mints deterministic environments with an answer key by construction to PROVE whether an agent did the job and to attribute failures (env vs agent). DSec is a substrate LayerLens could conceivably run on; it is not a substitute for verification, attribution, or the trust wall. Its lifecycle mechanics (stateful pause/resume, pack_diff checkpoint/branch) are backend capabilities; LayerLens's opportunity is to make environment lifecycle legible and verifiable in the product (see I-0007). Validation, not threat: environments are now an industrial-scale concern.

## LayerLens relevance
- Positioning ammunition (infra to run vs instrument to verify). Feeds nursery thesis N-03.
- Open questions: what state an environment keeps and when it ends (control/recovery), and deterministic replay as a visible surface.
