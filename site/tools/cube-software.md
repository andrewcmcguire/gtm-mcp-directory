# Cube Software: MCP server status, API access gate and what it does

> Spreadsheet-native FP&A planning and reporting platform for finance teams; revenue-scenario modeling is one... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Forecasting & Revenue](../categories/forecasting-revenue.md) /
Cube Software

# Cube Software

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Forecasting & Revenue](../categories/forecasting-revenue.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [cubesoftware.com](https://cubesoftware.com) · entry id 12-cube-software · source 12-forecasting-revenue.md line 207

**What it does**
Spreadsheet-native FP&A planning and reporting platform for finance teams; revenue-scenario modeling is one supported use case rather than a dedicated CRM-native sales-forecasting product.

**AI features, separated from automation with an AI label on it**
Markets an "Agentic Finance Layer" and AI agents included on every tier, covering budget narratives, variance/actuals-vs-forecast analysis, and "three revenue scenarios" modeling - vendor-described, not independently verified against a specific model architecture.

**RevOps role**
FP&A-adjacent planning layer, included here (like Vareto) because revenue-scenario modeling is one of its supported use cases, not because it is a CRM-native pipeline-forecasting specialist.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - no manual API key management.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-08-25, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.cubesoftware.com/mcp ; docs: https://help.cubesoftware.com/hc/en-us/articles/45569561283092-Connect-Cube-to-AI-Apps-via-MCP-Server

- [https://www.cubesoftware.com/mcp](https://www.cubesoftware.com/mcp)
- [https://help.cubesoftware.com/hc/en-us/articles/45569561283092-Connect-Cube-to-AI-Apps-via-MCP-Server](https://help.cubesoftware.com/hc/en-us/articles/45569561283092-Connect-Cube-to-AI-Apps-via-MCP-Server)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. MCP is included on Silver and Gold tiers (available as a paid add-on on the entry Bronze tier); no free tier or self-serve signup - all pricing is quote-only ("Get a quote").

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Model a revenue plan](../jobs/model-revenue-plan.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.cubesoftware.com/mcp](https://www.cubesoftware.com/mcp)
- [https://www.cubesoftware.com/pricing](https://www.cubesoftware.com/pricing)
- [https://help.cubesoftware.com/hc/en-us/articles/45569561283092-Connect-Cube-to-AI-Apps-via-MCP-Server](https://help.cubesoftware.com/hc/en-us/articles/45569561283092-Connect-Cube-to-AI-Apps-via-MCP-Server)
- [https://www.pulsemcp.com/servers?q=cube](https://www.pulsemcp.com/servers?q=cube)

4 source URLs. Raw sources field, verbatim:

https://www.cubesoftware.com/mcp, https://www.cubesoftware.com/pricing, https://help.cubesoftware.com/hc/en-us/articles/45569561283092-Connect-Cube-to-AI-Apps-via-MCP-Server, https://www.pulsemcp.com/servers?q=cube

**Notes, verbatim from the file**
A separate community MCP server (github.com/isaacwasserman/mcp_cube_server) exists for "Cube" the open-source semantic-layer/BI engine (cube.dev) - a different, unrelated product from Cube Software the FP&A vendor. Do not conflate the two when searching "Cube MCP."

**Provenance**

- **Entry id**: 12-cube-software

- **Source file**: 12-forecasting-revenue.md

- **Source line**: 207

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
