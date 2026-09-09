# Smartlead: MCP server status, API access gate and what it does

> Cold email outreach platform for managing campaigns across many mailboxes, with built-in deliverability... Official MCP, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Smartlead

# Smartlead

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-02
CLI: smartlead

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [smartlead.ai](https://smartlead.ai) · entry id 02-smartlead · source 02-engagement-outbound.md line 141

**What it does**
Cold email outreach platform for managing campaigns across many mailboxes, with built-in deliverability infrastructure and a unified reply inbox.

**AI features, separated from automation with an AI label on it**
"SmartAgents"/"SmartAI Bot" claim to research leads and draft persona-specific copy via generative AI - genuinely LLM-based per vendor description. "AI-powered" warmup is mostly scripted open/read/reply simulation, borderline as "AI." Sender rotation, DNS setup, and verification are plain automation.

**RevOps role**
Outbound email sequencing/deliverability layer with agent-style lead research and reply-triage add-ons.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key, passed as the user_api_key query parameter on the SSE endpoint URL; SSE transport only (the help article says streamable HTTP is not supported), and the vendor FAQ says only Claude Desktop is supported for now

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server](https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server (first-party; endpoint https://mcp.smartlead.ai/sse?user_api_key=YOUR_API_KEY. Community alternative: https://github.com/LeadMagic/smartlead-mcp-server, listed at https://www.pulsemcp.com/servers/leadmagic-smartlead)

- [https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server](https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server)
- [https://mcp.smartlead.ai/sse?user_api_key=YOUR_API_KEY](https://mcp.smartlead.ai/sse?user_api_key=YOUR_API_KEY)
- [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server)
- [https://www.pulsemcp.com/servers/leadmagic-smartlead](https://www.pulsemcp.com/servers/leadmagic-smartlead)

**What this server exposes**

- **Tools named**: 116
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-09
- **Repo read**: LeadMagic/smartlead-mcp-server
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **smartlead_add_client_to_system** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_add_email_account_to_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_add_lead_to_global_blocklist** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_add_leads_to_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_add_or_update_campaign_webhook** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_campaign_follow_up_reply_rate** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_campaign_lead_to_reply_time** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_campaign_leads_take_for_first_reply** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_campaign_list** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_campaign_overall_stats** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_campaign_response_stats** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_campaign_status_stats** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_client_list** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_client_month_wise_count** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_client_overall_stats** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_day_wise_overall_stats** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_day_wise_positive_reply_stats** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_lead_category_wise_response** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_lead_overall_stats** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_mailbox_domain_wise_health_metrics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_mailbox_name_wise_health_metrics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_mailbox_overall_stats** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_mailbox_provider_wise_overall_performance** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_overall_stats_v2** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_analytics_team_board_overall_stats** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_auto_generate_mailboxes** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_create_automated_placement_test** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_create_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_create_client** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_create_client_api_key** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_create_email_account** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_create_folder** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_create_manual_placement_test** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_delete_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_delete_campaign_webhook** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_delete_client_api_key** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_delete_folder** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_delete_lead_by_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_delete_tests_in_bulk** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_download_campaign_data** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_export_campaign_data** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_fetch_all_campaigns_using_lead_id** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_fetch_all_leads_from_account** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_fetch_campaign_analytics_by_date_range** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_fetch_lead_by_email** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_fetch_lead_categories** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_fetch_lead_message_history** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_fetch_leads_from_global_blocklist** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_forward_reply** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_all_clients** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_all_email_accounts** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_all_folders** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_blacklists** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaign_lead_statistics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaign_mailbox_statistics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaign_sequence** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaign_sequence_analytics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaign_statistics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaign_statistics_by_date_range** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaign_top_level_analytics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaign_top_level_analytics_by_date_range** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_campaigns_with_analytics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_client_api_keys** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_dkim_details** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_domain_blacklist** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_domain_list** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_email_account_by_id** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_email_reply_headers** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_folder_by_id** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_geo_wise_report** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_ip_blacklist_count** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_ip_details** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_mailbox_count** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_mailbox_summary** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_provider_wise_report** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_rdns_report** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_region_wise_provider_ids** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_schedule_history** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_sender_account_list** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_sender_account_wise_report** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_spam_filter_report** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_spam_test_details** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_spam_test_email_content** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_spf_details** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_team_details** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_vendors** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_warmup_stats_by_email_account_id** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_webhooks_by_campaign_id** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_get_webhooks_publish_summary** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_list_all_tests** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_list_campaigns** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_list_email_accounts_per_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_list_leads_by_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_pause_lead_by_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_place_order_for_mailboxes** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_reconnect_failed_email_accounts** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_remove_email_account_from_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_reply_to_lead_from_master_inbox** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_reset_client_api_key** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_resume_lead_by_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_retrigger_failed_events** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_save_campaign_sequence** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_search_domain** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_stop_automated_test** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_unsubscribe_lead_from_all_campaigns** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_unsubscribe_lead_from_campaign** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_update_campaign_schedule** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_update_campaign_settings** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_update_campaign_status** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_update_email_account** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_update_email_account_tag** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_update_email_account_warmup** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_update_lead_by_id** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_update_lead_category** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **smartlead_view_download_statistics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-09. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: smartlead
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-09

Install, as the source shows it:

```
npm install -g @smartlead/cli
```

quoted from [https://www.npmjs.com/package/@smartlead/cli](https://www.npmjs.com/package/@smartlead/cli) on 2026-09-09, via npm

Packages seen, with the version on 2026-09-09:

- [npm: @smartlead/cli 0.1.0](https://www.npmjs.com/package/@smartlead/cli)
- [npm: @bcharleson/smartlead-cli 0.1.13, third party](https://www.npmjs.com/package/@bcharleson/smartlead-cli)
- [pypi: smartlead-cli 0.1.4, third party](https://pypi.org/project/smartlead-cli/)
- [pypi: smartlead-cli 0.1.4, third party](https://pypi.org/project/smartlead-cli/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-09.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server)

**On GitHub**

No GitHub organisation could be tied to smartlead.ai with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

6 candidate accounts seen and rejected by the evidence rules: LeadMagic, Smartleader, smartleadmagnet, Smartlead-Public, Smartlead-AI-promo. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.smartlead.ai/pricing](https://www.smartlead.ai/pricing)
- [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server)
- [https://www.pulsemcp.com/servers/leadmagic-smartlead](https://www.pulsemcp.com/servers/leadmagic-smartlead)
- [https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server](https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server)

4 source URLs. Raw sources field, verbatim:

https://www.smartlead.ai/pricing, https://github.com/LeadMagic/smartlead-mcp-server, https://www.pulsemcp.com/servers/leadmagic-smartlead, https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server

**Notes, verbatim from the file**
API/webhooks/CRM integration require the Pro plan ($94/mo) or higher, not the base Base plan ($39/mo). No official first-party MCP found - several overlapping community implementations exist with varying maintenance; verify before adopting. 2026-09-02: mcp_status community -> official. Smartlead's own help center now documents a first-party server at https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server: endpoint mcp.smartlead.ai/sse with the API key in the URL, SSE only, Claude Desktop only per the vendor FAQ, covering campaign data, diagnostics and lead retrieval. The earlier "no official MCP" sentence is superseded. The LeadMagic community server stays listed as the alternative for clients that need stdio or streamable HTTP.

**Provenance**

- **Entry id**: 02-smartlead

- **Source file**: 02-engagement-outbound.md

- **Source line**: 141

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-09

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
