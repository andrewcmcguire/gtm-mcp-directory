# Local (stdio) vs remote (HTTP) MCP servers: which one you are installing

> A local MCP server runs as a process on your machine and talks over standard input and output. A remote one is a URL you connect to. The practical differences: credentials, latency, updates and who can see your queries.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is the difference between a local and a remote MCP server?

**The short answer**

A local MCP server runs as a process on your own machine and talks to the client over standard input and output. A remote server is an HTTP endpoint you point the client at. Local means your credentials stay on your machine and you control the version. Remote means the vendor updates it and nothing has to be installed.

Every MCP server has to answer the same question: how do the bytes get from the client to the server. There are two established answers.

## Local, over standard input and output

The client launches the server as a child process and they talk over stdin and stdout. Nothing listens on a port, nothing crosses the network, and the server has whatever access your user account has. This is why so many install snippets are a command and a list of arguments rather than a URL. It is also why a local server can reach your file system, and why installing one from an unknown source is the same class of decision as installing any other program.

## Remote, over HTTP

The client connects to a URL the vendor hosts. Nothing is installed, the vendor ships fixes without you doing anything, and the auth is usually a browser sign in rather than a pasted key. The tradeoffs are the ordinary ones for hosted software: your queries reach their infrastructure, an outage on their side is an outage for your agent, and you are on whatever version they deployed this morning.

## Which one the GTM tools ship

Both, and the entries say which. Of the 165 servers found in this directory, 174 carry a parseable URL in their mcp_url field and 47 of those URLs point at a GitHub repository rather than a hosted endpoint, which is a strong hint the install is a local one you run yourself. The transport is recorded verbatim on the tool page wherever the vendor documents it, including one entry where the vendor's own registry record and a third party directory disagree about the transport and both are printed rather than one being picked.

## The practical rule

If the setup asks for a command, it is local and your machine is the boundary. If it asks for a URL and sends you to a browser, it is remote and the vendor is the boundary. Read the auth field on the tool page before either one: that field is copied verbatim from the vendor's documentation on this site precisely because it is the sentence that decides how much of your account is now reachable.

## Sources

- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [Model Context Protocol, connect an MCP server to a client](https://modelcontextprotocol.io/quickstart/user) https://modelcontextprotocol.io/quickstart/user
- [Model Context Protocol, official documentation](https://modelcontextprotocol.io) https://modelcontextprotocol.io

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-25. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is an MCP server?](what-is-an-mcp-server.md)
- [How do I add an MCP server to my AI client?](how-do-i-add-an-mcp-server-to-claude-desktop.md)
- [Which GTM MCP servers use OAuth instead of an API key?](which-gtm-mcp-servers-use-oauth.md)
- [What are the security risks of connecting an AI agent to my GTM stack?](what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack.md)

## In the directory

- [Servers by auth type](../lists/auth-types.md)
