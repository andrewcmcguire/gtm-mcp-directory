# Seismic: MCP server status, API access gate and what it does

> Sales enablement platform with a "Seismic for Meetings" module, powered by its "Aura" AI engine, that... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Seismic

# Seismic

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [seismic.com](https://seismic.com) · entry id 03-seismic · source 03-conversation-intel.md line 372

**What it does**
Sales enablement platform with a "Seismic for Meetings" module, powered by its "Aura" AI engine, that records, transcribes, and analyzes sales meetings.

**AI features, separated from automation with an AI label on it**
Aura AI engine performs meeting analysis (topics discussed, questions asked, suggested next steps) plus sentiment analysis on recorded conversations - genuine call-analysis AI layered onto the core content/enablement product, not just content recommendation.

**RevOps role**
Enablement-plus-meeting-intelligence platform similar to Highspot, exposing content, engagement, and meeting data to AI agents via MCP.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Streamable HTTP transport per Seismic's MCP documentation; the specific credential type (API key vs. OAuth) was not confirmed in the sources reviewed.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server](https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official (Early Access)

mcp_url, verbatim from the file:

https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server

- [https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server](https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (inferred). No public self-serve pricing; Seismic sells via enterprise contracts, and the MCP server itself is explicitly labeled "Early Access," implying a limited/gated rollout even for existing customers.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Retrieve sales content](../jobs/retrieve-sales-content.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server](https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server)
- [https://www.seismic.com/platform/meetings/](https://www.seismic.com/platform/meetings/)
- [https://www.seismic.com/enablement-explainers/what-is-seismic-aura/](https://www.seismic.com/enablement-explainers/what-is-seismic-aura/)
- [https://www.seismic.com/enablement-explainers/conversational-intelligence/](https://www.seismic.com/enablement-explainers/conversational-intelligence/)

4 source URLs. Raw sources field, verbatim:

https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server, https://www.seismic.com/platform/meetings/, https://www.seismic.com/enablement-explainers/what-is-seismic-aura/, https://www.seismic.com/enablement-explainers/conversational-intelligence/

**Notes, verbatim from the file**
Included per the schema's conditional instruction - Seismic qualifies via its Aura-powered Meetings module. MCP server status is "Early Access," worth re-checking as it matures.

**Provenance**

- **Entry id**: 03-seismic

- **Source file**: 03-conversation-intel.md

- **Source line**: 372

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
