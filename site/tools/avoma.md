# Avoma: MCP server status, API access gate and what it does

> AI meeting platform combining scheduling, note-taking, and conversation intelligence (deal insights,... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Avoma

# Avoma

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [avoma.com](https://avoma.com) · entry id 03-avoma · source 03-conversation-intel.md line 220

**What it does**
AI meeting platform combining scheduling, note-taking, and conversation intelligence (deal insights, coaching) for sales teams.

**AI features, separated from automation with an AI label on it**
AI-generated summaries, conversation insights and key-topic extraction, deal-insight extraction feeding forecasts.

**RevOps role**
Combined scheduling-plus-conversation-intelligence layer; a solo operator needs a paid Organization-tier seat to reach the API/MCP.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: API key pair (CLIENT_KEY:CLIENT_SECRET) generated at Settings → Organization → Developer.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://help.avoma.com/admins-add-avoma-mcp-connector-in-claude](https://help.avoma.com/admins-add-avoma-mcp-connector-in-claude)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://help.avoma.com/admins-add-avoma-mcp-connector-in-claude (redirect correction 2026-08-28: the address previously recorded here, help.avoma.com/avoma-mcp-server-user-guide, 301s to this one through one intermediate hop, and this one returns 200. Full API reference at dev.avoma.com); works with Claude Desktop only as of this research, though other MCP clients are "being considered" per the vendor.

- [https://help.avoma.com/admins-add-avoma-mcp-connector-in-claude](https://help.avoma.com/admins-add-avoma-mcp-connector-in-claude)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. No permanent free tier - only a 14-day trial. API access requires the Organization plan ($29/user/mo annual and up); the entry Startup plan does not include it.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Book a meeting](../jobs/book-a-meeting.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://help.avoma.com/admins-add-avoma-mcp-connector-in-claude](https://help.avoma.com/admins-add-avoma-mcp-connector-in-claude)
- [https://www.avoma.com/blog/avoma-mcp-server](https://www.avoma.com/blog/avoma-mcp-server)
- [https://help.avoma.com/api-documentation](https://help.avoma.com/api-documentation)
- [https://www.avoma.com/pricing](https://www.avoma.com/pricing)

4 source URLs. Raw sources field, verbatim:

https://help.avoma.com/admins-add-avoma-mcp-connector-in-claude, https://www.avoma.com/blog/avoma-mcp-server, https://help.avoma.com/api-documentation, https://www.avoma.com/pricing

**Notes, verbatim from the file**
None.

**Provenance**

- **Entry id**: 03-avoma

- **Source file**: 03-conversation-intel.md

- **Source line**: 220

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
