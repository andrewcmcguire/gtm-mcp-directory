# What is an MCP client? The apps that can connect to an MCP server

> An MCP client is the piece inside an AI application that holds a connection to one MCP server. Which apps have one, and why it decides what your agent can do more than the model does.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is an MCP client?

**The short answer**

An MCP client is the component inside an AI application that opens and holds one connection to one MCP server. The application you use is the host; it runs one client per server it is connected to. If your app has no MCP client, no MCP server on earth is useful to it.

The distinction matters when something does not work. People say the server is broken when the actual problem is that their application does not support the transport the server uses, or does not support MCP at all.

Host applications with MCP client support include Anthropic's own Claude apps and Claude Code, and coding environments and assistants that have added it. The auth notes recorded on entries in this directory name **Claude, ChatGPT and Cursor** as the clients whose sign in flows vendors write documentation for, which is a useful signal about where adoption actually is: vendors document against the clients their customers use.

## What the client is responsible for

- **Discovery.** Asking the server what tools, resources and prompts it offers, and handing that list to the model.

- **Permission.** Deciding whether a tool call the model wants to make gets executed, and whether a human is asked first. This is the single most important behaviour and it is implemented by the client, not by the protocol and not by the server.

- **Transport.** Launching a local server as a subprocess, or connecting to a remote one over HTTP and handling the auth.

## Why this decides what your agent can do

Two people can run the same model against the same server and get different capabilities, because their clients differ in what they expose and how they gate approval. When you are choosing where to build a GTM agent, the client's permission model is worth more attention than the model's benchmark scores. An agent that writes to your CRM with no approval step is a different risk than the same agent asking first, and that choice lives in the client.

This directory records the vendor side of that relationship: which vendors ship a server, what it authenticates with, and whether you can get an account without a sales call. Which client you point at it is your decision and there is no ranking of clients here.

## Sources

- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [Model Context Protocol, connect an MCP server to a client](https://modelcontextprotocol.io/quickstart/user) https://modelcontextprotocol.io/quickstart/user
- [Model Context Protocol, official documentation](https://modelcontextprotocol.io) https://modelcontextprotocol.io

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-28. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is an MCP server?](what-is-an-mcp-server.md)
- [What is the Model Context Protocol?](what-is-the-model-context-protocol.md)
- [How do I add an MCP server to my AI client?](how-do-i-add-an-mcp-server-to-claude-desktop.md)
- [How do I stop an AI agent writing bad data to my CRM?](how-do-i-stop-an-agent-writing-bad-data-to-my-crm.md)

## In the directory

- [The MCP layer category](../categories/mcp-infrastructure.md)
