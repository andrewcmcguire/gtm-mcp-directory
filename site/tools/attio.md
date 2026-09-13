# Attio: MCP server status, API access gate and what it does

> A CRM built around a flexible, user-defined data model (not fixed contact/company/deal objects) with... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Attio

# Attio

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07
CLI: attio

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [attio.com](https://attio.com) · entry id 06-attio · source 06-revops-infra.md line 58

**What it does**
A CRM built around a flexible, user-defined data model (not fixed contact/company/deal objects) with real-time sync and an API-first architecture.

**AI features, separated from automation with an AI label on it**
Confirmed AI surface is thin in what's publicly documented - automatic data enrichment and meeting-intelligence tooling are mentioned as part of the MCP tool surface, but no distinct named AI-agent product on the scale of Agentforce or Breeze was found; treated as unconfirmed rather than asserted.

**RevOps role**
A newer, flexible-schema CRM competing for data-team/startup RevOps stacks that want customizable record objects; one of the cleaner "log in with your own account, no API key" MCP implementations found in this research.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - one-time login as the user's own Attio account, no API key needed. Reads auto-approve; writes require confirmation. Permissions mirror whatever the logged-in user already has in the workspace.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.attio.com/mcp/overview](https://docs.attio.com/mcp/overview)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.attio.com/mcp ; https://docs.attio.com/mcp/overview (endpoint: https://mcp.attio.com/mcp)

- [https://mcp.attio.com/mcp](https://mcp.attio.com/mcp)
- [https://docs.attio.com/mcp/overview](https://docs.attio.com/mcp/overview)

**What this server exposes**

- **Tools named**: 41
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **add-record-to-list** Add a record to a list as a new list entry evidence: in the vendor docs · calling it writes

- **create-comment** Create a new comment on a record, list entry, or as a reply to an existing comment thread evidence: in the vendor docs · calling it writes

- **create-list** Create a new list to group and track records of a single object type evidence: in the vendor docs · calling it writes

- **create-note** Create a new note attached to a record evidence: in the vendor docs · calling it writes

- **create-record** Create a new record (person, company, deal, or custom object) evidence: in the vendor docs · calling it writes

- **create-task** Create a new task with optional deadline, assignee, and linked record evidence: in the vendor docs · calling it writes

- **delete-comment** Delete a comment that you created evidence: in the vendor docs · calling it writes

- **get-call-recording** Retrieve full details and transcript of a specific call recording evidence: in the vendor docs · calling it reads

- **get-email-content** Retrieve the full body of a specific email evidence: in the vendor docs · calling it reads

- **get-note-body** Retrieve the full content of a specific note evidence: in the vendor docs · calling it reads

- **get-records-by-ids** Retrieve full details for specific records by their IDs evidence: in the vendor docs · calling it reads

- **list-attribute-definitions** List all attributes available on an object type, including their types and valid options evidence: in the vendor docs · calling it reads

- **list-comment-replies** Fetch additional replies for a top-level comment thread evidence: in the vendor docs · calling it reads

- **list-comments** List comments on a record or list entry, with paginated top-level comments and inline replies evidence: in the vendor docs · calling it reads

- **list-list-attribute-definitions** List the available entry attributes for a given list evidence: in the vendor docs · calling it reads

- **list-lists** List all lists in the workspace, with optional filtering by name or slug evidence: in the vendor docs · calling it reads

- **list-objects** List all objects in the workspace (e.g. companies, people, deals), with optional fuzzy search by name or API slug evidence: in the vendor docs · calling it reads

- **list-records** List records in a given object with optional filtering and sorting evidence: in the vendor docs · calling it reads

- **list-records-in-list** List entries in a given list with optional filtering and sorting evidence: in the vendor docs · calling it reads

- **list-tasks** List tasks in the workspace with optional filters evidence: in the vendor docs · calling it reads

- **list-workspace-members** List members in the workspace with their details and team memberships evidence: in the vendor docs · calling it reads

- **list-workspace-teams** List all teams in the workspace evidence: in the vendor docs · calling it reads

- **merge-records** Merge two records of the same object into one new record evidence: in the vendor docs · calling it writes

- **query-particle-sql** Execute a read-only SQL query against your workspace data evidence: in the vendor docs · calling it reads

- **run-basic-report** Run aggregate reports on records or list entries evidence: in the vendor docs · calling it reads

- **search-call-recordings-by-metadata** Search call recordings by participants, related records, title, or time range evidence: in the vendor docs · calling it reads

- **search-emails-by-metadata** Search emails by participants, domain, or time range evidence: in the vendor docs · calling it reads

- **search-meetings** Search past and upcoming meetings by participants, related records, or time range evidence: in the vendor docs · calling it reads

- **search-notes-by-metadata** Search notes by parent record, author, meeting, or creation time evidence: in the vendor docs · calling it reads

- **search-records** Full-text search for records (people, companies, deals, etc.) by name, email, domain, or other indexed attributes evidence: in the vendor docs · calling it reads

- **semantic-search-call-recordings** Find call recordings by topic using AI-powered semantic search evidence: in the vendor docs · calling it reads

- **semantic-search-emails** Find emails by topic using AI-powered semantic search evidence: in the vendor docs · calling it reads

- **semantic-search-notes** Find notes by topic using AI-powered semantic search evidence: in the vendor docs · calling it reads

- **update-list** Update a list's name, API slug, or permissions evidence: in the vendor docs · calling it writes

- **update-list-entry-by-id** Update an existing list entry when you already know the entry_id evidence: in the vendor docs · calling it writes

- **update-list-entry-by-record-id** Find and update a list entry using its parent record ID evidence: in the vendor docs · calling it writes

- **update-note** Append or prepend content to a note, or update its title evidence: in the vendor docs · calling it writes

- **update-record** Update an existing record by record_id evidence: in the vendor docs · calling it writes

- **update-task** Update a task's deadline, status, assignee, or linked record evidence: in the vendor docs · calling it writes

- **upsert-record** Create or update a record using a matching attribute (e.g., email or domain) evidence: in the vendor docs · calling it writes

- **whoami** Get information about the current user's identity and workspace membership evidence: in the vendor docs · calling it reads

119 of the 437 entries that record an official or community MCP server carry a harvested tool list. The other 318 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: attio
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g attio
```

quoted from [https://www.npmjs.com/package/attio](https://www.npmjs.com/package/attio) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: attio 1.0.4](https://www.npmjs.com/package/attio)
- [npm: attio-cli 0.3.1, third party](https://www.npmjs.com/package/attio-cli)
- [pypi: attio 0.24.0, third party](https://pypi.org/project/attio/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the Free plan (up to 3 seats) includes API access, rate-limited (~1,000 calls/hour). Paid tiers: Plus $29/user/mo, Pro $69/user/mo, Enterprise custom.

**API documentation**

No documentation URL recorded.

604 of 934 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/attio](https://github.com/attio) tied to the vendor by rule 3, account website https://attio.com has the vendor's domain, confidence strong

- **Public repositories**: 19, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [notion-app](https://github.com/attio/notion-app) | app | | 0 | 2026-09-07 | |
| [lemlist-app](https://github.com/attio/lemlist-app) | app | | 0 | 2026-09-04 | |
| [pandadoc-app](https://github.com/attio/pandadoc-app) | app | | 0 | 2026-09-03 | |
| [aircall-app](https://github.com/attio/aircall-app) | app | | 0 | 2026-09-03 | |
| [asana-app](https://github.com/attio/asana-app) | app | | 0 | 2026-08-20 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 934 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://docs.attio.com/mcp/overview](https://docs.attio.com/mcp/overview)
- [https://mcp.attio.com/](https://mcp.attio.com/)
- [https://attio.com/pricing](https://attio.com/pricing)
- [https://mcp.attio.com/mcp](https://mcp.attio.com/mcp)

4 source URLs. Raw sources field, verbatim:

https://docs.attio.com/mcp/overview, https://mcp.attio.com/, https://attio.com/pricing, https://mcp.attio.com/mcp

**Notes, verbatim from the file**
Community/unofficial Attio MCP servers also exist (e.g. kesslerio/attio-mcp-server) and are separate from the official mcp.attio.com hosted server linked above. 2026-09-07: https://mcp.attio.com/mcp returned 401 to an MCP initialize POST (https://mcp.attio.com/mcp).

**Provenance**

- **Entry id**: 06-attio

- **Source file**: 06-revops-infra.md

- **Source line**: 58

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
