# HubSpot: products, MCP servers and connect URLs, one vendor page

> HubSpot (hubspot.com): 3 products in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 25 tools catalogued. Data baked 2026-09-08.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
HubSpot

# HubSpot

3 products in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-08

Vendor domain: [hubspot.com](https://hubspot.com) · [Public company brief (HUBS)](https://andrewcmcguire.com/companies/hubspot/) · vendor page id hubspot-com

**The rollup**

- **Products**: 3, facts checked by hand 2026-08-24, 2026-09-02

- **Official MCP servers**: 1 of 3, as recorded on 2026-08-24, 2026-09-02

- **Community MCP servers**: 0 of 3

- **Live handshake**: 0 of 3 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 3: a server you install and run yourself

- **Docs only**: 0 of 3: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 25 named across 1 measured server, harvested 2026-09-08

- **Bench tested**: 0 of 3 here, 1 of 336 across the directory

- **Ships a CLI**: 3 of 3 official, 0 community only, 0 none found, harvested 2026-09-08

- **GitHub organisation**: [github.com/HubSpot](https://github.com/HubSpot), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 3**

### [HubSpot](../tools/hubspot.md)

An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: did not answer, 2026-09-04

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: 25 named, harvested 2026-09-08, catalogue fixed

- **last_checked**: 2026-08-24

### [HubSpot Breeze (AI Prospecting Agent)](../tools/hubspot-breeze.md)

Monitors accounts for buying signals (funding, leadership changes, site visits) via integrated data providers (ZoomInfo, Apollo, Surfe, Seamless), identifies decision-makers, and drafts personalized outreach emails in a rep's voice; can send with human review...

[No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED

- **Endpoint probe**: n/a, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-02

### [Clearbit (now HubSpot Breeze Intelligence)](../tools/clearbit.md)

A firmographic/contact data lookup service that fills in company and contact fields (size, industry, revenue, location, social profiles, etc.) from a third-party data pool; formerly sold as a standalone API, now sold only as an add-on inside the HubSpot CRM.

[No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: n/a, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-02

**The gates, in plain words**

1 of 3 free to start, a solo operator gets API access without talking to anyone. 1 of 3 paid and self serve, API access by paying, no sales call. 1 of 3 enterprise only, API access needs a contract.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)

11 distinct job labels, the union across 3 products, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

No product of this vendor records an MCP endpoint or docs URL that the probe could classify.

**Command line**

### [HubSpot](../tools/hubspot.md) hs official CLI

```
npm install -g @hubspot/cli
```

quoted from [https://www.npmjs.com/package/@hubspot/cli](https://www.npmjs.com/package/@hubspot/cli) on 2026-09-08, via npm

Login or key hint: hs init

harvested 2026-09-08, all on the [tool page](../tools/hubspot.md).

### [Clearbit (now HubSpot Breeze Intelligence)](../tools/clearbit.md) hubspot official CLI

```
npm install -g @hubspot/cli
```

quoted from [https://github.com/HubSpot/hubspot-cli](https://github.com/HubSpot/hubspot-cli) on 2026-09-08, via npm

Login or key hint: hs init

harvested 2026-09-08, all on the [tool page](../tools/clearbit.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/HubSpot](https://github.com/HubSpot) tied to the vendor by rule 3, account website http://product.hubspot.com/ has the vendor's domain, confidence strong

- **Public repositories**: 99, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 5 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [HubSpot-public-api-spec-collection](https://github.com/HubSpot/HubSpot-public-api-spec-collection) | API client | | 45 | 2026-09-08 | |
| [agent-cli-skills](https://github.com/HubSpot/agent-cli-skills) | CLI | | 23 | 2026-09-08 | |
| [hubspot-project-components](https://github.com/HubSpot/hubspot-project-components) | docs or examples | Provides sample components for HubSpot projects. | 25 | 2026-09-08 | 2.3.0 |
| [hubspot-cms-vscode](https://github.com/HubSpot/hubspot-cms-vscode) | plugin or integration | A HubL language extension for the Visual Studio Code IDE, allowing for :rocket: fast local HubSpot CMS Platform... | 75 | 2026-09-08 | v1.7.5 |
| [boomslang](https://github.com/HubSpot/boomslang) | other | Python, but Java | 6 | 2026-09-08 | build-cfcfca4ac2ca188e3acd2a3abe8bed21bc281917 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 3 products are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-08 by build_directory.py (phase 1).
