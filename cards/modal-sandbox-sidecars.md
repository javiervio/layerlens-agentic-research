# Modal Sandbox Sidecars — a trust-boundary pattern for agent sandboxes

- authors_or_org: Modal
- canonical_url: https://modal.com/blog/introducing-sandbox-sidecars-trust-boundary (not independently opened; modal.com is EGRESS_BLOCKED in this sandbox, consistent with prior runs)
- discovered_url: inbox/competitors/LATEST.md (2026-W41 harvest, Modal sitemap) title, then WebSearch for content
- discovered_via: feed (competitor inbox harvester, title only) then search
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-10-01 (per inbox sitemap listing); public alpha per Modal's own changelog (date not independently confirmed)
- retrieved_at: 2026-10-12
- source_type: post (vendor feature launch, read via secondary summaries; Modal's own blog/changelog/docs pages referenced but not independently opened)
- access_scope: incomplete access (several consistent secondary summaries, including one quoting Modal's own docs example; modal.com itself blocked to direct fetch)
- sections_read: n/a (secondary summaries only)
- topics: trust boundary, sandbox lifecycle, credential isolation

## Claims from this source
- C-0054: Modal's Sandbox Sidecars run a second, isolated container alongside an agent's main Sandbox on the same host, intended to separate trusted from untrusted code (e.g. running the agent itself in the sidecar while agent-generated code executes in the main Sandbox), communicating over what Modal claims is a low-latency private bridge "3x faster" than using two separate Sandboxes. Modal positions this as the recommended way to keep secrets out of agent-generated code (secrets injection via the sidecar, not the main sandbox). Feature is in public alpha as of this run.
  - locator: secondary summaries (one quoting Modal's own documented example directly); no primary page opened
  - evidence_label: incomplete access (vendor's own claimed numbers relayed via search, not independently verified — per PROTOCOL.md rule 4, a vendor announcement is not proof)
  - limitations: no primary source; the "3x faster" and isolation-guarantee claims are vendor-stated, not independently benchmarked by any source found; feature is alpha, mechanics may change.
  - relationship to existing claims: a new, concrete commercial data point for the trust-wall conversation (T-02) and T-06 (environment lifecycle) — the credential-isolation pattern (keep secrets in a process/container the agent cannot read, let agent-generated code run elsewhere) is the same shape as Braintrust's Harbor pattern (C-0010, "platform API key in the host process") and LayerLens's own trust wall (seed/knobs never served to an agent-facing key), now from a third infrastructure vendor, reinforcing that this is a converging industry pattern rather than one company's idea.

## LayerLens relevance
- open question(s) touched: #3 (replayability/isolation, general trust-wall positioning). Folds into the existing Modal competitive.md entry (upgrading "rotation coverage only, nothing first-party read" toward a specific, comparable mechanic) and into T-02's trust-wall discussion as a third convergent example of the "keep secrets in a boundary the agent cannot touch" pattern (after LayerLens's own trust wall and Braintrust's Harbor).
