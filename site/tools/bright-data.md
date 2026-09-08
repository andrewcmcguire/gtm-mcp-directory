# Bright Data: MCP server status, API access gate and what it does

> A general-purpose web-scraping/proxy infrastructure platform (residential proxies, browser automation,... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Bright Data

# Bright Data

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [brightdata.com](https://brightdata.com) · entry id 01-bright-data · source 01-data-enrichment.md line 426

**What it does**
A general-purpose web-scraping/proxy infrastructure platform (residential proxies, browser automation, structured scraping APIs) that GTM engineers repurpose to pull LinkedIn, company-site, and directory data when off-the-shelf enrichment providers lack a record.

**AI features, separated from automation with an AI label on it**
The MCP server exposes scraping/browsing/search tools an LLM agent can call and chain; underlying page parsing uses pattern- and ML-based extraction, not a proprietary "enrichment AI" - Bright Data is fundamentally a scraping/proxy company wearing an agent-tooling wrapper.

**RevOps role**
Fallback/last-resort scraping layer in a waterfall enrichment stack, used when structured providers (ZoomInfo, PDL, Clearbit) return no match.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (Bright Data API token)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/brightdata/brightdata-mcp

- [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)

**What this server exposes**

- **Tools named**: 19
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-08
- **Repo read**: brightdata/brightdata-mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **diagnose_scraping_approach** Run a two-step diagnostic to discover the correct evidence: in the server source · calling it reads

- **discover** Search the web and rank results by AI-driven relevance. evidence: in the server source · calling it reads

- **extract** Scrape a webpage and extract structured data as JSON. evidence: in the server source · calling it reads

- **list_dataset_fields** List the filterable fields of a searchable dataset evidence: in the server source · calling it reads

- **scrape_as_html** Scrape a single webpage URL with advanced options for evidence: in the server source · calling it reads

- **scrape_as_markdown** Scrape a single webpage URL with advanced options for evidence: in the server source · calling it reads

- **scrape_batch** Scrape multiple webpages URLs with advanced options for evidence: in the server source · calling it reads

- **scraping_browser_get_html** Get the HTML content of the current page. Avoid using this evidence: in the server source · calling it reads

- **scraping_browser_get_text** Get the text content of the current page evidence: in the server source · calling it reads

- **scraping_browser_go_back** Go back to the previous page evidence: in the server source · calling it reads

- **scraping_browser_go_forward** Go forward to the next page evidence: in the server source · calling it reads

- **scraping_browser_navigate** Navigate a scraping browser session to a new URL evidence: in the server source · calling it reads

- **scraping_browser_screenshot** Take a screenshot of the current page evidence: in the server source · calling it reads

- **scraping_browser_scroll** Scroll to the bottom of the current page evidence: in the server source · calling it reads

- **search_dataset** Search a Bright Data dataset by a filter and get matching evidence: in the server source · calling it reads

- **search_engine** Scrape search results from Google, Bing or Yandex. Returns evidence: in the server source · calling it reads

- **search_engine_batch** Run multiple search queries simultaneously. Returns evidence: in the server source · calling it reads

- **session_stats** Tell the user about the tool usage during this session evidence: in the server source · calling it reads

- **web_scraping_strategy** Decision tree for picking the right Bright Data tool. evidence: in the server source · calling it reads

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. Every name across every server is on the [tools index](../tools-index.md).

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)

**Jobs it can do**

- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)
- [https://mcpservers.org/servers/brightdata/brightdata-mcp](https://mcpservers.org/servers/brightdata/brightdata-mcp)
- [https://brightdata.com/pricing/mcp-server](https://brightdata.com/pricing/mcp-server)

3 source URLs. Raw sources field, verbatim:

https://github.com/brightdata/brightdata-mcp, https://mcpservers.org/servers/brightdata/brightdata-mcp, https://brightdata.com/pricing/mcp-server

**Notes, verbatim from the file**
Broader-scope than a purpose-built contact-enrichment vendor - it's web-data infrastructure, not a firmographic/contact database. Self-serve signup with pay-as-you-go and subscription plans; not enterprise-only for basic access. The MCP server alone exposes 69 tools spanning search, scraping, and browser automation.

**Provenance**

- **Entry id**: 01-bright-data

- **Source file**: 01-data-enrichment.md

- **Source line**: 426

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
