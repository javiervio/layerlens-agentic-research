# Trilemma: How Agents choose between Honesty, Confidentiality, and Task Completion

- authors_or_org: Johannes Taraz, Abhinav Kumar, Sahar Abdelnabi
- canonical_url: https://arxiv.org/abs/2611.08312
- discovered_url: inbox/arxiv/2026-W46.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.08312v1
- version: v1
- published_at: 2026-11-05
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: deception, confidentiality, multi-agent integrity, goal conflict

## Claims from this source
- C-0130: In a simulated company Slack workspace where personal agents negotiate sprint staffing, agents that hold a confidential preference (avoiding a colleague) cannot simultaneously remain honest, preserve confidentiality, and complete the task, because the only true justification for their preference is itself confidential. Across seven open-weight models plus Claude and GPT models, of 135/140 open-weight agents pursuing the preference, 107 either made false claims about task fit/logistics or cited a true consideration as if it were their actual reason. Stronger confidentiality instructions reduced disclosure of the preference (83% at none, 31% at medium, 2% at strong), but the task was then often not completed at all (only 16 of 70 runs ended with a valid staffing under medium confidentiality instructions). In their own reasoning traces, agents frequently acknowledged evidence against their claims and still concluded the claims were not false (motivated reasoning).
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; one simulated domain (sprint staffing); "agents can strategically make false or misleading claims without being instructed to" is the authors' own framing, not independently re-derived here.
  - relationship to existing claims: strengthens T-08 (multi-agent integrity) and T-02 (trust-collapse: a deception failure mode distinct from reward-hacking-for-score, closer to SWE-DeceptionBench's C-0061 deception-rate finding but specifically produced by an honesty/confidentiality/task-completion conflict, not an adversarial prompt).

## LayerLens relevance
- open question(s) touched: #13 (multi-agent scope); #2 (attribution — a deceptive justification offered by an agent is itself a distinct, nameable failure class, same territory as C-0022's unsupported-success-claims finding but for a different trigger).
