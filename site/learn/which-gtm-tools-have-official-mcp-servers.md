# Which GTM tools have official MCP servers? 200 of 1251, counted

> 200 of 1,251 go to market tools ship an MCP server their own vendor builds and maintains. The full list by category, with server URLs and auth. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Learn](index.md) / What the data says

**What the data says**

# Which GTM tools have official MCP servers?

**The short answer**

200 of the 1,251 go to market tools in this directory ship an official MCP server, meaning the vendor builds and maintains it. A further 540 have a community built server. The heaviest concentrations are in enrichment, RevOps infrastructure and signals.

Official is a strict test here. The vendor has to ship and maintain the server itself. A wrapper built by Zapier, Composio, viaSocket or any other integration platform is recorded as community no matter how well it works, because when the underlying API changes, only one of those two has a team whose job it is to notice.

## Where the 200 sit

| Category | Official | Community | Of total | The list |
|---|---|---|---|---|
| [Data & Enrichment](../categories/data-enrichment.md) | 42 | 121 | 235 | [open](../lists/mcp-data-enrichment.md) |
| [RevOps Infra](../categories/revops-infra.md) | 29 | 24 | 102 | [open](../lists/mcp-revops-infra.md) |
| [Engagement & Outbound](../categories/engagement-outbound.md) | 23 | 58 | 173 | [open](../lists/mcp-engagement-outbound.md) |
| [Signals & Intent](../categories/signals-intent-abm.md) | 20 | 25 | 85 | [open](../lists/mcp-signals-intent-abm.md) |
| [Conversation Intel](../categories/conversation-intel.md) | 19 | 6 | 51 | [open](../lists/mcp-conversation-intel.md) |
| [MCP Layer](../categories/mcp-infrastructure.md) | 14 | 247 | 266 | [open](../lists/mcp-mcp-infrastructure.md) |
| [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | 11 | 8 | 57 | [open](../lists/mcp-inbound-plg-chat.md) |
| [AI SDRs](../categories/ai-sdr-agents.md) | 8 | 12 | 65 | [open](../lists/mcp-ai-sdr-agents.md) |
| [Proposals & Deals](../categories/proposals-deals.md) | 8 | 5 | 30 | [open](../lists/mcp-proposals-deals.md) |
| [Community & Dark Social](../categories/community-dark-social.md) | 8 | 3 | 21 | [open](../lists/mcp-community-dark-social.md) |
| [Scheduling & Routing](../categories/scheduling-routing.md) | 5 | 4 | 19 | [open](../lists/mcp-scheduling-routing.md) |
| [Video Prospecting](../categories/video-prospecting.md) | 4 | 6 | 24 | [open](../lists/mcp-video-prospecting.md) |
| [Email Deliverability](../categories/email-deliverability.md) | 4 | 6 | 28 | [open](../lists/mcp-email-deliverability.md) |
| [Forecasting & Revenue](../categories/forecasting-revenue.md) | 3 | 10 | 33 | [open](../lists/mcp-forecasting-revenue.md) |
| [Enablement & Coaching](../categories/enablement-coaching.md) | 2 | 5 | 62 | [open](../lists/mcp-enablement-coaching.md) |

Counted 2026-09-12 from directory.json, reconciled against tools_recount.py. Entry counts: 16 products appear in two categories and are counted in both here.

## The full list

All 200 are published on one page with the server URL, the auth model and the access gate for each: [the official MCP servers list](../lists/official-mcp-servers.md). 758 entries across the directory carry a parseable server URL; where a vendor claims a server in prose without one, that is recorded as a risk on the methodology page rather than quietly cleaned up.

## The first fifteen, in the published order

- [Airbyte](../tools/airbyte.md) Official MCP · Free to start
Open-source/cloud ELT platform with 600+ connectors moving data from SaaS tools and databases into warehouses; increasingly positions itself as a...
- [Anymail Finder](../tools/anymail-finder.md) Official MCP · Free to start
Takes a name plus a company, domain, or LinkedIn URL, verifies the resulting work email against the mail server in real time, and only charges when...
- [Apideck](../tools/apideck.md) Official MCP · Free to start
A unified API that normalises 200+ SaaS connectors into single data models, exposed as one MCP endpoint covering CRM, accounting, HRIS, ATS, file...
- [Apify](../tools/apify.md) Official MCP · Free to start
A cloud platform for running "Actors" (hosted scrapers and automation programs, thousands of them in a public store) that extract web data such as...
- [Attio](../tools/attio.md) Official MCP · Free to start
A CRM built around a flexible, user-defined data model (not fixed contact/company/deal objects) with real-time sync and an API-first architecture.
- [Autobound](../tools/autobound.md) Official MCP · Free to start
Generates personalised outbound email copy and openers from live buyer signals, and sells the underlying signal data as an API and MCP feed.
- [Browserbase](../tools/browserbase.md) Official MCP · Free to start
A hosted headless-browser service (sessions, proxies, stealth, session recording) with Stagehand, its natural-language browser automation layer, so...
- [Buffer](../tools/buffer.md) Official MCP · Free to start
A social-media scheduling and publishing tool covering channels, a posting queue, drafts, ideas and per-post analytics, with a remote MCP server that...
- [Cal.com](../tools/cal-com.md) Official MCP · Free to start
Open-source scheduling infrastructure - booking pages, event types, and a scheduling API/platform - offered both as a free, self-hostable open-source...
- [Calendly](../tools/calendly.md) Official MCP · Free to start
Prospect-facing scheduling links and booking pages that let invitees book meetings directly onto a rep's calendar based on defined availability rules.
- [Cargo](../tools/cargo.md) Official MCP · Free to start
A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment,...
- [Census (now operates as "Fivetran Activations")](../tools/census.md) Official MCP · Free to start
Was a standalone reverse-ETL tool for syncing warehouse data (Snowflake, BigQuery, etc.) into GTM tools like Salesforce/HubSpot without code; the...
- [Common Paper](../tools/common-paper.md) Official MCP · Free to start
Contract system built for startups - standardized, mutually-agreeable contract templates (MSAs, DPAs, order forms) plus a workflow/e-signature layer,...
- [Composio](../tools/composio.md) Official MCP · Free to start
A hosted integration/auth platform that lets AI agents and MCP clients call actions across 1,000+ SaaS apps (HubSpot, Slack, Gmail, GitHub, Notion,...
- [Crustdata](../tools/crustdata.md) Official MCP · Free to start
A real-time API for company and person firmographic/growth data (headcount trends, funding, tech stack, web traffic, social signals), positioned as...

175 more are on the linked page. The cut is the display limit, not a ranking.

## The caveat that matters

An official server is not the same as a server you can use. 41 of these sit behind an enterprise gate: a contract, a seat count or a procurement cycle before anybody gets a key. Check the gate column, not just the status.

## Sources

- [The GTM MCP Directory, the official servers list](../lists/official-mcp-servers.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site
- [The GTM MCP Directory, the counted data](../data.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-12. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [How many GTM tools have MCP servers?](how-many-gtm-tools-have-mcp-servers.md)
- [What is the difference between an official and a community MCP server?](official-vs-community-mcp-server.md)
- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)
- [Which GTM tools can a solo operator use with an AI agent?](which-gtm-tools-can-a-solo-operator-use.md)

## In the directory

- [The official servers list](../lists/official-mcp-servers.md)
- [By MCP status](../mcp/index.md)
