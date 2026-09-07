# monday.com (monday CRM): MCP server status, API access gate and what it does

> A work-management platform whose CRM product runs pipelines, contacts, accounts and deal activity as boards... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
monday.com (monday CRM)

# monday.com (monday CRM)

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [monday.com/crm](https://monday.com/crm) · entry id 06-monday-com · source 06-revops-infra.md line 550

**What it does**
A work-management platform whose CRM product runs pipelines, contacts, accounts and deal activity as boards and items, with a first-party remote MCP server that lets an AI client read and update that data on the user's behalf.

**AI features, separated from automation with an AI label on it**
The platform ships a "Sidekick" AI assistant, an agent builder and AI-drafted content, all metered in the same credit pool as other AI usage. The MCP server itself is plumbing: it lets an outside model act, and monday's own page is careful to say the tools inherit the connected user's permissions rather than adding any.

**RevOps role**
A self-serve CRM and workflow system of record for SMB and mid-market teams, and one of the few CRMs in this file whose MCP server is available on a free plan, which makes it the cheapest hands-on target in the category.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth for the remote server. The vendor states "monday MCP remote server connects via the secure OAuth protocol" and that an admin must first install the monday MCP app from the monday marketplace; the separate local server instead takes a monday.com API token on the command line.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.monday.com/mcp for the remote server (product page: https://monday.com/w/mcp; the separate open-source local server is documented at https://developer.monday.com/apps/docs/mondaycom-mcp-integration and published as @mondaydotcomorg/monday-api-mcp) ; repo https://github.com/mondaycom/mcp

- [https://mcp.monday.com/mcp](https://mcp.monday.com/mcp)
- [https://monday.com/w/mcp](https://monday.com/w/mcp)
- [https://developer.monday.com/apps/docs/mondaycom-mcp-integration](https://developer.monday.com/apps/docs/mondaycom-mcp-integration)
- [https://github.com/mondaycom/mcp](https://github.com/mondaycom/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the vendor's MCP page states "MCP is currently available for all monday.com plans. Admins must install the monday MCP app from the monday marketplace to enable access." monday.com's pricing page publishes a Free tier at "$0 free forever" for up to 2 seats, with Basic at $9, Standard at $12 and Pro at $19 per seat per month billed annually. Note that the paid tiers bundle monthly AI credits and the pricing page describes external agent and custom app access to monday data as something to "Buy more as needed", so heavy agent traffic is metered even where the connector itself is not gated.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/mondaycom/mcp](https://github.com/mondaycom/mcp)

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://monday.com/w/mcp](https://monday.com/w/mcp)
- [https://monday.com/pricing](https://monday.com/pricing)
- [https://developer.monday.com/apps/docs/mondaycom-mcp-integration](https://developer.monday.com/apps/docs/mondaycom-mcp-integration)
- [https://github.com/mondaycom/mcp](https://github.com/mondaycom/mcp)
- [https://mcp.monday.com/mcp](https://mcp.monday.com/mcp)

5 source URLs. Raw sources field, verbatim:

https://monday.com/w/mcp, https://monday.com/pricing, https://developer.monday.com/apps/docs/mondaycom-mcp-integration, https://github.com/mondaycom/mcp, https://mcp.monday.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.monday.com/mcp returned HTTP 401 with {"error":"invalid_token","error_description":"Missing or invalid access token"}, confirming a live auth-gated server. TWO SERVERS, NOT ONE, and they are easy to conflate: the remote OAuth server at mcp.monday.com/mcp that the marketing page documents, and an official open-source local server run over stdio via npx @mondaydotcomorg/monday-api-mcp with an API token, documented in the developer docs and requiring Node.js v20+. Both are first-party. The developer-docs page for the local server carries an "Updated 10 months ago" stamp. The admin-install requirement is the practical gate a solo operator will hit first: the connector is free on every plan but a workspace admin has to install the marketplace app before any user can connect, so on a shared account this is a permission problem rather than a billing one. monday's page also states the MCP operates entirely within monday's permission model and that access can be limited to specific workspaces. 2026-09-07: GitHub org mondaycom (homepage monday.com), repo mcp, 423 stars, pushed 2026-09-07. README: "monday.com MCP" with the npm badge for @mondaydotcomorg/monday-api-mcp; tree contains packages/agent-toolkit and a .mcp.json (https://github.com/mondaycom/mcp).

**Provenance**

- **Entry id**: 06-monday-com

- **Source file**: 06-revops-infra.md

- **Source line**: 550

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
