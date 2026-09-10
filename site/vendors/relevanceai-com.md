# Relevance AI: products, MCP servers and connect URLs, one vendor page

> Relevance AI (relevanceai.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-10.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Relevance AI

# Relevance AI

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-10

Vendor domain: [relevanceai.com](https://relevanceai.com) · vendor page id relevanceai-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 336 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-10

- **GitHub organisation**: [github.com/RelevanceAI](https://github.com/RelevanceAI), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Relevance AI](../tools/relevance-ai.md)

A platform for building and deploying specialist AI agents (research/enrichment, outbound prospecting, meeting scheduling, deal review, proposal building) that teams configure and progress toward autonomous ("L3 Autopilot") operation.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins](https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins) (docs page)

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

No job tag on any product of this vendor.

An empty list means nobody has tagged these entries, not that the tools do nothing.

**Connect URLs**

- [https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins](https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins) (Relevance AI, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Relevance AI](../tools/relevance-ai.md) relevanceai official CLI

```
pip install relevanceai
```

quoted from [https://pypi.org/project/relevanceai/](https://pypi.org/project/relevanceai/) on 2026-09-10, via pypi

harvested 2026-09-10, all on the [tool page](../tools/relevance-ai.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/RelevanceAI](https://github.com/RelevanceAI) tied to the vendor by rule 3, account website https://relevanceai.com has the vendor's domain, confidence strong

- **Public repositories**: 39, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 3 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [relevance-docs](https://github.com/RelevanceAI/relevance-docs) | docs or examples | | 3 | 2026-09-08 | |
| [content-cdn](https://github.com/RelevanceAI/content-cdn) | other | | 2 | 2026-09-08 | |
| [arg-releases](https://github.com/RelevanceAI/arg-releases) | CLI | Public release artifacts for the arg CLI (binary distribution only; source lives in the private monorepo) | 0 | 2026-08-24 | v0.3.19 |
| [cc-plugin](https://github.com/RelevanceAI/cc-plugin) | plugin or integration | RelevanceAI Claude Code plugin (Skills + MCP) | 1 | 2026-07-27 | |
| [homebrew-tap](https://github.com/RelevanceAI/homebrew-tap) | CLI | Homebrew tap for the arg CLI. Run: brew tap relevanceai/tap | 0 | 2026-05-14 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-10 by build_directory.py (phase 1).
