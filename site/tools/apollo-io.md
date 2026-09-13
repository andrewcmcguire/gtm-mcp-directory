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
- **Docs URL**: [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/apolloio/apollo-mcp-plugin

- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)

**What this server exposes**

- **Tools named**: 20
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-12
- **Repo read**: apolloio/apollo-mcp-plugin
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **Endpoint** `https://mcp.apollo.io/mcp` evidence: in a README table · calling it reads

- **Need** Where to go evidence: in a README table · calling it reads

- **Path** Purpose evidence: in a README table · calling it reads

- **Skill** What it does evidence: in a README table · calling it reads

- **Symptom** What to check evidence: in a README table · calling it reads

- **Transport** Streamable HTTP evidence: in a README table · calling it reads

- **Version** `0.1.1` evidence: in a README table · calling it reads

- **apollo_analytics_sync_report** Retrieve sales analytics metrics and breakdowns. evidence: in a README table · calling it reads

- **apollo_contacts_create** Create a contact in the Apollo workspace. evidence: in a README table · calling it writes

- **apollo_email_accounts_index** List connected email/sending accounts. evidence: in a README table · calling it reads

- **apollo_emailer_campaigns_add_contact_ids** Add contacts to an outreach sequence. evidence: in a README table · calling it writes

- **apollo_emailer_campaigns_search** Find outreach sequences by name. evidence: in a README table · calling it reads

- **apollo_mixed_companies_search** Search Apollo's organization database by industry, size, location, and keywords. evidence: in a README table · calling it reads

- **apollo_mixed_people_api_search** Search Apollo's people database by title, seniority, location, and company filters. evidence: in a README table · calling it reads

- **apollo_organizations_bulk_enrich** Enrich multiple organizations in one call. evidence: in a README table · calling it reads

- **apollo_organizations_enrich** Enrich a single organization. evidence: in a README table · calling it reads

- **apollo_people_bulk_match** Match and enrich multiple people in one call. evidence: in a README table · calling it reads

- **apollo_people_match** Match and enrich a single person from available identifiers. evidence: in a README table · calling it reads

- **glama.json** Glama MCP directory metadata. evidence: in a README table · calling it reads

- **server.json** Official MCP Registry metadata (name, version, transport, endpoint). evidence: in a README table · calling it reads

119 of the 437 entries that record an official or community MCP server carry a harvested tool list. The other 318 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

604 of 934 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)

**On GitHub**

[github.com/apolloio](https://github.com/apolloio) tied to the vendor by rule 1, account website https://www.apollo.io has the vendor's domain, confidence strong

- **Public repositories**: 10, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-08-31

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [apollo-io-cli](https://github.com/apolloio/apollo-io-cli) | CLI | The Official Apollo.io CLI | 53 | 2026-08-31 | v2.1.0 |
| [claude-statusline](https://github.com/apolloio/claude-statusline) | other | | 1 | 2026-08-26 | |
| [homebrew-apollo-io-cli](https://github.com/apolloio/homebrew-apollo-io-cli) | CLI | Homebrew tap for apollo-io-cli | 1 | 2026-08-07 | |
| [apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) | MCP server | Connect Claude Code + Cowork to Apollo MCP via this plugin | 20 | 2026-07-20 | v0.1.1 |
| [n8n-nodes-apollo](https://github.com/apolloio/n8n-nodes-apollo) | plugin or integration | Official Apollo.io n8n community node for lead enrichment and organization enrichment | 1 | 2026-07-17 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

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

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 934 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
