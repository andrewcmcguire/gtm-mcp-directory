# Fellow: MCP server status, API access gate and what it does

> A meeting assistant that records, transcribes and summarises calls, then turns them into action items and... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Fellow

# Fellow

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [fellow.ai](https://fellow.ai) · entry id 03-fellow · source 03-conversation-intel.md line 411

**What it does**
A meeting assistant that records, transcribes and summarises calls, then turns them into action items and decisions tied to the calendar event they came from.

**AI features, separated from automation with an AI label on it**
AI-generated meeting summaries, action-item extraction and talking points. The transcription and calendar sync are automation.

**RevOps role**
Meeting record and follow-up source that an agent can query directly instead of scraping the CRM activity log.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth, with OAuth 2.0 dynamic discovery supported.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://fellow.app/mcp](https://fellow.app/mcp)Probed**: 2026-08-25, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-08-25 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://fellow.app/mcp (docs: https://developers.fellow.ai/reference/mcp-server)

- [https://fellow.app/mcp](https://fellow.app/mcp)
- [https://developers.fellow.ai/reference/mcp-server](https://developers.fellow.ai/reference/mcp-server)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (API access is listed on Team at $7/user/mo annual and every tier above; the Free plan does not include it)

**API documentation**

[https://developers.fellow.ai/reference/mcp-server](https://developers.fellow.ai/reference/mcp-server)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://developers.fellow.ai/reference/mcp-server](https://developers.fellow.ai/reference/mcp-server)
- [https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server](https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server)
- [https://fellow.ai/blog/fellow-mcp-server/](https://fellow.ai/blog/fellow-mcp-server/)
- [https://fellow.ai/pricing](https://fellow.ai/pricing)

4 source URLs. Raw sources field, verbatim:

https://developers.fellow.ai/reference/mcp-server, https://help.fellow.ai/en/articles/12622641-fellow-s-mcp-server, https://fellow.ai/blog/fellow-mcp-server/, https://fellow.ai/pricing

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. ADMIN-GATED, which is a distinct gate from the usual pricing gate and worth naming: a workspace admin must enable "Allow users to create MCP connections" under Settings, Security before any individual user can connect at all. Access then inherits the connecting user's existing Fellow permissions. The vendor does not state which pricing plan is required, so api_gate is recorded as unknown rather than guessed. [api_gate 2026-08-25] Reclassified unknown -> paid from the vendor's own page (https://fellow.ai/pricing): API access is listed on Team at $7/user/mo annual and every tier above; the Free plan does not include it.

**Provenance**

- **Entry id**: 03-fellow

- **Source file**: 03-conversation-intel.md

- **Source line**: 411

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
