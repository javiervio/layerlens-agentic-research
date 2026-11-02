# Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance

- authors_or_org: Antonio Ken Iannillo, Joshua Segun Owotogbe, Roberto Natella, Francesco Avallone, Kristina Kudryavtseva, Indika Kumara
- canonical_url: https://arxiv.org/abs/2610.32555
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.SE)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.32555v1
- version: v1
- published_at: 2026-10-23
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox)
- sections_read: abstract
- topics: MCP fault injection, tool-calling reliability, harness-level error handling, capability vs. robustness

## Claims from this source
- C-0095: MCP-Injector is a protocol-aware fault-injection middleware calibrated against the **observed incident distribution of the real public MCP ecosystem** (mined from 57,240 issue/PR threads across 1,774 open-source MCP repositories), injecting permanent/transient/intermittent tool faults. Across a 1,350-cell experiment (two model sizes — 20B, 120B — three agent stacks: custom plan-and-execute, OpenAI Agents SDK, LangChain — three fault conditions): a permanent-heavy stress profile caused task-completion score to fall **60%, from 8.08 to 3.23 out of 10**, and **the larger (120B) model retained no larger share of its fault-free score under faults than the smaller (20B) model** (resilience-ratio model, p=0.96) — its completion rate under faults was, if anything, lower. The authors conclude **"framework-level error handling matters more than model scale."**
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; two model sizes within one family (gpt-oss), not a broad model census; fault profile calibrated to public MCP repos specifically, may not represent LayerLens's own shipped system types (Salesforce/Linear/SEC EDGAR/Stripe/Gmail) which are not raw MCP tool wrappers.
  - relationship to existing claims: **a third independent instance of thesis T-07** (capability does not self-correct for flawed interfaces) — the title states the finding almost as a restatement of T-07 itself, and "scale does not purchase fault tolerance" is the cleanest, most quantified version of this pattern recorded yet (alongside C-0018's MCP error-message finding and C-0021's capability-correlates-with-more-exploitation finding). Directly strengthens I-0009.

## LayerLens relevance
- open question(s) touched: #2 (attribution — a tool fault vs. a model reasoning failure are distinguishable causes this paper's own framework separates), #7 (recovery).
- This is squarely on-point for I-0009 (agent-actionable error and recovery guidance): LayerLens's own system types wrap real APIs that do fail (rate limits, auth expiry, transient errors), and this paper shows directly that a bigger/better model does not compensate for a badly-handled fault — reinforcing that "framework-level error handling" (i.e., what the environment's tool surfaces communicate on failure) is the leverage point, not model choice. Strengthens T-07 to three families and I-0009's evidence base.
