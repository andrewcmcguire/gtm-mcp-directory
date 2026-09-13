# Grain: MCP server status, API access gate and what it does

> AI meeting notetaker that records and transcribes calls and builds a searchable, cross-meeting library synced... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Grain

# Grain

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-09-07

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

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.grain.com/_/mcp ; https://developers.grain.com/mcp (server endpoint https://api.grain.com/_/mcp) ; repo https://github.com/grain-team/grain-meeting-memory-plugin

- [https://api.grain.com/_/mcp](https://api.grain.com/_/mcp)
- [https://developers.grain.com/mcp](https://developers.grain.com/mcp)
- [https://github.com/grain-team/grain-meeting-memory-plugin](https://github.com/grain-team/grain-meeting-memory-plugin)

**What this server exposes**

- **Tools named**: 15
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **fetch_deal** Get detailed deal information evidence: in the vendor docs · calling it reads · required: deal_id

- **fetch_meeting** Get detailed information about a specific meeting evidence: in the vendor docs · calling it reads · required: meeting_id

- **fetch_meeting_coaching_feedback** Get detailed coaching scorecard for specific meeting evidence: in the vendor docs · calling it reads · required: meeting_id

- **fetch_meeting_notes** Get AI-generated meeting notes (more concise than transcripts) evidence: in the vendor docs · calling it reads · required: meeting_id

- **fetch_meeting_transcript** Retrieve full meeting transcript evidence: in the vendor docs · calling it reads · required: meeting_id

- **list_all_deals** Access HubSpot Deal intelligence evidence: in the vendor docs · calling it reads

- **list_attended_meetings** Get filtered list of all accessible meetings evidence: in the vendor docs · calling it reads

- **list_coaching_feedback** Get AI-generated sales coaching insights evidence: in the vendor docs · calling it reads

- **list_meetings** Get filtered list of all accessible meetings evidence: in the vendor docs · calling it reads

- **list_open_deals** Access HubSpot Deal intelligence evidence: in the vendor docs · calling it reads

- **list_workspace_users** Get all users in your Grain workspace evidence: in the vendor docs · calling it reads

- **myself** Get your Grain account information evidence: in the vendor docs · calling it reads

- **search_companies** Find companies that participated in meetings when filtering evidence: in the vendor docs · calling it reads · required: search_strings

- **search_meetings** Semantic search across all meeting transcripts evidence: in the vendor docs · calling it reads · required: search_string

- **search_persons** Search for meeting participants when filtering evidence: in the vendor docs · calling it reads · required: search_string

119 of the 251 entries that record an official or community MCP server carry a harvested tool list. The other 132 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. The Free plan has no API access; Personal API access (via a Personal Access Token) starts at the Starter plan, so a solo operator can reach it but must pay. Workspace-wide API access requires Business/Enterprise plus admin rights.

**API documentation**

No documentation URL recorded.

374 of 468 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/grain-team/grain-meeting-memory-plugin](https://github.com/grain-team/grain-meeting-memory-plugin)

**On GitHub**

[github.com/grain-team](https://github.com/grain-team) tied to the vendor by rule 3, account website https://grain.com has the vendor's domain, confidence strong

- **Public repositories**: 13, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-08-17

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [milvex](https://github.com/grain-team/milvex) | other | An Elixir Client for Milvus | 4 | 2026-08-17 | v0.14.2 |
| [grain-meeting-memory-plugin](https://github.com/grain-team/grain-meeting-memory-plugin) | plugin or integration | | 1 | 2026-07-27 | |
| [ueberauth_hubspot](https://github.com/grain-team/ueberauth_hubspot) | other | Hubspot Strategy for Überauth | 0 | 2026-05-22 | |
| [meeting-data-analysis](https://github.com/grain-team/meeting-data-analysis) | other | For customers to pull meeting metrics | 0 | 2025-12-22 | |
| [grain-workspace-api-example](https://github.com/grain-team/grain-workspace-api-example) | docs or examples | Example of how to iterate over all recordings in a workspace to download the transcripts | 0 | 2025-07-10 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Search across recorded calls](../jobs/search-call-library.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 468 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developers.grain.com/mcp](https://developers.grain.com/mcp)
- [https://support.grain.com/en/articles/15507288-grain-api](https://support.grain.com/en/articles/15507288-grain-api)
- [https://grain.com/pricing](https://grain.com/pricing)
- [https://api.grain.com/_/mcp](https://api.grain.com/_/mcp)

4 source URLs. Raw sources field, verbatim:

https://developers.grain.com/mcp, https://support.grain.com/en/articles/15507288-grain-api, https://grain.com/pricing, https://api.grain.com/_/mcp

**Notes, verbatim from the file**
An unofficial third-party server (https://github.com/eadm/grain-mcp-server) also exists - prefer the official one. 2026-09-07: https://api.grain.com/_/mcp returned 401 to an MCP initialize POST (https://api.grain.com/_/mcp). 2026-09-12 (P6-04 repo sweep): first-party repository recorded at https://github.com/grain-team/grain-meeting-memory-plugin - first-party Claude plugin that wires the hosted server, NOT the server source. Evidence: the org grain-team, tied to grain.com by harvest_orgs.py domain evidence, and the repo's .mcp.json declares an http server at https://api.grain.com/_/mcp, which is the endpoint this entry already records.

**Provenance**

- **Entry id**: 03-grain

- **Source file**: 03-conversation-intel.md

- **Source line**: 106

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
