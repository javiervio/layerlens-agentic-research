# Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction

- authors_or_org: Haoran Bu, Yiting Shen, Litian Zhang, Ruihan Hu, Xi Zhang
- canonical_url: https://arxiv.org/abs/2610.38209v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.MA harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.38209v1
- version: v1
- published_at: 2026-10-28
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: agent memory, trust wall, provenance/authority, social engineering

## Claims from this source
- C-0123: The authors formalize Role Grounding Attack (RGA): an attacker publishes an experience-sharing post quoting an inner conversation (between the attacker's own agent and the attacker's own user) that expresses the attacker-user's preferences; when a victim agent reads and remembers from this nested structure, its memory loses the context binding and grounds the attacker's preference to the *victim's own* user instead (Role Grounding Misattribution). The misattributed preference persists through retrieval and later influences the victim's decisions. Instantiated as tool-selection manipulation (steers the victim toward an attacker-controlled tool) and privacy leakage (further causes the victim to include sensitive information in tool arguments to satisfy a misattributed task requirement), both achieve high attack success rates across five mainstream memory systems and six language models.
  - locator: abstract (verbatim)
  - evidence_label: bounded empirical (a formalized attack model tested across five memory systems and six models, with high reported success rates though exact numbers not in the abstract itself)
  - limitations: abstract only; exact attack-success-rate figures and per-system/per-model breakdowns not captured; a constructed red-team study, not an observed real-world exploit.
  - relationship to existing claims: names a genuinely new vulnerability class distinct from everything T-02's trust-wall cluster already tracks (credential/secret leakage, ground-truth access, confidentiality-mosaic inference) — this is about *authorship/authority* of a remembered preference being forgeable, not the content's secrecy or accuracy. Forms a clean attack/defense pair with ClawMMU (C-0124, same inbox), which proposes exactly the structural fix (label every memory entry with its owner/scope/origin/authority; authority never self-elevates) this attack exploits the absence of.

## LayerLens relevance
- open question(s) touched: #7 (human control — a misattributed "preference" is a kind of silent authority escalation), general scope area "context and memory" per PROTOCOL.md
