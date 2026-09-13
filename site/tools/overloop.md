# Overloop: MCP server status, API access gate and what it does

> Sales engagement and lead-gen platform for finding, verifying, and contacting B2B prospects via automated... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Overloop

# Overloop

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24
CLI: overloop (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [overloop.com](https://overloop.com) · entry id 02-overloop · source 02-engagement-outbound.md line 331

**What it does**
Sales engagement and lead-gen platform for finding, verifying, and contacting B2B prospects via automated email and LinkedIn campaigns.

**AI features, separated from automation with an AI label on it**
Vendor claims an "AI engine" that builds multichannel campaigns, analyzes a prospect's website/social profiles to write "ultra-personalized" cold emails, drafts contextual follow-ups from thread history, and personalizes LinkedIn connection requests - plausible LLM-based personalization per vendor description, not independently verified.

**RevOps role**
Multichannel outbound sequencing/lead-gen layer, now organizationally tied to Sortlist (a B2B agency-matching marketplace).

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: api key via OVERLOOP_API_KEY environment variable

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/sortlist/overloop-mcp

- [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp)

**What this server exposes**

- **Tools named**: 54
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: sortlist/overloop-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **add_campaign_step** Add a step to a campaign. Use previous_step_id to position it in the sequence. For condition branches, set position: 0 (yes) or 1 (no). evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **add_to_exclusion_list** Add an email address or domain to the exclusion list evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **archive_conversation** Archive a conversation evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **assign_conversation** Assign a conversation to a team member evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clone_sourcing** Create a copy of a sourcing (new sourcing starts in paused status) evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_campaign** Create a new campaign (created in evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_list** Create a new list evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_organization** Create a new organization. Pass return_existing=true to return an existing one if a duplicate is found. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_prospect** Create a new prospect. Pass return_existing=true to return an existing prospect if one with the same email or LinkedIn profile already exists. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_sourcing** Create a standalone sourcing to discover prospects from Overloop\ evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_campaign** Permanently delete a campaign evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_list** Permanently delete a list evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_organization** Permanently delete an organization evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_prospect** Permanently delete a prospect evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_sourcing** Permanently delete a sourcing evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **disenroll_prospect** Disenroll a prospect from a campaign evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **enroll_prospect** Enroll a prospect into a campaign evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_account** Get your Overloop account information including plan details and remaining credits evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_campaign** Retrieve a campaign by ID. Use expand=steps,sourcing to include details. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_campaign_enrollment** Retrieve a specific campaign enrollment evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_campaign_step** Retrieve a specific campaign step evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_conversation** Retrieve a conversation by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_current_user** Get the user associated with the current API key evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_list** Retrieve a list by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_organization** Retrieve an organization by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_prospect** Retrieve a prospect by ID or email address evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_sourcing** Retrieve a sourcing by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_user** Retrieve a user by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_campaign_enrollments** List enrollments for a campaign (paginated) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_campaign_steps** List steps for a campaign (paginated) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_campaigns** List campaigns (paginated). Supports sorting, filtering, and search. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_conversations** List conversations (paginated). Supports sorting, filtering by archived status, and search. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_custom_fields** List all custom fields defined in your account. Use the identifier (e.g. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_exclusion_list** List exclusion list items (paginated). The exclusion list prevents emails from being sent to specific addresses or domains. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_lists** List all prospect lists (paginated) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_organizations** List organizations (paginated). Supports sorting, filtering, and search. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_prospects** List prospects (paginated). Supports sorting, filtering, and search. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_sending_addresses** List all connected sending addresses for your account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_sourcing_search_options** List available values for sourcing search criteria (locations, industries, technologies, company_sizes, management_levels, departments). Use field and q params to search within a specific field. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_sourcings** List sourcings (paginated). Supports filtering by status and search. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_step_types** List all available campaign step types grouped by category, with default configs evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_users** List all team members (paginated) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **pause_sourcing** Pause an active sourcing to temporarily stop prospect discovery evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **remove_campaign_step** Remove a step from a campaign evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **remove_from_exclusion_list** Remove an item from the exclusion list evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **start_sourcing** Activate a paused sourcing to resume prospect discovery evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **unarchive_conversation** Unarchive a conversation evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_campaign** Update campaign settings. Pass status evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_campaign_step** Update a campaign step evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_conversation** Update the conversation name evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_list** Update a list name evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_organization** Update an organization. Only provided fields are changed. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_prospect** Update a prospect. Only provided fields are changed. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_sourcing** Update a sourcing evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 521 entries that record an official or community MCP server carry a harvested tool list. The other 402 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: overloop
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g overloop-cli
```

quoted from [https://www.npmjs.com/package/overloop-cli](https://www.npmjs.com/package/overloop-cli) on 2026-09-12, via npm, a third party source

Packages seen, with the version on 2026-09-12:

- [npm: overloop-cli 1.4.0, third party](https://www.npmjs.com/package/overloop-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

635 of 1032 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp)

**On GitHub**

[github.com/overloop-crm](https://github.com/overloop-crm) tied to the vendor by rule 3, account website https://overloop.com has the vendor's domain, confidence strong

- **Public repositories**: 3, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2023-07-18

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [overloop-account-enricher](https://github.com/overloop-crm/overloop-account-enricher) | other | | 0 | 2023-07-18 | |
| [omniauth-slack](https://github.com/overloop-crm/omniauth-slack) | other | | 0 | 2019-08-06 | |
| [hunterio](https://github.com/overloop-crm/hunterio) | SDK | A Ruby wrapper around Hunter.io API V2 | 3 | 2019-07-09 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Find a work email address](../jobs/find-work-email.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 1,032 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://overloop.com/pricing](https://overloop.com/pricing)
- [https://overloop.com/](https://overloop.com/)
- [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp)

3 source URLs. Raw sources field, verbatim:

https://overloop.com/pricing, https://overloop.com/, https://github.com/sortlist/overloop-mcp

**Notes, verbatim from the file**
Formerly Prospect.io. REST API is available at the Growth tier ($99/user/mo) and above, not Starter ($69/user/mo). The only known MCP server lives under github.com/sortlist (not Overloop's own org) and carries a beta notice - consistent with signs the product now operates under Sortlist; flagged as a business-continuity consideration, not a confirmed shutdown.

**Provenance**

- **Entry id**: 02-overloop

- **Source file**: 02-engagement-outbound.md

- **Source line**: 331

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
