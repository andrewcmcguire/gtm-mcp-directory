# Systems of record and plumbing - GTM jobs an agent can ask for

> Read, write and move the data the rest of the stack argues about. 6 jobs and 79 tagged entries in The GTM MCP Directory.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[By job](index.md) / Systems of record and plumbing

**Job family**

## Systems of record and plumbing

Read, write and move the data the rest of the stack argues about. 6 jobs, 79 tagged entries, 50 distinct entries across the family.

- [Read CRM records](read-crm-records.md) - 13 tools · 10 official MCP. Query contacts, accounts, deals and activity out of a system of record.
- [Write CRM records](write-crm-records.md) - 28 tools · 18 official MCP. Create or update records, log activity, or push data back into a system of record.
- [Query a data warehouse](query-data-warehouse.md) - 2 tools · 2 official MCP. Run analytical queries against the modeled GTM data, not against the CRM.
- [Sync records between systems](sync-records-between-systems.md) - 9 tools · 8 official MCP. Move data between the warehouse, the CRM and the rest of the stack. ETL, reverse ETL, MDM.
- [Run an automation workflow](run-automation-workflow.md) - 18 tools · 10 official MCP. Trigger or execute a multi-step workflow across tools, deterministic or agent-driven.
- [Route an inbound lead](route-inbound-lead.md) - 9 tools · 4 official MCP. Decide which rep, queue or territory an inbound lead or signal belongs to and hand it over.

### Every entry tagged with a job in this family

Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.

- [Airbyte](../tools/airbyte.md) airbyte.com Open-source/cloud ELT platform with 600+ connectors moving data from SaaS tools and databases into warehouses; increasingly positions itself as a context layer for AI agents via a hosted Context Store. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Apideck](../tools/apideck.md) apideck.com A unified API that normalises 200+ SaaS connectors into single data models, exposed as one MCP endpoint covering CRM, accounting, HRIS, ATS, file storage and issue tracking. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Attio](../tools/attio.md) attio.com A CRM built around a flexible, user-defined data model (not fixed contact/company/deal objects) with real-time sync and an API-first architecture. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Cargo](../tools/cargo.md) getcargo.ai A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment, scoring, routing, CRM sync - as code, run by AI agents. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Fathom](../tools/fathom.md) fathom.video Free AI meeting recorder/notetaker that transcribes calls and generates summaries, action items, and CRM sync. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Fireflies.ai](../tools/fireflies-ai.md) fireflies.ai Records and transcribes meetings and exposes the data through an open GraphQL API and an in-app AI assistant ("AskFred") for summaries, search, and CRM writeback. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Fivetran](../tools/fivetran.md) fivetran.com Managed ELT pipeline platform; for GTM purposes, the relevant piece is its Salesforce/HubSpot/Marketo/Outreach/Salesloft/Gong/Zendesk connectors that land CRM and GTM-tool data in a warehouse, plus... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Hightouch](../tools/hightouch.md) hightouch.com A CDP/reverse-ETL platform that syncs warehouse data (Snowflake, BigQuery, Databricks, Redshift) to 300+ downstream tools (ad platforms, CRMs, marketing automation) for audience activation and personalization. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [HubSpot](../tools/hubspot.md) hubspot.com An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [n8n](../tools/n8n.md) n8n.io A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes, usable self-hosted or as managed cloud. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Pipedrive](../tools/pipedrive.md) pipedrive.com A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Retool](../tools/retool.md) retool.com A low-code platform for building internal tools/dashboards/admin panels on top of databases and APIs; in a GTM context, used to build custom RevOps tooling - lead-routing consoles, deal-desk approval apps,... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md) snowflake.com Cloud data warehouse that acts as the central store where GTM data (CRM, product usage, marketing, support) gets modeled and joined; increasingly the platform other reverse-ETL tools (Hightouch, Fivetran... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Zapier](../tools/zapier.md) zapier.com A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate agent product. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Affinity](../tools/affinity.md) affinity.co A relationship-intelligence CRM for deal teams that auto-builds the contact graph from email and calendar activity and scores relationship strength, rather than relying on reps to log activity. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Airspeed (formerly Glyphic)](../tools/airspeed.md) goairspeed.com Records and analyses sales calls, then scores deals against playbooks and writes structured output back into the CRM. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Attention](../tools/attention.md) attention.com Captures, transcribes, and analyzes sales and customer conversations, automatically syncing structured insights to the CRM. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Chili Piper](../tools/chili-piper.md) chilipiper.com Inbound lead-routing and instant meeting-booking platform ("Concierge") that qualifies web-form leads and books them directly onto the right rep's calendar in real time. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Chili Piper](../tools/chili-piper.md) chilipiper.com Inbound lead routing and meeting-scheduling platform - converts web-form submissions and inbound leads into booked meetings in seconds, with rep-availability and fairness-rule logic. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Inbound & PLG Chat](../categories/inbound-plg-chat.md) · Cross listed, canonical home is Scheduling & Routing

