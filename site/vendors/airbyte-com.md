# Airbyte: products, MCP servers and connect URLs, one vendor page

> Airbyte (airbyte.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 4 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Airbyte

# Airbyte

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [airbyte.com](https://airbyte.com) · vendor page id airbyte-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 4 named across 1 measured server, harvested 2026-09-11

- **Bench tested**: 0 of 1 here, 1 of 374 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-11

- **GitHub organisation**: none tied to airbyte.com with evidence on 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Airbyte](../tools/airbyte.md)

Open-source/cloud ELT platform with 600+ connectors moving data from SaaS tools and databases into warehouses; increasingly positions itself as a context layer for AI agents via a hosted Context Store.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://docs.airbyte.com/ai-agents/interfaces/mcp](https://docs.airbyte.com/ai-agents/interfaces/mcp) (docs page)

- **Tools catalogued**: 4 named, harvested 2026-09-11, catalogue fixed

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)

1 distinct job label, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://docs.airbyte.com/ai-agents/interfaces/mcp](https://docs.airbyte.com/ai-agents/interfaces/mcp) (Airbyte, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Airbyte](../tools/airbyte.md) airbyte-config community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
npm install -g airbyte-config-cli
```

quoted from [https://www.npmjs.com/package/airbyte-config-cli](https://www.npmjs.com/package/airbyte-config-cli) on 2026-09-11, via npm, a third party source

harvested 2026-09-11, all on the [tool page](../tools/airbyte.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

No GitHub organisation could be tied to airbyte.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: airbyte, airbytehq, AirbyteTeam, airbytez, Airbyte-Solutions-Team. A name match alone is never accepted; the account has to point at the vendor domain.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 374 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
