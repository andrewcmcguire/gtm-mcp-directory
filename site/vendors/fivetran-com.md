# Fivetran: products, MCP servers and connect URLs, one vendor page

> Fivetran (fivetran.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 2 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Fivetran

# Fivetran

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [fivetran.com](https://fivetran.com) · vendor page id fivetran-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 1 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 2 named across 1 measured server, harvested 2026-09-11

- **Bench tested**: 0 of 1 here, 1 of 374 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-11

- **GitHub organisation**: [github.com/fivetran](https://github.com/fivetran), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Fivetran](../tools/fivetran.md)

Managed ELT pipeline platform; for GTM purposes, the relevant piece is its Salesforce/HubSpot/Marketo/Outreach/Salesloft/Gong/Zendesk connectors that land CRM and GTM-tool data in a warehouse, plus (post-Census) its "Activations" reverse-ETL product for...

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) (docs page)

- **Tools catalogued**: 2 named, harvested 2026-09-11, catalogue fixed

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)

1 distinct job label, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) (Fivetran, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Fivetran](../tools/fivetran.md) fivetran-cli community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
pip install fivetran-cli
```

quoted from [https://pypi.org/project/fivetran-cli/](https://pypi.org/project/fivetran-cli/) on 2026-09-11, via pypi, a third party source

harvested 2026-09-11, all on the [tool page](../tools/fivetran.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/fivetran](https://github.com/fivetran) tied to the vendor by rule 1, account website https://fivetran.com has the vendor's domain, confidence strong

- **Public repositories**: 144, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [fivetran_sdk_tools](https://github.com/fivetran/fivetran_sdk_tools) | SDK | Local testing tools for Partner SDK and Connector SDK | 0 | 2026-09-08 | 2.26.0908.001 |
| [great_expectations](https://github.com/fivetran/great_expectations) | other | Always know what to expect from your data. | 11,776 | 2026-09-08 | 1.22.0 |
| [community_connectors](https://github.com/fivetran/community_connectors) | SDK | Fivetran Connector SDK Connectors Catalog | 85 | 2026-09-08 | |
| [connector_sdk](https://github.com/fivetran/connector_sdk) | SDK | Build custom connectors on Fivetran's platform | 133 | 2026-09-07 | |
| [dbt_openai](https://github.com/fivetran/dbt_openai) | other | | 0 | 2026-09-04 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 374 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
