# Annotrace: A Workbench for Step-Level Annotation of Agent Traces

- authors_or_org: Arun Josephraj Arokiaraj, Chenyi Huang, Sahan Bulathwela, Zekun Wu, Bin Wu
- canonical_url: https://arxiv.org/abs/2610.23284v1
- discovered_url: inbox/arxiv/2026-W43.md (cs.MA)
- discovered_via: feed
- doi_or_arxiv_id: 2610.23284v1
- version: v1
- published_at: 2026-10-16
- retrieved_at: 2026-10-26
- source_type: paper
- access_scope: abstract only (arxiv.org EGRESS_BLOCKED; read verbatim from the arXiv inbox)
- sections_read: abstract (verbatim, via inbox)
- topics: trace annotation tooling, step-level granularity, human-AI joint annotation

## Claims from this source
- C-0079: Annotrace is a workbench addressing a recognized gap: observability platforms record agent traces but offer no structured labelling, while existing annotation tools label text but have no notion of a step, delegation, or tool call. Annotrace reads six trace formats (including OpenTelemetry GenAI, LangSmith, and Langfuse) and turns each run into an ordered, nested list of steps at a consistent granularity. The annotator writes a labelling codebook; a frontier model proposes a starting set from a sample of the annotator's own traces, then answers the same questions the human is asked, making annotation a joint human-AI process with measured agreement between any two annotators (human or AI). On a multi-agent question-answering corpus, Annotrace reproduces a previous manual effort's 235 annotation units exactly, and two models labelling the same traces agree 91% of the time at kappa=0.82.
  - locator: abstract, verbatim
  - evidence_label: documented capability / bounded empirical (abstract read directly)
  - limitations: abstract only; one corpus for the reproduction/agreement numbers; cross-format "step" unit is the authors' own definition, not an industry standard.
  - relationship to existing claims: a concrete, general-purpose tool for exactly the problem T-03/I-0003 is about — turning a raw trace into attributable, labelled units at a defined granularity — but built as a research/ops annotation workbench rather than a product-facing attribution surface. Useful as a reference for what "a step" should mean when LayerLens's own trace UI surfaces attribution as a location (I-0003's hypothesis): delegation and tool-call boundaries, not raw log lines.

## LayerLens relevance
- open question(s) touched: #2 (attribution), #9 (comparison as the signature surface — a consistent step unit across trace formats is a prerequisite for any trajectory diff to be legible).
