# What is an MCP server? A plain definition, plus how many GTM tools have one

> An MCP server is a small program that exposes one system's capabilities to an AI agent in a standard shape. 156 of 293 GTM tools ship one officially. Counted 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is an MCP server?

**The short answer**

An MCP server is a small program that sits in front of one system and offers its capabilities to an AI agent in a standard shape, so any agent that speaks the Model Context Protocol can call that system without custom integration code being written for it first.

Before MCP, connecting an agent to a tool meant writing glue: read the vendor's API docs, wrap the endpoints you care about in functions, describe those functions to the model, handle the auth, and then do the whole thing again for the next tool and again for the next agent framework. The work scaled with tools multiplied by agents.

An MCP server collapses that. The server is written once, by whoever knows the system best, and it advertises three kinds of thing to any client that connects: **tools**, which are actions the agent can invoke; **resources**, which are pieces of context the agent can read; and **prompts**, which are reusable instruction templates the user can trigger. The agent discovers what is available at connection time rather than being told in advance, which is why the same agent can pick up a server it has never seen and use it correctly.

Two things an MCP server is not. It is not a hosted service you sign up for, necessarily: many run as a local process on your own machine and talk to the client over standard input and output. And it is not a security boundary you get for free. The server runs with whatever credentials you hand it, and it can only be as careful as the person who wrote it.

## How many GTM tools actually have one

This directory checked 293 go to market tools and found **156 with an official server**, the vendor's own, plus 26 where somebody outside the vendor built one. That is 62% of the entries reachable by an agent through MCP at all. 87 had no server found on the date they were checked, and 15 could not be settled either way.

The gap between those two numbers is the whole reason this directory exists. A category can be sold entirely on the language of AI and still have almost nothing an agent can call.

## What to check before you trust one

- **Who built it.** A vendor maintained server and a weekend wrapper both work on day one. Only one of them is somebody's job on day two hundred.

- **How it authenticates.** 52 of the 182 servers in this directory use OAuth, which keeps a revocable scoped token on the vendor side. Others take an API key you paste into a config file. [The full auth breakdown is here](../lists/auth-types.md).

- **What it can reach.** A server is a door into a system. The permissions on the credential you give it are the only thing deciding how far into that system an agent can walk.

## Sources

- [Model Context Protocol, official documentation](https://modelcontextprotocol.io) https://modelcontextprotocol.io
- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [Anthropic, Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) https://www.anthropic.com/news/model-context-protocol
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is the Model Context Protocol?](what-is-the-model-context-protocol.md)
- [What is the difference between an official and a community MCP server?](official-vs-community-mcp-server.md)
- [Which GTM tools have official MCP servers?](which-gtm-tools-have-official-mcp-servers.md)
- [How do I add an MCP server to my AI client?](how-do-i-add-an-mcp-server-to-claude-desktop.md)

## In the directory

- [The 156 official servers](../lists/official-mcp-servers.md)
- [Every MCP status](../mcp/index.md)
