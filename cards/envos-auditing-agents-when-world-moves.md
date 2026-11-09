# EnvOS: Auditing Computer-Use Agents When the World Moves On

- authors_or_org: Ankush Kadu, Athira Gopal, Niharika Singh, Arpit Jain, Aswanth Krishnan
- canonical_url: https://arxiv.org/abs/2610.40246v1
- discovered_url: inbox/arxiv/2026-W45.md (cs.HC harvest)
- discovered_via: feed
- doi_or_arxiv_id: arXiv:2610.40246v1
- version: v1
- published_at: 2026-10-29
- retrieved_at: 2026-11-09
- source_type: paper
- access_scope: abstract only (verbatim)
- sections_read: abstract
- topics: environments, task feasibility, attribution, stale observations, verifier/grader integrity

## Claims from this source
- C-0114: EnvOS is a framework for building and certifying environments that change mid-task (a value the agent already saw changes before it acts). Before any agent runs, it checks that each change fires correctly, the task remains solvable, and the grader separates correct from incorrect behavior; after each run, a separate code path re-checks the verdict from archived evidence. In clinic booking, Claude Opus 5 went 0/16 with no extra signal, 2/16 when reminded to re-check, 15/16 when the updated value was shown (significant after full correction, p=0.00293); in insurance-claim approval, results varied by model (Opus 5 self-checked at 10/10; Sonnet 5 rose from 1/10 to 9/10 only when shown the current policy again, significant pre-registered but not after full correction). Stress-testing the grading itself: on 26 blind-corrupted episodes the pipeline accepted none as clean; on 39 externally-generated corrupted episodes it caught 25 (vs. 4 for simple log checks).
  - locator: abstract (verbatim)
  - evidence_label: bounded empirical (a named framework with a concrete, numbers-bearing application plus a grader stress-test, not yet broadly adopted)
  - limitations: abstract only; two domains tested (clinic booking, insurance-claim approval); "whether an agent caught a change varied with the model and the interface," an explicitly acknowledged limit on generalization; some significance results do not survive multiple-testing correction.
  - relationship to existing claims: a direct, close match to I-0002's own hypothesis (feasibility checking at authoring time) and I-0011 (stale observations) — EnvOS unifies both into one certification pipeline (pre-run: change fires + task stays solvable + grader discriminates; post-run: independent verdict re-check from archived evidence) and adds a concrete number for how much a stale-value-shown intervention can matter (0/16 to 15/16).

## LayerLens relevance
- open question(s) touched: #2 (failure attribution — explicitly separates "the agent," "a change that didn't fire," "an update the agent never received," and "a grader that scored wrongly" as distinct causes), #4 (task feasibility — direct match to I-0002), #8 (environments that change mid-task, adjacent to the living-graph idea's premise that state is not static)
