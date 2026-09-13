# LeadMagic: products, MCP servers and connect URLs, one vendor page

> LeadMagic (leadmagic.io): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 19 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
LeadMagic

# LeadMagic

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [leadmagic.io](https://leadmagic.io) · vendor page id leadmagic-io

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 1 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 19 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 604 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/LeadMagic](https://github.com/LeadMagic), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [LeadMagic](../tools/leadmagic.md)

A B2B contact/company data API and CLI that finds and validates work emails, mobile numbers, and social-to-email matches, plus company/job/ad-intelligence lookups, billing only for successful (valid) results.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp) (docs page)

- **Tools catalogued**: 19 named, harvested 2026-09-12, catalogue fixed

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Scrape job postings](../jobs/scrape-job-postings.md)

5 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp) (LeadMagic, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [LeadMagic](../tools/leadmagic.md) leadmagic community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
npm install -g leadmagic-agent-cli
```

quoted from [https://www.npmjs.com/package/leadmagic-agent-cli](https://www.npmjs.com/package/leadmagic-agent-cli) on 2026-09-12, via npm, a third party source

1 more install command, harvested 2026-09-12, all on the [tool page](../tools/leadmagic.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/LeadMagic](https://github.com/LeadMagic) tied to the vendor by rule 1, account website https://leadmagic.io has the vendor's domain, confidence strong

- **Public repositories**: 10, forks excluded, as read on 2026-09-08
- **Mention MCP**: 6 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [gtm-skills](https://github.com/LeadMagic/gtm-skills) | other | GTM agent skills for Claude Code, Codex, and GitHub Copilot: sales, marketing, SEO, RevOps, and customer research... | 48 | 2026-09-07 | v0.26.0 |
| [leadmagic-openapi](https://github.com/LeadMagic/leadmagic-openapi) | API client | OpenAPI 3.1 specification for the LeadMagic B2B data enrichment REST API: email finder, email validation, people and... | 2 | 2026-09-07 | v1.0.0 |
| [leadmagic-cursor-plugin](https://github.com/LeadMagic/leadmagic-cursor-plugin) | plugin or integration | LeadMagic Cursor plugin for B2B research, email finding, company intelligence, and data enrichment through hosted MCP... | 0 | 2026-09-07 | |
| [leadmagic-skills](https://github.com/LeadMagic/leadmagic-skills) | API client | LeadMagic agent skills and Claude Code plugin for B2B enrichment, people and company search, REST API integration, and... | 0 | 2026-09-07 | |
| [leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp) | MCP server | Local TypeScript MCP server for the LeadMagic API: email finder, email validation, company enrichment, and research... | 7 | 2026-09-07 | v1.0.3 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 604 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
