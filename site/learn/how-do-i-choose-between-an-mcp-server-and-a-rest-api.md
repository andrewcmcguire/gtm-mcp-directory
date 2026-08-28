# MCP server or REST API? When each one is the right call for a GTM agent

> An MCP server is faster to wire and the vendor decides what it exposes. A REST API is more work and you decide. When each is right, with the coverage numbers that force the decision.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# Should I use a tool's MCP server or its REST API?

**The short answer**

Use the MCP server when it exists and exposes what you need: it is faster to wire, and any client can use it. Use the REST API when you need something the server does not expose, when you want tight control over rate limits and error handling, or when there is no server at all, which is the case for 117 of 293 entries here.

## What each one gives you

| | MCP server | REST API plus your own wrapper |
|---|---|---|
| Time to first call | Minutes, if a server exists | Hours to days |
| Who decides the surface | The vendor | You |
| Reuse across clients | Any MCP client | Whatever you wrote it for |
| Rate limit and retry control | Whatever the server does | Yours |
| Breaks when | The vendor changes the server | The vendor changes the API |
| Available for | 165 of 293 entries here | Most of the rest, if they document one |

## The honest default

Start with the server if there is one. The whole point of a protocol is that you stop writing the same integration twice, and 144 vendors here have already done the work for you. Move to the API when you hit a specific wall, and you will know exactly which wall it was.

## When the API is clearly right

- **The server is thin.** A server exposing three tools over an API with forty endpoints is a demo. Read the vendor's docs before assuming parity.

- **You need volume.** Batch and pagination behaviour is where an agent oriented server and a data pipeline part company.

- **The server is community built and you cannot carry the risk.** 21 entries here are in that position.

- **There is no server.** 117 entries, and 263 of 293 entries have no documentation URL recorded either, which is its own kind of answer.

## The thing that decides it more often than either

The access gate. 77 entries need a contract before you get any credential at all, and at that point the protocol question is academic. Check [the gate](../gates/index.md) before you design either integration.

## Sources

- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [The GTM MCP Directory, by MCP status](../mcp/index.md) this site
- [The GTM MCP Directory, by access gate](../gates/index.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-28. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is an MCP server?](what-is-an-mcp-server.md)
- [Which GTM tools have no MCP server?](which-gtm-tools-have-no-mcp-server.md)
- [How do I build an MCP server for a tool that does not have one?](how-do-i-build-an-mcp-server-for-a-tool-that-has-none.md)
- [What is an API access gate and why does it matter for AI agents?](what-is-an-api-access-gate.md)

## In the directory

- [By MCP status](../mcp/index.md)
- [By access gate](../gates/index.md)
