# From Observations to Authorized Actions: Measuring Source Information in Android Agents

- authors_or_org: Hyobin Ahn, Dongjae Lee
- canonical_url: https://arxiv.org/abs/2610.15502v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.OS)
- discovered_via: feed
- doi_or_arxiv_id: 2610.15502v1
- version: v1
- published_at: 2026-10-11
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: provenance tracking, authorization, mobile agents

## Claims from this source
- C-0081: Android agents read content from apps and web pages and act with the user's authority, yet cannot reliably tell *where* content came from. The WebView accessibility fields the authors inspected expose the host application but omit the document-level origins available inside the browser, so an agent reading through this interface cannot check which document supplied an object (confirmed by a limited reproduction on an unmodified WebView). Two prototypes were built and separately evaluated: an application-source monitor (withholds side-effecting calls whose signed source record contains an untrusted application) blocked every selected attack write in tested runs, but also withheld benign sends issued after reading untrusted content, flagged benign tasks using external content, and carried source records forward into a later, unrelated clean task. A WebView source-reference gate (checks object origins/reference lifetime via a modified browser) selected no disallowed object in a separate 24-trial evaluation, but is not an integrated defense (lacks authenticated browser delivery and atomic capture of selected bytes and origin).
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly; two separately evaluated prototypes)
  - limitations: abstract only; Android/WebView-specific, not a general OS or agent-framework finding; the application-source monitor's own false-positive pattern (withholding benign actions, carrying stale source records into unrelated tasks) is itself a usability cost the authors report candidly, not a solved problem.
  - relationship to existing claims: a new domain instance of a recurring theme — an agent acting with real authority cannot verify the provenance of the information it is acting on. Related to, but distinct from, I-0011/Concord (C-0064, staleness of an observation's *content*) and I-0009 (misleading *error* messages): this is about not knowing the *source* of an observation at authorization time, in a mobile/OS context rather than a tool-call or sandboxed-environment context.

## LayerLens relevance
- open question(s) touched: #2 (attribution — "where did this information come from" is itself an attribution question, here applied to authorization rather than post-hoc debugging), #7 (recovery/control). General relevance: a reminder that any LayerLens system type where an agent observes third-party-sourced content before acting (e.g. Gmail) could face an analogous "can the agent/environment itself verify where this content came from" question.
