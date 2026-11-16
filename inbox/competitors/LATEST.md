# Competitor / team harvest 2026-W47 (fetched 2026-11-16)

Recent posts from competitor and reference-team blogs, pulled from their RSS/Atom feeds by a GitHub Actions runner (the cloud research sandbox cannot reach these directly). Read this alongside inbox/arxiv/. Sources with no feed are listed so you cover them via WebSearch and log the gap honestly.

## Coverage this run
- Braintrust: 6 posts via https://www.braintrust.dev/sitemap.xml (sitemap fallback; titles fetched per page)
- Arize: 6 posts via https://arize.com/blog/feed/
- E2B: 6 posts via https://e2b.dev/rss.xml
- Browserbase: 6 posts via https://www.browserbase.com/sitemap.xml (sitemap fallback; titles fetched per page)
- Modal: 6 posts via https://modal.com/sitemap.xml (sitemap fallback; titles fetched per page)
- Prime Intellect: 6 posts via https://www.primeintellect.ai/sitemap.xml (sitemap fallback; titles fetched per page)
- LangChain / LangSmith: NO FEED OR SITEMAP FOUND (cover via WebSearch; home https://blog.langchain.com/)
- Galileo: NO FEED OR SITEMAP FOUND (cover via WebSearch; home https://galileo.ai/blog)
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

### Manage Braintrust with Terraform
- date: 2026-11-10
- link: https://www.braintrust.dev/blog/terraform

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

### How Artificial Analysis Puts Frontier Models to the Test with E2B
- date: Tue, 10 Nov 2026
- link: https://e2b.dev/customers/artificial-analysis

How Artificial Analysis uses E2B to run agentic benchmarks on public and pre-release models, from zero to thousands of tasks in seconds.
### NVIDIA Vera brings faster compute to E2B sandboxes
- date: Mon, 09 Nov 2026
- link: https://e2b.dev/resources/nvidia-vera-brings-faster-compute-to-e2b-sandboxes

Faster compute and memory population, with capacity for 1,550 loaded sandboxes on one server. Here’s why Vera matters for E2B’s agent cloud.
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

### Inkling 2 Small is now available on Modal
- date: 2026-11-14
- link: https://modal.com/changelog/inkling-2-small-is-now-available-on-modal

### Scaling Intelligence: A landmark commission and exhibition
- date: 2026-11-13
- link: https://modal.com/blog/scaling-intelligence

### Sandbox resourcing: burst, don
- date: 2026-11-12
- link: https://modal.com/blog/sandbox-bursting

### New Sandbox Events UI for execs, TCP tunnels, and HTTP requests
- date: 2026-11-12
- link: https://modal.com/changelog/new-sandbox-events-ui-for-execs-tcp-tunnels-and-http-requests

### Modal becomes a gVisor maintainer
- date: 2026-11-11
- link: https://modal.com/blog/modal-gvisor-maintainer

### View invoices directly in the Modal dashboard
- date: 2026-11-11
- link: https://modal.com/changelog/view-invoices-directly-in-the-modal-dashboard

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

### Teach Genie One your workflows: The ultimate guide for skills in Genie One
- date: Mon, 16 Nov 2026
- link: https://www.databricks.com/blog/teach-genie-one-your-workflows-ultimate-guide-skills-genie-one

Every team has “recipes” that govern how they work. The way finance puts together...
### Apache Spark vs Apache Flink: which should you use?
- date: Sat, 14 Nov 2026
- link: https://www.databricks.com/blog/spark-vs-flink

For most teams, Apache Spark™ is the better choice. Spark runs batch ETL, SQL analytics,...
### OpenAI and Databricks: Enterprise AI on your governed data
- date: Fri, 13 Nov 2026
- link: https://www.databricks.com/blog/openai-and-databricks-enterprise-ai-your-governed-data

Greg Brockman, co-founder and President of OpenAI, has a simple way to describe AI...
### Dispelling LTAP myths
- date: Thu, 12 Nov 2026
- link: https://www.databricks.com/blog/dispelling-ltap-myths

Reynold Xin's post "From monolith to Lakebase to LTAP" explained what LTAP is and...
### How Constellation is building a governed data foundation on Databricks
- date: Thu, 12 Nov 2026
- link: https://www.databricks.com/blog/how-constellation-building-governed-data-foundation-databricks

Constellation operates the largest nuclear fleet in the United States. For them,...
### Eclipse Aerospace simplifies flight-data ingestion with Databricks
- date: Thu, 12 Nov 2026
- link: https://www.databricks.com/blog/eclipse-aerospace-simplifies-flight-data-ingestion-databricks

As organizations in aerospace, manufacturing, life sciences, and other data-intensive...
## Patronus AI
Source: https://www.patronus.ai/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://www.patronus.ai/blog

### Who Is the Right Expert for AI?
- date: 2026-11-13
- link: https://www.patronus.ai/blog/right-expert-for-ai

### Few Word Do Trick: Open Models Cut the Filler
- date: 2026-11-11
- link: https://www.patronus.ai/blog/few-word-do-trick

### GlobeBench: A Benchmark for Text-Based World Models
- date: 2026-11-11
- link: https://www.patronus.ai/blog/globebench

### FigmaTrace: A Training Dataset for Figma Design Workflows
- date: 2026-11-09
- link: https://www.patronus.ai/blog/figmatrace-a-comprehensive-training-dataset-for-figma-design-workflows

### Getting GLM-5.2 NVFP4 Post-Training Off the Ground
- date: 2026-11-09
- link: https://www.patronus.ai/blog/getting-glm-5-2-nvfp4-post-training-off-the-ground

### Generative Simulators: Scaling Environments for Agents
- date: 2026-11-09
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

### Product Changelogs, November 13, 2026
- date: 2026-11-13
- link: https://www.confident-ai.com/docs/changelog/2026/11/13

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

## Langfuse
Source: https://langfuse.com/sitemap.xml (sitemap fallback; titles fetched per page) | Home: https://langfuse.com/blog

### Should you use an LLM Proxy to Build your Application?
- date: 2026-11-16
- link: https://langfuse.com/blog/2024-09-langfuse-proxy

### Langfuse launches AI Gateway
- date: 2026-11-13
- link: https://langfuse.com/blog/introducing-gateway

### Call Microsoft Azure and Google AI Studio models through the AI Gateway
- date: 2026-11-13
- link: https://langfuse.com/changelog/2026-11-12-ai-gateway-azure-google-ai-studio

### Restrict models per AI Gateway key
- date: 2026-11-13
- link: https://langfuse.com/changelog/2026-11-13-ai-gateway-key-model-restrictions

### Call Google Vertex AI models through the AI Gateway
- date: 2026-11-13
- link: https://langfuse.com/changelog/2026-11-13-ai-gateway-vertex-ai

### Langfuse AI Gateway public beta
- date: 2026-11-12
- link: https://langfuse.com/changelog/2026-11-04-ai-gateway-public-beta

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
