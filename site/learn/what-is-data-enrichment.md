# What is data enrichment? The definition, and which vendors an agent can call

> Data enrichment turns a thin identifier into a full record. 38 enrichment tools are counted here and 31 ship an official MCP server.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is data enrichment in sales?

**The short answer**

Data enrichment is taking a thin identifier you already have, such as a domain, an email or a LinkedIn URL, and returning a fuller record: the person's title and employer, or the company's size, industry, location and technology stack. It is the step that turns a name into something you can act on.

Enrichment vendors differ mostly in where the data comes from and how fresh it is: contributed data from users, licensed data, public web crawling, or a blend. This directory does not measure accuracy or coverage. Nobody has run these tools for it, and a coverage claim without a test is a vendor's number repeated back.

## The four shapes of the job

| What you have | The job | Tools tagged | Official MCP | Free tier |
|---|---|---|---|---|
| A company domain | [enrich a company from a domain](../jobs/enrich-company-from-domain.md) | 34 | 24 | 15 |
| A LinkedIn profile URL | [enrich a person from a linkedin url](../jobs/enrich-person-from-linkedin-url.md) | 12 | 8 | 3 |
| A name and a company | [find a work email address](../jobs/find-work-email.md) | 29 | 22 | 12 |
| An email address | [reverse-look-up a person from an email](../jobs/reverse-lookup-person-from-email.md) | 1 | 0 | 1 |

Counted 2026-09-03. Entry counts, not product counts: a tool listed in two categories is counted in both.

## Why this category is the exception

Data & Enrichment is the most agent reachable category in this directory: 31 official servers and 2 community across 38 entries, with 17 free to start. That is not an accident. These vendors already sold an API as the product, so exposing it through a second protocol was a small step rather than a strategy change.

Compare that with categories whose product is a user interface. When the interface is the product, the API is a cost, and the MCP server is a cost on top of a cost.

## The one thing to check first

Credits. Enrichment is metered, and an agent in a loop is very good at spending a month of quota in an afternoon. This directory records the access gate, not pricing or quota sizes, so read the vendor's own page before you point an autonomous loop at one.

## Sources

- [The GTM MCP Directory, Data and Enrichment](../categories/data-enrichment.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which data enrichment tools can an AI agent use for free?](which-data-enrichment-tools-can-an-agent-use-for-free.md)
- [How do I enrich a LinkedIn profile with an AI agent?](how-do-i-enrich-a-linkedin-profile-with-an-ai-agent.md)
- [Which tools can enrich a company from its domain?](which-tools-can-enrich-a-company-from-a-domain.md)
- [How do I find someone's work email with an AI agent?](how-do-i-find-a-work-email-with-an-ai-agent.md)

## In the directory

- [Data and Enrichment](../categories/data-enrichment.md)
- [Enrichment tools with MCP servers](../lists/mcp-data-enrichment.md)
