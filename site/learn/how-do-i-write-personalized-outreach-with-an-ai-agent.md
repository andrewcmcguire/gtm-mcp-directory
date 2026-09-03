# How do I write personalised outreach with an AI agent? Research first, then draft

> 51 tools here are tagged with drafting personalised outreach. Why the research step decides the quality, and which parts an agent can call directly.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I write personalised outreach with an AI agent?

**The short answer**

The drafting is the easy half and it is not where quality comes from. What decides whether a message is worth sending is what the agent knew before it started writing, which means the research calls matter more than the model or the prompt.

## The order that works

| Step | The job | Tools tagged | Official MCP | Free tier |
|---|---|---|---|---|
| Research the account | [research an account before a call](../jobs/research-account-for-call-prep.md) | 17 | 10 | 3 |
| Find a real trigger | [detect a funding or news event](../jobs/detect-funding-or-news-event.md) | 12 | 10 | 4 |
| Scrape the specific page | [scrape a web page for facts](../jobs/scrape-web-page-for-facts.md) | 6 | 5 | 2 |
| Draft the message | [draft personalized outreach](../jobs/draft-personalized-outreach.md) | 51 | 25 | 6 |
| Send it | [run an email sequence](../jobs/run-email-sequence.md) | 45 | 24 | 3 |
| Read what happened | [read outreach performance](../jobs/read-outreach-performance.md) | 14 | 7 | 2 |

## Why the research step is the whole game

51 entries here are tagged [draft personalized outreach](../jobs/draft-personalized-outreach.md), the most tagged job in the entire vocabulary. Drafting is commoditised: every tool in the category will write you a competent paragraph. None of them can invent the fact that makes the paragraph worth reading. That fact comes from a research call, and research is where coverage is thinner: 10 official servers across 17 tagged entries.

## The tools an agent can call for the drafting step

- [Autobound](../tools/autobound.md) Official MCP · Free to start
Generates personalised outbound email copy and openers from live buyer signals, and sells the underlying signal data as an API and MCP feed.
- [Hightouch](../tools/hightouch.md) Official MCP · Free to start
A CDP/reverse-ETL platform that syncs warehouse data (Snowflake, BigQuery, Databricks, Redshift) to 300+ downstream tools (ad platforms, CRMs,...
- [HubSpot](../tools/hubspot.md) Official MCP · Free to start
An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform.
- [Lusha](../tools/lusha.md) Official MCP · Free to start
A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting platform, and bulk CSV/API enrichment for...
- [ZoomInfo](../tools/zoominfo.md) Official MCP · Free to start
A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human...
- [Amplemarket](../tools/amplemarket.md) Official MCP · Enterprise leaning
An all-in-one sales engagement platform that finds leads, runs multichannel outbound sequences (email/social/phone/voice), and optimizes email...
- [Apollo.io](../tools/apollo-io.md) Official MCP · Paid, self-serve
A combined B2B contact database (265M+ contacts) and sales engagement platform in one product - prospect search/filtering, email and call sequencing,...
- [HeyReach](../tools/heyreach.md) Official MCP · Paid, self-serve
Cloud-based LinkedIn outreach automation platform for agencies/sales teams running multi-account connection, messaging, and inbox campaigns from...
- [Instantly](../tools/instantly.md) Official MCP · Paid, self-serve
Cold email sending platform providing mailbox infrastructure, warmup, deliverability management, sequencing, and lead sourcing.
- [La Growth Machine](../tools/la-growth-machine.md) Official MCP · Paid, self-serve
Multi-channel prospecting platform that sequences outreach across LinkedIn, email, Twitter/X, and voice notes/calls from one campaign builder, with...

13 more are on the linked page. The cut is the display limit, not a ranking.

## The failure mode to design against

Personalisation at scale fails in a specific way: the agent finds a fact, the fact is wrong or stale, and the message is now confidently wrong in a way a generic message never would have been. A generic email is ignored. A wrongly personalised one is remembered.

Two guardrails. Make the agent cite the source of every claimed fact in its draft, in a field you can read. And require a human approval on the first send to any account, which costs you almost nothing when the list is good and saves you when it is not.

## What this directory will not tell you

Which tool writes better copy. There is no tool versus tool verdict anywhere on this site, and 0 of 293 entries have been run by anybody here.

## Sources

- [The GTM MCP Directory, draft personalized outreach](../jobs/draft-personalized-outreach.md) this site
- [The GTM MCP Directory, Engagement and Outbound](../categories/engagement-outbound.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-02. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Can an AI agent send email on my behalf?](can-an-ai-agent-send-email-on-my-behalf.md)
- [How do I build a prospect list with an AI agent?](how-do-i-build-a-prospect-list-with-an-ai-agent.md)
- [Which sales engagement tools have MCP servers?](which-sales-engagement-tools-have-mcp-servers.md)
- [What is an AI SDR?](what-is-an-ai-sdr.md)

## In the directory

- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Outreach and engagement](../jobs/family-outreach-and-engagement.md)
