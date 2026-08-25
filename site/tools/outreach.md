# Outreach: MCP server status, API access gate and what it does

> Sales engagement platform for building, running, and tracking multichannel outbound sequences (email, call,... Official MCP, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Outreach

# Outreach

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [outreach.io (site is mid-transition to outreach.ai)](https://outreach.io (site is mid-transition to outreach.ai)) · entry id 02-outreach · source 02-engagement-outbound.md line 7

**What it does**
Sales engagement platform for building, running, and tracking multichannel outbound sequences (email, call, social) and rep activity, tied into a CRM.

**AI features, separated from automation with an AI label on it**
Vendor markets "AI Agents" that act across the customer lifecycle, AI-assisted forecasting/pipeline projection, and real-time conversation intelligence (AI battle cards, objection handling, action-item detection during calls). None of the underlying model mechanics are disclosed publicly - these are vendor-stated capabilities, not independently verified.

**RevOps role**
Core outbound execution layer between prospecting/data tools and CRM - cadence orchestration, call/email logging, activity data feeding forecasting.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.1 with Dynamic Client Registration; also requires the org-level "Amplify" add-on to be enabled and admin-toggled - not available to every customer by default.

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.outreach.io/mcp/ ; overview at https://support.outreach.io/support/solutions/articles/159000425158-outreach-mcp-server-overview

- [https://api.outreach.io/mcp/](https://api.outreach.io/mcp/)
- [https://support.outreach.io/support/solutions/articles/159000425158-outreach-mcp-server-overview](https://support.outreach.io/support/solutions/articles/159000425158-outreach-mcp-server-overview)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

83 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://support.outreach.io/support/solutions/articles/159000425158-outreach-mcp-server-overview](https://support.outreach.io/support/solutions/articles/159000425158-outreach-mcp-server-overview)
- [https://support.outreach.io/support/solutions/articles/159000426361-where-are-the-outreach-development-portal-and-api-documentation-](https://support.outreach.io/support/solutions/articles/159000426361-where-are-the-outreach-development-portal-and-api-documentation-)
- [https://developers.outreach.io/](https://developers.outreach.io/)
- [https://www.outreach.ai/product](https://www.outreach.ai/product)

4 source URLs. Raw sources field, verbatim:

https://support.outreach.io/support/solutions/articles/159000425158-outreach-mcp-server-overview, https://support.outreach.io/support/solutions/articles/159000426361-where-are-the-outreach-development-portal-and-api-documentation-, https://developers.outreach.io/, https://www.outreach.ai/product

**Notes, verbatim from the file**
The official MCP server is gated behind the paid "Amplify" add-on plus admin enablement, not a free-for-all connector. Base API access requires requesting developer-portal access; no public self-serve pricing found, so api_gate is left unknown rather than assumed. Community/read-only alternatives also exist (github.com/ZLeventer/outreach-mcp-server, github.com/CDataSoftware/outreach.io-mcp-server-by-cdata).

**Provenance**

- **Entry id**: 02-outreach

- **Source file**: 02-engagement-outbound.md

- **Source line**: 7

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
