# Clari: products, MCP servers and connect URLs, one vendor page

> Clari (clari.com): 2 products in The GTM MCP Directory, 2 with an official MCP server, 0 answering a live handshake, 5 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Clari

# Clari

2 products in the directory
2 official MCP servers
0 live handshakes
Data baked 2026-09-12

Vendor domain: [clari.com](https://clari.com) · vendor page id clari-com

**The rollup**

- **Products**: 2, facts checked by hand 2026-09-07

- **Official MCP servers**: 2 of 2, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 2

- **Live handshake**: 0 of 2 answered an MCP initialize, 2 probed, 2026-09-04

- **Repo local**: 0 of 2: a server you install and run yourself

- **Docs only**: 2 of 2: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 5 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 2 here, 1 of 739 across the directory

- **Ships a CLI**: 0 of 2 official, 0 community only, 2 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/clari](https://github.com/clari), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 2**

### [Clari Copilot](../tools/clari-copilot.md)

Records and transcribes sales calls in real time and surfaces live coaching prompts, deal-risk flags, and auto-generated CRM updates during and after the call.

[Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://www.scalekit.com/connectors/claricopilot](https://www.scalekit.com/connectors/claricopilot) (docs page)

- **Tools catalogued**: 5 named, harvested 2026-09-12, catalogue fixed

- **last_checked**: 2026-09-07

### [Clari](../tools/clari.md)

Revenue operations platform that aggregates CRM, activity, and conversation data into pipeline inspection, forecasting, and deal-execution workflows.

[Official MCP](../mcp/official.md) · [Enterprise leaning](../gates/enterprise-leaning.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/](https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/) (docs page)

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 2 paid and self serve, API access by paying, no sales call. 1 of 2 enterprise leaning, self serve on paper and gated in practice.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

6 distinct job labels, the union across 2 products, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://www.scalekit.com/connectors/claricopilot](https://www.scalekit.com/connectors/claricopilot) (Clari Copilot, docs page, probed 2026-09-04)
- [https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/](https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/) (Clari, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

No CLI found for any product of this vendor by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**On GitHub**

[github.com/clari](https://github.com/clari) tied to the vendor by rule 3, account website http://www.clari.com has the vendor's domain, confidence strong

- **Public repositories**: 3, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2023-01-24

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [react-ios-switch](https://github.com/clari/react-ios-switch) | other | React switch component https://clari.github.io/react-ios-switch | 129 | 2023-01-24 | |
| [SFDCLeadConversion](https://github.com/clari/SFDCLeadConversion) | other | SFDC Custom package for exposing leadConversion using custom RestApi | 0 | 2019-08-26 | |
| [clari_dynamo](https://github.com/clari/clari_dynamo) | other | Customizable service layer around DynamoDB | 1 | 2015-07-27 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 739 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 2 products are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
