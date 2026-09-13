# Pipedrive: MCP server status, API access gate and what it does

> A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams. Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Pipedrive

# Pipedrive

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [pipedrive.com](https://pipedrive.com) · entry id 06-pipedrive · source 06-revops-infra.md line 81

**What it does**
A sales-pipeline-focused CRM built around deal-stage visualization and activity tracking for sales teams.

**AI features, separated from automation with an AI label on it**
Not independently characterized beyond the MCP layer in this research pass (marketing claims about a Pipedrive "Sales Assistant" were not verified against a primary source) - reported as unknown rather than repeated from memory. The MCP server itself is a connectivity feature, not an AI feature: it exposes CRM actions (search deals, create records, update contacts, schedule activities) to external AI assistants.

**RevOps role**
SMB/mid-market pipeline CRM; positions its MCP server as available to any plan tier, not gated behind enterprise, letting smaller teams connect AI assistants to live deal data without developer resources.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - "Connect in minutes through secure OAuth. No coding, no API development, no developer required." AI assistants can only see/edit what the logged-in Pipedrive user already has permission for; actions are logged for auditability.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://www.pipedrive.com/en/features/mcp-server](https://www.pipedrive.com/en/features/mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.pipedrive.com/mcp ; https://www.pipedrive.com/en/features/mcp-server

- [https://mcp.pipedrive.com/mcp](https://mcp.pipedrive.com/mcp)
- [https://www.pipedrive.com/en/features/mcp-server](https://www.pipedrive.com/en/features/mcp-server)

**What this server exposes**

- **Tools named**: 32
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **addActivity** Create a new activity evidence: in the vendor docs · calling it writes

- **addDeal** Create a new deal evidence: in the vendor docs · calling it writes

- **addLead** Create a new lead evidence: in the vendor docs · calling it writes

- **addNote** Adds a note attached to a deal, lead, contact or organization evidence: in the vendor docs · calling it reads

- **addOrganization** Create a new organization evidence: in the vendor docs · calling it writes

- **addPerson** Create a new contact evidence: in the vendor docs · calling it writes

- **convertLeadToDeal** Convert a lead into a deal evidence: in the vendor docs · calling it reads

- **getActivities** Fetch a list of activities evidence: in the vendor docs · calling it reads

- **getActivity** Fetch one specific activity evidence: in the vendor docs · calling it reads

- **getDeal** Fetch one specific deal evidence: in the vendor docs · calling it reads

- **getDeals** Fetch a list of deals evidence: in the vendor docs · calling it reads

- **getLead** Fetch one specific lead evidence: in the vendor docs · calling it reads

- **getLeadConversionStatus** Check whether a lead has been converted evidence: in the vendor docs · calling it reads

- **getLeads** Fetch a list of leads evidence: in the vendor docs · calling it reads

- **getNote** Fetch details of one specific note evidence: in the vendor docs · calling it reads

- **getNotes** Fetch the list of notes evidence: in the vendor docs · calling it reads

- **getOrganization** Fetch one specific organization evidence: in the vendor docs · calling it reads

- **getOrganizations** Fetch a list of organizations evidence: in the vendor docs · calling it reads

- **getPerson** Fetch one specific contact evidence: in the vendor docs · calling it reads

- **getPersons** Fetch a list of contacts evidence: in the vendor docs · calling it reads

- **getStage** Fetch details of one specific stage evidence: in the vendor docs · calling it reads

- **getStages** Fetch all stages in a pipeline evidence: in the vendor docs · calling it reads

- **searchDeals** Search deals by keyword evidence: in the vendor docs · calling it reads

- **searchLeads** Find leads by keyword or criteria evidence: in the vendor docs · calling it reads

- **searchOrganization** Search organizations by name or keyword evidence: in the vendor docs · calling it reads

- **searchPersons** Find contacts by name, email or other criteria evidence: in the vendor docs · calling it reads

- **updateActivity** Edit an existing activity evidence: in the vendor docs · calling it reads

- **updateDeal** Edit an existing deal evidence: in the vendor docs · calling it reads

- **updateLead** Edit an existing lead evidence: in the vendor docs · calling it reads

- **updateNote** Updates a specific note by its ID evidence: in the vendor docs · calling it reads

- **updateOrganization** Edit an existing organization evidence: in the vendor docs · calling it reads

- **updatePerson** Edit an existing contact evidence: in the vendor docs · calling it reads

119 of the 740 entries that record an official or community MCP server carry a harvested tool list. The other 621 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (for MCP access) - Pipedrive states the MCP server is available on all plans at no additional charge, metered by a token allotment included per plan with extra tokens purchasable. General (non-MCP) API access terms were not independently re-verified in this pass.

**API documentation**

No documentation URL recorded.

727 of 1251 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/pipedrive](https://github.com/pipedrive) tied to the vendor by rule 3, account website http://www.pipedrive.com has the vendor's domain, confidence strong

- **Public repositories**: 13, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [client-php](https://github.com/pipedrive/client-php) | SDK | Pipedrive API client for PHP | 64 | 2026-09-08 | 6.7.0 |
| [client-nodejs](https://github.com/pipedrive/client-nodejs) | SDK | Pipedrive API client for NodeJS | 234 | 2026-09-08 | v17.5.3 |
| [app-extensions-sdk](https://github.com/pipedrive/app-extensions-sdk) | SDK | SDK for Pipedrive app extensions | 8 | 2026-08-31 | |
| [create-pipedrive-app](https://github.com/pipedrive/create-pipedrive-app) | app | Scaffold a production-ready Pipedrive Marketplace app with OAuth, database, and App Extensions in seconds. | 4 | 2026-08-11 | |
| [test-public-npm-module](https://github.com/pipedrive/test-public-npm-module) | other | Public NPM module for testing publishing workflow | 0 | 2026-06-15 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 1,251 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Pipedrive (AI Sales Assistant / forecasting)

- **Category**: [Forecasting & Revenue](../categories/forecasting-revenue.md)

- **MCP status there**: No MCP found

- **Gate there**: Free to start

- **Source**: 12-forecasting-revenue.md line 150

- **Canonical page**: [Pipedrive](../tools/pipedrive.md)

What that listing says it does: Pipedrive's built-in AI-driven forecasting layer - not a separately branded "Insights" product, but the CRM's AI Sales Assistant plus probability-weighted pipeline forecasting math. See 06-revops-infra.md for Pipedrive's full CRM entry (general MCP server, OAuth, free-on-all-plans MCP access) - this entry covers only...

16 of the 1251 entries are cross listed like this. They are why the entry count is 1251 and the unique product count is 1235. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.pipedrive.com/en/features/mcp-server](https://www.pipedrive.com/en/features/mcp-server)
- [https://mcp.pipedrive.com/mcp](https://mcp.pipedrive.com/mcp)

2 source URLs. Raw sources field, verbatim:

https://www.pipedrive.com/en/features/mcp-server, https://mcp.pipedrive.com/mcp

**Notes, verbatim from the file**
A community/self-hosted alternative exists (github.com/WillDent/pipedrive-mcp-server) but is unofficial and separate from Pipedrive's own native server. 2026-09-07: https://mcp.pipedrive.com/mcp returned 401 {"success":false,"error":"unauthorized access","errorCode":401,"error_info":"Please check developers.pipedrive.com"} to an MCP initialize POST - a vendor-branded error on a vendor-owned mcp. subdomain (https://mcp.pipedrive.com/mcp).

**Provenance**

- **Entry id**: 06-pipedrive

- **Source file**: 06-revops-infra.md

- **Source line**: 81

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
