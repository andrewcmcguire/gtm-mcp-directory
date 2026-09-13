# Wistia: products, MCP servers and connect URLs, one vendor page

> Wistia (wistia.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Wistia

# Wistia

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [wistia.com](https://wistia.com) · vendor page id wistia-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 0 probed, no date

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 1,251 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/wistia](https://github.com/wistia), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Wistia](../tools/wistia.md)

A video hosting and marketing platform for business (player, channels, webinars, analytics, lead capture) with a REST API; sales and marketing teams use it for hosted demo and follow-up video with per-viewer engagement data.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Video Prospecting](../categories/video-prospecting.md)
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

### [Wistia](../tools/wistia.md) wistia official CLI

```
npm install -g @wistia/wistia-cli
```

quoted from [https://www.npmjs.com/package/@wistia/wistia-cli](https://www.npmjs.com/package/@wistia/wistia-cli) on 2026-09-12, via npm

harvested 2026-09-12, all on the [tool page](../tools/wistia.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/wistia](https://github.com/wistia) tied to the vendor by rule 3, account website https://wistia.com has the vendor's domain, confidence strong

- **Public repositories**: 58, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 3 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [wistia-typescript-sdk](https://github.com/wistia/wistia-typescript-sdk) | SDK | | 0 | 2026-09-08 | v2026.7.0 |
| [digestabot-demo](https://github.com/wistia/digestabot-demo) | docs or examples | Demonstration repo for https://github.com/chainguard-dev/digestabot/pull/74 | 0 | 2026-09-08 | |
| [homebrew-tap](https://github.com/wistia/homebrew-tap) | infrastructure | Homebrew Tap for Wistia Desktop | 0 | 2026-09-04 | |
| [json-mask-ruby](https://github.com/wistia/json-mask-ruby) | SDK | Google partial-response / JSON Mask field selectors for Ruby: filter JSON-compatible Hashes and Arrays without changing... | 0 | 2026-09-04 | |
| [elixir_nsq](https://github.com/wistia/elixir_nsq) | other | An NSQ client for Elixir and Erlang, written in Elixir. | 92 | 2026-09-04 | 1.2.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 1,251 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
