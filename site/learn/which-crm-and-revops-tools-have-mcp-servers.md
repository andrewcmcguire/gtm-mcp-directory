# CRM and RevOps tools with MCP servers: 22 of 23, counted

> 22 of the 23 revops infra tools in this directory have an MCP server: 22 official and 0 community. The list with server URLs and access gates. Counted 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / What the data says

**What the data says**

# Which CRM and RevOps tools have MCP servers?

**The short answer**

22 of the 23 revops infra entries in this directory have an MCP server: 22 built and maintained by the vendor and 0 built by somebody else. 12 are free to start and 4 need a contract before anybody gets an API key.

This is the layer an agent has to reach before anything else matters. A GTM agent that cannot read and write the system of record is a research assistant, not an operator. It is also, by some distance, the best covered layer in this directory.

The systems of record, the pipes between them, and the low-code layer a GTM engineer builds on top. Most of category has genuine AI now in one specific corner of the product - Agentforce, Breeze, AI Agent nodes - bolted onto a much larger base of plain rules-based automation. This file tries to draw that line honestly for each one.

## The ones an agent can call

- [Airbyte](../tools/airbyte.md) Official MCP · Free to start
Open-source/cloud ELT platform with 600+ connectors moving data from SaaS tools and databases into warehouses; increasingly positions itself as a...
- [Attio](../tools/attio.md) Official MCP · Free to start
A CRM built around a flexible, user-defined data model (not fixed contact/company/deal objects) with real-time sync and an API-first architecture.
- [Cargo](../tools/cargo.md) Official MCP · Free to start
A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment,...
- [Census (now operates as "Fivetran Activations")](../tools/census.md) Official MCP · Free to start
Was a standalone reverse-ETL tool for syncing warehouse data (Snowflake, BigQuery, etc.) into GTM tools like Salesforce/HubSpot without code; the...
- [Fivetran](../tools/fivetran.md) Official MCP · Free to start
Managed ELT pipeline platform; for GTM purposes, the relevant piece is its Salesforce/HubSpot/Marketo/Outreach/Salesloft/Gong/Zendesk connectors that...
- [Hightouch](../tools/hightouch.md) Official MCP · Free to start
A CDP/reverse-ETL platform that syncs warehouse data (Snowflake, BigQuery, Databricks, Redshift) to 300+ downstream tools (ad platforms, CRMs,...
- [HubSpot](../tools/hubspot.md) Official MCP · Free to start
An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform.
- [n8n](../tools/n8n.md) Official MCP · Free to start
A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes, usable self-hosted or as managed cloud.
- [Pipedrive](../tools/pipedrive.md) Official MCP · Free to start
A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams.
- [Retool](../tools/retool.md) Official MCP · Free to start
A low-code platform for building internal tools/dashboards/admin panels on top of databases and APIs; in a GTM context, used to build custom RevOps...
- [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md) Official MCP · Free to start
Cloud data warehouse that acts as the central store where GTM data (CRM, product usage, marketing, support) gets modeled and joined; increasingly the...
- [Zapier](../tools/zapier.md) Official MCP · Free to start
A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate agent product.
- [Affinity](../tools/affinity.md) Official MCP · Paid, self-serve
A relationship-intelligence CRM for deal teams that auto-builds the contact graph from email and calendar activity and scores relationship strength,...
- [Close (Close CRM)](../tools/close.md) Official MCP · Paid, self-serve
A sales CRM built for inside-sales teams with built-in calling, email, and SMS alongside pipeline/lead management - a communications-plus-CRM combo...
- [HighLevel (GoHighLevel)](../tools/highlevel.md) Official MCP · Paid, self-serve
An all-in-one agency CRM covering contacts, pipelines, conversations, calendars, payments and campaign automation across many client sub-accounts...
- [Make](../tools/make.md) Official MCP · Paid, self-serve
A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent and natural-language-build features...
- [Octave](../tools/octave.md) Official MCP · Paid, self-serve
A GTM context engine that stores a company's ICP, personas, positioning, competitors, proof points, and objections as one structured model, then...
- [Ortto](../tools/ortto.md) Official MCP · Paid, self-serve
A combined customer data platform and marketing automation tool for building multi-channel journeys across email, SMS, push, in-app and live chat.
- [Superblocks](../tools/superblocks.md) Official MCP · Paid, self-serve
A platform for building - and more distinctively, governing - AI-generated internal apps: lets business teams build apps (including importing...
- [Default](../tools/default.md) Official MCP · Enterprise only
An inbound go-to-market platform unifying revenue-stack data (a "Tables" data layer) with AI-agent-built workflows for lead routing, qualification,...
- [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md) Official MCP · Enterprise only
A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code app layer, with Agentforce as a layer on...
- [Syncari](../tools/syncari.md) Official MCP · Enterprise only
An "agentic master data management" (MDM) platform that unifies data across CRM/ERP/warehouse systems in real time and exposes that unified data to...

## The rest of the category

1 entries here had no server found, or the check could not settle it. That is not a verdict on the tools. It is a statement about what an agent can reach today.

- [Openprise](../tools/openprise.md) No MCP found · Enterprise only
A no-code RevOps data-orchestration platform automating GTM data workflows - list loading, cleansing, deduplication, enrichment,...

## The gate, which is the second question

| Gate | Entries |
|---|---|
| [Free to start](../gates/free.md) | 12 |
| [Paid, self-serve](../gates/paid.md) | 7 |
| [Enterprise only](../gates/enterprise-only.md) | 4 |

Counted 2026-08-25. Source file 06-revops-infra.md, content sha256 3e4d8d4f1635263c...

## Sources

- [The GTM MCP Directory, RevOps Infra](../categories/revops-infra.md) this site
- [RevOps Infra tools with MCP servers](../lists/mcp-revops-infra.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-25. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)
- [Which GTM tools have official MCP servers?](which-gtm-tools-have-official-mcp-servers.md)
- [How many GTM tools have MCP servers?](how-many-gtm-tools-have-mcp-servers.md)
- [What is a GTM tech stack?](what-is-a-gtm-tech-stack.md)

## In the directory

- [RevOps Infra](../categories/revops-infra.md)
- [With MCP servers](../lists/mcp-revops-infra.md)
