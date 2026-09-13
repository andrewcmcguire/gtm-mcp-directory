# Chili Piper: products, MCP servers and connect URLs, one vendor page

> Chili Piper (chilipiper.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 2 tools catalogued. Data baked 2026-09-13.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Chili Piper

# Chili Piper

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-13

Vendor domain: [chilipiper.com](https://chilipiper.com) · vendor page id chilipiper-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-25

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-25

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 2 named across 1 measured server, harvested 2026-09-13

- **Bench tested**: 0 of 1 here, 1 of 336 across the directory

- **Ships a CLI**: 0 of 1 official, 0 community only, 1 none found, harvested 2026-09-13

- **GitHub organisation**: [github.com/Chili-Piper](https://github.com/Chili-Piper), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Chili Piper](../tools/chili-piper.md)

Inbound lead-routing and instant meeting-booking platform ("Concierge") that qualifies web-form leads and books them directly onto the right rep's calendar in real time.

[Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) (docs page)

- **Tools catalogued**: 2 named, harvested 2026-09-13, catalogue fixed

- **last_checked**: 2026-08-25

**The gates, in plain words**

1 of 1 paid and self serve, API access by paying, no sales call.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Route an inbound lead](../jobs/route-inbound-lead.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

5 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) (Chili Piper, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

No CLI found for any product of this vendor by the 2026-09-13 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**On GitHub**

[github.com/Chili-Piper](https://github.com/Chili-Piper) tied to the vendor by rule 1, account website https://www.chilipiper.com/ has the vendor's domain, confidence strong

- **Public repositories**: 7, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [mcp-assets](https://github.com/Chili-Piper/mcp-assets) | MCP server | Official Chili Piper Skills and ChatGPT GPTs for the Chili Piper MCP - meeting diagnostics, routing audits, no-show... | 7 | 2026-09-08 | v1.0.0 |
| [terraform-provider-jitsu](https://github.com/Chili-Piper/terraform-provider-jitsu) | infrastructure | terraform provider for Jitsu | 0 | 2026-09-08 | v0.0.7 |
| [Integration](https://github.com/Chili-Piper/Integration) | plugin or integration | CP Integrations repository | 0 | 2026-03-30 | |
| [trivy-report-issue-action](https://github.com/Chili-Piper/trivy-report-issue-action) | infrastructure | Creates GitHub Issues from Trivy scan results. | 2 | 2025-02-20 | v1.2 |
| [repository-notifier](https://github.com/Chili-Piper/repository-notifier) | other | Repository Notifier Service | 0 | 2025-01-29 | v0.2 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-13 by build_directory.py (phase 1).
