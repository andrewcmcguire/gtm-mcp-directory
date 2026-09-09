# MCP Layer: 19 tools, 14 with an official MCP server

> The layer that sits between an AI agent and the hundred SaaS apps a GTM team actually runs on:... 19 tools counted, 14 with an official MCP server and 12 free to start.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[By category](index.md) / MCP Layer

**07 · mcp-infrastructure**

## MCP Layer

The layer that sits between an AI agent and the hundred SaaS apps a GTM team actually runs on: registries that just list servers, and aggregators that host/broker them. The load-bearing question for every entry below is who holds the OAuth tokens when you connect - read `notes` before you wire anything into a production agent.

- **entries in this file**: 19

- **Official MCP**: 14
- **MCP unknown**: 1
- **MCP not applicable**: 4

- **ship a CLI (official) as of 2026-09-09**: 9

- **Free to start**: 12
- **Paid, self-serve**: 2
- **Enterprise leaning**: 1
- **Enterprise only**: 1
- **Gate unknown**: 3

Source file: 07-mcp-infrastructure.md · content sha256 37ac5980797c44b6... · counts reconciled against tools_recount.py at build time.

- [The 14 with an MCP server](../lists/mcp-mcp-infrastructure.md)

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)
- [Discover MCP servers](../jobs/discover-mcp-servers.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

- [Apideck](../tools/apideck.md) apideck.com A unified API that normalises 200+ SaaS connectors into single data models, exposed as one MCP endpoint covering CRM, accounting, HRIS, ATS, file storage and issue tracking. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: apideck

- [Composio](../tools/composio.md) composio.dev A hosted integration/auth platform that lets AI agents and MCP clients call actions across 1,000+ SaaS apps (HubSpot, Slack, Gmail, GitHub, Notion, Stripe, and others) through Composio-managed OAuth. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: composio

- [Knit MCP](../tools/knit-mcp.md) getknit.dev A unified-API vendor that publishes hosted, serverless MCP servers for individual SaaS applications across CRM, ATS, HRIS, ticketing, accounting, calendar, email and e-sign, alongside its unified REST APIs and... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: knit-mcp (community)

- [Merge Agent Handler](../tools/merge-agent-handler.md) merge.dev Merge's tool-calling platform for AI agents: it wraps hundreds of third-party SaaS applications as pre-built MCP-ready connectors, bundles them into scoped "tool packs" per agent, brokers per-end-user... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Model Context Protocol - official servers repo](../tools/model-context-protocol-official-servers-repo.md) github.com The official reference-implementation repository for MCP, "managed by Anthropic, but built together with the community" - ships a small set of maintained example servers (Everything, Fetch, Filesystem, Git,... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Pipeworx](../tools/pipeworx.md) pipeworx.io A single MCP gateway that fronts a stated 1,532 live data sources as 5,871 tools behind one URL, weighted toward public and regulatory data (SEC EDGAR, FDA, the Federal Reserve, ClinicalTrials, USPTO, EPA, EU... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: pipeworx

- [StackOne](../tools/stackone.md) stackone.com A unified-API vendor that publishes a stated 518 managed MCP servers exposing 31,928 tools across HR, CRM, IT and finance applications, reachable through one endpoint with per-account routing, plus dynamic... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: stackone

- [usefulapi.io](../tools/usefulapi-io.md) usefulapi.io A hosted catalogue of 146 single-application MCP servers, one per SaaS product, each on its own subdomain, wrapping that product's public REST API as a named tool list with per-tool read and write labels and... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Zapier MCP](../tools/zapier-mcp.md) zapier.com Zapier's own MCP endpoint, letting Claude, ChatGPT, Cursor, and other MCP clients trigger the same 9,000+ app actions Zapier already exposes to its classic trigger-action Zaps. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: zapier-platform

- [Metorial](../tools/metorial.md) metorial.com A hosted MCP gateway that gives AI agents/"AI employees" centralized, governed access to a company's SaaS tools (Google Workspace, Microsoft 365, GitHub, Jira, Slack, Teams, Stripe, Salesforce, Zendesk, and... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · CLI: metorial

- [Pipedream MCP](../tools/pipedream-mcp.md) pipedream.com Pipedream's existing workflow/integration platform re-exposed as hosted MCP servers, giving an MCP client access to 3,000+ connected apps and 10,000+ pre-built tools via Pipedream Connect. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Paragon (ActionKit MCP)](../tools/paragon.md) useparagon.com An embedded integration platform for SaaS products, whose ActionKit product exposes a stated 1,000-plus actions across 130-plus third-party applications through one API and one MCP server, with Paragon... [Official MCP](../mcp/official.md) · [Enterprise leaning](../gates/enterprise-leaning.md) · CLI: whiskers

- [mcp.run / TurboMCP](../tools/mcp-run-turbomcp.md) turbomcp.ai An enterprise self-hosted MCP gateway and management platform - a trusted, admin-curated registry plus RBAC-controlled deployment of MCP servers across a team's own infrastructure (K8s, PaaS, VMs). [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Klavis AI](../tools/klavis-ai.md) klavis.ai Primarily an AI-agent training-data company - it builds "live environments for training AI agents" (long-horizon coding tasks and agentic tool-use scenarios), and separately mentions "production MCP servers"... [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md)

- [mcp.so](../tools/mcp-so.md) mcp.so A community MCP server/client directory (per its public reputation as one of the earlier MCP catalog sites) - could not independently re-verify current content in this research pass. [MCP unknown](../mcp/unknown.md) · [Gate unknown](../gates/unknown.md)

- [Claude / Anthropic MCP Connector Directory](../tools/claude-anthropic-mcp-connector-directory.md) claude.com Anthropic's own curated, in-product directory of MCP connectors that Claude users can browse and one-click-connect to, filterable by use case (sales, marketing, data, etc.) and by capability (read / read-write... [MCP not applicable](../mcp/n-a.md) · [Free to start](../gates/free.md)

- [PulseMCP](../tools/pulsemcp.md) pulsemcp.com A community-run browsable directory and news hub for the MCP ecosystem (servers, clients, use cases, and a newsletter called "The Agentic Loop") that links out to third-party servers rather than hosting them. [MCP not applicable](../mcp/n-a.md) · [Free to start](../gates/free.md) · CLI: air

- [Smithery](../tools/smithery.md) smithery.ai A registry and distribution marketplace for MCP servers - "publish once, install anywhere" - that indexes and distributes third-party servers rather than hosting them itself, plus an integrated... [MCP not applicable](../mcp/n-a.md) · [Free to start](../gates/free.md) · CLI: smithery

- [Glama (MCP directory)](../tools/glama.md) glama.ai A large searchable registry/catalog of open-source MCP servers (77,000+ listed as of this check), filterable by language, hosting type (remote/local/hybrid), capability, and category; also offers separate... [MCP not applicable](../mcp/n-a.md) · [Gate unknown](../gates/unknown.md)
