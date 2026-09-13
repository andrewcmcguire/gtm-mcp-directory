# CRM and RevOps tools with MCP servers: 30 of 42, counted

> 30 of the 42 revops infra tools in this directory have an MCP server: 29 official and 1 community. The list with server URLs and access gates. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Learn](index.md) / What the data says

**What the data says**

# Which CRM and RevOps tools have MCP servers?

**The short answer**

30 of the 42 revops infra entries in this directory have an MCP server: 29 built and maintained by the vendor and 1 built by somebody else. 14 are free to start and 5 need a contract before anybody gets an API key.

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
- [Google BigQuery](../tools/google-bigquery.md) Official MCP · Free to start
Google Cloud's serverless data warehouse, where many RevOps teams land CRM, product and billing data for modelling and reporting; a first-party...
- [Hightouch](../tools/hightouch.md) Official MCP · Free to start
A CDP/reverse-ETL platform that syncs warehouse data (Snowflake, BigQuery, Databricks, Redshift) to 300+ downstream tools (ad platforms, CRMs,...
- [HubSpot](../tools/hubspot.md) Official MCP · Free to start
An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform.
- [monday.com (monday CRM)](../tools/monday-com.md) Official MCP · Free to start
A work-management platform whose CRM product runs pipelines, contacts, accounts and deal activity as boards and items, with a first-party remote MCP...
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
- [dbt (dbt platform remote MCP)](../tools/dbt.md) Official MCP · Paid, self-serve
The transformation layer of the modern data stack: SQL models, tests and documentation compiled and run against a warehouse, with a hosted "dbt...
- [Hex](../tools/hex.md) Official MCP · Paid, self-serve
A collaborative data workspace (SQL and Python notebooks, published apps, a conversational "Threads" analysis mode) used by data and RevOps teams to...
- [HighLevel (GoHighLevel)](../tools/highlevel.md) Official MCP · Paid, self-serve
An all-in-one agency CRM covering contacts, pipelines, conversations, calendars, payments and campaign automation across many client sub-accounts...
- [Make](../tools/make.md) Official MCP · Paid, self-serve
A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent and natural-language-build features...
- [Microsoft Dynamics 365 Sales](../tools/microsoft-dynamics-365-sales.md) Official MCP · Paid, self-serve
Microsoft's enterprise CRM for sales, built on Dataverse and the Power Platform, covering leads, opportunities, accounts and forecasting, with a...
- [Nutshell CRM](../tools/nutshell-crm.md) Official MCP · Paid, self-serve
An SMB CRM covering leads, companies, people, pipelines and activity reporting, with email and calendar sync and built-in marketing tools, and a...
- [Octave](../tools/octave.md) Official MCP · Paid, self-serve
A GTM context engine that stores a company's ICP, personas, positioning, competitors, proof points, and objections as one structured model, then...
- [Ortto](../tools/ortto.md) Official MCP · Paid, self-serve
A combined customer data platform and marketing automation tool for building multi-channel journeys across email, SMS, push, in-app and live chat.
- [Superblocks](../tools/superblocks.md) Official MCP · Paid, self-serve
A platform for building - and more distinctively, governing - AI-generated internal apps: lets business teams build apps (including importing...
- [Zoho CRM](../tools/zoho-crm.md) Official MCP · Paid, self-serve
A full CRM platform for leads, contacts, deals, workflow automation and customisation, sold at the low end of the market, which in 2026 shipped four...
- [Looker](../tools/looker.md) Official MCP · Enterprise only
Google Cloud's governed BI platform (LookML semantic model, explores, Looks, dashboards, embedded analytics) that sits on top of a warehouse; two...
- [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md) Official MCP · Enterprise only
A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code app layer, with Agentforce as a layer on...
- [Syncari](../tools/syncari.md) Official MCP · Enterprise only
An "agentic master data management" (MDM) platform that unifies data across CRM/ERP/warehouse systems in real time and exposes that unified data to...
- [Morphed](../tools/morphed.md) Community MCP · Gate unknown
Morphed defines what your CRM must do, audits the source against it, then builds, migrates and verifies it - and keeps the plan live for the first 30...

## The rest of the category

12 entries here had no server found, or the check could not settle it. That is not a verdict on the tools. It is a statement about what an agent can reach today.

- [Default](../tools/default.md) MCP unknown · Enterprise only
An inbound go-to-market platform unifying revenue-stack data (a "Tables" data layer) with AI-agent-built workflows for lead routing, qualification,...
- [Openprise](../tools/openprise.md) No MCP found · Enterprise only
A no-code RevOps data-orchestration platform automating GTM data workflows - list loading, cleansing, deduplication, enrichment,...
- [Apsona](../tools/apsona.md) No MCP found · Gate unknown
All-in-one Salesforce data management-run reports, merge documents, clean records, and update data with no code. Apsona works natively inside...
- [Boomi](../tools/boomi.md) No MCP found · Gate unknown
Turn complexity into endless possibility with Boomi, a single platform that integrates applications, APIs, data, and AI agents.
- [CloudFiles](../tools/cloudfiles.md) No MCP found · Gate unknown
CloudFiles is an enterprise-grade, Salesforce-native platform to manage, process, generate, and automate every document without leaving Salesforce....
- [Databox](../tools/databox.md) No MCP found · Gate unknown
Databox is the agentic analytics platform that brings performance data, business context, and AI workflows together, so your team or agents act...
- [LinkPoint Connect](../tools/linkpoint-connect.md) No MCP found · Gate unknown
LinkPoint360 is a leading provider of email integration solutions for Salesforce & Microsoft Dynamics. Increase your productivity and CRM adoption...
- [Relate](../tools/relate.md) No MCP found · Gate unknown
Relate is a modern sales CRM platform that lets you bring your entire team together to collaborate on sales.
- [Streak](../tools/streak.md) No MCP found · Gate unknown
Manage sales and customer relationships directly inside Gmail. Streak is the CRM your team will actually use-integrated, smart, and loved by 750,000+...
- [Suger](../tools/suger.md) No MCP found · Gate unknown
Suger automates cloud GTM for ISVs selling on AWS, GCP, and Azure Marketplace. Streamline co-sell, private offers, metering, and CRM sync in one...
- [Tray.ai](../tools/tray-ai.md) No MCP found · Gate unknown
Tray.ai is the AI-native enterprise iPaaS for building AI agents, governing Model Context Protocol (MCP), and integrating 700+ apps - orchestration...
- [Vertify](../tools/vertify.md) No MCP found · Gate unknown
Unlock the full potential of your data with our enterprise data integration platform. Streamline data management and access to insights.

## The gate, which is the second question

| Gate | Entries |
|---|---|
| [Free to start](../gates/free.md) | 14 |
| [Paid, self-serve](../gates/paid.md) | 12 |
| [Enterprise only](../gates/enterprise-only.md) | 5 |
| [Gate unknown](../gates/unknown.md) | 11 |

Counted 2026-09-12. Source file 06-revops-infra.md, content sha256 1bf804b8ceb75116...

## Sources

- [The GTM MCP Directory, RevOps Infra](../categories/revops-infra.md) this site
- [RevOps Infra tools with MCP servers](../lists/mcp-revops-infra.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-12. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)
- [Which GTM tools have official MCP servers?](which-gtm-tools-have-official-mcp-servers.md)
- [How many GTM tools have MCP servers?](how-many-gtm-tools-have-mcp-servers.md)
- [What is a GTM tech stack?](what-is-a-gtm-tech-stack.md)

## In the directory

- [RevOps Infra](../categories/revops-infra.md)
- [With MCP servers](../lists/mcp-revops-infra.md)
