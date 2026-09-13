# Apollo.io: products, MCP servers and connect URLs, one vendor page

> Apollo.io (apollo.io): 2 products in The GTM MCP Directory, 2 with an official MCP server, 0 answering a live handshake, 40 tools catalogued. Data baked 2026-09-13.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Apollo.io

# Apollo.io

2 products in the directory
2 official MCP servers
0 live handshakes
Data baked 2026-09-13

Vendor domain: [apollo.io](https://apollo.io) · vendor page id apollo-io

**The rollup**

- **Products**: 2, facts checked by hand 2026-08-24, 2026-09-03

- **Official MCP servers**: 2 of 2, as recorded on 2026-08-24, 2026-09-03

- **Community MCP servers**: 0 of 2

- **Live handshake**: 0 of 2 answered an MCP initialize, 2 probed, 2026-09-04

- **Repo local**: 2 of 2: a server you install and run yourself

- **Docs only**: 0 of 2: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 40 named across 2 measured servers, harvested 2026-09-13

- **Bench tested**: 0 of 2 here, 1 of 336 across the directory

- **Ships a CLI**: 0 of 2 official, 0 community only, 2 none found, harvested 2026-09-13

- **GitHub organisation**: [github.com/apolloio](https://github.com/apolloio), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 2**

### [Apollo.io](../tools/apollo-io.md)

A combined B2B contact database (265M+ contacts) and sales engagement platform in one product - prospect search/filtering, email and call sequencing, and contact/organization enrichment.

[Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) (docs page)

- **Tools catalogued**: 20 named, harvested 2026-09-13, catalogue fixed

- **last_checked**: 2026-09-03

### [Apollo.io Sequences (Emailer Campaigns)](../tools/apollo-io-sequences.md)

Apollo's outbound-sequencing feature - multi-step, multi-channel (email/call/task) cadences that enroll contacts pulled from Apollo's prospecting database and track send/reply state.

[Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) (docs page)

- **Tools catalogued**: 20 named, harvested 2026-09-13, catalogue fixed

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 2 paid and self serve, API access by paying, no sales call. 1 of 2 enterprise only, API access needs a contract.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)

10 distinct job labels, the union across 2 products, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) (Apollo.io, docs page, probed 2026-09-04)
- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) (Apollo.io Sequences (Emailer Campaigns), docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

No CLI found for any product of this vendor by the 2026-09-13 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**On GitHub**

[github.com/apolloio](https://github.com/apolloio) tied to the vendor by rule 1, account website https://www.apollo.io has the vendor's domain, confidence strong

- **Public repositories**: 10, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-08-31

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [apollo-io-cli](https://github.com/apolloio/apollo-io-cli) | CLI | The Official Apollo.io CLI | 53 | 2026-08-31 | v2.1.0 |
| [claude-statusline](https://github.com/apolloio/claude-statusline) | other | | 1 | 2026-08-26 | |
| [homebrew-apollo-io-cli](https://github.com/apolloio/homebrew-apollo-io-cli) | CLI | Homebrew tap for apollo-io-cli | 1 | 2026-08-07 | |
| [apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) | MCP server | Connect Claude Code + Cowork to Apollo MCP via this plugin | 20 | 2026-07-20 | v0.1.1 |
| [n8n-nodes-apollo](https://github.com/apolloio/n8n-nodes-apollo) | plugin or integration | Official Apollo.io n8n community node for lead enrichment and organization enrichment | 1 | 2026-07-17 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 2 products are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-13 by build_directory.py (phase 1).
