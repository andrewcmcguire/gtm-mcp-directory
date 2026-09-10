# Unify: MCP server status, API access gate and what it does

> A hybrid signals-plus-agent platform: AI agents build targeted account/prospect lists from 40+ data sources,... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
Unify

# Unify

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-08-24
CLI: unify-cli (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.unifygtm.com](https://www.unifygtm.com) · entry id 04-unify · source 04-ai-sdr-agents.md line 106

**What it does**
A hybrid signals-plus-agent platform: AI agents build targeted account/prospect lists from 40+ data sources, write personalized outbound copy, and run multi-channel sequences triggered by intent signals ("plays").

**AI features, separated from automation with an AI label on it**
List-building from combined signals (job changes, funding, hiring, web visits, tech stack) and copywriting are AI-driven; "your agent knows your CRM, your data, and how you sell" is vendor copy for a chat-based orchestration layer, not verified as autonomous end-to-end execution.

**RevOps role**
Combined signals-intent + outbound-execution layer - overlaps with both category 4 and category 5 (signals-intent-abm) in this directory.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Auth0 browser sign-in (auth.unifygtm.com); MCP caches the session cookie (~30-day life) rather than a refresh token - no password or key ever passed to the MCP client

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/footcarts/unify-mcp

- [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp)

**What this server exposes**

- **Tools named**: 45
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-10
- **Repo read**: footcarts/unify-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **add_to_unify_list** Add one or more people/companies to a List. Pass the List evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **check_unify_enrollment_reply** Whether a given enrollment has received a reply. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **count_unify_enrollments_for_action** Dry-run: count how many enrollments would be affected by a bulk action (use before unenroll). excludeStatuses defaults to [ evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_unify_task** Create a follow-up task on a Unify person. Type is the task category (PHONE_CALL, EMAIL, etc), priority is HIGH/MEDIUM/LOW, dueAt is an ISO timestamp. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_audience** Fetch an audience definition with its filter tree (personFiltersV2 / companyFiltersV2) and linked plays. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_audience_people_count** Total number of people currently matching an audience. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_company** Fetch a Unify company by id or domain. Returns full record: address, industry, description, revenue, employeeCount, intent, recordOwner, social links, plus all custom fields. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_current_user** Identity of the logged-in user (id, email, role, tenant, full permission flags). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_enrollment_steps** Per-step execution history for a single enrollment (one entry per step with status/startedAt/endedAt). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_object_record** Fetch one record by id from any object type. Returns full attributes including custom fields. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_person** Fetch a Unify person by id or email. Returns the full record (id, name, email, phones, title, status, recordOwner, lastWebsiteActivityAt, lead_source, company link, plus all custom fields). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_person_draft_note** Get the current draft note (if any) for a Unify person. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_play** Fetch a play definition (publishedObjectType, owner, isPaused, settings, retrigger config). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_sequence** Fetch a sequence definition with ordered steps and version metadata. By default step bodies (email HTML) are stripped; pass full=true to get raw output. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_sequence_metrics** Funnel breakdown for a sequence: total/inProgress/finished (subdivided by completed/replied/bounced/optedOut/excluded). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_unify_unseen_task_count** Number of unseen tasks for the current user. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_audience_companies** List companies currently matching an audience filter, paginated. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_audience_people** List people currently matching an audience filter, paginated. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_audiences** List audiences (filter-based dynamic groups) in the workspace. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_background_actions** Status of recent bulk actions (UNENROLL/REASSIGN/UPGRADE/REFRESH/RESTART). Filter by sequenceId, status[], startedWithinHours. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_folders** List folder tree for an entity type (LIST, AUDIENCE, SEQUENCE). Use to navigate organization structure. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_list_company_entries** List companies in a Company-list. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_list_person_entries** List people in a Person-list. Each entry has its own membership id (selectedEntryIds for removal). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_lists** List static-membership Lists. objectModel is evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_mailboxes** List sending mailboxes (id, emailAddress, displayName, primaryUser, provider, isPaused, isUnauthorized). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_object_records** Page through records of an object type. Optionally filter with a free-text search. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_object_types** List the Unify object types this MCP can introspect. Each type has dedicated search/get/sample tools. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_person_exclusions** List exclusion (suppression) rules currently affecting a Unify person. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_person_lists** List all Lists with a membership flag (objectEntryId is set when this person is in the list). evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_person_notes** List published + draft notes for a Unify person, paginated. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_person_opportunities** List CRM opportunities associated with a Unify person. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_person_sequence_enrollments** List all sequence enrollments (active + finished) for a Unify person, including step-level execution history. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_plays** List plays. Filter by objectType to get only PERSON-targeting or COMPANY-targeting plays. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_sequence_enrollments** List enrollments for a sequence with status, displayStatus, substatuses (isReplied/isBounced/etc), person, mailbox, and per-step executions. Paginated. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_sequences** List sequences in the workspace. Returns summarized rows (id/name/owner/etc); pass full=true for raw API output (large - includes full step bodies). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_unify_snippets** List snippets (reusable content blocks for emails, including SMART snippets with AI prompts). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **post_unify_person_note** Publish a note on a Unify person record. Reuses an existing draft if one is open for the current user; otherwise creates+publishes. The body is HTML - wrap text content in

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-10. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: unify-cli
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-10

Install, as the source shows it:

```
pip install unify-cli
```

quoted from [https://pypi.org/project/unify-cli/](https://pypi.org/project/unify-cli/) on 2026-09-10, via pypi, a third party source

Packages seen, with the version on 2026-09-10:

- [pypi: unify-cli 3.6.2, third party](https://pypi.org/project/unify-cli/)
- [pypi: unify-cli 3.6.2, third party](https://pypi.org/project/unify-cli/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-10.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, self-serve for the app (Free/$0, Base $20/seat/mo, Pro $60/seat/mo); "Open API + webhooks" is gated to the custom-priced Business tier only

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp)

**On GitHub**

[github.com/unifygtm](https://github.com/unifygtm) tied to the vendor by rule 3, account website https://unifygtm.com has the vendor's domain, confidence strong

- **Public repositories**: 7, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-01

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [bulk-api-connector-examples](https://github.com/unifygtm/bulk-api-connector-examples) | docs or examples | Directory of example Connector implementations using the Unify Bulk API | 0 | 2026-09-01 | |
| [agent-plugins](https://github.com/unifygtm/agent-plugins) | plugin or integration | Official Unify GTM agent plugins for cursor, codex and claude. | 0 | 2026-08-25 | |
| [sdk-python](https://github.com/unifygtm/sdk-python) | SDK | Official Python SDK for the Unify API. | 0 | 2026-06-18 | v0.1.3 |
| [sdk-typescript](https://github.com/unifygtm/sdk-typescript) | SDK | Official TypeScript SDK for the Unify API. | 0 | 2026-06-17 | v0.1.3 |
| [intent-js-client](https://github.com/unifygtm/intent-js-client) | SDK | JavaScript client for interacting with the Unify Intent API in the browser. | 11 | 2026-06-14 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Build a target account list](../jobs/build-target-account-list.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.unifygtm.com](https://www.unifygtm.com)
- [https://www.unifygtm.com/pricing](https://www.unifygtm.com/pricing)
- [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp)

3 source URLs. Raw sources field, verbatim:

https://www.unifygtm.com, https://www.unifygtm.com/pricing, https://github.com/footcarts/unify-mcp

**Notes, verbatim from the file**
The MCP is an unaffiliated, community-maintained repo (0 stars, ~12 commits as of this check) - functional-looking but not vendor-backed; don't represent it as official to a reader. Official API is enterprise-gated even though the app itself is self-serve down to $0.

**Provenance**

- **Entry id**: 04-unify

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 106

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-10

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
