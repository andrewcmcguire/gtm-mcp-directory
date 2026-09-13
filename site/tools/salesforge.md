# Salesforge: MCP server status, API access gate and what it does

> Multi-channel cold outreach platform (email + LinkedIn) with an AI SDR product ("Agent Frank") layered on top... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Salesforge

# Salesforge

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24
CLI: forge

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [salesforge.ai](https://salesforge.ai) · entry id 02-salesforge · source 02-engagement-outbound.md line 236

**What it does**
Multi-channel cold outreach platform (email + LinkedIn) with an AI SDR product ("Agent Frank") layered on top of standard sequencing.

**AI features, separated from automation with an AI label on it**
Agent Frank generates dynamically-written emails per selected tone (Playful, Formal, Curious, Urgent, etc.) - genuinely LLM-based copy generation, not static templates, per vendor description. Vendor claims Frank is "trained on proprietary data lake" and "modeled after top 1% reps" - unverifiable marketing language, flagged as vendor-stated only. Core sequencing/reply capture is plain automation with AI analysis layered on top.

**RevOps role**
Multichannel outbound sequencing with an AI SDR agent as an optional higher tier for more autonomous prospecting.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key via HTTP header (X-Salesforge-Key)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/SalesforgeAI/forge-mcp

- [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp)

**What this server exposes**

- **Tools named**: 109
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: SalesforgeAI/forge-mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **add_dnc_entries** No description was recorded with the name. evidence: in the server source · calling it reads

- **assign_sender_profiles_to_sequence** No description was recorded with the name. evidence: in the server source · calling it reads

- **assign_subsequence** No description was recorded with the name. evidence: in the server source · calling it reads

- **bulk_create_contacts** No description was recorded with the name. evidence: in the server source · calling it reads

- **bulk_update_contacts** No description was recorded with the name. evidence: in the server source · calling it reads

- **confirm_enrollment_preflight** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_action_node** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_condition_node** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_contact** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_sequence** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_subsequence** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_subsequence_trigger** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_webhook** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_workspace** No description was recorded with the name. evidence: in the server source · calling it reads

- **delete_sender_profile** No description was recorded with the name. evidence: in the server source · calling it reads

- **delete_sequence** No description was recorded with the name. evidence: in the server source · calling it reads

- **delete_sequence_node** No description was recorded with the name. evidence: in the server source · calling it reads

- **download_email_attachment** No description was recorded with the name. evidence: in the server source · calling it reads

- **download_email_attachments** No description was recorded with the name. evidence: in the server source · calling it reads

- **enroll_contacts** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_contact** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_mailbox** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_me** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_sequence** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_sequence_node** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_sequence_schedule** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_sequence_settings** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_thread** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_validation_results** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_webhook** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_workspace** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_bulk_dns_update** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_check_domain_availability** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_check_domain_availability_bulk** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_create_credit_balance** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_disable_autorenew** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_enable_autorenew** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_get_alternative_domains** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_get_credit_balance** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_get_domain_dns** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_list_domains** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_purchase_domains** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_update_credit_balance** No description was recorded with the name. evidence: in the server source · calling it reads

- **infraforge_update_domain_dns** No description was recorded with the name. evidence: in the server source · calling it reads

- **launch_sequence** No description was recorded with the name. evidence: in the server source · calling it reads

- **leadsforge_get_department_filters** No description was recorded with the name. evidence: in the server source · calling it reads

- **leadsforge_get_employee_range_filters** No description was recorded with the name. evidence: in the server source · calling it reads

- **leadsforge_get_seniority_filters** No description was recorded with the name. evidence: in the server source · calling it reads

- **leadsforge_search_lookalikes** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_action_types** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_condition_types** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_contacts** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_custom_variables** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_mailboxes** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_primebox_labels** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_primebox_threads** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_sender_profiles** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_sequence_branches** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_sequence_nodes** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_sequence_sender_profiles** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_sequences** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_subsequence_members** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_subsequence_parents** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_subsequence_triggers** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_webhooks** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_workspaces** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_bulk_disable_autorenew** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_bulk_dns_update** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_bulk_enable_autorenew** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_check_domain_availability** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_check_domain_availability_bulk** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_create_workspace** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_delete_domain_masking** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_delete_workspace** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_disable_autorenew** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_enable_autorenew** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_get_domain_dns** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_list_domains** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_list_workspaces** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_purchase_domain_masking** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_purchase_domains** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_transfer_domains** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_update_domain_dns** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_update_domain_forwards** No description was recorded with the name. evidence: in the server source · calling it reads

- **mailforge_update_workspace** No description was recorded with the name. evidence: in the server source · calling it reads

- **preflight_enrollments** No description was recorded with the name. evidence: in the server source · calling it reads

- **preview_enrollment_move** No description was recorded with the name. evidence: in the server source · calling it reads

- **primeforge_bulk_dns_update** No description was recorded with the name. evidence: in the server source · calling it reads

- **primeforge_buy_domains** No description was recorded with the name. evidence: in the server source · calling it reads

- **primeforge_create_mailboxes_for_domain** No description was recorded with the name. evidence: in the server source · calling it reads

- **primeforge_delete_domain** No description was recorded with the name. evidence: in the server source · calling it reads

- **primeforge_get_domain** No description was recorded with the name. evidence: in the server source · calling it reads

- **primeforge_get_domain_dns** No description was recorded with the name. evidence: in the server source · calling it reads

- **primeforge_list_domains** No description was recorded with the name. evidence: in the server source · calling it reads

- **primeforge_search_domains** No description was recorded with the name. evidence: in the server source · calling it reads

- **remove_enrollments** No description was recorded with the name. evidence: in the server source · calling it reads

- **remove_sender_profiles_from_sequence** No description was recorded with the name. evidence: in the server source · calling it reads

- **reply_to_email** No description was recorded with the name. evidence: in the server source · calling it reads

- **set_sequence_status** No description was recorded with the name. evidence: in the server source · calling it reads

- **start_email_validation** No description was recorded with the name. evidence: in the server source · calling it reads

- **update_action_node** No description was recorded with the name. evidence: in the server source · calling it reads

- **update_contact** No description was recorded with the name. evidence: in the server source · calling it reads

- **update_sender_profile** No description was recorded with the name. evidence: in the server source · calling it reads

- **update_sequence** No description was recorded with the name. evidence: in the server source · calling it reads

- **update_sequence_schedule** No description was recorded with the name. evidence: in the server source · calling it reads

- **update_sequence_settings** No description was recorded with the name. evidence: in the server source · calling it reads

- **update_thread_label** No description was recorded with the name. evidence: in the server source · calling it reads

- **warmforge_create_workspace** No description was recorded with the name. evidence: in the server source · calling it reads

- **warmforge_list_workspaces** No description was recorded with the name. evidence: in the server source · calling it reads

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: forge
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @salesforge/forge-cli
```

quoted from [https://www.npmjs.com/package/@salesforge/forge-cli](https://www.npmjs.com/package/@salesforge/forge-cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @salesforge/forge-cli 1.0.0](https://www.npmjs.com/package/@salesforge/forge-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

428 of 559 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp)

**On GitHub**

[github.com/SalesforgeAI](https://github.com/SalesforgeAI) tied to the vendor by rule 1, the directory already classed this repo first-party and its owner is an Organization, confidence strong

- **Public repositories**: 3, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [forge-mcp](https://github.com/SalesforgeAI/forge-mcp) | MCP server | MCP server for Salesforge products - manage contacts, sequences, domains, mailboxes and more from any MCP-compatible AI... | 2 | 2026-09-08 | |
| [forge-cli](https://github.com/SalesforgeAI/forge-cli) | CLI | Forge CLI | 1 | 2026-09-03 | |
| [emailengine-mcp](https://github.com/SalesforgeAI/emailengine-mcp) | MCP server | EmailEngine MCP built on top of learn.emailengine.app/docs | 0 | 2026-08-18 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 559 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Salesforge (Agent Frank)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: Official MCP

- **Gate there**: Paid, self-serve

- **Source**: 04-ai-sdr-agents.md line 372

- **Canonical page**: [Salesforge](../tools/salesforge.md)

What that listing says it does: An AI agent ("Agent Frank") that prospects, writes tailored outreach, sends across email and LinkedIn, manages follow-up sequences, and books meetings - positioned to either join a human team or fully replace one rep.

16 of the 559 entries are cross listed like this. They are why the entry count is 559 and the unique product count is 543. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.salesforge.ai/](https://www.salesforge.ai/)
- [https://www.salesforge.ai/pricing](https://www.salesforge.ai/pricing)
- [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp)

3 source URLs. Raw sources field, verbatim:

https://www.salesforge.ai/, https://www.salesforge.ai/pricing, https://github.com/SalesforgeAI/forge-mcp

**Notes, verbatim from the file**
Both API and MCP access are restricted to the Growth plan ($80/mo) and up, not the base Pro plan ($40/mo); not enterprise-only. A standalone Agent Frank plan runs $499/mo. The "top 1% sales rep" / proprietary-data-lake claims are unverified marketing and should not be repeated as fact.

**Provenance**

- **Entry id**: 02-salesforge

- **Source file**: 02-engagement-outbound.md

- **Source line**: 236

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
