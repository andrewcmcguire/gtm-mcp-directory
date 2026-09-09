# Exa: products, MCP servers and connect URLs, one vendor page

> Exa (exa.ai): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 11 tools catalogued. Data baked 2026-09-09.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Exa

# Exa

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-09

Vendor domain: [exa.ai](https://exa.ai) · vendor page id exa-ai

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-03

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-03

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 1 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 11 named across 1 measured server, harvested 2026-09-09

- **Bench tested**: 1 of 1 here, 1 of 336 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-09

- **GitHub organisation**: [github.com/exa-labs](https://github.com/exa-labs), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Exa](../tools/exa.md)

A search API that returns web pages and structured results ranked by semantic/meaning similarity to a query (embeddings-based) rather than keyword matching, plus tools to fetch page contents and get LLM-generated answers with citations; used in GTM stacks...

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
BENCH-TESTED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) (docs page)

- **Tools catalogued**: 11 named, harvested 2026-09-09, catalogue fixed

- **last_checked**: 2026-09-03

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)

2 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) (Exa, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Exa](../tools/exa.md) exa-cli community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
pip install exa-cli
```

quoted from [https://pypi.org/project/exa-cli/](https://pypi.org/project/exa-cli/) on 2026-09-09, via pypi, a third party source

harvested 2026-09-09, all on the [tool page](../tools/exa.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/exa-labs](https://github.com/exa-labs) tied to the vendor by rule 1, account website https://exa.ai has the vendor's domain, confidence strong

- **Public repositories**: 50, forks excluded, as read on 2026-09-08
- **Mention MCP**: 3 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [agent-skills](https://github.com/exa-labs/agent-skills) | other | Official skills for the Exa API. | 46 | 2026-09-03 | |
| [exa-js](https://github.com/exa-labs/exa-js) | SDK | The Official Exa Javascript SDK | 130 | 2026-09-03 | v2.20.0 |
| [exa-py](https://github.com/exa-labs/exa-py) | SDK | The Official Exa Python Package | 233 | 2026-09-03 | v2.20.0 |
| [exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) | MCP server | Exa MCP for web search and web crawling! | 4,987 | 2026-08-21 | |
| [company-researcher](https://github.com/exa-labs/company-researcher) | other | Company Researcher tool helps you instantly understand any company inside out. | 1,494 | 2026-08-08 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 1 of this vendor's 1 product is among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-09 by build_directory.py (phase 1).
