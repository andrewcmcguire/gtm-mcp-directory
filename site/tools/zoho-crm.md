# Zoho CRM: MCP server status, API access gate and what it does

> A full CRM platform for leads, contacts, deals, workflow automation and customisation, sold at the low end of... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Zoho CRM

# Zoho CRM

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [zoho.com/crm](https://zoho.com/crm) · entry id 06-zoho-crm · source 06-revops-infra.md line 598

**What it does**
A full CRM platform for leads, contacts, deals, workflow automation and customisation, sold at the low end of the market, which in 2026 shipped four separately scoped MCP servers so an agent can be given exactly as much CRM access as a task needs.

**AI features, separated from automation with an AI label on it**
Zoho markets AI agents on its Professional tier and above, and the MCP layer is presented as the way an outside model acts on CRM data. The four-server split is a governance design rather than an AI feature: the intelligence is on the client side.

**RevOps role**
System of record for cost-sensitive SMB and mid-market teams, and the clearest worked example in this directory of scoping an agent's CRM reach by choosing which server to connect rather than by trusting a permission model after the fact.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The vendor's page describes a four-step setup ending in "Authenticate via OAuth. Connect your Zoho CRM account. Your agent inherits your permissions and nothing beyond that."

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.zoho.com/crm/developer/mcp.html is the vendor's own MCP product page describing four servers (Data Insights, Data Operations, Modules, Workflow and Automation); per-server endpoints are issued from Zoho's in-product Server Registry and the host is mcp.zoho.com

- [https://www.zoho.com/crm/developer/mcp.html](https://www.zoho.com/crm/developer/mcp.html)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 380 entries that record an official or community MCP server carry a harvested tool list. The other 261 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's own pricing page lists APIs as a Standard-tier feature and describes them as "Connect Zoho CRM to any app and perform actions with 5000 API calls/day." The fetch on this date rendered prices in Indian rupees (Standard 800, Professional 1,400, Enterprise 2,400 per user per month), so no dollar figure is recorded here rather than converted. Every tier carries a self-serve free trial.

**API documentation**

No documentation URL recorded.

528 of 784 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/catalystbyzoho](https://github.com/catalystbyzoho) tied to the vendor by rule 3, account website https://catalyst.zoho.com has the vendor's domain, confidence strong

- **Public repositories**: 74, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-04

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [zcatalyst-sdk-js](https://github.com/catalystbyzoho/zcatalyst-sdk-js) | SDK | Modularized CATALYST SDK for JavaScript. | 3 | 2026-09-04 | v0.0.5 |
| [agent-skills](https://github.com/catalystbyzoho/agent-skills) | infrastructure | AI agent skills for Catalyst by Zoho - enables Claude, Gemini, Cursor, Copilot, and Windsurf to write deployment-ready... | 59 | 2026-08-28 | v2026.08.22-a720b7b |
| [slate](https://github.com/catalystbyzoho/slate) | docs or examples | Client framework examples and boilerplate templates. | 2 | 2026-08-24 | |
| [codex-plugin](https://github.com/catalystbyzoho/codex-plugin) | plugin or integration | Repository of OpenAI Codex plugins | 0 | 2026-08-16 | |
| [zcatalyst-cli](https://github.com/catalystbyzoho/zcatalyst-cli) | CLI | Official Command Line Interface for Catalyst By Zoho | 1 | 2026-08-12 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

513 of 784 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.zoho.com/crm/developer/mcp.html](https://www.zoho.com/crm/developer/mcp.html)
- [https://www.zoho.com/crm/zohocrm-pricing.html](https://www.zoho.com/crm/zohocrm-pricing.html)
- [https://mcp.zoho.com](https://mcp.zoho.com)

3 source URLs. Raw sources field, verbatim:

https://www.zoho.com/crm/developer/mcp.html, https://www.zoho.com/crm/zohocrm-pricing.html, https://mcp.zoho.com

**Notes, verbatim from the file**
Verified 2026-09-07: the host https://mcp.zoho.com answered a POST with HTTP 400 and a Zoho-formatted JSON body, {"status":"failure","data":{"error_code":"INVALID_REQUEST_METHOD","message":"The http request method type is not a valid one"}}, which proves a live Zoho service at that host but is NOT an MCP initialize response, because the per-server paths are issued from the in-product Server Registry and were not obtainable without an account. No bare endpoint is therefore recorded above and the mcp_url points at the vendor's own documentation page instead; SCHEMA law 1 is satisfied by that page, not by a probe. THE FOUR-SERVER SPLIT IS THE STORY and is worth a segment: Data Insights is read-only (pipeline questions with no write path at all), Data Operations is full CRUD, Modules can change schema and layouts, and Workflow and Automation can create workflow rules and blueprints. Almost every other CRM in this file ships one server and one blast radius. Zoho's own copy for the read-only server, "Read everything. Risk nothing", is the cleanest statement of the design anyone in this category has published. Caveat found on the page: its "Get started" button links to a signup URL carrying plan=enterprise, which sits oddly against the Standard-tier API line on the pricing page; the plan floor for MCP specifically was not stated anywhere that could be read and is not guessed here.

**Provenance**

- **Entry id**: 06-zoho-crm

- **Source file**: 06-revops-infra.md

- **Source line**: 598

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
