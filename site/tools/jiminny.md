# Jiminny: MCP server status, API access gate and what it does

> Records, transcribes, and scores sales calls, syncing action items and summaries into the CRM. Community MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Jiminny

# Jiminny

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [jiminny.com](https://jiminny.com) · entry id 03-jiminny · source 03-conversation-intel.md line 334

**What it does**
Records, transcribes, and scores sales calls, syncing action items and summaries into the CRM.

**AI features, separated from automation with an AI label on it**
AI-generated call summaries and action items, conversation scoring/coaching tools per product marketing - depth not independently verified in this research.

**RevOps role**
Mid-market call-recording and coaching layer with a documented but not fully transparent API surface.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Community server: JIMINNY_TOKEN API token. Zapier's hosted connector uses Zapier's own OAuth layer.

- **Parsed URLs**: 2 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp ; https://zapier.com/mcp/jiminny - both third-party; no official Jiminny-branded MCP announcement was found.

- [https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp](https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp)
- [https://zapier.com/mcp/jiminny](https://zapier.com/mcp/jiminny)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (no pricing page exists on any path and neither the site nor the integrations page mentions an API; the only route is contact-us)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://help.jiminny.com/en/articles/9527212-what-is-the-jiminny-api](https://help.jiminny.com/en/articles/9527212-what-is-the-jiminny-api)
- [https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp](https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp)
- [https://zapier.com/mcp/jiminny](https://zapier.com/mcp/jiminny)
- [https://apitracker.io/a/jiminny](https://apitracker.io/a/jiminny)
- [https://www.jiminny.com/](https://www.jiminny.com/)

5 source URLs. Raw sources field, verbatim:

https://help.jiminny.com/en/articles/9527212-what-is-the-jiminny-api, https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp, https://zapier.com/mcp/jiminny, https://apitracker.io/a/jiminny, https://www.jiminny.com/

**Notes, verbatim from the file**
Added as an expansion beyond the seed list - a second mid-market Gong/Chorus competitor worth tracking. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.jiminny.com/): no pricing page exists on any path and neither the site nor the integrations page mentions an API; the only route is contact-us.

**Provenance**

- **Entry id**: 03-jiminny

- **Source file**: 03-conversation-intel.md

- **Source line**: 334

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
