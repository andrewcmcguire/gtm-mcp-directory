# How do I connect Claude to my CRM? The MCP route, step by step

> Connect an AI assistant to your CRM through an MCP server. Which CRM and RevOps tools have one (21 official of 23), what to check first, and the order to do it in.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I connect Claude to my CRM?

**The short answer**

If your CRM ships an MCP server, you add it to your client's server configuration, authenticate, and the assistant can then read and write records as tools. If it does not, you either use a community server, an automation platform that proxies tool calls, or you write a thin wrapper over the CRM's REST API yourself.

## 1. Find out whether a server exists

RevOps Infra is the best covered layer in this directory: 21 official servers and 0 community across 23 entries, with only 1 where none was found. Check your specific system on [the RevOps tools with MCP servers list](../lists/mcp-revops-infra.md), and read the auth field on its page before anything else.

## 2. Decide what the credential is allowed to do

This is the step people skip and regret. The server can do whatever your credential can do, and an instruction not to write is a suggestion rather than a boundary. Create a dedicated integration user or a scoped token at the CRM, not a copy of your admin credentials. Where the vendor offers OAuth, take it: the token is scoped and you can revoke it from their side without touching your config.

## 3. Add the server to the client

A local server is a command the client launches. A remote one is a URL the client connects to, usually followed by a browser sign in. The local shape looks like this, and the exact block comes from your vendor's own documentation rather than from here.

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

## 4. Test reads before you allow writes

Ask for a record you already know the answer to. Check the field names come back the way you expect, that record ownership and permissions behave, and that the record limit on a query is what you assumed. Only then let anything write.

## 5. Wire the rest of the chain

A CRM connection on its own is a search box. The value shows up when the assistant can also research and enrich, then write the result back.

| Step | The job | Tools tagged | Official MCP | Free tier |
|---|---|---|---|---|
| Read CRM records | [read crm records](../jobs/read-crm-records.md) | 13 | 10 | 5 |
| Write CRM records | [write crm records](../jobs/write-crm-records.md) | 28 | 18 | 7 |
| Sync records between systems | [sync records between systems](../jobs/sync-records-between-systems.md) | 9 | 8 | 6 |
| Enrich a company from a domain | [enrich a company from a domain](../jobs/enrich-company-from-domain.md) | 34 | 24 | 15 |
| Research an account before a call | [research an account before a call](../jobs/research-account-for-call-prep.md) | 17 | 10 | 3 |

## If your CRM has no server

9 entries in this directory are tagged [proxy tool calls to saas apps](../jobs/proxy-tool-calls-to-saas.md): platforms that stand between an agent and somebody's SaaS and expose the calls as tools. That is the fastest route and it puts a third party in the middle of your credential, which is a tradeoff to make deliberately rather than by accident.

## Sources

- [The GTM MCP Directory, RevOps Infra](../categories/revops-infra.md) this site
- [Model Context Protocol, connect an MCP server to a client](https://modelcontextprotocol.io/quickstart/user) https://modelcontextprotocol.io/quickstart/user
- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-04. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [How do I stop an AI agent writing bad data to my CRM?](how-do-i-stop-an-agent-writing-bad-data-to-my-crm.md)
- [Which CRM and RevOps tools have MCP servers?](which-crm-and-revops-tools-have-mcp-servers.md)
- [How do I add an MCP server to my AI client?](how-do-i-add-an-mcp-server-to-claude-desktop.md)
- [What are the security risks of connecting an AI agent to my GTM stack?](what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack.md)

## In the directory

- [RevOps tools with MCP servers](../lists/mcp-revops-infra.md)
- [Write CRM records](../jobs/write-crm-records.md)
