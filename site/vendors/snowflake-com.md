# Snowflake (Cortex AI, as GTM/RevOps warehouse layer): products, MCP servers and connect URLs, one vendor page

> Snowflake (Cortex AI, as GTM/RevOps warehouse layer) (snowflake.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 24 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Snowflake (Cortex AI, as GTM/RevOps warehouse layer)

# Snowflake (Cortex AI, as GTM/RevOps warehouse layer)

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [snowflake.com](https://snowflake.com) · [Public company brief (SNOW)](https://andrewcmcguire.com/companies/snowflake/) · vendor page id snowflake-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 24 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 884 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/Snowflake-Labs](https://github.com/Snowflake-Labs), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md)

Cloud data warehouse that acts as the central store where GTM data (CRM, product usage, marketing, support) gets modeled and joined; increasingly the platform other reverse-ETL tools (Hightouch, Fivetran Activations) and app tools (Retool, Superblocks) sit on...

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) (docs page)

- **Tools catalogued**: 24 named, harvested 2026-09-12, catalogue dynamic, the server exposes the customer's own workspace

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Query a data warehouse](../jobs/query-data-warehouse.md)

1 distinct job label, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) (Snowflake (Cortex AI, as GTM/RevOps warehouse layer), docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md) snowflake-cli official CLI

```
brew install snowflake-cli
```

quoted from [https://formulae.brew.sh/formula/snowflake-cli](https://formulae.brew.sh/formula/snowflake-cli) on 2026-09-12, via brew

harvested 2026-09-12, all on the [tool page](../tools/snowflake.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/Snowflake-Labs](https://github.com/Snowflake-Labs) tied to the vendor by rule 1, account website https://developers.snowflake.com/ has the vendor's domain, confidence strong

- **Public repositories**: 125, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 4 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [sfquickstarts](https://github.com/Snowflake-Labs/sfquickstarts) | other | Follow along with our tutorials to get you up and running with Snowflake. | 17 | 2026-09-08 | |
| [pg_lake](https://github.com/Snowflake-Labs/pg_lake) | other | pg_lake: Postgres with Iceberg and data lake access | 1,637 | 2026-09-08 | v3.5.0 |
| [coco-skills](https://github.com/Snowflake-Labs/coco-skills) | CLI | This is a curated collection of Agent Skills for Cortex Code ("CoCo") - Snowflake's CLI for building with AI. | 29 | 2026-09-08 | |
| [swt-tokyo-2026-coco](https://github.com/Snowflake-Labs/swt-tokyo-2026-coco) | other | | 0 | 2026-09-08 | |
| [sfguide-create-a-route-optimisation-and-vehicle-route-plan-simulator](https://github.com/Snowflake-Labs/sfguide-create-a-route-optimisation-and-vehicle-route-plan-simulator) | other | | 12 | 2026-09-08 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 884 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
