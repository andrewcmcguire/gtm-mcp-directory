# Close (Close CRM): MCP server status, API access gate and what it does

> A sales CRM built for inside-sales teams with built-in calling, email, and SMS alongside pipeline/lead... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Close (Close CRM)

# Close (Close CRM)

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [close.com](https://close.com) · entry id 06-close · source 06-revops-infra.md line 102

**What it does**
A sales CRM built for inside-sales teams with built-in calling, email, and SMS alongside pipeline/lead management - a communications-plus-CRM combo rather than a pure system of record.

**AI features, separated from automation with an AI label on it**
Close's pricing page reportedly references an "AI Sales Agent" but this was not independently verified against a primary product page in this pass - flagged as under-researched rather than asserted. The MCP server itself is connectivity (create leads, log calls, send SMS, manage tasks), not an AI feature.

**RevOps role**
SMB/startup sales CRM often chosen for native calling/SMS; its MCP server pitches "run ops tasks via Claude" as a differentiator for small sales teams without dedicated RevOps engineering.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Dual - OAuth 2.0 with Dynamic Client Registration (recommended; used by Claude, ChatGPT, Cursor) or API-key auth via custom headers (Close-API-Key, Close-Scope). Three scope tiers: mcp.read, mcp.write_safe, mcp.write_destructive.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://help.close.com/integrations/close-mcp-server](https://help.close.com/integrations/close-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.close.com/mcp ; https://help.close.com/integrations/close-mcp-server (redirect correction 2026-08-28: the address previously recorded here, help.close.com/docs/mcp-server, 308s to this one and this one returns 200. Endpoint: https://mcp.close.com/mcp)

- [https://mcp.close.com/mcp](https://mcp.close.com/mcp)
- [https://help.close.com/integrations/close-mcp-server](https://help.close.com/integrations/close-mcp-server)

**What this server exposes**

- **Tools named**: 116
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **activity_search** Search for activities. Results are returned ordered by date descending. evidence: in the vendor docs · calling it reads

- **aggregation** Perform an aggregation to answer questions like: How many emails were sent this week? evidence: in the vendor docs · calling it reads

- **apply_voice_agent_update** Apply a previously proposed voice agent update. evidence: in the vendor docs · calling it writes

- **close_product_knowledge_search** Search Close product documentation and knowledge base for relevant information. evidence: in the vendor docs · calling it reads

- **create_address** Add a new address to an existing lead (company). evidence: in the vendor docs · calling it writes

- **create_call_task** Schedule a call task on a lead, assigned to either a user or a voice agent. evidence: in the vendor docs · calling it writes

- **create_comment** Add a comment to a commentable object (note, call, opportunity, task, custom object, etc.). evidence: in the vendor docs · calling it writes

- **create_contact** Create a new contact for a lead. evidence: in the vendor docs · calling it writes

- **create_custom_activity_instance** Create a new custom activity instance on a lead. evidence: in the vendor docs · calling it writes

- **create_custom_object_instance** Create a new custom object instance on a lead. evidence: in the vendor docs · calling it writes

- **create_draft_email** Create a draft email on a lead. evidence: in the vendor docs · calling it writes

- **create_email_template** Create a new email template. evidence: in the vendor docs · calling it writes

- **create_lead** Create a new lead (company). evidence: in the vendor docs · calling it writes

- **create_lead_status** Create a new lead status. evidence: in the vendor docs · calling it writes

- **create_note** Create a new note on a lead. evidence: in the vendor docs · calling it writes

- **create_opportunity** Create a new opportunity. evidence: in the vendor docs · calling it writes

- **create_opportunity_status_tool** Create a new opportunity status. evidence: in the vendor docs · calling it writes

- **create_pipeline** Create a new opportunity pipeline. evidence: in the vendor docs · calling it writes

- **create_sms_template** Create a new SMS template. evidence: in the vendor docs · calling it writes

- **create_task** Create a new task for a lead. evidence: in the vendor docs · calling it writes

- **create_workflow** Create a new workflow (a.k.a. sequence) with Draft status. evidence: in the vendor docs · calling it writes

- **customized_builtin_labels** Return the customized builtin labels. evidence: in the vendor docs · calling it reads

- **delete_address** Delete an address from an existing lead (company). evidence: in the vendor docs · calling it writes

- **delete_call_task** Delete a call task. evidence: in the vendor docs · calling it writes

- **delete_contact** Permanently delete an existing contact. evidence: in the vendor docs · calling it writes

- **delete_custom_activity_instance** Permanently delete an existing custom activity instance. evidence: in the vendor docs · calling it writes

- **delete_custom_object_instance** Permanently delete an existing custom object instance. evidence: in the vendor docs · calling it writes

- **delete_email_template** Permanently delete an email template. evidence: in the vendor docs · calling it writes

- **delete_lead** Permanently delete an existing lead (company) by ID. evidence: in the vendor docs · calling it writes

- **delete_lead_smart_view** Permanently delete a lead smart view (saved search). evidence: in the vendor docs · calling it writes

- **delete_lead_status** Permanently delete a lead status. evidence: in the vendor docs · calling it writes

- **delete_note** Permanently delete an existing note. evidence: in the vendor docs · calling it writes

- **delete_opportunity** Permanently delete an opportunity. evidence: in the vendor docs · calling it writes

- **delete_opportunity_status_tool** Permanently delete an opportunity status. evidence: in the vendor docs · calling it writes

- **delete_pipeline** Permanently delete an opportunity pipeline. evidence: in the vendor docs · calling it writes

- **delete_sms_template** Permanently delete an SMS template. evidence: in the vendor docs · calling it writes

- **delete_task** Permanently delete an existing task by ID. evidence: in the vendor docs · calling it writes

- **enrich_field** Use AI to determine and set the value of a field on a lead or contact. evidence: in the vendor docs · calling it writes

- **fetch** Retrieve the contents of an arbitrary object by its ID. evidence: in the vendor docs · calling it reads

- **fetch_call** Fetch a single call activity by ID. evidence: in the vendor docs · calling it reads

- **fetch_call_task** Fetch a single call task by ID. evidence: in the vendor docs · calling it reads

- **fetch_comment** Fetch a single comment by ID. evidence: in the vendor docs · calling it reads

- **fetch_contact** Fetch an existing contact by ID. evidence: in the vendor docs · calling it reads

- **fetch_custom_activity_instance** Fetch an existing custom activity instance by ID. evidence: in the vendor docs · calling it reads

- **fetch_custom_object_instance** Fetch an existing custom object instance by ID. evidence: in the vendor docs · calling it reads

- **fetch_custom_object_type** Fetch a single custom object type by its ID. evidence: in the vendor docs · calling it reads

- **fetch_email_template** Fetch an email template by ID. evidence: in the vendor docs · calling it reads

- **fetch_invoice** Fetch one of the organization's billing invoices by id. evidence: in the vendor docs · calling it spends money

- **fetch_lead** Fetch an existing lead (company) by ID. evidence: in the vendor docs · calling it reads

- **fetch_lead_smart_view** Fetch a lead smart view (saved search) by ID. evidence: in the vendor docs · calling it reads

- **fetch_lead_status** Fetch a lead status by ID. evidence: in the vendor docs · calling it reads

- **fetch_meeting_transcript** Fetch a meeting's Notetaker transcript(s) by meeting activity ID. evidence: in the vendor docs · calling it reads

- **fetch_membership** Fetch one of the organization's members by user id. evidence: in the vendor docs · calling it reads

- **fetch_note** Fetch an existing note by ID. evidence: in the vendor docs · calling it reads

- **fetch_opportunity** Fetch a specific opportunity by ID. evidence: in the vendor docs · calling it reads

- **fetch_opportunity_status** Fetch an opportunity status by ID. evidence: in the vendor docs · calling it reads

- **fetch_pipeline_and_opportunity_statuses** Fetch an opportunity pipeline, including its opportunity statuses, by ID. evidence: in the vendor docs · calling it reads

- **fetch_role** Fetch one of the organization's roles by id, with every permission it grants. evidence: in the vendor docs · calling it reads

- **fetch_sms_template** Fetch an SMS template by ID. evidence: in the vendor docs · calling it reads

- **fetch_task** Fetch an existing task by ID. evidence: in the vendor docs · calling it reads

- **find_agent_configs** List all voice agents configured for the organization. evidence: in the vendor docs · calling it reads

- **find_call_outcomes** List all outcomes applicable to calls available in the organization. evidence: in the vendor docs · calling it reads

- **find_call_tasks** Find call tasks based on various filters. evidence: in the vendor docs · calling it reads

- **find_contact_custom_fields** List all contact custom fields defined for the organization. evidence: in the vendor docs · calling it reads

- **find_custom_activities** List all active (non-archived) Custom Activity Types in the organization. evidence: in the vendor docs · calling it reads

- **find_custom_activity_instances** Find a lead's custom activity instances based on various filters. evidence: in the vendor docs · calling it reads

- **find_custom_object_instances** Find a lead's custom object instances. evidence: in the vendor docs · calling it reads

- **find_custom_object_types** List all custom object types in the organization. evidence: in the vendor docs · calling it reads

- **find_email_templates** List or find email templates evidence: in the vendor docs · calling it reads

- **find_forms** List all web forms in the organization. evidence: in the vendor docs · calling it reads

- **find_groups** List all groups in the organization. evidence: in the vendor docs · calling it reads

- **find_invoices** Find the organization's billing invoices, newest first. evidence: in the vendor docs · calling it spends money

- **find_lead_custom_fields** List all lead custom fields defined for the organization. evidence: in the vendor docs · calling it reads

- **find_lead_smart_views** List lead smart views (saved searches). evidence: in the vendor docs · calling it reads

- **find_lead_statuses** List or find lead statuses for the organization evidence: in the vendor docs · calling it reads

- **find_meeting_outcomes** List all outcomes applicable to meetings available in the organization. evidence: in the vendor docs · calling it reads

- **find_memberships** List the organization's members with each member's role name. evidence: in the vendor docs · calling it reads

- **find_notes** Find notes based on various filters. evidence: in the vendor docs · calling it reads

- **find_opportunities** Find opportunities by status (active/won/lost), owner, lead, or close-date range. evidence: in the vendor docs · calling it reads

- **find_opportunity_custom_fields** List all opportunity custom fields defined for the organization. evidence: in the vendor docs · calling it reads

- **find_pipelines_and_opportunity_statuses** List all opportunity pipelines and their opportunity statuses in the organization. evidence: in the vendor docs · calling it reads

- **find_scheduling_links** List available scheduling links for the user and org. evidence: in the vendor docs · calling it reads

- **find_sms_templates** List or find SMS templates evidence: in the vendor docs · calling it reads

- **find_tasks** Find tasks based on various filters. evidence: in the vendor docs · calling it reads

- **find_voice_agents** List all voice agents configured for the organization. evidence: in the vendor docs · calling it reads

- **find_workflows** List or find workflows evidence: in the vendor docs · calling it reads

- **get_ai_credit_usage** AI credit usage for the billing account, broken down by feature. evidence: in the vendor docs · calling it spends money

- **get_billing_summary** Billing summary for the organization's billing account. evidence: in the vendor docs · calling it spends money

- **get_fields** Use this tool ONLY to get a list of fields for the aggregation tool. evidence: in the vendor docs · calling it reads

- **get_voice_agent_overview_report** Cross-agent rollup for the Voice Agents list page. evidence: in the vendor docs · calling it reads

- **get_voice_agent_performance_report** Performance metrics for one voice agent. evidence: in the vendor docs · calling it reads

- **get_voice_agents** Return detailed configuration for one or more voice agents. evidence: in the vendor docs · calling it reads

- **lead_search** Perform a simple lead search and return the initial set of results. evidence: in the vendor docs · calling it writes

- **list_membership_requests** List pending requests to join the current organization. evidence: in the vendor docs · calling it reads

- **list_roles** List the roles that can be assigned in the organization. evidence: in the vendor docs · calling it reads

- **org_info** Return general information about the organization and the user. evidence: in the vendor docs · calling it reads

- **org_users** Return active users (memberships) which are part of the current org. evidence: in the vendor docs · calling it reads

- **paginate_search** Paginate a search to retrieve more results. evidence: in the vendor docs · calling it reads

- **propose_voice_agent_update** Propose a voice agent configuration update from natural-language feedback. evidence: in the vendor docs · calling it writes

- **schedule_voice_agent_call** Schedule a voice agent to call a lead's contact. evidence: in the vendor docs · calling it writes

- **search** Perform a natural language search for leads or contacts. evidence: in the vendor docs · calling it reads

- **update_call_task** Update a call task. evidence: in the vendor docs · calling it writes

- **update_contact** Update an existing contact. evidence: in the vendor docs · calling it writes

- **update_custom_activity_instance** Update an existing custom activity instance. evidence: in the vendor docs · calling it writes

- **update_custom_object_instance** Update an existing custom object instance. evidence: in the vendor docs · calling it writes

- **update_draft_email** Update an existing draft email. evidence: in the vendor docs · calling it writes

- **update_email_template** Update an existing email template. evidence: in the vendor docs · calling it writes

- **update_lead** Update an existing lead (company). evidence: in the vendor docs · calling it writes

- **update_lead_smart_view** Update a lead smart view (saved search). evidence: in the vendor docs · calling it writes

- **update_lead_status** Update the label of an existing lead status. evidence: in the vendor docs · calling it writes

- **update_note** Update an existing note. evidence: in the vendor docs · calling it writes

- **update_opportunity** Update an existing opportunity. evidence: in the vendor docs · calling it writes

- **update_opportunity_status_tool** Update the label of an existing opportunity status. evidence: in the vendor docs · calling it writes

- **update_pipeline** Update an existing opportunity pipeline. evidence: in the vendor docs · calling it writes

- **update_sms_template** Update an existing SMS template. evidence: in the vendor docs · calling it writes

- **update_task** Update an existing task. evidence: in the vendor docs · calling it writes

119 of the 437 entries that record an official or community MCP server carry a harvested tool list. The other 318 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - no free tier; API access is included on every paid plan starting at Solo (~$19/user/mo standard). No enterprise-sales gate, but a subscription is required.

**API documentation**

No documentation URL recorded.

604 of 934 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/close](https://github.com/close) tied to the vendor by rule 3, account website https://close.com/ has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2025-08-28

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [.github](https://github.com/close/.github) | other | | 0 | 2025-08-28 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Place an outbound call](../jobs/place-outbound-call.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 934 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://help.close.com/integrations/close-mcp-server](https://help.close.com/integrations/close-mcp-server)
- [https://help.close.com/llms.txt](https://help.close.com/llms.txt)
- [https://mcp.close.com/mcp](https://mcp.close.com/mcp)

3 source URLs. Raw sources field, verbatim:

https://help.close.com/integrations/close-mcp-server, https://help.close.com/llms.txt, https://mcp.close.com/mcp

**Notes, verbatim from the file**
Supports HTTP Streamable transport and integrates with Claude (web/desktop/code), ChatGPT, Cursor, VS Code, and n8n per its own docs. A separate community CLI tool (bcharleson/close-crm-cli) also exists and is unofficial. 2026-09-07: Official MCP registry carries com.close/close-mcp (DNS-verified close.com namespace) with remote https://mcp.close.com/mcp; that URL returned 401 to an MCP initialize (https://mcp.close.com/mcp).

**Provenance**

- **Entry id**: 06-close

- **Source file**: 06-revops-infra.md

- **Source line**: 102

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