- [Clay](../tools/clay.md) clay.com A spreadsheet-style workflow/orchestration tool that runs lead and company records through "waterfall" lookups across 100-200+ third-party data providers (Apollo, Lusha, Clearbit, etc.) and chains automation... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Close (Close CRM)](../tools/close.md) close.com A sales CRM built for inside-sales teams with built-in calling, email, and SMS alongside pipeline/lead management - a communications-plus-CRM combo rather than a pure system of record. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Grain](../tools/grain.md) grain.com AI meeting notetaker that records and transcribes calls and builds a searchable, cross-meeting library synced to the CRM. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md)

- [HighLevel (GoHighLevel)](../tools/highlevel.md) gohighlevel.com An all-in-one agency CRM covering contacts, pipelines, conversations, calendars, payments and campaign automation across many client sub-accounts from one place. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Make](../tools/make.md) make.com A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent and natural-language-build features layered on top. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Ortto](../tools/ortto.md) ortto.com A combined customer data platform and marketing automation tool for building multi-channel journeys across email, SMS, push, in-app and live chat. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Otter.ai](../tools/otter-ai.md) otter.ai AI meeting notetaker whose Sales Agent variant pulls CRM context before a call and flags objections, competitor mentions, and pricing discussion live, then writes summaries and next steps back to the CRM. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Outreach](../tools/outreach.md) outreach.ai Sales engagement platform for building, running, and tracking multichannel outbound sequences (email, call, social) and rep activity, tied into a CRM. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md) salesforce.com A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code app layer, with Agentforce as a layer on top for configuring autonomous AI agents that read... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [RevOps Infra](../categories/revops-infra.md)

- [Salesloft](../tools/salesloft.md) salesloft.com Sales engagement platform (merged with Clari in Dec 2025) for multichannel outbound cadences, call/email execution, and rep activity tracking that feeds forecasting. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Surfe](../tools/surfe.md) surfe.com A Chrome extension plus API that pulls contacts and companies off LinkedIn, runs them through a multi-vendor waterfall to find verified emails and mobile numbers, and pushes the records into a CRM. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Syncari](../tools/syncari.md) syncari.com An "agentic master data management" (MDM) platform that unifies data across CRM/ERP/warehouse systems in real time and exposes that unified data to both humans (dashboards/BI) and AI agents. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [RevOps Infra](../categories/revops-infra.md)

- [RevenueHero](../tools/revenuehero.md) revenuehero.io Instant meeting-scheduling and inbound-lead-routing tool that qualifies web-form leads against CRM data and books them directly onto the right rep's calendar without a redirect. [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Clari Copilot](../tools/clari-copilot.md) clari.com Records and transcribes sales calls in real time and surfaces live coaching prompts, deal-risk flags, and auto-generated CRM updates during and after the call. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Copy.ai (GTM AI Platform)](../tools/copy-ai.md) copy.ai Pivoted from an AI copywriting tool to a workflow-building platform ("Copy Agents") that automates GTM tasks - prospecting/lead research, inbound enrichment, content generation, deal analysis - via user-built... [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [AI SDRs](../categories/ai-sdr-agents.md)

- [Jiminny](../tools/jiminny.md) jiminny.com Records, transcribes, and scores sales calls, syncing action items and summaries into the CRM. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Default](../tools/default.md) default.com An inbound go-to-market platform unifying revenue-stack data (a "Tables" data layer) with AI-agent-built workflows for lead routing, qualification, and meeting scheduling. [MCP unknown](../mcp/unknown.md) · [Enterprise only](../gates/enterprise-only.md) · [RevOps Infra](../categories/revops-infra.md)

