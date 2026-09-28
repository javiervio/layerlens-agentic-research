# Agent runbook

The exact steps of a single weekly run. You (the cloud agent) start with zero context. This repo is your only memory. Follow these steps in order. Read `PROTOCOL.md` first, in full, and obey it.

## 0. Orient

1. Read `PROTOCOL.md`, `LAYERLENS_CONTEXT.md`, and `SOURCES.md` in full.
2. Read `knowledge/claims.md`, `knowledge/competitive.md`, and `knowledge/changelog.md`.
3. Read the last few files in `runs/` to see what the previous runs covered, what failed, and what is pending.
4. If any of these cannot be read, record the problem in a run log and stop before overwriting anything.

## 1. Discover

Combine the four angles in `SOURCES.md`: category searches, named team channels, citations, and public posts. Search by problem, not by lab name. Use a seven-day overlap window against the last run's date so late-published work is not missed. Consider up to about 25 candidates. Deduplicate by arXiv id, DOI, event, and evidence family. A blog, a LinkedIn post, and an X thread about one launch are one event.

Budget guidance per run: about ten searches, split roughly four on research, four on teams and competitors, two on deliberate exploration or contradicting evidence. Rotate which teams you check so the whole `SOURCES.md` list gets covered over several weeks. If a family is skipped, note it as pending for next run.

## 2. Read and record

Open original sources. A search snippet only justifies discovery, never a claim. Open up to two sources deeply this run; skim the rest to triage. Mind the cloud network limits (see the "Network reality" section in `SOURCES.md`): to read deeply, prefer reachable mirrors such as a paper's GitHub repo, and use WebSearch content; when only a search summary is available, mark the card "incomplete access (search summary only)" and still record the canonical link for Javier. A blocked fetch is never a run failure. For each source that earns a card, create `cards/<short-slug>.md` using the template in `cards/README.md`. Record: title, authors or organization, canonical URL, the URL you discovered it through, date (or "date unknown" if only relative), version, date read, how much you read, the claims with their locators, evidence label, and limitations.

If you could only reach the abstract, say so and do not describe methods or results you did not see.

## 3. Compare against what we know

For each new claim, compare it to `knowledge/claims.md`: does it confirm, extend, contradict, supersede, or add nothing. Preserve prior sources and history. A contradiction opens an entry in the changelog for review; it does not automatically make the new claim true. Update `knowledge/competitive.md` with evidence, never inferring a missing capability from silence.

## 4. Update the knowledge files

**Order is mandatory: re-analyze the existing record FIRST, create new entries LAST.** Nothing is ever added "because it is Monday." A run with zero new entries but two confidence upgrades is a good run.

0a. **Corroboration pass (before creating anything, and across EVERY layer of the record).** Walk every new finding against the whole existing record, not just feature candidates: claims in `knowledge/claims.md`, each idea's hypothesis in `ideas/backlog.md`, feature rows and their scores, the open design questions in `LAYERLENS_CONTEXT.md` (a finding can partially answer one — say so), and even `SOURCES.md` itself (a source that keeps producing nothing can be demoted). For each, decide: does it confirm, strengthen, weaken, contradict, or partially answer something we already hold? Apply those effects first — raise or lower confidence with the reason and the new evidence link, bump idea maturity, recompute matrix scores, annotate the open question. Research alone can validate a hypothesis (that is an evidence-validated upgrade, distinct from a product-check-validated one — label which kind it is). Slow validation of existing hypotheses is the primary product of a run; new entries are the leftover.

0b. **Dedup gate (for whatever remains).** A new claim, pain point, idea, or feature may only be created after checking it against ALL existing entries (claims by topic, ideas by pain point and open question, features by area and pain point). Near-duplicates get merged into the existing entry as added evidence, never created twice. Every genuinely new entry must carry a one-line dedup note: "Dedup: checked against I-xxxx / F-xxxx; distinct because ...". An entry without that line is invalid.

1. Add or update claims in `knowledge/claims.md`, each with its source link, date, and confidence-with-reasons.
2. Update `knowledge/competitive.md` for any team finding, using the sequence in `PROTOCOL.md`: problem, their solution, its limits, our users' need, a LayerLens alternative, the comparison that would validate it.
3. Append to `knowledge/changelog.md`: what changed this run, which prior claim it affects, and what is still in dispute.
4. Update `ideas/backlog.md` (see `PROTOCOL.md`, "The ideas backlog"): for each finding with a product implication, attach its evidence to an existing idea (raise its evidence count and maturity if warranted) or create a new L0 idea. Update the prioritization table at the top. Never let a single mention reach L2 (ready to spec).
5. Update `features/matrix.csv` (rules in `features/README.md`): add a row for any idea that gained a product-shaped hypothesis, refresh evidence links and maturity on existing rows, recompute Confidence, Priority, and Label. Never delete a row. If this is the first run of the month, prepare the ranked top-3 recommendation for the brief.

## 5. Write the weekly brief

Write `briefs/YYYY-Www.md` (ISO week, for example `2026-W40.md`) AND overwrite `LATEST_BRIEF.md` with the same content. Keep it to a five-minute read. Structure:

- **What deserves your attention** (up to five signals). Roughly two research, two competitive, one connection between them. Each: what it is, why it matters, the link, and what changed since last week. Do not pad to hit a quota; fewer is fine.
- **What changed in what we know**: prior claim, new evidence, current status.
- **One concept to understand better**: a plain-language explanation, an example, and when it does not apply. Tie it to a LayerLens open question where you can.
- **Possible applications to LayerLens** (one or two): problem, how others solve it, the gap, the assumption about our product, and a small test a designer could run. Reference the specific open question from `LAYERLENS_CONTEXT.md` by number.
- **Ideas that advanced**: which `ideas/backlog.md` entries gained evidence or moved up a maturity level this run (id, what moved, new level). Omit if nothing moved.
- **Feature ranking moves**: any `features/matrix.csv` rows added or re-ranked this run (id, old score to new score, why). On the first run of each month, add the ranked recommendation: top 3 by priority, one line of "why now" each, and what evidence would change the ranking. Omit on other weeks if nothing moved.
- **For you**: one comprehension question and one small design exercise.
- **Coverage and gaps**: what you reviewed, what was inaccessible, what is pending. Never claim complete coverage of a field from a few searches.

Distinguish a genuinely new publication from an old foundation you happened to discover this week.

## 6. Update the learning file

Append to `learning/tutor.md`: the concept from this week's brief, the exercise, and a slot for Javier's answer. Do not mark anything as "learned"; that only happens when Javier records his own explanation.

## 7. Log the run

Create `runs/YYYY-MM-DD.md` recording: date, sources reviewed, sources that failed and why, candidates considered, cards created, claims changed, brief written yes/no, and final status (complete, partial, failed, or no relevant findings). "No relevant findings" is only valid if the intended sources were actually reviewed.

## 8. Commit and push

```
git add -A
git commit -m "Weekly research run: <date> (<n> cards, <m> claim changes)"
git push origin main
```

If the push fails, the run is incomplete. Record the failure in the run log and do not claim success. Never overwrite existing files with empty content if a step failed midway.
