# Super Send: MCP server status, API access gate and what it does

> Cold email sequencing platform providing dedicated, warmed sending infrastructure with adaptive pacing based... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Super Send

# Super Send

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [supersend.io](https://supersend.io) · entry id 02-super-send · source 02-engagement-outbound.md line 274

**What it does**
Cold email sequencing platform providing dedicated, warmed sending infrastructure with adaptive pacing based on live deliverability signals.

**AI features, separated from automation with an AI label on it**
"AI Bounce Analysis" categorizes send failures (bad address, server block, temporary failure) - genuinely ML-classification per vendor. "AI-categorized" inbox auto-sorts replies across many senders. Adaptive pacing/placement testing is described as signal-driven automation, not explicitly AI.

**RevOps role**
Dedicated sending-infrastructure layer for outbound email, positioned as an infrastructure/deliverability specialist rather than a full sequencing+CRM platform.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key, Streamable HTTP transport

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://docs.supersend.io/docs/mcp-server](https://docs.supersend.io/docs/mcp-server)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.supersend.io/docs/mcp-server (endpoint mcp.supersend.io)

- [https://docs.supersend.io/docs/mcp-server](https://docs.supersend.io/docs/mcp-server)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)
- [Check inbox placement](../jobs/check-inbox-placement.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.pulsemcp.com/servers/supersend](https://www.pulsemcp.com/servers/supersend)
- [https://supersend.io](https://supersend.io)

2 source URLs. Raw sources field, verbatim:

https://www.pulsemcp.com/servers/supersend, https://supersend.io

**Notes, verbatim from the file**
Vendor's own MCP docs state the MCP server is a paid service with no free tier. Smaller/lesser-known player than most others in this sweep, but has a real vendor-hosted, documented MCP server - more than several larger competitors (Klenty, Outplay, Mailshake, QuickMail) have.

**Provenance**

- **Entry id**: 02-super-send

- **Source file**: 02-engagement-outbound.md

- **Source line**: 274

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
