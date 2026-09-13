# RevOps Infra: 31 tools, 29 with an official MCP server

> The systems of record, the pipes between them, and the low-code layer a GTM engineer builds on top.... 31 tools counted, 29 with an official MCP server and 14 free to start.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[By category](index.md) / RevOps Infra

**06 · revops-infra**

## RevOps Infra

The systems of record, the pipes between them, and the low-code layer a GTM engineer builds on top. Most of category has genuine AI now in one specific corner of the product - Agentforce, Breeze, AI Agent nodes - bolted onto a much larger base of plain rules-based automation. This file tries to draw that line honestly for each one.

- **entries in this file**: 31

- **Official MCP**: 29
- **MCP unknown**: 1
- **No MCP found**: 1

- **ship a CLI (official) as of 2026-09-13**: 9

- **Free to start**: 14
- **Paid, self-serve**: 12
- **Enterprise only**: 5

Source file: 06-revops-infra.md · content sha256 92bc241926874ea0... · counts reconciled against tools_recount.py at build time.

- [The 29 with an MCP server](../lists/mcp-revops-infra.md)

- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

- [Airbyte](../tools/airbyte.md) airbyte.com Open-source/cloud ELT platform with 600+ connectors moving data from SaaS tools and databases into warehouses; increasingly positions itself as a context layer for AI agents via a hosted Context Store. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: airbyte-config (community)

- [Attio](../tools/attio.md) attio.com A CRM built around a flexible, user-defined data model (not fixed contact/company/deal objects) with real-time sync and an API-first architecture. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: attio

- [Cargo](../tools/cargo.md) getcargo.ai A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment, scoring, routing, CRM sync - as code, run by AI agents. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: cargo

- [Census (now operates as "Fivetran Activations")](../tools/census.md) getcensus.com Was a standalone reverse-ETL tool for syncing warehouse data (Snowflake, BigQuery, etc.) into GTM tools like Salesforce/HubSpot without code; the product now lives inside Fivetran as "Activations," same... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Fivetran](../tools/fivetran.md) fivetran.com Managed ELT pipeline platform; for GTM purposes, the relevant piece is its Salesforce/HubSpot/Marketo/Outreach/Salesloft/Gong/Zendesk connectors that land CRM and GTM-tool data in a warehouse, plus... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: fivetran-cli (community)

- [Google BigQuery](../tools/google-bigquery.md) cloud.google.com Google Cloud's serverless data warehouse, where many RevOps teams land CRM, product and billing data for modelling and reporting; a first-party remote MCP server exposes dataset and table metadata and SQL... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Hightouch](../tools/hightouch.md) hightouch.com A CDP/reverse-ETL platform that syncs warehouse data (Snowflake, BigQuery, Databricks, Redshift) to 300+ downstream tools (ad platforms, CRMs, marketing automation) for audience activation and personalization. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [HubSpot](../tools/hubspot.md) hubspot.com An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: hs

- [monday.com (monday CRM)](../tools/monday-com.md) monday.com A work-management platform whose CRM product runs pipelines, contacts, accounts and deal activity as boards and items, with a first-party remote MCP server that lets an AI client read and update that data on... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: mapps

- [n8n](../tools/n8n.md) n8n.io A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes, usable self-hosted or as managed cloud. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Pipedrive](../tools/pipedrive.md) pipedrive.com A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Retool](../tools/retool.md) retool.com A low-code platform for building internal tools/dashboards/admin panels on top of databases and APIs; in a GTM context, used to build custom RevOps tooling - lead-routing consoles, deal-desk approval apps,... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: retool (community)

- [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md) snowflake.com Cloud data warehouse that acts as the central store where GTM data (CRM, product usage, marketing, support) gets modeled and joined; increasingly the platform other reverse-ETL tools (Hightouch, Fivetran... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: snowflake-cli

- [Zapier](../tools/zapier.md) zapier.com A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate agent product. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · CLI: zapier-platform

- [Affinity](../tools/affinity.md) affinity.co A relationship-intelligence CRM for deal teams that auto-builds the contact graph from email and calendar activity and scores relationship strength, rather than relying on reps to log activity. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Close (Close CRM)](../tools/close.md) close.com A sales CRM built for inside-sales teams with built-in calling, email, and SMS alongside pipeline/lead management - a communications-plus-CRM combo rather than a pure system of record. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [dbt (dbt platform remote MCP)](../tools/dbt.md) getdbt.com The transformation layer of the modern data stack: SQL models, tests and documentation compiled and run against a warehouse, with a hosted "dbt platform" (formerly dbt Cloud) that adds scheduling, a Semantic... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · CLI: dbt

- [Hex](../tools/hex.md) hex.tech A collaborative data workspace (SQL and Python notebooks, published apps, a conversational "Threads" analysis mode) used by data and RevOps teams to answer questions on top of the warehouse. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [HighLevel (GoHighLevel)](../tools/highlevel.md) gohighlevel.com An all-in-one agency CRM covering contacts, pipelines, conversations, calendars, payments and campaign automation across many client sub-accounts from one place. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Make](../tools/make.md) make.com A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent and natural-language-build features layered on top. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Microsoft Dynamics 365 Sales](../tools/microsoft-dynamics-365-sales.md) microsoft.com Microsoft's enterprise CRM for sales, built on Dataverse and the Power Platform, covering leads, opportunities, accounts and forecasting, with a first-party MCP server that lets Copilot Studio agents and other... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Nutshell CRM](../tools/nutshell-crm.md) nutshell.com An SMB CRM covering leads, companies, people, pipelines and activity reporting, with email and calendar sync and built-in marketing tools, and a read-only MCP server that lets an assistant search that data and... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Octave](../tools/octave.md) octavehq.com A GTM context engine that stores a company's ICP, personas, positioning, competitors, proof points, and objections as one structured model, then serves that model to sequences, scripts, and AI agents at... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Ortto](../tools/ortto.md) ortto.com A combined customer data platform and marketing automation tool for building multi-channel journeys across email, SMS, push, in-app and live chat. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Superblocks](../tools/superblocks.md) superblocks.com A platform for building - and more distinctively, governing - AI-generated internal apps: lets business teams build apps (including importing prototypes from Claude, Lovable, or Replit) while giving... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · CLI: superblocks

- [Zoho CRM](../tools/zoho-crm.md) zoho.com A full CRM platform for leads, contacts, deals, workflow automation and customisation, sold at the low end of the market, which in 2026 shipped four separately scoped MCP servers so an agent can be given... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Looker](../tools/looker.md) cloud.google.com Google Cloud's governed BI platform (LookML semantic model, explores, Looks, dashboards, embedded analytics) that sits on top of a warehouse; two first-party MCP routes exist, a local MCP Toolbox prebuilt... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md) salesforce.com A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code app layer, with Agentforce as a layer on top for configuring autonomous AI agents that read... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · CLI: sf

- [Syncari](../tools/syncari.md) syncari.com An "agentic master data management" (MDM) platform that unifies data across CRM/ERP/warehouse systems in real time and exposes that unified data to both humans (dashboards/BI) and AI agents. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Default](../tools/default.md) default.com An inbound go-to-market platform unifying revenue-stack data (a "Tables" data layer) with AI-agent-built workflows for lead routing, qualification, and meeting scheduling. [MCP unknown](../mcp/unknown.md) · [Enterprise only](../gates/enterprise-only.md)

- [Openprise](../tools/openprise.md) openprisetech.com A no-code RevOps data-orchestration platform automating GTM data workflows - list loading, cleansing, deduplication, enrichment, scoring/segmentation, and lead routing across the marketing/sales stack. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)
