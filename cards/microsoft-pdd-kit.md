# Formally verifying agent-written full-stack web apps with PDD Kit

- authors_or_org: Alex Lavaee, Matthai Philipose, Microsoft Research
- canonical_url: https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/
- discovered_url: inbox/reference/LATEST.md (Microsoft Research feed, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-11-05
- retrieved_at: 2026-11-23
- source_type: post
- access_scope: full text, read directly (WebFetch; microsoft.com reliably reachable per SOURCES.md)
- sections_read: full text
- topics: formal verification, grader design, proof vs test, agent-written code

## Claims from this source
- C-0175: PDD Kit ("Proof-Driven Development," a research prototype, Rust-only today) addresses the problem that agent-written code is too voluminous to review line-by-line, and that agent-written tests tend to check what was built rather than what was requested, so test coverage can look healthy while the gap between request and implementation stays hidden. It reads code, asks clarifying questions, and records answers in an "intent artifact" linking each requirement to a formal Verus specification (where formalizable) or an informal spec checked by tests (for the rest); external services are modeled as uninterpreted, trust-boundary functions. The key distinction stated: "A passing test only shows the code worked on the inputs it tried," while "Verus proves" a property holds "for every input." Safeguards include a mutation check (planting one bug per `ensures` clause; a surviving mutant flags a clause that constrains nothing) and an LLM gap review for unproven, unchecked requirements; the authors explicitly warn against "vibe verification" (weak specs that verify but rule out little). On a ~5,000-line Rust pilot app, a login flow yielded eight `ensures` clauses, six trusted pieces, and a seven-task build plan; the developer merged without line-by-line review of the generated code. Stated limitation: "a wrong spec is still possible" — a proof shows code meets the spec, not that the spec is what the developer meant.
  - locator: full post text
  - evidence_label: documented capability (first-party, directly read; a research prototype, not generally available)
  - limitations: Rust-only; "proofs still take real effort, mostly in producing the proof itself"; unproven properties remain (e.g. whether the login future completes, timing, rate limiting); the whole chain (Verus, rustc, Z3, vstd) is itself assumed correct.
  - relationship to existing claims: converges this week with Soteria (C-0161, formally verified planning) and EvoTrias (C-0162, protected judge authority) on formal/proof-based verification layered over agent-generated artifacts — a genuine three-source convergence (two academic papers, one frontier-lab research prototype) in a single week. Its "test is evidence, proof is for every input" distinction is a new, nameable evidence-quality tier above LayerLens's own existing deterministic Graders.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — "proof vs test" is a stronger evidence-quality distinction than LayerLens's current grader taxonomy names explicitly), #11 (reviewer surface — a reviewer shown "this was proven, not just tested" is a stronger claim than a pass/fail badge)
- general: motivates a new idea, I-0015 (grade agent-written code/plans against a formally verified specification, not only tests), created this run from this source plus Soteria (C-0161).
