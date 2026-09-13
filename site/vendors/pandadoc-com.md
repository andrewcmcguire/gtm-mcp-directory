# PandaDoc: products, MCP servers and connect URLs, one vendor page

> PandaDoc (pandadoc.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
PandaDoc

# PandaDoc

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [pandadoc.com](https://pandadoc.com) · vendor page id pandadoc-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 934 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/PandaDoc](https://github.com/PandaDoc), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [PandaDoc](../tools/pandadoc.md)

Document builder/e-signature platform for proposals, quotes, and contracts, with AI-assisted content generation and CRM-linked workflows.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server) (docs page)

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Generate a proposal or quote](../jobs/generate-proposal-or-quote.md)
- [Send a document for signature](../jobs/send-document-for-signature.md)

2 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server) (PandaDoc, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [PandaDoc](../tools/pandadoc.md) pandadoc community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
pip install pandadoc
```

quoted from [https://pypi.org/project/pandadoc/](https://pypi.org/project/pandadoc/) on 2026-09-12, via pypi, a third party source

harvested 2026-09-12, all on the [tool page](../tools/pandadoc.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/PandaDoc](https://github.com/PandaDoc) tied to the vendor by rule 2, account website https://pandadoc.com has the vendor's domain, confidence strong

- **Public repositories**: 16, forks excluded, as read on 2026-09-08
- **Mention MCP**: 3 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [pandadoc-openapi-specification](https://github.com/PandaDoc/pandadoc-openapi-specification) | API client | | 6 | 2026-09-08 | v7.27.1 |
| [design-engineer-interview-200826-dry-run](https://github.com/PandaDoc/design-engineer-interview-200826-dry-run) | other | | 0 | 2026-08-20 | |
| [mcp-server-guide](https://github.com/PandaDoc/mcp-server-guide) | MCP server | Where to start to use PandaDoc MCP server | 2 | 2026-08-20 | v1.0.0 |
| [design-engineer-interview-170826](https://github.com/PandaDoc/design-engineer-interview-170826) | other | | 0 | 2026-08-17 | |
| [property-agreement-templates](https://github.com/PandaDoc/property-agreement-templates) | docs or examples | Free property and real estate agreement templates - residential and commercial leases, rental agreements,... | 0 | 2026-07-22 | v1.0.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 934 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
