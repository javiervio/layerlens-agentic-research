# Rasoi: Visual Diffs for Evaluating Structural Changes Made by Coding Agents

- authors_or_org: Riya Sahni, Aryan Kaul, Anushka Bhatnagar, Xuanming Zhang, Vivian Liu, Reya Vir et al.
- canonical_url: https://arxiv.org/abs/2611.16293v1
- discovered_url: inbox/arxiv/LATEST.md (cs.HC, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.16293v1
- version: v1
- published_at: 2026-11-12
- retrieved_at: 2026-11-23
- source_type: paper
- access_scope: abstract only (verbatim, read directly from the arXiv inbox)
- sections_read: abstract
- topics: human-agent interaction, oversight UX, visual diffs, trust

## Claims from this source
- C-0177: As coding agents take on larger changes, developers can lose track of how a codebase is evolving even when edits look correct on the surface (duplicated logic, out-of-scope module changes, removed functionality, architectural drift). Rasoi, a design probe, maps how a codebase's architecture evolves after each agent-made edit, letting developers inspect which architectural elements and relationships were added, modified, or removed across levels of abstraction. In a week-long study with 12 developers on their own codebases across varied domains, visual diffs helped developers see whether changes stayed in scope, notice unexpected restructuring, and relate modified parts to the whole system. The authors' finding: the value of this kind of oversight tool "lies less in making developers trust the agent and more in helping developers feel confident [...] in [their] ability to act" (abstract truncated at this point).
  - locator: abstract
  - evidence_label: bounded empirical (a qualitative field study, 12 developers, one week)
  - limitations: abstract only; small N, qualitative study design; "feel confident enough to act" is the authors' own framing, not an independently validated metric.
  - relationship to existing claims: directly relevant to T-04's open question of what oversight tooling should actually show — this is a rare real-world (not a benchmark) human-factor finding, and its reframing from "trust" to "confidence to act" is a useful distinction for how LayerLens should frame its own attribution/comparison surfaces: the goal may not be making a user trust the agent, but making them confident they can correctly judge and intervene.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — architecture-level diffs across abstraction levels are a structural-change analogue to LayerLens's own trace/trajectory diff ambitions), #9 (comparison as the signature surface — directly relevant to the v3 "unified DAG diff" direction)
- general: the "confidence to act, not trust" framing is worth citing when designing LayerLens's own comparison/attribution UI copy and success metrics.
