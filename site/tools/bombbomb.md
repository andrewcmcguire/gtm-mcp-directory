# BombBomb: MCP server status, API access gate and what it does

> Asynchronous video-messaging platform for sales, real estate, and CX teams to record and send personalized... Community MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
BombBomb

# BombBomb

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [bombbomb.com](https://bombbomb.com) · entry id 08-bombbomb · source 08-video-prospecting.md line 71

**What it does**
Asynchronous video-messaging platform for sales, real estate, and CX teams to record and send personalized one-to-one videos via email/text/CRM with open and watch tracking.

**AI features, separated from automation with an AI label on it**
Vendor states (Copilot add-on, Core+Copilot/Enterprise plans only) AI audio/noise cleanup, AI-suggested talking points/scripts, AI-generated titles/subject lines, AI summaries, smart team assignment, and a patented "fallback video" auto-send when a rep misses their assignment. Base Core plan (no Copilot) is plain recording/sending/tracking with no AI. None of the AI claims independently verified beyond vendor pages.

**RevOps role**
Outbound/relationship-nurture layer - personalized video touches inside email/CRM sequences, especially real estate and SMB sales.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Rides Zapier's own OAuth/API-key connection to BombBomb; not a native BombBomb MCP auth flow.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom)Probed**: 2026-09-03, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://zapier.com/mcp/bombbombcom (Zapier's generic MCP gateway exposing any Zapier-connected app, not a BombBomb-authored server; no dedicated repo found on GitHub, mcp.so, glama.ai, or pulsemcp.com)

- [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only. BombBomb has a public REST API (developer.bombbomb.com, SDKs for JS/Ruby/Go) but access is explicitly listed as an Enterprise-plan-only feature, not available on Core or Core+Copilot.

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

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://bombbomb.com/pricing/](https://bombbomb.com/pricing/)
- [https://bombbomb.com/copilot/](https://bombbomb.com/copilot/)
- [https://support.bombbomb.com/hc/en-us/articles/36078323159437-What-s-Included-in-My-Plan-Core-vs-Core-Copilot-vs-Enterprise](https://support.bombbomb.com/hc/en-us/articles/36078323159437-What-s-Included-in-My-Plan-Core-vs-Core-Copilot-vs-Enterprise)
- [https://developer.bombbomb.com/](https://developer.bombbomb.com/)
- [https://support.bombbomb.com/hc/en-us/articles/39269877765773-How-to-Get-Started-with-the-BombBomb-API](https://support.bombbomb.com/hc/en-us/articles/39269877765773-How-to-Get-Started-with-the-BombBomb-API)
- [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom)

6 source URLs. Raw sources field, verbatim:

https://bombbomb.com/pricing/, https://bombbomb.com/copilot/, https://support.bombbomb.com/hc/en-us/articles/36078323159437-What-s-Included-in-My-Plan-Core-vs-Core-Copilot-vs-Enterprise, https://developer.bombbomb.com/, https://support.bombbomb.com/hc/en-us/articles/39269877765773-How-to-Get-Started-with-the-BombBomb-API, https://zapier.com/mcp/bombbombcom

**Notes, verbatim from the file**
Pricing varies slightly by source (Core ~$36-42/user/mo, Core+Copilot ~$56-70/user/mo) - treat as approximate. Recent vendor material also refers to the product as "BombBomb Engage," suggesting a platform refresh/rebrand in progress.

**Provenance**

- **Entry id**: 08-bombbomb

- **Source file**: 08-video-prospecting.md

- **Source line**: 71

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
