# Competitor / team harvest 2026-W46 (fetched 2026-11-09)

Recent posts from competitor and reference-team blogs, pulled from their RSS/Atom feeds by a GitHub Actions runner (the cloud research sandbox cannot reach these directly). Read this alongside inbox/arxiv/. Sources with no feed are listed so you cover them via WebSearch and log the gap honestly.

## Coverage this run
- Braintrust: 6 posts via https://www.braintrust.dev/sitemap.xml (sitemap fallback; titles fetched per page)
- Arize: 6 posts via https://arize.com/blog/feed/
- E2B: 6 posts via https://e2b.dev/rss.xml
- Browserbase: 6 posts via https://www.browserbase.com/sitemap.xml (sitemap fallback; titles fetched per page)
- Modal: 6 posts via https://modal.com/sitemap.xml (sitemap fallback; titles fetched per page)
- Prime Intellect: 6 posts via https://www.primeintellect.ai/sitemap.xml (sitemap fallback; titles fetched per page)
- LangChain / LangSmith: NO FEED OR SITEMAP FOUND (cover via WebSearch; home https://blog.langchain.com/)
- Galileo: 6 posts via https://galileo.ai/sitemap.xml (sitemap fallback; titles fetched per page)
- Comet / Opik: 6 posts via https://www.comet.com/blog/feed
- Databricks: 6 posts via https://www.databricks.com/rss.xml
- Patronus AI: 6 posts via https://www.patronus.ai/sitemap.xml (sitemap fallback; titles fetched per page)
- Humanloop: 6 posts via https://humanloop.com/sitemap.xml (sitemap fallback; titles fetched per page)
- Confident AI (DeepEval): 6 posts via https://www.confident-ai.com/sitemap.xml (sitemap fallback; titles fetched per page)
- Langfuse: 6 posts via https://langfuse.com/sitemap.xml (sitemap fallback; titles fetched per page)
- Vals AI: NO FEED OR SITEMAP FOUND (cover via WebSearch; home https://www.vals.ai)
- Daytona: 6 posts via https://www.daytona.io/rss.xml
- Runloop: 6 posts via https://www.runloop.ai/sitemap.xml (sitemap fallback; titles fetched per page)

## Braintrust
Source: https://www.braintrust.dev/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://www.braintrust.dev/blog

### Understand how agents use your MCP server
- date: 2026-11-05
- link: https://www.braintrust.dev/blog/mcp-tracing

### The Trace Lake
- date: 2026-11-03
- link: https://www.braintrust.dev/blog/trace-lake

### Run evals 50% cheaper with workflow evals
- date: 2026-10-15
- link: https://www.braintrust.dev/blog/workflow-evals

### Application logs and agent traces in one view
- date: 2026-10-08
- link: https://www.braintrust.dev/blog/application-logs

### Optimizing coding agent usage and costs
- date: 2026-10-07
- link: https://www.braintrust.dev/blog/coding-agent-insights

### Faster queries for debugging production agents with Nitro
- date: 2026-09-24
- link: https://www.braintrust.dev/blog/nitro

## Arize
Source: https://arize.com/blog/feed/ | Home: https://arize.com/blog/

### Is the cheap model good enough? How to test a new model in your agent
- date: Thu, 05 Nov 2026
- link: https://arize.com/blog/how-to-test-a-new-model-in-your-agent/

A paper called GVS5H claims a cheap model in a manager/worker loop closes the gap to frontier models. I tested that against Opus 5.5 in my own agent, step by step: traces, evals, a dataset built from the traces and experiments, then compared pass rate, cost per solved problem and latency.
The post Is the cheap model good enough? How to test a new model in your agent appeared first on Arize AI.
### Arize Phoenix now updates model prices automatically
- date: Mon, 02 Nov 2026
- link: https://arize.com/blog/phoenix-automatic-model-pricing-updates/

Keep built-in model prices up to date with automatic catalog updates between Phoenix releases.
The post Arize Phoenix now updates model prices automatically appeared first on Arize AI.
### Evil Qwen and activation steering: why SBOMs aren’t enough
- date: Fri, 30 Oct 2026
- link: https://arize.com/blog/evil-qwen-activation-steering/

A one-neuron push turns Qwen3.5-4B hostile. At half strength it still does the sums and writes code, and it stops refusing. SBOMs and model signing tell you what you shipped. Only behavioral evals tell you what it does.
The post Evil Qwen and activation steering: why SBOMs aren&#8217;t enough appeared first on Arize AI.
### I put a ghost in Claude Code. Then I evaluated it.
- date: Tue, 27 Oct 2026
- link: https://arize.com/blog/i-put-a-ghost-in-claude-code-then-i-evaluated-it/

I built a Halloween Claude Code mod that grades each turn as a treat or a trick and blocks dangerous commands, then traced and evaluated it with Arize AX.
The post I put a ghost in Claude Code. Then I evaluated it. appeared first on Arize AI.
### A web page talked our agent into leaking a stranger’s data. Here’s how we caught it.
- date: Mon, 26 Oct 2026
- link: https://arize.com/blog/indirect-prompt-injection-ai-agents/

A web page told our support agent to look up a different customer, and the agent complied on 28 of 100 runs. Here's how we found the leak in an Arize Phoenix trace, blocked it with a scope guardrail, and set up an Arize AX monitor on the injection rate.
The post A web page talked our agent into leaking a stranger&#8217;s data. Here&#8217;s how we caught it. appeared first on Arize AI.
### How to build a software factory that tests its own prompts
- date: Thu, 22 Oct 2026
- link: https://arize.com/blog/how-to-build-a-software-factory-that-tests-its-own-prompts/

A small software factory that turns GitHub issues into released code, traces every station to Arize AX, and uses the verdicts it already produces to test and improve its own prompts before they go live.
The post How to build a software factory that tests its own prompts appeared first on Arize AI.
## E2B
Source: https://e2b.dev/rss.xml | Home: https://e2b.dev/blog

### Introducing E2B Workload Identity
- date: Tue, 03 Nov 2026
- link: https://e2b.dev/resources/introducing-e2b-workload-identity

Give each sandbox a signed identity so your backend can verify who is calling and decide what it can access, without distributing long-lived credentials.
### How E2B Uses Its Own Sandboxes to Develop E2B with AI
- date: Mon, 02 Nov 2026
- link: https://e2b.dev/resources/how-e2b-uses-its-own-sandboxes-to-develop-e2b-with-ai

Claude agents work E2B's backlog inside E2B sandboxes: an architect writes the work package, an engineer builds it, AI reviews it and a person signs off before production.
### How Niteshift Runs Full-Stack Coding Agents on E2B
- date: Wed, 28 Oct 2026
- link: https://e2b.dev/customers/niteshift

How Niteshift runs Claude Code, Codex, and other coding agents on E2B's agentic infrastructure, with full Docker dev environments and live previews that resume from memory snapshots in seconds.
### Sandboxes are dead
- date: Fri, 16 Oct 2026
- link: https://e2b.dev/resources/sandboxes-are-dead

From code snippets to entire computers, agents have outgrown the sandbox. E2B's next chapter is an agent-driven private cloud that adapts to every task.
### Best Code Execution Sandboxes for AI Agents in 2026
- date: Thu, 15 Oct 2026
- link: https://e2b.dev/resources/best-code-execution-sandboxes-for-ai-agents

Compare the best 2026 code execution sandboxes for AI agents. See how E2B stacks up against alternatives for isolation, BYOC, billing, and open source.
### How ClickUp Runs AI Code on Sensitive Data at Enterprise Scale
- date: Thu, 08 Oct 2026
- link: https://e2b.dev/customers/clickup

How ClickUp Brain² uses E2B sandboxes to run model-written code on sensitive workspace data, with isolated microVMs, prebuilt templates, and thousands of sandboxes in a minute.
## Browserbase
Source: https://www.browserbase.com/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://www.browserbase.com/blog

### How to build agent infrastructure
- date: 2026-11-05
- link: https://browserbase.com/blog/build-vs-buy-agent-infrastructure

### Introducing Stagehand 4.4: browser.disconnect(), crash-safe sessions, and more
- date: 2026-11-05
- link: https://browserbase.com/changelog/stagehand-4-4

### The Browser Blog
- date: 2026-11-05
- link: https://browserbase.com/blog/page/1/

### The Browser Blog
- date: 2026-11-05
- link: https://browserbase.com/blog/page/2/

### The Browser Blog
- date: 2026-11-05
- link: https://browserbase.com/blog/page/3/

### The Browser Blog
- date: 2026-11-05
- link: https://browserbase.com/blog/page/4/

## Modal
Source: https://modal.com/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://modal.com/blog

### How Snorkel runs realistic agent simulations with Modal
- date: 2026-11-06
- link: https://modal.com/blog/how-snorkel-runs-realistic-agent-simulations-with-modal

### New Image Builder version 2026.10 with updated trust stores
- date: 2026-11-02
- link: https://modal.com/changelog/new-image-builder-version-2026-10-with-updated-trust-stores

### DeepSeek V4.1 Flash 1017 is now available on Shared Endpoints
- date: 2026-10-27
- link: https://modal.com/changelog/deepseek-v4-1-flash-1017-now-available-on-shared-endpoints

### Exit Snapshots for Sandboxes available in Beta
- date: 2026-10-27
- link: https://modal.com/changelog/exit-snapshots-resume-sandbox-preserve-state

### Launching a trillion-parameter model at Sakana AI
- date: 2026-10-23
- link: https://modal.com/blog/sakana-case-study

### Sunsetting Modal Notebooks, effective today
- date: 2026-10-23
- link: https://modal.com/changelog/sunsetting-modal-notebooks

## Prime Intellect
Source: https://www.primeintellect.ai/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://www.primeintellect.ai/blog

### Learnings from Auditing Public Evaluations
- date: 2026-11-03
- link: https://www.primeintellect.ai/blog/auditing-public-evaluations

### Prime Mega MoE: Fast Fused MoE Kernels for Training
- date: 2026-10-29
- link: https://www.primeintellect.ai/blog/prime-mega-moe

### prime-rl 0.10.0: faster training, our new RL loss IPO, and one unified eval stack
- date: 2026-10-19
- link: https://www.primeintellect.ai/blog/prime-rl-0-10-verifiers-0-4

### Moondream is joining Prime Intellect
- date: 2026-10-13
- link: https://www.primeintellect.ai/blog/moondream

### Rewriting Prime Agent in Rust
- date: 2026-10-09
- link: https://www.primeintellect.ai/blog/prime-agent-rust

### On the Nature of the Swarm
- date: 2026-10-06
- link: https://www.primeintellect.ai/blog/on-the-nature-of-the-swarm

## Galileo
Source: https://galileo.ai/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://galileo.ai/blog

### Enterprise AI Governance From Pilot to Production
- date: unknown
- link: https://galileo.ai/blog/enterprise-ai-governance-pilot-to-production

### AI Operational Governance Model for Production Agents
- date: unknown
- link: https://galileo.ai/blog/ai-operational-governance-model

### Agent Development Lifecycle: 5 Production Stages
- date: unknown
- link: https://galileo.ai/blog/agent-development-lifecycle

### Agent Development Lifecycle Stages: 5-Step Guide
- date: unknown
- link: https://galileo.ai/blog/agent-development-lifecycle-stages

### Agent Observability Across Development Lifecycle
- date: unknown
- link: https://galileo.ai/blog/agent-observability-development-lifecycle

### Enterprise Agent Development Lifecycle Strategy
- date: unknown
- link: https://galileo.ai/blog/enterprise-agent-development-lifecycle-strategy

## Comet / Opik
Source: https://www.comet.com/blog/feed | Home: https://www.comet.com/blog

### Understanding Your Claude Code Spend: What’s Actually Driving the Cost
- date: Wed, 17 Jun 2026
- link: https://live-comet-marketing-site.pantheonsite.io/blog/claude-code-context-bloat/

I&#8217;ve been spending time looking at how teams are actually using Claude Code, and one thing keeps coming up: most of the cost surprises aren&#8217;t coming from where people expect. The instinct is to look at conversation history — keep prompts tight, avoid long threads, or explore smaller models. That&#8217;s not wrong, but it&#8217;s often [&#8230;]
The post Understanding Your Claude Code Spend: What&#8217;s Actually Driving the Cost appeared first on Comet.
### Optimizing Agentic Remediation for Financial Services with Opik
- date: Fri, 06 Nov 2026
- link: https://live-comet-marketing-site.pantheonsite.io/blog/optimize-finance-agent-with-opik/

Incident remediation agents are quickly emerging as one of the most compelling AI use cases for the enterprise. This is particularly true for large financial institutions, where complex infrastructure and the sheer volume of production signals make it difficult to distinguish genuine incidents from background noise. That&#8217;s where remediation agents step in — they can [&#8230;]
The post Optimizing Agentic Remediation for Financial Services with Opik appeared first on Comet.
### How to Trace and Evaluate a Google ADK Agent with Opik
- date: Thu, 05 Nov 2026
- link: https://live-comet-marketing-site.pantheonsite.io/blog/trace-evaluate-google-adk-agent-opik/

Trace a multi-agent Google ADK app with Opik, fix handoffs that split into two traces, and evaluate it on 23 hard support cases to compare two Gemini models on cost, speed and refund safety.
The post How to Trace and Evaluate a Google ADK Agent with Opik appeared first on Comet.
### Opik Security Incident: October 2026
- date: Tue, 27 Oct 2026
- link: https://live-comet-marketing-site.pantheonsite.io/blog/security-incident-october-2026/

No customer data, accounts, or API keys were accessed. On October 26, 2026, Comet contained a security incident affecting Opik on comet.com. This post explains what happened, what was affected, and what we have done in response. What happened Between October 24 and 26, 2026, an unauthorized party used a comet.com user API key from [&#8230;]
The post Opik Security Incident: October 2026 appeared first on Comet.
### Introducing Opik’s Generative Dashboard Builder
- date: Mon, 26 Oct 2026
- link: https://live-comet-marketing-site.pantheonsite.io/blog/introducing-opiks-generative-dashboard-builder/

At Comet, we’ve seen firsthand how teams in finance, tech, e-commerce, and beyond use the Opik platform to track critical metrics for monitoring and improving their agents. Those metrics vary widely — for instance, a financial services team checking that its internal support agent follows company policy will track very different metrics than an automotive [&#8230;]
The post Introducing Opik&#8217;s Generative Dashboard Builder appeared first on Comet.
### Train your own decision model
- date: Mon, 26 Oct 2026
- link: https://live-comet-marketing-site.pantheonsite.io/blog/train-a-decision-model/

Decision models drew wide attention in September, when TypeSafe AI launched Jev, a model that returns probabilities over a fixed set of answers instead of generating text. Open-source alternatives followed almost immediately: Latent.Space counted six in two days. Most writing about decision models since then defines them by their interface, which uses some sort of [&#8230;]
The post Train your own decision model appeared first on Comet.
## Databricks
Source: https://www.databricks.com/rss.xml | Home: https://www.databricks.com/blog

### Read, don't copy: replacing file feeds with OpenSharing - Part 2 (How to Implement)
- date: Fri, 06 Nov 2026
- link: https://www.databricks.com/blog/read-dont-copy-replacing-file-feeds-opensharing-part-2-how-implement

Many data-sharing architectures begin with a familiar pattern: A provider exports...
### Read, don't copy: replacing file and API feeds with OpenSharing - Part 1 (The Why)
- date: Fri, 06 Nov 2026
- link: https://www.databricks.com/blog/read-dont-copy-replacing-file-and-api-feeds-opensharing-part-1-why

If you ingest data from your customers over SFTP or APIs, you have probably asked...
### How public sector organizations can govern AI at scale
- date: Fri, 06 Nov 2026
- link: https://www.databricks.com/blog/how-public-sector-organizations-can-govern-ai-scale

Every government CIO has the same mandate right now: adopt AI, move faster, and do...
### Real-time fraud detection with Feature Views
- date: Thu, 05 Nov 2026
- link: https://www.databricks.com/blog/real-time-fraud-detection-feature-views

Real-time fraud detection depends on three kinds of features: what a customer did...
### A builder’s guide to scaling Databricks Apps
- date: Thu, 05 Nov 2026
- link: https://www.databricks.com/blog/builders-guide-scaling-databricks-apps

Congratulations, you've built an app on Databricks Apps, and it's gone from a couple...
### Which Data Collaboration Tool: OpenSharing, Clean Rooms, Marketplace
- date: Thu, 05 Nov 2026
- link: https://www.databricks.com/blog/which-data-collaboration-tool-opensharing-clean-rooms-marketplace

The world of sharing has extended far past tables. We can now securely share all...
## Patronus AI
Source: https://www.patronus.ai/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://www.patronus.ai/blog

### Getting GLM-5.2 NVFP4 Post-Training Off the Ground
- date: 2026-11-08
- link: https://www.patronus.ai/blog/getting-glm-5-2-nvfp4-post-training-off-the-ground

### SpeedrunBench: A Benchmark for Frontier Agents
- date: 2026-11-08
- link: https://www.patronus.ai/blog/introducing-speedrunbench-a-challenging-benchmark-for-frontier-agents

### Introducing MEMTRACK: A Benchmark for Agent Memory
- date: 2026-11-08
- link: https://www.patronus.ai/blog/memtrack

### Few Word Do Trick: Open Models Cut the Filler
- date: 2026-11-07
- link: https://www.patronus.ai/blog/few-word-do-trick

### GlobeBench: A Benchmark for Text-Based World Models
- date: 2026-11-07
- link: https://www.patronus.ai/blog/globebench

### Generative Simulators: Scaling Environments for Agents
- date: 2026-11-06
- link: https://www.patronus.ai/blog/introducing-generative-simulators

## Humanloop
Source: https://humanloop.com/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://humanloop.com/blog

### OpenAI Agents SDK
- date: 2025-05-06
- link: https://humanloop.com/blog/openai-agents-sdk

### LLM as a Judge
- date: 2025-05-04
- link: https://humanloop.com/blog/llm-as-a-judge

### Prompt Files
- date: 2025-04-05
- link: https://humanloop.com/blog/prompt-files

### Model Context Protocol (MCP) Explained
- date: 2025-04-04
- link: https://humanloop.com/blog/mcp

### What is LLM Observability and Monitoring?
- date: 2025-03-31
- link: https://humanloop.com/blog/llm-monitoring

### 5 LLM Evaluation Tools You Should Know in 2025
- date: 2025-03-19
- link: https://humanloop.com/blog/best-llm-evaluation-tools

## Confident AI (DeepEval)
Source: https://www.confident-ai.com/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://www.confident-ai.com/blog

### Product Changelogs, November 6, 2026
- date: 2026-11-07
- link: https://www.confident-ai.com/docs/changelog/2026/11/6

### Product Changelogs, October 30, 2026
- date: 2026-10-31
- link: https://www.confident-ai.com/docs/changelog/2026/10/30

### Introducing Confident Voice
- date: 2026-10-29
- link: https://www.confident-ai.com/blog/introducing-confident-voice

### Introducing Confident Monitor
- date: 2026-10-29
- link: https://www.confident-ai.com/blog/introducing-confident-ai-monitor

### Product Changelogs, October 23, 2026
- date: 2026-10-24
- link: https://www.confident-ai.com/docs/changelog/2026/10/23

### Confident AI Prompt Monitoring Guide
- date: 2026-10-23
- link: https://www.confident-ai.com/blog/confident-ai-prompt-monitoring-guide

## Langfuse
Source: https://langfuse.com/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://langfuse.com/blog

### Langfuse AI Gateway public beta
- date: 2026-11-09
- link: https://langfuse.com/changelog/2026-11-04-ai-gateway-public-beta

### Connect your S3 buckets with an IAM role
- date: 2026-11-09
- link: https://langfuse.com/changelog/2026-11-06-s3-iam-role-auth

### Skill Management in Langfuse
- date: 2026-11-06
- link: https://langfuse.com/changelog/2026-11-03-skill-management

### See when token usage is missing
- date: 2026-11-06
- link: https://langfuse.com/changelog/2026-11-06-retiring-tokenization

### State of LLMs on the Application Layer
- date: 2026-11-04
- link: https://langfuse.com/blog/2025-10-13-state-of-llms-september-2025

### Catching conversation signals in Langfuse
- date: 2026-11-04
- link: https://langfuse.com/blog/2026-09-23-catching-conversation-signals-in-langfuse

## Daytona
Source: https://www.daytona.io/rss.xml | Home: https://www.daytona.io/blog

### 1M to $100M Run Rate in 4 Quarters
- date: Tue, 03 Nov 2026
- link: https://www.daytona.io/dotfiles/1m-to-100m-run-rate-in-4-quarters

### Daytona runs the code, Notte runs the browser
- date: Fri, 30 Oct 2026
- link: https://www.daytona.io/dotfiles/daytona-runs-the-code-notte-runs-the-browser

### Daytona2: Agent Infrastructure Requires More Than Kubernetes
- date: Thu, 29 Oct 2026
- link: https://www.daytona.io/dotfiles/daytona2-agent-infrastructure-requires-more-than-kubernetes

### Daytona Raises $60M Series B to Build the Agent Cloud
- date: Tue, 20 Oct 2026
- link: https://www.daytona.io/dotfiles/daytona-raises-60m-series-b-to-build-the-agent-cloud

### When 2,000 Agents Share One CPU
- date: Wed, 07 Oct 2026
- link: https://www.daytona.io/dotfiles/when-2000-agents-share-one-cpu

### Daytona sandboxes are now a Convex component
- date: Wed, 30 Sep 2026
- link: https://www.daytona.io/dotfiles/daytona-sandboxes-convex-component

## Runloop
Source: https://www.runloop.ai/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://www.runloop.ai/blog

### Accrual Moves Coding Agents to the Cloud with Runloop
- date: 2026-08-21
- link: https://runloop.ai/blog/accrual-moves-coding-agents-to-the-cloud-with-runloop

### Trust your agent with a credit card, with Runloop and Kernel
- date: 2026-07-29
- link: https://runloop.ai/blog/trust-your-agent-with-a-credit-card-with-runloop-and-kernel

### ION Deploys AI Agents for Every Customer with Runloop
- date: 2026-06-24
- link: https://runloop.ai/blog/ion-case-study

### Announcing: Transparent Proxy for Runloop Tunnels
- date: 2026-06-24
- link: https://runloop.ai/blog/release-transparent-proxy-for-tunnels

### How Trajectory ran 10,000 concurrent devboxes on Runloop
- date: 2026-06-24
- link: https://runloop.ai/blog/runloop-trajectory-launch-partner-announcement

### Axons: Distributed Event Streams for Agents at Scale
- date: 2026-05-27
- link: https://runloop.ai/blog/axon-release-part-1
