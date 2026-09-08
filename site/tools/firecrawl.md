# Firecrawl: MCP server status, API access gate and what it does

> A web scraping and crawling API that turns any URL or whole site into clean markdown or structured JSON for... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Firecrawl

# Firecrawl

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07
CLI: firecrawl

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [firecrawl.dev](https://firecrawl.dev) · entry id 01-firecrawl · source 01-data-enrichment.md line 873

**What it does**
A web scraping and crawling API that turns any URL or whole site into clean markdown or structured JSON for LLM pipelines, with search, map, crawl, extract, parse and browser-interaction endpoints.

**AI features, separated from automation with an AI label on it**
The scrape and crawl core is deterministic fetching plus HTML-to-markdown conversion. AI enters in the extract mode (LLM-driven schema extraction from pages), the agent tool (autonomous web research) and the interact tool (natural-language browser actions); the vendor lists those as separate tools from plain scrape.

**RevOps role**
The web-fetch leg of a research or enrichment agent: pull a prospect's site, pricing page or changelog into markdown so a downstream model can extract firmographics, tech stack or trigger events without a data vendor.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key as an Authorization Bearer header, or browser sign-in via the /v2/mcp-oauth variant, or keyless with daily limits. The vendor docs state "Configure an API key in your client, no browser needed" for the key path and describe a "No account or key" mode that works "within daily limits".

- **Parsed URLs**: 5 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.firecrawl.dev/v2/mcp (docs: https://docs.firecrawl.dev/mcp-server; repo: https://github.com/firecrawl/firecrawl-mcp-server; search-only endpoint https://mcp.firecrawl.dev/v2/mcp-search; OAuth variant https://mcp.firecrawl.dev/v2/mcp-oauth)

- [https://mcp.firecrawl.dev/v2/mcp](https://mcp.firecrawl.dev/v2/mcp)
- [https://docs.firecrawl.dev/mcp-server](https://docs.firecrawl.dev/mcp-server)
- [https://github.com/firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)
- [https://mcp.firecrawl.dev/v2/mcp-search](https://mcp.firecrawl.dev/v2/mcp-search)
- [https://mcp.firecrawl.dev/v2/mcp-oauth](https://mcp.firecrawl.dev/v2/mcp-oauth)

**What this server exposes**

- **Tools named**: 13
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-08
- **Repo read**: firecrawl/firecrawl-mcp-server
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **agent** Multi-source research, unknown or many sites evidence: in a README table · calling it reads

- **crawl** Multi-page extraction (with limits) evidence: in a README table · calling it reads

- **developer** Programming questions over developer sources evidence: in a README table · calling it reads

- **firecrawl_parse** Parse one supported document into markdown, HTML, links, summary, targeted answers, or JSON matching a schema. Supported inputs include common HTML, PDF, Word, RTF, OpenDocument, and spreadsheet files; PDF parsing can be bounded with `pdfO evidence: answered tools/list · calling it reads

- **firecrawl_scrape** Retrieve and extract content from one supplied URL through Firecrawl. Use this when the request identifies a page and needs its content or defined fields. It can return markdown, HTML, links, screenshots, branding data, a targeted answer, evidence: answered tools/list · calling it reads · required: url

- **firecrawl_search** Search web, news, or image sources and return ranked results. Operators include quoted phrases, `-term`, `site:host`, `inurl:term`, `intitle:term`, and `related:host`; the set is non-exhaustive. `includeDomains` and `excludeDomains` are mu evidence: answered tools/list · calling it reads · required: query

- **interact** Interact with a URL or scraped page evidence: in a README table · calling it reads

- **map** Discovering URLs on a site evidence: in a README table · calling it reads

- **monitor** Recurring page checks evidence: in a README table · calling it reads

- **parse** Files and hosted upload refs evidence: in a README table · calling it reads

- **research** Paper and GitHub repository research evidence: in a README table · calling it reads

- **scrape** Single page content evidence: in a README table · calling it reads

- **search** Web search for info evidence: in a README table · calling it reads

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: firecrawl
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-08

Install, as the source shows it:

```
npm install -g firecrawl-cli
```

quoted from [https://docs.firecrawl.dev/sdks/cli](https://docs.firecrawl.dev/sdks/cli) on 2026-09-08, via npm

```
npx -y firecrawl-cli@latest
```

quoted from [https://docs.firecrawl.dev/sdks/cli](https://docs.firecrawl.dev/sdks/cli) on 2026-09-08, via npx

Login or key hint seen on the page:

firecrawl login

16 subcommands seen with the binary in the docs or README:
expand to read them

agent, browser, config, crawl, credit-usage, developer, init, interact, login, logout, map, monitor, scrape, search, version, view-config

Packages seen, with the version on 2026-09-08:

- [npm: firecrawl-cli 1.23.3](https://www.npmjs.com/package/firecrawl-cli)

Where it was documented:

- [https://docs.firecrawl.dev/sdks/cli](https://docs.firecrawl.dev/sdks/cli) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-08.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the vendor's pricing page states "Firecrawl gives you 1,000 free credits every month, which covers about 1,000 pages, and no card is required." Paid plans are listed at Hobby $16/month, Standard $83/month, Growth $333/month and Scale $599/month (billed yearly), Enterprise custom.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)

**On GitHub**

[github.com/firecrawl](https://github.com/firecrawl) tied to the vendor by rule 1, account website firecrawl.dev has the vendor's domain, confidence strong

- **Public repositories**: 86, forks excluded, as read on 2026-09-08
- **Mention MCP**: 3 of them
- **Look like CLIs**: 3 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [pdf-inspector](https://github.com/firecrawl/pdf-inspector) | other | Fast Rust library for PDF inspection, classification, and text extraction. Intelligently detects scanned vs text-based... | 18,944 | 2026-09-08 | v1.18.0 |
| [firecrawl-php](https://github.com/firecrawl/firecrawl-php) | SDK | | 2 | 2026-09-08 | |
| [firecrawl](https://github.com/firecrawl/firecrawl) | other | The context API to search, scrape, and interact with the web at scale. 🔥 | 177,931 | 2026-09-08 | v2.11.0 |
| [firecrawl-docs](https://github.com/firecrawl/firecrawl-docs) | docs or examples | Documentation for Firecrawl. | 92 | 2026-09-08 | |
| [firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) | MCP server | 🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients. | 7,418 | 2026-09-08 | v3.2.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://docs.firecrawl.dev/mcp-server](https://docs.firecrawl.dev/mcp-server)
- [https://www.firecrawl.dev/pricing](https://www.firecrawl.dev/pricing)
- [https://github.com/firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)
- [https://mcp.firecrawl.dev/v2/mcp](https://mcp.firecrawl.dev/v2/mcp)

4 source URLs. Raw sources field, verbatim:

https://docs.firecrawl.dev/mcp-server, https://www.firecrawl.dev/pricing, https://github.com/firecrawl/firecrawl-mcp-server, https://mcp.firecrawl.dev/v2/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.firecrawl.dev/v2/mcp with no key returned HTTP 200 with a JSON-RPC result (protocolVersion 2025-03-26, serverInfo name beginning "firecrawl-"), which matches the documented keyless mode. The control POST to /zzz-not-a-route on the same host returned 200 with the marketing site's HTML, so the control path is not a discriminator for this host and the JSON-RPC body is the evidence. The repo README lists scrape, map, search, crawl, parse, agent, interact, developer_search, research and monitor tools (14 or more). Firecrawl is a general web-data tool, not a contact database; it is in this category because GTM agents use it as the fetch layer under enrichment, the same reason Exa and Bright Data are here. 2026-09-07: https://mcp.firecrawl.dev/v2/mcp returned 200 with a JSON-RPC initialize result to an MCP initialize POST (https://mcp.firecrawl.dev/v2/mcp).

**Provenance**

- **Entry id**: 01-firecrawl

- **Source file**: 01-data-enrichment.md

- **Source line**: 873

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
