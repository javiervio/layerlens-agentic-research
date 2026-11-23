# Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents

- authors_or_org: Dimitris Papailiopoulos, Microsoft Research
- canonical_url: https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/
- discovered_url: inbox/reference/LATEST.md (Microsoft Research feed, 2026-W47)
- discovered_via: feed
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: 2026-11-10
- retrieved_at: 2026-11-23
- source_type: post
- access_scope: full text, read directly (WebFetch; microsoft.com reliably reachable per SOURCES.md)
- sections_read: full text
- topics: model-weight security, backdoors, trust wall, verification limits

## Claims from this source
- C-0174: "Lazarus" is a backdoor technique that reprograms dormant (rarely-firing) neurons so an otherwise normal agent executes malicious commands only when a hidden trigger appears (example: a date passing into 2027), inserted without retraining and requiring only inference-level compute — pretraining organizes representations well enough that a linear classifier fit on ~50 examples can separate trigger from non-trigger inputs, and chaining a few reprogrammed neurons can force arbitrary payloads into the residual stream and into a terminal. Reprogramming fewer than 10 dormant neurons suffices; the backdoored model passes standard evaluations and behaves normally until triggered. The post states plainly: "no scan can prove beyond any doubt that a model is safe" and "no audit can guarantee safe behavior" — reliable detection requires diffing against original, unmodified weights, making provenance essential. Mitigations proposed: weight-provenance verification tying a model to its publisher, scanning the surrounding software environment, separately-scanned containers, planned cryptographic model signing with tamper-evident provenance, and operational advice (limit agent permissions, monitor actions, review consequential actions before execution, treat audits as evidence not guarantees).
  - locator: full post text
  - evidence_label: documented capability (first-party, directly read; the research itself is presented as internal findings, not an independently peer-reviewed study)
  - limitations: the post's own description of the mechanism is stated to be simplified; no quantitative success/detection-rate table beyond the qualitative findings listed; the attack requires write access to a model checkpoint (a compromised account, pipeline, or storage system), so it is a supply-chain/insider threat, not a remote exploit of a running agent.
  - relationship to existing claims: a new, sharply-stated T-02 family, and the third independent source this run converging on "signed/scanned/verified is not the same property as behaviorally safe" — alongside C-0131 ("Signed, Sealed, Leaked," an academic MCP-tool paper) and Arize's own "Evil Qwen and activation steering" post (already in competitive.md, 2026-10-30) — a genuine three-source convergence (an academic paper, a competitor's blog, and a frontier lab's own research) landing on the identical lesson in close succession.

## LayerLens relevance
- open question(s) touched: #3 (deterministic replayability — provenance/hash verification is directly relevant to any "reproduce this exact run" affordance), #11 (reviewer surface — "an audit is evidence, not a guarantee" is a caution any LayerLens attestation/evidence-chain surface should carry explicitly, not imply certainty)
- general: LayerLens's trust wall concerns the environment side (seed/knobs hidden from the agent); this threat concerns the agent/model side (an agent-under-test's own weights could be compromised before LayerLens ever sees it) — worth a note that LayerLens's verification story is necessarily about behavior observed during a run, not a guarantee about what the agent-under-test's weights contain.
