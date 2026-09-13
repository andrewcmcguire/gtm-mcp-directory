# Pipeworx: products, MCP servers and connect URLs, one vendor page

> Pipeworx (pipeworx.io): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Pipeworx

# Pipeworx

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [pipeworx.io](https://pipeworx.io) · vendor page id pipeworx-io

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 0 probed, no date

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 0 named across 1 measured server, harvested 2026-09-12. A further 5,993 sit behind a gateway server and are counted separately, because a gateway re-exposes other vendors

- **Bench tested**: 0 of 1 here, 1 of 514 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/pipeworx-io](https://github.com/pipeworx-io), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Pipeworx](../tools/pipeworx.md)

A single MCP gateway that fronts a stated 1,532 live data sources as 5,871 tools behind one URL, weighted toward public and regulatory data (SEC EDGAR, FDA, the Federal Reserve, ClinicalTrials, USPTO, EPA, EU procurement), with per-application wrapper paths...

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED

- **Endpoint probe**: not probed yet, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: 5993 named, harvested 2026-09-12, catalogue gateway, counted apart from the vendor total

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

### [Pipeworx](../tools/pipeworx.md) pipeworx official CLI

```
npx pipeworx@latest
```

quoted from [https://pipeworx.io/docs/getting-started/cli/](https://pipeworx.io/docs/getting-started/cli/) on 2026-09-12, via npx

Login or key hint: export PIPEWORX_API_KEY = your_key_here

1 subcommands seen, harvested 2026-09-12, all on the [tool page](../tools/pipeworx.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/pipeworx-io](https://github.com/pipeworx-io) tied to the vendor by rule 1, the directory already classed this repo first-party and its owner is an Organization, confidence strong

- **Public repositories**: 150, forks excluded, as read on 2026-09-08
- **Mention MCP**: 150 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [mcp-symmap](https://github.com/pipeworx-io/mcp-symmap) | MCP server | SymMap v2 - Traditional Chinese Medicine association graph from symmap.org | 0 | 2026-09-08 | |
| [mcp-tcm-products](https://github.com/pipeworx-io/mcp-tcm-products) | MCP server | Traditional Chinese Medicine (TCM) products licensed in Singapore - the HSA Chinese Proprietary Medicine listing... | 0 | 2026-09-08 | |
| [mcp-hk-companies](https://github.com/pipeworx-io/mcp-hk-companies) | MCP server | Hong Kong Companies Registry open data - company name/BR-number search, new registrations, and name changes via... | 0 | 2026-09-07 | |
| [mcp-china-safe](https://github.com/pipeworx-io/mcp-china-safe) | MCP server | China SAFE (State Administration of Foreign Exchange) - 国家外汇管理局 | 0 | 2026-09-07 | |
| [mcp-china-air-quality](https://github.com/pipeworx-io/mcp-china-air-quality) | MCP server | China Air Quality MCP - nationwide hourly AQI from CNEMC (中国环境监测总站). | 0 | 2026-09-07 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 514 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
