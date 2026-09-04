# Lusha: MCP server status, API access gate and what it does

> A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting... Official MCP, Free to start. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Lusha

# Lusha

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [lusha.com](https://lusha.com) · entry id 01-lusha · source 01-data-enrichment.md line 84

**What it does**
A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting platform, and bulk CSV/API enrichment for finding direct dials, emails, and company data.

**AI features, separated from automation with an AI label on it**
Automated lead-recommendation lists and an AI email-writing assistant sit on top of the core lookup product. The core "reveal a contact" function is a straightforward database lookup, not AI - the AI features are add-ons for prioritization and copywriting.

**RevOps role**
Contact-level enrichment/lookup source, commonly used as one provider inside a Clay-style waterfall, or directly via the browser extension for individual/manual prospecting

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (LUSHA_API_KEY)

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/lusha-oss/lusha-public-api-mcp](https://github.com/lusha-oss/lusha-public-api-mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/lusha-oss/lusha-public-api-mcp (also https://github.com/lusha-oss/lusha-mcp-plugin; docs: https://docs.lusha.com/mcp-docs)

- [https://github.com/lusha-oss/lusha-public-api-mcp](https://github.com/lusha-oss/lusha-public-api-mcp)
- [https://github.com/lusha-oss/lusha-mcp-plugin](https://github.com/lusha-oss/lusha-mcp-plugin)
- [https://docs.lusha.com/mcp-docs](https://docs.lusha.com/mcp-docs)

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

- [https://github.com/lusha-oss/lusha-mcp-plugin](https://github.com/lusha-oss/lusha-mcp-plugin)
- [https://github.com/lusha-oss/lusha-public-api-mcp](https://github.com/lusha-oss/lusha-public-api-mcp)

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/lusha-oss/lusha-public-api-mcp](https://github.com/lusha-oss/lusha-public-api-mcp)
- [https://docs.lusha.com/mcp-docs](https://docs.lusha.com/mcp-docs)
- [https://docs.lusha.com/user-guide/lushas-api/all-there-is-to-know-about-lushas-api](https://docs.lusha.com/user-guide/lushas-api/all-there-is-to-know-about-lushas-api)
- [https://www.vendr.com/marketplace/lusha](https://www.vendr.com/marketplace/lusha)
- [https://www.saleshandy.com/blog/lusha-pricing/](https://www.saleshandy.com/blog/lusha-pricing/)
- [https://docs.lusha.com/apis/openapi/person-api](https://docs.lusha.com/apis/openapi/person-api)

6 source URLs. Raw sources field, verbatim:

https://github.com/lusha-oss/lusha-public-api-mcp, https://docs.lusha.com/mcp-docs, https://docs.lusha.com/user-guide/lushas-api/all-there-is-to-know-about-lushas-api, https://www.vendr.com/marketplace/lusha, https://www.saleshandy.com/blog/lusha-pricing/, https://docs.lusha.com/apis/openapi/person-api

**Notes, verbatim from the file**
Per Lusha's own docs, every user gets an API key by default on every plan including Free, with rate limits scaling by tier (Free/Starter: 40 req/min, 100/day; Premium: 300/min, 18,000/day). This contradicts some third-party pricing blogs claiming Free/Starter have no API access - the official docs were treated as authoritative. Self-serve seat purchasing tops out at 5 seats; beyond that, a Scale plan requires a sales quote. 2026-09-03: vendor docs state the Search Contacts endpoint (POST /v3/contacts/search) looks up contacts by "firstName + lastName + companyName or companyDomain" and returns a non-PII preview that includes linkedinUrl (https://docs.lusha.com/apis/openapi/person-api); MCP tool contacts_search is described as "Enrich contact data using email, LinkedIn URL, or name + company" (https://docs.lusha.com/mcp-docs); the docs state it is charged per successful result via the api_search action, with no unit price stated.

**Provenance**

- **Entry id**: 01-lusha

- **Source file**: 01-data-enrichment.md

- **Source line**: 84

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
