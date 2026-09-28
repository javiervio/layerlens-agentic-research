# LayerLens Agentic Environments Research

A private, self-updating research base on agentic environments, agents, evaluation, synthetic data, and human/agent interaction. It runs itself: a scheduled Claude Code cloud agent researches on a fixed rhythm, updates this repo, and writes a weekly brief you can read in five minutes.

Owner: Javier Viola. Purpose: stay current on agentic environment trends, known issues, and pain points, and turn that into design decisions for LayerLens Environments (Stratix).

## How it works

1. A scheduled cloud agent (a Claude Code "routine") wakes up once a week.
2. It clones this repo, reads the current state, and does fresh research from the web.
3. It records what it found as source cards, updates the knowledge files, and writes the week's brief.
4. It commits and pushes back to `main`. The `git diff` between weeks is literally "what changed."

The agent has zero memory of its own. **This repo is its memory.** Everything it needs to think lives here.

## Where to read

- **`LATEST_BRIEF.md`** at the repo root: the newest weekly brief. Start here every Monday.
- **`briefs/`**: every past brief, dated.
- **`knowledge/claims.md`**: the current state of what we believe, each claim with a link, date, and how confident we are.
- **`knowledge/competitive.md`**: what other teams are doing, framed as problem, their solution, its limits, and the LayerLens opportunity.
- **`ideas/backlog.md`**: a durable ledger of ideas for the Environments experience, each tied to a pain point, a user outcome, its evidence, and a maturity level (nascent to ready-to-spec). The deep-traceability layer.
- **`features/matrix.csv`**: the payoff. The ranked feature sheet (opens in Excel/Sheets): impact, effort, evidence-derived confidence, auto-computed priority, and labels (quick win, big bet, needs evidence). Rules in `features/README.md`. This is where you decide what to build.
- **`learning/tutor.md`**: concepts explained plainly plus your running comprehension log.

## The files the agent obeys (change these to steer it)

- **`PROTOCOL.md`**: the rules. Scope, evidence discipline, what it may and may not do.
- **`LAYERLENS_CONTEXT.md`**: what our Environments product is and our open design questions. This is what makes the research ours and not generic. Correct it whenever reality changes.
- **`SOURCES.md`**: where to look. Categories, teams, and search vocabulary.
- **`AGENT_RUNBOOK.md`**: the exact steps of a single run.

## How to use it as a designer

You do not need to run anything. Read the Monday brief. When a finding matters, promote it yourself: open a Linear ticket, sketch a flow, or add a note to `LAYERLENS_CONTEXT.md` as a new open question. The agent researches and proposes. You decide.
