# Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization

- authors_or_org: Anmol Agarwal, Natalie Neamtu, Pranjal Aggarwal, Seungone Kim, et al.
- canonical_url: https://arxiv.org/abs/2605.26457
- discovered_url: inbox/discovery/LATEST.md (openalex, 2026-W44) then inbox/fulltext/
- discovered_via: feed (discovery harvester)
- doi_or_arxiv_id: arXiv:2605.26457
- version: v1
- published_at: 2026-05-26
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (see the fulltext-harvester note in cards/are-gaia2-meta-environments.md — the inbox/fulltext/ file for this paper is the arXiv abstract page only, not the body)
- sections_read: abstract (verbatim)
- topics: verification-by-construction, LLM-as-judge limits, agentic environment design, formal specification

## Claims from this source
- C-0089: Verus-SpecGym is an agentic environment (581 Codeforces-derived spec-writing tasks, "Verus-SpecBench") where models interact with a real verifier (Verus, for Rust), bash, and the filesystem to write formal specifications; specs are graded by (a) extending the verifier so generated specs execute as real Rust code, tested against official tests plus adversarial "hack" cases, rather than (b) an LLM judge. The paper states directly: **"LLM-as-a-judge evaluation misses 26% of the failures our evaluator catches."** The strongest model (Gemini 3.1 Pro) solves 77.8% of tasks; other frontier models 51.1-57.8%; open-weight models only 21.5-25.5%.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; the 26% figure's exact denominator/methodology (how failures were enumerated, which LLM judge) not seen; single benchmark domain (formal verification of Rust code), may not generalize to open-ended tasks.
  - relationship to existing claims: **independently corroborates T-02/T-05's core argument with a concrete, execution-grounded number** — not a vendor claiming judges are biased, but a builder choosing a mechanical verifier specifically because the judge missed real failures, then quantifying the gap. Distinct evidence family from C-0002/C-0014/C-0027 (bias-focused) and C-0016 (agreement != verification) — this one is about judges' detection *recall*, not bias direction.
- C-0090 (same source): Even with a real, non-LLM verifier available, **spec autoformalization is "within reach for frontier agents but remains brittle even on problems where they can already generate correct code"** — the gap between generating correct code and generating a faithful formal spec of what "correct" means is itself hard, with common failure modes being specs that omit input assumptions, accept incorrect outputs, or reject valid ones.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: same as above.
  - relationship to existing claims: new angle on T-02 — distinguishes "can the agent solve the task" from "can the agent correctly specify what solving the task means," a sharper version of the ground-truth/answer-key authoring problem LayerLens's own minting already addresses by construction (the answer key is written in the same act as the data, not authored by an agent after the fact).

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — LLM judges miss real failures a mechanical check catches, a concrete number for keeping Graders load-bearing); differentiator #3 (reproducible, defensible grading).
- Directly strengthens the "keep deterministic Graders load-bearing" thread (T-02/T-05) with a builder's own quantified reason for choosing mechanical verification over an LLM judge, in a domain (formal spec-writing) far from benchmark-exploit auditing — a third kind of evidence (not bias, not gaming, but recall) for the same underlying design choice.
