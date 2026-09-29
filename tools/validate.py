#!/usr/bin/env python3
"""
Pre-commit validator for the sheet's data files. The weekly run MUST pass this
before committing (see AGENT_RUNBOOK.md). It fails loudly on the mistakes that
would break the Google Sheet or leave it half-filled, so the agent fixes them
before pushing rather than shipping a broken matrix.

Run: python3 tools/validate.py   (exit 0 = OK, exit 1 = problems printed)
"""
import csv, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []

MATRIX = os.path.join(ROOT, "features/matrix.csv")
EVIDENCE = os.path.join(ROOT, "features/evidence.csv")
THESES = os.path.join(ROOT, "knowledge/theses.csv")

MATRIX_COLS = ["Feature ID","Feature","Area","Pain point","Persona","Open Q","Idea ID",
    "Evidence links","Source dates","Maturity","Impact (1-5)","Effort (1-5)","Confidence",
    "Priority","Label","Status","Differentiator angle","Notes","Date added","Last update",
    "In plain terms","Evidence (#)","What moved","Why now"]
EVIDENCE_COLS = ["Feature ID","Source","Link","What it says","How it moved this feature"]
THESES_COLS = ["Thesis ID","Statement","Direction","Evidence (#)","Last change","Stratix implication"]

def load(path):
    with open(path, newline="") as f:
        return list(csv.reader(f))

def check_headers(rows, expected, name):
    if not rows:
        errors.append(f"{name}: file is empty"); return False
    if rows[0] != expected:
        errors.append(f"{name}: header mismatch.\n  expected: {expected}\n  found:    {rows[0]}")
        return False
    return True

def check_no_blanks(rows, name, allow_blank_cols=()):
    n = len(rows[0])
    for i, r in enumerate(rows[1:], 2):
        if len(r) != n:
            errors.append(f"{name} row {i}: has {len(r)} cells, expected {n}")
            continue
        for j, cell in enumerate(r):
            if not cell.strip() and rows[0][j] not in allow_blank_cols:
                errors.append(f"{name} row {i}: empty cell in column '{rows[0][j]}' (use a value, or 'date unknown'/'internal', never blank)")

# --- matrix ---
matrix_ids = set()
if os.path.exists(MATRIX):
    m = load(MATRIX)
    if check_headers(m, MATRIX_COLS, "matrix.csv"):
        check_no_blanks(m, "matrix.csv")
        h = {c: i for i, c in enumerate(m[0])}
        for i, r in enumerate(m[1:], 2):
            if len(r) != len(m[0]):
                continue
            fid = r[h["Feature ID"]]
            if fid in matrix_ids:
                errors.append(f"matrix.csv row {i}: duplicate Feature ID {fid}")
            matrix_ids.add(fid)
            for col in ("Impact (1-5)", "Effort (1-5)"):
                v = r[h[col]]
                if not (v.isdigit() and 1 <= int(v) <= 5):
                    errors.append(f"matrix.csv row {i} ({fid}): {col} must be 1-5, got '{v}'")
            if r[h["Maturity"]] not in ("L0", "L1", "L2"):
                errors.append(f"matrix.csv row {i} ({fid}): Maturity must be L0/L1/L2, got '{r[h['Maturity']]}'")
else:
    errors.append("features/matrix.csv is missing")

# --- evidence ---
if os.path.exists(EVIDENCE):
    e = load(EVIDENCE)
    if check_headers(e, EVIDENCE_COLS, "evidence.csv"):
        check_no_blanks(e, "evidence.csv")
        eh = {c: i for i, c in enumerate(e[0])}
        cited = set()
        for i, r in enumerate(e[1:], 2):
            if len(r) != len(e[0]):
                continue
            fid = r[eh["Feature ID"]]
            cited.add(fid)
            if matrix_ids and fid not in matrix_ids:
                errors.append(f"evidence.csv row {i}: Feature ID {fid} not found in matrix.csv")
        for fid in sorted(matrix_ids - cited):
            errors.append(f"evidence.csv: feature {fid} has NO evidence rows (every feature needs at least one readable source)")
else:
    errors.append("features/evidence.csv is missing")

# --- theses ---
if os.path.exists(THESES):
    t = load(THESES)
    if check_headers(t, THESES_COLS, "theses.csv"):
        check_no_blanks(t, "theses.csv")
else:
    errors.append("knowledge/theses.csv is missing")

if errors:
    print("VALIDATION FAILED (" + str(len(errors)) + " problem(s)). Fix before committing:\n")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print("Validation passed: matrix.csv, evidence.csv, theses.csv are well-formed and consistent.")
