# Fivetran: MCP server status, API access gate and what it does

> Managed ELT pipeline platform; for GTM purposes, the relevant piece is its... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Fivetran

# Fivetran

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [fivetran.com](https://fivetran.com) · entry id 06-fivetran · source 06-revops-infra.md line 345

**What it does**
Managed ELT pipeline platform; for GTM purposes, the relevant piece is its Salesforce/HubSpot/Marketo/Outreach/Salesloft/Gong/Zendesk connectors that land CRM and GTM-tool data in a warehouse, plus (post-Census) its "Activations" reverse-ETL product for pushing data back out to those same tools.

**AI features, separated from automation with an AI label on it**
Mostly plain data pipeline - the AI positioning is largely about being "AI-ready" infrastructure for downstream agents rather than AI inside the product itself. The one genuinely agentic piece is the official MCP server, which lets an AI assistant query/manage connections conversationally - that is real, not just marketing.

**RevOps role**
Core data-plumbing layer of a RevOps stack - lands CRM/marketing/sales-engagement data into the warehouse and, via Activations, pushes it back out so it can be modeled and reused across GTM tools.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: API key + API secret via env vars, generated from the Fivetran dashboard. Scoped permission tiers (read / read-write / read-write-delete) with a configurable disallowed-actions carve-out; confirms with the user before write/delete operations.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/fivetran/fivetran-mcp

- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the REST API is available on all Fivetran plans including the free trial; the Free plan is self-serve (500K MAR/mo for connections, 3,500 MAR for activations, 5,000 MMR for transformations, no payment info required).

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

**Jobs it can do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.fivetran.com/](https://www.fivetran.com/)
- [https://www.fivetran.com/pricing](https://www.fivetran.com/pricing)
- [https://fivetran.com/docs/activations](https://fivetran.com/docs/activations)
- [https://fivetran.com/docs/connectors/applications](https://fivetran.com/docs/connectors/applications)
- [https://fivetran.com/docs/rest-api](https://fivetran.com/docs/rest-api)
- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

6 source URLs. Raw sources field, verbatim:

https://www.fivetran.com/, https://www.fivetran.com/pricing, https://fivetran.com/docs/activations, https://fivetran.com/docs/connectors/applications, https://fivetran.com/docs/rest-api, https://github.com/fivetran/fivetran-mcp

**Notes, verbatim from the file**
Confirmed GTM-relevant connectors include Salesforce, HubSpot, Pipedrive, Copper, Close, Marketo, Pardot, Braze, Klaviyo, Outreach, Salesloft, Apollo, Reply.io, Zendesk, Intercom, Freshdesk, Help Scout, LinkedIn Ad Analytics, Google Ads, and Gong. See the Census entry above - that product now lives inside Fivetran as Activations.

**Provenance**

- **Entry id**: 06-fivetran

- **Source file**: 06-revops-infra.md

- **Source line**: 345

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
