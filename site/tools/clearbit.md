# Clearbit (now HubSpot Breeze Intelligence): MCP server status, API access gate and what it does

> A firmographic/contact data lookup service that fills in company and contact fields (size, industry, revenue,... No MCP found, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Clearbit (now HubSpot Breeze Intelligence)

# Clearbit (now HubSpot Breeze Intelligence)

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.hubspot.com/products/breeze/intelligence](https://www.hubspot.com/products/breeze/intelligence) · entry id 01-clearbit · source 01-data-enrichment.md line 103

**What it does**
A firmographic/contact data lookup service that fills in company and contact fields (size, industry, revenue, location, social profiles, etc.) from a third-party data pool; formerly sold as a standalone API, now sold only as an add-on inside the HubSpot CRM.

**AI features, separated from automation with an AI label on it**
Marketed as an "AI" feature of HubSpot's Breeze suite, but the core function is database lookup/matching against pre-aggregated firmographic and web data (i.e., automated enrichment, not generative or predictive AI). No independent evidence of model-based inference beyond standard matching/scoring.

**RevOps role**
Contact/company record enrichment and lead scoring input inside HubSpot CRM; no longer usable as a standalone enrichment layer outside HubSpot.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: not recorded

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

The mcp_url field is empty on this entry. 17 of 293 entries are.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.lead411.com/clearbit-pricing/](https://www.lead411.com/clearbit-pricing/)
- [https://derrick-app.com/en/pricing-clearbit-2/](https://derrick-app.com/en/pricing-clearbit-2/)
- [https://www.eesel.ai/blog/how-much-is-breeze-intelligence](https://www.eesel.ai/blog/how-much-is-breeze-intelligence)
- [https://community.hubspot.com/t5/Clearbit/Breeze-Intelligence/m-p/1143555](https://community.hubspot.com/t5/Clearbit/Breeze-Intelligence/m-p/1143555)
- [https://skrapp.io/blog/clearbit/](https://skrapp.io/blog/clearbit/)
- [https://salesmotion.io/blog/clearbit-alternatives-hubspot-acquisition](https://salesmotion.io/blog/clearbit-alternatives-hubspot-acquisition)
- [https://developers.hubspot.com/mcp](https://developers.hubspot.com/mcp)

7 source URLs. Raw sources field, verbatim:

https://www.lead411.com/clearbit-pricing/, https://derrick-app.com/en/pricing-clearbit-2/, https://www.eesel.ai/blog/how-much-is-breeze-intelligence, https://community.hubspot.com/t5/Clearbit/Breeze-Intelligence/m-p/1143555, https://skrapp.io/blog/clearbit/, https://salesmotion.io/blog/clearbit-alternatives-hubspot-acquisition, https://developers.hubspot.com/mcp

**Notes, verbatim from the file**
HubSpot acquired Clearbit (completed ~Dec 2024) and folded it into "Breeze Intelligence." The standalone Clearbit Enrichment API has been deprecated/closed to new customers - there is no independent API signup anymore. Access requires a paid HubSpot subscription (min. reported cost ~$75/mo combining HubSpot Starter + credits) plus HubSpot Credits for enrichment (~$0.01/credit per multiple sources); large-scale external use requires an Enterprise HubSpot contract negotiated with sales. No phone-number enrichment. No MCP server found for either legacy Clearbit or Breeze Intelligence - only generic third-party HubSpot-CRM MCP servers (unrelated to enrichment) were found. 2026-09-02: re-checked hubspot.com/llms.txt (no MCP mention) and HubSpot's MCP docs at developers.hubspot.com/mcp (endpoint mcp.hubspot.com, OAuth 2.0); those docs describe CRM access and make no mention of Breeze Intelligence, Clearbit or enrichment, so no MCP server found for this product.

**Provenance**

- **Entry id**: 01-clearbit

- **Source file**: 01-data-enrichment.md

- **Source line**: 103

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
