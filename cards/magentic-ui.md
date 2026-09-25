# Magentic-UI

- authors_or_org: Microsoft Research
- canonical_url: https://www.microsoft.com/en-us/research/publication/magentic-ui/
- discovered_url: seeded from SOURCES.md ("Reference points and benchmarks" — Microsoft HAX guidelines and Magentic-UI)
- discovered_via: citation (our own seed list, verifying relevance per SOURCES.md instructions)
- doi_or_arxiv_id: not captured this run
- version: n/a
- published_at: date unknown (not captured from the fetched excerpt)
- retrieved_at: 2026-09-25
- source_type: docs (Microsoft Research publication page)
- access_scope: sections listed — page summary via WebFetch, not the full paper/technical report
- sections_read: overview, "core approach to human oversight," interaction mechanisms list, key finding
- topics: human-agent interaction, oversight, human-in-the-loop, action guards

## Claims from this source

- C-0005: Magentic-UI is an open-source web interface (multi-agent architecture, web browsing/code execution/file manipulation, extensible via MCP) built around human-in-the-loop collaborative control rather than full autonomy, with named interaction mechanisms: co-planning, co-tasking, multi-tasking, action guards (safety checkpoints), and long-term memory.
  - locator: page overview + "Core Approach to Human Oversight" (via WebFetch summary)
  - evidence_label: documented capability (first-party description of their own system) / proposal for the framing that human-in-the-loop is "a promising path forward"
  - limitations: only a summary of the publication page was read, not the underlying technical report or any evaluation data; no quantitative results were captured.
  - relationship to existing claims: new

## LayerLens relevance

- Open question #2 (Failure attribution in the UI, "diagnosis as a door") and #6 (Human control and recovery): Magentic-UI's "action guards" (safety checkpoints) is conceptually adjacent to LayerLens's attribution chips being "a routed next action" — worth a deeper comparison in a future run (read the actual technical report / repo, not just the publication page) on exactly how action guards surface to a user and whether they name specific consequences before a confirmation, which is precisely open question #6's phrasing.
- Flagged as **incomplete access**: this card is based on a page summary, not the full paper. Do not cite specific mechanics of "action guards" as validated beyond "named as a concept" until a fuller read happens.
