# MCP Layer: 43 tools, 14 with an official MCP server

> The layer that sits between an AI agent and the hundred SaaS apps a GTM team actually runs on:... 43 tools counted, 14 with an official MCP server and 12 free to start.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[By category](index.md) / MCP Layer

**07 · mcp-infrastructure**

## MCP Layer

The layer that sits between an AI agent and the hundred SaaS apps a GTM team actually runs on: registries that just list servers, and aggregators that host/broker them. The load-bearing question for every entry below is who holds the OAuth tokens when you connect - read `notes` before you wire anything into a production agent.

- **entries in this file**: 43

- **Official MCP**: 14
- **Community MCP**: 24
- **MCP unknown**: 1
- **MCP not applicable**: 4

- **ship a CLI (official) as of 2026-09-12**: 9

- **Free to start**: 12
- **Paid, self-serve**: 2
- **Enterprise leaning**: 1
- **Enterprise only**: 1
- **Gate unknown**: 27

Source file: 07-mcp-infrastructure.md · content sha256 e0bec92380a25e5f... · counts reconciled against tools_recount.py at build time.

- [The 38 with an MCP server](../lists/mcp-mcp-infrastructure.md)

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

- [Paragon (ActionKit MCP)](../tools/paragon.md) useparagon.com An embedded integration platform for SaaS products, whose ActionKit product exposes a stated 1,000-plus actions across 130-plus third-party applications through one API and one MCP server, with Paragon... [Official MCP](../mcp/official.md) · [Enterprise leaning](../gates/enterprise-leaning.md) · CLI: para

- [mcp.run / TurboMCP](../tools/mcp-run-turbomcp.md) turbomcp.ai An enterprise self-hosted MCP gateway and management platform - a trusted, admin-curated registry plus RBAC-controlled deployment of MCP servers across a team's own infrastructure (K8s, PaaS, VMs). [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Klavis AI](../tools/klavis-ai.md) klavis.ai Primarily an AI-agent training-data company - it builds "live environments for training AI agents" (long-horizon coding tasks and agentic tool-use scenarios), and separately mentions "production MCP servers"... [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md)

