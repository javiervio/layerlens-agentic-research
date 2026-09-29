#!/usr/bin/env python3
"""
Weekly health check. Runs on a GitHub Actions runner and detects the SILENT
failures of the research system, the ones nobody would otherwise notice:

  - the weekly research run didn't happen (routine missed or failed to push)
  - a harvester inbox went stale or empty (feed/sitemap rot)
  - the Google Sheet's GitHub token is near expiry (sheet sync about to die)
  - LAYERLENS_CONTEXT.md hasn't been reviewed in a long time (applied output drifting)

Prints problems and exits 1 if any (the workflow then opens or updates a GitHub
issue, which emails the owner). Exits 0 and stays silent when healthy. Stdlib only.
"""
import subprocess, datetime, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today()
problems = []

def days_since(d):
    return (TODAY - d).days

def parse_iso(s):
    try:
        return datetime.date.fromisoformat(s[:10])
    except Exception:
        return None

# 1) Did a weekly research run land recently? Every run writes a runs/ log + a brief.
try:
    out = subprocess.check_output(
        ["git", "-C", ROOT, "log", "-1", "--format=%cI", "--", "runs/"],
        text=True).strip()
    last = parse_iso(out)
    if not last:
        problems.append("Could not determine the date of the last research run (no runs/ history found).")
    elif days_since(last) > 8:
        problems.append(f"No research run has committed to runs/ in {days_since(last)} days (last: {last}). The Monday routine may have missed or failed. Check https://claude.ai/code/routines/trig_01VZQffqF88D83eqbrTAy8my")
except Exception as e:
    problems.append(f"Health check could not read git history: {e}")

# 2) Are the three harvester inboxes fresh and non-empty?
INBOXES = {
    "arxiv": "inbox/arxiv/LATEST.md",
    "competitors": "inbox/competitors/LATEST.md",
    "reference": "inbox/reference/LATEST.md",
}
for name, rel in INBOXES.items():
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        problems.append(f"Inbox '{name}' is missing ({rel}). Its harvester workflow may be broken.")
        continue
    text = open(p, encoding="utf-8").read()
    m = re.search(r"fetched (\d{4}-\d{2}-\d{2})", text)
    d = parse_iso(m.group(1)) if m else None
    if not d:
        problems.append(f"Inbox '{name}' has no readable 'fetched' date; harvester output may be malformed.")
    elif days_since(d) > 8:
        problems.append(f"Inbox '{name}' is stale (last fetched {d}, {days_since(d)} days ago). Its harvester workflow may be failing.")
    entries = text.count("- link:")  # every harvester writes one "- link:" per entry
    if entries == 0 and name in ("arxiv", "competitors"):
        problems.append(f"Inbox '{name}' has 0 entries; every source may have stopped resolving (feed/sitemap rot).")

# 3) GH_TOKEN (Google Sheet sync) expiry reminder. Update this date when the token is rotated.
#    Fine-grained PAT created ~2026-09-29 with a 90-day expiry.
TOKEN_EXPIRY = datetime.date(2026, 12, 28)
dleft = (TOKEN_EXPIRY - TODAY).days
if dleft <= 10:
    problems.append(f"The Google Sheet's GitHub token (GH_TOKEN) expires around {TOKEN_EXPIRY} ({dleft} days). "
                    "Rotate it: create a new fine-grained read-only PAT for this repo, paste it into the sheet's "
                    "Apps Script > Project Settings > Script properties (GH_TOKEN), and update TOKEN_EXPIRY in this file.")

# 4) Is LAYERLENS_CONTEXT.md stale? Everything applied to LayerLens rests on it.
ctx = os.path.join(ROOT, "LAYERLENS_CONTEXT.md")
if os.path.exists(ctx):
    m = re.search(r"CONTEXT_REVIEWED:\s*(\d{4}-\d{2}-\d{2})", open(ctx, encoding="utf-8").read())
    d = parse_iso(m.group(1)) if m else None
    if not d:
        problems.append("LAYERLENS_CONTEXT.md has no CONTEXT_REVIEWED marker; cannot tell if it is current.")
    elif days_since(d) > 60:
        problems.append(f"LAYERLENS_CONTEXT.md was last reviewed {d} ({days_since(d)} days ago). "
                        "Confirm or correct it, then bump the CONTEXT_REVIEWED date. Applied hypotheses drift when this goes stale.")

if problems:
    print("RESEARCH SYSTEM HEALTH: problems found\n")
    for p in problems:
        print("- " + p)
    sys.exit(1)
print("RESEARCH SYSTEM HEALTH: all clear.")
