# Learning log

Your running record of building fluency in agentic environments. The agent adds a concept and an exercise each week; you add your own explanation in your words. A topic is only "learned" when you can explain it and say when it does not apply, not when a document was generated.

---

## Self-preference bias in LLM-as-judge

- **Plain explanation** (from the brief): When a model judges two answers and one was written by a model in its own family, the judge tends to score that answer higher — not because it's actually better, but because of some family resemblance the judge responds to. Surprisingly, this happens even when the judge can't reliably tell which answer is its own: the bias doesn't require self-recognition.
- **Example / counterexample**: In a pilot study, GPT-4o rated its own family's answers 0.21 points higher (on the study's Self-Preference Index) than a neutral panel would have; Claude Sonnet 4.6 and Claude Haiku 4.5 both showed +0.14. Counterexample/boundary: this was measured only on open-ended prompts with no objective ground truth — it hasn't been shown to hold the same way on verifiable tasks with a real answer key.
- **When it does not apply**: Deterministic, answer-key-graded tasks (LayerLens's "Graders"), where there's no subjective judgment call for a bias to act on in the first place. It's specifically a caution about the Judges/Scorers grader types.
- **This week's exercise**: Sketch (on paper or in words) what a "same-family judge" warning could look like in the Optimize or Insights/Evidence screen — where would it appear, and would it block anything or just inform?

**Your explanation in your own words** (you fill this):

**What you would look for in LayerLens** (you fill this):

**Level**: pending.

---

## pass@k versus pass^k (agent reliability)

- **Plain explanation** (from the brief): pass@k asks "does at least one of k attempts succeed" — a capability question, fine when you can discard the failures and keep the one that worked. pass^k asks "do all k attempts succeed" — a reliability question. An agent can score high on the first and low on the second at once: it can usually find *a* way to succeed while still being unpredictable on any single try.
- **Example / counterexample**: an agent that independently succeeds 80% of the time has pass@5 near 100% (very likely at least one of five works) but pass^5 around 33% (0.8^5) — all five succeeding is a much higher bar. That gap between the two numbers is the reliability problem, made concrete. Counterexample/boundary: if an agent's failures are correlated (it fails the exact same way every time, not randomly), pass@k and pass^k stop being simple powers of a single success rate — the independent-trials arithmetic above is a simplification worth checking against real repeated-run data, not a universal formula.
- **When it does not apply**: pass@k is the right lens when only one good outcome is needed and the rest can be thrown away (e.g. sample several drafts, a human picks the best). It's the wrong lens whenever every single run has to be trusted unsupervised — which is closer to how a real agent, or a LayerLens environment run, gets used in production.
- **This week's exercise**: Sketch (words or paper) what a pass^k-style reliability indicator could look like next to a run's score in LayerLens's Runs or Insights/Evidence view — a second number, a range, a small sparkline of k repeats? What's the smallest version that's still honest?
- **Source status**: the paper that proposed this distinction ("Towards a Science of AI Agent Reliability," arXiv:2602.16666) was only reachable via search summary this run (arxiv.org and mirrors were blocked) — the concept itself is solid arithmetic, but the paper's specific findings (15 models, "only small reliability improvements despite capability gains") are not yet independently confirmed. See `cards/ai-agent-reliability-science.md`.

**Your explanation in your own words** (you fill this):

**What you would look for in LayerLens** (you fill this):

**Level**: pending.

---

## reliability@k versus (broken) pass@k: what counts as "one try"?

- **Plain explanation** (from the brief): Last week's pass@k vs pass^k distinction assumed you already know how to count "k tries." This week found a sharper problem underneath: some benchmarks count k by treating unit tests *inside one submission* as if they were separate independent attempts, instead of counting genuinely independent full-task rollouts. That's like grading a single exam attempt by counting each question as a separate "try" — it makes a shaky result look far more consistent than it is.
- **Example / counterexample**: on real SWE-bench tasks, the mean hidden-test pass rate (fraction of individual tests passing, averaged) was 0.80 — looks strong. The strict resolve rate (did the whole task get solved correctly, as one real attempt) was 0.20 for the same runs — a 4x difference, purely from how "k" got counted. Counterexample/boundary: this specific trap only bites when a benchmark reports a "pass@k"-style number built from sub-results within one run; a benchmark that always reports single-attempt pass/fail has nothing to miscount.
- **When it does not apply**: if LayerLens (or anyone) only ever reports single-attempt, single-task outcomes with no k involved, this exact trap doesn't apply — but the moment a "how often does this agent succeed" number gets built from repeated attempts, this is the first thing to check.
- **This week's exercise**: pick one of LayerLens's shipped system types (Salesforce, Linear, SEC EDGAR, Stripe, or Gmail) and sketch, in words, what its 2-3 most common tool-call error messages probably look like today. For each, note whether an agent reading it could act on it directly (e.g. names a specific tool to call), or whether it reads like it was written for a human developer (e.g. "check your API key in the dashboard").
- **Source status**: the correction itself was read directly via a companion GitHub repo (github.com/nv78/Research-CodeBench); the underlying arXiv paper (2608.14711) was not opened directly (arxiv.org blocked) and author identities are not independently confirmed. Treat the mechanism and the qualitative direction as solid; treat the specific numbers as reported-by-the-repo, not independently re-derived. See `cards/reliability-at-k-vs-misapplied-pass-at-k.md`.

**Your explanation in your own words** (you fill this):

**What you would look for in LayerLens** (you fill this):

**Level**: pending.
