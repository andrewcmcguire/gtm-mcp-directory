# Crustdata: products, MCP servers and connect URLs, one vendor page

> Crustdata (crustdata.com): 2 products in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 3 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Crustdata

# Crustdata

2 products in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [crustdata.com](https://crustdata.com) · vendor page id crustdata-com

**The rollup**

- **Products**: 2, facts checked by hand 2026-09-07, 2026-09-12

- **Official MCP servers**: 1 of 2, as recorded on 2026-09-07, 2026-09-12

- **Community MCP servers**: 1 of 2

- **Live handshake**: 0 of 2 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 2: a server you install and run yourself

- **Docs only**: 1 of 2: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 3 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 2 here, 1 of 1,032 across the directory

- **Ships a CLI**: 0 of 2 official, 0 community only, 1 none found, harvested 2026-09-12

- **GitHub organisation**: none tied to crustdata.com with evidence on 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 2**

### [Crustdata](../tools/crustdata.md)

A real-time API for company and person firmographic/growth data (headcount trends, funding, tech stack, web traffic, social signals), positioned as infrastructure for time-sensitive GTM triggers and agent-built prospecting workflows.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://crustdata.com/](https://crustdata.com/) (docs page)

- **Tools catalogued**: 3 named, harvested 2026-09-12, catalogue fixed

- **last_checked**: 2026-09-07

### [Crustdata MCP](../tools/crustdata-mcp.md)

Crustdata provides real-time B2B data API for AI agents with 1B+ people and 60M+ companies to power sales, recruiting, and investment workflows.

[Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: not probed yet, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-12

**The gates, in plain words**

1 of 2 free to start, a solo operator gets API access without talking to anyone. 1 of 2 gate unknown, not established from public sources and published as unknown.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)

6 distinct job labels, the union across 2 products, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://crustdata.com/](https://crustdata.com/) (Crustdata, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

No CLI found for any product of this vendor by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**On GitHub**

No GitHub organisation could be tied to crustdata.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

1 candidate account seen and rejected by the evidence rules: crustdata. A name match alone is never accepted; the account has to point at the vendor domain.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 1,032 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 2 products are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
