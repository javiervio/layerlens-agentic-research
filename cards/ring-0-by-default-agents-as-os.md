# Ring-0 by Default: Agents as Operating Systems (AaOS)

- authors_or_org: Xiang Li, Aichun Huang, Zuyao Xu, Fasheng Miao, Zheli Liu
- canonical_url: https://arxiv.org/abs/2610.33753v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.OS harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.33753v1
- version: v1
- published_at: 2026-10-24
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: environments, trust wall / isolation, harness as infrastructure, attribution

## Claims from this source
- C-0113: Mapping 116 standard-OS-textbook mechanisms across 19 subsystems onto deployed LLM-agent harnesses, the authors find only 11 mechanisms isomorphic and 65 missing outright (mostly protections: privilege separation, resource quotas, transactions, tamper-proof audit); whatever the model outputs runs with the full authority of the host user ("ring 0"), and by Anderson's reference-monitor criteria (non-bypassable, tamper-proof, verifiable), prompt-written rules satisfy none of the three. Thirteen experiments against Claude Code, Codex CLI, and Gemini CLI (25 mechanisms whose documentation alone could not settle enforcement) found checks sit in single tools so the shell bypasses them, all three CLIs loaded forged transcript records on resume, and task control/sub-agent permissions/model-based monitors were weak; 16 of 25 predictions matched, 7 gained more precise description, 2 changed verdict on direct testing.
  - locator: abstract (verbatim)
  - evidence_label: bounded empirical (a systematic mapping plus 13 concrete experiments against three real, named production harnesses)
  - limitations: abstract only (methodology detail, e.g. exact test harness/versions, not read); a mapping exercise is partly a classification judgment call, though anchored to a named criteria (Anderson's reference-monitor properties) and validated against real behavior where testable.
  - relationship to existing claims: strongly extends and sharpens T-01 (harness as first-class artifact, not just a confound) and T-02 (declared isolation vs verified isolation) — this is the most systematic, largest-scope study yet of *why* agent harnesses lack OS-grade protections, naming concrete gaps (forged resumed transcripts, shell-bypassable single-tool checks) that are directly testable against any harness, including one LayerLens's own system types sit behind.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — many of the 65 "missing" mechanisms are exactly the protections an attribution surface would need to assume exist), #7 (human control and recovery — sub-agent permissions and task control flagged weak)
