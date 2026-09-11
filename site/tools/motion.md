# Motion: MCP server status, API access gate and what it does

> AI-driven work-management app that auto-schedules a user's tasks, projects, and meetings onto their calendar... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

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

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

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
- **Docs URL**: [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/RF-D/motion-mcp (one of several competing unofficial servers; also github.com/devondragon/MotionMCP, github.com/h3ro-dev/motion-mcp-server, github.com/christopher-czaban/motion-mcp-server, github.com/Identityex/use-motion-mcp-server) - the RF-D repo states plainly: "This is a community-built integration, not an official Motion product."

- [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp)

**What this server exposes**

- **Tools named**: 34
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-11
- **Repo read**: RF-D/motion-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **motion_add_custom_field_to_project** Add a custom field value to a project evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_add_custom_field_to_task** Add a custom field value to a task evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_complete_task** Mark a task as completed evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_create_comment** Add a new comment to a task evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_create_custom_field** Create a new custom field evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_create_project** Create a new project in Motion evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_create_recurring_task** Create a new recurring task evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_create_task** Create a new task in Motion evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_delete_comment** Delete a comment permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_delete_project** Delete a project permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_delete_recurring_task** Delete a recurring task permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_delete_task** Delete a task permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_get_comment** Get details of a specific comment evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_get_current_user** Get information about the currently authenticated user evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_get_project** Get detailed information about a specific project evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_get_recurring_task** Get details of a specific recurring task evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_get_schedule** Get schedule information for a user within a date range evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_get_task** Get detailed information about a specific task evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_get_user** Get information about a specific user by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_get_workspace** Get details of a specific workspace by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_list_comments** List all comments for a specific task evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_list_custom_fields** List all custom fields, optionally filtered by workspace evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_list_projects** List all projects, optionally filtered by workspace evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_list_recurring_tasks** List all recurring tasks, optionally filtered by workspace evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_list_tasks** List tasks with optional filters. Supports pagination via cursor. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_list_users** List all users, optionally filtered by workspace evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_list_workspaces** List all workspaces accessible to the authenticated user evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_move_task** Move a task to a different project evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_remove_custom_field_from_task** Remove a custom field value from a task evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_uncomplete_task** Mark a task as not completed evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_update_comment** Update the content of an existing comment evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_update_project** Update an existing project evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_update_recurring_task** Update an existing recurring task evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **motion_update_task** Update an existing task evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

120 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 105 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - Motion has no free tier at all (Pro AI $19/seat/mo, Business AI $29/seat/mo are the only listed plans); API access requires an API key issued to a paid account.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp)

**On GitHub**

No GitHub organisation could be tied to usemotion.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

8 candidate accounts seen and rejected by the evidence rules: RF-D, motion, motiondivision, motion-canvas, motioneye-project. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
