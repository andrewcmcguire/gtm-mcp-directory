# RocketReach: MCP server status, API access gate and what it does

> A large contact/company lookup database queried by name, company domain, or LinkedIn profile to find work... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
RocketReach

# RocketReach

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [rocketreach.co](https://rocketreach.co) · entry id 01-rocketreach · source 01-data-enrichment.md line 388

**What it does**
A large contact/company lookup database queried by name, company domain, or LinkedIn profile to find work emails, direct dials, and mobile numbers, with bulk lookup and CRM/Salesforce sync.

**AI features, separated from automation with an AI label on it**
No real AI in the core lookup; it's database matching/aggregation across public and proprietary sources with a confidence score. "AI-powered" marketing language overstates what is fundamentally record matching, not a novel model.

**RevOps role**
Contact-level waterfall enrichment / email+phone finder, typically one step in a Clay-style or CRM-integrated outbound stack.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.1, browser-based; ties to your existing RocketReach account and shares its credit pool (no separate API key needed for the official connector)

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://rocketreach.co/resources/products/mcp/](https://rocketreach.co/resources/products/mcp/)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://rocketreach.co/resources/products/mcp/ (setup docs: https://docs.rocketreach.co/reference/quick-start)

- [https://rocketreach.co/resources/products/mcp/](https://rocketreach.co/resources/products/mcp/)
- [https://docs.rocketreach.co/reference/quick-start](https://docs.rocketreach.co/reference/quick-start)

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

- [https://github.com/Meerkats-Ai/rocketreach-mcp-server](https://github.com/Meerkats-Ai/rocketreach-mcp-server)

**Jobs it can do**

- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://rocketreach.co/resources/products/mcp/](https://rocketreach.co/resources/products/mcp/)
- [https://docs.rocketreach.co/reference/quick-start](https://docs.rocketreach.co/reference/quick-start)
- [https://github.com/Meerkats-Ai/rocketreach-mcp-server](https://github.com/Meerkats-Ai/rocketreach-mcp-server)
- [https://salesintel.io/blog/rocketreach-pricing-plans/](https://salesintel.io/blog/rocketreach-pricing-plans/)
- [https://docs.rocketreach.co/reference/people-lookup-api.md](https://docs.rocketreach.co/reference/people-lookup-api.md)

5 source URLs. Raw sources field, verbatim:

https://rocketreach.co/resources/products/mcp/, https://docs.rocketreach.co/reference/quick-start, https://github.com/Meerkats-Ai/rocketreach-mcp-server, https://salesintel.io/blog/rocketreach-pricing-plans/, https://docs.rocketreach.co/reference/people-lookup-api.md

**Notes, verbatim from the file**
MCP billing explicitly shares the REST API's account-level rate limit/credits - no separate MCP fee. Full API access is reported (via third-party pricing writeups, not RocketReach's own live price page) to require the Ultimate plan (~$2,099/yr); lower tiers may have limited/no API access. An unofficial community MCP (Meerkats-Ai/rocketreach-mcp-server) also exists alongside the official connector. 2026-09-03: vendor docs state the People Lookup API (GET /person/lookup) takes name ("Must specify along with current_employer") plus current_employer and returns linkedin_url and linkedin_url_active (https://docs.rocketreach.co/reference/people-lookup-api.md); the quick-start names an MCP tool person_lookup (https://docs.rocketreach.co/reference/quick-start); the docs state the endpoint consumes export credits, with no unit price stated.

**Provenance**

- **Entry id**: 01-rocketreach

- **Source file**: 01-data-enrichment.md

- **Source line**: 388

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
