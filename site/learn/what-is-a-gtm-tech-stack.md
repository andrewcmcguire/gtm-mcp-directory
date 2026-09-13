# What is a GTM tech stack? The 15 layers, and how much of each an agent reaches

> A GTM tech stack is the set of systems a revenue team sells through. The 15 layers counted in this directory, with the share of each one an AI agent can currently call.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is a GTM tech stack?

**The short answer**

A GTM tech stack is every system a revenue team sells through, from the data that starts a conversation to the document that closes it. In this directory it is 15 layers and 784 tools, and the interesting question about a stack is no longer what is in it but how much of it anything can call.

Most stack diagrams are drawn by category because that is how software is sold. An agent does not experience it that way. It experiences a chain of doors, and the chain is only as good as its locked link.

## The layers, ordered by how reachable they are

| Layer | Tools | Official MCP | Community | Reachable |
|---|---|---|---|---|
| [MCP Layer](../categories/mcp-infrastructure.md) | 130 | 14 | 111 | 96% |
| [Data & Enrichment](../categories/data-enrichment.md) | 121 | 42 | 24 | 55% |
| [Video Prospecting](../categories/video-prospecting.md) | 19 | 4 | 6 | 53% |
| [Community & Dark Social](../categories/community-dark-social.md) | 21 | 8 | 3 | 52% |
| [RevOps Infra](../categories/revops-infra.md) | 73 | 29 | 8 | 51% |
| [Conversation Intel](../categories/conversation-intel.md) | 42 | 19 | 2 | 50% |
| [Scheduling & Routing](../categories/scheduling-routing.md) | 16 | 5 | 2 | 44% |
| [Proposals & Deals](../categories/proposals-deals.md) | 23 | 8 | 2 | 43% |
| [Signals & Intent](../categories/signals-intent-abm.md) | 61 | 20 | 5 | 41% |
| [Engagement & Outbound](../categories/engagement-outbound.md) | 105 | 23 | 10 | 31% |
| [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | 43 | 11 | 2 | 30% |
| [AI SDRs](../categories/ai-sdr-agents.md) | 44 | 8 | 4 | 27% |
| [Email Deliverability](../categories/email-deliverability.md) | 21 | 4 | 0 | 19% |
| [Forecasting & Revenue](../categories/forecasting-revenue.md) | 21 | 3 | 0 | 14% |
| [Enablement & Coaching](../categories/enablement-coaching.md) | 44 | 2 | 1 | 7% |

Counted 2026-09-12. Totals sum to 784 entries, which includes 16 products deliberately listed in two categories.

## What the ordering tells you

The top of that table is the infrastructure and data layers, where the API was always the product. The bottom is where the interface is the product: enablement, forecasting, community. The category sold hardest on autonomy, AI SDRs, sits well down it with 8 official servers out of 44.

If you are assembling a stack an agent can drive, build it from the top of that table down. The bottom is where you will still be writing glue, or clicking.

## The second filter

Reachable is not the same as available. 79 entries need a contract before anybody gets an API key. Cross those two columns before you plan anything: the list you actually get to build with is the 168 entries that have a server and are free to start or paid self serve.

## Sources

- [The GTM MCP Directory, by category](../categories/index.md) this site
- [The GTM MCP Directory, the counted data](../data.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-12. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)
- [What is a GTM engineer?](what-is-a-gtm-engineer.md)
- [How do I audit my GTM stack for agent readiness?](how-do-i-audit-my-gtm-stack-for-agent-readiness.md)
- [What is an API access gate and why does it matter for AI agents?](what-is-an-api-access-gate.md)

## In the directory

- [Every category](../categories/index.md)
- [The lists](../lists/index.md)
