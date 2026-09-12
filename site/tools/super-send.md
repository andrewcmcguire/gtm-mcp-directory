# Super Send: MCP server status, API access gate and what it does

> Cold email sequencing platform providing dedicated, warmed sending infrastructure with adaptive pacing based... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Super Send

# Super Send

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07
CLI: supersendtx

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [supersend.io](https://supersend.io) · entry id 02-super-send · source 02-engagement-outbound.md line 274

**What it does**
Cold email sequencing platform providing dedicated, warmed sending infrastructure with adaptive pacing based on live deliverability signals.

**AI features, separated from automation with an AI label on it**
"AI Bounce Analysis" categorizes send failures (bad address, server block, temporary failure) - genuinely ML-classification per vendor. "AI-categorized" inbox auto-sorts replies across many senders. Adaptive pacing/placement testing is described as signal-driven automation, not explicitly AI.

**RevOps role**
Dedicated sending-infrastructure layer for outbound email, positioned as an infrastructure/deliverability specialist rather than a full sequencing+CRM platform.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key, Streamable HTTP transport

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.supersend.io/docs/mcp-server](https://docs.supersend.io/docs/mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.supersend.io/mcp ; https://docs.supersend.io/docs/mcp-server (endpoint mcp.supersend.io)

- [https://mcp.supersend.io/mcp](https://mcp.supersend.io/mcp)
- [https://docs.supersend.io/docs/mcp-server](https://docs.supersend.io/docs/mcp-server)

**What this server exposes**

- **Tools named**: 45
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **activate_campaign** Turn a campaign on evidence: in the vendor docs · calling it reads · required: CampaignId

- **add_to_blacklist** Add to blacklist evidence: in the vendor docs · calling it writes

- **analyze_capacity_and_schedule** Capacity planning: when campaigns finish, allocated capacity evidence: in the vendor docs · calling it reads

- **analyze_domain_health** Per-domain DNS/health: SPF, DKIM, DMARC, MX, at-risk flags evidence: in the vendor docs · calling it reads

- **analyze_sender_health** Per-sender health: sends, bounces, at-risk flags evidence: in the vendor docs · calling it reads

- **bulk_import_contacts** Bulk import contacts evidence: in the vendor docs · calling it writes

- **create_campaign** Create a new campaign evidence: in the vendor docs · calling it writes · required: name, TeamId

- **create_contact** Create/upsert contact or profile-only evidence: in the vendor docs · calling it writes · required: TeamId

- **create_webhook** Create a webhook evidence: in the vendor docs · calling it writes · required: url, events

- **deactivate_campaign** Turn a campaign off evidence: in the vendor docs · calling it reads · required: CampaignId

- **delete_contact** Delete a contact (soft delete) evidence: in the vendor docs · calling it writes · required: ContactId

- **diagnose_deliverability** Deliverability diagnosis: reply rate, bounces, placement tests evidence: in the vendor docs · calling it reads

- **get_campaign** Get a campaign by ID evidence: in the vendor docs · calling it reads · required: CampaignId

- **get_campaign_sequence** Get campaign sequence evidence: in the vendor docs · calling it reads · required: CampaignId

- **get_contact** Get a contact by ID evidence: in the vendor docs · calling it reads · required: ContactId

- **get_conversation** Get a conversation by ID evidence: in the vendor docs · calling it reads · required: ConversationId

- **get_conversation_messages** Get messages in a conversation evidence: in the vendor docs · calling it reads · required: ConversationId

- **get_domain** Get a domain by ID evidence: in the vendor docs · calling it reads · required: DomainId

- **get_domain_bounce_insights** AI bounce breakdown per domain evidence: in the vendor docs · calling it reads · required: DomainId

- **get_event** Get an event by ID evidence: in the vendor docs · calling it reads · required: EventId

- **get_health** Check SuperSend API health and connectivity evidence: in the vendor docs · calling it reads

- **get_outbound_summary** Team outbound metrics: sends, replies, top campaigns evidence: in the vendor docs · calling it reads

- **get_sender** Get a sender by ID evidence: in the vendor docs · calling it reads · required: SenderId

- **get_sender_bounce_insights** AI bounce type breakdown per sender evidence: in the vendor docs · calling it reads · required: SenderId

- **get_team** Get a team by ID evidence: in the vendor docs · calling it reads · required: TeamId

- **list_blacklist** List blacklisted emails/domains evidence: in the vendor docs · calling it reads

- **list_campaigns** List campaigns in a team evidence: in the vendor docs · calling it reads · required: TeamId

- **list_contacts** List contacts in a team evidence: in the vendor docs · calling it reads · required: TeamId

- **list_conversations** List conversations evidence: in the vendor docs · calling it reads

- **list_domains** List managed domains evidence: in the vendor docs · calling it reads

- **list_events** List events (sends, opens, clicks, replies, bounces) evidence: in the vendor docs · calling it reads

- **list_labels** List conversation labels evidence: in the vendor docs · calling it reads

- **list_placement_tests** List placement tests evidence: in the vendor docs · calling it reads

- **list_senders** List email senders evidence: in the vendor docs · calling it reads

- **list_teams** List teams the user has access to evidence: in the vendor docs · calling it reads

- **list_webhooks** List webhooks evidence: in the vendor docs · calling it reads

- **purchase_domain** Purchase domains (requires payment method, contact details) evidence: in the vendor docs · calling it spends money

- **purchase_domains_and_mailboxes** Purchase domains and mailboxes in one transaction evidence: in the vendor docs · calling it spends money

- **purchase_mailbox** Purchase mailboxes for existing domains evidence: in the vendor docs · calling it spends money

- **remove_from_blacklist** Remove from blacklist evidence: in the vendor docs · calling it writes

- **send_conversation_message** Send a message in a conversation evidence: in the vendor docs · calling it writes · required: ConversationId

- **update_campaign_sequence** Update campaign sequence evidence: in the vendor docs · calling it writes

- **update_contact** Update a contact evidence: in the vendor docs · calling it writes · required: ContactId

- **update_sender** Update a sender evidence: in the vendor docs · calling it writes · required: SenderId

- **verify_email** Standalone email verification evidence: in the vendor docs · calling it reads · required: email

119 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 106 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: supersendtx
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g supersendtx-cli
```

quoted from [https://www.npmjs.com/package/supersendtx-cli](https://www.npmjs.com/package/supersendtx-cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: supersendtx-cli 0.15.5](https://www.npmjs.com/package/supersendtx-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

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

**On GitHub**

No GitHub organisation could be tied to supersend.io with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

3 candidate accounts seen and rejected by the evidence rules: Super-Send, SpacePayafrica, MeetContactsApp. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)
- [Check inbox placement](../jobs/check-inbox-placement.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.pulsemcp.com/servers/supersend](https://www.pulsemcp.com/servers/supersend)
- [https://supersend.io](https://supersend.io)
- [https://mcp.supersend.io/mcp](https://mcp.supersend.io/mcp)

3 source URLs. Raw sources field, verbatim:

https://www.pulsemcp.com/servers/supersend, https://supersend.io, https://mcp.supersend.io/mcp

**Notes, verbatim from the file**
Vendor's own MCP docs state the MCP server is a paid service with no free tier. Smaller/lesser-known player than most others in this sweep, but has a real vendor-hosted, documented MCP server - more than several larger competitors (Klenty, Outplay, Mailshake, QuickMail) have. 2026-09-07: https://mcp.supersend.io/mcp returned 401 with a JSON-RPC body: {"jsonrpc":"2.0","error":{"code":-32001,"message":"Missing or invalid credentials. Use Authorization: Bearer <key> or X-Supersend-Api-Key: <key>..."}} (https://mcp.supersend.io/mcp).

**Provenance**

- **Entry id**: 02-super-send

- **Source file**: 02-engagement-outbound.md

- **Source line**: 274

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
