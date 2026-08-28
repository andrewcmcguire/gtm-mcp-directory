# How do I find a work email with an AI agent? The wiring, and the guardrails

> 29 tools here are tagged with finding a work email and 22 have an official MCP server. How to chain finding with verification, and where it goes wrong.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I find someone's work email with an AI agent?

**The short answer**

Give a tool a name and a company domain, or a LinkedIn URL, and it returns a best guess address with a confidence signal. 29 entries here are tagged with that job, 22 have an official MCP server, and 12 are free to start. Always chain a verification step after it.

## The two step chain, and why it is two steps

Finding and verifying are different jobs done by different systems. A finder infers or looks up an address. A verifier tests whether a mailbox will accept mail for it. Sending to unverified addresses is the fastest way to damage a sending domain, and the damage lands on every campaign after it rather than on the one that caused it.

| Step | The job | Tools tagged | Official MCP | Free tier |
|---|---|---|---|---|
| Find the address | [find a work email address](../jobs/find-work-email.md) | 29 | 22 | 12 |
| Verify it is deliverable | [verify an email is deliverable](../jobs/verify-email-deliverable.md) | 15 | 11 | 6 |
| Warm the inbox first | [warm up an inbox](../jobs/warm-up-inbox.md) | 13 | 7 | 1 |
| Then send | [run an email sequence](../jobs/run-email-sequence.md) | 45 | 22 | 3 |

## The finders an agent can call

- [Anymail Finder](../tools/anymail-finder.md) Official MCP · Free to start
Takes a name plus a company, domain, or LinkedIn URL, verifies the resulting work email against the mail server in real time, and only charges when...
- [Enrow](../tools/enrow.md) Official MCP · Free to start
Finds and verifies work email addresses and direct phone numbers from a name plus company domain or a LinkedIn URL, charging only when it returns a...
- [FullEnrich](../tools/fullenrich.md) Official MCP · Free to start
A B2B contact-enrichment aggregator that runs a single lookup or bulk list through 15+ third-party data vendors in a "waterfall" and returns the...
- [Hunter.io](../tools/hunter-io.md) Official MCP · Free to start
An email-finding and verification tool - given a name, domain, or company, it locates likely professional email addresses (via domain...
- [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md) Official MCP · Free to start
Identifies companies visiting a website via IP-to-company matching, tracks page-level visit behavior, and surfaces intent signals plus verified...
- [LeadMagic](../tools/leadmagic.md) Official MCP · Free to start
A B2B contact/company data API and CLI that finds and validates work emails, mobile numbers, and social-to-email matches, plus...
- [Lusha](../tools/lusha.md) Official MCP · Free to start
A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting platform, and bulk CSV/API enrichment for...
- [Prospeo](../tools/prospeo.md) Official MCP · Free to start
A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given person or domain and returns basic...
- [ZoomInfo](../tools/zoominfo.md) Official MCP · Free to start
A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human...
- [Apollo.io](../tools/apollo-io.md) Official MCP · Paid, self-serve
A combined B2B contact database (265M+ contacts) and sales engagement platform in one product - prospect search/filtering, email and call sequencing,...
- [Clay](../tools/clay.md) Official MCP · Paid, self-serve
A spreadsheet-style workflow/orchestration tool that runs lead and company records through "waterfall" lookups across 100-200+ third-party data...
- [CUFinder](../tools/cufinder.md) Official MCP · Paid, self-serve
A credit-based B2B data lookup service where you feed in a company name, domain, LinkedIn URL, or person and get back an enriched company or contact...

12 more are on the linked page. The cut is the display limit, not a ranking.

## The free ones

- [Anymail Finder](../tools/anymail-finder.md) Official MCP · Free to start
Takes a name plus a company, domain, or LinkedIn URL, verifies the resulting work email against the mail server in real time, and only charges when...
- [Enrow](../tools/enrow.md) Official MCP · Free to start
Finds and verifies work email addresses and direct phone numbers from a name plus company domain or a LinkedIn URL, charging only when it returns a...
- [FullEnrich](../tools/fullenrich.md) Official MCP · Free to start
A B2B contact-enrichment aggregator that runs a single lookup or bulk list through 15+ third-party data vendors in a "waterfall" and returns the...
- [Hunter.io](../tools/hunter-io.md) Official MCP · Free to start
An email-finding and verification tool - given a name, domain, or company, it locates likely professional email addresses (via domain...
- [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md) Official MCP · Free to start
Identifies companies visiting a website via IP-to-company matching, tracks page-level visit behavior, and surfaces intent signals plus verified...
- [LeadMagic](../tools/leadmagic.md) Official MCP · Free to start
A B2B contact/company data API and CLI that finds and validates work emails, mobile numbers, and social-to-email matches, plus...
- [Lusha](../tools/lusha.md) Official MCP · Free to start
A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting platform, and bulk CSV/API enrichment for...
- [Prospeo](../tools/prospeo.md) Official MCP · Free to start
A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given person or domain and returns basic...
- [ZoomInfo](../tools/zoominfo.md) Official MCP · Free to start
A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human...
- [BetterContact](../tools/bettercontact.md) No MCP found · Free to start
A waterfall enrichment orchestrator that queries 20+ third-party email/phone data providers in sequence for a given contact, stopping once a verified...

2 more are on the linked page. The cut is the display limit, not a ranking.

## What nobody can tell you from a directory

Hit rate on your list. Every vendor publishes an aggregate number and none of them measured it on your accounts, in your geography, in your segment. The only way to know is to run the same hundred contacts through two or three and count. This directory measures none of that: it tells you which ones an agent can call and which ones you can get into.

## The guardrail

Put a hard cap on the tool call itself, not in the prompt. An agent that finds an address, fails verification, and retries with a different vendor is a sensible design and also a very efficient way to spend three months of credits in one evening.

## Sources

- [The GTM MCP Directory, find a work email](../jobs/find-work-email.md) this site
- [The GTM MCP Directory, verify an email is deliverable](../jobs/verify-email-deliverable.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-28. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which tools can find a work email address with an AI agent?](which-tools-can-find-a-work-email.md)
- [Which tools can verify an email address is deliverable?](which-tools-can-verify-an-email-address.md)
- [Can an AI agent send email on my behalf?](can-an-ai-agent-send-email-on-my-behalf.md)
- [What is data enrichment in sales?](what-is-data-enrichment.md)

## In the directory

- [Find a work email](../jobs/find-work-email.md)
- [Free tiers](../lists/free-api-tiers.md)
