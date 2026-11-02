# Agent Lightning v1.0: A 3,500-Line Lightweight Agentic RL Framework for Training Agents with Real Harnesses

- authors_or_org: Microsoft Research Asia
- canonical_url: https://www.microsoft.com/en-us/research/blog/agent-lightning-v1-0-a-3500-line-lightweight-agentic-rl-framework-for-training-agents-with-real-harnesses/
- discovered_url: inbox/reference/LATEST.md (Microsoft Research feed, 2026-W44)
- discovered_via: feed (reference harvester)
- doi_or_arxiv_id: n/a (blog post; underlying framework open-source)
- version: v1.0
- published_at: 2026-10-07
- retrieved_at: 2026-11-02
- source_type: docs / post
- access_scope: full text (fetched directly via WebFetch; microsoft.com remains reliably reachable)
- sections_read: full page
- topics: harness-coupled RL training, agent training infrastructure, harness as a first-class artifact

## Claims from this source
- C-0105: Agent Lightning v1.0 is an open-source RL framework (~3,500 lines) built around "Harnessed Agentic RL," where **"the same agent harness used in deployment participates directly in reinforcement learning"** — avoiding the common pattern of rebuilding an agent inside a training framework, which leaves the trained agent different from the deployed one. It works by placing an LLM proxy (an OpenAI-compatible API Gateway) between the unchanged harness and the model, recording prompts/responses/log-probs per rollout without the harness code needing to change; a Rollout Controller runs agent executions as local processes or Kubernetes jobs, separate from training; a Customized Trainer (built on verl) assembles training samples. On SWE-bench Verified, Qwen3.5-9B's Pass@1 rose from 41.8% to 56.4% (+14.6 points) using this approach with ~6,000 training samples built on SWE-smith/mini-SWE-agent; a "Collocated Async RL" mode reports ~2x end-to-end speedup over synchronous RL using fewer GPUs than conventional async RL.
  - locator: full page text
  - evidence_label: documented capability (first-party, directly read in full)
  - limitations: single-vendor framework; the Pass@1 gain is one benchmark/model pairing, not a broad census; "harness participates directly in training" is architecturally notable but the paper does not claim this transfers to harnesses with heavier external side effects (e.g., ones that call real paid APIs).
  - relationship to existing claims: new angle on T-01/T-06 — rather than treating the harness as a confound to control for when *evaluating* (C-0044, C-0093), this treats the harness as a first-class artifact worth *training through directly*, which implicitly validates the harness-matters thesis from the opposite direction (why bother keeping deployment and training harnesses identical, if harness didn't materially affect behavior?).

## LayerLens relevance
- open question(s) touched: general (environments/tools scope); loosely #1 (comparability — reinforces that harness identity is load-bearing enough that a frontier-lab-adjacent team built an entire training architecture around keeping it fixed, rather than training the harness away).
- Lower direct product relevance (this is a training-infrastructure paper, and LayerLens's Environments pillar is post-hoc evaluation, not RL training) but useful corroboration that "harness matters as much as model" (I-0004's build caution) is now acted on by builders, not just observed by auditors.
