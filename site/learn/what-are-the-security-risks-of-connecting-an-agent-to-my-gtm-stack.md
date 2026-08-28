# MCP security risks in a GTM stack: credentials, injection and blast radius

> Connecting an agent to your CRM, your enrichment vendors and your mailbox creates four specific risks. What they are, and what the auth data across GTM MCP servers says about them.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What are the security risks of connecting an AI agent to my GTM stack?

**The short answer**

Four risks matter: the credential you hand the server can usually do far more than the one task, tool results are untrusted text that can carry instructions the model may follow, a community server is code from a stranger running on your machine, and an agent that can send or write can do it at machine speed before anybody notices.

## 1. The credential is the blast radius

An MCP server does what your credential allows, not what the tool description says. A CRM key scoped to full access does not become read only because the agent was only asked to read. Scope the credential at the vendor, not in the prompt. Of the 165 servers counted here, [the OAuth ones](../lists/auth-oauth.md) are the better shape for this: the token is scoped and revocable from the vendor side without touching the agent's config.

## 2. Tool output is untrusted input

An agent reads what a tool returns. A scraped page, an inbound email, a CRM note or a form submission can contain text written by someone who wants your agent to do something. If that text reaches the model and the model can call tools, the instruction can be acted on. This is the single most GTM specific risk on this list, because the entire job involves ingesting text strangers wrote. Keep destructive tools behind human approval and do not let a research step and a send step share an unsupervised loop.

## 3. A community server is somebody's code on your machine

21 entries here have a community server, and a locally installed server runs with your user's permissions. Read who published it, whether the vendor acknowledges it, and what it wants access to. The repo health rail that would date stamp each one has not been run for this build, so this directory publishes no staleness claim at all rather than a stale one.

## 4. Speed is the amplifier

Every failure above already existed with scripts. What is new is that nobody wrote the sequence in advance. 45 entries here are tagged [run an email sequence](../jobs/run-email-sequence.md) and 28 are tagged [write crm records](../jobs/write-crm-records.md). Those two capabilities in one unsupervised loop is how a bad enrichment result becomes two thousand wrong emails and a polluted CRM in the same afternoon.

## The short checklist

- Separate read credentials from write credentials, and prefer OAuth where the vendor offers it.

- Require approval on anything that sends, spends or writes.

- Log every tool call with its arguments. If you cannot answer what the agent did on Tuesday, you do not have an agent, you have an incident waiting for a date.

- Sandbox a new server before it touches production data, and read the verbatim auth field on its tool page first.

## Sources

- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [Model Context Protocol, official documentation](https://modelcontextprotocol.io) https://modelcontextprotocol.io
- [The GTM MCP Directory, servers by auth type](../lists/auth-types.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-28. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which GTM MCP servers use OAuth instead of an API key?](which-gtm-mcp-servers-use-oauth.md)
- [What is the difference between a local and a remote MCP server?](stdio-vs-remote-mcp-servers.md)
- [How do I stop an AI agent writing bad data to my CRM?](how-do-i-stop-an-agent-writing-bad-data-to-my-crm.md)
- [Can an AI agent send email on my behalf?](can-an-ai-agent-send-email-on-my-behalf.md)

## In the directory

- [Servers by auth type](../lists/auth-types.md)
