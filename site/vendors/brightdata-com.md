# Bright Data: products, MCP servers and connect URLs, one vendor page

> Bright Data (brightdata.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 19 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Bright Data

# Bright Data

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [brightdata.com](https://brightdata.com) · vendor page id brightdata-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 1 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 19 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 982 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/brightdata](https://github.com/brightdata), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Bright Data](../tools/bright-data.md)

A general-purpose web-scraping/proxy infrastructure platform (residential proxies, browser automation, structured scraping APIs) that GTM engineers repurpose to pull LinkedIn, company-site, and directory data when off-the-shelf enrichment providers lack a...

[Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) (docs page)

- **Tools catalogued**: 19 named, harvested 2026-09-12, catalogue fixed

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 paid and self serve, API access by paying, no sales call.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)

1 distinct job label, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) (Bright Data, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Bright Data](../tools/bright-data.md) bdata official CLI

```
npm install -g @brightdata/cli
```

quoted from [https://www.npmjs.com/package/@brightdata/cli](https://www.npmjs.com/package/@brightdata/cli) on 2026-09-12, via npm

harvested 2026-09-12, all on the [tool page](../tools/bright-data.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/brightdata](https://github.com/brightdata) tied to the vendor by rule 1, account website https://brightdata.com has the vendor's domain, confidence strong

- **Public repositories**: 62, forks excluded, as read on 2026-09-08
- **Mention MCP**: 7 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [cli](https://github.com/brightdata/cli) | CLI | Official Bright Data CLI - scrape, search, and extract structured web data directly from your terminal. | 6,365 | 2026-09-07 | v0.3.5 |
| [skills](https://github.com/brightdata/skills) | other | | 257 | 2026-09-06 | |
| [answer-engines-country-codes](https://github.com/brightdata/answer-engines-country-codes) | other | Answer engine country codes | 3 | 2026-08-12 | |
| [sdk-python](https://github.com/brightdata/sdk-python) | SDK | Bright Data's python SDK, use it to call bright data's scrape and search tools. bypass any Bot-detection or Captcha and... | 91 | 2026-08-12 | v2.5.2 |
| [brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | MCP server | A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access. | 2,634 | 2026-08-12 | v2.11.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 982 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
