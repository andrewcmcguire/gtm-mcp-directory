# Circleback: MCP server status, API access gate and what it does

> AI meeting notetaker that produces structured notes, action items and insights from calls, and connects email... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Circleback

# Circleback

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [circleback.ai](https://circleback.ai) · entry id 03-circleback · source 03-conversation-intel.md line 451

**What it does**
AI meeting notetaker that produces structured notes, action items and insights from calls, and connects email threads to the same relationship record.

**AI features, separated from automation with an AI label on it**
Structured note and action-item extraction, meeting insights, and automatic profile and company entity resolution across meetings and connected email. The email-plus-meeting relationship graph is the differentiator versus transcript-only tools.

**RevOps role**
Meeting-capture and relationship-context layer for a small GTM team, uniquely readable by an agent because MCP appears to be the only programmatic surface.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth with dynamic client registration, compliant with the authenticated remote MCP spec. Centrally hosted and managed by Circleback.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://circleback.ai/api/mcp](https://circleback.ai/api/mcp)Probed**: 2026-08-25, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-08-25 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://circleback.ai/api/mcp (docs: https://support.circleback.ai/en/articles/13249081-circleback-mcp; guide: https://circleback.ai/blog/how-to-connect-circleback-mcp)

- [https://circleback.ai/api/mcp](https://circleback.ai/api/mcp)
- [https://support.circleback.ai/en/articles/13249081-circleback-mcp](https://support.circleback.ai/en/articles/13249081-circleback-mcp)
- [https://circleback.ai/blog/how-to-connect-circleback-mcp](https://circleback.ai/blog/how-to-connect-circleback-mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://support.circleback.ai/en/articles/13249081-circleback-mcp](https://support.circleback.ai/en/articles/13249081-circleback-mcp)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Summarize a meeting](../jobs/summarize-meeting.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://support.circleback.ai/en/articles/13249081-circleback-mcp](https://support.circleback.ai/en/articles/13249081-circleback-mcp)
- [https://circleback.ai/blog/how-to-connect-circleback-mcp](https://circleback.ai/blog/how-to-connect-circleback-mcp)
- [https://circleback.ai/blog/what-is-mcp-meeting-tool](https://circleback.ai/blog/what-is-mcp-meeting-tool)
- [https://circleback.ai/pricing](https://circleback.ai/pricing)
- [https://circleback.ai/](https://circleback.ai/)

5 source URLs. Raw sources field, verbatim:

https://support.circleback.ai/en/articles/13249081-circleback-mcp, https://circleback.ai/blog/how-to-connect-circleback-mcp, https://circleback.ai/blog/what-is-mcp-meeting-tool, https://circleback.ai/pricing, https://circleback.ai/

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. STRUCTURALLY THE MOST INTERESTING ENTRY IN THIS FILE: Circleback appears to have NO traditional REST API at all, which would make MCP its only programmatic access path. That is the first instance in this directory of a vendor shipping MCP INSTEAD of an API rather than in addition to one, and if it holds up it is a genuine leading indicator for the category. Flagged as an appearance, not a settled fact: absence of a public API page is not proof no API exists. Eleven tools documented: SearchMeetings, ReadMeetings, SearchTranscripts, GetTranscriptsForMeetings, SearchActionItems, SearchCalendarEvents, SearchEmails, FindProfiles, FindCompanies, ListTags, SearchSupportArticles. Published plans: Individual $20.83/user/mo, Team $25/user/mo, Enterprise custom, with a free trial. Which plans include MCP is NOT stated on either the pricing page or the MCP doc, so treat plan-gating as unknown within the paid gate. ENDPOINT DISCREPANCY: search results surface app.circleback.ai/api/mcp while the vendor support article gives circleback.ai/api/mcp; the support article value is used here.

**Provenance**

- **Entry id**: 03-circleback

- **Source file**: 03-conversation-intel.md

- **Source line**: 451

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
