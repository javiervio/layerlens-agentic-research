# Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation

- authors_or_org: Osamudiamen Edogun, Joshua Obigwe, Irfan Mehmood
- canonical_url: https://arxiv.org/abs/2611.09807
- discovered_url: inbox/arxiv/2026-W46.md (cs.CL)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.09807v1
- version: v1
- published_at: 2026-11-06
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: context engineering, compaction, memory, RAG comparison

## Claims from this source
- C-0142: Comparing compaction (compress each turn into atomic facts and search those) against retrieval-augmented generation (keep the transcript, search it) on LoCoMo, with both arms answering all 1,985 questions against the same stores, same generator/judge, paired on one row to license McNemar's exact test on the 512 disagreeing questions: on the four categories comparable prior work reports, compaction scores 71.4% vs. 64.6% (6.8-point lead, p=5.5e-08) at 34% fewer prompt tokens. Including a fifth, adversarial category that comparable work drops, the lead falls to 2.0 points and loses significance, because the RAG baseline leads on the adversarial set by 14.6 points. The lead has structure: it shrinks as the reference answer demands more exact source wording (9.6 points ahead at 1-2 reference words, 3.1 points behind past eight), tracking token overlap rather than judge behavior — "compaction keeps what a fact asserts and discards how it was said," winning where the answer is a value and losing where it is a phrasing.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly, with stated statistical tests)
  - limitations: abstract only; one benchmark (LoCoMo); four negative results reported with power calculations but not detailed in the abstract.
  - relationship to existing claims: directly extends C-0004 (Anthropic's context-engineering guidance naming compaction and structured note-taking as techniques) with a controlled, statistically rigorous comparison and a genuine nuance: compaction is not a strict upgrade over RAG, it trades phrasing-fidelity and adversarial robustness for token efficiency and value-recall. Also complements C-0149 (Anthropic's own "components of agent memory" post, this run) on what compaction/structured memory can and cannot preserve.

## LayerLens relevance
- open question(s) touched: general (context and memory scope, 15% of budget per PROTOCOL.md). Background/context for any future LayerLens memory or context-management design, not yet tied to a specific open question.
