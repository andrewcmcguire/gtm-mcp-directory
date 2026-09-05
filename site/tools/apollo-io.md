# Apollo.io: MCP server status, API access gate and what it does

> A combined B2B contact database (265M+ contacts) and sales engagement platform in one product - prospect... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Apollo.io

# Apollo.io

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [apollo.io](https://apollo.io) · entry id 01-apollo-io · source 01-data-enrichment.md line 27

**What it does**
A combined B2B contact database (265M+ contacts) and sales engagement platform in one product - prospect search/filtering, email and call sequencing, and contact/organization enrichment.

**AI features, separated from automation with an AI label on it**
An "AI Assistant" and "AI Research" tool (bundled into every tier including Free) summarize accounts and draft outreach copy; sequence automation is rules-based, not AI. The prospecting/search function itself is plain filtered database lookup dressed up alongside the AI-labeled writing/research add-ons.

**RevOps role**
Combined data + outbound engagement layer, often the SDR's primary daily tool for prospecting and sequencing, syncing results into the CRM

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (Apollo.io sign-in/authorization flow in the client)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/apolloio/apollo-mcp-plugin

- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)
- [https://docs.apollo.io/docs](https://docs.apollo.io/docs)
- [https://www.landbase.com/blog/apollo-pricing](https://www.landbase.com/blog/apollo-pricing)
- [https://hackingdemand.com/blog/apollo-io-pricing-2026](https://hackingdemand.com/blog/apollo-io-pricing-2026)
- [https://www.warmly.ai/p/blog/apollo-pricing](https://www.warmly.ai/p/blog/apollo-pricing)
- [https://docs.apollo.io/reference/people-enrichment](https://docs.apollo.io/reference/people-enrichment)

6 source URLs. Raw sources field, verbatim:

https://github.com/apolloio/apollo-mcp-plugin, https://docs.apollo.io/docs, https://www.landbase.com/blog/apollo-pricing, https://hackingdemand.com/blog/apollo-io-pricing-2026, https://www.warmly.ai/p/blog/apollo-pricing, https://docs.apollo.io/reference/people-enrichment

**Notes, verbatim from the file**
Free tier exists with a real (if limited) database and ~900 credits/year, rising to ~10,000 credits/month for accounts with a verified corporate email domain. Basic public API access is available to all paid customers; fuller API capability is gated to the Organization plan (~$119/user/month annual). Several unofficial community MCP servers also exist on GitHub (lkm1developer, edwardchoh, Inferensys, adamanz, others) alongside Apollo's own official plugin. 2026-09-03: vendor docs state the People Enrichment endpoint (POST /people/match) accepts first_name and last_name (or name) with organization_name or domain and returns linkedin_url, "The URL for the person's LinkedIn profile" (https://docs.apollo.io/reference/people-enrichment); MCP tool apollo_people_match is described as "Match and enrich a single person from available identifiers" (https://github.com/apolloio/apollo-mcp-plugin); the docs state credits are charged only if credit-consuming data is found, 1 credit for demographics or email plus 8 credits if a mobile phone is returned.

**Provenance**

- **Entry id**: 01-apollo-io

- **Source file**: 01-data-enrichment.md

- **Source line**: 27

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
