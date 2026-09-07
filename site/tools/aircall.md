# Aircall: MCP server status, API access gate and what it does

> A cloud phone system and call centre for sales and support teams (numbers, dialer campaigns, call recording,... Community MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Aircall

# Aircall

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [aircall.io](https://aircall.io) · entry id 02-aircall · source 02-engagement-outbound.md line 600

**What it does**
A cloud phone system and call centre for sales and support teams (numbers, dialer campaigns, call recording, SMS, CRM integrations) with a public REST API and webhooks.

**AI features, separated from automation with an AI label on it**
The vendor sells add-on AI (Voice Agents, Messaging Agents, AI Assist for call summaries and transcription) priced separately from the plan; the telephony core is not AI. No first-party MCP was found; the only servers are third-party wrappers over the public API.

**RevOps role**
The calling layer of an outbound stack; an MCP over it lets an agent log calls, pull recordings and run dialer campaigns from CRM context.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: api key. The community server takes an Aircall API ID and API token, which the public API checks as HTTP Basic auth ("The api_id is the username and the api_token is the password" per the vendor's developer docs). OAuth 2.0 exists for marketplace partner apps, not for this server.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/themobilefirstco/aircall-mcp-server (73 tools, stdio; a remote third-party wrapper also answers at https://aircall.usefulapi.io/mcp)

- [https://github.com/themobilefirstco/aircall-mcp-server](https://github.com/themobilefirstco/aircall-mcp-server)
- [https://aircall.usefulapi.io/mcp](https://aircall.usefulapi.io/mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's pricing page lists "250+ integrations and API access" on the Essentials plan, the entry tier, with the dollar amounts not rendered on the page on this date; the Custom plan carries a 25-licence minimum and "Access to API developer support". No free plan.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/themobilefirstco/aircall-mcp-server](https://github.com/themobilefirstco/aircall-mcp-server)

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://github.com/themobilefirstco/aircall-mcp-server](https://github.com/themobilefirstco/aircall-mcp-server)
- [https://aircall.io/pricing/](https://aircall.io/pricing/)
- [https://developers.aircall.io/api-references](https://developers.aircall.io/api-references)
- [https://aircall.usefulapi.io/mcp](https://aircall.usefulapi.io/mcp)

4 source URLs. Raw sources field, verbatim:

https://github.com/themobilefirstco/aircall-mcp-server, https://aircall.io/pricing/, https://developers.aircall.io/api-references, https://aircall.usefulapi.io/mcp

**Notes, verbatim from the file**
The GitHub README states "This MCP server is NOT built, maintained, or endorsed by Aircall", so this is community by the author's own declaration: MIT licensed, 73 tools across calls, contacts, users, teams, numbers, tags, webhooks, SMS, dialer campaigns and integrations, run locally over stdio. Probed 2026-09-07: POST of an MCP initialize to the third-party remote wrapper https://aircall.usefulapi.io/mcp returned HTTP 200 with a JSON-RPC result, serverInfo name "aircall-mcp" version "1.0.0" (protocolVersion 2025-06-18); the control POST to /zzz-not-a-route returned 403 with an HTML page. That server is live but it is usefulapi.io's, not Aircall's (see the usefulapi.io entry in 07-mcp-infrastructure.md), and a live wrapper does not make the status official. The vendor's pricing page rendered plan names and feature lists but the prices came through as empty placeholders, so no price is recorded. 2026-09-07: https://aircall.usefulapi.io/mcp returned 200 with a JSON-RPC initialize result to an MCP initialize POST (https://aircall.usefulapi.io/mcp).

**Provenance**

- **Entry id**: 02-aircall

- **Source file**: 02-engagement-outbound.md

- **Source line**: 600

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
