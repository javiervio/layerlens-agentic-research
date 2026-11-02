# Permission to Retry: A Study of Authorization and Recovery in AI Agent Workflows

- authors_or_org: Deekshith Marla, Kushagra Bhatnagar
- canonical_url: https://arxiv.org/abs/2610.31916
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.SE)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.31916v1
- version: v1
- published_at: 2026-10-22
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox)
- sections_read: abstract
- topics: authorization, recovery, checkpoint/retry semantics, conformance testing

## Claims from this source
- C-0100: The paper decomposes a durable agent's resume/retry behavior into **four distinct obligations**: checkpoint state, permission to dispatch, evidence of an external effect, and permission to reconcile — arguing these are separable concerns, not one blended "did it work" question. A prospectively-frozen conformance study executed **336 histories** on native LangGraph and Temporal hosts, crossing 14 schedules, three provider contracts, and four application policies, scored against a **provider effect ledger hidden from the recovering application** (i.e., the test checks against ground truth the agent cannot see, a BenchJack-style isolation design). All 168 paired host cells had identical checked outcomes (host-portability result). Per host: retained-ledger reconciliation passed all 42 histories (21 checked completions, 15 denials, 6 unknown-outcomes-with-reservations-retained); cached retry, revalidation-before-retry, and stable-key retry passed 30/36/31 histories respectively (not perfect). A separate 16-case component study on a real enterprise platform (InfinityOS, Arya.ai) exercised exported authority/worker/recovery/settlement code against repository fakes.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; two specific hosts (LangGraph, Temporal); the 30/36/31 (not-all-passing) results for three of four retry strategies are not broken down by failure mode in what was read.
  - relationship to existing claims: new — closest thing yet in this knowledge base to a formal taxonomy of what "safe retry" requires, complementary to (not the same as) C-0026/ACRFence's attack-focused framing (T-06's remote-state branch) and C-0034's governance-layer proposal — this paper's four-obligation split (checkpoint / dispatch permission / effect evidence / reconciliation permission) is a concrete decomposition a LayerLens checkpoint/branch/retry feature could borrow directly.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery), #3 (deterministic replayability — the "hidden provider effect ledger" test design is structurally similar to LayerLens's own trust wall, checking against ground truth the agent-under-test cannot see).
- Strengthens **I-0006** (confirmations naming specific consequences) and **I-0007** (lifecycle legibility/checkpoint-branch): a confirmation or recovery affordance over a remote-write system type (Stripe, Salesforce) should make these four obligations visible and distinct, rather than collapsing them into a single "retry?" prompt — a concrete design decomposition to test LayerLens's own retry/recovery UI against, once product access allows it.
