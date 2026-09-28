# Magentic-UI

- authors_or_org: Microsoft Research
- canonical_url: https://www.microsoft.com/en-us/research/publication/magentic-ui/
- discovered_url: seeded from SOURCES.md ("Reference points and benchmarks" — Microsoft HAX guidelines and Magentic-UI)
- discovered_via: citation (our own seed list, verifying relevance per SOURCES.md instructions)
- doi_or_arxiv_id: not captured this run
- version: n/a
- published_at: date unknown (not captured from the fetched excerpt)
- retrieved_at: 2026-09-25 (page summary); extended 2026-09-28 with a direct read of the GitHub repo README and configuration docs
- source_type: docs (Microsoft Research publication page; extended with github.com/microsoft/magentic-ui, reachable directly via WebFetch)
- access_scope: sections listed — 2026-09-25 was a page summary via WebFetch; 2026-09-28 added a full direct read of the repo README and raw.githubusercontent.com/microsoft/magentic-ui/main/docs/configuration.md
- sections_read: overview, "core approach to human oversight," interaction mechanisms list, key finding (2026-09-25); README action-guards description, configuration.md's "Tool Approval" section in full (2026-09-28)
- topics: human-agent interaction, oversight, human-in-the-loop, action guards, tool approval policies

## Claims from this source

- C-0005: Magentic-UI is an open-source web interface (multi-agent architecture, web browsing/code execution/file manipulation, extensible via MCP) built around human-in-the-loop collaborative control rather than full autonomy, with named interaction mechanisms: co-planning, co-tasking, multi-tasking, action guards (safety checkpoints), and long-term memory.
  - locator: page overview + "Core Approach to Human Oversight" (via WebFetch summary)
  - evidence_label: documented capability (first-party description of their own system) / proposal for the framing that human-in-the-loop is "a promising path forward"
  - limitations: only a summary of the publication page was read, not the underlying technical report or any evaluation data; no quantitative results were captured.
  - relationship to existing claims: new

- C-0011: (2026-09-28 addition, directly read) Magentic-UI implements "action guards" concretely as a configurable **tool approval policy** with three named settings: `auto_approve` (no user checks, "eval / trusted setups only"), `require_approval_untrusted` (the default — prompts before tool calls deemed untrusted, auto-approves read-only calls), and `require_approval_all` (every tool call requires confirmation). Policies are set per-agent (orchestrator or web_surfer) via YAML config.
  - locator: raw.githubusercontent.com/microsoft/magentic-ui/main/docs/configuration.md, "Tool Approval" section, read in full
  - evidence_label: documented capability (first-party docs, directly read, not a summary)
  - limitations: the documentation, as read, does **not** state what information a confirmation dialog actually displays to the user, whether it names the specific consequence of the pending action, or whether an approval is scoped to one action, one session, or persists across a run. Per PROTOCOL.md rule 5 ("absence of evidence is not evidence of absence"), this is recorded as "not described in what we read," not as "Magentic-UI lacks this feature" — the README pointed to a further limitations.md that was not fetched this run.
  - relationship to existing claims: extends C-0005 by replacing the vague "action guards" framing with the actual three-tier policy mechanism.

## LayerLens relevance

- Open question #2 (Failure attribution in the UI, "diagnosis as a door") and #6/#7 (Human control and recovery, "do confirmations show specific consequences?"): Magentic-UI's three-tier tool-approval policy (C-0011) is a concrete, comparable design LayerLens can benchmark against — it answers "can a human set how cautious the agent should be" (yes, per-agent, three levels) but, as read, leaves open exactly the question LayerLens's open question #7 asks verbatim: whether a confirmation names specific consequences. That gap is worth testing directly (open `docs/limitations.md` or the actual approval-prompt UI code next run) before assuming either product is ahead here.
- No longer flagged as incomplete access for the tool-approval mechanism specifically (C-0011, directly read); the original publication-page summary (C-0005: co-planning/co-tasking/multi-tasking/long-term memory) remains incomplete access until those specific mechanics are read directly.
