# Zoom Revenue Accelerator: MCP server status, API access gate and what it does

> Zoom's built-in conversation/revenue-intelligence layer that analyzes Zoom Meetings and Phone calls for deal... Official MCP, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Zoom Revenue Accelerator

# Zoom Revenue Accelerator

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [zoom.com](https://zoom.com) · entry id 03-zoom-revenue-accelerator · source 03-conversation-intel.md line 315

**What it does**
Zoom's built-in conversation/revenue-intelligence layer that analyzes Zoom Meetings and Phone calls for deal insights, scorecards, and account activity.

**AI features, separated from automation with an AI label on it**
Transcripts and summaries, next-steps and objection extraction, deal scorecards, and account-activity rollups, per the MCP connector's documented data surface.

**RevOps role**
Native conversation-intelligence layer for teams already standardized on Zoom, now exposed to external AI agents via an official MCP connector.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - Zoom user-level OAuth access token (env var ZOOM_REVENUE_ACCELERATOR_MCP_ACCESS_TOKEN), plus an OpenAI Codex plugin variant.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/](https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/ ; https://github.com/zoom/zoom-plugin/blob/main/CONNECTORS.md

- [https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/](https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/)
- [https://github.com/zoom/zoom-plugin/blob/main/CONNECTORS.md](https://github.com/zoom/zoom-plugin/blob/main/CONNECTORS.md)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown/enterprise-leaning. Zoom Revenue Accelerator ships as an add-on to Zoom's paid meeting plans; explicit self-serve pricing for a single-seat/solo API user was not found in this research.

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/zoom/zoom-plugin/blob/main/CONNECTORS.md](https://github.com/zoom/zoom-plugin/blob/main/CONNECTORS.md)

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/](https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/)
- [https://github.com/zoom/zoom-plugin/blob/main/CONNECTORS.md](https://github.com/zoom/zoom-plugin/blob/main/CONNECTORS.md)
- [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0082725](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0082725)
- [https://developers.zoom.us/docs/api/rest/reference/iq/methods/](https://developers.zoom.us/docs/api/rest/reference/iq/methods/)
- [https://developers.zoom.us/docs/api/iq/](https://developers.zoom.us/docs/api/iq/)

5 source URLs. Raw sources field, verbatim:

https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/, https://github.com/zoom/zoom-plugin/blob/main/CONNECTORS.md, https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0082725, https://developers.zoom.us/docs/api/rest/reference/iq/methods/, https://developers.zoom.us/docs/api/iq/

**Notes, verbatim from the file**
None. [api_gate 2026-08-25] Re-checked and left unknown, honestly: Zoom's own API docs state the caller must be a Revenue Accelerator-licensed user on a paid account, so a licence condition IS documented; but every Revenue Accelerator product and pricing path 404'd, so whether a solo operator can buy that licence self-serve is unconfirmed and the gate stays unknown rather than being guessed at. Checked against https://developers.zoom.us/docs/api/iq/.

**Provenance**

- **Entry id**: 03-zoom-revenue-accelerator

- **Source file**: 03-conversation-intel.md

- **Source line**: 315

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
