# Weezly: MCP server status, API access gate and what it does

> AI sales-video plus scheduling platform - record once, AI generates many personalized variants with cloned... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Weezly

# Weezly

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [weezly.com](https://weezly.com) · entry id 08-weezly · source 08-video-prospecting.md line 223

**What it does**
AI sales-video plus scheduling platform - record once, AI generates many personalized variants with cloned voice/face claimed, and each video carries an integrated meeting-booking page; aimed at lead-gen agencies and SDR teams.

**AI features, separated from automation with an AI label on it**
Vendor claims both voice AND face cloning for bulk personalization ("thousands of customized sales videos with cloned voice and face") - a more aggressive claim than most peers in this file. Not independently verified beyond the vendor site and directory listings.

**RevOps role**
Video-plus-scheduling hybrid - bundles a meeting-booking CTA directly into the personalized video (vendor claims +38% more meetings booked vs. video alone, not independently verified).

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Zapier-mediated connection.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://zapier.com/mcp/weezly](https://zapier.com/mcp/weezly)Probed**: 2026-09-03, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://zapier.com/mcp/weezly (Zapier-hosted; very limited scope confirmed - only scheduling webhook actions such as "Invitee Created"/"Invitee Canceled" were found, not video or campaign actions)

- [https://zapier.com/mcp/weezly](https://zapier.com/mcp/weezly)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (custom integrations and API access are an Ultra-tier exclusive at a published $2,899/mo; the $39/mo Growth and $999/mo Agency tiers do not include it, so the price is public but far above solo-operator range)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)
- [Book a meeting](../jobs/book-a-meeting.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://weezly.com/](https://weezly.com/)
- [https://weezly.com/automated-sales-videos/](https://weezly.com/automated-sales-videos/)
- [https://weezly.com/product/](https://weezly.com/product/)
- [https://zapier.com/mcp/weezly](https://zapier.com/mcp/weezly)
- [https://weezly.com/pricing](https://weezly.com/pricing)

5 source URLs. Raw sources field, verbatim:

https://weezly.com/, https://weezly.com/automated-sales-videos/, https://weezly.com/product/, https://zapier.com/mcp/weezly, https://weezly.com/pricing

**Notes, verbatim from the file**
Real and currently operating (active Chrome Web Store listing, YouTube channel, live trial signup), but MCP coverage found is thin and scheduling-only, not video/campaign functionality. [api_gate 2026-08-25] Reclassified unknown -> paid from the vendor's own page (https://weezly.com/pricing): custom integrations and API access are an Ultra-tier exclusive at a published $2,899/mo; the $39/mo Growth and $999/mo Agency tiers do not include it, so the price is public but far above solo-operator range.

**Provenance**

- **Entry id**: 08-weezly

- **Source file**: 08-video-prospecting.md

- **Source line**: 223

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
