# How do I stop an AI agent polluting my CRM? Five controls that actually hold

> 28 tools here are tagged with writing CRM records. The five controls that keep an agent from quietly corrupting the system of record, and why the prompt is not one of them.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I stop an AI agent writing bad data to my CRM?

**The short answer**

Scope the credential, separate read from write, require approval on writes, write to a staging field or object before the real one, and log every call with its arguments. The prompt is not a control: an instruction not to write is a suggestion, a read only credential is a boundary.

## The five controls

- **Two credentials, not one.** A read credential for research, a write credential for the one step that writes. 13 entries here are tagged [read crm records](../jobs/read-crm-records.md) and 28 are tagged [write crm records](../jobs/write-crm-records.md). Treat them as different systems.

- **Approval on the write tool.** Implemented in the client, where the human is, not in the prompt where the model is.

- **Write somewhere reversible first.** A staging object, a custom field, or a note, reviewed before it becomes the record of truth. Undoing four thousand silent field updates is not a small afternoon.

- **Validate before writing.** An enrichment miss should fail the step, not write an empty string over a good value. Ask what your chain does with a null before you find out at scale.

- **Log every call with its arguments and its result.** If you cannot answer what the agent wrote on Tuesday and why, you do not have an agent, you have an incident with a future date.

## The failure that actually happens

Not a malicious agent. A bad enrichment result written confidently into a field somebody else's report depends on, four thousand times, overnight, correctly according to every instruction it was given. The chain is [enrich a company from a domain](../jobs/enrich-company-from-domain.md) into [write crm records](../jobs/write-crm-records.md) and the weak link is the join between them, not either tool.

## The other risk in the same place

A CRM note is text a stranger may have written. If your agent reads notes and can also call tools, the note is an input channel. Keep destructive tools behind approval, and do not let a research loop and a write loop run unsupervised in the same session.

## What to check on the tool page before you start

The verbatim auth field, whether the vendor offers OAuth, and whether the credential can be scoped. 95 of the 167 servers here document an OAuth flow, which is the shape you want for anything that writes.

## Sources

- [The GTM MCP Directory, write CRM records](../jobs/write-crm-records.md) this site
- [Model Context Protocol, the specification](https://modelcontextprotocol.io/specification) https://modelcontextprotocol.io/specification
- [The GTM MCP Directory, servers by auth type](../lists/auth-types.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [How do I connect Claude to my CRM?](how-do-i-connect-claude-to-my-crm.md)
- [What are the security risks of connecting an AI agent to my GTM stack?](what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack.md)
- [Which CRM and RevOps tools have MCP servers?](which-crm-and-revops-tools-have-mcp-servers.md)
- [Which GTM MCP servers use OAuth instead of an API key?](which-gtm-mcp-servers-use-oauth.md)

## In the directory

- [Write CRM records](../jobs/write-crm-records.md)
- [Systems of record](../jobs/family-systems-of-record.md)
