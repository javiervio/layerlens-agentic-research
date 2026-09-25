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
