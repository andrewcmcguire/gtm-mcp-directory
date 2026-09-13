# Unify: products, MCP servers and connect URLs, one vendor page

> Unify (unifygtm.com): 1 product in The GTM MCP Directory, 0 with an official MCP server, 0 answering a live handshake, 13 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Unify

# Unify

1 product in the directory
0 official MCP servers
0 live handshakes
Data baked 2026-09-12

Vendor domain: [unifygtm.com](https://unifygtm.com) · vendor page id unifygtm-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 0 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 1 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 1 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 13 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 884 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/unifygtm](https://github.com/unifygtm), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Unify](../tools/unify.md)

A hybrid signals-plus-agent platform: AI agents build targeted account/prospect lists from 40+ data sources, write personalized outbound copy, and run multi-channel sequences triggered by intent signals ("plays").

[Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp) (docs page)

- **Tools catalogued**: 13 named, harvested 2026-09-12, catalogue fixed

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 paid and self serve, API access by paying, no sales call.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Build a target account list](../jobs/build-target-account-list.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

8 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp) (Unify, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Unify](../tools/unify.md) unify-cli community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
pip install unify-cli
```

quoted from [https://pypi.org/project/unify-cli/](https://pypi.org/project/unify-cli/) on 2026-09-12, via pypi, a third party source

harvested 2026-09-12, all on the [tool page](../tools/unify.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/unifygtm](https://github.com/unifygtm) tied to the vendor by rule 3, account website https://unifygtm.com has the vendor's domain, confidence strong

- **Public repositories**: 7, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-01

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [bulk-api-connector-examples](https://github.com/unifygtm/bulk-api-connector-examples) | docs or examples | Directory of example Connector implementations using the Unify Bulk API | 0 | 2026-09-01 | |
| [agent-plugins](https://github.com/unifygtm/agent-plugins) | plugin or integration | Official Unify GTM agent plugins for cursor, codex and claude. | 0 | 2026-08-25 | |
| [sdk-python](https://github.com/unifygtm/sdk-python) | SDK | Official Python SDK for the Unify API. | 0 | 2026-06-18 | v0.1.3 |
| [sdk-typescript](https://github.com/unifygtm/sdk-typescript) | SDK | Official TypeScript SDK for the Unify API. | 0 | 2026-06-17 | v0.1.3 |
| [intent-js-client](https://github.com/unifygtm/intent-js-client) | SDK | JavaScript client for interacting with the Unify Intent API in the browser. | 11 | 2026-06-14 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 884 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
