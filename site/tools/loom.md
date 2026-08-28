# Loom: MCP server status, API access gate and what it does

> Async video-messaging platform; in its sales use case, reps record personalized video messages with... Community MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Loom

# Loom

[Community MCP](../mcp/community.md)
[Free to start](../gates/free.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [loom.com](https://loom.com) · entry id 08-loom · source 08-video-prospecting.md line 33

**What it does**
Async video-messaging platform; in its sales use case, reps record personalized video messages with name/company variables, track prospect views, and embed CTAs/booking links directly in the video.

**AI features, separated from automation with an AI label on it**
Vendor states (Business+AI / Enterprise tiers only) AI-generated titles/summaries/auto-chapters, automatic filler-word/silence removal, an AI-drafted follow-up email companion, and transcription/captioning in 50+ languages (base transcription ships even on the free tier; the AI enrichment layer is gated). Variable-based name/company personalization, view tracking, and CTA embedding are plain templating/automation, not AI, despite being marketed alongside the AI features. Vendor's own 18% engagement-lift claim not independently verified.

**RevOps role**
Lower-overhead async video touch for individual AEs/SDRs/CSMs - follow-ups and lightweight prospecting rather than a managed outbound-campaign engine.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: karbassi/mcp-loom uses Loom's undocumented internal GraphQL API via a browser session cookie (connect.sid) manually extracted from a logged-in session - no official API key exists for this per the project's own README.

- **Parsed URLs**: 3 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/karbassi/mcp-loom (largest community implementation, ~58 tools against Loom's internal GraphQL API); smaller variants at https://github.com/m2ai-mcp-servers/loom-mcp and https://github.com/CaliLuke/loom-mcp

- [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom)
- [https://github.com/m2ai-mcp-servers/loom-mcp](https://github.com/m2ai-mcp-servers/loom-mcp)
- [https://github.com/CaliLuke/loom-mcp](https://github.com/CaliLuke/loom-mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (recordSDK and embedSDK are self-serve via a developer-portal account and Loom's own dev site says start building with recordSDK today for free; this is a record/embed SDK rather than a general REST API and no SDK pricing tiers are published)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/CaliLuke/loom-mcp](https://github.com/CaliLuke/loom-mcp)
- [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom)
- [https://github.com/m2ai-mcp-servers/loom-mcp](https://github.com/m2ai-mcp-servers/loom-mcp)

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.loom.com/use-case/sales](https://www.loom.com/use-case/sales)
- [https://www.loom.com/pricing](https://www.loom.com/pricing)
- [https://www.loom.com/sdk](https://www.loom.com/sdk)
- [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom)
- [https://jira.atlassian.com/browse/LOOM-690](https://jira.atlassian.com/browse/LOOM-690)
- [https://dev.loom.com/](https://dev.loom.com/)

6 source URLs. Raw sources field, verbatim:

https://www.loom.com/use-case/sales, https://www.loom.com/pricing, https://www.loom.com/sdk, https://github.com/karbassi/mcp-loom, https://jira.atlassian.com/browse/LOOM-690, https://dev.loom.com/

**Notes, verbatim from the file**
Loom's dominant real-world use case remains general screen-recording/async communication, not outbound sales specifically - this entry evaluates only the sales-messaging angle per research scope. Watch for name collisions: several "Loom MCP" search results (e.g. a PulseMCP listing, maxsloef/loom-mcp) belong to an unrelated text/prompt-exploration tool that also happens to be called "loom." [api_gate 2026-08-25] Reclassified unknown -> free from the vendor's own page (https://dev.loom.com/): recordSDK and embedSDK are self-serve via a developer-portal account and Loom's own dev site says start building with recordSDK today for free; this is a record/embed SDK rather than a general REST API and no SDK pricing tiers are published.

**Provenance**

- **Entry id**: 08-loom

- **Source file**: 08-video-prospecting.md

- **Source line**: 33

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
