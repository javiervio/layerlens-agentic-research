# ThinkingBox — "The Agent Said It Was Done. The Database Disagreed."

- authors_or_org: Microsoft (reportedly with Hugging Face co-publication); one secondary source names Microsoft applied scientist Tuhin Kundu
- canonical_url: unconfirmed exact page (https://huggingface.co/blog/microsoft/thinkingbox was the inbox-listed link but huggingface.co is EGRESS_BLOCKED in this sandbox and the page was not independently opened)
- discovered_url: inbox/reference/LATEST.md (2026-W41 harvest, Hugging Face feed) title, then WebSearch for content
- discovered_via: feed (reference inbox harvester, title only) then search
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: disputed across secondary sources (one: 2026-10-03 joint HF/Microsoft post; another: an August 19, 2026 Microsoft Command Line blog post for an earlier open-source sandbox framework version; a third: September 9, 2026 per a newsletter aggregator) — treat publication date as unconfirmed
- retrieved_at: 2026-10-12
- source_type: post (benchmark announcement, read via multiple secondary summaries only; dates and framing conflict across sources, flagged honestly rather than resolved)
- access_scope: incomplete access (several independent secondary summaries agree on the benchmark's core design and headline numbers; the original Hugging Face/Microsoft post was not independently opened)
- sections_read: n/a (secondary summaries only)
- topics: outcome-vs-state grading, reliability (pass@k vs pass^k), false-success claims, enterprise benchmark

## Claims from this source
- C-0053: ThinkingBox is reported as a 507-task stateful business-workflow benchmark (retail, auto insurance, travel, neobanking, consulting support) that grades agents only by what they actually leave behind in the database/system state, not by what the agent claims at the end. Its illustrative example: a support agent makes nine tool calls and closes a ticket as "resolved" even though the database shows a required field (a carrier exception) still open — the ticket should have stayed on hold. One secondary source reports a headline reliability gap it calls the "discovery-reliability gap": the best-performing model reached 65.36% pass@1 but only 25.25% pass^20 (succeeding on all of 20 repeated attempts).
  - locator: multiple independent secondary summaries (runtimewire.com, cryptobriefing.com, hermes-ai.net, toolnavs.com), broadly consistent on the benchmark design and the illustrative example; the exact pass@1/pass^20 figures come from one source (cryptobriefing.com) and were not independently cross-verified against a second
  - evidence_label: incomplete access (no primary source opened; the benchmark's existence and design are corroborated across several independent secondary outlets, but the headline numbers rest on a single secondary source and the publication date is disputed across sources — both flagged rather than treated as settled)
  - limitations: no primary text; pass@1/pass^20 numbers single-sourced; publication date genuinely unclear (three different dates reported by three sources).
  - relationship to existing claims: a vivid, concrete new family for two ideas at once. For I-0001/F-0001 (pass^k reliability readout): a large, named benchmark reporting a near-40-point gap between pass@1 and pass^20 is exactly the kind of number that would motivate a pass^k readout, if confirmed. For I-0003/F-0002 and T-02 (attribution, false-success claims): the "ticket closed as resolved, database says otherwise" example is architecturally identical to C-0022's finding (agents report success without evidence after a failure) and to LayerLens's own existing V1 design choice (claims stored beside verdicts, never used as evidence) — ThinkingBox appears to operationalize exactly that principle as a benchmark's grading philosophy (grade state, not self-report).

## LayerLens relevance
- open question(s) touched: #5 (reliability vs. one lucky pass — directly, if the pass@1/pass^20 numbers hold up), #2 (attribution — state-based grading over self-report, validating an existing V1 choice). Given the access-scope and date caveats, this is recorded as a lead worth a direct read (if huggingface.co ever becomes reachable, or via a local full-web session) rather than fully load-bearing evidence yet. No new idea/feature row created (dedup discipline): strengthens I-0001 and I-0003 as a pending-confirmation data point.
- **Recheck priority**: next run should attempt to open the primary Hugging Face/Microsoft post directly to resolve the publication-date conflict and verify the pass@1/pass^20 figures before they are relied on in a design decision.
