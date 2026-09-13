# Browserbase: products, MCP servers and connect URLs, one vendor page

> Browserbase (browserbase.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 6 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Browserbase

# Browserbase

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [browserbase.com](https://browserbase.com) · vendor page id browserbase-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 0 probed, no date

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 6 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 982 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/browserbase](https://github.com/browserbase), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Browserbase](../tools/browserbase.md)

A hosted headless-browser service (sessions, proxies, stealth, session recording) with Stagehand, its natural-language browser automation layer, so agents can navigate, act on and extract from web pages that plain HTTP fetching cannot reach.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: not probed yet, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: 6 named, harvested 2026-09-12, catalogue fixed

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

### [Browserbase](../tools/browserbase.md) bb9 official CLI

```
npm install -g browse
```

quoted from [https://docs.browserbase.com/integrations/skills/browse-cli](https://docs.browserbase.com/integrations/skills/browse-cli) on 2026-09-12, via npm

Login or key hint: export BROWSERBASE_API_KEY = "your_api_key"

1 more install command, 13 subcommands seen, harvested 2026-09-12, all on the [tool page](../tools/browserbase.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/browserbase](https://github.com/browserbase) tied to the vendor by rule 3, account website https://www.browserbase.com has the vendor's domain, confidence strong

- **Public repositories**: 60, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [stagehand](https://github.com/browserbase/stagehand) | SDK | The SDK For Browser Agents | 24,174 | 2026-09-08 | stagehand-server-v3/v3.7.6 |
| [sdk-python](https://github.com/browserbase/sdk-python) | SDK | Python SDK for Browserbase | 92 | 2026-09-03 | v1.18.1 |
| [sdk-node](https://github.com/browserbase/sdk-node) | SDK | Node.js SDK for Browserbase | 64 | 2026-09-03 | v2.19.1 |
| [skills](https://github.com/browserbase/skills) | other | Browserbase's official collection of agent skills to access the web. | 3,715 | 2026-09-02 | |
| [sdk-functions-node](https://github.com/browserbase/sdk-functions-node) | SDK | The Browserbase Functions SDK lets you define, develop, and deploy serverless browser automation functions on... | 4 | 2026-08-28 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 982 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
