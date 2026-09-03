# MCP tools, resources and prompts: the three things a server offers

> An MCP server can expose three kinds of capability: tools the agent invokes, resources it reads, and prompts a user triggers. What each one is for, and which one you actually care about for GTM work.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What are MCP tools, resources and prompts?

**The short answer**

An MCP server offers three kinds of thing. Tools are actions the model can invoke and that can change something. Resources are data the client can read into context. Prompts are prewritten instruction templates a user chooses. For go to market work, tools are almost always the part that matters.

**Tools** are functions with a name, a description and a typed argument schema. The model picks one, fills the arguments and the client executes it. Anything that finds a person, writes a record, sends a message or spends credits is a tool. Tools are model controlled, which is exactly why the approval behaviour in your client matters.

**Resources** are addressable pieces of context: a file, a record, a document, a query result. They are read, not run. The application decides which resources to pull into context, so they are application controlled rather than model controlled. In a GTM stack a resource is typically the account record or the transcript you want the model to reason over.

**Prompts** are reusable instruction templates the server publishes, surfaced in the client as something a person picks deliberately. They are user controlled. A vendor might ship a prompt for "prepare me for this call" that pulls the right resources and calls the right tools in the right order.

## Why the split exists

Three different parties decide. The model chooses tools, the application chooses resources, the human chooses prompts. That is a permission design, not a filing system, and it is the part of MCP most worth understanding before you connect an agent to anything that can send email on your behalf.

## What this means for the GTM stack

When a vendor here says it ships an MCP server, in practice that nearly always means tools: search, enrich, create, send. This directory records what the vendor documents and does not enumerate the tool surface of each server, because that would need each server to be installed and run, and 0 tools in this directory have been run by anybody here.

The closest published proxy is the job tags. 827 tags across 271 entries record what each vendor says its tool does, in the agent's own phrasing, which is the vocabulary you would expect its tools to be named after.

## Sources

- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [Model Context Protocol, official documentation](https://modelcontextprotocol.io) https://modelcontextprotocol.io
- [modelcontextprotocol/servers, the reference server repository](https://github.com/modelcontextprotocol/servers) https://github.com/modelcontextprotocol/servers

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is an MCP server?](what-is-an-mcp-server.md)
- [What is an MCP client?](what-is-an-mcp-client.md)
- [What is the Model Context Protocol?](what-is-the-model-context-protocol.md)
- [How do I stop an AI agent writing bad data to my CRM?](how-do-i-stop-an-agent-writing-bad-data-to-my-crm.md)

## In the directory

- [Every job an agent asks for](../jobs/index.md)
