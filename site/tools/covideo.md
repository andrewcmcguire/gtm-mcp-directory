# Covideo: MCP server status, API access gate and what it does

> Records/sends/tracks personalized video messages via email, SMS, and social with Outlook/Gmail add-ins and... MCP unknown, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Covideo

# Covideo

[MCP unknown](../mcp/unknown.md)
[Enterprise only](../gates/enterprise-only.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [covideo.com](https://covideo.com) · entry id 08-covideo · source 08-video-prospecting.md line 185

**What it does**
Records/sends/tracks personalized video messages via email, SMS, and social with Outlook/Gmail add-ins and CRM integrations; heavily used in automotive-dealership sales but marketed broadly for sales enablement.

**AI features, separated from automation with an AI label on it**
Vendor markets an "AI Suite": "Create" (AI-generated personalized videos/inventory showcases at scale), "Accelerate" (automated follow-up), "Enhance" (audio/video polish). Confirmation limited to the vendor's own site - no independent third-party technical review found.

**RevOps role**
Sales-enablement/dealer video messaging with tracking analytics (opens, watch %, viewer identity).

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: unknown. Covideo's developer portal (developer.covideo.com) returned HTTP 401 during this research (requires an authenticated account to view), so API/MCP auth details could not be independently confirmed. Support docs describe bearer-token REST auth generally, but no MCP-specific reference was found.

- **Parsed URLs**: 0 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (Covideo publishes no pricing at all - /pricing is a get-a-quote form and every plan requires sales - and /api returns No Access while the integrations page never mentions an API)

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.covideo.com/](https://www.covideo.com/)
- [https://www.covideo.com/sales-enablement-tools/](https://www.covideo.com/sales-enablement-tools/)
- [https://developer.covideo.com/](https://developer.covideo.com/)
- [https://support.covideo.com/en/collections/2472505-integrations](https://support.covideo.com/en/collections/2472505-integrations)
- [https://www.covideo.com/pricing/](https://www.covideo.com/pricing/)
- 401 on fetch - portal exists but gated

5 source URLs. Raw sources field, verbatim:

https://www.covideo.com/, https://www.covideo.com/sales-enablement-tools/, https://developer.covideo.com/ (401 on fetch - portal exists but gated), https://support.covideo.com/en/collections/2472505-integrations, https://www.covideo.com/pricing/

**Notes, verbatim from the file**
Confirmed actively operating in 2026 (current-year copyright, live dealership testimonials, active support). Long-running vendor (20+ years in business, per vendor claim). [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.covideo.com/pricing/): Covideo publishes no pricing at all - /pricing is a get-a-quote form and every plan requires sales - and /api returns No Access while the integrations page never mentions an API. 2026-09-02: re-checked covideo.com/llms.txt (served a marketing page, no MCP mention) and web search (hits are Coveo and Invideo, unrelated); the developer portal remains gated, so nothing new could be read. Kept unknown.

**Provenance**

- **Entry id**: 08-covideo

- **Source file**: 08-video-prospecting.md

- **Source line**: 185

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
