# What is buyer intent data? Definition, sources, and what an agent can fetch

> Buyer intent data is evidence that an account is researching a problem you solve. Where it comes from, what it is worth, and which of the 30 tools tagged with it an agent can call.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is buyer intent data?

**The short answer**

Buyer intent data is evidence that an account is actively researching something you sell: content consumption on third party networks, review site activity, job postings, technology changes, or visits to your own site. It is a prioritisation input, not a prediction, and its quality depends entirely on where the signal came from.

Intent is sold as one thing and is at least four. Knowing which one you are buying is the whole skill.

- **First party.** Behaviour on your own properties. Highest quality, smallest volume, and it is yours.

- **De-anonymised traffic.** Turning an anonymous visit into a company, sometimes a person. 11 entries here are tagged [identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md).

- **Third party topic intent.** Aggregated content consumption across publisher networks. Broad, and the further from your product the topic is, the noisier it gets.

- **Observable events.** A funding round, a hiring pattern, a technology added or dropped. Not intent in the strict sense, but checkable and often more actionable. 12 entries are tagged [detect a funding or news event](../jobs/detect-funding-or-news-event.md), 5 are tagged [scrape job postings](../jobs/scrape-job-postings.md) and 14 are tagged [detect a company's tech stack](../jobs/detect-technographics.md).

## What an agent can actually fetch

30 entries are tagged [fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md). Of those, 18 have an official MCP server, 10 have none found, and 13 are reachable by a solo operator without a contract. The category they mostly live in, Signals & Intent, carries 10 enterprise only entries out of 28, the second highest enterprise gate share in this directory.

That combination is the honest summary of intent data as a category: technically callable, often commercially closed.

## The tools tagged with it that a solo operator can reach

- [Autobound](../tools/autobound.md) Official MCP · Free to start
Generates personalised outbound email copy and openers from live buyer signals, and sells the underlying signal data as an API and MCP feed.
- [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md) Official MCP · Free to start
Identifies companies visiting a website via IP-to-company matching, tracks page-level visit behavior, and surfaces intent signals plus verified...
- [TheirStack](../tools/theirstack.md) Official MCP · Free to start
Tracks 233M+ job postings across 195+ countries and 33,000+ technologies to detect hiring signals, technographic footprint, and buying-intent signals...
- [Warmly (Warmly.ai)](../tools/warmly.md) Official MCP · Free to start
De-anonymizes website visitors at the person and company level from site traffic, and aggregates first-party (web/product/CRM), second-party...
- [Amplemarket](../tools/amplemarket.md) No MCP found · Enterprise leaning
An all-in-one sales engagement platform that finds leads, runs multichannel outbound sequences (email/social/phone/voice), and optimizes email...
- [Factors.ai](../tools/factors-ai.md) Official MCP · Paid, self-serve
De-anonymizes website visitors and tracks named-account behavior (page visits, LinkedIn/Google ad engagement, email/content engagement, third-party...
- [Lead411](../tools/lead411.md) Official MCP · Paid, self-serve
A B2B contact and company database with verified emails, direct dials, and growth/intent triggers, queryable by search or by an enrichment API.
- [lemlist](../tools/lemlist.md) Official MCP · Paid, self-serve
Multichannel sales engagement platform combining lead database/enrichment, email/LinkedIn/call/SMS sequencing, and a unified inbox.
- [Snitcher](../tools/snitcher.md) Official MCP · Paid, self-serve
Identifies anonymous website visitor companies via IP-to-company database matching, tracks on-site behavior (pages viewed, session length, return...
- [Trigify (Trigify.io)](../tools/trigify.md) Community MCP · Paid, self-serve
Monitors LinkedIn, X/Twitter, Reddit, YouTube, and podcasts for keyword mentions and engagement (likes, comments, shares, job changes), mapping who...

7 more are on the linked page. The cut is the display limit, not a ranking.

## Sources

- [The GTM MCP Directory, Signals and Intent](../categories/signals-intent-abm.md) this site
- [The GTM MCP Directory, fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-28. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which tools can identify anonymous website visitors?](which-tools-can-identify-anonymous-website-visitors.md)
- [What is an API access gate and why does it matter for AI agents?](what-is-an-api-access-gate.md)
- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)
- [How do I build a prospect list with an AI agent?](how-do-i-build-a-prospect-list-with-an-ai-agent.md)

## In the directory

- [Signals and Intent](../categories/signals-intent-abm.md)
- [Signals tools with MCP servers](../lists/mcp-signals-intent-abm.md)
