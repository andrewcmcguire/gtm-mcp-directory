# Seismic: MCP server status, API access gate and what it does

> Sales enablement platform with a "Seismic for Meetings" module, powered by its "Aura" AI engine, that... Official MCP, Enterprise only. Checked 2026-09-07.

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
Checked 2026-09-07

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

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server](https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official (Early Access)

mcp_url, verbatim from the file:

https://mcp.seismic.com/ ; https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server

- [https://mcp.seismic.com/](https://mcp.seismic.com/)
- [https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server](https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server)

**What this server exposes**

- **Tools named**: 20
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **Add content to DSR** Adds a selected Seismic content to a chosen Digital Sales Room (DSR) evidence: in the vendor docs · calling it writes · required: dsrId, contentVersionId

- **Add content to meeting** Add Seismic content to meeting evidence: in the vendor docs · calling it writes

- **Create a DSR engagement** Creates a new Digital Sales Room (DSR) from provided template and request parameters evidence: in the vendor docs · calling it writes

- **Generate LiveSend link** Generates a LiveSend link with configurable settings and provided contents evidence: in the vendor docs · calling it reads

- **Generate answers or summaries by Generative Search** Generates a natural-language answer to a user question and returns the supporting sources used evidence: in the vendor docs · calling it reads

- **Get CRM context by ID** Retrieves CRM context information by context ID evidence: in the vendor docs · calling it reads · required: context ID

- **Get DSR comments and user details** Returns comments and associated user details for a Digital Sales Room evidence: in the vendor docs · calling it reads

- **Get available CRM Systems** Retrieves a list of all available CRM systems integrated with the platform evidence: in the vendor docs · calling it reads

- **Get contents by Generative Search** Retrieves relevant sources for a user query without generating an answer evidence: in the vendor docs · calling it reads

- **Get meeting details by ID** Retrieves complete meeting information by meeting ID evidence: in the vendor docs · calling it reads · required: meeting ID

- **Get meeting list** Get a paginated list of meetings based on created time evidence: in the vendor docs · calling it reads

- **Get post meeting overview** Get the post meeting overview, which include the summaries, the action items, content recommendations evidence: in the vendor docs · calling it writes · required: meeting ID

- **Get post-meeting brief** Retrieves the AI-generated post-meeting brief for a specific meeting evidence: in the vendor docs · calling it writes · required: meeting ID

- **Get pre-meeting brief** Retrieves AI-generated pre-meeting brief information for a specific meeting evidence: in the vendor docs · calling it reads · required: meeting ID, CRM account

- **Get the DSR engagement list** Retrieve a paginated list of DSR engagements that match CRM context and filter criteria evidence: in the vendor docs · calling it reads

- **Get the meeting engagement list** Retrieve a paginated list of meeting engagements that match CRM context and filter criteria evidence: in the vendor docs · calling it reads

- **Get the transcript analysis of meeting** Get the transcript analysis of meeting by meeting id evidence: in the vendor docs · calling it reads · required: meeting ID

- **List DSR templates** Lists available DSR templates with identifiers and descriptive metadata evidence: in the vendor docs · calling it reads

- **Search CRM Contexts** Searches for CRM context objects using natural language queries and optional filters evidence: in the vendor docs · calling it reads · required: query

- **Update meeting metadata** Updates meeting engagement metadata such as agenda entries, notes, and tags evidence: in the vendor docs · calling it writes

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (inferred). No public self-serve pricing; Seismic sells via enterprise contracts, and the MCP server itself is explicitly labeled "Early Access," implying a limited/gated rollout even for existing customers.

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/seismic](https://github.com/seismic) tied to the vendor by rule 3, account website https://seismic.com has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-08-31

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [teams-policy-config](https://github.com/seismic/teams-policy-config) | other | Teams Policy Config | 0 | 2026-08-31 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Retrieve sales content](../jobs/retrieve-sales-content.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 649 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server](https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server)
- [https://www.seismic.com/platform/meetings/](https://www.seismic.com/platform/meetings/)
- [https://www.seismic.com/enablement-explainers/what-is-seismic-aura/](https://www.seismic.com/enablement-explainers/what-is-seismic-aura/)
- [https://www.seismic.com/enablement-explainers/conversational-intelligence/](https://www.seismic.com/enablement-explainers/conversational-intelligence/)
- [https://mcp.seismic.com/](https://mcp.seismic.com/)

5 source URLs. Raw sources field, verbatim:

https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server, https://www.seismic.com/platform/meetings/, https://www.seismic.com/enablement-explainers/what-is-seismic-aura/, https://www.seismic.com/enablement-explainers/conversational-intelligence/, https://mcp.seismic.com/

**Notes, verbatim from the file**
Included per the schema's conditional instruction - Seismic qualifies via its Aura-powered Meetings module. MCP server status is "Early Access," worth re-checking as it matures. 2026-09-07: https://mcp.seismic.com/ returned 401 to an MCP initialize POST while https://mcp.seismic.com/zzznotamcp returned 404, so the root is a live route on a dedicated vendor mcp. subdomain (https://mcp.seismic.com/).

**Provenance**

- **Entry id**: 03-seismic

- **Source file**: 03-conversation-intel.md

- **Source line**: 372

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
