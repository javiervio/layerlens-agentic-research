# Soei: Structured Observability of Evidence and Intent for Multi-Agent AI Software Engineering

- authors_or_org: Mohammed Nayeem Khan, K S Sarun Kumar
- canonical_url: https://arxiv.org/abs/2610.39468v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.MA harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.39468v1
- version: v1
- published_at: 2026-10-29
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: attribution, trust wall, real production evidence, provenance/attestation

## Claims from this source
- C-0116: Studying 45 real coding-agent sessions (102,233 records, 20,577 tool executions, 2,336 human-to-agent episodes), the authors verify an existing open-source observability tool (Agenttrail) against its own source and find nine documented mechanisms hold at file-and-line level but two event pipelines are never unified and its Map service has an unauthenticated local mutation surface. With a blind-audited classifier (83.3%/96.7% precision), they estimate 23.4% (95% CI 17.1-35.7) of code-editing episodes end with no independent check after the last edit, and 57.8% of to-dos marked complete after editing had no proof in between; 42% of sessions ran over 24 hours, 48.1% of transcript bytes exceeded a 2 MiB replay bound, and 1,326 records in 16 sessions contained credential-like strings. Their proposed system, Soei, is an acknowledgement-aware event schema plus a hash-chained local ledger (20% of raw size, holds no content/credentials, verifies ~126k events/s, detects tampering and replays deterministically) and a W3C PROV-aligned graph with a verification layer that keeps a completion claim separate from proof.
  - locator: abstract (verbatim)
  - evidence_label: bounded empirical (real production trace data, 45 sessions, with a validated classifier and an open-source tool verified against its own source)
  - limitations: abstract only; 45 sessions is a modest real-world sample, one organization's usage pattern; classifier precision (not perfect) introduces some estimation uncertainty on the headline percentages.
  - relationship to existing claims: a real-production instance of C-0022's core pattern (agent claims completion, verdict should not trust the claim) at genuinely large scale (102K+ records) — "57.8% of to-dos marked complete had no proof in between" is a concrete number for exactly why LayerLens's "claims stored beside verdicts, never used as evidence" design matters. Also a direct, concrete example of the credential-in-transcript risk this knowledge base has tracked since the trust-wall cluster began (1,326 credential-like strings found in 16 of 45 sessions).

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — "what was actually done, by whom, whether it is finished" is exactly the attribution question), #11 (reviewer surface — a verification layer separating claim from proof, tamper detection, deterministic replay)
