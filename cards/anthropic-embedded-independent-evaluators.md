# Anthropic's embedded/independent-evaluator program: an update on independent evaluators, and partnering with Accenture on embedded evaluation

- authors_or_org: Anthropic
- canonical_url: https://www.anthropic.com/news/an-update-on-independent-evaluators ; https://www.anthropic.com/news/accenture-embedded-evaluation
- discovered_url: inbox/reference/LATEST.md (Anthropic sitemap, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-10-15 (independent evaluators update); 2026-11-13 listing in Anthropic's sitemap for the Accenture post (content references an October 2026 commitment; exact original publish date of the Accenture post not separately confirmed)
- retrieved_at: 2026-11-23
- source_type: post
- access_scope: full text, read directly (WebFetch; anthropic.com reliably reachable per SOURCES.md)
- sections_read: full text of both posts
- topics: third-party verification, attestation, governance, reviewer trust

## Claims from this source
- C-0173: Anthropic has begun giving a team from METR (an independent AI-model-risk-assessment nonprofit) employee-like access — hardware, office space, and internal tools roughly on par with Anthropic's own risk-assessment teams — with METR free to publish its own risk-level analysis; Anthropic cannot veto publication but can require redaction of predefined categories (customer data, privileged material, model architecture information), which METR may note the extent of. Anthropic describes a three-tier model for independent evaluator access (narrowly-scoped with approval-gated publication; broader access with publish-without-approval; the METR "employee-like" tier) and states "every frontier AI company should do the same." Separately, Anthropic and Accenture (via Accenture's Faculty unit) are building an "embedded evaluator" partnership — evaluators working inside the AI company with access comparable to an employee's, observing training, following build/deploy decisions, and reporting incidents — with Anthropic and Accenture each expecting to invest at least $1 billion over five years. Anthropic states plainly: "There are, as yet, no standards for what information embedded evaluators should have access to," and that its own approach is expected to evolve.
  - locator: full post text (both URLs)
  - evidence_label: documented capability (first-party, directly read)
  - limitations: this is AI-safety/governance-level third-party audit of the company, not a product-level mechanism for an agent-evaluation customer's own reviewer to check a specific claim; the access/publication model is new and explicitly described as having no established standards yet.
  - relationship to existing claims: a significant, frontier-lab-scale real-world instance of the broader pattern I-0014 tracks (a reviewer accepting a claim without trusting the claimant) — here the "claimant" is the AI company itself and the "reviewer" is an embedded third party, a different altitude from I-0014's product-level attestation surface but the same underlying principle: access to evidence, not a badge, is what earns trust. Also relevant to T-02 (trust collapse making verifiable, independently-checkable claims a purchasable/demanded property) at an industry-wide, governance level.

## LayerLens relevance
- open question(s) touched: #11 (the reviewer surface — a real, concrete, three-tier framework for "how much access and publication freedom does an independent verifier need" is a useful outside reference point, even though it operates at a different scale than a LayerLens reviewer checking one evaluation's evidence chain)
- general: worth citing as evidence that "independent, verifiable evaluation" is becoming an expected, invested-in industry practice (frontier labs, not just eval-tooling vendors) — relevant context for LayerLens's own "independent, trustworthy" positioning conversation (see also the Vals AI competitive.md entry).
