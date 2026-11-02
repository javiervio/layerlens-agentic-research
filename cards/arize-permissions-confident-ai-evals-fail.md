# Arize ("AI agent permissions") and Confident AI ("Three Ways AI Systems Fail Even When Evals Pass") — two thin leads

- authors_or_org: Arize AI; Confident AI (DeepEval)
- canonical_url: https://arize.com/blog/ai-agent-permissions/ ; https://www.confident-ai.com/blog/three-ways-ai-systems-fail-even-when-evals-pass
- discovered_url: inbox/competitors/LATEST.md (Arize feed and Confident AI sitemap, 2026-W44)
- discovered_via: feed (competitor harvester) then search
- doi_or_arxiv_id: n/a
- version: n/a
- published_at: Arize 2026-10-15; Confident AI date disputed (a third-party index gives 2026-04-07, unverified; the post appears in this week's sitemap crawl)
- retrieved_at: 2026-11-02
- source_type: post
- access_scope: incomplete access — both are thinner than usual: WebSearch returned only the teaser/opening framing for each, not the full argument (arize.com and confident-ai.com both read via search summary only, not opened directly)
- sections_read: n/a (search teaser only)
- topics: agent permissions/authorization, evaluation blind spots

## Claims from this source
- C-0110 (Arize): The post frames a problem directly on point for LayerLens's open question #7: **"a model can't reliably verify [authorization] just because someone claims to have them in a conversation"** — and the teaser adds agents fail in both directions (sometimes wrongly refusing, sometimes wrongly proceeding) when permission is ambiguous. No further argument or recommendation was retrievable this run.
  - locator: WebSearch teaser of the Arize blog post (title, dek, opening sentence)
  - evidence_label: incomplete access (teaser-level only — the weakest access tier recorded this run; recorded honestly per PROTOCOL rather than inferring the rest of the argument)
  - limitations: only the framing of the problem was retrieved, no result, mechanism, or recommendation.
  - relationship to existing claims: adjacent to **I-0006** (confirmations naming consequences) and ContractWarden's scope-level pre-authorization pattern (C-0047) — a vendor independently naming the same "an agent cannot verify its own authorization from conversational claims alone" problem, but with no retrievable solution to compare against yet.
- C-0111 (Confident AI): The post argues agents can "pass evals" while exhibiting real failure modes evals don't catch; two of the stated three modes were retrievable — **using the wrong tool and still passing** (framed as shortcut behavior, not reliable reasoning) and **skipping a required step**. The third failure mode could not be retrieved. A related post from the same vendor ("Your AI Agent Passed Evals. That's the Problem.") makes the same general point: passing shows tests didn't catch a failure mode, not that the system works.
  - locator: WebSearch teaser/partial summary
  - evidence_label: incomplete access (two of three list items only; could not confirm DeepEval-framework specifics)
  - limitations: incomplete list (2 of 3 modes); publication date unconfirmed.
  - relationship to existing claims: a vendor's own, independently-arrived-at restatement of T-02's core argument (evals passing is not the same as the system working) — doesn't add a new mechanism, but is a useful "the market already says this" citation, and the named failure modes (wrong-tool-but-passes, skipped-required-step) overlap with I-0003's attribution scope (trajectory deviation despite passing output checks, per C-0043's enterprise finding).

## LayerLens relevance
- open question(s) touched: #7 (Arize permissions); #2 (Confident AI evals-pass-anyway).
- Both are logged honestly as thin, incomplete-access leads rather than inflated into full findings — worth a direct re-read if either domain becomes reachable, or if Javier has a saved link for either.
