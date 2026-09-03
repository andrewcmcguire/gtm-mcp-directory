# What is the Model Context Protocol (MCP)? The open standard, explained

> The Model Context Protocol is an open standard for connecting AI applications to external tools and data, published by Anthropic and adopted across the industry. What it standardises and what it deliberately does not.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is the Model Context Protocol?

**The short answer**

The Model Context Protocol, or MCP, is an open standard that defines how an AI application talks to an external system: how it discovers what is available, how it calls a tool, and how results come back. Anthropic published it and released it as an open specification with reference implementations.

MCP describes a client and a server exchanging JSON-RPC messages. The **host** is the application a person is actually using. Inside it, a **client** holds one connection to one **server**, and the server is the thing that knows how to talk to a particular system: a database, a file system, a CRM, a search index.

What the standard fixes is the shape of the conversation. How a server declares its tools, how arguments are described, how a call is made, how errors and results are returned, how a server can ask the client for something back. Because that shape is fixed, an agent does not need bespoke code per integration, and a vendor does not need to ship a different connector for every AI product on the market.

What the standard deliberately does not fix is what any of it means. MCP will not tell you whether a tool called `search_contacts` returns verified emails or guesses, whether the account behind it has quota left, or whether the vendor will still maintain the server next quarter. Those are directory questions, not protocol questions, which is precisely the gap this site was built to fill.

## Where it stands

The specification is versioned by date and has been revised several times since first release, adding an authorization framework, a streamable HTTP transport alongside the original local transport, and richer tool output. Read the versioned spec rather than any blog post, including this one, for the current state of it.

Adoption is visible in this directory's own data rather than in anyone's press release. 147 of 293 go to market vendors ship a first party server today, and the auth notes on those entries name Claude, ChatGPT and Cursor as the clients they document sign in flows for.

## Why it matters for go to market work

GTM runs on a stack of systems that do not talk to each other: a CRM, an enrichment vendor, a sequencer, a call recorder, a warehouse. The reason a GTM engineer spends their week on plumbing is that every pair of those systems needs its own bridge. A protocol that makes each system speak once, to anything, is the first credible attack on that problem, and the reason it matters to measure which vendors have actually adopted it.

## Sources

- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [Anthropic, Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) https://www.anthropic.com/news/model-context-protocol
- [modelcontextprotocol/servers, the reference server repository](https://github.com/modelcontextprotocol/servers) https://github.com/modelcontextprotocol/servers

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-02. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is an MCP server?](what-is-an-mcp-server.md)
- [What is an MCP client?](what-is-an-mcp-client.md)
- [What are MCP tools, resources and prompts?](what-are-mcp-tools-resources-and-prompts.md)
- [What is the difference between a local and a remote MCP server?](stdio-vs-remote-mcp-servers.md)

## In the directory

- [The MCP layer category](../categories/mcp-infrastructure.md)
