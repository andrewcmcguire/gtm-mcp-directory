# Tally: products, MCP servers and connect URLs, one vendor page

> Tally (tally.so): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Tally

# Tally

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [tally.so](https://tally.so) · vendor page id tally-so

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 0 probed, no date

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 514 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/tallyforms](https://github.com/tallyforms), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Tally](../tools/tally.md)

A free-first online form builder (unlimited forms and submissions on the free plan, conditional logic, payments, signatures, file uploads) with a REST API, webhooks and a hosted MCP server.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
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

### [Tally](../tools/tally.md) tally-cli community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
pip install tally-cli
```

quoted from [https://pypi.org/project/tally-cli/](https://pypi.org/project/tally-cli/) on 2026-09-12, via pypi, a third party source

harvested 2026-09-12, all on the [tool page](../tools/tally.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/tallyforms](https://github.com/tallyforms) tied to the vendor by rule 3, account website https://tally.so has the vendor's domain, confidence strong

- **Public repositories**: 2, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-05-11

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [n8n-nodes-tallyforms](https://github.com/tallyforms/n8n-nodes-tallyforms) | plugin or integration | n8n trigger for Tally form submissions | 6 | 2026-05-11 | v1.3.3 |
| [framer-plugin](https://github.com/tallyforms/framer-plugin) | plugin or integration | The Tally plugin for Framer makes it effortless to embed any published Tally form directly into your Framer projects. | 3 | 2025-12-12 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 514 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
