# Braintrust confirms AWS cloud breach, issues emergency API key rotation alert to all customers

- authors_or_org: press coverage of Braintrust's own disclosure (TechCrunch, SecurityWeek, SecurityAffairs et al.)
- canonical_url: https://www.braintrust.dev (Braintrust's own notice; braintrust.dev EGRESS_BLOCKED again this run, consistent with every prior run) — press coverage: https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/
- discovered_url: WebSearch, following up a Comet-incident search that surfaced this as an adjacent, previously-untracked event
- discovered_via: search
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-05-04 (detected) / 2026-05-06 (customer notification)
- retrieved_at: 2026-11-16
- source_type: postmortem (via press coverage; Braintrust's own notice not independently fetched, domain blocked)
- access_scope: incomplete access (multiple consistent secondary press reports; Braintrust's own site unreachable)
- sections_read: WebSearch summary of multiple press accounts
- topics: real production credential incident, AI provider API keys, vendor postmortem

## Claims from this source
- C-0153: On 2026-05-04, Braintrust detected unauthorized access to one of its AWS cloud accounts containing customer API keys; it posted a website notice on 2026-05-05 and emailed customers requesting key rotation on 2026-05-06. Braintrust locked down the affected account, restricted access to related systems, and rotated internal credentials. Exposure was reportedly limited to AI-provider keys customers had stored in Braintrust; guidance was to rotate the AI-provider key, update Braintrust's stored key, revoke the old one, and monitor usage. One otherwise-uncorroborated secondary source claimed Stripe/Cloudflare/Notion keys were also exposed — flagged here as unverified, not repeated as fact.
  - locator: multiple consistent WebSearch press summaries (TechCrunch, SecurityWeek, SecurityAffairs, others); Braintrust's own first-party notice not independently read this run.
  - evidence_label: incomplete access (press coverage of a vendor disclosure, not the primary notice itself; the number of affected customers is explicitly undisclosed per the sources found)
  - limitations: no primary-source text read (braintrust.dev blocked, consistent with every run since 2026-09-29); this incident is from May 2026 — six months old, newly discovered by this knowledge base rather than new-this-week, flagged accordingly per AGENT_RUNBOOK's "distinguish a genuinely new publication from an old foundation you happened to discover this week."
  - relationship to existing claims: a significant, previously-untracked real incident at Braintrust specifically — the single most-cited "team to watch" in SOURCES.md, already carrying a documented credential-isolation story (Harbor, C-0010) about keeping API keys out of agent-reachable code. This incident is a different failure mode (Braintrust's own AWS account was compromised, an operational/infra breach, not an agent escaping a sandbox) but is directly relevant competitive context: the same company whose product pitch includes "the platform API key stays in the host process, out of reach of agent code" had its own cloud account breached, exposing the very category of credential (AI-provider keys) its own security story is about protecting.

## LayerLens relevance
- open question(s) touched: general (competitive — Braintrust); T-02 (trust-collapse — a vendor's operational security and its product's security story are two different things worth evaluating separately; useful caution for how LayerLens frames its own trust-wall claims externally — a design-time guarantee does not guarantee the company's own operational security).
