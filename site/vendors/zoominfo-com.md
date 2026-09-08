# ZoomInfo: products, MCP servers and connect URLs, one vendor page

> ZoomInfo (zoominfo.com): 2 products in The GTM MCP Directory, 1 with an official MCP server, 1 answering a live handshake, 56 tools catalogued. Data baked 2026-09-08.

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
Data baked 2026-09-08

Vendor domain: [zoominfo.com](https://zoominfo.com) · vendor page id zoominfo-com

**The rollup**

- **Products**: 2, facts checked by hand 2026-09-02, 2026-09-03

- **Official MCP servers**: 1 of 2, as recorded on 2026-09-02, 2026-09-03

- **Community MCP servers**: 1 of 2

- **Live handshake**: 1 of 2 answered an MCP initialize, 2 probed, 2026-09-04

- **Repo local**: 1 of 2: a server you install and run yourself

- **Docs only**: 0 of 2: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 56 named across 2 measured servers, harvested 2026-09-08

- **Bench tested**: 0 of 2 here, 1 of 336 across the directory

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 2**

### [ZoomInfo](../tools/zoominfo.md)

A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human researchers, used for prospecting, account research, and lead enrichment.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED

- **Endpoint probe**: answered, asking for a key, 2026-09-04

- **Connect URL**: [https://mcp.zoominfo.com/mcp](https://mcp.zoominfo.com/mcp) (endpoint)

- **Tools catalogued**: 17 named, harvested 2026-09-08, catalogue fixed

- **last_checked**: 2026-09-03

### [Chorus](../tools/chorus.md)

Records, transcribes, and analyzes sales calls, meetings, and emails, and syncs the resulting insights into the CRM.

[Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED

- **Endpoint probe**: repo or package: install and run locally, 2026-09-04

- **Connect URL**: [https://github.com/opensourceops/chorus-mcp-server](https://github.com/opensourceops/chorus-mcp-server) (docs page)

- **Tools catalogued**: 39 named, harvested 2026-09-08, catalogue fixed

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

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 2 products are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-08 by build_directory.py (phase 1).
