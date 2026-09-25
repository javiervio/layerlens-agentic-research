# Source cards

One file per source the agent reads deeply, named `<short-slug>.md`. A card is the traceable record behind a claim: it preserves the links and the exact scope of what was read. The agent creates these per `AGENT_RUNBOOK.md`.

## Template

```
# <Original title>

- authors_or_org:
- canonical_url:
- discovered_url:
- discovered_via: feed | search | citation | post | Javier
- doi_or_arxiv_id:
- version:
- published_at:            # or "date unknown" if only relative
- retrieved_at:            # date read
- source_type: paper | docs | study | issue | postmortem | post | release
- access_scope: full text | sections listed | abstract only
- sections_read:
- topics:

## Claims from this source
- C-xxxx: statement, with precise scope
  - locator: section, table, or short quoted fragment
  - evidence_label:
  - limitations:
  - relationship to existing claims: confirms | extends | contradicts | supersedes | new

## For social posts, also record
- permalink:
- author affiliation (verified):
- thread context:
- linked evidence:

## LayerLens relevance
- open question(s) touched (by number), or "general"
```
