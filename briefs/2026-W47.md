# Weekly brief — 2026-W47

A five-minute read. Full detail lives in `knowledge/`, `cards/`, `ideas/backlog.md`, and `features/matrix.csv`.

## What deserves your attention

**1. An outside paper independently lands on almost exactly LayerLens's own attribution framing.** "Hard Issue, Weak Model, or Bad Run?" asks the same three-way question LayerLens's trust wall is built around (is this the task's fault, the model's fault, or just a bad run) and finds that today's trajectory-reading failure predictors barely do better than a score that never looks at the run at all — they mostly just re-measure task difficulty and model identity. [arxiv.org/abs/2611.08285](https://arxiv.org/abs/2611.08285). What changed: new this week; the cleanest external validation yet that this category system is the right one, not just a need for one.

**2. Anthropic itself published a working, cryptographic way to prove which model answered — and it costs ~80x more compute to use.** "Provable inference" lets anyone check a response came from a specific, committed model without re-running it or seeing its weights, formally proven in Lean. On a 400B-parameter model, proving costs roughly two orders of magnitude more than normal inference, and the method only covers 1,024 tokens of context and greedy decoding. [anthropic.com/research/provable-inference](https://www.anthropic.com/research/provable-inference). What changed: a frontier AI lab, not just an academic security group, is now building toward "a reviewer checks the evidence, not a badge" — exactly open question #11 — though this specific method is a research prototype, not something buildable today.

**3. Three real, named security incidents at eval/observability vendors surfaced in a single run.** Comet/Opik disclosed a flaw that exposed 29 internal API keys; a six-month-old, previously-untracked Braintrust incident (an AWS account breach exposing customer-stored AI-provider keys) came to light while following up the Comet story; and Prime Intellect disclosed its own benchmark-answer-leakage finding. [comet.com/.../security-incident-october-2026](https://www.comet.com/site/blog/security-incident-october-2026/). What changed: trust-collapse (thesis T-02) is now dominated by real operational incidents, not only adversarial research audits — and ironically, Braintrust's own breach exposed exactly the category of credential its flagship "Harbor" feature is designed to protect.

**4. "Signed is not the same as safe" showed up twice this week, from completely different directions.** A new paper demonstrates a signed, authenticated MCP tool that still conceals data-exfiltrating code past a state-of-the-art defense [arxiv.org/abs/2611.06585](https://arxiv.org/abs/2611.06585); the same week, Arize's own blog wrote "SBOMs and model signing tell you what you shipped; only behavioral evals tell you what it does." What changed: a genuine three-source convergence (an academic paper, a competitor's product blog, and a second paper on signed multi-agent handoffs) on one lesson, in one week — worth citing directly when explaining why LayerLens's trust wall is about behavior, not credentials.

**5. Multi-agent integrity failures more than doubled this run.** Five new, independent findings (apparent agreement that doesn't match agents' own private judgments; agents forced to choose between honesty, confidentiality, and finishing the task; a signed handoff defeated by corrupting the data before it was signed, not after) arrived in one week, taking thesis T-08 from 4 to 9 evidence families. None of this changes LayerLens's current single-agent-against-environment scope, but it sharpens exactly what a future multi-agent extension would need a dedicated check for.

## What changed in what we know

| Prior claim | New evidence | Current status |
|---|---|---|
| Attribution (agent/environment/grader) is a useful but mostly LayerLens-internal framing | An outside paper (C-0127) independently proposes almost the identical three-way split for coding-agent failure prediction | Strengthened: external validation that the category system itself is right, not just the need for a category system |
| Cryptographic/proof-based verification (T-09) is an early-stage research idea from academic groups | Anthropic (C-0148) and CORDE (C-0141) bring it to 4 families, including a frontier lab's own prototype with a concrete, quantified cost (~72-94x overhead) | Upgraded from "new thesis" to "strengthening" — real, but now has a believable near-term cost ceiling attached |
| "Declared isolation is not verified isolation" (T-02) was mostly about sandboxes and inference-serving side-channels | This week extends it to signed tools and signed inter-agent handoffs specifically — "signed" joins "sandboxed" and "offline" as a word that sounds safer than it is | Sharper, more citable framing for explaining the trust wall externally |
| Multi-agent scope (open Q#13) was a "documented, evidenced risk" with 4 evidence families | 5 new families arrive in one run, more than doubling the thesis | Still "do nothing (stay single-agent) is a valid conclusion," but reached with considerably more evidence now |

## One concept to understand better: "signed" and "verified" are not the same claim as "safe"

A digital signature (or a "verified" badge, or an "offline" label) tells you *who* vouched for something or *what boundary* was declared — it does not tell you the thing actually behaves the way that vouching implies. This week's clearest example: a signed MCP tool passed every authenticity check while quietly leaking data to an allowed destination, because the signature covers the tool's identity, not its runtime behavior. The same logic explains why an "offline" sandbox turned out not to be (a prior finding), why a signed inter-agent handoff was still forgeable (corrupt the data *before* signing it, and the signature just makes the corruption look official), and why SBOMs don't catch a one-neuron activation push that turns a model hostile.

**When it doesn't apply**: if the thing being signed/verified is itself the complete, final artifact being trusted (e.g., a cryptographic proof that *is* the answer, like Anthropic's provable inference or PCM's proof-carrying messages), there's no behavior left to diverge from the claim — the proof and the claim are the same object. The distinction matters specifically when a signature/badge is a proxy for something else (identity standing in for behavior, a network label standing in for actual isolation).

**Ties to LayerLens**: open question #2 (attribution) and #11 (the reviewer surface) both hinge on this distinction. LayerLens's own trust wall already behaves correctly here (it hides the seed/knobs structurally, rather than just labeling an agent "untrusted"), but it is worth an explicit design-review pass: does anything in the product ever use a credential, a signature, or a status label as a stand-in for an actual behavioral guarantee?

## Possible applications to LayerLens

**1. Memory/retrieved-content provenance (ties to open question #7 and the general context/memory scope).** Problem: nothing in a typical agent memory or multi-agent handoff pipeline records who actually said something or with what authority — an attacker-controlled source can get recorded as if the user said it, and this week's papers show signing the handoff afterward doesn't fix a corruption introduced before signing. How others solve it: label every memory entry's owner/scope/origin/authority and check it at every boundary (ClawMMU); extract requirements as verbatim, checkable predicates before signing (Signed but Not Safe). The gap: LayerLens doesn't yet have (as far as this research agent can tell) a cross-session memory capability where this risk would bite, but any future one would inherit it immediately. The assumption to test: if/when LayerLens builds memory or multi-step handoffs between system types, authorship tracking needs to be designed in from the start, not bolted on. Small test a designer could run: sketch what a "memory entry" would need to carry (not just content, but origin and authority) for one of LayerLens's own system types, and check whether today's data model has anywhere to put that information.

**2. Reviewer-facing attestation (ties to open question #11, now a strong candidate — I-0014/F-0014 promoted to L2 this run).** Problem: Riley needs to accept a claim ("this run was verified") without trusting the claimant, but attestation today is API-only with no reviewer-facing surface. How others solve it, at a spectrum of cost: a cheap tamper-evident disclosure log (CORDE, ~0.5% overhead) up to a full cryptographic proof (Anthropic's own prototype, ~80x overhead). The gap: no mechanism in this spectrum has been checked against what LayerLens's attestation API actually returns today. The assumption to test: that a lightweight, log-style mechanism (closer to CORDE than to a full zkSNARK) could give Riley something to actually look at, not just a verified badge. Small test: have someone with product access pull up today's attestation API response for a real run and sketch, in five minutes, what a reviewer-facing "check this claim" screen built directly from that response would show.

## Ideas that advanced

- **I-0013** (memory/retrieved-content provenance and authority): **promoted L1 -> L2**. Six independent sources now, across three distinct mechanisms, plus a first-party Anthropic admission of the underlying risk.
- **I-0014** (reviewer-facing attestation): **promoted L1 -> L2**. Four independent sources now, including Anthropic itself entering this space.
- **I-0001, I-0003, I-0004, I-0007, I-0008, I-0010, I-0011** all gained new evidence this run and stay at their existing maturity (L1).
- **I-0006** (consequence-naming confirmations) gained two more adjacent sources and stays at L0 — the field's own literal white space (what text a confirmation shows) remains unclaimed even as its surrounding territory keeps growing.

## Feature ranking moves

- **F-0013** (memory/provenance labeling): **L1 -> L2**, priority 0.45 -> 0.68.
- **F-0014** (reviewer-facing attestation): **L1 -> L2**, priority 0.60 -> 0.90, now the second-highest-priority item behind F-0005.
- F-0001, F-0002, F-0003, F-0006, F-0007, F-0008, F-0010, F-0011 all gained evidence this run; no maturity or priority change (see `features/matrix.csv` "What moved" column for each).

## For you

**Comprehension question**: In your own words, why doesn't signing a message (or badging something "verified") guarantee the thing it's attached to actually behaves safely? Can you name one place in LayerLens's own shipped product where a status label or a credential check currently stands in for an actual behavioral guarantee — and one place where it doesn't?

**Design exercise**: Pick one of LayerLens's shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, Gmail). Sketch, in a few bullet points, what would need to change if that system type ever carried memory or state across more than one task/session — specifically, how would you record *who* said something (the real user vs. a record the agent read) alongside *what* was said?

## Coverage and gaps

Reviewed in full: the never-before-processed W46 harvest across all five inboxes (176 arXiv papers, the discovery trend radar, 6 fulltext files, 16 competitor teams, 11 reference sources). Read directly in full via WebFetch: two Anthropic posts and one Microsoft Research post. Followed up via WebSearch: Prime Intellect's own audit post, Comet's security incident, a deliberate T-01 contradicting-evidence search (found none, again), and a follow-up that surfaced the previously-untracked Braintrust incident.

Inaccessible or incomplete this run: Prime Intellect's and Braintrust's own first-party pages (both domain-blocked, as every prior run) — both incidents rest on secondary coverage, not primary text. The `inbox/fulltext/` abstract-page-scrape bug (flagged in `SOURCES.md` for several weeks now) persists for the two newest files fetched this run. Pending: a primary-source check on "On Randomness in Agentic Evals" (found via WebSearch only) before its specific numbers are cited externally.

This was not the first run of the month (that was 2026-11-02), so no monthly synthesis section this week.
