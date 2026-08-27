# How do I audit my GTM stack for agent readiness? A four column spreadsheet

> A repeatable audit of your own stack: four columns, one row per tool, and the three numbers that tell you whether an agent can do anything useful in it.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I audit my GTM stack for agent readiness?

**The short answer**

List every tool you pay for, then fill four columns: does it have an MCP server, who built it, how does it authenticate, and can you get API access on your current contract. Sort by the jobs you actually need. The gaps are your roadmap and usually two or three of them matter.

## The four columns

- **Server.** Official, community, none found, or unknown. Look it up on the tool's page here, then confirm against the vendor's own developer documentation.

- **Maintainer.** Official means first party and nothing else. A wrapper from an integration platform is community, whoever built it.

- **Auth.** OAuth, API key, or both. This decides what your security review will say and how much of your account a leaked credential exposes.

- **Your access.** Not the published gate, your actual contract. Plenty of enterprise gated tools are wide open to a customer who already has the agreement, which is why 31 entries here ship an official server behind a gate that is irrelevant if you are already inside it.

## Then sort by job, not by category

A stack audit by category tells you what you bought. An audit by job tells you what an agent can do. Take the five or six jobs your team actually needs, and check coverage on each one against the 55 job pages here. The [jobs index](../jobs/index.md) carries the official server count and the solo reachable count for every one of them.

## The three numbers to write at the top

- **Reachable share.** How many of your tools an agent can call at all. The directory wide figure is 56%, so anything above that is a good stack for this.

- **The broken link.** The one job in your critical chain with no coverage. There is almost always exactly one, and it is worth more attention than the other nine.

- **Write surface.** How many of your reachable tools can change something rather than only read. That number is your risk register.

## Then do the boring part

Re-run it quarterly. This is the fastest moving column in the whole dataset: the same audit six months from now will have different answers, and the only way to see the movement is to have written the first one down with dates on it. That is exactly why every number on this site ships with the date it was measured.

## Sources

- [The GTM MCP Directory, by job](../jobs/index.md) this site
- [The GTM MCP Directory, the counted data](../data.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-25. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What does agent ready mean for a GTM tool?](what-does-agent-ready-mean.md)
- [How do I check whether a tool has an MCP server?](how-do-i-check-if-a-tool-has-an-mcp-server.md)
- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)
- [What is a GTM tech stack?](what-is-a-gtm-tech-stack.md)

## In the directory

- [Every job](../jobs/index.md)
- [The data endpoint](../data.md)
