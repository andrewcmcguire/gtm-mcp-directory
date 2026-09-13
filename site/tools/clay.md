# Clay: MCP server status, API access gate and what it does

> A spreadsheet-style workflow/orchestration tool that runs lead and company records through "waterfall"... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Clay

# Clay

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [clay.com](https://clay.com) · entry id 01-clay · source 01-data-enrichment.md line 46

**What it does**
A spreadsheet-style workflow/orchestration tool that runs lead and company records through "waterfall" lookups across 100-200+ third-party data providers (Apollo, Lusha, Clearbit, etc.) and chains automation steps ("recipes") to build, enrich, and route prospect lists into a CRM or sequencer.

**AI features, separated from automation with an AI label on it**
"Claygent" is a genuine LLM agent that can browse the web and do open-ended research inside a workflow step (e.g., "find this company's funding stage"), plus an AI formula/code generator for building enrichment logic. This is real AI for the unstructured-research steps; the waterfall/enrichment core is deterministic API-calling across vendors, not AI itself.

**RevOps role**
Sits between raw data vendors and the CRM/outbound stack as the enrichment-orchestration layer a RevOps team builds once and reps or automations call into

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Session cookie - the same token used to log into app.clay.com in-browser, which grants full account access (tables, records, enrichments, CRM integrations, credits), not a scoped API key

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://www.clay.com/mcp](https://www.clay.com/mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.clay.com/mcp (docs: https://university.clay.com/docs/mcp-settings)

- [https://www.clay.com/mcp](https://www.clay.com/mcp)
- [https://university.clay.com/docs/mcp-settings](https://university.clay.com/docs/mcp-settings)

**What this server exposes**

- **Tools named**: 89
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: shanefirek/clay-mcp-public
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **clay_add_enrichment_provider** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_add_to_sequence** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_analyze_table** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_auto_enrich** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_batch_create_records** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_build_input_mapping** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_bulk_fetch_records** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_check_table_drift** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_compare_snapshots** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_ai_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_claygent_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_claygent_from_template** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_email_waterfall** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_enrichment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_formula_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_http_api_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_phone_waterfall** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_record** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_subroutine_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_table** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_text_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_view** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_waterfall_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_webhook_auth_token** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_webhook_table** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_create_workbook** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_delete_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_delete_records** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_delete_source** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_delete_view** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_discover** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_duplicate_table** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_duplicate_view** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_enrich_company** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_enrich_person** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_export_table** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_filter_view** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_find_funding** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_find_job_changes** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_find_linkedin_posts** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_find_news** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_find_similar_companies** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_full_lead_workflow** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_generate_formula** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_generate_prompt** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_action_schema** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_field_config** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_prompt_template** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_providers_by_category** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_record** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_registry** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_source** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_table** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_tech_stack** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_get_waterfall_presets** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_available_actions** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_claygents** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_enrichments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_integrations** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_prompt_templates** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_records** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_sources** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_table_enrichments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_tables** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_list_workbook_tables** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_lookup_company** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_lookup_person** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_push_to_hubspot** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_push_to_salesforce** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_push_to_sheets** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_research_company** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_run_enrichment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_score_leads** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_search_enrichments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_search_records** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_send_slack_notification** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_set_webhook_response_type** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_share_table** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_snapshot_table** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_snapshot_workspace** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_suggest_enrichments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_update_field** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_update_record** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_validate_emails** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_wait_for_enrichment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_wizard_find_companies** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_wizard_find_people** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **clay_write_personalized_email** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

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

- [https://github.com/shanefirek/clay-mcp-public](https://github.com/shanefirek/clay-mcp-public)

**On GitHub**

[github.com/clay-run](https://github.com/clay-run) tied to the vendor by rule 3, account website https://clay.com has the vendor's domain, confidence strong

- **Public repositories**: 11, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [public-docs](https://github.com/clay-run/public-docs) | docs or examples | MD files of Clay documentation | 5 | 2026-09-08 | |
| [agent-plugins](https://github.com/clay-run/agent-plugins) | CLI | Build with Clay in your AI coding agent - skills, MCP tools, and the clay CLI for Claude Code, Codex, and Cursor.... | 111 | 2026-09-03 | clay-cli-v0.16.0 |
| [action-template-nodejs](https://github.com/clay-run/action-template-nodejs) | docs or examples | A Clay Action Template - NodeJs | 1 | 2020-09-15 | |
| [base-app-starter](https://github.com/clay-run/base-app-starter) | docs or examples | Base Starter App | 1 | 2020-09-04 | |
| [keyword-lists](https://github.com/clay-run/keyword-lists) | other | Some keyword lists | 0 | 2020-02-05 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Build a target account list](../jobs/build-target-account-list.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 559 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.clay.com/mcp](https://www.clay.com/mcp)
- [https://university.clay.com/docs/mcp-settings](https://university.clay.com/docs/mcp-settings)
- [https://github.com/shanefirek/clay-mcp-public](https://github.com/shanefirek/clay-mcp-public)
- [https://www.landbase.com/blog/clay-pricing](https://www.landbase.com/blog/clay-pricing)
- [https://www.warmly.ai/p/blog/clay-pricing](https://www.warmly.ai/p/blog/clay-pricing)
- [https://michaelsaruggia.com/blog/clay-pricing-change-2026](https://michaelsaruggia.com/blog/clay-pricing-change-2026)
- [https://www.clay.com/integrations/action/find-a-persons-linkedin-via-name-and-company-smarte](https://www.clay.com/integrations/action/find-a-persons-linkedin-via-name-and-company-smarte)

7 source URLs. Raw sources field, verbatim:

https://www.clay.com/mcp, https://university.clay.com/docs/mcp-settings, https://github.com/shanefirek/clay-mcp-public, https://www.landbase.com/blog/clay-pricing, https://www.warmly.ai/p/blog/clay-pricing, https://michaelsaruggia.com/blog/clay-pricing-change-2026, https://www.clay.com/integrations/action/find-a-persons-linkedin-via-name-and-company-smarte

**Notes, verbatim from the file**
Self-serve plans exist (Free, Launch ~$185/mo, Growth ~$495/mo as of the March 2026 repricing) with a dual Data Credits / Actions system, so a solo operator can get in without sales - but real usage costs scale fast via credit top-ups (50% premium) and this pricing structure changed substantially in March 2026. A separate 73-tool community MCP (github.com/shanefirek/clay-mcp-public) also exists. Caution: "Clay" the personal-CRM app (clay.earth, github.com/mesh/clay-mcp) is an unrelated product with its own MCP - do not confuse it with Clay.com in this directory. 2026-09-03: Clay's integration catalog lists the action "Find a Person's LinkedIn via Name and Company with SMARTe", described as "This action enables users to find a person's LinkedIn profile using their name and company", returning Contact Social URL and billed by Clay Credits or Bring Your Own Account with no unit cost stated (https://www.clay.com/integrations/action/find-a-persons-linkedin-via-name-and-company-smarte); the Clay MCP docs list People Search, Company Search and Functions and name no LinkedIn-finder tool (https://university.clay.com/docs/mcp-settings).

**Provenance**

- **Entry id**: 01-clay

- **Source file**: 01-data-enrichment.md

- **Source line**: 46

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
