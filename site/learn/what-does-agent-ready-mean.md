# What does agent ready mean? A definition you can check, not a marketing claim

> Agent ready is vendor language. Here is the version you can verify: does a server exist, who maintains it, how does it authenticate, and can you get in without a contract. Measured across 293 GTM tools.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What does agent ready mean for a GTM tool?

**The short answer**

Agent ready is a marketing phrase with no agreed definition, and at least one large vendor markets it as product language. The checkable version is four questions: is there an MCP server or a documented API, did the vendor build it, how does it authenticate, and can one person get access without a procurement cycle.

This site does not use agent ready as a rating, because a rating nobody can reproduce is an opinion. It publishes the inputs instead, and lets you decide what threshold you care about.

## The four checks

- **Is there a server at all.** 144 of 293 entries have an official one, 21 have a community one, 117 had none found on the date checked, and 7 could not be settled.

- **Who maintains it.** Official means first party. A wrapper built by a third party integration platform does not count here no matter how well it works, because the failure mode is different: a community server can be abandoned without the vendor ever noticing.

- **How does it authenticate.** OAuth with a scoped, revocable token is a different security conversation from an API key in a config file. [The split across every server here is published.](../lists/auth-types.md)

- **Can you get in.** 174 of 293 entries are free to start or paid self serve, and 77 need a contract. Cross that with the server column and 123 entries pass both tests. An official MCP server behind a procurement cycle is not agent ready for most of the people reading this.

## The trap in the phrase

An impressive number of tools describe themselves as built for agents while shipping nothing an external agent can call. The two claims live in different places: one on the homepage, one in the developer docs. The directory records the second and cites it.

The reverse trap is real too. A tool with no MCP server and a clean, documented REST API is often more usable to an agent than a tool with a thin server and no docs. 263 of 293 entries have no documentation URL recorded at all, which is its own signal.

## The phrase itself

Agent ready is in active commercial use as product language by at least one large data vendor, so it is not neutral ground. The term used throughout this site is **agent reachable**, and it means exactly one thing: a server was found, on a stated date, and who built it is recorded.

## Sources

- [The GTM MCP Directory, methodology](../methodology.md) this site
- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [The GTM MCP Directory, by access gate](../gates/index.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-28. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is an MCP server?](what-is-an-mcp-server.md)
- [What is the difference between an official and a community MCP server?](official-vs-community-mcp-server.md)
- [What is an API access gate and why does it matter for AI agents?](what-is-an-api-access-gate.md)
- [How do I audit my GTM stack for agent readiness?](how-do-i-audit-my-gtm-stack-for-agent-readiness.md)

## In the directory

- [By MCP status](../mcp/index.md)
- [By access gate](../gates/index.md)
