# Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions

- authors_or_org: Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang, Wooseong Yang, Yuwei Han, Philip S. Yu
- canonical_url: https://arxiv.org/abs/2610.22138v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: 2610.22138v1
- version: v1
- published_at: 2026-10-15
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: multi-agent trust, private vs public belief, adversarial conformity, N-04

## Claims from this source
- C-0080: In a ten-agent factual discussion, one or three adversarial agents repeatedly assert a plausible false answer. Probing each benign agent's *private* answer (via a separate hidden call) versus its *public* stance reveals the two diverge sharply: without an attacker, groups are stable (only 0.6% of benign agents finish holding the false answer). With one adversarial agent, 44.8% of benign agents end up privately holding the false answer; with three, 60.5%. With three adversaries present, benign agents privately hold the false answer in 51.6% of exposed turns but publicly endorse it in only 19.7% of those same turns — most of the influence is invisible in the visible discussion. Agents that retain the true answer often fail to defend it; once adopted, false answers spread among benign agents, and baseline model knowledge does not predict robustness.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; six models, three factual-QA datasets, a minimal/synthetic adversary design (fixed repeated false assertion), not a naturalistic multi-agent deployment.
  - relationship to existing claims: a structurally new mechanism for N-04 (multi-agent systems evaluation nursery) and T-03 (attribution): it shows that a multi-agent trace's visible/public record can systematically under-represent what agents actually came to believe — private belief collapses more than the public discussion shows. This complicates any attribution or evaluation approach that reads only the visible trace/transcript (as most current trace-based tooling, including Annotrace/C-0079 and MASCope/C-0067, does by necessity): the "ground truth" of an agent's actual belief state may not be recoverable from the trace alone in an adversarial multi-agent setting.

## LayerLens relevance
- open question(s) touched: #13 (multi-agent scope — directly feeds the still-undecided strategic question of whether LayerLens's environment/verification model should extend to multi-agent systems; if so, this paper argues the visible trace is an incomplete source of truth for what happened). General: also a sharper, multi-agent-specific instance of C-0016's finding that agreement/consensus is not verification.
