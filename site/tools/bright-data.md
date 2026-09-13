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
CLI: bdata

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
- **Harvested**: 2026-09-12
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

119 of the 251 entries that record an official or community MCP server carry a harvested tool list. The other 132 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: bdata
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @brightdata/cli
```

quoted from [https://www.npmjs.com/package/@brightdata/cli](https://www.npmjs.com/package/@brightdata/cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @brightdata/cli 0.3.6](https://www.npmjs.com/package/@brightdata/cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

374 of 468 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)

**On GitHub**

[github.com/brightdata](https://github.com/brightdata) tied to the vendor by rule 1, account website https://brightdata.com has the vendor's domain, confidence strong

- **Public repositories**: 62, forks excluded, as read on 2026-09-08
- **Mention MCP**: 7 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [cli](https://github.com/brightdata/cli) | CLI | Official Bright Data CLI - scrape, search, and extract structured web data directly from your terminal. | 6,365 | 2026-09-07 | v0.3.5 |
| [skills](https://github.com/brightdata/skills) | other | | 257 | 2026-09-06 | |
| [answer-engines-country-codes](https://github.com/brightdata/answer-engines-country-codes) | other | Answer engine country codes | 3 | 2026-08-12 | |
| [sdk-python](https://github.com/brightdata/sdk-python) | SDK | Bright Data's python SDK, use it to call bright data's scrape and search tools. bypass any Bot-detection or Captcha and... | 91 | 2026-08-12 | v2.5.2 |
| [brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | MCP server | A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access. | 2,634 | 2026-08-12 | v2.11.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 468 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
