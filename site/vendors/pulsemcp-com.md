# PulseMCP: products, MCP servers and connect URLs, one vendor page

> PulseMCP (pulsemcp.com): 1 product in The GTM MCP Directory, 0 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
PulseMCP

# PulseMCP

1 product in the directory
0 official MCP servers
0 live handshakes
Data baked 2026-09-12

Vendor domain: [pulsemcp.com](https://pulsemcp.com) · vendor page id pulsemcp-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 0 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 0 probed, no date

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 1,251 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/pulsemcp](https://github.com/pulsemcp), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [PulseMCP](../tools/pulsemcp.md)

A community-run browsable directory and news hub for the MCP ecosystem (servers, clients, use cases, and a newsletter called "The Agentic Loop") that links out to third-party servers rather than hosting them.

[MCP not applicable](../mcp/n-a.md) · [Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED

- **Endpoint probe**: n/a, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: not measured

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Discover MCP servers](../jobs/discover-mcp-servers.md)

1 distinct job label, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

No product of this vendor records an MCP endpoint or docs URL that the probe could classify.

**Command line**

### [PulseMCP](../tools/pulsemcp.md) air official CLI

```
npm install -g @pulsemcp/air-cli
```

quoted from [https://www.npmjs.com/package/@pulsemcp/air-cli](https://www.npmjs.com/package/@pulsemcp/air-cli) on 2026-09-12, via npm

harvested 2026-09-12, all on the [tool page](../tools/pulsemcp.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/pulsemcp](https://github.com/pulsemcp) tied to the vendor by rule 3, account website pulsemcp.com has the vendor's domain, confidence strong

- **Public repositories**: 7, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-06

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [air](https://github.com/pulsemcp/air) | other | A lightweight, open source framework that enables org/team collaboration on open standard-powered AI-related artifacts... | 3 | 2026-09-06 | |
| [mcp-servers](https://github.com/pulsemcp/mcp-servers) | MCP server | MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers... | 80 | 2026-08-30 | gmail-workspace-mcp-server@0.4.12 |
| [linear-mcp-client-bridge](https://github.com/pulsemcp/linear-mcp-client-bridge) | MCP server | An example for how we can de-facto inject a highly capable agent and MCP client into just about any software service. | 0 | 2026-06-24 | |
| [switchboard](https://github.com/pulsemcp/switchboard) | other | Free, self-hostable OSS that saves agent transcripts from Claude Code, Codex, and other coding agents for retroactive... | 2 | 2026-06-13 | |
| [ai-artifacts](https://github.com/pulsemcp/ai-artifacts) | other | Skills, Hooks, and other artifacts developed by the PulseMCP team that may be useful to others. | 2 | 2026-06-04 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 1,251 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
