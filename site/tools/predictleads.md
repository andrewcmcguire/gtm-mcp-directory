# PredictLeads: MCP server status, API access gate and what it does

> Aggregates five signal categories (job openings, technology detections, news events, business connections,... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
PredictLeads

# PredictLeads

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://predictleads.com](https://predictleads.com) · entry id 05-predictleads · source 05-signals-intent-abm.md line 493

**What it does**
Aggregates five signal categories (job openings, technology detections, news events, business connections, firmographics) across 129M companies in 195 countries by scraping public web sources - company sites, job boards, DNS/HTML/JS technology footprints, news.

**AI features, separated from automation with an AI label on it**
Primarily data aggregation and rules-based signal detection (technology fingerprinting via HTML/DNS signatures, keyword-matched job posting parsing) - no core ML/LLM claimed for the underlying detection. The MCP server is an LLM-agent interface layer over existing structured data, not a new AI capability.

**RevOps role**
Data layer/signal feed, typically consumed via API into a CRM, enrichment pipeline, or scoring model rather than used as a standalone UI tool.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (same API key/token used for REST API calls, per vendor blog)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.predictleads.com/](https://mcp.predictleads.com/)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.predictleads.com/

- [https://mcp.predictleads.com/](https://mcp.predictleads.com/)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited)

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Scrape job postings](../jobs/scrape-job-postings.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://predictleads.com/](https://predictleads.com/)
- [https://predictleads.com/blog/company-intelligence-api-gtm-teams/](https://predictleads.com/blog/company-intelligence-api-gtm-teams/)
- [https://blog.predictleads.com/2026/05/13/technographic-data-api-for-b2b-enrichment](https://blog.predictleads.com/2026/05/13/technographic-data-api-for-b2b-enrichment)

3 source URLs. Raw sources field, verbatim:

https://predictleads.com/, https://predictleads.com/blog/company-intelligence-api-gtm-teams/, https://blog.predictleads.com/2026/05/13/technographic-data-api-for-b2b-enrichment

**Notes, verbatim from the file**
Free tier confirmed - "sign up and get 100 free API requests/month," paid plans beyond that referenced but not itemized on the pages checked. One of the more solo-operator-friendly tools in this category - free tier plus a documented MCP with simple API-key auth.

**Provenance**

- **Entry id**: 05-predictleads

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 493

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
