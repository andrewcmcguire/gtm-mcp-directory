# How do I add an MCP server to an AI client? Local and remote, step by step

> Adding an MCP server to a client: the two shapes it takes, what each field in the config does, where credentials go, and the four things that go wrong most often.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I add an MCP server to my AI client?

**The short answer**

There are two shapes. A local server is a command the client launches as a subprocess, configured with a command, its arguments and any environment variables it needs. A remote server is a URL you point the client at, usually followed by a browser sign in. Your client's own documentation is the authority on where that configuration lives.

## The local shape

The client starts the server as a child process and talks to it over standard input and output. Nothing listens on a port and nothing crosses the network. The configuration is a name, a command, its arguments, and the environment the process needs.

```
{
 "mcpServers": {
 "some-gtm-tool": {
 "command": "npx",
 "args": ["-y", "@vendor/mcp-server"],
 "env": { "VENDOR_API_KEY": "the key you generated in the vendor dashboard" }
 }
 }
}
```

Three details that matter. The name is yours and appears in the client. The command has to be on the path the client uses, which is often not the path your shell uses. And the environment block is where credentials go: they live in a file on your machine, in plain text, so treat that file the way you would treat any other file holding an API key.

## The remote shape

You give the client a URL, it connects over HTTP, and auth is usually a browser sign in that hands back a scoped token. Nothing is installed and the vendor ships updates without you. Of the 165 servers counted here, [the OAuth ones](../lists/auth-oauth.md) are almost all this shape.

## The four things that go wrong

- **The client does not support it.** Not every AI application has an MCP client, and some support only one transport. That is a client limitation, not a broken server.

- **The command is not found.** Use an absolute path, or check what environment the client launches processes in.

- **The credential is wrong or unscoped.** Read the verbatim auth line on the tool page in this directory before you generate anything; several vendors require a specific plan or an account level flag before MCP access works at all.

- **It connected and there are no tools.** Usually an auth failure that the client reported quietly. Check the server's own logs.

## Where to find the right block

Every tool page here prints the vendor's mcp_url and mcp_auth verbatim, exactly as recorded, plus a link to the vendor's own documentation where one is published. 174 entries carry a parseable URL and 30 carry a documentation URL. No install snippet is reproduced anywhere on this site, because a snippet copied from a directory is a snippet that goes stale without anybody noticing.

## Sources

- [Model Context Protocol, connect an MCP server to a client](https://modelcontextprotocol.io/quickstart/user) https://modelcontextprotocol.io/quickstart/user
- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [modelcontextprotocol/servers, the reference server repository](https://github.com/modelcontextprotocol/servers) https://github.com/modelcontextprotocol/servers

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-25. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is the difference between a local and a remote MCP server?](stdio-vs-remote-mcp-servers.md)
- [What is an MCP client?](what-is-an-mcp-client.md)
- [How do I connect Claude to my CRM?](how-do-i-connect-claude-to-my-crm.md)
- [Which GTM MCP servers use OAuth instead of an API key?](which-gtm-mcp-servers-use-oauth.md)

## In the directory

- [The official servers list](../lists/official-mcp-servers.md)
- [Servers by auth type](../lists/auth-types.md)
