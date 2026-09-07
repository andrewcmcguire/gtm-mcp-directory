# Wistia: MCP server status, API access gate and what it does

> A video hosting and marketing platform for business (player, channels, webinars, analytics, lead capture)... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Wistia

# Wistia

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [wistia.com](https://wistia.com) · entry id 08-wistia · source 08-video-prospecting.md line 281

**What it does**
A video hosting and marketing platform for business (player, channels, webinars, analytics, lead capture) with a REST API; sales and marketing teams use it for hosted demo and follow-up video with per-viewer engagement data.

**AI features, separated from automation with an AI label on it**
Not the product's centre; the vendor markets analytics and lead-gen automation. The MCP server is a connectivity layer over the existing API (media, folders, channels, webinars, captions, customizations, tags, analytics, stats, sharing, remix and account toolsets), not an AI feature.

**RevOps role**
A hosted-video layer under sales follow-up and marketing; the MCP gives an agent read and write over media and viewer analytics, which is engagement signal, not video generation.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth or an access token as an Authorization Bearer header. The docs state "If you use an access token you need to add the Authorization: Bearer in your configuration." An optional toolsets query parameter (for example ?toolsets=media,analytics) restricts the exposed tools; "By default the server exposes every tool it has, which is a lot of them." The docs also state "Currently, the Wistia MCP server is only available to owners and managers of an account."

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.wistia.com/mcp/api (docs: https://docs.wistia.com/docs/mcp-server-guide; registry name io.github.wistia/wistia-api-mcp)

- [https://api.wistia.com/mcp/api](https://api.wistia.com/mcp/api)
- [https://docs.wistia.com/docs/mcp-server-guide](https://docs.wistia.com/docs/mcp-server-guide)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the pricing page lists Free at $0/month ("25 GB storage", "1 user only", "Wistia Branding"), Business $79/month, Business + Lead gen $329/month and Enterprise custom; the MCP guide says custom connectors work across Free, Pro, Max, Team and Enterprise plans, and the API docs authenticate with an account access token with no plan condition stated.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://docs.wistia.com/docs/mcp-server-guide](https://docs.wistia.com/docs/mcp-server-guide)
- [https://wistia.com/pricing](https://wistia.com/pricing)
- [https://docs.wistia.com/docs/making-api-requests](https://docs.wistia.com/docs/making-api-requests)
- [https://api.wistia.com/mcp/api](https://api.wistia.com/mcp/api)

4 source URLs. Raw sources field, verbatim:

https://docs.wistia.com/docs/mcp-server-guide, https://wistia.com/pricing, https://docs.wistia.com/docs/making-api-requests, https://api.wistia.com/mcp/api

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://api.wistia.com/mcp/api returned HTTP 401 with JSON reading "unauthorized"; the control POST to /zzz-not-a-route returned 403 with an empty body. The statuses differ, so the 401 is specific to the MCP route rather than a blanket wall, but the control did not return 404, so this is recorded as a live auth-gated server on the vendor's host with a weaker control than the standard 404. The plan names in the MCP guide (Free, Pro, Max, Team) do not match the plan names on the current pricing page (Free, Business, Business + Lead gen, Enterprise); the guide is older than the price list. Like Vidyard in this file, Wistia is a hosting platform with a sales use case, not a purpose-built prospecting-video tool, which keeps headline finding 6 in INDEX.md intact. 2026-09-07: https://api.wistia.com/mcp/api returned 401 to an MCP initialize POST (https://api.wistia.com/mcp/api).

**Provenance**

- **Entry id**: 08-wistia

- **Source file**: 08-video-prospecting.md

- **Source line**: 281

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
