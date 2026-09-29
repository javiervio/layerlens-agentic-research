# Trajectory-Level Security Debt in LLM Coding Agents

- authors_or_org: Prateek Kumar Rajput, Abdoul Kader Kabore, Yewei Song, Melissa Tessa, Tailia Malloy, Jacques Klein et al.
- canonical_url: https://arxiv.org/abs/2609.35199
- discovered_url: inbox/arxiv/LATEST.md (2026-W40 harvest, cs.SE)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2609.35199
- version: v1
- published_at: 2026-09-28
- retrieved_at: 2026-09-29
- source_type: paper
- access_scope: abstract only, read directly and verbatim via the arXiv inbox harvester (primary text, not a search summary; arxiv.org itself was not fetched and is blocked this run)
- sections_read: abstract
- topics: agent evaluation, trajectory-level assessment, security, SAST tooling

## Claims from this source
- C-0029: Proposes the Security Debt Line Integral (SDLI), a metric that accumulates static-analysis security risk over an agent's intermediate code states each time it reaches a new best test-pass ratio, rather than scoring only the final submitted artifact. Instantiated with four SAST tools across 830 passing SWE-bench runs, 712 ProgramBench final workspaces, and 13 public MirrorCode trajectories. Two-tool CWE-class agreement (i.e., two different security scanners agreeing on a vulnerability class) occurred in only 3.9% of SWE-bench runs and 26.2% of the higher-passing ProgramBench subset (dropping to 6.2% after excluding three advisory-heavy CWE classes) — the authors are explicit these are scanner findings, not confirmed exploitable vulnerabilities. A repair case study reduced the scanner signal while preserving tested behavior, but also showed sensitivity to equivalent API rewrites (i.e., a semantically identical rewrite can flip the scanner's verdict).
  - locator: abstract, verbatim.
  - evidence_label: bounded empirical (abstract read directly).
  - limitations: abstract only; low two-tool agreement (3.9-26.2%) suggests SAST-tool disagreement is itself a major confound, so the underlying "true" security-debt rate is not established, only that trajectory-level security tracking surfaces something final-artifact-only evaluation misses; authors themselves note SDLI's value for steering agents or confirming exploitable vulnerabilities "remains to be established."
  - relationship to existing claims: new — first claim specifically on security posture tracked across a trajectory rather than at the final artifact only. Complements T-03 (failure attribution) and I-0003 with a different dimension (security debt, not correctness) but shares the same underlying principle: intermediate states carry information the final state alone hides.

## LayerLens relevance
- open question(s) touched: #9 (comparison as the signature surface — a trajectory-level metric is exactly the kind of thing a trajectory diff view could expose), #2 (attribution, in the general sense that "passed but accumulated risk along the way" is a distinct outcome from a clean pass).
- General relevance: LayerLens's actions/state graders already look at what changed, not just the final answer; this paper is external validation that trajectory-level assessment (beyond pass/fail) is an active, if immature, research direction. Not tied to an existing idea/feature row this run — recorded as a claim and open-question note rather than forced into a new idea, per dedup discipline.
