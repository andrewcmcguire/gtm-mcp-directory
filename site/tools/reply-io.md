# Reply.io: MCP server status, API access gate and what it does

> Multichannel sales engagement platform for email, LinkedIn, call, and SMS outreach with an AI SDR product... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Reply.io

# Reply.io

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07
CLI: reply

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [reply.io](https://reply.io) · entry id 02-reply-io · source 02-engagement-outbound.md line 179

**What it does**
Multichannel sales engagement platform for email, LinkedIn, call, and SMS outreach with an AI SDR product layered on top.

**AI features, separated from automation with an AI label on it**
"Jason," Reply.io's AI SDR agent, claims to autonomously find prospects, send personalized messages, and manage responses - vendor-stated, genuinely LLM-driven per description but not independently verified. AI-generated icebreakers, first-step emails, and reply categorization are also vendor-claimed AI. Core sequencing/warmup/analytics are plain automation.

**RevOps role**
Multichannel outbound sequencing layer with an AI SDR agent tier positioned as a semi-autonomous prospecting add-on.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (personal API key over HTTPS, included in free trial)

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://reply.io/mcp/ ; repo https://github.com/reply-team/reply-mcp

- [https://reply.io/mcp/](https://reply.io/mcp/)
- [https://github.com/reply-team/reply-mcp](https://github.com/reply-team/reply-mcp)

**What this server exposes**

- **Tools named**: 71
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Repo read**: reply-team/reply-mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **reply_add_contact_to_sequence** Enroll up to 100 existing contacts into a sequence evidence: in the vendor docs · calling it writes

- **reply_add_knowledge_base_source** Add a web-page URL source to a knowledge base evidence: in the vendor docs · calling it writes

- **reply_approve_message** Approve one draft and send it immediately evidence: in the vendor docs · calling it writes

- **reply_assign_email_account_to_sequence** Link a mailbox to a sequence evidence: in the vendor docs · calling it reads

- **reply_assign_linkedin_account_to_sequence** Link a LinkedIn account to a sequence evidence: in the vendor docs · calling it reads

- **reply_assign_schedule_to_sequence** Set the sending schedule (business-hours window) evidence: in the vendor docs · calling it writes

- **reply_attach_knowledge_base_to_sequence** Attach a knowledge base to an AI SDR sequence evidence: in the vendor docs · calling it reads

- **reply_attach_offer_to_sequence** Attach an offer to an AI SDR sequence evidence: in the vendor docs · calling it reads

- **reply_attach_playbook_to_sequence** Attach a playbook to an AI SDR sequence evidence: in the vendor docs · calling it reads

- **reply_blacklist_contact** Blacklist a contact's email (or whole domain) from outreach evidence: in the vendor docs · calling it reads

- **reply_bulk_approve_messages** Approve and send up to 100 drafts (atomic batch) evidence: in the vendor docs · calling it writes

- **reply_change_contact_owner** Reassign up to 100 contacts to another user evidence: in the vendor docs · calling it reads

- **reply_change_inbox_category** Assign or clear a thread's workspace category evidence: in the vendor docs · calling it writes

- **reply_change_status_in_sequence** Set one contact's per-sequence status evidence: in the vendor docs · calling it writes

- **reply_compare_sequence_performance** Side-by-side metrics for up to 25 sequences evidence: in the vendor docs · calling it reads

- **reply_complete_task** Mark a task completed (with optional call resolution) evidence: in the vendor docs · calling it reads

- **reply_create_contact** Create a contact (needs a name plus email or LinkedIn URL) evidence: in the vendor docs · calling it writes

- **reply_create_knowledge_base** Create a knowledge base evidence: in the vendor docs · calling it writes

- **reply_create_offer** Create an offer Jason can pitch evidence: in the vendor docs · calling it writes

- **reply_create_playbook** Create a playbook (Team or Organization visibility) evidence: in the vendor docs · calling it writes

- **reply_create_reengagement_card** Add a reengagement card (with send-after days) evidence: in the vendor docs · calling it writes

- **reply_create_reply_handler** Add a reply handler (question type to instructions) evidence: in the vendor docs · calling it writes

- **reply_create_task** Create a standalone task (ToDo / Call / Meeting / LinkedIn and others) evidence: in the vendor docs · calling it writes

- **reply_delete_knowledge_base_source** Remove a URL source from a knowledge base evidence: in the vendor docs · calling it writes

- **reply_delete_reengagement_card** Remove a reengagement card evidence: in the vendor docs · calling it writes

- **reply_delete_reply_handler** Remove a reply handler evidence: in the vendor docs · calling it writes

- **reply_diagnose** Explain why a sequence isn't sending and how to fix it evidence: in a README table · calling it reads

- **reply_duplicate_playbook** Duplicate a playbook into a new one evidence: in the vendor docs · calling it reads

- **reply_filter_contacts** List contacts by list/sequence membership and/or free-text search evidence: in the vendor docs · calling it reads

- **reply_generate_offer_from_website** Draft offer fields from a company website (does not save) evidence: in the vendor docs · calling it reads

- **reply_get_app_map** Catalog of app areas with in-app navigation steps and links evidence: in the vendor docs · calling it reads

- **reply_get_contact_activity** Activity history for one contact (sends, opens, replies, calls) evidence: in the vendor docs · calling it reads

- **reply_get_inbox_emails** List inbox threads (email and LinkedIn) with short previews evidence: in the vendor docs · calling it reads

- **reply_get_knowledge_base** Full detail of one knowledge base (instructions, URL sources) evidence: in the vendor docs · calling it reads

- **reply_get_knowledge_base_article** Read a full Help Center article by slug evidence: in the vendor docs · calling it reads

- **reply_get_offer** Full offer content (ICP, value props, proof points, CTAs) evidence: in the vendor docs · calling it reads

- **reply_get_playbook** Full playbook, including the instruction body evidence: in the vendor docs · calling it reads

- **reply_get_reengagement_card** Full detail of one reengagement card evidence: in the vendor docs · calling it reads

- **reply_get_reply_handler** Full detail of one reply handler evidence: in the vendor docs · calling it reads

- **reply_get_sequence_stats** Email and LinkedIn performance metrics for one sequence evidence: in the vendor docs · calling it reads

- **reply_get_sequence_step_variants** Read a message step's A/B content variants (subject, body) evidence: in the vendor docs · calling it reads

- **reply_get_sequence_steps** List a sequence's ordered steps (type, delay, position, variant count) evidence: in the vendor docs · calling it reads

- **reply_list_email_accounts** List mailboxes with connection status, daily limits, tags evidence: in the vendor docs · calling it reads

- **reply_list_knowledge_bases** List Jason knowledge bases evidence: in the vendor docs · calling it reads

- **reply_list_linkedin_accounts** List connected LinkedIn accounts with health and tier evidence: in the vendor docs · calling it reads

- **reply_list_my_tasks** List your tasks, filterable by type / status / due window / contact evidence: in the vendor docs · calling it reads

- **reply_list_offers** List Jason offers (id plus name) evidence: in the vendor docs · calling it reads

- **reply_list_pending_approvals** The queue of Jason drafts awaiting approval evidence: in the vendor docs · calling it reads

- **reply_list_playbooks** List Jason playbooks (id, name, visibility) evidence: in the vendor docs · calling it reads

- **reply_list_reengagement_cards** List reengagement (win-back) cards in a knowledge base evidence: in the vendor docs · calling it reads

- **reply_list_reply_handlers** List reply handlers in a knowledge base evidence: in the vendor docs · calling it reads

- **reply_list_schedules** List sending schedules (timezone, default flag, slot counts) evidence: in the vendor docs · calling it reads

- **reply_mark_contacts_as_replied** Mark up to 100 contacts as replied (or clear the flag) evidence: in the vendor docs · calling it reads

- **reply_pause_sequence** Pause a sequence; halt in-flight scheduled steps evidence: in the vendor docs · calling it reads

- **reply_regenerate_message** Ask Jason to rewrite a pending draft (optionally with feedback) evidence: in the vendor docs · calling it reads

- **reply_reject_message** Reject a draft and remove the contact from the sequence evidence: in the vendor docs · calling it writes

- **reply_report_unsupported_request** Log a capability Reply.io does not have, for the product team evidence: in the vendor docs · calling it reads

- **reply_search_contacts** Look up contacts by exact email or LinkedIn URL evidence: in the vendor docs · calling it reads

- **reply_search_knowledge_base** Search the Reply.io Help Center for how-to articles evidence: in the vendor docs · calling it reads

- **reply_search_lists** Resolve a contact list name to its ListId evidence: in the vendor docs · calling it reads

- **reply_search_sequences** Find sequences by name / status / archive flag; returns per-sequence summary fields evidence: in the vendor docs · calling it writes

- **reply_search_team_members** Resolve a teammate name/email to their UserId evidence: in the vendor docs · calling it reads

- **reply_send_inbox_reply** Send a reply on an existing thread (body only in v1) evidence: in the vendor docs · calling it writes

- **reply_set_sequence_reply_mode** Set Jason's Review / Autonomous reply mode evidence: in the vendor docs · calling it writes

- **reply_start_sequence** Start or resume a sequence so it begins sending evidence: in the vendor docs · calling it writes

- **reply_update_contact** Patch fields on an existing contact evidence: in the vendor docs · calling it reads

- **reply_update_knowledge_base** Rename or edit a knowledge base's instructions evidence: in the vendor docs · calling it reads

- **reply_update_offer** Patch an offer evidence: in the vendor docs · calling it reads

- **reply_update_playbook** Patch a playbook evidence: in the vendor docs · calling it reads

- **reply_update_reengagement_card** Patch a reengagement card evidence: in the vendor docs · calling it reads

- **reply_update_reply_handler** Patch a reply handler evidence: in the vendor docs · calling it reads

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: reply
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g reply-cli
```

quoted from [https://docs.reply.io/cli/overview](https://docs.reply.io/cli/overview) on 2026-09-12, via npm

```
npx -y reply-cli
```

quoted from [https://docs.reply.io/cli/overview](https://docs.reply.io/cli/overview) on 2026-09-12, via npx

Login or key hint seen on the page:

reply auth

Subcommands seen with the binary:

api, auth, profile, skills, team

Where it was documented:

- [https://docs.reply.io/cli/overview](https://docs.reply.io/cli/overview) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/reply-team/reply-mcp](https://github.com/reply-team/reply-mcp)

**On GitHub**

[github.com/reply-team](https://github.com/reply-team) tied to the vendor by rule 1, account website https://reply.io has the vendor's domain, confidence strong

- **Public repositories**: 6, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [oleg-automate](https://github.com/reply-team/oleg-automate) | other | | 0 | 2026-09-03 | |
| [jason-ai](https://github.com/reply-team/jason-ai) | other | | 1 | 2026-08-18 | |
| [reply-cli](https://github.com/reply-team/reply-cli) | CLI | | 1 | 2026-08-14 | v0.9.0 |
| [reply-skills](https://github.com/reply-team/reply-skills) | other | | 1 | 2026-08-14 | |
| [reply-mcp](https://github.com/reply-team/reply-mcp) | MCP server | | 1 | 2026-08-03 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 649 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Reply.io (Jason AI)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: Official MCP

- **Gate there**: Paid, self-serve

- **Source**: 04-ai-sdr-agents.md line 182

- **Canonical page**: [Reply.io](../tools/reply-io.md)

What that listing says it does: A multichannel sales engagement platform whose AI layer ("Jason AI," per widely reported branding) generates outreach emails/follow-ups and automates sequencing across email, calls, and tasks.

16 of the 649 entries are cross listed like this. They are why the entry count is 649 and the unique product count is 633. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://reply.io/mcp/](https://reply.io/mcp/)
- [https://reply.io/](https://reply.io/)
- [https://github.com/reply-team/reply-mcp](https://github.com/reply-team/reply-mcp)

3 source URLs. Raw sources field, verbatim:

https://reply.io/mcp/, https://reply.io/, https://github.com/reply-team/reply-mcp

**Notes, verbatim from the file**
Vendor states API/webhook access is included across all pricing tiers starting at Standard ($59/mo); some MCP operations consume metered API credits. Site returned HTTP 403 to direct fetch and was retrieved via a read-only proxy - treat pricing figures as slightly less certain than directly-fetched pages. 2026-09-07: GitHub org reply-team, repo reply-mcp; README reads "Reply.io MCP Server - Connect Reply.io to your AI client" and links reply.io and docs.reply.io/reply-mcp (https://github.com/reply-team/reply-mcp).

**Provenance**

- **Entry id**: 02-reply-io

- **Source file**: 02-engagement-outbound.md

- **Source line**: 179

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
