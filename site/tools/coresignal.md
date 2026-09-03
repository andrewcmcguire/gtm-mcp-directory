# Coresignal: MCP server status, API access gate and what it does

> Sells structured B2B datasets and APIs (company, employee/people, job-posting records) scraped and normalized... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Coresignal

# Coresignal

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [coresignal.com](https://coresignal.com) · entry id 01-coresignal · source 01-data-enrichment.md line 407

**What it does**
Sells structured B2B datasets and APIs (company, employee/people, job-posting records) scraped and normalized from public and professional-network sources, delivered as bulk datasets or pay-per-call enrichment APIs.

**AI features, separated from automation with an AI label on it**
Uses ML for record matching, deduplication, and entity resolution across sources - this is data-cleaning automation, not generative AI, despite "AI-powered" framing on marketing pages.

**RevOps role**
Bulk data-layer feed for enrichment pipelines/warehouses - used to seed or backfill CRM/Clay-style tables rather than for one-off lookups.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.1 - per docs, the data key is fetched live with every request and never stored, allowing instant revocation

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://coresignal.com/mcp-server/](https://coresignal.com/mcp-server/)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://coresignal.com/mcp-server/

- [https://coresignal.com/mcp-server/](https://coresignal.com/mcp-server/)

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

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Scrape job postings](../jobs/scrape-job-postings.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://coresignal.com/mcp-server/](https://coresignal.com/mcp-server/)
- [https://docs.coresignal.com/pricing](https://docs.coresignal.com/pricing)
- [https://coresignal.com/pricing/](https://coresignal.com/pricing/)
- [https://docs.coresignal.com/employee-api/base-employee-api/endpoints/search-filters.md](https://docs.coresignal.com/employee-api/base-employee-api/endpoints/search-filters.md)

4 source URLs. Raw sources field, verbatim:

https://coresignal.com/mcp-server/, https://docs.coresignal.com/pricing, https://coresignal.com/pricing/, https://docs.coresignal.com/employee-api/base-employee-api/endpoints/search-filters.md

**Notes, verbatim from the file**
Self-serve API subscriptions start at $49/month (credit-based), with a 7-day free trial (2,000 credits); full bulk datasets start at $1,000; larger volumes require custom enterprise pricing. Credit costs vary by tier (Base/Clean = 1 credit/record, Multi-Source = 2 credits/record). 2026-09-03: vendor docs state the Base Employee API search filter endpoint (/cdapi/v2/employee_base/search/filter) filters by full_name and experience_company_name, and its example records carry a professional-network profile url field; the vendor's docs say professional network, not LinkedIn (https://docs.coresignal.com/employee-api/base-employee-api/endpoints/search-filters.md); no MCP tool name and no unit price are stated there.

**Provenance**

- **Entry id**: 01-coresignal

- **Source file**: 01-data-enrichment.md

- **Source line**: 407

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
