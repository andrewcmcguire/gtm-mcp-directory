# Salesforce (core CRM/platform) + Agentforce: MCP server status, API access gate and what it does

> A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

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
CLI: sf

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
- **Docs URL**: [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/salesforcecli/mcp (Salesforce DX/CLI MCP server, dev-tooling use case); https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html and https://github.com/forcedotcom/mcp-hosted (Salesforce Hosted MCP Servers, GA April 2026, external AI clients read/act on live org data)

- [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp)
- [https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html)
- [https://github.com/forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)

**What this server exposes**

- **Tools named**: 17
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-12
- **Repo read**: salesforcecli/mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **ALLOW_ALL_ORGS** Allow access to all authorized orgs. Use this value with caution. evidence: in a README table · calling it reads

- **DEFAULT_TARGET_DEV_HUB** Allow access to your default Dev Hub org. If you've set a local default Dev Hub org in your DX project, the MCP server uses it. If not, the server uses a globally-set default Dev Hub org. evidence: in a README table · calling it writes

- **DEFAULT_TARGET_ORG** Allow access to your default org. If you've set a local default org in your DX project, the MCP server uses it. If not, the server uses a globally-set default org. evidence: in a README table · calling it writes

- **aura-experts** Tools that provide Aura component analysis, blueprinting, and migration expertise.. evidence: in a README table · calling it reads

- **code-analysis** Tools for static analysis of your code using Salesforce Code Analyzer. evidence: in a README table · calling it reads

- **core** Core set of DX MCP tools. This toolset is always enabled. evidence: in a README table · calling it writes

- **data** Tools to manage the data in your org, such as listing all accounts. evidence: in a README table · calling it reads

- **devops** Tools to securely and autonomously read, manage, and operate DevOps Center resources. evidence: in a README table · calling it reads

- **experts-validation** Tools to validate and score LWC components for production readiness across accessibility, security, and best practices. evidence: in a README table · calling it reads

- **lwc-experts** Tools to assist with Lightning Web Component (LWC) development, testing, optimization, and best practices. evidence: in a README table · calling it reads

- **metadata** Tools to deploy and retrieve metadata to and from your org and your DX project. evidence: in a README table · calling it reads

- **mobile** Tools for mobile development and capabilities. evidence: in a README table · calling it reads

- **mobile-core** A subset of tools from the `mobile` toolset focused on essential mobile capabilities. evidence: in a README table · calling it reads

- **orgs** Tools to manage your authorized orgs. evidence: in a README table · calling it reads

- **scale-products** Tools for detecting and fixing Apex performance. evidence: in a README table · calling it reads

- **testing** Tools to test your code and features. evidence: in a README table · calling it reads

- **users** Tools to manage org users, such as assigning a permission set. evidence: in a README table · calling it writes

119 of the 251 entries that record an official or community MCP server carry a harvested tool list. The other 132 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: sf
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @salesforce/cli
```

quoted from [https://www.npmjs.com/package/@salesforce/cli](https://www.npmjs.com/package/@salesforce/cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @salesforce/cli 2.150.6](https://www.npmjs.com/package/@salesforce/cli)
- [pypi: salesforcecli 0.0.12, third party](https://pypi.org/project/salesforcecli/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only for the MCP-enabled path - Salesforce Hosted MCP Servers require Enterprise Edition or above. Raw REST API access is free on Developer Edition sandboxes; production-tier API pricing/inclusion by edition was not independently confirmed and is marked unknown rather than guessed.

**API documentation**

No documentation URL recorded.

374 of 468 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)
- [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp)

**On GitHub**

[github.com/salesforcecli](https://github.com/salesforcecli) tied to the vendor by rule 1, account website https://developer.salesforce.com/tools/salesforcecli has the vendor's domain, confidence strong

- **Public repositories**: 75, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 16 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [plugin-trust](https://github.com/salesforcecli/plugin-trust) | plugin or integration | | 2 | 2026-09-08 | 4.0.12 |
| [plugin-apex](https://github.com/salesforcecli/plugin-apex) | CLI | Salesforce CLI Plugin that hosts the Apex commands | 5 | 2026-09-08 | 4.1.2 |
| [cli](https://github.com/salesforcecli/cli) | CLI | The `sf` cli. | 180 | 2026-09-08 | 2.151.6 |
| [plugin-data-setup-transfer](https://github.com/salesforcecli/plugin-data-setup-transfer) | plugin or integration | | 0 | 2026-09-07 | 1.0.2 |
| [plugin-data-code-extension](https://github.com/salesforcecli/plugin-data-code-extension) | plugin or integration | | 0 | 2026-09-07 | 1.4.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 468 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Salesforce Agentforce (SDR Agent)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: No MCP found

- **Gate there**: Enterprise only

- **Source**: 04-ai-sdr-agents.md line 220

- **Canonical page**: [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md)

What that listing says it does: A prebuilt agent within Salesforce's Agentforce platform intended to handle inbound lead engagement and outbound prospecting conversations natively inside Sales Cloud, escalating to a human rep once a prospect is ready.

16 of the 468 entries are cross listed like this. They are why the entry count is 468 and the unique product count is 452. The canonical home is declared in INDEX.md, not chosen by the parser.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
