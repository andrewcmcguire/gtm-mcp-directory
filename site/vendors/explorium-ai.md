# Explorium: products, MCP servers and connect URLs, one vendor page

> Explorium (explorium.ai): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 11 tools catalogued. Data baked 2026-09-09.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Explorium

# Explorium

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-09

Vendor domain: [explorium.ai](https://explorium.ai) · vendor page id explorium-ai

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 11 named across 1 measured server, harvested 2026-09-09

- **Bench tested**: 0 of 1 here, 1 of 336 across the directory

- **Ships a CLI**: 0 of 1 official, 0 community only, 1 none found, harvested 2026-09-09

- **GitHub organisation**: [github.com/explorium-ai](https://github.com/explorium-ai), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Explorium](../tools/explorium.md)

Aggregates roughly 50 third-party data sources into one API/platform for business and prospect lookup (firmographics, contacts, technographics, business events), claiming coverage of 150M+ companies and 800M+ contacts.

[Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://www.explorium.ai/mcp/](https://www.explorium.ai/mcp/) (docs page)

- **Tools catalogued**: 11 named, harvested 2026-09-09, catalogue fixed

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 1 paid and self serve, API access by paying, no sales call.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)

6 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://www.explorium.ai/mcp/](https://www.explorium.ai/mcp/) (Explorium, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

No CLI found for any product of this vendor by the 2026-09-09 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**On GitHub**

[github.com/explorium-ai](https://github.com/explorium-ai) tied to the vendor by rule 2, account website https://www.explorium.ai has the vendor's domain, confidence strong

- **Public repositories**: 20, forks excluded, as read on 2026-09-08
- **Mention MCP**: 7 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [vibeprospecting-mcp](https://github.com/explorium-ai/vibeprospecting-mcp) | MCP server | Power your chat with B2B data to create lead lists, research companies, personalize your outreach, and more. | 33 | 2026-09-08 | 2.0.0 |
| [explorium-mintlify-docs](https://github.com/explorium-ai/explorium-mintlify-docs) | docs or examples | Explorium documentation over mintlify | 0 | 2026-09-08 | |
| [vibeprospecting-plugin](https://github.com/explorium-ai/vibeprospecting-plugin) | plugin or integration | Power your chat with B2B data to create lead lists, research companies, personalize your outreach, and more. | 28 | 2026-09-08 | |
| [agentsource-mcp-ext](https://github.com/explorium-ai/agentsource-mcp-ext) | MCP server | Access live company and contact data through Explorium's MCP server | 9 | 2026-08-25 | v2.0.9 |
| [workflows-starter-template](https://github.com/explorium-ai/workflows-starter-template) | docs or examples | | 0 | 2026-08-19 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-09 by build_directory.py (phase 1).
