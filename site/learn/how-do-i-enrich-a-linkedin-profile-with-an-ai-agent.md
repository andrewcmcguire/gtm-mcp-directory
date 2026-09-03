# How do I enrich a LinkedIn profile with an AI agent? The callable tools

> 12 tools in this directory are tagged with enriching a person from a LinkedIn URL, and 8 have an official MCP server. How to wire it, and what to be careful about.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I enrich a LinkedIn profile with an AI agent?

**The short answer**

You give a tool the profile URL and it returns a structured record: name, title, employer, and often a work email. 12 entries here are tagged with that job and 8 ship an official MCP server, so an agent can make the call with no glue code.

## The tools an agent can call directly

- [Lusha](../tools/lusha.md) Official MCP · Free to start
A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting platform, and bulk CSV/API enrichment for...
- [CUFinder](../tools/cufinder.md) Official MCP · Paid, self-serve
A credit-based B2B data lookup service where you feed in a company name, domain, LinkedIn URL, or person and get back an enriched company or contact...
- [Dropcontact](../tools/dropcontact.md) Official MCP · Paid, self-serve
A France-based, GDPR-oriented contact enrichment and email-finding/verification service that takes a name plus company (name, domain, or LinkedIn...
- [Fiber AI](../tools/fiber-ai.md) Official MCP · Paid, self-serve
B2B search and enrichment APIs for finding companies and people by structured filters or natural language, then revealing work emails and phone...
- [PhantomBuster](../tools/phantombuster.md) Official MCP · Paid, self-serve
General browser-automation/data-extraction platform ("Phantoms") that runs cloud scripts to scrape and act on LinkedIn and other web platforms -...
- [RocketReach](../tools/rocketreach.md) Official MCP · Paid, self-serve
A large contact/company lookup database queried by name, company domain, or LinkedIn profile to find work emails, direct dials, and mobile numbers,...
- [Wiza](../tools/wiza.md) Official MCP · Paid, self-serve
Pulls verified work emails and mobile numbers for people found on LinkedIn or Sales Navigator and exports them to CSV or a CRM.
- [Surfe](../tools/surfe.md) Official MCP · Enterprise only
A Chrome extension plus API that pulls contacts and companies off LinkedIn, runs them through a multi-vendor waterfall to find verified emails and...
- [People Data Labs](../tools/people-data-labs.md) Community MCP · Free to start
A raw person/company data API that returns profile records (name, job history, education, skills, social handles, contact fields) matched by...

## The free to start ones

- [Lusha](../tools/lusha.md) Official MCP · Free to start
A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting platform, and bulk CSV/API enrichment for...
- [People Data Labs](../tools/people-data-labs.md) Community MCP · Free to start
A raw person/company data API that returns profile records (name, job history, education, skills, social handles, contact fields) matched by...
- [Datagma](../tools/datagma.md) No MCP found · Free to start
An all-in-one B2B enrichment platform that finds work emails and verified mobile phone numbers, appends firmographic company data, and offers a Sales...

## The chain most people actually want

A profile URL is rarely the end state. The usual sequence is profile to person record to work email to verified email, and each step is a different job with different coverage.

| Step | The job | Tools tagged | Official MCP | Free tier |
|---|---|---|---|---|
| Enrich the person from the URL | [enrich a person from a linkedin url](../jobs/enrich-person-from-linkedin-url.md) | 12 | 8 | 3 |
| Find the work email | [find a work email address](../jobs/find-work-email.md) | 29 | 22 | 12 |
| Verify it is deliverable | [verify an email is deliverable](../jobs/verify-email-deliverable.md) | 15 | 12 | 6 |
| Enrich their company | [enrich a company from a domain](../jobs/enrich-company-from-domain.md) | 34 | 24 | 14 |
| Write it to the CRM | [write crm records](../jobs/write-crm-records.md) | 28 | 18 | 7 |

## Three things to be careful about

- **Scraping is not the same as enrichment.** Some vendors return data from a licensed or contributed dataset keyed on the profile URL. Others fetch the page. Those are different products with different terms, and this directory records what the vendor says rather than adjudicating which is which.

- **Personal data has rules.** Enriching a person is processing personal data, and your obligations do not change because an agent did it. Nothing here is legal advice.

- **Credits disappear fast.** An agent looping over a list will spend an evaluation tier before you have finished reading the docs. Set a hard cap on the tool call, not just in the prompt.

## The honest limit of this page

Nobody here has run any of these tools. 0 of 293 entries are bench tested, so treat this as a shortlist to test rather than a result.

## Sources

- [The GTM MCP Directory, enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md) this site
- [The GTM MCP Directory, Data and Enrichment](../categories/data-enrichment.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is data enrichment in sales?](what-is-data-enrichment.md)
- [How do I find someone's work email with an AI agent?](how-do-i-find-a-work-email-with-an-ai-agent.md)
- [Which data enrichment tools can an AI agent use for free?](which-data-enrichment-tools-can-an-agent-use-for-free.md)
- [Which tools can enrich a company from its domain?](which-tools-can-enrich-a-company-from-a-domain.md)

## In the directory

- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Data and Enrichment](../categories/data-enrichment.md)
