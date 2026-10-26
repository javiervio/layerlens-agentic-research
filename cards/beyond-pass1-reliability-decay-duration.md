# Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents

- authors_or_org: Khanal, Tao, Zhou (Northern Kentucky University) — author affiliation per WebSearch summary, not independently confirmed
- canonical_url: https://arxiv.org/abs/2603.29231
- discovered_url: found via WebSearch while pursuing this run's deliberate contradicting-evidence slice on T-01 (searching for evidence that run-to-run reliability concerns have been resolved)
- discovered_via: search
- doi_or_arxiv_id: 2603.29231
- version: v1 (per arxiv.org/html/2603.29231v1 seen in search results)
- published_at: date unknown (not stated in what was read; arXiv id prefix 2603 suggests March 2026)
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: incomplete access (arxiv.org EGRESS_BLOCKED per standing pattern; read only via WebSearch summary, not the primary text or inbox)
- sections_read: WebSearch summary only
- topics: reliability decay by task duration, T-01/I-0001

## Claims from this source
- C-0087: This paper constructs a 396-task benchmark across four task-duration buckets and three domains, and evaluates 10 open-source models across 23,392 episodes (k=3 repeats, two agent scaffolds). Its core claim is that reliability and capability diverge as task length grows: existing benchmarks are structurally blind to this divergence because they report only pass@1 on short, atomic tasks. The paper proposes a "Reliability Decay Curve" (RDC) characterizing how pass^k degrades as task duration increases, among other metrics.
  - locator: WebSearch summary (title, author/institution, task/episode counts, and the RDC concept were corroborated across multiple search result snippets; the paper's own abstract was not read verbatim)
  - evidence_label: incomplete access
  - limitations: WebSearch summary only, not the paper's own text; the specific wording "super-linear" decay (used in an earlier, broader search query) was not confirmed in the snippets retrieved and should not be attributed to this paper without a primary-source check; author affiliation unconfirmed beyond the search snippet.
  - relationship to existing claims: this run's deliberate ~20%-budget search for evidence that might contradict T-01 (reliability concerns have been resolved, or scores are now trustworthy) surfaced no counter-evidence — instead it surfaced this paper, a new, large-scale (23,392 episodes) independent family *reinforcing* T-01 from a specific new angle (reliability as an explicit function of task duration, not just of repeated sampling at one task length). Worth recording honestly: the contradicting-evidence search this run found only further corroboration, which is itself informative (no counter-signal turned up this run, strengthening confidence that T-01 is not merely an echo chamber of a few related papers).

## LayerLens relevance
- open question(s) touched: #5 (reliability vs one lucky pass — directly on point, and adds a dimension this knowledge base had not explicitly separated out before: reliability decay specifically as task duration increases, distinct from decay across repeated runs of the same task). Relevant to I-0001's hypothesis that LayerLens should recommend more runs (higher k) where variance is detected — this paper suggests task duration itself is a leading indicator of where that extra scrutiny is most needed, before any variance is even empirically observed.
