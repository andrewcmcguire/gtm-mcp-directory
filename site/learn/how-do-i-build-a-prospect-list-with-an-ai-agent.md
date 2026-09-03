# How do I build a prospect list with an AI agent? The chain, and its coverage

> Building a target list with an agent: the five jobs it needs, how many tools carry each one, and which parts of the chain have almost no MCP coverage.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I build a prospect list with an AI agent?

**The short answer**

The chain is: define the account criteria, search a company database, enrich each company, find the right people inside them, then score and prioritise. Each of those is a separate job in this directory with its own coverage, and the account list step is the thinnest link.

## The chain

| Step | The job | Tools tagged | Official MCP | Free tier |
|---|---|---|---|---|
| Build the target account list | [build a target account list](../jobs/build-target-account-list.md) | 7 | 4 | 1 |
| Search companies by firmographics | [search companies by firmographics](../jobs/search-companies-by-firmographics.md) | 15 | 12 | 4 |
| Enrich each company from its domain | [enrich a company from a domain](../jobs/enrich-company-from-domain.md) | 34 | 24 | 14 |
| Search people by criteria | [search people by criteria](../jobs/search-people-by-criteria.md) | 24 | 16 | 6 |
| Score and prioritise | [score and prioritize leads](../jobs/score-and-prioritize-leads.md) | 24 | 13 | 4 |

Counted 2026-09-03. Entry counts rather than product counts.

## Where it is thin

[build a target account list](../jobs/build-target-account-list.md) is tagged on only 7 entries, of which 4 have an official server. In practice this step is usually done by combining a firmographic search with a signal rather than by a tool sold as list building, which is a reasonable thing for an agent to orchestrate itself.

## The tools with the deepest coverage in the chain

- [Crustdata](../tools/crustdata.md) Official MCP · Free to start
A real-time API for company and person firmographic/growth data (headcount trends, funding, tech stack, web traffic, social signals), positioned as...
- [Prospeo](../tools/prospeo.md) Official MCP · Free to start
A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given person or domain and returns basic...
- [ZoomInfo](../tools/zoominfo.md) Official MCP · Free to start
A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human...
- [Apollo.io](../tools/apollo-io.md) Official MCP · Paid, self-serve
A combined B2B contact database (265M+ contacts) and sales engagement platform in one product - prospect search/filtering, email and call sequencing,...
- [Coresignal](../tools/coresignal.md) Official MCP · Paid, self-serve
Sells structured B2B datasets and APIs (company, employee/people, job-posting records) scraped and normalized from public and professional-network...
- [Explorium](../tools/explorium.md) Official MCP · Paid, self-serve
Aggregates roughly 50 third-party data sources into one API/platform for business and prospect lookup (firmographics, contacts, technographics,...
- [Fiber AI](../tools/fiber-ai.md) Official MCP · Paid, self-serve
B2B search and enrichment APIs for finding companies and people by structured filters or natural language, then revealing work emails and phone...
- [Lead411](../tools/lead411.md) Official MCP · Paid, self-serve
A B2B contact and company database with verified emails, direct dials, and growth/intent triggers, queryable by search or by an enrichment API.

5 more are on the linked page. The cut is the display limit, not a ranking.

## Add a signal, or you have built a directory rather than a list

A list of companies matching a size and an industry is not a prospect list, it is a phone book. The difference is a reason to reach out now. 12 entries are tagged [detect a funding or news event](../jobs/detect-funding-or-news-event.md), 5 are tagged [scrape job postings](../jobs/scrape-job-postings.md), 14 are tagged [detect a company's tech stack](../jobs/detect-technographics.md) and 10 are tagged [track job changes](../jobs/track-job-changes.md). Those are the cheapest sources of a real reason.

## Then stop

Building the list and sending to it are different decisions. Keep the send behind a human approval until you have read what the chain produced at least twice, because an agent will build a list of four thousand as easily as forty and will not feel embarrassed about either.

## Sources

- [The GTM MCP Directory, by job](../jobs/index.md) this site
- [The GTM MCP Directory, Data and Enrichment](../categories/data-enrichment.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which tools can enrich a company from its domain?](which-tools-can-enrich-a-company-from-a-domain.md)
- [What is buyer intent data?](what-is-buyer-intent-data.md)
- [How do I write personalised outreach with an AI agent?](how-do-i-write-personalized-outreach-with-an-ai-agent.md)
- [Which tools can identify anonymous website visitors?](which-tools-can-identify-anonymous-website-visitors.md)

## In the directory

- [Find people and companies](../jobs/family-find-people-and-companies.md)
- [Signals and research](../jobs/family-signals-and-research.md)
