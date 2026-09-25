# The Judge in the Mirror: self-preference bias in LLM-as-judge, without self-recognition

- authors_or_org: Han Kim, IOV Labs (아이오브연구소)
- canonical_url: https://github.com/hankimis/self-preference
- discovered_url: WebSearch "self-preference bias LLM judge github repository benchmark code"
- discovered_via: search
- doi_or_arxiv_id: none found (independent GitHub research note, not an arXiv submission)
- version: n/a (repo README as of retrieval date)
- published_at: date unknown (no explicit date in README; repo appears current as of this run)
- retrieved_at: 2026-09-25
- source_type: post (research repo / README write-up)
- access_scope: sections listed — full README read
- sections_read: Methodology, Self-Preference Index definition, Per-Model Results, Authors, Key Limitations
- topics: LLM-as-judge, self-preference bias, evaluation reliability, position bias

## Claims from this source

- C-0002: Across four frontier models in two vendor families (GPT-4o-mini, GPT-4o from OpenAI; Claude Haiku 4.5, Claude Sonnet 4.6 from Anthropic), blind pairwise judging of 24 open-ended prompts (1,152 total pairwise judgments, both presentation orders tested) produced a mean Self-Preference Index (SPI) of +0.14 — every judge rated its own model family's answers higher than a leave-one-out consensus of the other judges would. Per-model: GPT-4o-mini +0.07, GPT-4o +0.21, Claude Haiku 4.5 +0.14, Claude Sonnet 4.6 +0.14.
  - locator: README "Per-Model Results"
  - evidence_label: bounded empirical (explicitly labeled a pilot by the author)
  - limitations: author states this is pilot scale — 24 prompts, 4 models, 2 families, a 3-judge consensus baseline; open-ended prompts only (no verifiable/ground-truth tasks); response length correlates with win rate (SPI is designed to control for this, but raw scores mix quality and length).
  - relationship to existing claims: new
- C-0002b: Only Claude Sonnet 4.6 showed above-chance self-recognition (+0.29 discrimination) when separately asked whether it authored a given response; the other three models performed at chance.
  - locator: README "Recognition Probe" / "Per-Model Results"
  - evidence_label: bounded empirical
  - limitations: same pilot-scale caveats as above; self-recognition and self-preference are shown to be dissociable (bias exists even without reliable recognition), which the author's title makes explicit ("without self-recognition").
  - relationship to existing claims: new

## LayerLens relevance

- Open question #2 (Failure attribution in the UI) and differentiator #3 (reproducible, defensible grading — "a self-check wobbles"): this is direct, quantified evidence that an LLM Judge is not neutral about outputs from its own model family, even in blind conditions and even absent reliable self-recognition. It supports keeping mechanical Graders as the load-bearing verdict and treating Judges/Scorers explicitly as policy-tuned, bias-prone signals — and suggests the product should flag (not just allow) a Judge whose model family matches the agent-under-test.
- Confidence: moderate — the finding is internally consistent and the author is transparent about pilot-scale limits, but this is a single independent repo (not peer-reviewed, not an org with a track record we've verified), on 24 prompts. Treat as a lead to corroborate, not a settled fact. The larger academic literature on self-preference/self-enhancement bias in LLM judges (e.g. NeurIPS 2024 work referenced in general search results) points the same direction but was not independently opened this run.
