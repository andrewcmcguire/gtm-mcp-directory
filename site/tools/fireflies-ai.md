# Fireflies.ai: MCP server status, API access gate and what it does

> Records and transcribes meetings and exposes the data through an open GraphQL API and an in-app AI assistant... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Fireflies.ai

# Fireflies.ai

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [fireflies.ai](https://fireflies.ai) · entry id 03-fireflies-ai · source 03-conversation-intel.md line 87

**What it does**
Records and transcribes meetings and exposes the data through an open GraphQL API and an in-app AI assistant ("AskFred") for summaries, search, and CRM writeback.

**AI features, separated from automation with an AI label on it**
Meeting summarization, AskFred conversational Q&A over transcript history, action-item extraction. "AI credits" gate some advanced AI actions even on paid plans; core transcription is ASR/automation.

**RevOps role**
Low-friction, developer-accessible conversation-data layer - the clearest solo-operator-friendly option among the recording-based tools.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (Google/Microsoft, recommended) or manual API key for Claude Desktop and other MCP clients.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol (server endpoint https://api.fireflies.ai/mcp)

- [https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol](https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol)
- [https://api.fireflies.ai/mcp](https://api.fireflies.ai/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (probable, not fully confirmed). The GraphQL API key is generated from Account → Integrations with no plan restriction stated in Fireflies' own quickstart docs, and multiple secondary sources report API access on every tier including free - but no primary Fireflies source explicitly states "the free tier includes API access," so treat as probable rather than certain.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Search across recorded calls](../jobs/search-call-library.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://docs.fireflies.ai/getting-started/introduction](https://docs.fireflies.ai/getting-started/introduction)
- [https://docs.fireflies.ai/getting-started/quickstart](https://docs.fireflies.ai/getting-started/quickstart)
- [https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol](https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol)
- [https://guide.fireflies.ai/articles/3734844560-learn-about-the-fireflies-pricing-plans](https://guide.fireflies.ai/articles/3734844560-learn-about-the-fireflies-pricing-plans)

4 source URLs. Raw sources field, verbatim:

https://docs.fireflies.ai/getting-started/introduction, https://docs.fireflies.ai/getting-started/quickstart, https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol, https://guide.fireflies.ai/articles/3734844560-learn-about-the-fireflies-pricing-plans

**Notes, verbatim from the file**
This is the Gong-vs-Fireflies contrast the directory is built to surface: an open, self-serve GraphQL API plus an official MCP server, versus Gong's sales-gated everything.

**Provenance**

- **Entry id**: 03-fireflies-ai

- **Source file**: 03-conversation-intel.md

- **Source line**: 87

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
