# Amplemarket: MCP server status, API access gate and what it does

> An all-in-one sales engagement platform that finds leads, runs multichannel outbound sequences... Official MCP, Enterprise leaning. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Amplemarket

# Amplemarket

[Official MCP](../mcp/official.md)
[Enterprise leaning](../gates/enterprise-leaning.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [amplemarket.com](https://amplemarket.com) · entry id 02-amplemarket · source 02-engagement-outbound.md line 445

**What it does**
An all-in-one sales engagement platform that finds leads, runs multichannel outbound sequences (email/social/phone/voice), and optimizes email deliverability.

**AI features, separated from automation with an AI label on it**
Vendor markets "Duo Copilot" as an AI sales agent - generative personalization/objection handling in outreach copy, AI-driven signal detection across job changes/reviews/social/website visits, AI voice cloning for personalized voice notes, and AI company research/copywriting. Vendor-stated only; independent verification of what is genuinely ML-driven vs. templated was not possible from public sources.

**RevOps role**
Outbound execution layer (sequencing, deliverability, unified inbox) that would sit downstream of a data/enrichment source, feeding activity data into a CRM.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 sign-in with the Amplemarket account in the browser; the knowledge article says no API keys are needed. Rate limit 100 requests per minute per user.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.amplemarket.com/mcp ; https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server (endpoint https://mcp.amplemarket.com/mcp; product page https://www.amplemarket.com/mcp)

- [https://mcp.amplemarket.com/mcp](https://mcp.amplemarket.com/mcp)
- [https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server](https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server)
- [https://www.amplemarket.com/mcp](https://www.amplemarket.com/mcp)

**What this server exposes**

- **Tools named**: 52
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-11
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **act_on_duo_lead** Accept, schedule, dismiss, or regenerate a Duo lead. evidence: in the vendor docs · calling it writes

- **add_account_note** Add a note to an account. evidence: in the vendor docs · calling it writes

- **add_contact_note** Add a note to a contact. evidence: in the vendor docs · calling it writes

- **add_lead_list_column** Add a new custom column to a lead list. evidence: in the vendor docs · calling it writes

- **add_leads_to_list** Add leads to an existing list by email, LinkedIn URL, or name plus company. evidence: in the vendor docs · calling it writes

- **add_leads_to_sequence** Enroll leads in an existing sequence. evidence: in the vendor docs · calling it writes

- **append_stage_to_sequence** Add a step to an existing draft sequence. evidence: in the vendor docs · calling it writes

- **ask_analytics** Ask natural language questions about your Amplemarket analytics: sequences, emails, LinkedIn, phone calls, meetings, and more. evidence: in the vendor docs · calling it reads

- **check_excluded_domains** Check whether one or more domains are on your exclusion list. evidence: in the vendor docs · calling it reads

- **check_excluded_emails** Check whether one or more email addresses are on your exclusion list. evidence: in the vendor docs · calling it reads

- **complete_task** Mark a task as completed. evidence: in the vendor docs · calling it reads

- **create_lead_list** Create a new lead list. evidence: in the vendor docs · calling it writes

- **create_saved_search** Save a named set of people search filters as a saved search. evidence: in the vendor docs · calling it writes

- **create_sequence** Create a new empty draft sequence. evidence: in the vendor docs · calling it writes

- **create_task** Create a one-off task for a contact, such as a call, email, or custom action. evidence: in the vendor docs · calling it writes

- **create_workflow** Create a draft workflow from natural language instructions using the Amplemarket AI Workflows agent. evidence: in the vendor docs · calling it writes

- **enrich_company** Get company details, industry, size, funding, tech stack, location, by domain or LinkedIn URL. evidence: in the vendor docs · calling it reads

- **enrich_person** Get detailed profile data for a person by email, LinkedIn URL, or name plus company. evidence: in the vendor docs · calling it reads

- **get_account** Get detailed information about a specific account. evidence: in the vendor docs · calling it reads · required: account id

- **get_contact** Retrieve a single contact from your Amplemarket account by ID. evidence: in the vendor docs · calling it reads · required: contact id

- **get_inbox_thread** Get a single inbox thread with its full message history. evidence: in the vendor docs · calling it reads

- **get_lead_list** View a specific lead list and its leads. evidence: in the vendor docs · calling it reads

- **get_messaging_settings** Retrieve your Duo AI messaging configuration: value propositions, tone of voice, and sequence instructions. evidence: in the vendor docs · calling it reads

- **get_outbox_entry** Get a single outbox entry with its full rendered content and engagement details. evidence: in the vendor docs · calling it reads

- **get_persona** Get a persona's saved search filters and metadata. evidence: in the vendor docs · calling it reads

- **get_saved_search** Get the full details of a saved search, including its filters and lead count stats. evidence: in the vendor docs · calling it reads

- **get_sequence** Get full details of a specific sequence including all steps and their content. evidence: in the vendor docs · calling it reads

- **get_sequence_lead** Get full detail on a single lead in a sequence. evidence: in the vendor docs · calling it reads

- **get_workflow** Get the full definition of a workflow: triggers, enrollment filters, and every step. evidence: in the vendor docs · calling it reads

- **get_workflow_creation** Poll the result of a create_workflow request. evidence: in the vendor docs · calling it reads

- **list_accounts** List accounts in Amplemarket filtered by name, domain, owner, or tags. evidence: in the vendor docs · calling it reads

- **list_contacts** List contacts in Amplemarket and filter by name, email, or account. evidence: in the vendor docs · calling it reads

- **list_duo_leads** List Duo recommended leads for you or a rep you manage. evidence: in the vendor docs · calling it reads

- **list_inbox_threads** List Unibox inbox threads for email or LinkedIn. evidence: in the vendor docs · calling it reads

- **list_lead_lists** List your existing lead lists. evidence: in the vendor docs · calling it reads

- **list_outbox_entries** List scheduled and past outgoing steps for email or LinkedIn. evidence: in the vendor docs · calling it reads

- **list_personas** List the account's saved personas. evidence: in the vendor docs · calling it reads

- **list_saved_searches** List saved searches visible to you, with optional filtering by owner or name. evidence: in the vendor docs · calling it reads

- **list_sequence_leads** List leads enrolled in a sequence with optional filters by status. evidence: in the vendor docs · calling it reads

- **list_sequences** List sequences in your account, with optional filters by name, status, creator, and priority. evidence: in the vendor docs · calling it reads

- **list_tasks** List your tasks with optional filters by type, status, sequence, or due date. evidence: in the vendor docs · calling it reads

- **list_workflows** List workflows in your account, most recently edited first. evidence: in the vendor docs · calling it reads

- **remove_lead_list_column** Delete a column and its data from a lead list. evidence: in the vendor docs · calling it writes

- **remove_leads_from_lead_list** Remove one or more leads from a lead list. evidence: in the vendor docs · calling it writes

- **remove_leads_from_sequence** Remove one or more leads from a sequence. evidence: in the vendor docs · calling it writes

- **rename_lead_list_column** Rename an existing column in a lead list. evidence: in the vendor docs · calling it reads

- **search_companies** Search for companies by name, domain, industry, size, location, type, and more. evidence: in the vendor docs · calling it reads

- **search_people** Search for people using the same filters available in Amplemarket Searcher: name, title, seniority, department, location, company, industry, company size, and more. evidence: in the vendor docs · calling it reads

- **skip_task** Skip a task, removing it from your queue without completing it. evidence: in the vendor docs · calling it reads

- **update_lead_list_entry** Update one or more cell values for a specific lead in a list. evidence: in the vendor docs · calling it writes

- **update_sequence_lead** Update the dynamic field values of a lead already enrolled in a sequence. evidence: in the vendor docs · calling it writes

- **update_sequence_stage** Edit the content of an existing step in a draft sequence. evidence: in the vendor docs · calling it reads

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise leaning

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-leaning (any customer can self-generate a key at Settings > API, but there is no card checkout - every tier's CTA is a sales form and the lowest published tier is Startup at $600/mo annual)

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/amplemarket](https://github.com/amplemarket) tied to the vendor by rule 3, account website https://amplemarket.com has the vendor's domain, confidence strong

- **Public repositories**: 4, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-08-18

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [skills](https://github.com/amplemarket/skills) | other | Amplemarket skills | 5 | 2026-08-18 | workflow-migration-v3.2.0 |
| [.github](https://github.com/amplemarket/.github) | other | Amplemarket Public Github profile | 1 | 2025-07-03 | |
| [ample_sfdc_flow_action](https://github.com/amplemarket/ample_sfdc_flow_action) | infrastructure | | 1 | 2025-05-27 | |
| [amplemarket_zendesk](https://github.com/amplemarket/amplemarket_zendesk) | other | Amplemarket Zendesk app | 1 | 2021-03-31 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Amplemarket (Duo Copilot)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: Official MCP

- **Gate there**: Paid, self-serve

- **Source**: 04-ai-sdr-agents.md line 410

- **Canonical page**: [Amplemarket](../tools/amplemarket.md)

What that listing says it does: An all-in-one sales platform (lead gen + multichannel engagement + deliverability) with an AI agent layer ("Duo Copilot") that detects buying signals, writes and A/B-tests email copy (including AI voice-cloned voice notes), runs multichannel sequences, and suggests meeting follow-ups.

16 of the 336 entries are cross listed like this. They are why the entry count is 336 and the unique product count is 320. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.amplemarket.com/](https://www.amplemarket.com/)
- [https://glama.ai/mcp/servers?query=amplemarket](https://glama.ai/mcp/servers?query=amplemarket)
- [https://www.amplemarket.com/pricing](https://www.amplemarket.com/pricing)
- [https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server](https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server)
- [https://www.amplemarket.com/mcp](https://www.amplemarket.com/mcp)
- [https://mcp.amplemarket.com/mcp](https://mcp.amplemarket.com/mcp)

6 source URLs. Raw sources field, verbatim:

https://www.amplemarket.com/, https://glama.ai/mcp/servers?query=amplemarket, https://www.amplemarket.com/pricing, https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server, https://www.amplemarket.com/mcp, https://mcp.amplemarket.com/mcp

**Notes, verbatim from the file**
No public API/developer-docs page was found (an /api path 404'd, help-center subdomain unreachable) - could not confirm whether a general-purpose API exists at all. The one MCP hit indexed under Amplemarket's name (glama.ai/mcp/servers/artem-amplemarket/amplemarket-pylon-mcp) only searches Amplemarket's Pylon-hosted help-center articles, not the sales platform - not counted as a product MCP. [api_gate 2026-08-25] Reclassified unknown -> enterprise-leaning from the vendor's own page (https://www.amplemarket.com/pricing): any customer can self-generate a key at Settings > API, but there is no card checkout - every tier's CTA is a sales form and the lowest published tier is Startup at $600/mo annual. 2026-09-02: mcp_status none-found -> official, reconciled with the Amplemarket (Duo Copilot) entry in 04-ai-sdr-agents.md, which already recorded it. The help-center subdomain is reachable now: https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server returned 200 and documents the endpoint https://mcp.amplemarket.com/mcp (OAuth 2.0 sign-in, no API keys; Claude, ChatGPT, Claude Code, Cursor and any remote-capable client; prospect search, enrichment, sequences, lead lists, workflows, analytics; enrichment via MCP costs 0.5 credits). The endpoint answered 401 with a Bearer challenge today, which is the expected behaviour of an OAuth-gated MCP server. https://www.amplemarket.com/mcp links to the same guide. 2026-09-07: https://mcp.amplemarket.com/mcp returned 401 "Jwt is missing" to an MCP initialize POST. Vendor-owned mcp. subdomain (https://mcp.amplemarket.com/mcp).

**Provenance**

- **Entry id**: 02-amplemarket

- **Source file**: 02-engagement-outbound.md

- **Source line**: 445

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
