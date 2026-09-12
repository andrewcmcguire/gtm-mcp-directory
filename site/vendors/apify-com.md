# Apify: products, MCP servers and connect URLs, one vendor page

> Apify (apify.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Apify

# Apify

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [apify.com](https://apify.com) · vendor page id apify-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 0 probed, no date

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 336 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/apify](https://github.com/apify), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Apify](../tools/apify.md)

A cloud platform for running "Actors" (hosted scrapers and automation programs, thousands of them in a public store) that extract web data such as LinkedIn posts, Google Maps listings, company sites and social feeds into datasets, with an API, scheduling and...

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: not probed yet, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

No job tag on any product of this vendor.

An empty list means nobody has tagged these entries, not that the tools do nothing.

**Connect URLs**

No product of this vendor records an MCP endpoint or docs URL that the probe could classify.

**Command line**

### [Apify](../tools/apify.md) actor official CLI

```
npm install -g apify-cli
```

quoted from [https://www.npmjs.com/package/apify-cli](https://www.npmjs.com/package/apify-cli) on 2026-09-12, via npm

1 more install command, harvested 2026-09-12, all on the [tool page](../tools/apify.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/apify](https://github.com/apify) tied to the vendor by rule 3, account website https://apify.com/ has the vendor's domain, confidence strong

- **Public repositories**: 122, forks excluded, as read on 2026-09-08
- **Mention MCP**: 12 of them
- **Look like CLIs**: 3 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [agent-skills](https://github.com/apify/agent-skills) | other | Collection of Apify agent skills | 2,371 | 2026-09-08 | |
| [apify-evals](https://github.com/apify/apify-evals) | other | | 0 | 2026-09-08 | |
| [cgroups-sensor](https://github.com/apify/cgroups-sensor) | other | Utility functions to measure resource limits from cgroups in scenarios where psutils is not sufficient. | 0 | 2026-09-08 | |
| [actor-templates](https://github.com/apify/actor-templates) | docs or examples | This project is the :house: home of Apify Actor templates to help users quickly get started. Contributions welcome! | 60 | 2026-09-08 | |
| [apify-mcp-server](https://github.com/apify/apify-mcp-server) | MCP server | The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites,... | 6,380 | 2026-09-08 | v0.15.4 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
