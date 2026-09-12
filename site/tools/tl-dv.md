# tl;dv: MCP server status, API access gate and what it does

> Records and transcribes Zoom, Google Meet, and Microsoft Teams calls, layering on sales coaching (playbook... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
tl;dv

# tl;dv

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24
CLI: tldv (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [tldv.io](https://tldv.io) · entry id 03-tl-dv · source 03-conversation-intel.md line 201

**What it does**
Records and transcribes Zoom, Google Meet, and Microsoft Teams calls, layering on sales coaching (playbook monitoring, objection handling) at higher tiers.

**AI features, separated from automation with an AI label on it**
Multi-meeting AI speaker insights, sales playbook monitoring and coaching, AI objection handling, AI-generated notes/summaries.

**RevOps role**
Recording-plus-coaching layer with a genuinely reachable paid entry point ($18-29/mo) for a solo operator, unlike most enterprise-gated tools in this category.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: API key generated at Settings → Personal Settings → API keys.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/tldv-public/tldv-mcp-server (npm package tldv-mcp) ; https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/

- [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server)
- [https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/](https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/)

**What this server exposes**

- **Tools named**: 4
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: tldv-public/tldv-mcp-server
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **get-highlights** Allows you to get highlights from a meeting by providing a meeting ID. evidence: in the server source · calling it reads

- **get-meeting-metadata** Get a meeting by its ID. The meeting ID is a unique identifier for a meeting. It will return the meeting metadata, including the name, the date, the organizer, participants and more. evidence: in the server source · calling it reads

- **get-transcript** Get transcript by meeting ID. The transcript is a list of messages exchanged between the participants in the meeting. It evidence: in the server source · calling it reads

- **list-meetings** List all meetings based on the filters provided. You can filter by date, status, and more. Those meetings are the sames you have access to in the TLDV app. evidence: in the server source · calling it reads

119 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 106 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: tldv
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g tldv-cli
```

quoted from [https://www.npmjs.com/package/tldv-cli](https://www.npmjs.com/package/tldv-cli) on 2026-09-12, via npm, a third party source

Packages seen, with the version on 2026-09-12:

- [npm: tldv-cli 0.1.0, third party](https://www.npmjs.com/package/tldv-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. The general API ships from the Pro plan ($18-29/mo); tl;dv's own MCP setup docs state you need a Business or Enterprise account specifically for the MCP server, since the free tier excludes API access entirely either way.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server)

**On GitHub**

[github.com/tldv-public](https://github.com/tldv-public) tied to the vendor by rule 1, the directory already classed this repo first-party and its owner is an Organization, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2025-12-12

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server) | MCP server | | 14 | 2025-12-12 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server)
- [https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/](https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/)
- [https://www.claap.io/blog/tl-dv-pricing](https://www.claap.io/blog/tl-dv-pricing)
- [https://salestools.club/apis/tldv](https://salestools.club/apis/tldv)

4 source URLs. Raw sources field, verbatim:

https://github.com/tldv-public/tldv-mcp-server, https://tldv.io/blog/tldv-mcp-elevating-meeting-intelligence-with-ai-driven-contextualization/, https://www.claap.io/blog/tl-dv-pricing, https://salestools.club/apis/tldv

**Notes, verbatim from the file**
None.

**Provenance**

- **Entry id**: 03-tl-dv

- **Source file**: 03-conversation-intel.md

- **Source line**: 201

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
