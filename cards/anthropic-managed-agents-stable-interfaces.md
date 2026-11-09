# Scaling Managed Agents with stable interfaces

- authors_or_org: Anthropic
- canonical_url: https://www.anthropic.com/research/managed-agents
- discovered_url: inbox/reference/2026-W45.md (Anthropic sitemap harvest)
- discovered_via: feed
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-10-30
- retrieved_at: 2026-11-09
- source_type: post
- access_scope: full text (fetched directly; anthropic.com remains reliably reachable from this sandbox)
- sections_read: full post
- topics: harness as infrastructure, comparability, agent runtime architecture

## Claims from this source
- C-0125: Anthropic's Managed Agents service virtualizes three components of a long-horizon hosted agent — Session (an append-only log of everything that happened), Harness (the loop calling Claude and routing tool calls), and Sandbox (the execution environment) — behind small, stable interfaces (e.g. `execute(name, input) -> string`, `wake(sessionId)`, `getSession(id)`, `emitEvent`, `getEvents`) designed, explicitly by analogy to an OS kernel's process/file abstractions, to "outlast any particular implementation." The stated motivation: "harnesses encode assumptions about what Claude can't do," and those assumptions "can go stale as models improve" — their concrete example is that context-reset logic added for Sonnet 4.5's "context anxiety" became "dead weight" on Opus 4.5. Decoupling the brain (model calls) from the hands (sandboxed execution) is reported to cut p50 time-to-first-token roughly 60% and p95 over 90% (no baseline values or methodology given). The post does not describe a versioning scheme, deprecation policy, compatibility guarantee across model/harness updates, reproducibility guidance, or how a user would be told something changed.
  - locator: full post (direct read)
  - evidence_label: documented capability (first-party architecture description from the vendor itself) for the architecture and the stated harness-staleness motivation; the latency numbers are a vendor-reported claim without methodology, so treat as anecdotal signal, not bounded empirical.
  - limitations: a single vendor's own post, not independently verified; no baseline/methodology for the latency numbers; explicitly silent on versioning, reproducibility, and comparability — this silence is itself notable (see relationship below) but is an absence, not a claim.
  - relationship to existing claims: a first-party, frontier-lab-scale corroboration of T-01's "harness is a first-class artifact that goes stale" argument, with the clearest concrete illustration yet of *why* (a model-specific workaround becoming dead weight on the next model) — complements C-0044/C-0093/C-0115's confound-detection framing with a builder's own stated reason harnesses need re-engineering over time. Notably, even this meta-harness abstraction does not address open question #1 (comparability) or #5 (what "repeat a run" means) — Anthropic's own newest agent infrastructure post is silent on versioning/reproducibility, consistent with this remaining genuine, unclaimed white space industry-wide, not just for LayerLens.

## LayerLens relevance
- open question(s) touched: #1 (comparability — notably unaddressed even here), #5 (repeat-a-run — likewise unaddressed)
