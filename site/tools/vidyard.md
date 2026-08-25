# Vidyard: MCP server status, API access gate and what it does

> AI-powered video-selling platform for recording, personalizing (including AI-avatar-generated), and sending... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Vidyard

# Vidyard

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [vidyard.com](https://vidyard.com) · entry id 08-vidyard · source 08-video-prospecting.md line 14

**What it does**
AI-powered video-selling platform for recording, personalizing (including AI-avatar-generated), and sending trackable video messages to prospects via email, CRM, and sales-engagement sequences.

**AI features, separated from automation with an AI label on it**
Vendor states AI Avatars (train a digital avatar from ~90 seconds of footage, then generate personalized scripts using prospect name/company/insight data without re-recording) and a "Video Sales Agent" that auto-generates and sends personalized video on CRM/sequence triggers. Engagement analytics (view rate, watch time, CTA clicks) are plain tracking, not AI. None of the avatar/voice-quality or personalization-lift claims independently verified beyond vendor's own description.

**RevOps role**
Personalized video touchpoints inside outbound sequences (Salesloft, Outreach, Apollo) or CRM workflows (HubSpot, Salesforce), with engagement data synced back to CRM.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Not documented in technical detail on the viaSocket listing ("built-in authentication"). Vidyard's own Video Agent REST API (separate from any MCP) uses an admin API token requiring "Edit Integrations"/"Edit API tokens" account permissions.

- **Parsed URLs**: 1 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://viasocket.com/mcp/vidyard (third-party viaSocket connector; no vendor-published or GitHub/registry-listed dedicated server found on mcp.so, glama.ai, or pulsemcp.com)

- [https://viasocket.com/mcp/vidyard](https://viasocket.com/mcp/vidyard)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, with conflicting detail. Vidyard's own docs say the Video Agent API is available on Free/Starter/Teams/Enterprise but caps non-add-on accounts at 15 AI videos total; a secondary source (Claap) states general API access is Enterprise-only on Starter/Teams. Treat as paid at minimum, likely more for full access.

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

- [https://www.vidyard.com/](https://www.vidyard.com/)
- [https://www.vidyard.com/blog/ai-avatars-in-sales-and-marketing/](https://www.vidyard.com/blog/ai-avatars-in-sales-and-marketing/)
- [https://developer.vidyard.com/](https://developer.vidyard.com/)
- [https://knowledge.vidyard.com/hc/en-us/articles/42909331296411-Using-the-Vidyard-Video-Agent-API](https://knowledge.vidyard.com/hc/en-us/articles/42909331296411-Using-the-Vidyard-Video-Agent-API)
- [https://viasocket.com/mcp/vidyard](https://viasocket.com/mcp/vidyard)
- [https://www.claap.io/blog/vidyard-pricing](https://www.claap.io/blog/vidyard-pricing)

6 source URLs. Raw sources field, verbatim:

https://www.vidyard.com/, https://www.vidyard.com/blog/ai-avatars-in-sales-and-marketing/, https://developer.vidyard.com/, https://knowledge.vidyard.com/hc/en-us/articles/42909331296411-Using-the-Vidyard-Video-Agent-API, https://viasocket.com/mcp/vidyard, https://www.claap.io/blog/vidyard-pricing

**Notes, verbatim from the file**
The only MCP hit is a thin, low-detail third-party viaSocket connector - no dedicated GitHub repo or registry listing found. Treat "community" mcp_status here as low-confidence.

**Provenance**

- **Entry id**: 08-vidyard

- **Source file**: 08-video-prospecting.md

- **Source line**: 14

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
