# Towards a Science of AI Agent Reliability

- authors_or_org: Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan — Princeton (accepted as an ICML 2026 poster)
- canonical_url: https://arxiv.org/abs/2602.16666
- discovered_url: WebSearch ""Towards a Science of AI Agent Reliability" github repo pass@k variance" (followed a lead from the deliberate-contradicting-evidence search on non-determinism in agent evaluation)
- discovered_via: search
- doi_or_arxiv_id: arXiv:2602.16666
- version: not confirmed
- published_at: not confirmed (ICML 2026 poster listing implies acceptance well before the conference; exact arXiv submission date not surfaced)
- retrieved_at: 2026-09-28
- source_type: paper
- access_scope: abstract only, second-hand — arxiv.org, alphaxiv.org, and huggingface.co/papers (all three tried) were EGRESS_BLOCKED this run. A GitHub repo reportedly exists ("code to reproduce the experiments is available on GitHub" per search summaries) but its URL did not surface in any search result opened, and a direct GitHub search for it returned zero matches. Everything below is WebSearch's generated summary, not text opened directly.
- sections_read: none directly. Flagged **incomplete access (search summary only)**.
- topics: agent reliability, consistency, robustness, predictability, safety, pass@k vs pass^k, reliability metrics

## Claims from this source

- C-0008: The paper proposes twelve metrics decomposing agent reliability into four dimensions (consistency, robustness, predictability, safety), and distinguishes pass@k (probability at least one of k attempts succeeds — a capability measure, appropriate when any one success counts) from pass^k (probability all k attempts succeed — a reliability measure). Reported methodology: each task run K=5 times for consistency, J=5 paraphrases per prompt for robustness, and infrastructure faults (e.g. API errors) injected at p_fault=0.2. Reportedly evaluated 15 models across two benchmarks and found that recent capability gains "have only yielded small improvements in reliability."
  - locator: none — search-summary only.
  - evidence_label: incomplete access
  - limitations: no primary text opened; cannot confirm the exact 12 metrics, which two benchmarks were used, which 15 models, or the magnitude of "small improvements." The authorship (Kapoor and Narayanan are also behind the Holistic Agent Leaderboard / Pareto-curve critique of leaderboards — see the princeton-hal-leaderboard card) raises this claim's credibility as a lead worth pursuing, but authorship reputation is not a substitute for reading the paper, and this is explicitly noted as a confidence factor, not evidence.
  - relationship to existing claims: new — directly on point for open question #5, where our knowledge base previously had nothing.

## LayerLens relevance

- **Open question #5, almost verbatim**: "A new model call does not guarantee the same trajectory; how do we express variation across attempts (reliability versus one lucky pass)?" The pass@k / pass^k distinction is exactly this question stated as a metric design choice — pass@k rewards a lucky pass, pass^k does not. If LayerLens's Optimize/Runs surfaces are currently reporting something pass@k-shaped (e.g. "did this pass at least once"), this paper (once actually read) would be the direct citation to justify also surfacing a pass^k-shaped view (did it pass reliably across repeats).
- Also touches open question #1 (comparability): a reliability metric only means something if the repeat count (k) and the perturbation method (paraphrase, fault injection) are stated alongside the number — another instance of PROTOCOL.md's evidence-discipline rule #7 ("check numbers are comparable before ranking them").
- Action for next run: high priority to actually open this paper — try arxiv.org/pdf/2602.16666 directly (sometimes /pdf/ routes differ from /abs/ in what gets blocked), and do a targeted search for the GitHub org of the Princeton PLI/SAgE group (same lab as HAL) since the repo is reported to exist but its URL was not found this run.
