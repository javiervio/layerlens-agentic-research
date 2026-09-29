# Build an Agent Workbench on OpenAI's Agents API (E2B blog)

- authors_or_org: E2B
- canonical_url: https://e2b.dev/resources/build-an-agent-workbench-on-openais-agents-api
- discovered_url: inbox/competitors/LATEST.md (GitHub Actions RSS harvester, E2B feed https://e2b.dev/rss.xml)
- discovered_via: feed (via inbox harvester)
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-09-10
- retrieved_at: 2026-09-29
- source_type: post
- access_scope: RSS description only (one sentence); the full post was NOT read (e2b.dev EGRESS_BLOCKED to WebFetch this run, confirmed again)
- sections_read: RSS feed summary sentence only
- topics: sandbox infrastructure, environment lifecycle, checkpoint/pause/fork

## Claims from this source
- C-0028: E2B's own blog (first-party feed, not a third-party aggregator) describes a workbench built on OpenAI's Agents API (beta) and E2B sandboxes featuring an "application-managed lifecycle, one sandbox per chat, pause and fork" — i.e., E2B sandboxes support pause and fork as first-class lifecycle primitives, at least in this reference workbench pattern.
  - locator: RSS feed item description, verbatim: "A workbench built on OpenAI's Agents API (beta) and E2B sandboxes: application-managed lifecycle, one sandbox per chat, pause and fork."
  - evidence_label: documented capability (first-party source) but at abstract/summary-only access scope — this is a one-sentence RSS description, not the full post, so treat the *existence* of pause/fork as confirmed first-party, but not the underlying mechanics, guarantees, or limitations.
  - limitations: only a one-sentence feed summary; the full post (with actual implementation detail) was not reachable this run; resolves, in direction only, the prior competitive.md note that E2B's session-lifecycle claims were "third-party blog only, unconfirmed" — this is now first-party for pause/fork specifically, though still thin.
  - relationship to existing claims: fifth data point for thesis T-06 (environment-lifecycle/checkpoint-rollback-fork convergence), and the first one from an already-commercial, productized sandbox vendor rather than a research paper — i.e., the pattern is not just academic, it is already shipping in industry infrastructure.

## LayerLens relevance
- open question(s) touched: #7 (human control and recovery), #3 (deterministic replayability).
- Updates the E2B entry in `knowledge/competitive.md` from "insufficient evidence, do nothing" to a thin but first-party confirmed capability.
