# Feature matrix

**Live sheet: https://docs.google.com/spreadsheets/d/1tRhbi2gFUaG30n4ioDpNjEafBay1rgTtPCvGPAj8LY4/edit** (permanent URL, never recreated). It self-syncs from this repo hourly via the Apps Script in `sheet-sync.gs`: the Data tab mirrors `matrix.csv`, the Matrix tab computes Confidence, Priority, and Label with live formulas, and the Overrides tab is where Javier's Impact/Effort/Decision overrides go (they always win over synced values; the agent folds them back into the CSV, recorded as overrides).

`matrix.csv` is the canonical data where research becomes product: every feature recommendation for the Environments experience, scored and ranked. It opens directly in Excel, Numbers, or Google Sheets. The agent owns keeping it current; Javier owns decisions.

## The traceability chain (nothing enters without it)

Every row must be traceable end to end:

**source (paper/post/experiment, with link) → claim (C-xxxx in `knowledge/claims.md`) → pain point → idea (I-xxxx in `ideas/backlog.md`) → hypothesis → feature (F-xxxx here) → decision.**

A feature row without an Idea ID and at least one evidence link is invalid. The deep reasoning lives in the idea entry; the matrix is the ranked, scannable view on top of it.

**Completeness and dating are hard rules.** Every cell in every row must be filled — no blanks, ever ("date unknown" is a valid value; an empty cell is not). Every evidence link travels with its dates in the `Source dates` column: publication date (or "date unknown") and the date we read it. `Date added` and `Last update` are always stamped. Before committing, the agent must validate the CSV (equal column counts, no empty cells, Priority = round(Impact x Confidence / Effort, 2)); a run that would commit an invalid matrix must fix it first.

**Plain-language is mandatory.** Every feature carries an **In plain terms** value: two to four jargon-free sentences saying what the feature would do and why it helps, written so Javier understands the feature without opening a single paper. No LayerLens/ML jargon, no citations, no metric names, just what it is and what changes for the user. This column leads the sheet view (right after the feature name). A feature without a plain-terms explanation is incomplete.

**Duplicates are forbidden.** A new row requires a dedup check against all existing rows (by pain point and area) recorded in Notes; near-duplicates merge as added evidence on the existing row instead.

## Scoring (same scheme as the MinervaBlue matrix, adapted)

**Priority = Impact × Confidence / Effort**, rounded to 2 decimals.

- **Impact (1-5)**, anchored to user outcomes, not excitement:
  - 5 = changes a core decision users make (ship/don't ship, trust/don't trust) or lands directly on a moat differentiator
  - 4 = removes a documented pain point for a P0 persona in a primary flow
  - 3 = meaningfully improves comprehension, speed, or recovery in a primary flow
  - 2 = improves a secondary flow or a P1-persona task
  - 1 = polish
- **Effort (1-5)**, the agent's estimate from what it knows of the v1 codebase and surfaces: 1 = badge/copy/metadata-level, 2 = one surface touched using existing data, 3 = one surface plus new computation, 4 = multiple surfaces or new backend interaction, 5 = new subsystem. **Every effort value is an estimate pending engineering sizing; treat it as a conversation starter, not a commitment.**
- **Confidence is not a gut feeling — it is derived from evidence maturity** in `ideas/backlog.md`:
  - L0 nascent (single mention) → 0.3
  - L1 developing (multiple sources, or one strong source + outcome + validation plan) → 0.6
  - L2 ready to spec → 0.9
  - +0.1 if the linked product check or user test has been run and supports it (cap 1.0)

This is why a single mention can never rank high: at L0 the confidence multiplier crushes the score by design. Corroboration, not enthusiasm, moves a feature up.

## Labels (auto-assigned by the rules, in this order)

1. **Dropped / Parked / Promoted** — Javier decided (overrides everything; record the reason in Notes).
2. **Needs evidence** — maturity is L0. Not scoreable for action yet, listed so it is not forgotten.
3. **Needs sizing** — Impact or Effort missing.
4. **Quick win** — Impact ≥ 4 and Effort ≤ 2.
5. **Big bet** — Impact ≥ 4 and Effort ≥ 4 (worth it, needs a real slot).
6. **Reconsider** — Impact ≤ 2 and Effort ≥ 4.
7. **Proposed** — everything else with a valid score.

## Status column

`Idea` (lives here only) → `Checked` (the product check ran; result noted) → `Promoted` (Javier moved it to Linear/Figma) → `Building` / `Shipped` / `Parked` / `Dropped`. Only Javier moves a row past `Checked`.

## Who does what

- **The agent (every run)**: adds rows when an idea earns one, updates evidence links and maturity, recomputes Confidence, Priority, and Label, and never deletes a row (dropped rows are labeled, not removed).
- **The agent (first run of each month)**: writes a short ranked recommendation in the brief — the top 3 candidates by priority with a one-line "why now" each, plus anything whose evidence changed enough to re-rank.
- **Javier**: validates Impact/Effort where he disagrees (his numbers win; the agent records the override), runs or delegates the product checks, and decides Promote / Park / Drop.
