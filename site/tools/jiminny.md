# Jiminny: MCP server status, API access gate and what it does

> Records, transcribes, and scores sales calls, syncing action items and summaries into the CRM. Community MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Jiminny

# Jiminny

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [jiminny.com](https://jiminny.com) · entry id 03-jiminny · source 03-conversation-intel.md line 334

**What it does**
Records, transcribes, and scores sales calls, syncing action items and summaries into the CRM.

**AI features, separated from automation with an AI label on it**
AI-generated call summaries and action items, conversation scoring/coaching tools per product marketing - depth not independently verified in this research.

**RevOps role**
Mid-market call-recording and coaching layer with a documented but not fully transparent API surface.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Community server: JIMINNY_TOKEN API token. Zapier's hosted connector uses Zapier's own OAuth layer.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp](https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://mcp.jiminny.com/mcp ; https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp ; https://zapier.com/mcp/jiminny - both third-party; no official Jiminny-branded MCP announcement was found. ; repo https://github.com/fzheng0222/jiminny-mcp

- [https://mcp.jiminny.com/mcp](https://mcp.jiminny.com/mcp)
- [https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp](https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp)
- [https://zapier.com/mcp/jiminny](https://zapier.com/mcp/jiminny)
- [https://github.com/fzheng0222/jiminny-mcp](https://github.com/fzheng0222/jiminny-mcp)

**What this server exposes**

- **Tools named**: 3
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-11
- **Repo read**: fzheng0222/jiminny-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **jiminny_get_summary** AI-generated summary, action items, and key points evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **jiminny_get_transcript** Full transcript with speaker labels and timestamps evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **jiminny_list_conversations** Lists recorded calls (paginated, newest first) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

120 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 105 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (no pricing page exists on any path and neither the site nor the integrations page mentions an API; the only route is contact-us)

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/fzheng0222/jiminny-mcp](https://github.com/fzheng0222/jiminny-mcp)

**On GitHub**

[github.com/jiminny](https://github.com/jiminny) tied to the vendor by rule 3, account website https://jiminny.com has the vendor's domain, confidence strong

- **Public repositories**: 7, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-06-04

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [oauth2-dialpad](https://github.com/jiminny/oauth2-dialpad) | other | | 0 | 2026-06-04 | |
| [record-public](https://github.com/jiminny/record-public) | other | | 0 | 2025-12-01 | |
| [join-the-team](https://github.com/jiminny/join-the-team) | other | Interested in joining the Jiminny Engineering team? Start here! | 10 | 2024-03-29 | |
| [oauth2-aircall](https://github.com/jiminny/oauth2-aircall) | other | | 0 | 2024-03-01 | |
| [oauth2-salesloft](https://github.com/jiminny/oauth2-salesloft) | infrastructure | | 0 | 2023-10-11 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://help.jiminny.com/en/articles/9527212-what-is-the-jiminny-api](https://help.jiminny.com/en/articles/9527212-what-is-the-jiminny-api)
- [https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp](https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp)
- [https://zapier.com/mcp/jiminny](https://zapier.com/mcp/jiminny)
- [https://apitracker.io/a/jiminny](https://apitracker.io/a/jiminny)
- [https://www.jiminny.com/](https://www.jiminny.com/)
- [https://github.com/fzheng0222/jiminny-mcp](https://github.com/fzheng0222/jiminny-mcp)
- [https://mcp.jiminny.com/mcp](https://mcp.jiminny.com/mcp)

7 source URLs. Raw sources field, verbatim:

https://help.jiminny.com/en/articles/9527212-what-is-the-jiminny-api, https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp, https://zapier.com/mcp/jiminny, https://apitracker.io/a/jiminny, https://www.jiminny.com/, https://github.com/fzheng0222/jiminny-mcp, https://mcp.jiminny.com/mcp

**Notes, verbatim from the file**
Added as an expansion beyond the seed list - a second mid-market Gong/Chorus competitor worth tracking. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.jiminny.com/): no pricing page exists on any path and neither the site nor the integrations page mentions an API; the only route is contact-us. 2026-09-07: fzheng0222/jiminny-mcp is a real server (pyproject.toml + src/server.py, README lists transcript/summary tools) but the owner is an individual, not Jiminny (https://github.com/fzheng0222/jiminny-mcp).

**Provenance**

- **Entry id**: 03-jiminny

- **Source file**: 03-conversation-intel.md

- **Source line**: 334

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
