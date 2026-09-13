# monday.com (monday CRM): products, MCP servers and connect URLs, one vendor page

> monday.com (monday CRM) (monday.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 5 tools catalogued. Data baked 2026-09-13.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
monday.com (monday CRM)

# monday.com (monday CRM)

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-13

Vendor domain: [monday.com](https://monday.com) · [Public company brief (MNDY)](https://andrewcmcguire.com/companies/monday-com/) · vendor page id monday-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 0 probed, no date

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 5 named across 1 measured server, harvested 2026-09-13

- **Bench tested**: 0 of 1 here, 1 of 336 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-13

- **GitHub organisation**: [github.com/mondaycom](https://github.com/mondaycom), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [monday.com (monday CRM)](../tools/monday-com.md)

A work-management platform whose CRM product runs pipelines, contacts, accounts and deal activity as boards and items, with a first-party remote MCP server that lets an AI client read and update that data on the user's behalf.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: not probed yet, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: 5 named, harvested 2026-09-13, catalogue fixed

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

### [monday.com (monday CRM)](../tools/monday-com.md) mapps official CLI

```
npm install -g @mondaycom/apps-cli
```

quoted from [https://www.npmjs.com/package/@mondaycom/apps-cli](https://www.npmjs.com/package/@mondaycom/apps-cli) on 2026-09-13, via npm

harvested 2026-09-13, all on the [tool page](../tools/monday-com.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/mondaycom](https://github.com/mondaycom) tied to the vendor by rule 1, account website https://monday.com has the vendor's domain, confidence strong

- **Public repositories**: 40, forks excluded, as read on 2026-09-08
- **Mention MCP**: 5 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [vibe](https://github.com/mondaycom/vibe) | MCP server | 🎨 Vibe Design System - Official monday.com UI resources for application development in React.js | 675 | 2026-09-08 | @vibe/wizard@4.0.4 |
| [mcli](https://github.com/mondaycom/mcli) | CLI | Monday CLI | 1 | 2026-09-08 | v0.8.0 |
| [mcp](https://github.com/mondaycom/mcp) | MCP server | Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context... | 423 | 2026-09-07 | |
| [n8n-nodes-monday-models](https://github.com/mondaycom/n8n-nodes-monday-models) | plugin or integration | n8n community node for monday.com Models API - use monday-hosted AI chat models in Agents and Chains | 0 | 2026-08-11 | |
| [monday-sdk-js](https://github.com/mondaycom/monday-sdk-js) | SDK | Node.js and JavaScript SDK for developing over the monday.com platform | 102 | 2026-08-10 | 0.5.9 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-13 by build_directory.py (phase 1).
