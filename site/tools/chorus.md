# Chorus: MCP server status, API access gate and what it does

> Records, transcribes, and analyzes sales calls, meetings, and emails, and syncs the resulting insights into... No MCP found, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Chorus

# Chorus

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [zoominfo.com/products/chorus](https://zoominfo.com/products/chorus) · entry id 03-chorus · source 03-conversation-intel.md line 68

**What it does**
Records, transcribes, and analyzes sales calls, meetings, and emails, and syncs the resulting insights into the CRM.

**AI features, separated from automation with an AI label on it**
Talk-ratio and sentiment scoring, competitor-mention detection, deal-risk/momentum scoring (declining engagement, negative sentiment trends, stalled deals), and coaching scorecards tracking methodology adherence. Transcription itself is standard ASR. Vendor "14 patents" marketing language was not independently verified.

**RevOps role**
Call-capture and coaching layer, differentiated from standalone conversation-intelligence tools by direct access to ZoomInfo's B2B contact/firmographic database.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a for MCP. The REST API uses a per-user API token generated in Chorus's Personal Settings page.

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (inferred, not an explicit vendor statement). No public self-serve pricing exists - the product page routes only to "Request Demo," and secondary sources note API access is not included on every ZoomInfo/Chorus plan.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.zoominfo.com/products/chorus](https://www.zoominfo.com/products/chorus)
- [https://api-docs.chorus.ai/](https://api-docs.chorus.ai/)
- [https://www.claap.io/blog/chorus-ai-api](https://www.claap.io/blog/chorus-ai-api)
- [https://pipeline.zoominfo.com/sales/introducing-zoominfo-chorus](https://pipeline.zoominfo.com/sales/introducing-zoominfo-chorus)

4 source URLs. Raw sources field, verbatim:

https://www.zoominfo.com/products/chorus, https://api-docs.chorus.ai/, https://www.claap.io/blog/chorus-ai-api, https://pipeline.zoominfo.com/sales/introducing-zoominfo-chorus

**Notes, verbatim from the file**
None.

**Provenance**

- **Entry id**: 03-chorus

- **Source file**: 03-conversation-intel.md

- **Source line**: 68

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
