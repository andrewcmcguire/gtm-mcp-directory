# What does it cost to run a GTM agent? What this directory can and cannot tell you

> This directory tracks access gates, not prices. What it can tell you: 61 tools are free to start and 77 need a contract. What it cannot, and where the cost actually lands.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How much does it cost to run an AI agent on a GTM stack?

**The short answer**

This directory does not track prices, credits or quotas, so it cannot give you a number and will not pretend to. What it can tell you is which doors open without a sales call: 61 entries are free to start, 113 are paid self serve, and 77 need a contract.

## What is actually being tracked here

- **Tracked:** the access gate, in four buckets, with a source URL, for every entry. 32 entries could not be established from public sources and are published as unknown rather than guessed.

- **Not tracked:** price, credit cost per lookup, quota size, rate limits, overage behaviour, minimum contract value, or what a free tier does with your data. None of it should be inferred from anything on this site.

## Where the cost actually lands

Three places, and the model is usually the smallest of them.

- **Metered data calls.** Enrichment, verification and intent are priced per lookup, and an agent generates lookups at a rate no human workflow ever did. This is where budgets go.

- **Seats and contracts.** The 77 enterprise gated entries here carry a floor that has nothing to do with usage.

- **Model tokens.** Real, and usually the line item people worry about first and should worry about third.

## The cheapest honest way to find out

Build the smallest end to end chain on free tiers, run a hundred records through it, and count. 46 products here are both free to start and have an MCP server, which is enough to build a research and contact chain without spending anything. [The free tier list is here.](../lists/free-api-tiers.md)

## The control that saves you

Cap the tool call, not the prompt. A hard limit on calls per run, enforced in your client or your wrapper, is the difference between an experiment and an invoice. An agent that retries a failed lookup against three vendors is a sensible design and an extremely efficient way to spend a quarter's credits in an evening.

## Sources

- [The GTM MCP Directory, by access gate](../gates/index.md) this site
- [The GTM MCP Directory, free API tiers](../lists/free-api-tiers.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is an API access gate and why does it matter for AI agents?](what-is-an-api-access-gate.md)
- [Which GTM MCP servers are free to use?](which-mcp-servers-are-free-to-use.md)
- [Which GTM tools can a solo operator use with an AI agent?](which-gtm-tools-can-a-solo-operator-use.md)
- [How many GTM tools are enterprise gated?](how-many-gtm-tools-are-enterprise-gated.md)

## In the directory

- [Free tiers](../lists/free-api-tiers.md)
- [By access gate](../gates/index.md)
