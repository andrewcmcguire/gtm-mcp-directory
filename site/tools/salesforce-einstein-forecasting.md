# Salesforce Einstein Forecasting: MCP server status, API access gate and what it does

> Sales Cloud's AI forecasting feature, analyzing past opportunities, account history, and activities plus rep... No MCP found, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Forecasting & Revenue](../categories/forecasting-revenue.md) /
Salesforce Einstein Forecasting

# Salesforce Einstein Forecasting

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Forecasting & Revenue](../categories/forecasting-revenue.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [salesforce.com](https://salesforce.com) · entry id 12-salesforce-einstein-forecasting · source 12-forecasting-revenue.md line 302

**What it does**
Sales Cloud's AI forecasting feature, analyzing past opportunities, account history, and activities plus rep win-rates to generate revenue predictions with confidence ranges. See 06-revops-infra.md for Salesforce's full platform entry (Agentforce, Hosted MCP Servers, enterprise-only MCP gate) - this entry covers only the forecasting-specific angle.

**AI features, separated from automation with an AI label on it**
Genuine ML forecasting - distinguishes between existing opportunities, newly created ones, and early closures, and surfaces the key factors influencing each prediction rather than a single black-box number.

**RevOps role**
Native forecasting layer inside Salesforce's core CRM, an alternative to bolting on a third-party forecasting tool for orgs already paying for Unlimited Edition or the Einstein add-on.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found (forecast-specific; general Salesforce MCP entry covered in 06-revops-infra.md - no forecasting-specific MCP tools or endpoints found distinct from that general server)

mcp_url, verbatim from the file:

none (forecast-specific)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only for this specific feature - Einstein Forecasting requires Sales Cloud Unlimited Edition or a Sales Cloud Einstein license add-on, on top of whatever gate applies to Salesforce's general API/MCP access.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://trailhead.salesforce.com/content/learn/modules/sales-forecasting/view-and-set-sales-forecasts](https://trailhead.salesforce.com/content/learn/modules/sales-forecasting/view-and-set-sales-forecasts)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 17 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://trailhead.salesforce.com/content/learn/modules/sales-forecasting/view-and-set-sales-forecasts

**Notes, verbatim from the file**
Cross-reference only - do not duplicate the full Salesforce/Agentforce entry already researched in 06-revops-infra.md.

**Provenance**

- **Entry id**: 12-salesforce-einstein-forecasting

- **Source file**: 12-forecasting-revenue.md

- **Source line**: 302

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
