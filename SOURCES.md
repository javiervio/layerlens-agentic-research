# Sources

Where the agent looks. A seed list, not a cage. The agent should follow citations backward and forward and add new authors and organizations when they bring real evidence, always recording the channel that surfaced them.

## Network reality in the cloud sandbox (read this first)

The weekly run happens in a cloud sandbox with a restricted network (a current platform limitation as of late September 2026, not a choice of ours). Work with it, do not fight it:

- **WebSearch works** and returns real content and summaries. Treat it as the primary tool for BOTH discovery and first-pass reading.
- **WebFetch reliably reaches:** github.com, raw.githubusercontent.com, anthropic.com, microsoft.com, plus package registries and major version-control and cloud hosts.
- **WebFetch is blocked for** arxiv.org (all paths), huggingface.co, wikipedia, modelcontextprotocol.io, and most vendor blogs — confirmed as of 2026-09-29 to also include alphaxiv.org, pith.science, www.braintrust.dev (blocked three runs running), e2b.dev (blocked again), www.primeintellect.ai/docs.primeintellect.ai (blocked again), modal.com, and newly confirmed this run: arize.com and www.browserbase.com. GitHub repos remain the reliable workaround: several arXiv papers this run had a companion GitHub repo (README with the paper's own numbers) that was fully reachable even though the paper's own arxiv.org page was not — always check for one before marking a source incomplete access.
- **Escalation note (2026-09-29)**: www.braintrust.dev has now been WebFetch-blocked three consecutive runs (2026-09-25, -28, -29), and richer WebSearch queries return the same secondary-summary depth each time (diminishing returns). Per this file's own "links Javier saved" allowance, the next step for Braintrust specifically is to ask Javier whether he has an authorized/saved link, rather than repeating the same WebSearch pattern indefinitely.
- **Newly confirmed blocked this run (2026-09-29, pass 3)**: mlflow.org, openrouter.ai, deepeval.com, www.honeyhive.ai, www.oreilly.com — all blocked while trying to directly read vendor coverage of "Jev" (TypeSafe AI). This continues the pattern: individual vendor blogs/docs are broadly blocked, but their GitHub repos (github.com/TypeSafeAI/jev-harness, github.com/dataelvisliang/jev-as-a-judge-scaffold) were fully reachable and gave richer primary content than any blocked page would have. Keep checking GitHub first for any new vendor or paper before marking incomplete access.
- **2026-10-05 update**: `eunomia.dev` newly confirmed EGRESS_BLOCKED (a blog covering the ACRFence paper). `github.com/ChaokunChang/crab` (an arXiv paper's companion repo) was fully reachable and gave a complete, detailed README — once again, check GitHub first. **Braintrust escalation resolved in the negative**: this run re-tried `www.braintrust.dev` directly via the exact link already saved in this file's "Saved links" section below — still EGRESS_BLOCKED. This confirms the block is a whole-domain sandbox network-policy block, not a login/paywall a saved link can route around. Braintrust coverage will stay titles-only (via the competitor-inbox harvester, which runs outside this sandbox) until/unless the sandbox's own egress allowlist changes — stop re-trying the saved link every run; it is not going to behave differently. **Harvester cron-trigger gap (2026-10-05)**: the three GitHub Actions harvesters (`arxiv-harvest.yml`, `competitor-harvest.yml`, `reference-harvest.yml`) are each configured with a Monday cron schedule, but checking `mcp__github__actions_list` for each workflow shows every run to date was a manual `workflow_dispatch` (from initial setup, 2026-09-28/29) — none has a `schedule`-triggered run yet, including this morning, the first Monday since they were set up. The inboxes are accordingly six days stale. This is an infra issue for Javier to check (did the cron fire and get recorded oddly, or did it simply not fire?), not something a research pass can fix; this run fell back to live WebSearch/WebFetch per this file's own guidance for an unreachable family.

**The inboxes (primary fix for the egress block):** GitHub Actions harvesters run on GitHub's own runners (full internet) before each Monday run and commit content the cloud sandbox cannot fetch:
- `inbox/arxiv/LATEST.md` (`tools/arxiv_harvest.py`): recent, relevance-filtered arXiv papers with verbatim abstracts and canonical links.
- `inbox/competitors/LATEST.md` (`tools/competitor_harvest.py`): recent posts from the 17-company competitor watchlist (feeds + sitemaps), plus a coverage note for any with no feed.
- `inbox/reference/LATEST.md` (`tools/reference_harvest.py`): recent posts from frontier-lab blogs (OpenAI, Google DeepMind, Google Research, Microsoft Research, Hugging Face, Anthropic) and high-signal analysts (Interconnects, Import AI, Simon Willison, Latent Space). Curated for signal, not volume.

Read ALL THREE inboxes first: they are directly-read primary text, not search summaries, and need no blocked fetch. They do not replace the four angles, they seed research and competitor coverage reliably so a run is never arxiv-only. Social (LinkedIn, X) has no harvester (those sites block automated fetch); cover it best-effort via WebSearch and log the gap honestly. For full text of a specific source, hand it to a local deep-read session.

How to read deeply anyway, in priority order:
1. Read the arXiv inbox (`inbox/arxiv/LATEST.md`), then discover more with WebSearch.
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

Some entries below are inferred from LayerLens's own moat and persona docs (which name Braintrust, LangSmith, Opik, Databricks, Galileo, Vals AI) plus obvious peers; Javier should prune or add. "auto" = the harvester pulls its blog/changelog via feed or sitemap; "WebSearch" = no harvestable blog path, covered via search.

| Entity | Category | Harvest | What to investigate |
|---|---|---|---|
| Braintrust | Evaluation / observability | auto (sitemap) | Comparing experiments and runs, sandboxed evals, sharing |
| Arize | Evaluation / observability | auto (feed) | Moving from detected problems to criteria, tests, decisions |
| Galileo | Evaluation / observability | auto (sitemap) | Agent eval, guardrails, how they frame reliability |
| Comet / Opik | Evaluation / observability | auto (feed) | Open-source eval, tracing, judge/scorer approach |
| Databricks | Eval platform (Mosaic AI Agent Eval) | auto (feed, broad) | Agent evaluation inside a data platform |
| Patronus AI | Evaluation / guardrails | auto (sitemap) | Automated eval, hallucination/safety scoring |
| Humanloop | Evaluation / prompt ops | auto (sitemap) | Eval workflows, human feedback |
| Confident AI (DeepEval) | Open-source eval | auto (sitemap) | Metrics, judges, test-style evals |
| Langfuse | Tracing / eval (open source) | WebSearch | Tracing, datasets, eval; verify blog/changelog path |
| Vals AI | Independent model/agent evals | WebSearch | Named "most dangerous" in the moat doc; independent benchmarking. First real read 2026-10-05: ~30 independent benchmarks (legal/finance/healthcare/coding/math), a GDP-weighted "Vals Index," published cost+accuracy+latency methodology — see `knowledge/competitive.md` |
| LangChain / LangSmith | Agent framework + eval platform | WebSearch (flagged "NO FEED OR SITEMAP FOUND" by the competitor harvester; was missing from this table entirely until 2026-10-05, despite being named in LayerLens's own moat doc — added as a standing gap-closure) | Multi-turn trajectory evals, auto-categorized failure insights (Insights Agent), side-by-side experiment comparison. First real read 2026-10-05, search-summary only — see `knowledge/competitive.md` |
| E2B | Sandbox infrastructure | auto (feed) | Sandbox lifecycle, tool integration, session continuity |
| Browserbase | Web execution and interaction | auto (sitemap) | Latency, developer experience, what they measure |
| Daytona | Agent sandbox infrastructure | auto (feed) | Sandbox lifecycle, dev environments for agents |
| Runloop | Agent sandbox infrastructure | auto (sitemap) | Sandboxes, benchmarking harnesses |
| Prime Intellect | Training and environments | auto (sitemap) | Environment construction, verification, RL sandboxes |
| Modal | Infrastructure | auto (sitemap) | Coordination of training, execution, environments; bottlenecks |
| TypeSafe AI | Judge/decision-model infra (new, 2026-09-29) | WebSearch (no feed/sitemap checked yet) | Decision-only "System One" judge (Jev), confidence-cascade escalation to LLM judges; independently adopted by Arize/Confident AI/Langfuse/Browserbase within one week — see `knowledge/competitive.md` |

The competitor harvester (`tools/competitor_harvest.py`) tries each source's RSS/Atom feed first, then falls back to its **sitemap.xml** for feedless sites (this reaches Braintrust, Browserbase, Modal, and Prime Intellect blogs/changelogs, which have no feed). Only sources with neither are logged "cover via WebSearch."

## Social / X (all companies)

X (Twitter) is a good, timely source for every company here. The harvester cannot pull it (X requires auth, blocks automated fetch, and scraping is against its terms), so **social is WebSearch best-effort**: each run, for the rotation's companies, WebSearch their recent public posts and record what was reachable vs not (never claim full coverage of X). For each watchlist company, find and verify its official X handle from its own site, then record it here as you confirm it.

### Saved links (provided by Javier, use directly)

- Braintrust blog: https://www.braintrust.dev/blog
- Braintrust X: https://x.com/braintrust/highlights

Note: earlier planning material referenced a project called "OpenClaw" and some specific vendor posts and paper ids. Those were not independently verified and must not be treated as real until confirmed by a reachable canonical source.

## Evidence labels (use on every claim)

- **Documented capability**: an official source states a product behavior. Check version and access.
- **Bounded empirical evidence**: a study describes method and results for specific conditions.
- **Independent corroboration**: different groups give compatible evidence (confirm they are not the same experiment).
- **Proposal or interpretation**: a framework, position, or our own inference.
- **Anecdotal signal**: a single reported experience. Useful to investigate, not to prove prevalence.
- **Incomplete access**: only abstract, fragment, or a secondary reference was available.
