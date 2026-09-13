# Composio: products, MCP servers and connect URLs, one vendor page

> Composio (composio.dev): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 6 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Composio

# Composio

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [composio.dev](https://composio.dev) · vendor page id composio-dev

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 6 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 604 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/ComposioHQ](https://github.com/ComposioHQ), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Composio](../tools/composio.md)

A hosted integration/auth platform that lets AI agents and MCP clients call actions across 1,000+ SaaS apps (HubSpot, Slack, Gmail, GitHub, Notion, Stripe, and others) through Composio-managed OAuth.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://docs.composio.dev/docs/single-toolkit-mcp](https://docs.composio.dev/docs/single-toolkit-mcp) (docs page)

- **Tools catalogued**: 6 named, harvested 2026-09-12, catalogue dynamic, the server exposes the customer's own workspace

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

1 distinct job label, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://docs.composio.dev/docs/single-toolkit-mcp](https://docs.composio.dev/docs/single-toolkit-mcp) (Composio, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Composio](../tools/composio.md) composio official CLI

```
curl -fsSL https://composio.dev/install | bash
```

quoted from [https://composio.dev/cli](https://composio.dev/cli) on 2026-09-12, via shell

Login or key hint: composio login --agent

2 more install commands, 12 subcommands seen, harvested 2026-09-12, all on the [tool page](../tools/composio.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/ComposioHQ](https://github.com/ComposioHQ) tied to the vendor by rule 2, account website https://composio.dev has the vendor's domain, confidence strong

- **Public repositories**: 14, forks excluded, as read on 2026-09-08
- **Mention MCP**: 4 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [composio](https://github.com/ComposioHQ/composio) | MCP server | Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you... | 30,092 | 2026-09-08 | @composio/cli@0.4.2-beta.384 |
| [logo-cdn](https://github.com/ComposioHQ/logo-cdn) | other | oss logo cdn of composio toolkits | 7 | 2026-09-08 | |
| [helm-charts](https://github.com/ComposioHQ/helm-charts) | infrastructure | Helm charts to deploy Composio | 2 | 2026-09-07 | r20260908_01 |
| [composio-base-py](https://github.com/ComposioHQ/composio-base-py) | SDK | | 3 | 2026-08-19 | v1.44.0 |
| [composio-plugin-openai](https://github.com/ComposioHQ/composio-plugin-openai) | plugin or integration | | 4 | 2026-08-11 | v0.2.3 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 604 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
