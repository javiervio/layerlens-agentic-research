# Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning

- authors_or_org: Zuo Gou, Chenhao Lu
- canonical_url: https://arxiv.org/abs/2611.08144
- discovered_url: inbox/arxiv/2026-W46.md (cs.SE)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2611.08144v1
- version: v1
- published_at: 2026-11-05
- retrieved_at: 2026-11-16
- source_type: paper
- access_scope: abstract only (verbatim, read directly via arXiv-harvest inbox)
- sections_read: abstract
- topics: environment/trainer boundary, attribution, trust wall, outcome-only checks vs process checks

## Claims from this source
- C-0128: When an RL environment runs outside the trainer (another process/machine/language), many faults at that boundary raise no error. Across Pendulum, HalfCheetah, Hopper, and a 7-joint arm, the authors injected up to 23 faults into what crosses the wire and 2 into the trainer's log. A learning-curve threshold caught at most one run in ten, and comparison with fault-free seeds caught at most 21%; a clean evaluation of all 1,060 final policies agreed with these curve checks — of 728 boundary-fault runs both curve checks passed, 723 scored within three standard deviations of fault-free seeds, even though nearly all of them ended on different weights. In contrast, a step ledger kept on both sides of the boundary and compared step-by-step caught and located every injected fault, at a median 3% training-time cost on Pendulum. An episode record kept at the environment side also caught faults injected into the trainer's own log.
  - locator: abstract, verbatim
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; robotics RL domains (Pendulum/HalfCheetah/Hopper/Pusher), not LayerLens's own system types; single-machine and one two-machine condition tested.
  - relationship to existing claims: strengthens T-02 (outcome-only checks miss nearly everything; a real-production instance of the pattern C-0043's 92.6%-hidden-deviation finding already showed) and T-03 (attribution requires checking the run itself, not just its outcome — directly parallel to C-0048 Agent-Warden's below-the-trace causal recovery). New and sharply relevant: this paper's "boundary" is literally agent-environment, LayerLens's own exact seam.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — a concrete demonstration that checking only the final outcome across a run misses nearly every real fault, while a step-level ledger at the environment's own side catches all of them, which is architecturally close to what LayerLens's deterministic minting + answer-key-at-request-time already does); #3 (deterministic replayability).
