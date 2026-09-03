# Bonjoro: MCP server status, API access gate and what it does

> Personalized 1:1 and 1:many video-messaging platform triggered by CRM events (new signup, first purchase,... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Bonjoro

# Bonjoro

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [bonjoro.com](https://bonjoro.com) · entry id 08-bonjoro · source 08-video-prospecting.md line 204

**What it does**
Personalized 1:1 and 1:many video-messaging platform triggered by CRM events (new signup, first purchase, deal-stage change), used across sales and customer-success teams.

**AI features, separated from automation with an AI label on it**
Primarily a recording/workflow-automation tool rather than AI-generation-heavy - no evidence found of generative-AI video personalization (voice cloning, AI avatars); personalization is human-recorded and CRM-triggered, not machine-generated.

**RevOps role**
Personalized-video triggers embedded in CRM lifecycle stages - a sales/customer-success crossover tool (50,000+ businesses claimed by vendor).

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Rides a Zapier account connection (OAuth to Zapier, which holds the Bonjoro-side connection).

- **Parsed URLs**: 1 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://zapier.com/mcp/bonjoro (Zapier's generic MCP gateway; no vendor-published first-party server found)

- [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. REST API access is gated to the Grrrowth and Company/Enterprise plans ($79-399+/mo); Zapier/CRM integrations are available from the Free tier up, but the direct API is not.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.bonjoro.com/](https://www.bonjoro.com/)
- [https://www.bonjoro.com/teams/customer-success](https://www.bonjoro.com/teams/customer-success)
- [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro)
- [https://www.bonjoro.com/pricing](https://www.bonjoro.com/pricing)

4 source URLs. Raw sources field, verbatim:

https://www.bonjoro.com/, https://www.bonjoro.com/teams/customer-success, https://zapier.com/mcp/bonjoro, https://www.bonjoro.com/pricing

**Notes, verbatim from the file**
Well-established (founded 2017); confirmed real and currently active.

**Provenance**

- **Entry id**: 08-bonjoro

- **Source file**: 08-video-prospecting.md

- **Source line**: 204

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
