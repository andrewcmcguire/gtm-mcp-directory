# Diffbot: MCP server status, API access gate and what it does

> A web-extraction and "Knowledge Graph" company that crawls the public web and structures it into an entity... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Diffbot

# Diffbot

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [diffbot.com](https://diffbot.com) · entry id 01-diffbot · source 01-data-enrichment.md line 521

**What it does**
A web-extraction and "Knowledge Graph" company that crawls the public web and structures it into an entity graph (organizations, people, articles) queryable for company/entity enrichment, plus raw article/page-extraction APIs.

**AI features, separated from automation with an AI label on it**
Uses its own long-standing computer-vision and NLP models to parse unstructured web pages into structured entities - genuinely closer to ML-based extraction than most "AI enrichment" marketing, though the enrichment/matching layer on top is standard graph lookup.

**RevOps role**
Entity/company-graph enrichment and web-data extraction layer - used to backfill firmographic detail or monitor company/news events rather than for direct person-level contact finding.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (free Diffbot token required to use the MCP tools)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/diffbot/diffbot-mcp

- [https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp)

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp)
- [https://www.diffbot.com/pricing](https://www.diffbot.com/pricing)
- [https://www.diffbot.com/products/knowledge-graph](https://www.diffbot.com/products/knowledge-graph)

3 source URLs. Raw sources field, verbatim:

https://github.com/diffbot/diffbot-mcp, https://www.diffbot.com/pricing, https://www.diffbot.com/products/knowledge-graph

**Notes, verbatim from the file**
Diffbot is a horizontal web-data/knowledge-graph company, not a purpose-built B2B contact tool - its GTM relevance is mainly company/entity-level enrichment, not email/phone finding. Free tier: 10,000 credits/month, no credit card required. Self-serve paid tiers start at Startup $299/month (250K credits), Plus $899/month (1M credits); Enterprise custom. Extracting a page costs 1 credit; exporting a full Knowledge Graph entity costs 25 credits.

**Provenance**

- **Entry id**: 01-diffbot

- **Source file**: 01-data-enrichment.md

- **Source line**: 521

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
