# Which GTM tools have no MCP server? 117 of 293, and what that means

> 117 of 293 GTM tools had no MCP server found on the date they were checked. The list, the categories it clusters in, and why none found is not the same as none exists.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / What the data says

**What the data says**

# Which GTM tools have no MCP server?

**The short answer**

117 of the 293 entries in this directory had no MCP server found at the time of the check. That is a statement about a search on a stated date, not a claim that no server exists, and every entry carries the date its facts were pulled.

The list matters more than it looks. If a tool your team depends on is on it, that is the work item: either an API and some glue, or a case to the vendor, or a decision to route around it.

## Where none found clusters

| Category | No server | Of total | Share |
|---|---|---|---|
| [Enablement & Coaching](../categories/enablement-coaching.md) | 12 | 14 | 86% |
| [Forecasting & Revenue](../categories/forecasting-revenue.md) | 14 | 17 | 82% |
| [Community & Dark Social](../categories/community-dark-social.md) | 12 | 16 | 75% |
| [AI SDRs](../categories/ai-sdr-agents.md) | 17 | 23 | 74% |
| [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | 10 | 15 | 67% |
| [Email Deliverability](../categories/email-deliverability.md) | 8 | 13 | 62% |
| [Proposals & Deals](../categories/proposals-deals.md) | 6 | 14 | 43% |
| [Scheduling & Routing](../categories/scheduling-routing.md) | 5 | 14 | 36% |
| [Engagement & Outbound](../categories/engagement-outbound.md) | 9 | 27 | 33% |
| [Signals & Intent](../categories/signals-intent-abm.md) | 9 | 28 | 32% |
| [Video Prospecting](../categories/video-prospecting.md) | 4 | 14 | 29% |
| [Conversation Intel](../categories/conversation-intel.md) | 4 | 24 | 17% |
| [Data & Enrichment](../categories/data-enrichment.md) | 5 | 38 | 13% |
| [MCP Layer](../categories/mcp-infrastructure.md) | 1 | 13 | 8% |
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
- [Landbot](../tools/landbot.md) No MCP found · Free to start
No-code visual builder for chatbots deployed on websites, WhatsApp, and Messenger, blending rule-based flows with LLM-powered conversation.
- [Pipedrive](../tools/pipedrive.md) Official MCP · Free to start
A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams.
- [Recapped.io](../tools/recapped-io.md) No MCP found · Free to start
Digital sales room and customer-onboarding collaboration platform for tracking mutual action plans, content sharing, and buyer engagement through the...
- [Tidio](../tools/tidio.md) No MCP found · Free to start
Customer-service platform combining live chat, a help desk, and an AI agent ("Lyro") that resolves routine support/sales questions automatically.
- [AiSDR](../tools/aisdr.md) No MCP found · Paid, self-serve
An AI sales agent that researches prospects via "Live AI search," writes and sends personalized email/LinkedIn outreach, qualifies replies, and books...
- [Albacross](../tools/albacross.md) No MCP found · Paid, self-serve
Identifies which companies visit a website via IP-to-company matching, tracks on-site and off-site behavioral/intent signals, and enriches identified...
- [Brand24](../tools/brand24.md) No MCP found · Paid, self-serve
Tracks brand/keyword mentions across social media, news, blogs, forums, podcasts, and review sites, then scores sentiment and surfaces coverage...
- [BuzzSumo](../tools/buzzsumo.md) No MCP found · Paid, self-serve
Researches top-performing content and social engagement by topic, tracks brand/competitor mentions, and surfaces influencers, built on a large...
- [Chatbase](../tools/chatbase.md) No MCP found · Paid, self-serve
No-code AI agent builder for deploying chat/voice/email support-and-sales bots across a website widget and channels like WhatsApp and Slack.
- [Clara (Clara Labs)](../tools/clara.md) No MCP found · Paid, self-serve
AI scheduling assistant reached by CC'ing "Clara" on an email thread - it reads the thread, proposes times, handles replies, and confirms meetings...
- [Clearbit Reveal (rebranded: HubSpot Breeze Intelligence)](../tools/clearbit-reveal.md) No MCP found · Paid, self-serve
Identifies companies visiting a website via IP-to-company matching, then enriches contact/company CRM records with firmographic data (employee count,...

100 more are on the linked page. The cut is the display limit, not a ranking.

[The full list of 117 is here](../lists/no-mcp-server.md), each row carrying the date its entry was last checked. If you know one of them shipped a server, that correction is the most valuable thing anyone can send this directory.

## Sources

- [The GTM MCP Directory, no MCP server found](../lists/no-mcp-server.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site
- [The GTM MCP Directory, submit a correction](../submit.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-25. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [How many GTM tools have MCP servers?](how-many-gtm-tools-have-mcp-servers.md)
- [How do I build an MCP server for a tool that does not have one?](how-do-i-build-an-mcp-server-for-a-tool-that-has-none.md)
- [Should I use a tool's MCP server or its REST API?](how-do-i-choose-between-an-mcp-server-and-a-rest-api.md)
- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)

## In the directory

- [No MCP server found](../lists/no-mcp-server.md)
- [Submit a correction](../submit.md)
