# Ebsta: MCP server status, API access gate and what it does

> Revenue-intelligence add-on for Salesforce/HubSpot that syncs email and calendar activity into the CRM and... No MCP found, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Forecasting & Revenue](../categories/forecasting-revenue.md) /
Ebsta

# Ebsta

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Forecasting & Revenue](../categories/forecasting-revenue.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [ebsta.com](https://ebsta.com) · entry id 12-ebsta · source 12-forecasting-revenue.md line 74

**What it does**
Revenue-intelligence add-on for Salesforce/HubSpot that syncs email and calendar activity into the CRM and layers on relationship scoring, conversation capture, and pipeline forecasting.

**AI features, separated from automation with an AI label on it**
Vendor makes strong outcome guarantees ("guarantees to achieve accurate forecasts to +/-10%," quota-attainment improvement within 6 months) but discloses no technical detail on the underlying scoring/forecasting methodology anywhere reviewed - treat as business-outcome marketing claims, not verified ML claims. Core "Relationship Intelligence" (activity/email/calendar capture) is workflow automation and data capture, not predictive modeling, despite the "Intelligence" branding.

**RevOps role**
CRM-data-hygiene plus relationship/forecast layer sitting on top of Salesforce/HubSpot - a lighter-weight add-on rather than a full-stack revenue platform.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

none

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (the pricing page shows get-a-quote buttons and a compare-plans section but no prices and no API mention on any tier; docs.ebsta.com does not resolve)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Write CRM records](../jobs/write-crm-records.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.ebsta.com](https://www.ebsta.com)
- [https://www.ebsta.com/pricing/](https://www.ebsta.com/pricing/)
- [https://www.xpay.sh/agent-ready-index/ebsta/](https://www.xpay.sh/agent-ready-index/ebsta/)

3 source URLs. Raw sources field, verbatim:

https://www.ebsta.com, https://www.ebsta.com/pricing/, https://www.xpay.sh/agent-ready-index/ebsta/

**Notes, verbatim from the file**
A third-party "Agent-Ready SaaS Index" (xpay.sh) references an "MCP Server Card" score for Ebsta, but this could not be confirmed as evidence of a real MCP server on direct fetch - it reads as a category label in that site's own scoring framework, not a real Ebsta MCP. Logged as none-found per the schema's URL-required law. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.ebsta.com/pricing/): the pricing page shows get-a-quote buttons and a compare-plans section but no prices and no API mention on any tier; docs.ebsta.com does not resolve.

**Provenance**

- **Entry id**: 12-ebsta

- **Source file**: 12-forecasting-revenue.md

- **Source line**: 74

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
