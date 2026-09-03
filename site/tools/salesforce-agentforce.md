# Salesforce (core CRM/platform) + Agentforce: MCP server status, API access gate and what it does

> A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Salesforce (core CRM/platform) + Agentforce

# Salesforce (core CRM/platform) + Agentforce

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [salesforce.com](https://salesforce.com) · entry id 06-salesforce-agentforce · source 06-revops-infra.md line 11

**What it does**
A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code app layer, with Agentforce as a layer on top for configuring autonomous AI agents that read Salesforce data, decide on an action, and execute it or hand off to a human.

**AI features, separated from automation with an AI label on it**
Agentforce is the genuine AI layer - LLM-driven agents that plan and act on CRM data, and as of Agentforce 3 can act as an MCP client to call external MCP servers. The base platform's automation (Flow, process builder) is plain rules-based automation, not AI.

**RevOps role**
The system-of-record CRM most large/enterprise RevOps stacks are built on; Agentforce + Hosted MCP is Salesforce's play to let external AI tools (or its own agents) read/act on that system of record directly.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth + PKCE via an External Client App (scopes mcp_api, refresh_token); every MCP call runs under the authenticated user's own permissions (CRUD/FLS/sharing rules apply), not a service account. The DX/CLI server instead relies on orgs pre-authorized via `sf org login web`.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/salesforcecli/mcp (Salesforce DX/CLI MCP server, dev-tooling use case); https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html and https://github.com/forcedotcom/mcp-hosted (Salesforce Hosted MCP Servers, GA April 2026, external AI clients read/act on live org data)

- [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp)
- [https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html)
- [https://github.com/forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only for the MCP-enabled path - Salesforce Hosted MCP Servers require Enterprise Edition or above. Raw REST API access is free on Developer Edition sandboxes; production-tier API pricing/inclusion by edition was not independently confirmed and is marked unknown rather than guessed.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)
- [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp)

**Jobs it can do**

- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Salesforce Agentforce (SDR Agent)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: No MCP found

- **Gate there**: Enterprise only

- **Source**: 04-ai-sdr-agents.md line 220

- **Canonical page**: [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md)

What that listing says it does: A prebuilt agent within Salesforce's Agentforce platform intended to handle inbound lead engagement and outbound prospecting conversations natively inside Sales Cloud, escalating to a human rep once a prospect is ready.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://developer.salesforce.com/blogs/2025/06/introducing-mcp-support-across-salesforce](https://developer.salesforce.com/blogs/2025/06/introducing-mcp-support-across-salesforce)
- [https://developer.salesforce.com/blogs/2026/04/salesforce-hosted-mcp-servers-are-now-generally-available](https://developer.salesforce.com/blogs/2026/04/salesforce-hosted-mcp-servers-are-now-generally-available)
- [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp)
- [https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html)
- [https://developer.salesforce.com/blogs/2026/07](https://developer.salesforce.com/blogs/2026/07)
- (Headless 360 MCP Server Beta announcement)

5 source URLs. Raw sources field, verbatim:

https://developer.salesforce.com/blogs/2025/06/introducing-mcp-support-across-salesforce, https://developer.salesforce.com/blogs/2026/04/salesforce-hosted-mcp-servers-are-now-generally-available, https://github.com/salesforcecli/mcp, https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html, https://developer.salesforce.com/blogs/2026/07 (Headless 360 MCP Server Beta announcement)

**Notes, verbatim from the file**
The Headless 360 MCP Server (beta, July 2026) exposes only four tools - Discover, Describe, Dispatch, Dispatch Read Only - that map to a growing skill library, rather than one tool per Salesforce operation; a deliberate design choice to avoid thousands of individual MCP tools. Agentforce and Hosted MCP Server pricing were not disclosed in sources found - unknown, not guessed.

**Provenance**

- **Entry id**: 06-salesforce-agentforce

- **Source file**: 06-revops-infra.md

- **Source line**: 11

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
