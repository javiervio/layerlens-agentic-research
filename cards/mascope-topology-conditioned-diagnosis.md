# Know the Shape, Find the Fault: Topology-Conditioned Diagnosis of Multi-Agent LLM Failures

- authors_or_org: Xinwen Liu, Zhuocheng Pan, Isabella Zhu, Jawei Zhang, Xudong Liu, Tianyu Wo
- canonical_url: https://arxiv.org/abs/2610.10126
- discovered_url: inbox/arxiv/LATEST.md (2026-W42 harvest)
- discovered_via: feed
- doi_or_arxiv_id: 2610.10126v1
- version: v1
- published_at: 2026-10-07
- retrieved_at: 2026-10-19
- source_type: paper
- access_scope: abstract (verbatim, directly read via arXiv harvester inbox)
- sections_read: abstract only
- topics: multi-agent failure attribution, communication topology, diagnosis cost

## Claims from this source
- C-0067: MASCope is a two-stage framework for diagnosing multi-agent-LLM coordination failures by first recovering communication topology from execution traces that lack explicit topology labels (a Trace Structural Extractor grounding an interaction graph in message evidence), then classifying failures using the trace, predicted topology, an empirical failure prior from separately labeled traces, and a short description of topology-specific failure patterns (a Topology-Conditioned Judge). A statistically significant association between topology and failure type was found (chi^2 = 409.9, p = 1.2e-70). On 851 MAST-clean traces, ground-truth topology context raised gpt-mini's Macro-F1 from 0.173 to 0.350; with predicted (not ground-truth) topology the pipeline reached 0.346, close to a trace-only gpt-5.4 baseline's 0.372, at roughly 6% of the cost of repeated gpt-5.4 diagnosis for 1,000 traces (including one topology extraction).
  - locator: abstract
  - evidence_label: bounded empirical (abstract read directly)
  - limitations: abstract only; single labeled dataset (MAST-clean); "approaching" a stronger baseline, not beating it
  - relationship to existing claims: a new family for T-03 and nursery N-04 (multi-agent system evaluation) — the first claim in this knowledge base to formalize *communication topology* as a structural cue for attribution in multi-agent failures, complementary to C-0015's per-model failure taxonomy and C-0017's mechanism-level single-agent attribution.

## LayerLens relevance
- open question(s) touched: #2 (failure attribution), #13 (multi-agent scope — a concrete method for attributing blame within a multi-agent system, relevant if LayerLens's environment/verification model is ever extended beyond single-agent-against-environment).
