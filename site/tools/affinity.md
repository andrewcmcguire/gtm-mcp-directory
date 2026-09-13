# Affinity: MCP server status, API access gate and what it does

> A relationship-intelligence CRM for deal teams that auto-builds the contact graph from email and calendar... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Affinity

# Affinity

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [affinity.co](https://affinity.co) · entry id 06-affinity · source 06-revops-infra.md line 471

**What it does**
A relationship-intelligence CRM for deal teams that auto-builds the contact graph from email and calendar activity and scores relationship strength, rather than relying on reps to log activity.

**AI features, separated from automation with an AI label on it**
Semantic search across companies and people, relationship-strength scoring, and meeting-transcript retrieval. The contact-graph construction itself is automation over mail and calendar metadata, not AI.

**RevOps role**
System of record for relationship-driven pipelines, primarily private capital, with warm-path discovery layered on top of the CRM itself.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth where the client supports it, otherwise an API key. Local deployment is API key only. All MCP queries inherit the connecting user's existing Affinity permissions.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.affinity.co/mcp (docs: https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP)

- [https://mcp.affinity.co/mcp](https://mcp.affinity.co/mcp)
- [https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP](https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP)

**What this server exposes**

- **Tools named**: 52
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **create_company** Create a new company record evidence: in the vendor docs · calling it writes

- **create_field** Define a new field on a list, on companies, on people, or on opportunities evidence: in the vendor docs · calling it reads

- **create_interaction** Log a meeting, call, or chat message with one or more people evidence: in the vendor docs · calling it reads

- **create_list** Create a new list for organizing companies, people, or opportunities evidence: in the vendor docs · calling it writes

- **create_list_entry** Add an existing person or company as a list entry to a list evidence: in the vendor docs · calling it writes

- **create_list_field_dropdown_option** Add a new selectable option to a dropdown field on a list evidence: in the vendor docs · calling it writes

- **create_note** Create a note and attach it to a person, company, opportunity, or meeting evidence: in the vendor docs · calling it writes

- **create_opportunity** Create a new opportunity and attach it to a list evidence: in the vendor docs · calling it writes

- **create_person** Add a new person record to your team's address book evidence: in the vendor docs · calling it writes

- **create_reminder** Set up a new reminder evidence: in the vendor docs · calling it writes

- **delete_list_field_dropdown_option** Remove a dropdown option from a list field evidence: in the vendor docs · calling it writes

- **delete_reminder** Delete an existing reminder evidence: in the vendor docs · calling it writes

- **get_company_info** Get detailed profile and field data for a specific company evidence: in the vendor docs · calling it reads

- **get_company_list_entries** See which lists a company appears on evidence: in the vendor docs · calling it reads

- **get_company_relationships** View which teammates have relationships at a company and their strength evidence: in the vendor docs · calling it reads

- **get_current_user** Check who you're authenticated as and verify your connection evidence: in the vendor docs · calling it reads

- **get_entities_attached_to_note** Find what records are linked to a specific note evidence: in the vendor docs · calling it reads

- **get_entity_field_dropdown_options** See what dropdown options are available on a person or company field evidence: in the vendor docs · calling it reads

- **get_entity_fields** See what fields are available for people or companies evidence: in the vendor docs · calling it reads

- **get_field_value_changes** See the history of changes to a field's values over time evidence: in the vendor docs · calling it reads

- **get_list_field_dropdown_options** See what dropdown options are available on a list field evidence: in the vendor docs · calling it reads

- **get_list_fields** See what fields are available on a specific list evidence: in the vendor docs · calling it reads

- **get_list_info** Get metadata and a direct link for a specific list evidence: in the vendor docs · calling it reads

- **get_lists** See all lists you have access to, optionally filtered by name evidence: in the vendor docs · calling it reads

- **get_meetings** Get past and upcoming meeting interactions and attendees evidence: in the vendor docs · calling it reads

- **get_meetings_for_entity** Get meetings for a specific person, company, or opportunity evidence: in the vendor docs · calling it reads

- **get_notes_for_entity** Get all notes attached to a specific record evidence: in the vendor docs · calling it reads

- **get_person_info** Get detailed profile and field data for a specific person evidence: in the vendor docs · calling it reads

- **get_person_list_entries** See which lists a person appears on evidence: in the vendor docs · calling it reads

- **get_person_relationships** View which teammates know a specific person and relationship strength evidence: in the vendor docs · calling it reads

- **get_reminders** See all of your team's reminders evidence: in the vendor docs · calling it reads

- **get_saved_view_list_entries** Pull the list entries that match a saved view's filters evidence: in the vendor docs · calling it reads

- **get_saved_views** See the saved views configured on a list evidence: in the vendor docs · calling it reads

- **get_single_list_entry** Get a specific entry on a list evidence: in the vendor docs · calling it reads

- **get_transcript_fragments** Retrieve dialogue fragments of your team's meeting transcripts evidence: in the vendor docs · calling it reads

- **query_notes** Find notes by creator or date range evidence: in the vendor docs · calling it reads

- **render_warm_intro_graph** Render the ranked intro paths as an interactive network graph evidence: in the vendor docs · calling it reads

- **search_all_companies** Exhaustively list or filter companies with cursor-based pagination evidence: in the vendor docs · calling it reads

- **search_companies_top_matches** Search for companies using natural language, structured filters, or both evidence: in the vendor docs · calling it reads

- **search_files** Search files by keyword, across all files or scoped to a company evidence: in the vendor docs · calling it reads

- **search_list_entries** Search, filter, and sort entries on a specific list, with cursor-based pagination evidence: in the vendor docs · calling it reads

- **search_notes** Search notes by keyword, across all notes or scoped to a company evidence: in the vendor docs · calling it reads

- **search_opportunities** Search for opportunities by keyword or list them all evidence: in the vendor docs · calling it reads

- **search_persons** Search people across your org using structured filters, sorts, and/or a keyword evidence: in the vendor docs · calling it reads

- **send_feedback** Submit feedback about a missing capability or limitation directly to Affinity evidence: in the vendor docs · calling it reads

- **update_company** Update an existing company's name, domain, or associated people evidence: in the vendor docs · calling it writes

- **update_list_field_dropdown_option** Rename or restyle an existing dropdown option on a list field evidence: in the vendor docs · calling it reads

- **update_opportunity** Rename an opportunity or change its company and person associations evidence: in the vendor docs · calling it reads

- **update_person** Update an existing person's name, email addresses, or company associations evidence: in the vendor docs · calling it writes

- **update_reminder** Update an existing reminder's details evidence: in the vendor docs · calling it writes

- **upsert_entity_field_values** Create or update field values on a person or company evidence: in the vendor docs · calling it writes

- **upsert_list_entry_field_values** Create or update field values in bulk for a specific list entry evidence: in the vendor docs · calling it writes

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP](https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/affinity](https://github.com/affinity) tied to the vendor by rule 3, account website https://affinity.co/ has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2019-08-22

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [redlock-cs-async](https://github.com/affinity/redlock-cs-async) | other | Asynchronous Distributed lock with Redis and C# (based on http://redis.io/topics/distlock) | 1 | 2019-08-22 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Discover warm intro paths](../jobs/discover-warm-intro-paths.md)
- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 649 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP](https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP)
- [https://www.affinity.co/blog/affinity-is-building-the-best-mcp-for-private-capital](https://www.affinity.co/blog/affinity-is-building-the-best-mcp-for-private-capital)
- [https://www.affinity.co/product/crm](https://www.affinity.co/product/crm)
- [https://mcp.affinity.co/mcp](https://mcp.affinity.co/mcp)

4 source URLs. Raw sources field, verbatim:

https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP, https://www.affinity.co/blog/affinity-is-building-the-best-mcp-for-private-capital, https://www.affinity.co/product/crm, https://mcp.affinity.co/mcp

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. API and MCP access are restricted to the Scale, Advanced and Enterprise tiers; lower tiers cannot use it at all. Launched in beta in 2026 with roughly 33 read and write tools. TRANSFERABILITY CAVEAT: Affinity is aimed at VC, PE and investment banking rather than classic B2B SaaS sales, so the relationship-strength model is tuned for a different motion than most of this directory. Included because the auto-built relationship graph is the same job Centralize (05) and The Swarm (01) do, approached from a third direction, and the three together are a coherent lane. 2026-09-07: https://mcp.affinity.co/mcp returned 401 to an MCP initialize POST (https://mcp.affinity.co/mcp).

**Provenance**

- **Entry id**: 06-affinity

- **Source file**: 06-revops-infra.md

- **Source line**: 471

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
