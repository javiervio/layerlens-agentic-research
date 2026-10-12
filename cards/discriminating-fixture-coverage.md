# Discriminating Fixture Coverage in Agent-Infrastructure Verification Suites

- authors_or_org: Xin Xu, Siru Tao
- canonical_url: https://arxiv.org/abs/2610.02928v1
- discovered_url: inbox/arxiv/LATEST.md (2026-W41 harvest, cs.SE)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2610.02928v1
- version: v1
- published_at: 2026-10-02
- retrieved_at: 2026-10-12
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the harvested inbox; arxiv.org itself not reachable this run)
- sections_read: abstract
- topics: verification suite validity, mutation testing, invariant suites, agent infrastructure

## Claims from this source
- C-0046: Applying mutation analysis to an invariant suite for a multi-session agent state-projection layer: the standard validation practice (suite passes a believed-correct implementation, fails a believed-broken one) certified a suite in which a mutant removing event-identity deduplication survived every check. After repair, running the frozen 12-check suite against 10 adversarially-designed mutants it was never built against, it killed only 5; the other 5 failed in two distinct, previously invisible ways (3 never activated because no fixture exercised that input; 2 corrupted state no oracle in the suite could observe) — neither visible from a pass/fail report. Enumerating seven discriminating input-space dimensions and adding one fixture per uncovered dimension (reusing existing oracles) killed all 5 remaining survivors.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly; a pre-registered repair result on the authors' own challenge set, not an independently held-out estimate — the authors themselves flag this distinction)
  - limitations: abstract only; single verification suite/system (a multi-session agent state-projection layer); "repair result on the same challenge set" per the authors, not a second held-out validation.
  - relationship to existing claims: a new, structurally distinct family for T-02 (benchmark/verification trust is collapsing) — prior T-02 evidence audits *benchmarks* (agent-facing scoring) for exploitability; this audits a *verification/invariant suite itself* (infrastructure-facing correctness checks) for coverage gaps, using mutation testing rather than exploit-construction. The core finding generalizes directly: "the suite passes a known-good and fails a known-bad implementation" is exactly the validation standard most verification infrastructure (including, plausibly, LayerLens's own graders) would cite as proof of correctness, and this paper shows that standard alone is insufficient — a suite can pass that bar and still miss real defect classes.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — a grader/verifier that "passes" is not proof its coverage is complete), #3 (deterministic replayability, adjacent — an under-covered invariant suite can silently certify a broken restore). Strengthens I-0003/F-0002 with a genuinely new angle: a candidate internal practice (mutation-test LayerLens's own answer-key/action/state graders, not just the agents they grade) worth naming as a possible method, distinct from attribution-in-the-UI. Not a new idea/feature row this run (dedup discipline) — recorded as a method/claim to fold into I-0003's evidence and as a positioning note that "our graders are deterministic" is a necessary, not sufficient, trust claim.
