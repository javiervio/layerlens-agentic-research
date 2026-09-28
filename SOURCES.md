# Sources

Where the agent looks. A seed list, not a cage. The agent should follow citations backward and forward and add new authors and organizations when they bring real evidence, always recording the channel that surfaced them.

## Network reality in the cloud sandbox (read this first)

The weekly run happens in a cloud sandbox with a restricted network (a current platform limitation as of late September 2026, not a choice of ours). Work with it, do not fight it:

- **WebSearch works** and returns real content and summaries. Treat it as the primary tool for BOTH discovery and first-pass reading.
- **WebFetch reliably reaches:** github.com, raw.githubusercontent.com, anthropic.com, microsoft.com, plus package registries and major version-control and cloud hosts.
- **WebFetch is blocked for** arxiv.org (all paths), huggingface.co, wikipedia, modelcontextprotocol.io, and most vendor blogs.

How to read deeply anyway, in priority order:
1. Discover with WebSearch.
2. To actually read a source, prefer a **reachable mirror**: an arXiv paper almost always has a companion **GitHub repo** (README, docs, sometimes the full text) that IS reachable; a tool or protocol usually has its repo and docs on GitHub; Anthropic and Microsoft pages can be fetched directly.
3. If the only thing available is a WebSearch summary and no reachable original exists, that is **incomplete access**. Label the claim and the card accordingly per `PROTOCOL.md`, do not describe methods or results you could not open, and **still record the canonical link** (for example the arxiv.org URL) so Javier can open it himself.

Never mark a blocked fetch as a run failure. It is an expected constraint; route around it and report coverage honestly in the run log.

## Discovery must combine four angles

Do not rely on a single search. Every run should mix:
1. **Category feeds and searches** (arXiv, below).
2. **Named team channels** (docs, changelogs, engineering blogs, status pages).
3. **Citations** (what a strong paper cites, and what cites it).
4. **Public posts** from identified people and teams (with permalinks and verified affiliation).

## arXiv categories

Search across, not only the latest week (foundations are often older):
`cs.MA` (multiagent systems, directly on-topic), `cs.AI`, `cs.CL`, `cs.HC`, `cs.LG`, `cs.DC`, `cs.OS`, `cs.SE`.

The cs.MA recent listing is a high-signal feed to watch: https://arxiv.org/list/cs.MA/recent

Feeds (for reference; verify before relying on any as a live connector):
- https://rss.arxiv.org/rss/cs.AI
- https://rss.arxiv.org/rss/cs.CL
- https://rss.arxiv.org/rss/cs.HC
- https://rss.arxiv.org/rss/cs.LG

## Search vocabulary

Use as building blocks, adapt syntax to the search tool. Search by problem, not by lab name.

| Area | Terms |
|---|---|
| Environments | agent environment, stateful sandbox, agentic training infrastructure, environment generation, executable environment, task feasibility, world simulation |
| Infrastructure | sandbox lifecycle, microVM, snapshot, pause resume, provisioning, environment reproducibility, rollout orchestration |
| Evaluation | agent evaluation, trajectory, outcome verification, benchmark contamination, reward hacking, reproducibility, run comparability |
| UX and control | human-agent interaction, co-planning, intervention, oversight, recovery, agent observability, handoff, failure attribution |
| Synthetic data | synthetic trajectories, user simulation, scenario generation, diversity, validation, distribution shift, model collapse |
| Context and memory | agent memory, context engineering, retrieval, stale memory, long-horizon agents |
| Integration | MCP, AG-UI, A2A, tool calling, structured state, streaming events |
| Team experience | lessons learned, postmortem, incident, bottleneck, what broke, tradeoffs, migration, release notes |

Keep roughly 20% of the search budget for evidence that could contradict what we currently believe, or that comes from an adjacent field. This is a deliberate guard against an echo chamber.

## Reference points and benchmarks (verify each)

- WebArena, tau-bench, tau2-bench (reproducible task environments with simulated users and domain policies).
- Anthropic engineering writing on building agents, context engineering, and evaluating agents.
- Microsoft HAX guidelines and Magentic-UI (human/agent interaction research).
- MCP (https://modelcontextprotocol.io), AG-UI (https://docs.ag-ui.com), A2A (https://a2a-protocol.org).

## Teams and companies to watch (seed list, confirm relevance)

Framed as "possible reference or competitor, pending our context." For each, find from their official site: docs, changelog, repo, status page, engineering blog, and public social. Record which exist and which were reachable this run.

| Entity | Why it might matter | What to investigate |
|---|---|---|
| Braintrust | Evaluation and observability | How they compare experiments and runs, sandboxed evals, sharing |
| Arize | Evaluation and observability | Moving from detected problems to criteria, tests, decisions |
| E2B | Sandbox infrastructure | Sandbox lifecycle, tool integration, session continuity |
| Browserbase | Web execution and interaction | Latency, developer experience, what they measure |
| Prime Intellect | Training and environments | Environment construction, verification, RL sandboxes |
| Modal | Infrastructure | Coordination of training, execution, environments; bottlenecks |

Note: earlier planning material referenced a project called "OpenClaw" and some specific vendor posts and paper ids. Those were not independently verified and must not be treated as real until confirmed by a reachable canonical source.

## Evidence labels (use on every claim)

- **Documented capability**: an official source states a product behavior. Check version and access.
- **Bounded empirical evidence**: a study describes method and results for specific conditions.
- **Independent corroboration**: different groups give compatible evidence (confirm they are not the same experiment).
- **Proposal or interpretation**: a framework, position, or our own inference.
- **Anecdotal signal**: a single reported experience. Useful to investigate, not to prove prevalence.
- **Incomplete access**: only abstract, fragment, or a secondary reference was available.