- [Anyquery](../tools/anyquery.md) anyquery.dev Run SQL on GitHub, Notion, Spotify, Gmail, Airtable, Google Sheets, CSVs, Parquet, logs - and 40+ more. One binary, one dialect. Then hand it to an LLM over MCP. Open source, AGPL-3.0. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Apex Log MCP by Certinia](../tools/apex-log-mcp-by-certinia.md) npmjs.com Apex Log MCP Server - AI-powered Salesforce Apex debug log analysis. Find performance bottlenecks, slow methods, SOQL bottlenecks, and governor limit issues. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Apex MCP SDK by bfmvsa](../tools/apex-mcp-sdk-by-bfmvsa.md) github.com Apex SDK for building Model Context Protocol (MCP) servers natively in Salesforce - bfmvsa/mcp-apex-sdk [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Flipfactory CRM MCP](../tools/flipfactory-crm-mcp.md) npmjs.com MCP CRM Bridge - Connect your AI tools to HubSpot, Pipedrive, and more [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [HubSpot MCP by baryhuang](../tools/hubspot-mcp-by-baryhuang.md) github.com A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [IN2 Agent MCP](../tools/in2-agent-mcp.md) github.com IN2 MCP stdio server: turns Campfire Salesforce requirements into verified org changes, driven by a Claude Code supervisor. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Insaight](../tools/insaight.md) github.com LinkedIn prospect intelligence inside Claude - MCP server + 8 skills that research people, companies and comment threads, draft outreach, and learn what gets replies. - spirosbax/insaight [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [MCP Force by RapidoCloud](../tools/mcp-force-by-rapidocloud.md) github.com An MCP server to expose Salesforce APIs as tools for AI Agents - RapidoCloud/mcp-force [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [MCP-Salesforce by smn2gnt](../tools/mcp-salesforce-by-smn2gnt.md) github.com MCP Salesforce connector. Contribute to smn2gnt/MCP-Salesforce development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Mesh](../tools/mesh.md) me.sh Mesh is a beautiful rolodex and CRM for iPhone, Mac, Windows, and web, built automatically to help you manage your personal and professional relationships. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Munin](../tools/munin.md) getmunin.com The customer platform for the agentic era. MCP-first, open source, self-hostable. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Pipedrive MCP by comma-compliance](../tools/pipedrive-mcp-by-comma-compliance.md) github.com Pipedrive CRM server for the Model Context Protocol (MCP). 75 tools covering full CRUD, custom field resolution, and shortcut tools for common CRM workflows. - comma-compliance/pipedrive-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [S.C.A.L.A.](../tools/s-c-a-l-a.md) get-scala.com S.C.A.L.A. is the AI operating system for businesses. CRM, financial analysis, SARA WhatsApp AI, Process Analyzer and 20 business verticals. Try it free. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Salesforce CLI MCP](../tools/salesforce-cli-mcp.md) github.com MCP Server for interacting with Salesforce instances - salesforcecli/mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Salesforce Docs MCP by Sanket](../tools/salesforce-docs-mcp-by-sanket.md) github.com A local-first MCP server for searching Salesforce Developer Documentation. Search 360+ official Salesforce PDF docs from VS Code or Claude Desktop. - SalesforceDiariesBySanket/salesforce-docs-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Salesforce MCP by advancedcommunities](../tools/salesforce-mcp-by-advancedcommunities.md) github.com MCP server that enables AI assistants to interact with Salesforce orgs through the Salesforce CLI, providing tools for Apex execution, SOQL queries, metadata management, code analysis, and development... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Salesforce MCP by jaworjar95](../tools/salesforce-mcp-by-jaworjar95.md) github.com A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Salesforce MCP by kablewy](../tools/salesforce-mcp-by-kablewy.md) github.com Model Context Protocol server for Salesforce REST API integration - kablewy/salesforce-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Salesforce MCP by SurajAdsul](../tools/salesforce-mcp-by-surajadsul.md) github.com An MCP (Model Context Protocol) server implementation that integrates Claude with Salesforce, enabling natural language interactions with your Salesforce data and metadata. This server allows Claude to query,... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Salesforce MCP by timescale](../tools/salesforce-mcp-by-timescale.md) github.com API wrapped around our salesforce database. Contribute to timescale/tiger-salesforce-mcp-server development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Salesforce MCP by tsmztech](../tools/salesforce-mcp-by-tsmztech.md) github.com Salesforce MCP Server. Contribute to tsmztech/mcp-server-salesforce development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Salesforce MCP Lib by Damecek](../tools/salesforce-mcp-lib-by-damecek.md) context7.com Salesforce MCP Library is a local stdio bridge for Salesforce MCP endpoints using OAuth client credentials, featuring a reusable Apex MCP library and JSON-RPC 2.0 core. - Latest version [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Twenty CRM MCP](../tools/twenty-crm-mcp.md) github.com A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Vibe Prospecting MCP](../tools/vibe-prospecting-mcp.md) vibeprospecting.ai Professional prospecting inside the chat you already use. 50+ B2B data sources to build lead lists, research accounts, and find decision makers. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [mcp.so](../tools/mcp-so.md) mcp.so A community MCP server/client directory (per its public reputation as one of the earlier MCP catalog sites) - could not independently re-verify current content in this research pass. [MCP unknown](../mcp/unknown.md) · [Gate unknown](../gates/unknown.md)

- [Claude / Anthropic MCP Connector Directory](../tools/claude-anthropic-mcp-connector-directory.md) claude.com Anthropic's own curated, in-product directory of MCP connectors that Claude users can browse and one-click-connect to, filterable by use case (sales, marketing, data, etc.) and by capability (read / read-write... [MCP not applicable](../mcp/n-a.md) · [Free to start](../gates/free.md)

- [PulseMCP](../tools/pulsemcp.md) pulsemcp.com A community-run browsable directory and news hub for the MCP ecosystem (servers, clients, use cases, and a newsletter called "The Agentic Loop") that links out to third-party servers rather than hosting them. [MCP not applicable](../mcp/n-a.md) · [Free to start](../gates/free.md) · CLI: air

- [Smithery](../tools/smithery.md) smithery.ai A registry and distribution marketplace for MCP servers - "publish once, install anywhere" - that indexes and distributes third-party servers rather than hosting them itself, plus an integrated... [MCP not applicable](../mcp/n-a.md) · [Free to start](../gates/free.md) · CLI: smithery

- [Glama (MCP directory)](../tools/glama.md) glama.ai A large searchable registry/catalog of open-source MCP servers (77,000+ listed as of this check), filterable by language, hosting type (remote/local/hybrid), capability, and category; also offers separate... [MCP not applicable](../mcp/n-a.md) · [Gate unknown](../gates/unknown.md)
