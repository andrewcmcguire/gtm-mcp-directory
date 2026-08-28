# Fathom: MCP server status, API access gate and what it does

> Free AI meeting recorder/notetaker that transcribes calls and generates summaries, action items, and CRM sync. Community MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Fathom

# Fathom

[Community MCP](../mcp/community.md)
[Free to start](../gates/free.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [fathom.video](https://fathom.video) · entry id 03-fathom · source 03-conversation-intel.md line 182

**What it does**
Free AI meeting recorder/notetaker that transcribes calls and generates summaries, action items, and CRM sync.

**AI features, separated from automation with an AI label on it**
AI-generated meeting summaries and highlights, action-item extraction; the free plan caps advanced AI summaries at the first 5 calls/month.

**RevOps role**
Low-friction meeting-capture layer, notable in this category for a genuinely open, no-paywall API.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Community servers authenticate with a Fathom API key (FATHOM_API_KEY environment variable).

- **Parsed URLs**: 3 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community (no official MCP found; three unofficial/community wrappers exist - see mcp_url)

mcp_url, verbatim from the file:

https://github.com/trevorwelch/fathom-video-mcp ; https://github.com/lukas-bekr/fathom-mcp ; https://github.com/druellan/Fathom-Simple-MCP (all explicitly labeled unofficial/community by their authors)

- [https://github.com/trevorwelch/fathom-video-mcp](https://github.com/trevorwelch/fathom-video-mcp)
- [https://github.com/lukas-bekr/fathom-mcp](https://github.com/lukas-bekr/fathom-mcp)
- [https://github.com/druellan/Fathom-Simple-MCP](https://github.com/druellan/Fathom-Simple-MCP)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free. API access is included on all plan tiers including Free, with public developer docs and a downloadable OpenAPI spec - you can generate a key and start calling the API without upgrading. No published enterprise-only API tier.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/druellan/Fathom-Simple-MCP](https://github.com/druellan/Fathom-Simple-MCP)
- [https://github.com/lukas-bekr/fathom-mcp](https://github.com/lukas-bekr/fathom-mcp)
- [https://github.com/trevorwelch/fathom-video-mcp](https://github.com/trevorwelch/fathom-video-mcp)

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://pipeline.zoominfo.com/sales/fathom-api-review](https://pipeline.zoominfo.com/sales/fathom-api-review)
- [https://www.fathom.ai/pricing](https://www.fathom.ai/pricing)
- [https://github.com/trevorwelch/fathom-video-mcp](https://github.com/trevorwelch/fathom-video-mcp)
- [https://github.com/lukas-bekr/fathom-mcp](https://github.com/lukas-bekr/fathom-mcp)

4 source URLs. Raw sources field, verbatim:

https://pipeline.zoominfo.com/sales/fathom-api-review, https://www.fathom.ai/pricing, https://github.com/trevorwelch/fathom-video-mcp, https://github.com/lukas-bekr/fathom-mcp

**Notes, verbatim from the file**
Another Fireflies-style contrast case: free API access, but no official MCP server yet - only community wrappers.

**Provenance**

- **Entry id**: 03-fathom

- **Source file**: 03-conversation-intel.md

- **Source line**: 182

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
