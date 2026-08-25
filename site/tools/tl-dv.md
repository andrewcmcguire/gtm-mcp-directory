# tl;dv: MCP server status, API access gate and what it does

> Records and transcribes Zoom, Google Meet, and Microsoft Teams calls, layering on sales coaching (playbook... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
tl;dv

# tl;dv

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [tldv.io](https://tldv.io) · entry id 03-tl-dv · source 03-conversation-intel.md line 201

**What it does**
Records and transcribes Zoom, Google Meet, and Microsoft Teams calls, layering on sales coaching (playbook monitoring, objection handling) at higher tiers.

**AI features, separated from automation with an AI label on it**
Multi-meeting AI speaker insights, sales playbook monitoring and coaching, AI objection handling, AI-generated notes/summaries.

**RevOps role**
Recording-plus-coaching layer with a genuinely reachable paid entry point ($18-29/mo) for a solo operator, unlike most enterprise-gated tools in this category.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: API key generated at Settings → Personal Settings → API keys.

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/tldv-public/tldv-mcp-server (npm package tldv-mcp) ; https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/

- [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server)
- [https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/](https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. The general API ships from the Pro plan ($18-29/mo); tl;dv's own MCP setup docs state you need a Business or Enterprise account specifically for the MCP server, since the free tier excludes API access entirely either way.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server)

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server)
- [https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/](https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/)
- [https://www.claap.io/blog/tl-dv-pricing](https://www.claap.io/blog/tl-dv-pricing)
- [https://salestools.club/apis/tldv](https://salestools.club/apis/tldv)

4 source URLs. Raw sources field, verbatim:

https://github.com/tldv-public/tldv-mcp-server, https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/, https://www.claap.io/blog/tl-dv-pricing, https://salestools.club/apis/tldv

**Notes, verbatim from the file**
None.

**Provenance**

- **Entry id**: 03-tl-dv

- **Source file**: 03-conversation-intel.md

- **Source line**: 201

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
