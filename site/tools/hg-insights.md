# HG Insights (Phoenix platform): MCP server status, API access gate and what it does

> Aggregates B2B technographic data (software/tech a company runs, sourced from job postings, web crawling,... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
HG Insights (Phoenix platform)

# HG Insights (Phoenix platform)

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://hginsights.com](https://hginsights.com) · entry id 05-hg-insights · source 05-signals-intent-abm.md line 232

**What it does**
Aggregates B2B technographic data (software/tech a company runs, sourced from job postings, web crawling, public filings, partner feeds), firmographics, IT spend estimates, and third-party intent (via TrustRadius review/research activity) into a unified company profile.

**AI features, separated from automation with an AI label on it**
Long-standing data-aggregation/technographics business that predates the "AI" framing. Newer "RGI Agent Builder" and MCP layer expose existing structured data to AI agents - infrastructure for AI, not AI-derived data itself; skeptical of "AI-ready infrastructure" marketing beyond that.

**RevOps role**
Firmographic/technographic enrichment and account intelligence, feeding ICP fit-scoring and territory/account prioritization upstream of outbound.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (`x-api-key` header; throttled to 100 calls/60 seconds per connection)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://learn.microsoft.com/en-us/connectors/hginsightsmcp/](https://learn.microsoft.com/en-us/connectors/hginsightsmcp/)Probed**: 2026-08-25, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://learn.microsoft.com/en-us/connectors/hginsightsmcp/ (Microsoft-certified connector, publisher HG Insights)

- [https://learn.microsoft.com/en-us/connectors/hginsightsmcp/](https://learn.microsoft.com/en-us/connectors/hginsightsmcp/)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://hginsights.com/gtm-data-insights/gtm-infrastructure/](https://hginsights.com/gtm-data-insights/gtm-infrastructure/)
- [https://hginsights.com/solutions-use-case/gtm-infrastructure-for-ai-agents/](https://hginsights.com/solutions-use-case/gtm-infrastructure-for-ai-agents/)
- [https://learn.microsoft.com/en-us/connectors/hginsightsmcp/](https://learn.microsoft.com/en-us/connectors/hginsightsmcp/)
- [https://data-docs.hginsights.com/v2/guides/overview](https://data-docs.hginsights.com/v2/guides/overview)
- [https://phoenix.hginsights.com/features](https://phoenix.hginsights.com/features)

5 source URLs. Raw sources field, verbatim:

https://hginsights.com/gtm-data-insights/gtm-infrastructure/, https://hginsights.com/solutions-use-case/gtm-infrastructure-for-ai-agents/, https://learn.microsoft.com/en-us/connectors/hginsightsmcp/, https://data-docs.hginsights.com/v2/guides/overview, https://phoenix.hginsights.com/features

**Notes, verbatim from the file**
The AI-agent/MCP product is described as "early access request" only, no self-serve signup found, consistent with HG Insights' historical enterprise-contract business model. Note: madkudu.com now 301-redirects to hginsights.com, indicating MadKudu (predictive PQL scoring) has been folded into HG Insights - see Sweep notes.

**Provenance**

- **Entry id**: 05-hg-insights

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 232

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
