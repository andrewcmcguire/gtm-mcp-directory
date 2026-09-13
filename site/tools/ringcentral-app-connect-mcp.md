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

**What this server exposes**

- **Tools named**: 14
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **cancelAppointment** ⚠️ REQUIRES CRM CONNECTION. | Cancel an existing appointment or event in the CRM platform by its ID. This action is destructive - the appointment will be removed. evidence: answered tools/list · calling it reads · required: appointmentId

- **confirmAppointment** ⚠️ REQUIRES CRM CONNECTION. | Confirm an existing appointment or event in the CRM platform by its ID. Returns the updated appointment details. evidence: answered tools/list · calling it reads · required: appointmentId

- **createAppointment** ⚠️ REQUIRES CRM CONNECTION. | Create a new appointment or event in the CRM platform. Returns the created appointment ID and details. evidence: answered tools/list · calling it writes · required: title, startTimeUtc, durationMinutes

- **createCallLog** ⚠️ REQUIRES CRM CONNECTION. | Create only one call log in the CRM platform. Returns the created log ID if successful. To use with `rcGetCallLogs`: pass a single item from the `records[]` array directly as `incomingData.logInfo`. evidence: answered tools/list · calling it writes

- **createContact** ⚠️ REQUIRES CRM CONNECTION. | Create a new contact in the CRM platform. Returns the created contact information if successful. evidence: answered tools/list · calling it writes · required: phoneNumber

- **findContactByName** ⚠️ REQUIRES CRM CONNECTION. | Search for a contact in the CRM platform by name. Returns contact details if found. evidence: answered tools/list · calling it reads · required: name

- **findContactByPhone** ⚠️ REQUIRES CRM CONNECTION. | Search for a contact in the CRM platform by phone number. Returns contact details if found. evidence: answered tools/list · calling it reads · required: phoneNumber

- **getHelp** Get a quick guide on what this integration can do and how to get started. evidence: answered tools/list · calling it reads

- **getPublicConnectors** Get available connectors. Returns an interactive widget - do NOT summarize or list the results in text, just show the widget. evidence: answered tools/list · calling it reads

- **getSessionInfo** Get the current user session info, including RingCentral identity and CRM connection status. evidence: answered tools/list · calling it reads

- **listAppointments** ⚠️ REQUIRES CRM CONNECTION. | List appointments or events from the CRM platform. Use the `filter` param to get upcoming, today's, past, or all appointments. For a specific window, supply `startDate` and `endDate` (YYYY-MM-DD) directly. evidence: answered tools/list · calling it reads

- **logout** Logout the user from the CRM platform. evidence: answered tools/list · calling it reads

- **rcGetCallLogs** ⚠️ REQUIRES CRM CONNECTION. | Get call logs from RingCentral. Returns a `records[]` array. Each item in `records` is a complete RingCentral call log object that can be passed DIRECTLY as `incomingData.logInfo` to the `createCallLog` tool - evidence: answered tools/list · calling it reads · required: timeFrom, timeTo

- **updateAppointment** ⚠️ REQUIRES CRM CONNECTION. | Update or reschedule an existing appointment or event in the CRM platform. Provide only the fields you want to change alongside the appointmentId. evidence: answered tools/list · calling it writes · required: appointmentId

119 of the 396 entries that record an official or community MCP server carry a harvested tool list. The other 277 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - a RingCentral subscription is required and the Labs MCP servers carry no separate price. The vendor's plans and pricing page states "RingCentral provides a suite of powerful APIs for voice, SMS/MMS, team messaging, video, fax, data management and system configuration." Per-seat prices on that page are rendered client-side and were not captured by this fetch, so no figure is recorded here.

**API documentation**

No documentation URL recorded.

555 of 834 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/ringcentral/ringcentral-mcp-docs](https://github.com/ringcentral/ringcentral-mcp-docs)

**On GitHub**

[github.com/ringcentral](https://github.com/ringcentral) tied to the vendor by rule 2, account website https://developers.ringcentral.com/ has the vendor's domain, confidence strong

- **Public repositories**: 149, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [ringcentral-embeddable](https://github.com/ringcentral/ringcentral-embeddable) | plugin or integration | RingCentral Embeddable widget | 92 | 2026-09-08 | 2.3.1 |
| [trello-notification-app](https://github.com/ringcentral/trello-notification-app) | plugin or integration | Trello notification and bot add-in for RingCentral | 4 | 2026-09-07 | |
| [engage-voice-embeddable](https://github.com/ringcentral/engage-voice-embeddable) | other | (Beta)RingCentral RingCX Embeddable widget | 7 | 2026-09-07 | 0.1.0 |
| [rc-unified-crm-extension](https://github.com/ringcentral/rc-unified-crm-extension) | plugin or integration | App Connect is a CRM integration framework to help developers quickly bring to market a full-featured CTI into... | 13 | 2026-09-07 | 1.7.44 |
| [ringcentral-call-control-js](https://github.com/ringcentral/ringcentral-call-control-js) | docs or examples | RingCentral Call Control SDK in JavaScript to control RingCentral calls on any endpoint. Demo URL: | 10 | 2026-09-07 | 0.2.12 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

563 of 834 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
