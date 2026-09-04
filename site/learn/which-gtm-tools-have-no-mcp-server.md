# Which GTM tools have no MCP server? 87 of 293, and what that means

> 87 of 293 GTM tools had no MCP server found on the date they were checked. The list, the categories it clusters in, and why none found is not the same as none exists.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Learn](index.md) / What the data says

**What the data says**

# Which GTM tools have no MCP server?

**The short answer**

87 of the 293 entries in this directory had no MCP server found at the time of the check. That is a statement about a search on a stated date, not a claim that no server exists, and every entry carries the date its facts were pulled.

The list matters more than it looks. If a tool your team depends on is on it, that is the work item: either an API and some glue, or a case to the vendor, or a decision to route around it.

## Where none found clusters

| Category | No server | Of total | Share |
|---|---|---|---|
| [Forecasting & Revenue](../categories/forecasting-revenue.md) | 13 | 17 | 76% |
| [Email Deliverability](../categories/email-deliverability.md) | 8 | 13 | 62% |
| [Enablement & Coaching](../categories/enablement-coaching.md) | 8 | 14 | 57% |
| [AI SDRs](../categories/ai-sdr-agents.md) | 13 | 23 | 57% |
| [Community & Dark Social](../categories/community-dark-social.md) | 6 | 16 | 38% |
| [Proposals & Deals](../categories/proposals-deals.md) | 5 | 14 | 36% |
| [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | 5 | 15 | 33% |
| [Video Prospecting](../categories/video-prospecting.md) | 4 | 14 | 29% |
| [Scheduling & Routing](../categories/scheduling-routing.md) | 4 | 14 | 29% |
| [Engagement & Outbound](../categories/engagement-outbound.md) | 6 | 27 | 22% |
| [Signals & Intent](../categories/signals-intent-abm.md) | 6 | 28 | 21% |
| [Data & Enrichment](../categories/data-enrichment.md) | 5 | 38 | 13% |
| [Conversation Intel](../categories/conversation-intel.md) | 3 | 24 | 12% |
| [RevOps Infra](../categories/revops-infra.md) | 1 | 23 | 4% |

## What none found does not mean

- **It does not mean no API.** Plenty of these have excellent REST APIs. An agent can still use them; somebody just has to write the wrapper.

- **It does not mean the vendor is behind.** It means a search on a date came back empty, and the date is on the entry.

- **It does not mean it will stay true.** This is the single fastest moving column in the whole dataset, which is why the check date ships with every row.

## The first fifteen

- [BetterContact](../tools/bettercontact.md) No MCP found · Free to start
A waterfall enrichment orchestrator that queries 20+ third-party email/phone data providers in sequence for a given contact, stopping once a verified...
- [Datagma](../tools/datagma.md) No MCP found · Free to start
An all-in-one B2B enrichment platform that finds work emails and verified mobile phone numbers, appends firmographic company data, and offers a Sales...
- [F5Bot](../tools/f5bot.md) No MCP found · Free to start
Monitors Reddit, Hacker News, and Lobsters for keyword mentions and sends email alerts within minutes of a match.
- [Findymail](../tools/findymail.md) No MCP found · Free to start
An email finder and verifier that locates a person's work email from a name+domain, domain-only search, or LinkedIn profile URL, verifies...
- [Landbase](../tools/landbase.md) No MCP found · Free to start
A GTM data platform that targets, qualifies, prioritizes, and enriches B2B accounts via AI agents using natural-language criteria, with continuous...
- [Pipedrive](../tools/pipedrive.md) Official MCP · Free to start
A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams.
- [Recapped.io](../tools/recapped-io.md) No MCP found · Free to start
Digital sales room and customer-onboarding collaboration platform for tracking mutual action plans, content sharing, and buyer engagement through the...
- [Scaledmail](../tools/scaledmail.md) No MCP found · Free to start
Cold-email infrastructure provider - sets up sending domains, configures DNS authentication (SPF/DKIM/DMARC) from day one, and rotates inboxes so...
- [Warmup Inbox](../tools/warmup-inbox.md) No MCP found · Free to start
Email warmup and deliverability platform running a network of 30,000+ real inboxes that exchange natural-looking email (opens, replies, stars) with a...
- [AiSDR](../tools/aisdr.md) No MCP found · Paid, self-serve
An AI sales agent that researches prospects via "Live AI search," writes and sends personalized email/LinkedIn outreach, qualifies replies, and books...
- [Albacross](../tools/albacross.md) No MCP found · Paid, self-serve
Identifies which companies visit a website via IP-to-company matching, tracks on-site and off-site behavioral/intent signals, and enriches identified...
- [BuzzSumo](../tools/buzzsumo.md) No MCP found · Paid, self-serve
Researches top-performing content and social engagement by topic, tracks brand/competitor mentions, and surfaces influencers, built on a large...
- [Clara (Clara Labs)](../tools/clara.md) No MCP found · Paid, self-serve
AI scheduling assistant reached by CC'ing "Clara" on an email thread - it reads the thread, proposes times, handles replies, and confirms meetings...
- [Clearbit Reveal (rebranded: HubSpot Breeze Intelligence)](../tools/clearbit-reveal.md) No MCP found · Paid, self-serve
Identifies companies visiting a website via IP-to-company matching, then enriches contact/company CRM records with firmographic data (employee count,...
- [Dubb](../tools/dubb.md) No MCP found · Paid, self-serve
Video sales-messaging platform with a built-in lightweight CRM - record/send personalized prospecting and follow-up videos via email, SMS, LinkedIn,...

71 more are on the linked page. The cut is the display limit, not a ranking.

[The full list of 87 is here](../lists/no-mcp-server.md), each row carrying the date its entry was last checked. If you know one of them shipped a server, that correction is the most valuable thing anyone can send this directory.

## Sources

- [The GTM MCP Directory, no MCP server found](../lists/no-mcp-server.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site
- [The GTM MCP Directory, submit a correction](../submit.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-04. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [How many GTM tools have MCP servers?](how-many-gtm-tools-have-mcp-servers.md)
- [How do I build an MCP server for a tool that does not have one?](how-do-i-build-an-mcp-server-for-a-tool-that-has-none.md)
- [Should I use a tool's MCP server or its REST API?](how-do-i-choose-between-an-mcp-server-and-a-rest-api.md)
- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)

## In the directory

- [No MCP server found](../lists/no-mcp-server.md)
- [Submit a correction](../submit.md)
