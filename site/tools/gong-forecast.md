# Gong Forecast: MCP server status, API access gate and what it does

> A licensed add-on module (separate from the base Gong Foundation license, with a lighter "Forecast... No MCP found, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Forecasting & Revenue](../categories/forecasting-revenue.md) /
Gong Forecast

# Gong Forecast

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Forecasting & Revenue](../categories/forecasting-revenue.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [gong.io](https://gong.io) · entry id 12-gong-forecast · source 12-forecasting-revenue.md line 131

**What it does**
A licensed add-on module (separate from the base Gong Foundation license, with a lighter "Forecast Essentials" tier bundled into Gong's Deal Execution package) that turns Gong's conversation-intelligence signals into AI deal-likelihood scores, risk indicators, forecast rollups, and forecast-analytics dashboards. See 03-conversation-intel.md for Gong's full platform entry (core product, general MCP server, enterprise-only API gate) - this entry covers only what's forecast-specific.

**AI features, separated from automation with an AI label on it**
AI Deal Likelihood/Revenue Predictor scoring using 300+ engagement/CRM signals; vendor claims "20% more precision than algorithms based on CRM data" (vendor-stated, not independently verified) because it draws on Gong's proprietary conversation-intelligence models rather than CRM fields alone. Risk indicators flag patterns like "buyer gone silent" or a single-threaded deal.

**RevOps role**
Forecast-rollup and deal-risk layer sitting on top of Gong's core conversation-intelligence product, competing directly with Clari and Kluster.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found (forecast-specific)

mcp_url, verbatim from the file:

none

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only, same gate as core Gong (see 03-conversation-intel.md). Gong's own Forecast/pipeline setup docs make no mention of API access for the Forecast module specifically.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://help.gong.io/docs/set-up-your-pipeline-view-and-begin-forecasting](https://help.gong.io/docs/set-up-your-pipeline-view-and-begin-forecasting)
- [https://www.gong.io/platform/revenue-forecasting-software](https://www.gong.io/platform/revenue-forecasting-software)
- [https://www.gong.io/sales-forecasting-software](https://www.gong.io/sales-forecasting-software)
- [https://www.pulsemcp.com/servers?q=gong](https://www.pulsemcp.com/servers?q=gong)

4 source URLs. Raw sources field, verbatim:

https://help.gong.io/docs/set-up-your-pipeline-view-and-begin-forecasting, https://www.gong.io/platform/revenue-forecasting-software, https://www.gong.io/sales-forecasting-software, https://www.pulsemcp.com/servers?q=gong

**Notes, verbatim from the file**
Checked for a Forecast-specific MCP distinct from Gong's general MCP server - none found. The community Gong MCP servers on PulseMCP (cedricziel/gong-mcp, JustinBeckwith/gongio-mcp, kenazk/gong-mcp) all wrap the general conversation-intelligence API (calls/transcripts); none expose Forecast-module data (deal-likelihood scores, rollups, risk indicators) as distinct tools. 2026-09-02: re-checked the official MCP registry for gong: io.github.JustinBeckwith/gongio-mcp and io.github.pipeworx-io/gong both wrap the general Gong API (calls, transcripts, users) with no forecast, deal-likelihood or pipeline tools. none-found (forecast-specific) stands.

**Provenance**

- **Entry id**: 12-gong-forecast

- **Source file**: 12-forecasting-revenue.md

- **Source line**: 131

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
