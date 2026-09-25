# Prime Intellect — prime-rl and Verifiers (Environments Hub ecosystem)

- authors_or_org: Prime Intellect (PrimeIntellect-ai)
- canonical_url: https://github.com/PrimeIntellect-ai/prime-rl ; https://github.com/PrimeIntellect-ai/verifiers
- discovered_url: WebSearch "Prime Intellect environments hub reinforcement learning verification 2026" -> GitHub repos (primeintellect.ai and docs.primeintellect.ai were blocked by this session's network egress policy, so the marketing/docs site itself could not be opened — see run log)
- discovered_via: search (Prime Intellect is a seeded "team to watch" in SOURCES.md)
- doi_or_arxiv_id: n/a
- version: n/a (repo state at retrieval; verifiers repo shows 2,378 commits, 683 forks, 171 PRs, 18 open issues, 4,700+ stars per GitHub UI)
- published_at: date unknown (ongoing project)
- retrieved_at: 2026-09-25
- source_type: docs (GitHub repo pages, first-party)
- access_scope: sections listed — repo description/README highlights for both repos, not full documentation
- sections_read: prime-rl README (framework overview, Environments Hub integration), verifiers README (description, scale indicators)
- topics: RL environments, verifiable reward, agentic training infrastructure

## Claims from this source

- C-0006: prime-rl is an open-source, asynchronous RL training framework built for scale (1T+ parameter MoE models across 1000+ GPUs, FSDP2/vLLM/FP8/expert+context parallelism), covering SFT, RL, and evaluation, with native integration into the Verifiers library and the Environments Hub for task environments (including SWE and agentic benchmarks).
  - locator: prime-rl README
  - evidence_label: documented capability (first-party)
  - limitations: scale numbers (1T+ params, 1000+ GPUs) are the vendor's own framing of capability, not an independently benchmarked result; we did not read the Environments Hub's own site (blocked), so we cannot confirm its claimed size (a WebSearch summary mentioned "2,500+ open-source RL environments," but this was **not independently verified** — treat as unconfirmed pending a run where primeintellect.ai/docs.primeintellect.ai are reachable).
  - relationship to existing claims: new
- C-0006b: The Verifiers library ("our library for RL environments + evals") has real, verifiable GitHub activity: 4,700+ stars, 683 forks, 2,378 commits, 171 PRs, 18 open issues at retrieval time; originally created by Will Brown.
  - locator: verifiers repo page (GitHub UI stats)
  - evidence_label: documented capability (directly observed, not vendor-claimed)
  - limitations: stats are a snapshot, will change; do not describe specific reward/verification mechanics beyond "verification is central to the design" since the deeper docs were not reachable this run.
  - relationship to existing claims: new

## LayerLens relevance

- General / differentiator #2 (deterministic free minting and the trust wall): Prime Intellect's model is verifiable-reward RL training at scale (a training-infrastructure angle), which is adjacent to but distinct from LayerLens's Environments pillar (evaluation/readiness rather than RL training at 1000-GPU scale) — worth clarifying in a future run whether Prime Intellect's environments are used for agent *evaluation* the way LayerLens's are, or purely for *training* rollouts, since that changes whether they are a reference point or a genuine competitor.
- Pending: a full read of the Environments Hub's own site/docs (blocked this run) to confirm environment count, verification mechanism details, and any evaluation (not just training) use cases.
