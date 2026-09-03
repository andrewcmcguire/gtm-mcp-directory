# HubSpot: MCP server status, API access gate and what it does

> An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

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
- **Probed**: 2026-09-03, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developers.hubspot.com/ai-tools/mcp

- [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - Free/Starter CRM tiers support private apps (API tokens) with real rate limits (100 req/10s per app, 250,000 req/day per account), scaling up to 1,000,000/day on Enterprise. A solo operator can get API access with no enterprise sales involvement.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: HubSpot (AI Forecasting)

- **Category**: [Forecasting & Revenue](../categories/forecasting-revenue.md)

- **MCP status there**: No MCP found

- **Gate there**: Paid, self-serve

- **Source**: 12-forecasting-revenue.md line 321

- **Canonical page**: [HubSpot](../tools/hubspot.md)

What that listing says it does: HubSpot's forecasting tool inside Sales Hub/Service Hub, turning pipeline data into revenue predictions via weighted-pipeline calculations plus an "AI forecasting" layer shown in-product. See 06-revops-infra.md for HubSpot's full platform entry (Breeze AI agents, official MCP servers, free API tier) - this entry...

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp)
- [https://knowledge.hubspot.com/ai-tools/use-breeze-ai](https://knowledge.hubspot.com/ai-tools/use-breeze-ai)
- [https://developers.hubspot.com/docs/api/usage-details](https://developers.hubspot.com/docs/api/usage-details)

3 source URLs. Raw sources field, verbatim:

https://developers.hubspot.com/ai-tools/mcp, https://knowledge.hubspot.com/ai-tools/use-breeze-ai, https://developers.hubspot.com/docs/api/usage-details

**Notes, verbatim from the file**
HubSpot runs two official MCP servers (Remote hosted + local Developer/CLI); numerous unofficial community HubSpot MCP servers also exist (e.g. axonops/hubspot-mcp) and should not be confused with the official one linked above.

**Provenance**

- **Entry id**: 06-hubspot

- **Source file**: 06-revops-infra.md

- **Source line**: 35

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
