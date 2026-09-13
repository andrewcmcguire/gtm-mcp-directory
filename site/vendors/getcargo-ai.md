# Cargo: products, MCP servers and connect URLs, one vendor page

> Cargo (getcargo.ai): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Cargo

# Cargo

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [getcargo.ai](https://getcargo.ai) · vendor page id getcargo-ai

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 0 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 1,032 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/getcargohq](https://github.com/getcargohq), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Cargo](../tools/cargo.md)

A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment, scoring, routing, CRM sync - as code, run by AI agents.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://docs.getcargo.ai/](https://docs.getcargo.ai/) (docs page)

- **Tools catalogued**: 0 named, harvested 2026-09-12, catalogue dynamic, the server exposes the customer's own workspace

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Route an inbound lead](../jobs/route-inbound-lead.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

5 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://docs.getcargo.ai/](https://docs.getcargo.ai/) (Cargo, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Cargo](../tools/cargo.md) cargo official CLI

```
npm install -g @cargo-ai/cli
```

quoted from [https://docs.getcargo.ai/cli/overview](https://docs.getcargo.ai/cli/overview) on 2026-09-12, via npm

Login or key hint: cargo-ai login --token

**On GitHub**

[github.com/getcargohq](https://github.com/getcargohq) tied to the vendor by rule 2, account name 'Cargo' equals the entry's display name, confidence check

- **Public repositories**: 5, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [gtm-skills](https://github.com/getcargohq/gtm-skills) | other | Standalone Cargo GTM agent skills - one job each. Find leads, enrich contacts, verify emails, track signals. | 3 | 2026-09-07 | |
| [cargo-skills](https://github.com/getcargohq/cargo-skills) | CLI | GTM engineering skills for AI coding agents - build lead lists, find & verify emails, waterfall enrichment, lead... | 17 | 2026-09-05 | |
| [cargo-manifest](https://github.com/getcargohq/cargo-manifest) | other | The software factory for go-to-market. An open-source monorepo holding your company context (ICP, personas, plays,... | 6 | 2026-09-03 | |
| [cargo-partner-skills](https://github.com/getcargohq/cargo-partner-skills) | other | | 0 | 2026-08-19 | |
| [dummy-integration](https://github.com/getcargohq/dummy-integration) | plugin or integration | | 2 | 2026-01-13 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 1,032 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
