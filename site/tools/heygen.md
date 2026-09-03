# HeyGen: MCP server status, API access gate and what it does

> AI avatar/video-generation platform with a documented sales-prospecting motion - batch-personalize one... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
HeyGen

# HeyGen

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [heygen.com](https://heygen.com) · entry id 08-heygen · source 08-video-prospecting.md line 147

**What it does**
AI avatar/video-generation platform with a documented sales-prospecting motion - batch-personalize one template into many prospect-specific versions (dynamic name/company/pain-point variables), with native HubSpot automation that generates and attaches a personalized video to a contact on lifecycle triggers (new lead, meeting booked, deal-stage change).

**AI features, separated from automation with an AI label on it**
Vendor states 200+ AI avatars, voice/spokesperson cloning, batch personalization at scale, 175+ language localization with lip-sync, and engagement analytics. Vendor blog cites a case study that Reply.io built an outbound motion on HeyGen and an agency generated 50,000+ personalized videos for AB InBev claiming up to 3x engagement - vendor-published/vendor-cited, not independently verified here.

**RevOps role**
Outbound/sequence-personalization layer plugging natively into HubSpot and, via Zapier/Make/n8n, into other CRMs.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - vendor states "connect your HeyGen account, no API key required"; generation draws down the premium credits already in the user's HeyGen plan rather than separate API billing.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.heygen.com/mcp/v1/](https://mcp.heygen.com/mcp/v1/)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.heygen.com/mcp/v1/ (docs: https://developers.heygen.com/mcp/overview; product page: https://www.heygen.com/model-context-protocol)

- [https://mcp.heygen.com/mcp/v1/](https://mcp.heygen.com/mcp/v1/)
- [https://developers.heygen.com/mcp/overview](https://developers.heygen.com/mcp/overview)
- [https://www.heygen.com/model-context-protocol](https://www.heygen.com/model-context-protocol)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, pay-as-you-go. Public REST API billed from a prepaid USD wallet per feature (e.g., roughly $0.05/sec for photo-avatar video, ~$0.000667/sec TTS, $1.00 per avatar-creation call); no free API tier found for developers, though a solo operator can start with a small prepaid balance.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.heygen.com/business/sales](https://www.heygen.com/business/sales)
- [https://www.heygen.com/integrations/hubspot](https://www.heygen.com/integrations/hubspot)
- [https://www.heygen.com/blog/best-ai-video-tools-sales-prospecting](https://www.heygen.com/blog/best-ai-video-tools-sales-prospecting)
- [https://developers.heygen.com/mcp/overview](https://developers.heygen.com/mcp/overview)
- [https://developers.heygen.com/docs/pricing](https://developers.heygen.com/docs/pricing)
- [https://www.heygen.com/model-context-protocol](https://www.heygen.com/model-context-protocol)

6 source URLs. Raw sources field, verbatim:

https://www.heygen.com/business/sales, https://www.heygen.com/integrations/hubspot, https://www.heygen.com/blog/best-ai-video-tools-sales-prospecting, https://developers.heygen.com/mcp/overview, https://developers.heygen.com/docs/pricing, https://www.heygen.com/model-context-protocol

**Notes, verbatim from the file**
Included despite defaulting to "generic AI-avatar platform" because it clears the "real sales-prospecting motion" bar set for this file: dedicated sales use-case page, native HubSpot lifecycle automation, and a named case study (Reply.io). Synthesia, researched alongside it, did not clear this bar - see Sweep notes.

**Provenance**

- **Entry id**: 08-heygen

- **Source file**: 08-video-prospecting.md

- **Source line**: 147

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
