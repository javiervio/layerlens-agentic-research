# Report: Progressive Disclosure of Agent Skills

- authors_or_org: Guilin Zhang, Kai Zhao, Priyanka Mudgal, Waleed Ammar, Xiquan Cui, Xu Chu et al. (Workday)
- canonical_url: https://arxiv.org/abs/2609.35692
- discovered_url: inbox/arxiv/LATEST.md (2026-W40 harvest, cs.AI)
- discovered_via: feed (arXiv inbox harvester)
- doi_or_arxiv_id: arXiv:2609.35692
- version: v1
- published_at: 2026-09-28
- retrieved_at: 2026-09-29
- source_type: paper (practitioner report)
- access_scope: abstract only, read directly and verbatim via the arXiv inbox harvester
- sections_read: abstract
- topics: agent skills/context management, production practitioner report, tool/skill libraries

## Claims from this source
- C-0031: A production practitioner report from Workday: as their deployed LLM agents' skills libraries (named procedures defined in-context) grow, so does operational cost. Progressive disclosure (lazy-loading skills only as needed, rather than always including the full library in context) empirically improves skill-retrieval quality, and only marginally degrades overall latency.
  - locator: abstract, verbatim.
  - evidence_label: bounded empirical (abstract read directly; first-party production report from a named, real company, not a lab benchmark).
  - limitations: abstract only; no specific numbers (retrieval-quality delta, latency delta) given in what was read; single company, single deployment context; "marginally degrades" is qualitative, not quantified in the abstract.
  - relationship to existing claims: new — first claim specifically on production skill-library scaling and lazy-loading as a practitioner pattern. Adjacent to, but distinct from, C-0004 (Anthropic's context-engineering guidance, which recommends just-in-time retrieval in general terms) — this is a concrete, measured production instance of the same principle.

## LayerLens relevance
- open question(s) touched: general ("context and tools" scope slice, 15% of effort split); loosely touches #6 (synthetic-data/tool legibility) in that a growing tool/system surface needs efficient exposure to an agent, similar to how LayerLens's own system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail) each carry their own tool surface.
- Not tied to an existing idea/feature row this run — recorded as background/context claim, not forced into a new idea, per dedup discipline (a single production report on skill-library lazy-loading doesn't yet map to a LayerLens-specific pain point beyond general awareness).
