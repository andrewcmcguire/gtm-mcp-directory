# Coresignal: MCP server status, API access gate and what it does

> Sells structured B2B datasets and APIs (company, employee/people, job-posting records) scraped and normalized... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Coresignal

# Coresignal

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

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

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://coresignal.com/mcp-server/](https://coresignal.com/mcp-server/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.coresignal.com/mcp/v2 ; https://coresignal.com/mcp-server/ ; repo https://github.com/Coresignal-com/coresignal-mcp

- [https://mcp.coresignal.com/mcp/v2](https://mcp.coresignal.com/mcp/v2)
- [https://coresignal.com/mcp-server/](https://coresignal.com/mcp-server/)
- [https://github.com/Coresignal-com/coresignal-mcp](https://github.com/Coresignal-com/coresignal-mcp)

**What this server exposes**

- **Tools named**: 6
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Repo read**: Coresignal-com/coresignal-mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **Action** Credits evidence: in a README table · calling it reads

- **artifact_read** Page rows back out of a delivered file evidence: in a README table · calling it reads

- **email_enrich** Get verified emails evidence: in the vendor docs · calling it reads

- **entity_fetch** Pull full profiles evidence: in the vendor docs · calling it reads

- **entity_fields** Explore available fields evidence: in the vendor docs · calling it reads

- **entity_search** Search in plain English; no query language needed evidence: in the vendor docs · calling it reads

119 of the 264 entries that record an official or community MCP server carry a harvested tool list. The other 145 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

400 of 514 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Coresignal-com/coresignal-mcp](https://github.com/Coresignal-com/coresignal-mcp)

**On GitHub**

[github.com/Coresignal-com](https://github.com/Coresignal-com) tied to the vendor by rule 1, account website https://coresignal.com/ has the vendor's domain, confidence strong

- **Public repositories**: 2, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-08-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [coresignal-mcp](https://github.com/Coresignal-com/coresignal-mcp) | MCP server | Coresignal MCP - fresh company, employee, and jobs records in real time | 2 | 2026-08-07 | |
| [n8n-nodes-coresignal-api](https://github.com/Coresignal-com/n8n-nodes-coresignal-api) | API client | | 0 | 2026-03-26 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Scrape job postings](../jobs/scrape-job-postings.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 514 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://coresignal.com/mcp-server/](https://coresignal.com/mcp-server/)
- [https://docs.coresignal.com/pricing](https://docs.coresignal.com/pricing)
- [https://coresignal.com/pricing/](https://coresignal.com/pricing/)
- [https://docs.coresignal.com/employee-api/base-employee-api/endpoints/search-filters.md](https://docs.coresignal.com/employee-api/base-employee-api/endpoints/search-filters.md)
- [https://github.com/Coresignal-com/coresignal-mcp](https://github.com/Coresignal-com/coresignal-mcp)
- [https://mcp.coresignal.com/mcp/v2](https://mcp.coresignal.com/mcp/v2)

6 source URLs. Raw sources field, verbatim:

https://coresignal.com/mcp-server/, https://docs.coresignal.com/pricing, https://coresignal.com/pricing/, https://docs.coresignal.com/employee-api/base-employee-api/endpoints/search-filters.md, https://github.com/Coresignal-com/coresignal-mcp, https://mcp.coresignal.com/mcp/v2

**Notes, verbatim from the file**
Self-serve API subscriptions start at $49/month (credit-based), with a 7-day free trial (2,000 credits); full bulk datasets start at $1,000; larger volumes require custom enterprise pricing. Credit costs vary by tier (Base/Clean = 1 credit/record, Multi-Source = 2 credits/record). 2026-09-03: vendor docs state the Base Employee API search filter endpoint (/cdapi/v2/employee_base/search/filter) filters by full_name and experience_company_name, and its example records carry a professional-network profile url field; the vendor's docs say professional network, not LinkedIn (https://docs.coresignal.com/employee-api/base-employee-api/endpoints/search-filters.md); no MCP tool name and no unit price are stated there. 2026-09-07: GitHub org Coresignal-com (homepage coresignal.com); README: "The official Model Context Protocol server for Coresignal" and names the endpoint https://mcp.coresignal.com/mcp/v2 (https://github.com/Coresignal-com/coresignal-mcp).

**Provenance**

- **Entry id**: 01-coresignal

- **Source file**: 01-data-enrichment.md

- **Source line**: 407

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
