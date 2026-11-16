# MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory

- authors_or_org: David H. Yang, Blake Bullwinkel, Amanda Minnich, Mohammad Mohammadi Amiri, Giorgio Severi
- canonical_url: https://arxiv.org/abs/2611.09721
- discovered_url: inbox/arxiv/2026-W46.md (cs.AI)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.09721v1
- version: v1
- published_at: 2026-11-06
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: agent memory, poisoning, provenance, benchmark

## Claims from this source
- C-0136: LLM agents using memory systems for long-horizon, multi-session tasks have a critical attack surface: malicious instructions encountered in one session can be stored and propagated through memory before being retrieved and acted on in later sessions, with downstream effects varying significantly by memory architecture. MemoryDojo is a benchmark tracing the lifecycle of poisoned information through agent memory across 155 multi-session long-horizon trajectories spanning four domains and five different memory systems. All five tested memory systems are susceptible to memory poisoning, with substantial variation in downstream effects; a proposed memory-aware poison-optimization process increases poisoning efficacy and highlights architectural differences.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; specific memory systems/domains not named in the abstract; "substantial variation" not quantified numerically in what was read.
  - relationship to existing claims: a second, independent benchmark-scale corroboration for I-0013's memory-provenance pain point, alongside C-0123 (Role Grounding Attack) and C-0124 (ClawMMU) — broader in scope (a general poisoning benchmark across five memory systems, not one specific attack construction) and a good complement to Patronus's MEMTRACK (C-0107, memory *retrieval effectiveness*) since this is about memory *integrity*.

## LayerLens relevance
- open question(s) touched: #7 (human control), general (context and memory scope). Strengthens I-0013 and I-0011; relevant if LayerLens ever builds or evaluates cross-session agent memory.
