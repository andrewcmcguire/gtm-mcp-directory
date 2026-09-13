# Retool: MCP server status, API access gate and what it does

> A low-code platform for building internal tools/dashboards/admin panels on top of databases and APIs; in a... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Retool

# Retool

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07
CLI: retool (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [retool.com](https://retool.com) · entry id 06-retool · source 06-revops-infra.md line 405

**What it does**
A low-code platform for building internal tools/dashboards/admin panels on top of databases and APIs; in a GTM context, used to build custom RevOps tooling - lead-routing consoles, deal-desk approval apps, data-correction UIs - on top of the warehouse/CRM.

**AI features, separated from automation with an AI label on it**
Real natural-language app-building ("prompt full-stack apps on your live production data," context-aware @mention editing), AI Workflows (chains AI calls with data/business logic, one-click RAG), and "AI Agents" framed as production-ready automations with audit trails - more than a chat-copilot bolt-on, but claims like "AI Agents handle customer support" should be read as marketing framing until seen in practice.

**RevOps role**
The app layer for RevOps - builds custom internal UIs on top of the warehouse/CRM for workflows off-the-shelf tools don't cover (approval flows, override consoles, ops dashboards).

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0. Endpoint pattern https:///mcp over HTTP.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://retool.com/blog/retool-mcp-server](https://retool.com/blog/retool-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official (public beta)

mcp_url, verbatim from the file:

https://mcp.retool.com/mcp ; https://retool.com/blog/retool-mcp-server ; repo https://github.com/tryretool/agent-plugins

- [https://mcp.retool.com/mcp](https://mcp.retool.com/mcp)
- [https://retool.com/blog/retool-mcp-server](https://retool.com/blog/retool-mcp-server)
- [https://github.com/tryretool/agent-plugins](https://github.com/tryretool/agent-plugins)

**What this server exposes**

- **Tools named**: 50
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **retool_cancel_react_app_thread_activity** Cancel activity on an active thread. evidence: in the vendor docs · calling it reads

- **retool_create_or_append_react_app_thread_message** Create or update an app from a natural-language prompt. evidence: in the vendor docs · calling it writes

- **retool_create_resource** Create a new resource. evidence: in the vendor docs · calling it writes

- **retool_create_user_invite** Create a user invite. evidence: in the vendor docs · calling it writes

- **retool_delete_user_invite** Delete a user invite by invite ID. evidence: in the vendor docs · calling it writes

- **retool_delete_user_invite_attribute** Delete a user attribute from a user invite. evidence: in the vendor docs · calling it writes

- **retool_delete_workflow** Delete a workflow by workflow ID. evidence: in the vendor docs · calling it writes

- **retool_execute_resource_ts** Execute a TypeScript snippet against selected resources. evidence: in the vendor docs · calling it reads

- **retool_finalize_prepared_import** Finalize a two-step import after the source zip is uploaded. evidence: in the vendor docs · calling it writes

- **retool_get_app** Get a single app by app ID. evidence: in the vendor docs · calling it reads

- **retool_get_environment** Get an environment by environment ID. evidence: in the vendor docs · calling it reads

- **retool_get_folder** Get a folder by folder ID. evidence: in the vendor docs · calling it reads

- **retool_get_group** Get a single permission group by group ID. evidence: in the vendor docs · calling it reads

- **retool_get_organization** Get organization settings. evidence: in the vendor docs · calling it reads

- **retool_get_react_app_thread_activity_status** Check whether an existing thread has active agent work. evidence: in the vendor docs · calling it reads

- **retool_get_resource** Get metadata for one resource by name. evidence: in the vendor docs · calling it reads

- **retool_get_resource_ts_definitions** Generate global variable bindings and TypeScript definitions for selected resources. evidence: in the vendor docs · calling it reads

- **retool_get_user** Get a single user by user ID. evidence: in the vendor docs · calling it reads

- **retool_get_user_invite** Get a single user invite by invite ID. evidence: in the vendor docs · calling it reads

- **retool_get_workflow** Get a workflow by workflow ID. evidence: in the vendor docs · calling it reads

- **retool_grant_app_access** Grant or update direct access to an app for a user, pending invite, or group. evidence: in the vendor docs · calling it writes

- **retool_list_app_access** List the users, invited users, and groups that currently have access to an app. evidence: in the vendor docs · calling it reads

- **retool_list_apps** List apps in the organization. evidence: in the vendor docs · calling it reads

- **retool_list_audit_logs** List audit log events in the organization. evidence: in the vendor docs · calling it reads

- **retool_list_environments** List environments in the organization. evidence: in the vendor docs · calling it reads

- **retool_list_folders** List folders in the organization. evidence: in the vendor docs · calling it reads

- **retool_list_groups** List permission groups in the organization, including their members. evidence: in the vendor docs · calling it reads

- **retool_list_pending_react_app_function_approvals** List publish-blocking approvals required for mutating functions. evidence: in the vendor docs · calling it reads

- **retool_list_pending_react_app_thread_reviews** List pending live human-in-the-loop review requests. evidence: in the vendor docs · calling it reads

- **retool_list_react_app_files** List file paths, sizes, and line counts for an app. evidence: in the vendor docs · calling it reads

- **retool_list_react_app_threads** List recently active threads for an app. evidence: in the vendor docs · calling it reads

- **retool_list_resource_folders** List resource folders in the organization. evidence: in the vendor docs · calling it reads

- **retool_list_resources** List resources available in the organization, including databases, APIs, storage, and AI providers. evidence: in the vendor docs · calling it reads

- **retool_list_user_invites** List user invites in the organization. evidence: in the vendor docs · calling it reads

- **retool_list_users** List users in the organization. evidence: in the vendor docs · calling it reads

- **retool_list_workflows** List workflows in the organization. evidence: in the vendor docs · calling it reads

- **retool_list_writable_app_folders** List the app folders the authenticated user can create apps in. evidence: in the vendor docs · calling it writes

- **retool_publish_react_app** Publish a thread using the same publish flow as the app builder. evidence: in the vendor docs · calling it reads

- **retool_read_react_app_files** Read the contents of specific files in an app. evidence: in the vendor docs · calling it reads

- **retool_read_react_app_thread_stream** Fetch the most recent persisted chat messages for an existing thread. evidence: in the vendor docs · calling it reads

- **retool_report_tool_usage_feedback** Report feedback about MCP tool usage. evidence: in the vendor docs · calling it reads

- **retool_respond_to_react_app_thread_review** Wait for a pending review request and submit the response. evidence: in the vendor docs · calling it reads

- **retool_revoke_app_access** Revoke direct app access for a user, pending invite, or group. evidence: in the vendor docs · calling it reads

- **retool_search_app_share_subjects** Search the app sharing directory for users, pending invites, and groups. evidence: in the vendor docs · calling it reads

- **retool_set_user_invite_attribute** Create or update a user attribute on a user invite. evidence: in the vendor docs · calling it writes

- **retool_start_prepared_import** Start a two-step import of a large existing app. evidence: in the vendor docs · calling it writes

- **retool_submit_prepared_import** Import an existing app in one step. evidence: in the vendor docs · calling it writes

- **retool_sync_react_app_thread** Sync an app's thread branch from external source control. evidence: in the vendor docs · calling it reads

- **retool_tail_react_app_thread_stream** Monitor an active thread and forward progress updates. evidence: in the vendor docs · calling it reads

- **retool_update_resource** Update an existing resource by name. evidence: in the vendor docs · calling it writes

119 of the 337 entries that record an official or community MCP server carry a harvested tool list. The other 218 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: retool
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g retool-cli
```

quoted from [https://www.npmjs.com/package/retool-cli](https://www.npmjs.com/package/retool-cli) on 2026-09-12, via npm, a third party source

Packages seen, with the version on 2026-09-12:

- [npm: retool-cli 1.0.29, third party](https://www.npmjs.com/package/retool-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the Free plan is self-serve with no sales conversation (unlimited apps, 500 workflow runs/mo, up to 5 users); cheapest paid Team plan is $10/mo per builder, annual.

**API documentation**

No documentation URL recorded.

494 of 694 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/tryretool/agent-plugins](https://github.com/tryretool/agent-plugins)

**On GitHub**

[github.com/tryretool](https://github.com/tryretool) tied to the vendor by rule 3, account website https://retool.com has the vendor's domain, confidence strong

- **Public repositories**: 41, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [agent-plugins](https://github.com/tryretool/agent-plugins) | plugin or integration | | 0 | 2026-09-08 | |
| [terraform-provider-retool](https://github.com/tryretool/terraform-provider-retool) | infrastructure | | 4 | 2026-09-04 | v2.1.0 |
| [legal](https://github.com/tryretool/legal) | other | Retool Legal Agreements and Policies | 1 | 2026-09-04 | |
| [terraform-retool-self-hosted-blueprints](https://github.com/tryretool/terraform-retool-self-hosted-blueprints) | infrastructure | Terraform modules to deploy self-hosted Retool to your cloud | 5 | 2026-09-03 | v0.3.5 |
| [retool-helm](https://github.com/tryretool/retool-helm) | infrastructure | | 54 | 2026-09-03 | v6.11.23 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Query a data warehouse](../jobs/query-data-warehouse.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 694 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://retool.com/pricing](https://retool.com/pricing)
- [https://retool.com/products/ai](https://retool.com/products/ai)
- [https://retool.com/blog/retool-mcp-server](https://retool.com/blog/retool-mcp-server)
- [https://mcp.retool.com/mcp](https://mcp.retool.com/mcp)

4 source URLs. Raw sources field, verbatim:

https://retool.com/pricing, https://retool.com/products/ai, https://retool.com/blog/retool-mcp-server, https://mcp.retool.com/mcp

**Notes, verbatim from the file**
The MCP server manages apps/workflows/users (build/edit/deploy apps, run queries, bulk user invites, access audits, resource enumeration) - an admin/dev-ops-facing MCP rather than an end-user data MCP. Available to both cloud and self-hosted customers per the announcement. 2026-09-07: https://mcp.retool.com/mcp returned 401 {"error":"Missing Authorization: Bearer <token> header"} to an MCP initialize POST; https://app.retool.com/mcp answers identically (https://mcp.retool.com/mcp). 2026-09-12 (P6-04 repo sweep): first-party repository recorded at https://github.com/tryretool/agent-plugins - first-party agent plugins for Claude Code, Cowork, ChatGPT and Codex that wire the hosted server, NOT the server source. Evidence: the org tryretool, tied to retool.com by harvest_orgs.py domain evidence, and claude/retool/.mcp.json declares an http MCP server at ${user_config.retool_url}/mcp.

**Provenance**

- **Entry id**: 06-retool

- **Source file**: 06-revops-infra.md

- **Source line**: 405

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
