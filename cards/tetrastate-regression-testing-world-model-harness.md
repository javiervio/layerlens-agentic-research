# One Verdict Is Not Enough: Regression Testing Learned World Models and Their Test Harnesses

- authors_or_org: Junyu Huo, Zihao Wan, Ziqi Mao, Gouri Ginde
- canonical_url: https://arxiv.org/abs/2610.41130v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.SE harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.41130v1
- version: v1
- published_at: 2026-10-30
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: comparability, harness as confound, verifier/grader integrity

## Claims from this source
- C-0115: TetraState is a regression-testing protocol (paired possible/impossible video tests) that runs each test under four fixed model-native configurations and assigns one of four outcome classes from the count of correct verdicts, reporting inconclusive/failed-execution tests separately and versioning the harness as part of the system under test. On all 506 IntPhys 2 Main tests across two systems (Cosmos 3 Nano, V-JEPA 2), two V-JEPA 2 harness revisions moved modal accuracy by only 0.2 and 2.6 points yet changed 11 and 214 individual test labels; in the second revision, accuracy rose even though fewer tests were judged correctly, and 43 regressions kept the same modal verdict, so a check that only watches the modal-verdict flip would miss them.
  - locator: abstract (verbatim)
  - evidence_label: bounded empirical (a concrete protocol applied to two real systems/harness revisions, with a named benchmark of 506 tests)
  - limitations: abstract only; two systems, two harness revisions — not yet a broad census; the authors themselves frame this as opening "a research agenda," not a finished solution.
  - relationship to existing claims: a sharp, small-scale but concrete instance of PROTOCOL.md's own comparability rule and T-01's harness-as-confound pattern — a harness revision that barely moves the *aggregate* score can still flip over 40% of *individual* test labels (214/506), and can even raise accuracy while a check that only watches the modal verdict misses real regressions. This is a vivid number for "a near-identical top-line score can mask large per-test churn," distinct from C-0044/C-0093's model-ranking-reversal framing.

## LayerLens relevance
- open question(s) touched: #1 (comparability — version the harness as part of the system under test, exactly LayerLens's own "immutable versions" differentiator), #5 (what "repeat a run" means — a harness bump is itself a kind of non-repeat)
