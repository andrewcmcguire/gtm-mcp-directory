# What is an AI agent in sales? Definition, and what one can actually reach

> An AI agent in sales is a model given tools, a goal and permission to act across several steps. What separates an agent from a chatbot or a workflow, and which parts of the GTM stack one can currently call.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is an AI agent in sales?

**The short answer**

An AI agent in sales is a language model given a goal, a set of tools it can call, and permission to take several steps in a row without a human approving each one. The tools are what make it an agent: without them it is a chatbot that can only produce text.

Three things get called agents and only one of them is. A **chatbot** answers in text. A **workflow** runs a fixed sequence somebody drew in advance, and it does the same thing every time. An **agent** decides which tool to call next based on what the last call returned, which is useful precisely because the path was not decided in advance and risky for the same reason.

In sales the loop usually looks like this: read a trigger, research the account, find the right person, find a way to reach them, draft something specific, send it, write what happened back to the CRM. Seven steps, and every one of them is a call into a different vendor's system. The agent is the easy part. The seven doors are the hard part.

## Which doors are open

Across 293 tools, 182 are callable through MCP and 132 are reachable by one person without a contract. By job, the loop above currently looks like this:

| Step | Job | Tools tagged | Official MCP | Solo reachable |
|---|---|---|---|---|
| Research the account | [research an account before a call](../jobs/research-account-for-call-prep.md) | 17 | 10 | 8 |
| Find the person | [search people by criteria](../jobs/search-people-by-criteria.md) | 24 | 17 | 17 |
| Get a work email | [find a work email address](../jobs/find-work-email.md) | 29 | 22 | 22 |
| Check it is deliverable | [verify an email is deliverable](../jobs/verify-email-deliverable.md) | 15 | 12 | 14 |
| Draft the message | [draft personalized outreach](../jobs/draft-personalized-outreach.md) | 51 | 28 | 25 |
| Send the sequence | [run an email sequence](../jobs/run-email-sequence.md) | 45 | 26 | 23 |
| Write it back to the CRM | [write crm records](../jobs/write-crm-records.md) | 28 | 18 | 14 |

Counted 2026-09-04. Official MCP counts entries, and an entry can be cross listed in a second category, which is why these numbers are entry counts rather than product counts.

## The honest limit

Nobody has run these tools for this directory. 1 are bench tested. Every number above says a vendor documents a capability and a server was found, not that the chain works end to end when you wire it together at two in the morning.

## Sources

- [Model Context Protocol, official documentation](https://modelcontextprotocol.io) https://modelcontextprotocol.io
- [The GTM MCP Directory, by job](../jobs/index.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-04. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is an AI SDR?](what-is-an-ai-sdr.md)
- [What is an MCP server?](what-is-an-mcp-server.md)
- [How do I connect Claude to my CRM?](how-do-i-connect-claude-to-my-crm.md)
- [What are the security risks of connecting an AI agent to my GTM stack?](what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack.md)

## In the directory

- [Every job an agent asks for](../jobs/index.md)
