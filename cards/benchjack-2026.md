# Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack

- authors_or_org: Hao Wang, Hanchen Li, Qiuyang Mang, Alvin Cheung, Koushik Sen, Dawn Song (2026)
- canonical_url: https://arxiv.org/abs/2605.12673
- discovered_url: https://www.google.com search "BenchJack github reward hacking agent benchmark audit" -> https://github.com/benchjack/benchjack
- discovered_via: search
- doi_or_arxiv_id: arXiv:2605.12673
- version: v1 (as cited in the project README; arxiv.org itself was unreachable this run, see limitations)
- published_at: May 2026
- retrieved_at: 2026-09-25
- source_type: post (project README, author-published summary of the paper)
- access_scope: sections listed — the GitHub README (results table, methodology summary, limitations, citation), not the arXiv PDF/HTML itself (arxiv.org was blocked by this session's network egress policy; see run log)
- sections_read: README.md in full (What It Is, Core Audit Pipeline, Audit Results table, Vulnerability Classes V1-V8, Citation, Key Limitations)
- topics: reward hacking, benchmark validity, evaluation integrity, agent/evaluator isolation

## Claims from this source

- C-0001: BenchJack, an automated red-team auditor combining static analysis (Semgrep, Bandit, Hadolint) with AI-driven reconnaissance and proof-of-concept exploit construction, found all 8 major agent benchmarks it audited (SWE-bench Verified, SWE-bench Pro, Terminal-Bench, WebArena, FieldWorkArena, OSWorld, GAIA, CAR-bench; 4,458 tasks total) to be exploitable, with 6 of 8 producing ~98-100% scores via exploits that did no genuine task-solving.
  - locator: README "Audit Results" table
  - evidence_label: bounded empirical
  - limitations: 8 benchmarks is not a census of the field; audited at a point in time — maintainers may have since patched; PoC exploits were "not automatically verified against targets" per the authors' own limitations list; the paper itself (methodology detail, statistics, related work) was not read directly.
  - relationship to existing claims: new
- C-0001b: BenchJack organizes exploit types into 8 vulnerability classes (V1: no agent/evaluator isolation; V2: ground-truth answers accessible at runtime; V3: RCE on untrusted input; V4: LLM judges vulnerable to prompt injection; V5: weak string-matching scoring; V6: evaluation edge-case gaps; V7: untrusted code runs with evaluator privileges; V8: unnecessary agent permissions).
  - locator: README "Vulnerability Classes (V1-V8)"
  - evidence_label: proposal / interpretation (a taxonomy proposed by the authors)
  - limitations: taxonomy, not independently validated against a broader benchmark population
  - relationship to existing claims: new
- C-0001c: In a follow-up iterative generative-adversarial pipeline (per the earlier WebSearch synthesis, not independently opened), applying patches iteratively reduced the ratio of hackable tasks from near 100% to <10% on four representative well-designed benchmarks.
  - locator: not independently verified — this detail came from a WebSearch summary, not from the opened README; flagged as **incomplete access**, do not treat as confirmed until a primary source is opened.
  - evidence_label: incomplete access
  - limitations: search-snippet only
  - relationship to existing claims: new, unconfirmed

## LayerLens relevance

- Open question #2 (Failure attribution in the UI): a benchmark where the agent can read the answer key or hijack the evaluator makes agent-vs-environment attribution meaningless — the "verdict" is manufactured, not diagnosed. This is the strongest available field evidence for why LayerLens's stated "trust wall" (seed/knobs never served to an agent-facing key) is addressing a documented, exploitable class of problem (V1, V2 in BenchJack's taxonomy) rather than a hypothetical one.
- General: also relevant to the differentiator "reproducible, defensible grading" — V4 (judge prompt-injection) and V5 (weak string matching) are exactly the failure modes that motivate keeping deterministic Graders load-bearing over Judges/Scorers.
- Note: arXiv (arxiv.org, all subdomains and mirrors tried: pith.science) was blocked by this session's egress policy throughout this run. The full paper's methodology and statistics beyond what the authors' own README states were not accessible. Recheck when network access allows opening the PDF/HTML directly.
