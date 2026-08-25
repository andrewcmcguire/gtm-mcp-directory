# Tavus: MCP server status, API access gate and what it does

> Developer platform for building real-time, two-way conversational AI video agents ("Conversational Video... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Tavus

# Tavus

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [tavus.io](https://tavus.io) · entry id 08-tavus · source 08-video-prospecting.md line 128

**What it does**
Developer platform for building real-time, two-way conversational AI video agents ("Conversational Video Interface") - positioned for GTM use cases like greeting website visitors and booking meetings, not primarily batch personalized-outbound video.

**AI features, separated from automation with an AI label on it**
Vendor states AI voice/face replicas ("Replica"), persona-driven real-time conversational agents, and a no-code agent builder ("PAL Maker"). This is a genuine real-time conversational-AI product per vendor's own architecture description (perception, understanding, voice, rendering components), not just a templated video swap - but capability claims are vendor-stated and not independently benchmarked here.

**RevOps role**
Conversational AI-agent layer for GTM (an AI rep that greets/qualifies a site visitor and books a meeting live) rather than a classic async 1:many personalized-outbound-video tool.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 browser-based flow; the exchange mints a per-user API key server-side, nothing stored in client config.

- **Parsed URLs**: 4 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.tavus.io/mcp (docs: https://docs.tavus.io/sections/agent-tools/mcp-server.md, https://docs.tavus.io/sections/agent-tools/mcp-tools-reference.md); community alternative at https://github.com/rakeshdavid/Tavus-MCP

- [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp)
- [https://docs.tavus.io/sections/agent-tools/mcp-server.md](https://docs.tavus.io/sections/agent-tools/mcp-server.md)
- [https://docs.tavus.io/sections/agent-tools/mcp-tools-reference.md](https://docs.tavus.io/sections/agent-tools/mcp-tools-reference.md)
- [https://github.com/rakeshdavid/Tavus-MCP](https://github.com/rakeshdavid/Tavus-MCP)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free tier available. Free plan includes 25 minutes of conversational video/month; Starter/solo-developer tier is $59/mo (100 min + 3 custom replicas); Growth $397/mo (1,250 min); Enterprise custom. Overage billed per-minute.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/rakeshdavid/Tavus-MCP](https://github.com/rakeshdavid/Tavus-MCP)

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.tavus.io/](https://www.tavus.io/)
- [https://www.tavus.io/pricing](https://www.tavus.io/pricing)
- [https://docs.tavus.io/llms.txt](https://docs.tavus.io/llms.txt)
- [https://docs.tavus.io/sections/agent-tools/mcp-server.md](https://docs.tavus.io/sections/agent-tools/mcp-server.md)
- [https://github.com/rakeshdavid/Tavus-MCP](https://github.com/rakeshdavid/Tavus-MCP)
- [https://coldiq.com/blog/tavus-video-prospecting](https://coldiq.com/blog/tavus-video-prospecting)

6 source URLs. Raw sources field, verbatim:

https://www.tavus.io/, https://www.tavus.io/pricing, https://docs.tavus.io/llms.txt, https://docs.tavus.io/sections/agent-tools/mcp-server.md, https://github.com/rakeshdavid/Tavus-MCP, https://coldiq.com/blog/tavus-video-prospecting

**Notes, verbatim from the file**
Third-party blogs (e.g. ColdIQ) frame Tavus as a "video prospecting" tool via its replica/clone capability, but Tavus's own current marketing emphasizes real-time conversational agents over the "record once, blast personalized clips" model most other entries in this file use - worth noting the mechanism differs from Vidyard/Sendspark/Potion even though the sales use case is real.

**Provenance**

- **Entry id**: 08-tavus

- **Source file**: 08-video-prospecting.md

- **Source line**: 128

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
