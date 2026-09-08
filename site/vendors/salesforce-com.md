# Salesforce: products, MCP servers and connect URLs, one vendor page

> Salesforce (salesforce.com): 2 products in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 17 tools catalogued. Data baked 2026-09-08.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Salesforce

# Salesforce

2 products in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-08

Vendor domain: [salesforce.com](https://salesforce.com) · [Public company brief (CRM)](https://andrewcmcguire.com/companies/salesforce/) · vendor page id salesforce-com

**The rollup**

- **Products**: 2, facts checked by hand 2026-08-24, 2026-09-02

- **Official MCP servers**: 1 of 2, as recorded on 2026-08-24, 2026-09-02

- **Community MCP servers**: 0 of 2

- **Live handshake**: 0 of 2 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 1 of 2: a server you install and run yourself

- **Docs only**: 0 of 2: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 17 named across 1 measured server, harvested 2026-09-08

- **Bench tested**: 0 of 2 here, 1 of 336 across the directory

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 2**

### [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md)

A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code app layer, with Agentforce as a layer on top for configuring autonomous AI agents that read Salesforce data, decide on an action, and execute it or...

[Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) (docs page)

- **Tools catalogued**: 17 named, harvested 2026-09-08, catalogue fixed

- **last_checked**: 2026-08-24

### [Salesforce Einstein Forecasting](../tools/salesforce-einstein-forecasting.md)

Sales Cloud's AI forecasting feature, analyzing past opportunities, account history, and activities plus rep win-rates to generate revenue predictions with confidence ranges. See 06-revops-infra.md for Salesforce's full platform entry (Agentforce, Hosted MCP...

[No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)
[Forecasting & Revenue](../categories/forecasting-revenue.md)
RESEARCHED

- **Endpoint probe**: n/a, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-02

**The gates, in plain words**

2 of 2 enterprise only, API access needs a contract.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

6 distinct job labels, the union across 2 products, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) (Salesforce (core CRM/platform) + Agentforce, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 2 products are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-08 by build_directory.py (phase 1).
