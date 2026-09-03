# Which GTM MCP servers use OAuth? The auth split across every server, counted

> Of the 182 GTM tools with an MCP server, 102 document an OAuth flow and 97 document an API key. Why the difference matters, and the full breakdown. Counted 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / What the data says

**What the data says**

# Which GTM MCP servers use OAuth instead of an API key?

**The short answer**

Of the 182 GTM tools with an MCP server in this directory, 102 document an OAuth or browser sign in flow and 97 document an API key or token. Some document both, usually OAuth for the hosted server and a key for the self hosted one.

This is a security question wearing a configuration question's clothes. OAuth hands the server a scoped token that the vendor can revoke without you touching anything. An API key is a string you paste into a config file on the machine running the agent, it is as powerful as whatever the vendor scoped it to, and it is revoked by rotating it and updating every place it was pasted.

Neither is wrong. Knowing which one you are about to wire in is not optional, particularly when the system on the other side can send mail as you or write to the system of record.

## The breakdown

| Auth | Servers | What it means |
|---|---|---|
| [OAuth](../lists/auth-oauth.md) | 52 | The server takes the user through a browser sign in and holds a scoped token. Nothing is pasted into a config... |
| [API key](../lists/auth-api-key.md) | 47 | The server authenticates with a key or token the operator generates and pastes in. Simple to wire, and the... |
| [OAuth or an API key](../lists/auth-either.md) | 50 | Both paths are documented. Usually OAuth for a hosted server and a key for the self hosted or legacy endpoint. |
| [Third party platform auth](../lists/auth-third-party.md) | 7 | Auth is handled by a connector platform sitting between the agent and the vendor, so the credential lives... |
| [Auth not recorded](../lists/auth-unrecorded.md) | 26 | The mcp_auth field on the entry is blank, or says unknown. Published as blank rather than guessed. |

Counted 2026-09-03 across the 182 entries with a server. The bucket is a keyword match over the mcp_auth field, run at build time and disclosed as such; the verbatim field is printed beside every row on [the auth pages](../lists/auth-types.md) so you can check the parse yourself. 288 of 293 entries record an auth value at all.

## What the OAuth entries have in common

They are mostly hosted, remote servers, and their documentation names the clients they were tested against. Several entries in this directory record sign in flows written specifically for Claude, ChatGPT and Cursor, which tells you where vendors think their customers are.

## The pattern to copy

Where a vendor offers both, take OAuth for anything running on a machine you do not physically control, and keep API keys for local servers where the key never leaves your box. Then scope the credential at the vendor rather than trusting the prompt: a read only key is a boundary, an instruction not to write is a suggestion.

## Sources

- [The GTM MCP Directory, servers by auth type](../lists/auth-types.md) this site
- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What are the security risks of connecting an AI agent to my GTM stack?](what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack.md)
- [What is the difference between a local and a remote MCP server?](stdio-vs-remote-mcp-servers.md)
- [What is an MCP server?](what-is-an-mcp-server.md)
- [How do I add an MCP server to my AI client?](how-do-i-add-an-mcp-server-to-claude-desktop.md)

## In the directory

- [Servers by auth type](../lists/auth-types.md)
