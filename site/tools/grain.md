# Grain: MCP server status, API access gate and what it does

> AI meeting notetaker that records and transcribes calls and builds a searchable, cross-meeting library synced... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Grain

# Grain

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [grain.com](https://grain.com) · entry id 03-grain · source 03-conversation-intel.md line 106

**What it does**
AI meeting notetaker that records and transcribes calls and builds a searchable, cross-meeting library synced to the CRM.

**AI features, separated from automation with an AI label on it**
Cross-meeting "Ask anything" Q&A over the meeting library, automatic action items/summaries. The official MCP tool list also exposes deal tools (list_open_deals, fetch_deal) and coaching-scorecard tools (list_coaching_feedback) gated to Business/Enterprise, implying deal-risk and coaching features exist beyond plain notetaking, though their depth wasn't independently verified from the marketing site alone.

**RevOps role**
Meeting-capture and AI-searchable knowledge layer with direct, official MCP access reachable on a paid Starter plan without enterprise sales engagement.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth via the native Claude integration, or manual server-URL setup for other MCP clients. Deal and coaching-feedback tools specifically require a Business or Enterprise plan.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-03, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developers.grain.com/mcp (server endpoint https://api.grain.com/_/mcp)

- [https://developers.grain.com/mcp](https://developers.grain.com/mcp)
- [https://api.grain.com/_/mcp](https://api.grain.com/_/mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. The Free plan has no API access; Personal API access (via a Personal Access Token) starts at the Starter plan, so a solo operator can reach it but must pay. Workspace-wide API access requires Business/Enterprise plus admin rights.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Search across recorded calls](../jobs/search-call-library.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developers.grain.com/mcp](https://developers.grain.com/mcp)
- [https://support.grain.com/en/articles/15507288-grain-api](https://support.grain.com/en/articles/15507288-grain-api)
- [https://grain.com/pricing](https://grain.com/pricing)

3 source URLs. Raw sources field, verbatim:

https://developers.grain.com/mcp, https://support.grain.com/en/articles/15507288-grain-api, https://grain.com/pricing

**Notes, verbatim from the file**
An unofficial third-party server (https://github.com/eadm/grain-mcp-server) also exists - prefer the official one.

**Provenance**

- **Entry id**: 03-grain

- **Source file**: 03-conversation-intel.md

- **Source line**: 106

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
