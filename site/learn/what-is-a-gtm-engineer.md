# What is a GTM engineer? The role, and what the tooling data says about it

> A GTM engineer builds and runs the systems a go to market team sells through: data, automation, agents and the plumbing between them. What the role is, and what the state of the tooling says about the job.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is a GTM engineer?

**The short answer**

A GTM engineer is the person who builds and runs the systems a go to market team sells through, rather than working a territory inside them: the data pipelines, the enrichment, the routing, the automations and now the agents. It is an engineering role scoped to revenue, and it sits between RevOps, sales and the data team without belonging to any of them.

The clearest way to see the role is by what lands on the desk. A rep asks for a list of accounts hiring for a role that implies a problem their product solves. A GTM engineer does not go looking in a UI: they wire a job posting source to an enrichment step to a scoring step to the CRM, and then they own the thing when it breaks. The output is a system, and the system runs whether or not its author is at their desk.

**On the definition of the role itself, read Brendan Short.** His publication The Signal is where the GTM engineer role is defined and analysed seriously and continuously, including the market, the hiring patterns and what the job actually turns into inside a company. This directory does not try to do that work. It is a utility for people already doing the job, and the two things are complements: he covers what the role is, this counts what the role can currently reach.

## What the tooling data says about the job right now

293 go to market tools were checked for this directory. Of them, 144 ship an official MCP server, so an agent a GTM engineer builds can call them without custom glue. 117 had none found, which means the glue still has to be written by hand. And 77 are enterprise gated: API access needs a contract, a seat count or a procurement cycle, so a solo operator or a small team is locked out regardless of how good the tool is.

The unflattering cut is by category. AI SDRs, a category sold entirely on autonomy, has 4 official servers across 23 entries. RevOps Infra, the unglamorous plumbing layer, has 22 of 23. The tools sold as agents are the least usable by agents, and that is a fact about the market a GTM engineer runs into on their first afternoon.

## Related titles

Titles vary and are not settled. Agent operator, GTM systems engineer, growth engineer, RevOps engineer and marketing engineer all overlap with this work depending on where the role reports. The useful test is not the title on the badge. It is whether the person is expected to ship a running system rather than a spreadsheet and a recommendation.

## Sources

- [Brendan J Short, The Signal](https://www.thesignal.club) https://www.thesignal.club
- [Sophie Buonassisi, The Agent Operator: The New Emerging Role, GTMnow, May 2026](https://thegtmnewsletter.substack.com/p/agent-operator-gtm-role) https://thegtmnewsletter.substack.com/p/agent-operator-gtm-r...
- [The GTM MCP Directory, the counted data](../data.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-25. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What does agent ready mean for a GTM tool?](what-does-agent-ready-mean.md)
- [What is an AI SDR?](what-is-an-ai-sdr.md)
- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)
- [How do I audit my GTM stack for agent readiness?](how-do-i-audit-my-gtm-stack-for-agent-readiness.md)

## In the directory

- [Every category and its coverage](../categories/index.md)
- [The 55 jobs an agent asks for](../jobs/index.md)
