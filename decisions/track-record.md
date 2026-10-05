# Track record

Every substantive call the system makes, logged when made and scored when reality answers. This is what makes recommendations auditable instead of asserted. A refuted call stays on the books; calibration comes from honesty, not from a clean sheet.

Schema per call: id, date made, the call (specific and falsifiable), basis (evidence at the time), horizon (when to score it), status (open / confirmed / refuted / partially confirmed / expired), outcome note with date.

---

## R-0001
- **Date**: 2026-09-29
- **Call**: F-0003 (tradeoff axis beside every comparison score) is the current top build candidate; it will hold or grow its lead as evidence accumulates, because comparison-honesty evidence keeps arriving.
- **Basis**: two independent sources (tau2-bench incident C-0003, HAL design C-0009); low effort on existing data.
- **Horizon**: 2026-12 (quarterly review).
- **Status**: **partially confirmed / off-track (scored early, 2026-Q4 review, 2026-10-05)**: F-0003's own evidence base has not grown (still 2 sources, priority steady at 1.20), but it did **not** hold the top rank — F-0005 overtook it within the same week the call was made (same-family judge bias was independently corroborated, jumping F-0005's priority 0.90 to 1.80). The "will hold or grow its lead" half of the call is refuted in direction, even though the underlying "comparison-honesty evidence keeps arriving" premise was correct for F-0003 specifically, just not fast enough to defend the #1 rank against a faster-moving sibling thesis. Scoring this honestly now rather than waiting for the full horizon, since the outcome is already legible. Horizon formally still 2026-12 for the "holds a top-3 slot" weaker version, which still looks likely to confirm (F-0003 remains rank 2).

## R-0002
- **Date**: 2026-09-29
- **Call**: Thesis T-01 (reliability overtaking capability) will strengthen: at least two more independent evidence families will arrive by year end.
- **Basis**: three families already (C-0003, C-0008, C-0009); ICML visibility tends to produce follow-on work.
- **Horizon**: 2026-12.
- **Status**: **CONFIRMED (2026-Q4 review, 2026-10-05)**: well ahead of the year-end horizon, T-01 now rests on six independent families (added C-0013, C-0015, and C-0019 since the call was made) with no counter-evidence recorded. Closing this call as confirmed rather than leaving it open to the original horizon, since the bar has already been cleared twice over.

## R-0003
- **Date**: 2026-09-29
- **Call**: Consequence-legibility (T-04 / F-0006) is genuine white space: no major agent product will have shipped consequence-naming confirmations before Stratix could.
- **Basis**: direct read of the field leader's docs (C-0011) plus a null search result; explicitly thin, that is why it is a call and not a fact.
- **Horizon**: 2027-03.
- **Status**: open — no movement this quarter (T-04 unchanged, F-0006 still L0, single source). Not yet re-searched directly this quarter; worth a dedicated search in Q1 2027 rather than passive waiting, since "no one has built it" is weak evidence by construction (absence of evidence).

## R-0004
- **Date**: 2026-09-29
- **Call**: F-0005 (flag same-family judge/agent pairings) belongs near the top of the build list: cheap (Effort 1), now evidence-backed (thesis T-05), and it will survive to a real decision rather than being dropped.
- **Basis**: two independent evidence families (C-0002 pilot + C-0014 12-model study) promoted N-02 to thesis T-05; priority rose 0.90 to 1.80, now rank 1 by score.
- **Horizon**: 2026-12 (quarterly review).
- **Status**: **tracking-confirmed (2026-Q4 review, 2026-10-05)**: F-0005 has held rank 1 by priority score every week since the call, and T-05 gained a third independent family (C-0027, 21-judge systematic study) in the interim, strengthening rather than weakening the basis. Still open to the full horizon pending Javier's actual build decision (a score rank is not the same as a decision), but trending to confirm.

## R-0005
- **Date**: 2026-10-05 (Q4 2026 decision brief)
- **Call**: Environment-lifecycle convergence (T-06) will keep splitting cleanly into a "local sandbox state" branch that commoditizes across more vendors (more teams will publish near-100%-recovery or millisecond-latency local checkpoint/rollback within two quarters) and a "remote/external state" branch that stays substantially unsolved and risk-laden (no team will publish a demonstrated-safe, general solution to the ACRFence attack classes within the same window).
- **Basis**: ten independent evidence families now in T-06, with the clearest recent split yet — Crab and DeltaBox (local, strong quantitative results) versus ACRFence and "Safe to Resume?" (remote, demonstrated attacks, no general fix yet) plus one proposed-but-unvalidated governance-layer design (C-0034).
- **Horizon**: 2027-04 (two quarters).
- **Status**: open.

## R-0006
- **Date**: 2026-10-05 (Q4 2026 decision brief)
- **Call**: I-0008 (ground truth for user-built/imported worlds) will still have zero external research corroboration by the next quarterly review (2027-01), because it was internally derived from a single conversation and the search terms that would surface it are generic enough to have already been tried incidentally across several runs without a hit.
- **Basis**: I-0008 has been L0 since 2026-09-29 with no change across six subsequent weekly passes; no dedicated search for it has been run, but it has not surfaced incidentally either.
- **Horizon**: 2027-01.
- **Status**: open. **Recommendation accompanying this call (see decisions/2026-Q4.md)**: park active pursuit of external corroboration for I-0008 until a real user-need signal arrives, rather than continuing to carry it as a search target with no hits.
