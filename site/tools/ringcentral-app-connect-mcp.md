# RingCentral App Connect MCP: MCP server status, API access gate and what it does

> One of four MCP servers RingCentral publishes through its Labs programme; this one bridges RingCentral... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
RingCentral App Connect MCP

# RingCentral App Connect MCP

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [ringcentral.com](https://ringcentral.com) · entry id 02-ringcentral-app-connect-mcp · source 02-engagement-outbound.md line 561

**What it does**
One of four MCP servers RingCentral publishes through its Labs programme; this one bridges RingCentral telephony to whichever CRM the customer has linked through the App Connect browser extension, so an assistant can look up or create CRM contacts, log a call to the CRM and pull RingCentral call logs.

**AI features, separated from automation with an AI label on it**
None in this server. It is a telephony-to-CRM bridge with nine tools; the intelligence is entirely on the client side. RingCentral's separate AI features (AI Receptionist, call summaries) are not exposed through this particular server.

**RevOps role**
Call logging and CRM hygiene for a RingCentral phone stack, aimed at teams whose CRM has no MCP server of its own; the vendor's docs say so explicitly rather than overselling it.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth plus a second, separate CRM link. The docs describe a two-layer model: RingCentral identity via OAuth 2.0 or SSO established when the server is added to the AI client, and then a CRM connection linked through the App Connect Chrome extension rather than inside the AI client, with only one CRM connected per RingCentral account at a time.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://unified-crm-extension.labs.ringcentral.com/mcp (docs: https://mcp.labs.ringcentral.com/docs/servers/app-connect/; server registry: https://mcp.labs.ringcentral.com/docs/servers/) ; repo https://github.com/ringcentral/ringcentral-mcp-docs

- [https://unified-crm-extension.labs.ringcentral.com/mcp](https://unified-crm-extension.labs.ringcentral.com/mcp)
- [https://mcp.labs.ringcentral.com/docs/servers/app-connect/](https://mcp.labs.ringcentral.com/docs/servers/app-connect/)
- [https://mcp.labs.ringcentral.com/docs/servers/](https://mcp.labs.ringcentral.com/docs/servers/)
- [https://github.com/ringcentral/ringcentral-mcp-docs](https://github.com/ringcentral/ringcentral-mcp-docs)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - a RingCentral subscription is required and the Labs MCP servers carry no separate price. The vendor's plans and pricing page states "RingCentral provides a suite of powerful APIs for voice, SMS/MMS, team messaging, video, fax, data management and system configuration." Per-seat prices on that page are rendered client-side and were not captured by this fetch, so no figure is recorded here.

**API documentation**

No documentation URL recorded.

289 of 318 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/ringcentral/ringcentral-mcp-docs](https://github.com/ringcentral/ringcentral-mcp-docs)

**Jobs it can do**

No job tag on this entry.

47 of 318 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://mcp.labs.ringcentral.com/docs/servers/app-connect/](https://mcp.labs.ringcentral.com/docs/servers/app-connect/)
- [https://mcp.labs.ringcentral.com/docs/servers/](https://mcp.labs.ringcentral.com/docs/servers/)
- [https://www.ringcentral.com/office/plansandpricing.html](https://www.ringcentral.com/office/plansandpricing.html)
- [https://github.com/ringcentral/ringcentral-mcp-docs](https://github.com/ringcentral/ringcentral-mcp-docs)
- [https://unified-crm-extension.labs.ringcentral.com/mcp](https://unified-crm-extension.labs.ringcentral.com/mcp)

5 source URLs. Raw sources field, verbatim:

https://mcp.labs.ringcentral.com/docs/servers/app-connect/, https://mcp.labs.ringcentral.com/docs/servers/, https://www.ringcentral.com/office/plansandpricing.html, https://github.com/ringcentral/ringcentral-mcp-docs, https://unified-crm-extension.labs.ringcentral.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07 and this one is unusual: POST of an MCP initialize to https://unified-crm-extension.labs.ringcentral.com/mcp returned HTTP 200 with a full initialize result, serverInfo name "rc-unified-crm-extension" version 1.0.0, protocol 2024-11-05. Tool discovery is open and unauthenticated by design; the docs confirm this, stating the RingEX servers need "no authentication required for tool discovery" and that only the tools marked as requiring a CRM connection need a linked account. Status is Beta and transport is SSE over HTTPS. The candid line on the vendor's own page is worth quoting in any coverage: "Some CRMs publish their own dedicated MCP servers with deeper, CRM-specific functionality. App Connect is most valuable when your CRM doesn't yet support MCP natively." A vendor telling a buyer to use someone else's server is rare enough to be the story. Three sibling servers are published in the same registry and are candidates for their own entries: RingEX Phone (12 tools), RingEX Chat (9 tools) and RingEX Admin (26 tools), all marked Preview. Nine tools here: getSessionInfo, getPublicConnectors, getHelp, findContactByName, findContactByPhone, createContact, createCallLog, rcGetCallLogs, logout. 2026-09-07: GitHub org ringcentral; repo is the MkDocs site for "RingCentral MCP Server Documentation" with per-server pages (docs/servers/app-connect.md) (https://github.com/ringcentral/ringcentral-mcp-docs).

**Provenance**

- **Entry id**: 02-ringcentral-app-connect-mcp

- **Source file**: 02-engagement-outbound.md

- **Source line**: 561

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
