# PredictLeads: products, MCP servers and connect URLs, one vendor page

> PredictLeads (predictleads.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 1 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
PredictLeads

# PredictLeads

1 product in the directory
1 official MCP server
1 live handshake
Data baked 2026-09-12

Vendor domain: [predictleads.com](https://predictleads.com) · vendor page id predictleads-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 0 of 1

- **Live handshake**: 1 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 374 across the directory

- **Ships a CLI**: 0 of 1 official, 0 community only, 1 none found, harvested 2026-09-11

- **GitHub organisation**: [github.com/PredictLeads](https://github.com/PredictLeads), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [PredictLeads](../tools/predictleads.md)

Aggregates five signal categories (job openings, technology detections, news events, business connections, firmographics) across 129M companies in 195 countries by scraping public web sources - company sites, job boards, DNS/HTML/JS technology footprints,...

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED

- **Endpoint probe**: answered, asking for a key, 2026-09-04

- **Connect URL**: [https://mcp.predictleads.com/](https://mcp.predictleads.com/) (endpoint)

- **Tools catalogued**: not measured

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Scrape job postings](../jobs/scrape-job-postings.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)

4 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://mcp.predictleads.com/](https://mcp.predictleads.com/) (PredictLeads, endpoint, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

No CLI found for any product of this vendor by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**On GitHub**

[github.com/PredictLeads](https://github.com/PredictLeads) tied to the vendor by rule 3, account website https://predictleads.com has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2025-11-26

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [n8n-nodes-predict-leads](https://github.com/PredictLeads/n8n-nodes-predict-leads) | plugin or integration | This is an n8n node that let's you use PredictLeads data in your workflow | 1 | 2025-11-26 | 1.0.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 374 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
