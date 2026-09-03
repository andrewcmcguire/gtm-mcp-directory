# API access gates: free, paid, or a procurement cycle before your agent starts

> An access gate is what stands between you and an API key. Across 293 GTM tools: 62 free to start, 112 paid self serve, 77 enterprise only.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is an API access gate and why does it matter for AI agents?

**The short answer**

An API access gate is what a vendor makes you do before you can get programmatic access. Free to start means you sign up and get a key. Paid self serve means you pay and get a key. Enterprise only means a contract, a seat count or a procurement cycle, which for one person with an agent is a closed door.

This is the second column nobody else publishes, and in practice it decides more than the feature list does. A tool with a magnificent API you cannot get into is worth exactly as much to your agent as a tool with no API.

## The four gates, counted

| Gate | Entries | What it means for one person with an agent |
|---|---|---|
| [Free to start](../gates/free.md) | 62 | Sign up, get a key, start calling. No conversation with anybody. |
| [Paid, self serve](../gates/paid.md) | 112 | A credit card is enough. Still no sales call. |
| [Enterprise leaning](../gates/enterprise-leaning.md) | 4 | Self serve on paper, gated in practice. |
| [Enterprise only](../gates/enterprise-only.md) | 77 | Contract, seat minimum or procurement. A solo operator is out. |
| [Unknown](../gates/unknown.md) | 32 | The gate could not be established from public sources and is published as unknown rather than guessed. |

6 further entries record n/a, where an API gate is not a meaningful question. Counted 2026-09-03 across 293 entries.

## Why unknown is such a large number

32 entries carry an unknown gate, and that is itself the finding. A vendor who does not publish whether you can buy API access, at what tier, is telling you something about how they expect you to buy. Unknown is a legal answer in this directory and it ships as unknown rather than being rounded into whichever bucket looks tidier.

## The intersection that matters

MCP status and access gate are separate columns for a reason. 35 entries ship an official MCP server behind an enterprise gate. The server is real, the protocol works, and most people reading this cannot call it. The [132 solo reachable entries](../lists/solo-reachable.md) are the list that matters if you are one person and a credit card.

## Sources

- [The GTM MCP Directory, by access gate](../gates/index.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What does agent ready mean for a GTM tool?](what-does-agent-ready-mean.md)
- [Which GTM tools can a solo operator use with an AI agent?](which-gtm-tools-can-a-solo-operator-use.md)
- [How many GTM tools are enterprise gated?](how-many-gtm-tools-are-enterprise-gated.md)
- [Which data enrichment tools can an AI agent use for free?](which-data-enrichment-tools-can-an-agent-use-for-free.md)

## In the directory

- [By access gate](../gates/index.md)
- [The free tiers](../lists/free-api-tiers.md)
