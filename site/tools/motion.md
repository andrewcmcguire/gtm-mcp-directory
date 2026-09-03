# Motion: MCP server status, API access gate and what it does

> AI-driven work-management app that auto-schedules a user's tasks, projects, and meetings onto their calendar... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
Motion

# Motion

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [usemotion.com](https://usemotion.com) · entry id 10-motion · source 10-scheduling-routing.md line 122

**What it does**
AI-driven work-management app that auto-schedules a user's tasks, projects, and meetings onto their calendar around priorities and deadlines, bundled with note-taking and document tools.

**AI features, separated from automation with an AI label on it**
Genuine, long-standing optimization algorithm - constraint-based task auto-scheduling that places and reshuffles tasks around existing meetings and deadlines; this is Motion's original scheduling engine, not LLM-based. Newer vendor-marketed features (AI Project Manager, AI Task Manager, AI Calendar Assistant, AI Meeting Notetaker, AI Docs Assistant, AI Chat) are plausibly LLM-backed, especially notetaking/summarization, but not independently verified against a technical teardown - treat as vendor-stated.

**RevOps role**
Personal/individual-rep calendar-and-task auto-scheduler - the "how does my day get built" layer for an AE or rep, not a prospect-facing booking tool.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: API key (MOTION_API_KEY from Motion Settings -> API), per community repos. Rate limits reported at 12 req/min for individual accounts, 120 req/min for team accounts.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp)Probed**: 2026-09-03, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/RF-D/motion-mcp (one of several competing unofficial servers; also github.com/devondragon/MotionMCP, github.com/h3ro-dev/motion-mcp-server, github.com/christopher-czaban/motion-mcp-server, github.com/Identityex/use-motion-mcp-server) - the RF-D repo states plainly: "This is a community-built integration, not an official Motion product."

- [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - Motion has no free tier at all (Pro AI $19/seat/mo, Business AI $29/seat/mo are the only listed plans); API access requires an API key issued to a paid account.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp)

**Jobs it can do**

- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://usemotion.com](https://usemotion.com)
- [https://www.usemotion.com/pricing](https://www.usemotion.com/pricing)
- [https://www.usemotion.com/help](https://www.usemotion.com/help)
- [https://api-docs.usemotion.com/](https://api-docs.usemotion.com/)
- [https://docs.usemotion.com/](https://docs.usemotion.com/)
- [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp)
- [https://mcp.so/servers/motion-mcp-server](https://mcp.so/servers/motion-mcp-server)

7 source URLs. Raw sources field, verbatim:

https://usemotion.com, https://www.usemotion.com/pricing, https://www.usemotion.com/help, https://api-docs.usemotion.com/, https://docs.usemotion.com/, https://github.com/RF-D/motion-mcp, https://mcp.so/servers/motion-mcp-server

**Notes, verbatim from the file**
No official MCP found despite an actively maintained vendor REST API and dev docs - the MCP ecosystem here is entirely community-built and fragmented across 5+ competing unofficial servers, a maturity gap relative to Reclaim/Calendly/Cal.com.

**Provenance**

- **Entry id**: 10-motion

- **Source file**: 10-scheduling-routing.md

- **Source line**: 122

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
