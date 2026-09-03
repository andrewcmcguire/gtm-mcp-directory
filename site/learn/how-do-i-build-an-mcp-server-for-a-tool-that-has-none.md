# How do I build an MCP server for a GTM tool that has none? Scope it small

> 110 GTM tools in this directory have no MCP server. What to build instead of a full API wrapper, and which gaps are worth filling first.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I build an MCP server for a tool that does not have one?

**The short answer**

Wrap the three or four calls you actually need as tools, not the vendor's whole API. Name each tool after the job an agent asks for rather than after the endpoint, keep the credential outside the code, and expect to maintain it when the vendor changes something.

## Scope it by job, not by endpoint

The mistake is mirroring the API. An agent does not want `GET /v2/contacts` with nineteen query parameters, it wants one tool called something like find a work email that takes a name and a domain. This directory's job vocabulary is exactly that shape: 55 verbs with objects, phrased from the agent's side, and it is a reasonable naming source for your tool surface.

## The practical checklist

- **Read the protocol documentation first**, and use an official SDK rather than hand rolling the message layer.

- **Keep credentials in the environment**, never in the tool arguments where they end up in a model's context.

- **Write the tool descriptions for the model.** They are the interface. Say what a tool does, what it costs, and what it returns when it finds nothing.

- **Return structured errors.** An agent that is told a lookup found nothing behaves; an agent handed an empty object hallucinates.

- **Rate limit inside the server.** The agent will not do it for you.

## Which gaps are worth filling

110 entries here have no server found. The more interesting cut is by job: some jobs have no tool at all with a first party server, which means every agent builder who needs that capability is currently writing the same wrapper. [The list of jobs with zero official servers is published here.](../learn/which-gtm-jobs-have-no-official-mcp-server.md)

## Before you publish it

Check the vendor's terms. A server that automates access in a way their terms forbid is a problem you inherit, not one you solved. And if you do publish it, tell them: a community server the vendor knows about is considerably more likely to survive their next API change.

If you build one for a tool listed here, [send it in](../submit.md). It gets recorded as community, with your URL, and the entry stops saying none found.

## Sources

- [Model Context Protocol, official documentation](https://modelcontextprotocol.io) https://modelcontextprotocol.io
- [modelcontextprotocol/servers, the reference server repository](https://github.com/modelcontextprotocol/servers) https://github.com/modelcontextprotocol/servers
- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [The GTM MCP Directory, submit a tool](../submit.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which GTM jobs can no tool do through an official MCP server?](which-gtm-jobs-have-no-official-mcp-server.md)
- [Which GTM tools have no MCP server?](which-gtm-tools-have-no-mcp-server.md)
- [What is the difference between an official and a community MCP server?](official-vs-community-mcp-server.md)
- [Should I use a tool's MCP server or its REST API?](how-do-i-choose-between-an-mcp-server-and-a-rest-api.md)

## In the directory

- [Jobs with no official server](../learn/which-gtm-jobs-have-no-official-mcp-server.md)
- [Submit a server](../submit.md)
