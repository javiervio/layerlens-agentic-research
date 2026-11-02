# ARE: Scaling Up Agent Environments and Evaluations

- authors_or_org: Romain Froger, Pierre Andrews, Matteo Bettini, et al. (Meta FAIR / Meta Agents Research)
- canonical_url: https://arxiv.org/abs/2509.17158
- discovered_url: inbox/discovery/LATEST.md (openalex, 2026-W44) then inbox/fulltext/
- discovered_via: feed (discovery harvester)
- doi_or_arxiv_id: arXiv:2509.17158 (v1 2025-09-21, v2 2025-12-10)
- version: v2
- published_at: 2025-09-21 (v1); 2025-12-10 (v2, this read)
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only — the inbox/fulltext/ file for this paper contains only the arXiv abstract landing page (scraped as plain text), not the paper's actual body; see note below.
- sections_read: abstract (verbatim), title, author list, submission history
- topics: environment construction, agent evaluation, asynchronous evaluation, benchmark design

## Note on this run's "full text" harvest
This paper was one of 6 the fulltext_fetch.py harvester pulled into `inbox/fulltext/` this run, labeled "full text via ar5iv/web." On inspection, all 6 files actually contain only the standard arXiv abstract landing page (title, authors, abstract, submission metadata) — not the ar5iv-rendered paper body. This is an infra finding, not a content problem: the fetcher's ar5iv/web fallback appears to be returning the abs page rather than the full HTML body. Flagged in `SOURCES.md` and the run log for Javier; this card and its sibling cards from the same harvest are accordingly labeled "abstract only," same confidence tier as a standard arXiv-inbox abstract read.

## Claims from this source
- C-0088: Meta's ARE platform builds environments with "their own rules, tools, content, and verifiers" and Gaia2 (built in ARE) runs **asynchronously**, which "surfac[es] new failure modes that are invisible in static settings"; across evaluated systems, "no system dominates across the intelligence spectrum," stronger reasoning trades off against efficiency, and budget-scaling curves plateau.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only; a major-lab systems paper, not independently verified beyond the abstract)
  - limitations: abstract only; no benchmark tables, no Gaia2 task count or concrete numbers seen; "no system dominates" and "plateau" are qualitative characterizations from the authors, not quantified here.
  - relationship to existing claims: new — first entry from Meta FAIR specifically; adjacent to C-0009 (HAL's cost-accuracy Pareto framing) via the "budget scaling curves plateau" point, and to T-01 (capability-vs-reliability/efficiency tradeoff).

## LayerLens relevance
- open question(s) touched: general (environment design philosophy — "each with their own rules, tools, content, and verifiers" mirrors LayerLens's own per-environment grader/trust-wall design); #8 (the living-graph/environment-design bet, as an external precedent for ambitious environment-construction abstractions, though ARE's own UI/UX is not described here); #1 (comparability — "no system dominates," echoes HAL's Pareto argument).
- Meta AI has no blog feed/sitemap per SOURCES.md ("NO FEED OR SITEMAP FOUND"); this is the first individual read of a Meta environments/evaluation research artifact in this knowledge base — see new competitive.md entry.
