# Opik Security Incident: October 2026

- authors_or_org: Comet
- canonical_url: https://www.comet.com/site/blog/security-incident-october-2026/
- discovered_url: inbox/competitors/2026-W46.md (Comet/Opik feed, title + short excerpt), followed up via WebSearch
- discovered_via: feed, then search
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-10-27
- retrieved_at: 2026-11-16
- source_type: postmortem
- access_scope: incomplete access (WebSearch summary of Comet's own post; the post itself not independently WebFetched this run)
- sections_read: WebSearch summary of the first-party postmortem
- topics: real production credential incident, trust wall, vendor postmortem

## Claims from this source
- C-0152: Comet contained a security incident on October 26, 2026: between October 24-26, an unauthorized party used a comet.com user API key from an inactive, non-admin account to exploit a flaw in Opik's AI-provider settings, obtaining 29 API keys Comet uses internally for OpenAI and Anthropic. Per Comet's own statement, no customer or user account was accessed; only keys in Comet's own internal Opik test workspaces were exposed. Comet revoked the 29 keys, now requires re-entering an API key when a provider address changes, and added monitoring for provider-settings changes and unusual outbound traffic. Self-hosted/open-source Opik deployments were unaffected (the incident was limited to comet.com).
  - locator: WebSearch summary of Comet's first-party postmortem
  - evidence_label: incomplete access (vendor's own account, not independently corroborated by a second source)
  - limitations: only Comet's own statement was found; no independent security-researcher confirmation located this run.
  - relationship to existing claims: a third real, named, vendor-disclosed production credential/data incident in this knowledge base's eval/observability-vendor cluster (after Arize's indirect-prompt-injection leak, C-0126, and this run's C-0153, Braintrust's AWS breach) — continuing the pattern that trust-collapse (T-02) shows up in ordinary operational failures at exactly the companies building trust/evaluation products, not only in adversarial research.

## LayerLens relevance
- open question(s) touched: general (competitive — Comet/Opik is a tracked "team to watch" per SOURCES.md); T-02 (a provider-settings flaw letting a stored key be exfiltrated is directly relevant to how LayerLens's own keys-and-permissions system should be designed and audited).
