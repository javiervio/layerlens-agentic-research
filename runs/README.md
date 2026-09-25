# Run logs

One file per run, named `YYYY-MM-DD.md`. The honest record of what each run actually did, so "no findings" can be told apart from "did not look." The agent writes these per `AGENT_RUNBOOK.md`.

## Template

```
# Run <YYYY-MM-DD>

- run_id:
- previous_state_read: yes/no
- sources_reviewed:
- sources_failed (with reason):
- candidates_considered:
- cards_created:
- claims_changed:
- brief_written: yes/no
- pending_for_next_run:
- final_status: complete | partial | failed | no relevant findings
- push_succeeded: yes/no
```
