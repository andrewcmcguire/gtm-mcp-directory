# Which data enrichment tools can an AI agent use for free? 17 counted

> 17 of the 38 data enrichment tools in this directory are free to start, and 14 of those also have an MCP server. The list, with what each one does. Counted 2026-08-28.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / What the data says

**What the data says**

# Which data enrichment tools can an AI agent use for free?

**The short answer**

17 of the 38 data enrichment tools counted here are free to start, meaning a solo operator can get API access without paying and without talking to anyone. 14 of those also ship an MCP server, so an agent can call them without any glue code.

Free to start is a gate, not a price. It means the door opens without a sales call. Every one of these vendors meters something, and this directory does not track credits, quotas or rate limits, so read the vendor's own pricing page before pointing a loop at one.

## Free to start, with an MCP server

- [Anymail Finder](../tools/anymail-finder.md) Official MCP · Free to start
Takes a name plus a company, domain, or LinkedIn URL, verifies the resulting work email against the mail server in real time, and only charges when...
- [Crustdata](../tools/crustdata.md) Official MCP · Free to start
A real-time API for company and person firmographic/growth data (headcount trends, funding, tech stack, web traffic, social signals), positioned as...
- [Diffbot](../tools/diffbot.md) Official MCP · Free to start
A web-extraction and "Knowledge Graph" company that crawls the public web and structures it into an entity graph (organizations, people, articles)...
- [Enrow](../tools/enrow.md) Official MCP · Free to start
Finds and verifies work email addresses and direct phone numbers from a name plus company domain or a LinkedIn URL, charging only when it returns a...
- [Exa](../tools/exa.md) Official MCP · Free to start
A search API that returns web pages and structured results ranked by semantic/meaning similarity to a query (embeddings-based) rather than keyword...
- [FullEnrich](../tools/fullenrich.md) Official MCP · Free to start
A B2B contact-enrichment aggregator that runs a single lookup or bulk list through 15+ third-party data vendors in a "waterfall" and returns the...
- [Hunter.io](../tools/hunter-io.md) Official MCP · Free to start
An email-finding and verification tool - given a name, domain, or company, it locates likely professional email addresses (via domain...
- [LeadMagic](../tools/leadmagic.md) Official MCP · Free to start
A B2B contact/company data API and CLI that finds and validates work emails, mobile numbers, and social-to-email matches, plus...
- [Lusha](../tools/lusha.md) Official MCP · Free to start
A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting platform, and bulk CSV/API enrichment for...
- [Prospeo](../tools/prospeo.md) Official MCP · Free to start
A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given person or domain and returns basic...
- [TheirStack](../tools/theirstack.md) Official MCP · Free to start
Tracks 233M+ job postings across 195+ countries and 33,000+ technologies to detect hiring signals, technographic footprint, and buying-intent signals...
- [Warmly (Warmly.ai)](../tools/warmly.md) Official MCP · Free to start
De-anonymizes website visitors at the person and company level from site traffic, and aggregates first-party (web/product/CRM), second-party...
- [ZoomInfo](../tools/zoominfo.md) Official MCP · Free to start
A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human...
- [People Data Labs](../tools/people-data-labs.md) Community MCP · Free to start
A raw person/company data API that returns profile records (name, job history, education, skills, social handles, contact fields) matched by...

## Free to start, no server found

- [BetterContact](../tools/bettercontact.md) No MCP found · Free to start
A waterfall enrichment orchestrator that queries 20+ third-party email/phone data providers in sequence for a given contact, stopping once a verified...
- [Datagma](../tools/datagma.md) No MCP found · Free to start
An all-in-one B2B enrichment platform that finds work emails and verified mobile phone numbers, appends firmographic company data, and offers a Sales...
- [Findymail](../tools/findymail.md) No MCP found · Free to start
An email finder and verifier that locates a person's work email from a name+domain, domain-only search, or LinkedIn profile URL, verifies...

## Why enrichment is the exception

Data & Enrichment is the most agent reachable category in the whole directory: 31 official servers and 2 community across 38 entries, with only 5 where none was found. These vendors were selling an API before MCP existed, so exposing it through one more protocol was a small step.

## What to check before you wire one in

- **What it takes as input.** A domain, an email or a LinkedIn URL are different jobs. 34 entries are tagged [enrich a company from a domain](../jobs/enrich-company-from-domain.md), 12 are tagged [enrich a person from a linkedin url](../jobs/enrich-person-from-linkedin-url.md) and 29 are tagged [find a work email address](../jobs/find-work-email.md).

- **What a failed lookup costs.** Some vendors charge for a miss, some do not. Not tracked here.

- **What the free tier is for.** Free tiers are usually sized for evaluation, and an agent is much better at consuming them than a human clicking is.

Nobody here has run any of these. 0 tools in this directory are bench tested, so treat the list as a starting point for your own test rather than as a result.

## Sources

- [The GTM MCP Directory, Data and Enrichment](../categories/data-enrichment.md) this site
- [The GTM MCP Directory, free API tiers](../lists/free-api-tiers.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-28. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is data enrichment in sales?](what-is-data-enrichment.md)
- [How do I enrich a LinkedIn profile with an AI agent?](how-do-i-enrich-a-linkedin-profile-with-an-ai-agent.md)
- [Which tools can enrich a company from its domain?](which-tools-can-enrich-a-company-from-a-domain.md)
- [Which GTM tools can a solo operator use with an AI agent?](which-gtm-tools-can-a-solo-operator-use.md)

## In the directory

- [Data and Enrichment](../categories/data-enrichment.md)
- [Free tiers](../lists/free-api-tiers.md)
