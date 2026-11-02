# Knowing Whom to Trust is not Enough: The Trust-Agreement Gap in Repeated Multi-Party LLM Negotiation

- authors_or_org: Amit Sarker, Moumita Choudhury, Saaduddin Mahmud, Shlomo Zilberstein
- canonical_url: https://arxiv.org/abs/2610.31971
- discovered_url: inbox/arxiv/LATEST.md (2026-W44, cs.MA)
- discovered_via: feed (arXiv harvester)
- doi_or_arxiv_id: arXiv:2610.31971v1
- version: v1
- published_at: 2026-10-22
- retrieved_at: 2026-11-02
- source_type: paper
- access_scope: abstract only (verbatim, via the arXiv inbox)
- sections_read: abstract
- topics: multi-agent trust modeling, negotiation, agreement vs. correctness

## Claims from this source
- C-0098: In a repeated, multi-party, multi-issue LLM negotiation framework (recurring agents, one participant covertly obstructing agreement), agents that explicitly maintain pairwise trust estimates across games can identify the adversary within a few games, but **accurate trust estimates do not consistently translate into better agreements** — a "trust-agreement gap." Explicit trust raised agreement rates by up to 23 percentage points, **but only when agents were explicitly guided to use that trust in their decisions** — forming an accurate trust estimate was not sufficient on its own.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract only)
  - limitations: abstract only; a constructed multi-agent negotiation testbed, not a real-world deployment; "up to 23 percentage points" is a best-case figure under explicit guidance, not an average effect.
  - relationship to existing claims: **a structurally distinct instance of T-02's "agreement is not verification" pattern** (alongside C-0016, Calibration Is Not Verification) — here the gap is not between consensus and correctness but between *knowing* who to trust and *acting* on it; also feeds nursery thesis N-04 (multi-agent systems evaluation) as a concrete mechanism-level finding about trust modeling specifically, distinct from MASCope's topology-based attribution (C-0067) or "Believed but Not Said"'s belief-collapse finding (C-0080).

## LayerLens relevance
- open question(s) touched: #13 (multi-agent scope — a concrete example of a trust/reputation mechanism multi-agent system evaluation would need to assess, if LayerLens ever extends to grading multi-agent collaboration).
- Lower direct product relevance than most of this run's findings (single-agent-against-environment remains LayerLens's current scope per open Q#13), but worth keeping in the N-04 nursery as a specific, well-defined mechanism (trust estimation that must be explicitly wired into decisions, not just computed) should the multi-agent-scope question ever be answered "yes."
