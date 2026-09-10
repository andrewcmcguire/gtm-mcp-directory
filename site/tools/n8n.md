# n8n: MCP server status, API access gate and what it does

> A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes,... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
n8n

# n8n

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [n8n.io](https://n8n.io) · entry id 06-n8n · source 06-revops-infra.md line 123

**What it does**
A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes, usable self-hosted or as managed cloud.

**AI features, separated from automation with an AI label on it**
The AI Agent node (built on LangChain) is n8n's genuine AI layer - an LLM (OpenAI, Claude, Gemini, or local via Ollama) that reads context, chooses among connected tools (HTTP calls, DB queries, code, APIs, or MCP servers), and decides its own next step. This is distinct from n8n's traditional deterministic nodes (IF/switch/HTTP request/etc.), which are plain rules-based automation - most of n8n's 400+ integrations fall in that non-AI bucket, and only the LangChain-powered nodes (Agent, Chains, Memory, Vector Store, ~70+ nodes total) are actually LLM-driven.

**RevOps role**
The general-purpose orchestration layer that glues the other tools (Salesforce, HubSpot, Attio, Pipedrive, Close) together - increasingly an MCP hub in both directions, since it can consume other vendors' MCP servers as an AI Agent's tools and expose its own workflows as an MCP server to other clients.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: MCP Server Trigger supports Bearer or Header auth to secure the exposed endpoint; supports SSE and streamable-HTTP transport with separate test/production URLs.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/n8n-io/n8n ; https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger (MCP Server Trigger - n8n exposes its own workflows as an MCP server) and https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp (MCP Client Tool - an n8n AI Agent calls external MCP servers as tools)

- [https://github.com/n8n-io/n8n](https://github.com/n8n-io/n8n)
- [https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)
- [https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp)

**What this server exposes**

What this server exposes is the customer's own workspace, not a fixed catalogue the vendor publishes. No tool list is the correct answer here rather than a gap, and the harvest recorded it as one.

Recorded by the harvest: the MCP trigger exposes whatever workflow the customer builds behind it

The count below still carries this entry on the unmeasured side, because there is no list to record. That is a different thing from a server nobody has read, and both are published rather than blended.

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-10. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-10 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - Community Edition is free to self-host under n8n's "fair-code" Sustainable Use License (source-available, not OSI open source); unlimited workflows/executions/users with no license fee unless reselling n8n's functionality as a product. Managed cloud plans run roughly the low-hundreds-of-dollars/mo range for hosted convenience.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/n8n-io/n8n](https://github.com/n8n-io/n8n)

**On GitHub**

[github.com/n8n-io](https://github.com/n8n-io) tied to the vendor by rule 2, account website https://n8n.io has the vendor's domain, confidence strong

- **Public repositories**: 35, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [terraform-aws-n8n](https://github.com/n8n-io/terraform-aws-n8n) | infrastructure | Production-grade n8n Enterprise on AWS - multi-main EKS, RDS Postgres, ElastiCache Redis, S3, and ALB in one terraform... | 13 | 2026-09-08 | 0.3.0 |
| [n8n](https://github.com/n8n-io/n8n) | MCP server | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host... | 203,741 | 2026-09-08 | n8n@2.39.0 |
| [n8n-docs](https://github.com/n8n-io/n8n-docs) | docs or examples | Documentation for n8n, a fair-code licensed automation tool with a free community edition and powerful enterprise... | 1,758 | 2026-09-08 | |
| [n8n-hosting](https://github.com/n8n-io/n8n-hosting) | docs or examples | Example of self-hosting n8n in various environments like docker, kubernetes, etc. | 1,734 | 2026-09-08 | v1.11.0 |
| [n8n-sandbox-service](https://github.com/n8n-io/n8n-sandbox-service) | other | | 18 | 2026-09-08 | service/v1.3.3 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)
- [https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp)
- [https://n8n.io/integrations/agent/](https://n8n.io/integrations/agent/)
- [https://github.com/n8n-io/n8n](https://github.com/n8n-io/n8n)

4 source URLs. Raw sources field, verbatim:

https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger, https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp, https://n8n.io/integrations/agent/, https://github.com/n8n-io/n8n

**Notes, verbatim from the file**
n8n's MCP nodes are first-party/built-in, not a community add-on - distinguish from third-party community MCP-related packages that also exist in the ecosystem. 2026-09-07: n8n publishes @n8n/mcp-apps and @n8n/mcp-browser to npm under the vendor-owned @n8n scope, both with repository git+https://github.com/n8n-io/n8n.git (https://github.com/n8n-io/n8n).

**Provenance**

- **Entry id**: 06-n8n

- **Source file**: 06-revops-infra.md

- **Source line**: 123

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-10

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
