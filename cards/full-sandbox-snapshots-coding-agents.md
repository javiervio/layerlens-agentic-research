# Returning to Development States: When Full Sandbox Snapshots Help Coding Agents

- authors_or_org: Daniel Thi Graviet, Tanmay Shah
- canonical_url: https://arxiv.org/abs/2610.13841
- discovered_url: inbox/arxiv/LATEST.md (2026-W42 harvest)
- discovered_via: feed
- doi_or_arxiv_id: 2610.13841v1
- version: v1
- published_at: 2026-10-09
- retrieved_at: 2026-10-19
- source_type: paper
- access_scope: abstract (verbatim, directly read via arXiv harvester inbox)
- sections_read: abstract only
- topics: environment lifecycle, checkpoint/restore, sandbox snapshots

## Claims from this source
- C-0060: Implementing Go-Explore-style search over full Daytona sandbox snapshots for coding agents, higher and more efficient solve rates depend mainly on progress that sits outside the repository itself — databases, services, and other runtime state, not just a git diff. Full-snapshot search is most effective specifically when long-horizon coding work spans multiple services whose state cannot be reconstructed from a single diff.
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; "Daytona snapshots" specifically (a named commercial vendor), not a general claim across sandbox providers; no quantitative solve-rate numbers given in the abstract
  - relationship to existing claims: a thirteenth independent family for T-06, and a direct, concrete argument for exactly the split T-06 already draws between "local sandbox state" (diffable, git-capturable) and the harder "remote/external state" (databases, services) branch — this paper is evidence that even within a single sandbox, the valuable state to preserve is disproportionately the non-repo, service-like state, which is architecturally closer to LayerLens's own system-type shape (Salesforce, Stripe, SEC EDGAR, etc. all being "a service with state," not a git repo).

## LayerLens relevance
- open question(s) touched: #3 (deterministic replayability), #7 (recovery — "full-snapshot search" as an alternative to the narrower, diff-based recovery most agent harnesses default to)
