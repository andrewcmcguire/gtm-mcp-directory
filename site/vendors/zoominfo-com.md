# ZoomInfo: products, MCP servers and connect URLs, one vendor page

> ZoomInfo (zoominfo.com): 2 products in The GTM MCP Directory, 1 with an official MCP server, 1 answering a live handshake, 56 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
ZoomInfo

# ZoomInfo

2 products in the directory
1 official MCP server
1 live handshake
Data baked 2026-09-12

Vendor domain: [zoominfo.com](https://zoominfo.com) · vendor page id zoominfo-com

**The rollup**

- **Products**: 2, facts checked by hand 2026-09-02, 2026-09-03

- **Official MCP servers**: 1 of 2, as recorded on 2026-09-02, 2026-09-03

- **Community MCP servers**: 1 of 2

- **Live handshake**: 1 of 2 answered an MCP initialize, 2 probed, 2026-09-04

- **Repo local**: 1 of 2: a server you install and run yourself

- **Docs only**: 0 of 2: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 56 named across 2 measured servers, harvested 2026-09-11

- **Bench tested**: 0 of 2 here, 1 of 374 across the directory

- **Ships a CLI**: 2 of 2 official, 0 community only, 0 none found, harvested 2026-09-11

- **GitHub organisation**: [github.com/Zoominfo](https://github.com/Zoominfo), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 2**

### [ZoomInfo](../tools/zoominfo.md)

A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human researchers, used for prospecting, account research, and lead enrichment.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: answered, asking for a key, 2026-09-04

- **Connect URL**: [https://mcp.zoominfo.com/mcp](https://mcp.zoominfo.com/mcp) (endpoint)

- **Tools catalogued**: 17 named, harvested 2026-09-11, catalogue fixed

- **last_checked**: 2026-09-03

### [Chorus](../tools/chorus.md)

Records, transcribes, and analyzes sales calls, meetings, and emails, and syncs the resulting insights into the CRM.

[Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/opensourceops/chorus-mcp-server](https://github.com/opensourceops/chorus-mcp-server) (docs page)

- **Tools catalogued**: 39 named, harvested 2026-09-11, catalogue fixed

- **last_checked**: 2026-09-02

**The gates, in plain words**

1 of 2 free to start, a solo operator gets API access without talking to anyone. 1 of 2 enterprise only, API access needs a contract.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)
- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Score rep performance](../jobs/score-rep-performance.md)

12 distinct job labels, the union across 2 products, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://mcp.zoominfo.com/mcp](https://mcp.zoominfo.com/mcp) (ZoomInfo, endpoint, probed 2026-09-04)
- [https://github.com/opensourceops/chorus-mcp-server](https://github.com/opensourceops/chorus-mcp-server) (Chorus, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [ZoomInfo](../tools/zoominfo.md) gtm official CLI

```
npm install -g @zoominfo/gtm-ai-cli
```

quoted from [https://gtm.ai/docs/cli](https://gtm.ai/docs/cli) on 2026-09-11, via npm

Login or key hint: gtm auth

1 more install command, 4 subcommands seen, harvested 2026-09-11, all on the [tool page](../tools/zoominfo.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/Zoominfo](https://github.com/Zoominfo) tied to the vendor by rule 1, account website https://www.zoominfo.com has the vendor's domain, confidence strong

- **Public repositories**: 8, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [zoominfo-mcp-plugin](https://github.com/Zoominfo/zoominfo-mcp-plugin) | MCP server | ZoomInfo MCP plugin | 7 | 2026-09-03 | |
| [n8n-nodes-zoominfo](https://github.com/Zoominfo/n8n-nodes-zoominfo) | plugin or integration | n8n community node for the ZoomInfo GTM API | 0 | 2026-09-02 | v1.0.0 |
| [gtm-ai-cli](https://github.com/Zoominfo/gtm-ai-cli) | CLI | A command-line tool for searching ZoomInfo's go-to-market data | 1 | 2026-08-30 | v1.1.0 |
| [homebrew-gtm-ai](https://github.com/Zoominfo/homebrew-gtm-ai) | infrastructure | Homebrew tap for gtm-ai formulae | 0 | 2026-08-26 | |
| [api-auth-java-client](https://github.com/Zoominfo/api-auth-java-client) | SDK | Zoominfo API's Java Authentication Client | 2 | 2026-06-30 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 374 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 2 products are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
