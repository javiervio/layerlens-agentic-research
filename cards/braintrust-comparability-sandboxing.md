# Braintrust — experiment comparison and sandboxed agent evals (Harbor)

- authors_or_org: Braintrust
- canonical_url: https://www.braintrust.dev/foundations/comparing-experiments ; https://www.braintrust.dev/blog/harbor-agent-evals ; https://www.braintrust.dev/docs/platform/experiments
- discovered_url: WebSearch "Braintrust eval experiment comparison sandboxed evals docs"
- discovered_via: search (Braintrust is a named "team to watch" in our own SOURCES.md; this run's rotation priority per the 2026-09-25 run log)
- doi_or_arxiv_id: n/a
- version: n/a (live product docs, no version stated)
- published_at: n/a (docs pages, undated)
- retrieved_at: 2026-09-28
- source_type: docs
- access_scope: abstract only, second-hand — www.braintrust.dev was EGRESS_BLOCKED this run (consistent with the 2026-09-25 run, which only reached a GitHub org listing for this vendor). Everything below is WebSearch's generated summary of the docs pages, not text opened directly.
- sections_read: none directly. Flagged **incomplete access (search summary only)**.
- topics: comparability, experiment comparison, sandboxed evals, trust boundary between eval platform and agent code

## Claims from this source

- C-0010: Braintrust's "Experiments" are described as immutable, comparable snapshots of an eval run; the comparison view reportedly shows two experiments side by side with score breakdowns, regression detection, and output diffs "at the test case level." Separately, Braintrust's "Harbor" integration for sandboxed agent evals is described as keeping the Braintrust API key "in the host process" so that "the plugin never passes it into the task container," meaning "agent code running in the sandbox cannot read it."
  - locator: none — search-summary only.
  - evidence_label: incomplete access
  - limitations: no primary text opened; cannot confirm whether the "output diff" is a full trajectory/step-level diff or only a final-output diff (this distinction matters directly for LayerLens open question #9); cannot confirm the Harbor sandboxing claim's actual isolation guarantees (e.g., whether it's enforced by the platform or only a convention of the plugin's design) beyond the one sentence surfaced by search.
  - relationship to existing claims: new. The Harbor sandboxing description is thematically close to LayerLens's own "trust wall" (seed/knobs never served to an agent-facing key) — both are a keep-the-answer/secret-out-of-the-agent-process design — but this is a different mechanism (an API key vs. a seed/knobs) protecting a different thing (platform credentials vs. grading determinism), so treat as an adjacent pattern, not the same claim, until a direct read confirms the actual scope of Harbor's isolation.

## LayerLens relevance

- **Open question #1 (Comparability)** and **#9 (Comparison as the signature surface)**: if Braintrust's comparison view really does show "output diffs at the test case level" but not a trajectory/step-level diff, that would be a concrete, nameable difference LayerLens's proposed "unified DAG diff for comparing trajectories" (v3 direction) could point to — but this needs a direct read to confirm before using it as a comparison claim, per PROTOCOL.md's rule that "different" must name a difference in actual behavior.
- The Harbor/trust-boundary pattern is worth tracking alongside BenchJack's V1/V2 vulnerability classes (card: hackdetect / benchjack) — another vendor independently arriving at "the agent must not be able to read the thing that grades it," which is soft corroboration that this is a real, recognized problem in the field rather than a LayerLens-specific design choice.
- Action for next run: retry www.braintrust.dev directly (docs, foundations, and blog subpaths); if still blocked a third run in a row, this vendor may need a saved/authorized link from Javier per PROTOCOL.md, since search-summary-only has now been the outcome twice.
