# Granola: MCP server status, API access gate and what it does

> General-purpose AI notetaker that generates enhanced meeting notes and summaries from a local desktop app. Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Granola

# Granola

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [granola.ai](https://granola.ai) · entry id 03-granola · source 03-conversation-intel.md line 296

**What it does**
General-purpose AI notetaker that generates enhanced meeting notes and summaries from a local desktop app.

**AI features, separated from automation with an AI label on it**
AI-enhanced note generation that blends your own typed notes with the transcript, plus meeting search. It is NOT a dedicated deal-scoring or CRM-writeback tool by design - it is horizontal, not sales-specific - though users can build sales workflows (e.g., drafting CRM notes from a sales call) on top of its MCP server.

**RevOps role**
Horizontal meeting-notes layer that a RevOps stack can wire into sales workflows via MCP, but it is not a conversation-intelligence product in the Gong/Chorus sense - no native deal scoring, no coaching scorecards.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - no manual API key required.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-03, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.pulsemcp.com/servers/granola (official server at https://mcp.granola.ai/mcp); also listed at https://mcpservers.org/servers/granola-mcp

- [https://www.pulsemcp.com/servers/granola](https://www.pulsemcp.com/servers/granola)
- [https://mcp.granola.ai/mcp](https://mcp.granola.ai/mcp)
- [https://mcpservers.org/servers/granola-mcp](https://mcpservers.org/servers/granola-mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (API access and MCP integration start on the Business plan at $14/user/mo; the $0 Basic plan has neither)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Bencockin/granola-mcp](https://github.com/Bencockin/granola-mcp)
- [https://github.com/chrisguillory/granola-mcp](https://github.com/chrisguillory/granola-mcp)

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Search across recorded calls](../jobs/search-call-library.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.pulsemcp.com/servers/granola](https://www.pulsemcp.com/servers/granola)
- [https://mcpservers.org/servers/granola-mcp](https://mcpservers.org/servers/granola-mcp)
- [https://github.com/chrisguillory/granola-mcp](https://github.com/chrisguillory/granola-mcp)
- [https://github.com/Bencockin/granola-mcp](https://github.com/Bencockin/granola-mcp)
- [https://www.granola.ai/pricing](https://www.granola.ai/pricing)

5 source URLs. Raw sources field, verbatim:

https://www.pulsemcp.com/servers/granola, https://mcpservers.org/servers/granola-mcp, https://github.com/chrisguillory/granola-mcp, https://github.com/Bencockin/granola-mcp, https://www.granola.ai/pricing

**Notes, verbatim from the file**
Included per the seed list, but flagged clearly: Granola is a horizontal notetaker with an official MCP server, not a sales-specific conversation-intelligence product - do not conflate it with Gong-class tools. [api_gate 2026-08-25] Reclassified unknown -> paid from the vendor's own page (https://www.granola.ai/pricing): API access and MCP integration start on the Business plan at $14/user/mo; the $0 Basic plan has neither.

**Provenance**

- **Entry id**: 03-granola

- **Source file**: 03-conversation-intel.md

- **Source line**: 296

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