- [Default](../tools/default.md) default.com "Agentic GTM infrastructure" platform unifying CRM, website-form, and enrichment data into one identity-resolved model, with lead routing, scheduling, enrichment, and workflow automation built on top. [MCP unknown](../mcp/unknown.md) · [Enterprise only](../gates/enterprise-only.md) · [Scheduling & Routing](../categories/scheduling-routing.md) · Cross listed, canonical home is RevOps Infra

- [Groove](../tools/groove.md) groove.co Salesforce-native sales engagement and prospecting platform - multichannel outbound automation and activity capture - operated as a module of the Clari revenue platform since its 2023 acquisition. [MCP unknown](../mcp/unknown.md) · [Enterprise only](../gates/enterprise-only.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [LeanData](../tools/leandata.md) leandata.com GTM lead-routing/orchestration platform for Salesforce-centric revenue teams - routes leads, signals, and buying-group activity to the right rep/queue across the customer lifecycle, plus a scheduling add-on... [MCP unknown](../mcp/unknown.md) · [Enterprise only](../gates/enterprise-only.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Pipedrive (AI Sales Assistant / forecasting)](../tools/pipedrive.md) pipedrive.com Pipedrive's built-in AI-driven forecasting layer - not a separately branded "Insights" product, but the CRM's AI Sales Assistant plus probability-weighted pipeline forecasting math. See 06-revops-infra.md for... [No MCP found](../mcp/none-found.md) · [Free to start](../gates/free.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md) · Cross listed, canonical home is RevOps Infra

- [HubSpot (AI Forecasting)](../tools/hubspot.md) hubspot.com HubSpot's forecasting tool inside Sales Hub/Service Hub, turning pipeline data into revenue predictions via weighted-pipeline calculations plus an "AI forecasting" layer shown in-product. See... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md) · Cross listed, canonical home is RevOps Infra

- [Kixie](../tools/kixie.md) kixie.com Sales engagement / power-dialer platform (PowerCall) with multi-line parallel dialing, local-presence calling, and CRM-embedded calling/texting. [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Aviso](../tools/aviso.md) aviso.com AI revenue operations platform combining pipeline forecasting, conversation/deal intelligence, and agentic workflow automation for sales, RevOps, and customer success teams. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [Ebsta](../tools/ebsta.md) ebsta.com Revenue-intelligence add-on for Salesforce/HubSpot that syncs email and calendar activity into the CRM and layers on relationship scoring, conversation capture, and pipeline forecasting. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [Momentum](../tools/momentum.md) momentum.io Turns sales call and CRM activity into automatic Slack deal-channel updates, deal-risk alerts, and CRM field updates ("revenue orchestration"). [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Openprise](../tools/openprise.md) openprisetech.com A no-code RevOps data-orchestration platform automating GTM data workflows - list loading, cleansing, deduplication, enrichment, scoring/segmentation, and lead routing across the marketing/sales stack. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md) · [RevOps Infra](../categories/revops-infra.md)

- [Salesforce Agentforce (SDR Agent)](../tools/salesforce-agentforce.md) salesforce.com A prebuilt agent within Salesforce's Agentforce platform intended to handle inbound lead engagement and outbound prospecting conversations natively inside Sales Cloud, escalating to a human rep once a prospect... [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md) · [AI SDRs](../categories/ai-sdr-agents.md) · Cross listed, canonical home is RevOps Infra

- [Tofu](../tools/tofu.md) tofuhq.com A campaign-automation platform ("Agentic GTM") that runs always-on, personalized outbound/nurture/re-engagement campaigns inside an existing CRM and sales-engagement stack, rather than acting as a standalone... [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md) · [AI SDRs](../categories/ai-sdr-agents.md)

- [Kronologic](../tools/kronologic.md) kronologic.com Automated meeting-booking platform that sends calendar invites directly (not just booking links) on a rep's behalf and negotiates meeting times over email, aimed mainly at customer-expansion motions (renewals,... [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Salesroom](../tools/salesroom.md) salesroom.com Real-time AI video-conferencing platform for sales calls that coaches reps live against playbooks (MEDDIC, Challenger, BANT, Sandler) during the meeting. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md) · [Conversation Intel](../categories/conversation-intel.md)
