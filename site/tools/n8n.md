# n8n: MCP server status, API access gate and what it does

> A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes,... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
n8n

# n8n

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [n8n.io](https://n8n.io) · entry id 06-n8n · source 06-revops-infra.md line 120

**What it does**
A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes, usable self-hosted or as managed cloud.

**AI features, separated from automation with an AI label on it**
The AI Agent node (built on LangChain) is n8n's genuine AI layer - an LLM (OpenAI, Claude, Gemini, or local via Ollama) that reads context, chooses among connected tools (HTTP calls, DB queries, code, APIs, or MCP servers), and decides its own next step. This is distinct from n8n's traditional deterministic nodes (IF/switch/HTTP request/etc.), which are plain rules-based automation - most of n8n's 400+ integrations fall in that non-AI bucket, and only the LangChain-powered nodes (Agent, Chains, Memory, Vector Store, ~70+ nodes total) are actually LLM-driven.

**RevOps role**
The general-purpose orchestration layer that glues the other tools (Salesforce, HubSpot, Attio, Pipedrive, Close) together - increasingly an MCP hub in both directions, since it can consume other vendors' MCP servers as an AI Agent's tools and expose its own workflows as an MCP server to other clients.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: MCP Server Trigger supports Bearer or Header auth to secure the exposed endpoint; supports SSE and streamable-HTTP transport with separate test/production URLs.

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger (MCP Server Trigger - n8n exposes its own workflows as an MCP server) and https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp (MCP Client Tool - an n8n AI Agent calls external MCP servers as tools)

- [https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)
- [https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - Community Edition is free to self-host under n8n's "fair-code" Sustainable Use License (source-available, not OSI open source); unlimited workflows/executions/users with no license fee unless reselling n8n's functionality as a product. Managed cloud plans run roughly the low-hundreds-of-dollars/mo range for hosted convenience.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)
- [https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp)
- [https://n8n.io/integrations/agent/](https://n8n.io/integrations/agent/)

3 source URLs. Raw sources field, verbatim:

https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger, https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp, https://n8n.io/integrations/agent/

**Notes, verbatim from the file**
n8n's MCP nodes are first-party/built-in, not a community add-on - distinguish from third-party community MCP-related packages that also exist in the ecosystem.

**Provenance**

- **Entry id**: 06-n8n

- **Source file**: 06-revops-infra.md

- **Source line**: 120

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
