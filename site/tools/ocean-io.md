# Ocean.io: MCP server status, API access gate and what it does

> A company-search and "lookalike" prospecting tool that finds businesses similar to a given target account... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Ocean.io

# Ocean.io

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.ocean.io](https://www.ocean.io) · entry id 01-ocean-io · source 01-data-enrichment.md line 160

**What it does**
A company-search and "lookalike" prospecting tool that finds businesses similar to a given target account based on industry, size, geography, and website content, and exports the resulting account lists.

**AI features, separated from automation with an AI label on it**
Genuinely model-based: the vendor describes crawling company website text and building NLP/ML-derived "Context Vector" embeddings per company, then scoring similarity across firmographic + semantic + digital-footprint signals to produce lookalike matches. This is closer to real applied ML (embedding similarity) than most "AI" enrichment claims, though the underlying accuracy is not independently verified here.

**RevOps role**
Account-based prospecting/lookalike list-building, typically used to expand a target account list from a set of best-fit customers before enrichment and outreach.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (api-token passed as a URL parameter to the hosted MCP endpoint)

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://app.ocean.io/docs/getting-started/mcp](https://app.ocean.io/docs/getting-started/mcp)Probed**: 2026-08-25, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://app.ocean.io/docs/getting-started/mcp (endpoint: https://api.ocean.io/mcp/?api-token=YOUR_API_TOKEN)

- [https://app.ocean.io/docs/getting-started/mcp](https://app.ocean.io/docs/getting-started/mcp)
- [https://api.ocean.io/mcp/?api-token=YOUR_API_TOKEN](https://api.ocean.io/mcp/?api-token=YOUR_API_TOKEN)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Meerkats-Ai/ocean-io-mcp-server](https://github.com/Meerkats-Ai/ocean-io-mcp-server)

**Jobs it can do**

- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Build a target account list](../jobs/build-target-account-list.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.ocean.io/pricing](https://www.ocean.io/pricing)
- [https://book.ocean.io/campaign/api-pricing](https://book.ocean.io/campaign/api-pricing)
- [https://app.ocean.io/docs/getting-started/mcp](https://app.ocean.io/docs/getting-started/mcp)
- [https://github.com/Meerkats-Ai/ocean-io-mcp-server](https://github.com/Meerkats-Ai/ocean-io-mcp-server)
- [https://openbenchmarks.com/lookalikes/ocean-io](https://openbenchmarks.com/lookalikes/ocean-io)
- [https://www.ocean.io/features/ai-company-search](https://www.ocean.io/features/ai-company-search)

6 source URLs. Raw sources field, verbatim:

https://www.ocean.io/pricing, https://book.ocean.io/campaign/api-pricing, https://app.ocean.io/docs/getting-started/mcp, https://github.com/Meerkats-Ai/ocean-io-mcp-server, https://openbenchmarks.com/lookalikes/ocean-io, https://www.ocean.io/features/ai-company-search

**Notes, verbatim from the file**
Direct pricing-page fetch was blocked (403/header errors), so plan names/prices are taken from search-result snippets only: a Trial tier ($0, 14-day) and paid tiers reported variously as Premium ~$79/mo and Professional ~$129/mo, or ~$32/mo billed yearly for 9,000 credits in another source - figures are inconsistent across secondary sources and should be re-verified directly on ocean.io before publishing a hard number. No self-serve free API tier was confirmed; the API pricing page directs to "contact team for expert guidance," suggesting API-level access may require a sales conversation even though the platform itself has a self-serve trial. A separate third-party/community MCP repo also exists (github.com/Meerkats-Ai/ocean-io-mcp-server) but the official vendor-hosted MCP at api.ocean.io/mcp is the primary one.

**Provenance**

- **Entry id**: 01-ocean-io

- **Source file**: 01-data-enrichment.md

- **Source line**: 160

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
