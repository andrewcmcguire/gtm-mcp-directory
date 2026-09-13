# HubSpot: MCP server status, API access gate and what it does

> An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
HubSpot

# HubSpot

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24
CLI: hs

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [hubspot.com](https://hubspot.com) · entry id 06-hubspot · source 06-revops-infra.md line 35

**What it does**
An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform.

**AI features, separated from automation with an AI label on it**
Breeze is HubSpot's real AI layer - a conversational Assistant plus autonomous Agents (Customer Agent for support deflection, Prospecting Agent for outreach, Content Agent for content generation) that run independently rather than just answering questions; the older ChatSpot product has been folded into Breeze. Most of HubSpot's workflow tooling outside Breeze remains conventional rules-based automation.

**RevOps role**
Popular CRM/marketing-hub for SMB-to-mid-market RevOps stacks; the MCP servers let AI coding/agent tools (Claude, Cursor, ChatGPT) read/write HubSpot data directly, alongside HubSpot's own in-product Breeze agents.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 for the hosted Remote MCP Server (migrating to OAuth 2.1 with PKCE + refresh-token rotation), explicitly excluding custom Sensitive Data Properties/PHI; the separate local Developer MCP Server authenticates via the HubSpot CLI.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developers.hubspot.com/ai-tools/mcp

- [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp)

**What this server exposes**

- **Tools named**: 25
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **discover_hubspot_schema** Search HubSpot schema to discover available object types, or look up specific known types directly evidence: in the vendor docs · calling it reads

- **get_campaign_attribution_reports** Get revenue and deal attribution data for campaigns, scoped to closed-won deal attribution evidence: in the vendor docs · calling it reads

- **get_content_analytics_report** Run content analytics across landing pages, website pages, and blog posts evidence: in the vendor docs · calling it reads

- **get_conversation_channel_metadata** List the inboxes, channels, and channel instances available in the account evidence: in the vendor docs · calling it reads

- **get_crm_objects** Fetch one or more CRM objects by their IDs in a single request evidence: in the vendor docs · calling it reads

- **get_marketing_email_analytics** Get analytics data for marketing emails based on sends within a given date range evidence: in the vendor docs · calling it reads

- **get_organization_details** Lists organization-wide teams, job titles, seat counts, and account information evidence: in the vendor docs · calling it reads

- **get_properties** Get full property definitions, including data types and enumeration values evidence: in the vendor docs · calling it reads

- **get_user_details** Returns the authenticated user's information, account details, and per-object access evidence: in the vendor docs · calling it reads

- **manage_blog_post** Create, update, publish, and inspect HubSpot blog posts evidence: in the vendor docs · calling it writes

- **manage_campaign_objects** Create or update marketing campaigns and manage campaign asset associations evidence: in the vendor docs · calling it writes

- **manage_crm_objects** Create or update CRM records or activities evidence: in the vendor docs · calling it writes

- **manage_landing_page** Create, edit, style, publish, clone, and inspect landing pages evidence: in the vendor docs · calling it writes

- **manage_marketing_email** Manage marketing email settings and content evidence: in the vendor docs · calling it reads

- **manage_onboarding** Assess an account's CRM onboarding status and guide users through onboarding steps evidence: in the vendor docs · calling it reads

- **query_crm_data** Query HubSpot CRM data using SQL with HubSpot-specific extensions evidence: in the vendor docs · calling it reads

- **read_campaign_data** Read campaign analytics, asset metrics, or contact data in a single operation evidence: in the vendor docs · calling it reads

- **render_asset** Display a read-only preview card for a HubSpot asset such as a landing page or blog post evidence: in the vendor docs · calling it writes

- **render_landing_page_ui** Display a landing page preview card with an editor link evidence: in the vendor docs · calling it reads

- **search_conversations** Search conversations and messages from HubSpot inboxes evidence: in the vendor docs · calling it reads

- **search_crm_objects** Search and filter CRM records using filter groups, text queries, sorting, and pagination evidence: in the vendor docs · calling it reads

- **search_owners** Find CRM record owners by name or email, or look up owners by ID evidence: in the vendor docs · calling it reads

- **search_properties** Find property definitions for an object type using keyword search evidence: in the vendor docs · calling it reads

- **submit_feedback** Send feedback about the MCP server experience to HubSpot evidence: in the vendor docs · calling it writes

- **tool_guidance** Retrieve usage instructions and guidance for one or more HubSpot MCP tools evidence: in the vendor docs · calling it reads

119 of the 251 entries that record an official or community MCP server carry a harvested tool list. The other 132 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: hs
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @hubspot/cli
```

quoted from [https://www.npmjs.com/package/@hubspot/cli](https://www.npmjs.com/package/@hubspot/cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @hubspot/cli 8.14.0](https://www.npmjs.com/package/@hubspot/cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - Free/Starter CRM tiers support private apps (API tokens) with real rate limits (100 req/10s per app, 250,000 req/day per account), scaling up to 1,000,000/day on Enterprise. A solo operator can get API access with no enterprise sales involvement.

**API documentation**

No documentation URL recorded.

374 of 468 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/HubSpot/hubspot-mcp-plugins](https://github.com/HubSpot/hubspot-mcp-plugins)

**On GitHub**

[github.com/HubSpot](https://github.com/HubSpot) tied to the vendor by rule 3, account website http://product.hubspot.com/ has the vendor's domain, confidence strong

- **Public repositories**: 99, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 5 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [HubSpot-public-api-spec-collection](https://github.com/HubSpot/HubSpot-public-api-spec-collection) | API client | | 45 | 2026-09-08 | |
| [agent-cli-skills](https://github.com/HubSpot/agent-cli-skills) | CLI | | 23 | 2026-09-08 | |
| [hubspot-project-components](https://github.com/HubSpot/hubspot-project-components) | docs or examples | Provides sample components for HubSpot projects. | 25 | 2026-09-08 | 2.3.0 |
| [hubspot-cms-vscode](https://github.com/HubSpot/hubspot-cms-vscode) | plugin or integration | A HubL language extension for the Visual Studio Code IDE, allowing for :rocket: fast local HubSpot CMS Platform... | 75 | 2026-09-08 | v1.7.5 |
| [boomslang](https://github.com/HubSpot/boomslang) | other | Python, but Java | 6 | 2026-09-08 | build-cfcfca4ac2ca188e3acd2a3abe8bed21bc281917 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 468 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: HubSpot (AI Forecasting)

- **Category**: [Forecasting & Revenue](../categories/forecasting-revenue.md)

- **MCP status there**: No MCP found

- **Gate there**: Paid, self-serve

- **Source**: 12-forecasting-revenue.md line 321

- **Canonical page**: [HubSpot](../tools/hubspot.md)

What that listing says it does: HubSpot's forecasting tool inside Sales Hub/Service Hub, turning pipeline data into revenue predictions via weighted-pipeline calculations plus an "AI forecasting" layer shown in-product. See 06-revops-infra.md for HubSpot's full platform entry (Breeze AI agents, official MCP servers, free API tier) - this entry...

16 of the 468 entries are cross listed like this. They are why the entry count is 468 and the unique product count is 452. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp)
- [https://knowledge.hubspot.com/ai-tools/use-breeze-ai](https://knowledge.hubspot.com/ai-tools/use-breeze-ai)
- [https://developers.hubspot.com/docs/api/usage-details](https://developers.hubspot.com/docs/api/usage-details)
- [https://github.com/HubSpot/hubspot-mcp-plugins](https://github.com/HubSpot/hubspot-mcp-plugins)

4 source URLs. Raw sources field, verbatim:

https://developers.hubspot.com/ai-tools/mcp, https://knowledge.hubspot.com/ai-tools/use-breeze-ai, https://developers.hubspot.com/docs/api/usage-details, https://github.com/HubSpot/hubspot-mcp-plugins

**Notes, verbatim from the file**
HubSpot runs two official MCP servers (Remote hosted + local Developer/CLI); numerous unofficial community HubSpot MCP servers also exist (e.g. axonops/hubspot-mcp) and should not be confused with the official one linked above. 2026-09-09 (P6-04 repo sweep): first-party repository recorded at https://github.com/HubSpot/hubspot-mcp-plugins, the org HubSpot, last push 2026-09-08. Its README reads "Repo containing the configuration for the HubSpot MCP Server to be added to Claude Code", so it carries the server's client configuration, not the server source. The org also owns https://github.com/HubSpot/mcp-server, described "MCP Server for HubSpot", but a contents read on 2026-09-09 returned an EMPTY repository, so it is named here and deliberately not recorded as a source.

**Provenance**

- **Entry id**: 06-hubspot

- **Source file**: 06-revops-infra.md

- **Source line**: 35

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
