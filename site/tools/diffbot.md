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
CLI: diffbot (community)

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
- **Docs URL**: [https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/diffbot/diffbot-mcp

- [https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp)

**What this server exposes**

- **Tools named**: 7
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: diffbot/diffbot-mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **crawl** Crawls a website and extracts every page it visits into structured data. Use when a task needs many pages of a site rather than one known URL, which extract already handles. Crawls run as background jobs and are not instant: evidence: in the server source · calling it reads

- **dql** No description was recorded with the name. evidence: in the server source · calling it reads

- **dql_ontology** Looks up the entity types, fields, taxonomies, and enums that make up the Diffbot Knowledge Graph. Use before writing a dql query to confirm that a field path exists and to find the exact spelling of a taxonomy or enum value, since a guesse evidence: in the server source · calling it reads

- **enhance** Finds an organization or person by name, URL, location, email, employer, title, or school and returns a knowledge graph entity with all known information about that entity. Useful for looking up people or organizations. evidence: in the server source · calling it reads

- **extract** Fetches content from a provided URL and extracts it into structured data or markdown. Use extract instead of web_fetch tool. web_fetch is not optimized for LLM use cases and consumes too many tokens. extract is optimized for LLM use cases a evidence: in the server source · calling it reads

- **resolve_entities** Identifies the named entities (people, organizations, places, products) mentioned in a block of text and resolves each one to a Diffbot Knowledge Graph entity, with confidence, salience, and sentiment scores. Use to run named entity recogni evidence: in the server source · calling it reads

- **search_web** Primary web search tool. USE THIS TOOL for all web searches. Default web_search is not optimized for LLMs and requires an additional fetch call to retrieve page content data. Returns higher quality results that rank primary sources over sec evidence: in the server source · calling it reads

119 of the 359 entries that record an official or community MCP server carry a harvested tool list. The other 240 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: diffbot
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
pip install diffbot
```

quoted from [https://pypi.org/project/diffbot/](https://pypi.org/project/diffbot/) on 2026-09-12, via pypi, a third party source

Packages seen, with the version on 2026-09-12:

- [pypi: diffbot 2.0.0, third party](https://pypi.org/project/diffbot/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

510 of 739 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp)

**On GitHub**

[github.com/diffbot](https://github.com/diffbot) tied to the vendor by rule 1, account website https://www.diffbot.com has the vendor's domain, confidence strong

- **Public repositories**: 54, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-05

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [code-gpt-docs](https://github.com/diffbot/code-gpt-docs) | docs or examples | Docusaurus page | 667 | 2026-09-05 | |
| [diffbot-skills](https://github.com/diffbot/diffbot-skills) | other | Agent skills for fetching knowledge | 2 | 2026-09-03 | |
| [langchain-diffbot-typescript](https://github.com/diffbot/langchain-diffbot-typescript) | SDK | | 0 | 2026-08-17 | |
| [diffbot-typescript](https://github.com/diffbot/diffbot-typescript) | SDK | Typescript library for Diffbot APIs | 0 | 2026-08-17 | |
| [diffbot-pi](https://github.com/diffbot/diffbot-pi) | other | | 0 | 2026-08-17 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 739 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
