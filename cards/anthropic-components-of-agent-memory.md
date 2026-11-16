# The components of agent memory

- authors_or_org: Anthropic
- canonical_url: https://www.anthropic.com/research/components-of-agent-memory
- discovered_url: inbox/reference/2026-W46.md (Anthropic sitemap)
- discovered_via: feed
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-11-06
- retrieved_at: 2026-11-16
- source_type: post
- access_scope: full text (WebFetch; anthropic.com reliably reachable per SOURCES.md)
- sections_read: full post
- topics: agent memory, staleness, provenance, authority, context engineering

## Claims from this source
- C-0149: Anthropic describes a four-layer memory hierarchy (transcripts; memory notes Claude writes during a session; memory representations built offline, e.g. wikis; injected context loaded at session start) plus "dreaming," an offline process reflecting on transcripts to correct mistakes, build notes/representations, and decide what to preload — explicitly separated from weight changes, in-context learning, and compaction. Anthropic states plainly that a memory note "that's wrong from the start or that drifts as the environment changes can be read, and trusted, by Claude in a later session" (in a Pokémon-playing case study, an incorrect note led Claude to declare a dungeon "DONE" and walk backward off a ledge) — a first-party admission of exactly the staleness/provenance risk I-0011/I-0013 track. Concrete findings: judging what is salient beats exhaustive logging (Sonnet 3.7 wrote 413 memory files and earned one badge; Fable 5 wrote ~10 files and earned four, storing strategy/tested rules the screen couldn't show); describing memory's *purpose* rather than a fixed procedure works better (fixed rules like "record only failures" hurt stronger models); weaker models need more steering (prompting Sonnet 4.6 to read and test memory nearly doubled its score, 0.330->0.641, while Sonnet 5 reads memory unprompted 9/10 times); dreaming that checks notes against transcripts repairs errors (using transcripts as ground truth, Claude re-entered a cave and reached its goal after a note was corrected); wiki-building scales incrementally (performance on 25 questions grew from 13% to 48% over 128 sessions; wiki+search reached 61% vs. 53% for search alone); and goal-specific memory beats shared tables for fact retention (one page per contract, quoting terms verbatim, kept all 57 facts vs. 41/57 surviving in a shared table). Stated limitations: dreaming requires compute and continuous checking may be impractical; writing notes in-session draws attention from the main task, while dreaming's output may not be immediately accessible; wikis aren't always better (no gain on one task; 1.77x the corpus size while "abstracting nothing" on another); results are limited (one run per model in the Pokémon case study); "no model can really know what will happen in future turns."
  - locator: full post (WebFetch summary, key figures and quotes preserved)
  - evidence_label: documented capability / bounded empirical (first-party, directly read; some findings from single-run case studies the authors themselves flag as limited evidence)
  - limitations: several headline numbers (413 vs. ~10 files, the 0.330->0.641 jump, the 13%->48% wiki curve) come from single-run case studies per Anthropic's own caveat, not controlled multi-seed experiments.
  - relationship to existing claims: a first-party, frontier-lab corroboration of I-0011 (stale observations) and I-0013 (memory provenance/authority) — Anthropic's own words ("a note that's wrong... can be read, and trusted, by Claude in a later session") describe precisely the risk the Role Grounding Attack (C-0123) and Concord (C-0064) independently studied adversarially and architecturally; this is the first time this knowledge base has a vendor's own plain admission of the failure mode, not just an attack/benchmark paper. Also directly extends C-0004/C-0142 (compaction vs. RAG-style memory) with a fourth memory-architecture family.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery — memory staleness/drift as a source of error a user needs to inspect and correct), general (context and memory scope). Strengthens I-0011 and I-0013 with a first-party admission from the frontier lab most associated with agent-harness design; useful, highly citable language for explaining the staleness/provenance risk to a non-technical stakeholder.
