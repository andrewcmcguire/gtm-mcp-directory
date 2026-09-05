# Pipedrive: MCP server status, API access gate and what it does

> A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams. Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Pipedrive

# Pipedrive

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [pipedrive.com](https://pipedrive.com) · entry id 06-pipedrive · source 06-revops-infra.md line 79

**What it does**
A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams.

**AI features, separated from automation with an AI label on it**
Not independently characterized beyond the MCP layer in this research pass (marketing claims about a Pipedrive "Sales Assistant" were not verified against a primary source) - reported as unknown rather than repeated from memory. The MCP server itself is a connectivity feature, not an AI feature: it exposes CRM actions (search deals, create records, update contacts, schedule activities) to external AI assistants.

**RevOps role**
SMB/mid-market pipeline CRM; positions its MCP server as available to any plan tier, not gated behind enterprise, letting smaller teams connect AI assistants to live deal data without developer resources.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - "Connect in minutes through secure OAuth. No coding, no API development, no developer required." AI assistants can only see/edit what the logged-in Pipedrive user already has permission for; actions are logged for auditability.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.pipedrive.com/en/features/mcp-server](https://www.pipedrive.com/en/features/mcp-server)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.pipedrive.com/en/features/mcp-server

- [https://www.pipedrive.com/en/features/mcp-server](https://www.pipedrive.com/en/features/mcp-server)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (for MCP access) - Pipedrive states the MCP server is available on all plans at no additional charge, metered by a token allotment included per plan with extra tokens purchasable. General (non-MCP) API access terms were not independently re-verified in this pass.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Pipedrive (AI Sales Assistant / forecasting)

- **Category**: [Forecasting & Revenue](../categories/forecasting-revenue.md)

- **MCP status there**: No MCP found

- **Gate there**: Free to start

- **Source**: 12-forecasting-revenue.md line 150

- **Canonical page**: [Pipedrive](../tools/pipedrive.md)

What that listing says it does: Pipedrive's built-in AI-driven forecasting layer - not a separately branded "Insights" product, but the CRM's AI Sales Assistant plus probability-weighted pipeline forecasting math. See 06-revops-infra.md for Pipedrive's full CRM entry (general MCP server, OAuth, free-on-all-plans MCP access) - this entry covers only...

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.pipedrive.com/en/features/mcp-server](https://www.pipedrive.com/en/features/mcp-server)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 14 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://www.pipedrive.com/en/features/mcp-server

**Notes, verbatim from the file**
A community/self-hosted alternative exists (github.com/WillDent/pipedrive-mcp-server) but is unofficial and separate from Pipedrive's own native server.

**Provenance**

- **Entry id**: 06-pipedrive

- **Source file**: 06-revops-infra.md

- **Source line**: 79

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
