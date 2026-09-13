# MeetGeek: MCP server status, API access gate and what it does

> Automatic meeting recorder and transcriber that produces summaries, highlights and conversation analytics... Official MCP, Free to start. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
MeetGeek

# MeetGeek

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-25
CLI: meetgeek (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [meetgeek.ai](https://meetgeek.ai) · entry id 03-meetgeek · source 03-conversation-intel.md line 431

**What it does**
Automatic meeting recorder and transcriber that produces summaries, highlights and conversation analytics across Zoom, Teams and Meet.

**AI features, separated from automation with an AI label on it**
AI summaries and highlight detection, plus meeting analytics such as talk-time and engagement metrics. Transcription in 100+ languages is commodity ASR; the analytics layer is the closest thing to a differentiator.

**RevOps role**
Zero-cost entry point for putting real meeting transcripts in front of an agent, useful as the cheapest way to prototype a conversation-intel workflow before paying for Gong or Avoma.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Two paths. The cloud server uses OAuth 2.0 with Google or Microsoft sign-in and no API key. The self-hosted server runs locally on Node.js and authenticates to api.meetgeek.ai with a MeetGeek API key from account settings.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL**: [https://mcp.meetgeek.ai/mcp](https://mcp.meetgeek.ai/mcp)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-04 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.meetgeek.ai/mcp (cloud; docs https://support.meetgeek.ai/en/articles/13491658-public-mcp-cloud-guide). Self-hosted open source: https://github.com/meetgeekai/meetgeek-mcp-server

- [https://mcp.meetgeek.ai/mcp](https://mcp.meetgeek.ai/mcp)
- [https://support.meetgeek.ai/en/articles/13491658-public-mcp-cloud-guide](https://support.meetgeek.ai/en/articles/13491658-public-mcp-cloud-guide)
- [https://github.com/meetgeekai/meetgeek-mcp-server](https://github.com/meetgeekai/meetgeek-mcp-server)

**What this server exposes**

- **Tools named**: 6
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: meetgeekai/meetgeek-mcp-server
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **highlights** No description was recorded with the name. evidence: in the server source · calling it reads

- **meetingDetails** No description was recorded with the name. evidence: in the server source · calling it reads

- **meetings** No description was recorded with the name. evidence: in the server source · calling it reads

- **summary** No description was recorded with the name. evidence: in the server source · calling it reads

- **teamMeetings** No description was recorded with the name. evidence: in the server source · calling it reads

- **transcript** No description was recorded with the name. evidence: in the server source · calling it reads

119 of the 251 entries that record an official or community MCP server carry a harvested tool list. The other 132 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: meetgeek
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g meetgeek-cli
```

quoted from [https://www.npmjs.com/package/meetgeek-cli](https://www.npmjs.com/package/meetgeek-cli) on 2026-09-12, via npm, a third party source

Packages seen, with the version on 2026-09-12:

- [npm: meetgeek-cli 0.1.2, third party](https://www.npmjs.com/package/meetgeek-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

[https://docs.meetgeek.ai/](https://docs.meetgeek.ai/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/meetgeekai/meetgeek-mcp-server](https://github.com/meetgeekai/meetgeek-mcp-server)

**On GitHub**

[github.com/meetgeekai](https://github.com/meetgeekai) tied to the vendor by rule 1, the directory already classed this repo first-party and its owner is an Organization, confidence strong

- **Public repositories**: 5, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-03-12

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [onechart](https://github.com/meetgeekai/onechart) | other | | 0 | 2026-03-12 | v1.0.13 |
| [meetgeek-mcp-server](https://github.com/meetgeekai/meetgeek-mcp-server) | MCP server | Official MeetGeek MCP Server | 23 | 2026-02-05 | |
| [meetgeekai-n8n-node](https://github.com/meetgeekai/meetgeekai-n8n-node) | SDK | n8n community node for integrating with the Meetgeek app | 4 | 2025-10-17 | |
| [meetgeek-mcp-test](https://github.com/meetgeekai/meetgeek-mcp-test) | MCP server | | 0 | 2025-07-23 | |
| [release-action](https://github.com/meetgeekai/release-action) | infrastructure | | 0 | 2024-06-05 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 468 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/meetgeekai/meetgeek-mcp-server](https://github.com/meetgeekai/meetgeek-mcp-server)
- [https://support.meetgeek.ai/en/articles/13491658-public-mcp-cloud-guide](https://support.meetgeek.ai/en/articles/13491658-public-mcp-cloud-guide)
- [https://support.meetgeek.ai/en/articles/11939580-mcp-server](https://support.meetgeek.ai/en/articles/11939580-mcp-server)
- [https://meetgeek.ai/pricing](https://meetgeek.ai/pricing)
- [https://meetgeek.ai/integrations/meetgeek-mcp](https://meetgeek.ai/integrations/meetgeek-mcp)
- [https://meetgeek.ai/blog/meetgeek-mcp-server](https://meetgeek.ai/blog/meetgeek-mcp-server)

6 source URLs. Raw sources field, verbatim:

https://github.com/meetgeekai/meetgeek-mcp-server, https://support.meetgeek.ai/en/articles/13491658-public-mcp-cloud-guide, https://support.meetgeek.ai/en/articles/11939580-mcp-server, https://meetgeek.ai/pricing, https://meetgeek.ai/integrations/meetgeek-mcp, https://meetgeek.ai/blog/meetgeek-mcp-server

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. THE LOOSEST GATE FOUND IN THIS PASS, and the sharpest contrast in the whole directory: the pricing page lists "API and MCP access" as included on the free Basic plan, and the cloud MCP guide states the MeetGeek requirement is "Free plan minimum". Published plans: Basic free forever, Pro $9.99/user/mo, Business $17/user/mo, Enterprise custom. The practical constraint is data volume, not access: Basic caps at 3 hours of transcription per month. Set that beside Gong in this same file, where API access in practice means a five-figure enterprise contract, and the pair is a complete segment on its own. Eight cloud tools: list_user_meetings, list_team_meetings, get_meeting_details, get_meeting_transcript, get_meeting_summary, get_meeting_highlights, get_meeting_insights, upload_recording_for_analysis. That last one is a WRITE path, which is rarer than it sounds; most meeting MCPs found in this sweep are strictly read-only. The GitHub org meetgeekai is the vendor's own org, which is what makes the self-hosted repo count as official rather than community. Client-side plan requirements apply separately (Claude Pro/Team/Enterprise, ChatGPT Plus/Team/Enterprise).

**Provenance**

- **Entry id**: 03-meetgeek

- **Source file**: 03-conversation-intel.md

- **Source line**: 431

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
