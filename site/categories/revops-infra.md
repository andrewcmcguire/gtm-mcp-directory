# RevOps Infra: 23 tools, 21 with an official MCP server

> The systems of record, the pipes between them, and the low-code layer a GTM engineer builds on top.... 23 tools counted, 21 with an official MCP server and 12 free to start.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[By category](index.md) / RevOps Infra

**06 · revops-infra**

## RevOps Infra

The systems of record, the pipes between them, and the low-code layer a GTM engineer builds on top. Most of category has genuine AI now in one specific corner of the product - Agentforce, Breeze, AI Agent nodes - bolted onto a much larger base of plain rules-based automation. This file tries to draw that line honestly for each one.

- **entries in this file**: 23

- **Official MCP**: 21
- **MCP unknown**: 1
- **No MCP found**: 1

- **Free to start**: 12
- **Paid, self-serve**: 7
- **Enterprise only**: 4

Source file: 06-revops-infra.md · content sha256 7121303ec7ab7bdf... · counts reconciled against tools_recount.py at build time.

- [The 21 with an MCP server](../lists/mcp-revops-infra.md)

- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

- [Airbyte](../tools/airbyte.md) airbyte.com Open-source/cloud ELT platform with 600+ connectors moving data from SaaS tools and databases into warehouses; increasingly positions itself as a context layer for AI agents via a hosted Context Store. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Attio](../tools/attio.md) attio.com A CRM built around a flexible, user-defined data model (not fixed contact/company/deal objects) with real-time sync and an API-first architecture. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Cargo](../tools/cargo.md) getcargo.ai A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment, scoring, routing, CRM sync - as code, run by AI agents. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Census (now operates as "Fivetran Activations")](../tools/census.md) getcensus.com Was a standalone reverse-ETL tool for syncing warehouse data (Snowflake, BigQuery, etc.) into GTM tools like Salesforce/HubSpot without code; the product now lives inside Fivetran as "Activations," same... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Fivetran](../tools/fivetran.md) fivetran.com Managed ELT pipeline platform; for GTM purposes, the relevant piece is its Salesforce/HubSpot/Marketo/Outreach/Salesloft/Gong/Zendesk connectors that land CRM and GTM-tool data in a warehouse, plus... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Hightouch](../tools/hightouch.md) hightouch.com A CDP/reverse-ETL platform that syncs warehouse data (Snowflake, BigQuery, Databricks, Redshift) to 300+ downstream tools (ad platforms, CRMs, marketing automation) for audience activation and personalization. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [HubSpot](../tools/hubspot.md) hubspot.com An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [n8n](../tools/n8n.md) n8n.io A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes, usable self-hosted or as managed cloud. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Pipedrive](../tools/pipedrive.md) pipedrive.com A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Retool](../tools/retool.md) retool.com A low-code platform for building internal tools/dashboards/admin panels on top of databases and APIs; in a GTM context, used to build custom RevOps tooling - lead-routing consoles, deal-desk approval apps,... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md) snowflake.com Cloud data warehouse that acts as the central store where GTM data (CRM, product usage, marketing, support) gets modeled and joined; increasingly the platform other reverse-ETL tools (Hightouch, Fivetran... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Zapier](../tools/zapier.md) zapier.com A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate agent product. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Affinity](../tools/affinity.md) affinity.co A relationship-intelligence CRM for deal teams that auto-builds the contact graph from email and calendar activity and scores relationship strength, rather than relying on reps to log activity. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Close (Close CRM)](../tools/close.md) close.com A sales CRM built for inside-sales teams with built-in calling, email, and SMS alongside pipeline/lead management - a communications-plus-CRM combo rather than a pure system of record. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [HighLevel (GoHighLevel)](../tools/highlevel.md) gohighlevel.com An all-in-one agency CRM covering contacts, pipelines, conversations, calendars, payments and campaign automation across many client sub-accounts from one place. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Make](../tools/make.md) make.com A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent and natural-language-build features layered on top. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Octave](../tools/octave.md) octavehq.com A GTM context engine that stores a company's ICP, personas, positioning, competitors, proof points, and objections as one structured model, then serves that model to sequences, scripts, and AI agents at... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Ortto](../tools/ortto.md) ortto.com A combined customer data platform and marketing automation tool for building multi-channel journeys across email, SMS, push, in-app and live chat. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Superblocks](../tools/superblocks.md) superblocks.com A platform for building - and more distinctively, governing - AI-generated internal apps: lets business teams build apps (including importing prototypes from Claude, Lovable, or Replit) while giving... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md) salesforce.com A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code app layer, with Agentforce as a layer on top for configuring autonomous AI agents that read... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Syncari](../tools/syncari.md) syncari.com An "agentic master data management" (MDM) platform that unifies data across CRM/ERP/warehouse systems in real time and exposes that unified data to both humans (dashboards/BI) and AI agents. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Default](../tools/default.md) default.com An inbound go-to-market platform unifying revenue-stack data (a "Tables" data layer) with AI-agent-built workflows for lead routing, qualification, and meeting scheduling. [MCP unknown](../mcp/unknown.md) · [Enterprise only](../gates/enterprise-only.md)

- [Openprise](../tools/openprise.md) openprisetech.com A no-code RevOps data-orchestration platform automating GTM data workflows - list loading, cleansing, deduplication, enrichment, scoring/segmentation, and lead routing across the marketing/sales stack. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)
