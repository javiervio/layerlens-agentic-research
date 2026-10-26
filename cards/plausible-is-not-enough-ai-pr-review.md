# Plausible Is Not Enough: Trust and Evidence in AI-Authored Pull Request Review

- authors_or_org: Md Shamimur Rahman, Khairul Alam, Banani Roy, Chanchal K. Roy
- canonical_url: https://arxiv.org/abs/2610.21144v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.SE)
- discovered_via: feed
- doi_or_arxiv_id: 2610.21144v1
- version: v1
- published_at: 2026-10-15
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: human oversight of AI-authored work, evidence requirements, T-04

## Claims from this source
- C-0075: A survey of 239 practitioners across 31 countries, using matched questions about human-authored (HPR) versus AI-authored (AIPR) pull requests, found reviewers apply a visibly different and stricter standard to AI-authored work: 64.9% reported lower initial trust in AIPRs; respondents relied less on author track record and subsystem familiarity and more on human-prompter expertise and bounded change size; 61.1% reported higher evidence requirements for AIPRs overall; the share who would block approval under residual uncertainty rose from 19.4% (HPR) to 43.9% (AIPR); unclear ownership more often paused AIPR review (29.3% vs 14.6%). Reviewers prioritized test inspection, project context, local execution, and partial reimplementation to verify non-trivial logic. The authors frame AIPR review as "an evidence-ownership problem, not merely a correctness check," and recommend tools expose provenance, distinguish generated claims from human-validated evidence, and make uncertainty visible before approval.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (practitioner survey, abstract read directly)
  - limitations: abstract only; self-reported survey data (stated intentions, not observed behavior); code-review specific, not agent-task approval in general, though the underlying human-factor (higher evidence bar for AI-authored work) plausibly generalizes.
  - relationship to existing claims: new, direct human-factor evidence for T-04 (consequence legibility is white space) — this is the first claim in this knowledge base with a real survey measuring how much more evidence humans actually want before approving AI-authored work, rather than inferring the need from design principles alone. Strengthens I-0006's premise (confirmations/approvals need more than a plausible-looking result) with a concrete persona-level number.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — "do confirmations show specific consequences," reframed here as "does the interface expose provenance and uncertainty before approval"), #11 (the reviewer surface). Directly relevant to any LayerLens flow where a human approves agent-proposed changes: provenance and uncertainty visibility, not just a pass/fail result, are what reviewers say they actually want.
