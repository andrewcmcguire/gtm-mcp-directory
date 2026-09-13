# Clay: products, MCP servers and connect URLs, one vendor page

> Clay (clay.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 89 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Clay

# Clay

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [clay.com](https://clay.com) · vendor page id clay-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-03

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-03

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 89 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 934 across the directory

- **Ships a CLI**: 0 of 1 official, 0 community only, 1 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/clay-run](https://github.com/clay-run), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Clay](../tools/clay.md)

A spreadsheet-style workflow/orchestration tool that runs lead and company records through "waterfall" lookups across 100-200+ third-party data providers (Apollo, Lusha, Clearbit, etc.) and chains automation steps ("recipes") to build, enrich, and route...

[Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://www.clay.com/mcp](https://www.clay.com/mcp) (docs page)

- **Tools catalogued**: 89 named, harvested 2026-09-12, catalogue fixed

- **last_checked**: 2026-09-03

**The gates, in plain words**

1 of 1 paid and self serve, API access by paying, no sales call.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Build a target account list](../jobs/build-target-account-list.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

7 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://www.clay.com/mcp](https://www.clay.com/mcp) (Clay, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

No CLI found for any product of this vendor by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**On GitHub**

[github.com/clay-run](https://github.com/clay-run) tied to the vendor by rule 3, account website https://clay.com has the vendor's domain, confidence strong

- **Public repositories**: 11, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [public-docs](https://github.com/clay-run/public-docs) | docs or examples | MD files of Clay documentation | 5 | 2026-09-08 | |
| [agent-plugins](https://github.com/clay-run/agent-plugins) | CLI | Build with Clay in your AI coding agent - skills, MCP tools, and the clay CLI for Claude Code, Codex, and Cursor.... | 111 | 2026-09-03 | clay-cli-v0.16.0 |
| [action-template-nodejs](https://github.com/clay-run/action-template-nodejs) | docs or examples | A Clay Action Template - NodeJs | 1 | 2020-09-15 | |
| [base-app-starter](https://github.com/clay-run/base-app-starter) | docs or examples | Base Starter App | 1 | 2020-09-04 | |
| [keyword-lists](https://github.com/clay-run/keyword-lists) | other | Some keyword lists | 0 | 2020-02-05 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 934 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
