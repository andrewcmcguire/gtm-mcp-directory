# Meltwater: products, MCP servers and connect URLs, one vendor page

> Meltwater (meltwater.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Meltwater

# Meltwater

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [meltwater.com](https://meltwater.com) · vendor page id meltwater-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-02

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-02

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 559 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/meltwater](https://github.com/meltwater), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Meltwater](../tools/meltwater.md)

Media-intelligence and social-listening platform that consolidates news coverage, social conversations, and AI-generated content into prioritized alerts and workflows for PR, comms, and marketing teams.

[Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://developer.meltwater.com/guides/meltwater-mcp/overview/](https://developer.meltwater.com/guides/meltwater-mcp/overview/) (docs page)

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-02

**The gates, in plain words**

1 of 1 enterprise only, API access needs a contract.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

1 distinct job label, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://developer.meltwater.com/guides/meltwater-mcp/overview/](https://developer.meltwater.com/guides/meltwater-mcp/overview/) (Meltwater, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Meltwater](../tools/meltwater.md) generateJwk official CLI

```
npm install -g @meltwater/jwk-converter-cli
```

quoted from [https://www.npmjs.com/package/@meltwater/jwk-converter-cli](https://www.npmjs.com/package/@meltwater/jwk-converter-cli) on 2026-09-12, via npm

harvested 2026-09-12, all on the [tool page](../tools/meltwater.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/meltwater](https://github.com/meltwater) tied to the vendor by rule 3, account website https://underthehood.meltwater.com has the vendor's domain, confidence strong

- **Public repositories**: 20, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 3 of them
- **Latest push**: 2026-08-11

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [meltwater-plugins](https://github.com/meltwater/meltwater-plugins) | plugin or integration | Official Meltwater plugins for AI assistants and developer platforms. | 0 | 2026-08-11 | |
| [aws-configuration-fetcher](https://github.com/meltwater/aws-configuration-fetcher) | other | A simple system for gathering configuration from both SSM and Secrets Manager in AWS | 0 | 2026-08-03 | |
| [meltwater-api-examples](https://github.com/meltwater/meltwater-api-examples) | docs or examples | Example code for Meltwater API customers building their own solutions for PR & marketing use cases | 2 | 2026-07-14 | |
| [meltwater-killercoda](https://github.com/meltwater/meltwater-killercoda) | other | Meltwater Engineering's Public / Shared Training Center | 2 | 2026-06-26 | |
| [terraform-aws-asg-dns-handler](https://github.com/meltwater/terraform-aws-asg-dns-handler) | infrastructure | Terraform module for dynamically setting hostnames following a pattern on instances in AWS Auto Scaling Groups | 77 | 2026-06-25 | v2.1.8 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 559 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
