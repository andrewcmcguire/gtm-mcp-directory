# JustCall: MCP server status, API access gate and what it does

> A cloud phone, SMS and WhatsApp platform for sales and support teams built by SaaS Labs, with a sales dialer,... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
JustCall

# JustCall

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [justcall.io](https://justcall.io) · entry id 02-justcall · source 02-engagement-outbound.md line 542

**What it does**
A cloud phone, SMS and WhatsApp platform for sales and support teams built by SaaS Labs, with a sales dialer, CRM integrations and AI voice agents, plus a hosted MCP server that lets an assistant read and act on calls, messages, contacts, numbers and users.

**AI features, separated from automation with an AI label on it**
Conversation intelligence, AI coaching, agent assist, automatic call scoring, transcription, moment analysis and sentiment analysis are all first-party features, and an AI Voice Agent product handles inbound calls. The MCP server itself adds no intelligence; it exposes the account to whatever model is calling.

**RevOps role**
The dialer and multichannel messaging layer for an SMB or mid-market outbound team, sitting between the CRM and the phone network, and now callable by an agent for logging, follow-up and campaign work.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key. The vendor's docs show an Authorization header of the form "Bearer :", a key and secret pair joined by a colon, for Cursor, Windsurf and Claude Desktop alike.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.justcall.host/mcp (docs: https://developer.justcall.io/docs/mcp; source repo: https://github.com/saaslabsco/justcall-mcp-server)

- [https://mcp.justcall.host/mcp](https://mcp.justcall.host/mcp)
- [https://developer.justcall.io/docs/mcp](https://developer.justcall.io/docs/mcp)
- [https://github.com/saaslabsco/justcall-mcp-server](https://github.com/saaslabsco/justcall-mcp-server)

**What this server exposes**

- **Tools named**: 50
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: saaslabsco/justcall-mcp-server
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **add_contacts_blacklist** Add one or more contacts to the JustCall account evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **add_salesdialer_campaign_contact** Add contact to a specific Sales Dialer campaign identified by Campaign ID evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **add_salesdialer_contacts_dnca** Add one or more contacts to the Sales Dialer\ evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **check_whatsapp_message_reply** Check for the most recent inbound whatsapp message from a contact number evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_appointment** Schedule a new appointment on a specific JustCall calendar evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_contact** Create a new contact in the JustCall account evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_salesdialer_campaign** Create a new Sales Dialer campaign in the JustCall account evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_salesdialer_contact** Create a new contact in Sales Dialer evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_voice_agent_call** Initiate an outbound call from a configured AI voice agent to a contact number evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_webhook** Create a new webhook endpoint to receive real-time notifications evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_account_analytics** Retrieve aggregated call analytics at the JustCall account level evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_agent_analytics** Retrieve call performance analytics for a specific agent identified by Agent ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_appointment** Retrieve details of a specific appointment by its ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_call_ai_analysis** Retrieve AI-generated analysis for a specific call by Call ID associated with either JustCall or Sales Dialer evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_contact** Retrieve detailed information for a specific contact by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_meeting_ai_analysis** Retrieve AI-generated analysis for a specific meeting identified by Instance ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_number** Retrieve detailed information for a specific phone number by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_number_analytics** Retrieve call analytics for a specific JustCall phone number evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_salesdialer_agent_analytics** Retrieve call performance analytics of a specific agent for a Sales Dialer campaign evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_salesdialer_call** Retrieve detailed information for a specific Sales Dialer call by Call ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_salesdialer_campaign** Retrieve detailed information for a specific Sales Dialer campaign by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_salesdialer_contact** Retrieve detailed information for a specific contact in Sales Dialer by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_user** Retrieve detailed information for a specific user by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_user_group** Retrieve detailed information for a specific user group by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_whatsapp_message** Retrieve detailed information for a specific whatsapp message by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **import_salesdialer_contacts** Import multiple contacts into Sales Dialer or a campaign in bulk evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **import_salesdialer_contacts_status** Check the status of a bulk import job/request by its batch ID evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_appointment_slots** Retrieve all available time slots for appointments on a specific JustCall calendar evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_blacklist_contacts** Retrieve all blacklist contacts from the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_calls_ai_analysis** Retrieve AI-generated analysis for all calls associated with either JustCall or Sales Dialer evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_contacts** Retrieve all contacts associated with the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_meetings_ai_analysis** Retrieve AI-generated analysis for recorded meetings evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_numbers** Retrieve all phone numbers associated with the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_salesdialer_calls** Retrieve all calls made via the Sales Dialer in JustCall evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_salesdialer_campaign_contacts** Retrieve all contacts in a specific Sales Dialer campaign identified by Campaign ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_salesdialer_campaigns** Retrieve all Sales Dialer campaigns in the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_salesdialer_contacts** Retrieve all contacts from Sales Dialer in the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_salesdialer_custom_fields** Fetch all custom contact fields defined in your Sales Dialer account and their details evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_user_groups** Retrieve all user groups defined in the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_users** Retrieve all users associated with the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_voice_agents** Retrieve all AI voice agents associated with the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_webhooks** Retrieve all configured webhooks evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_whatsapp_messages** Retrieve all whatsapp messages associated with the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_whatsapp_templates** Retrieve all whatsapp message templates available in the JustCall account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **send_whatsapp_message** Send a new whatsapp message to a contact number evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_contact** Update/modify details of an existing contact in the JustCall account evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_contact_status** Add or remove a contact from DND/DNM/Blacklist lists in the JustCall account evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_salesdialer_campaign** Update/modify details of an existing Sales Dialer campaign in the JustCall account evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_salesdialer_contact** Update/modify details of an existing contact in Sales Dialer identified by ID evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_user_availability** Update a user evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - JustCall publishes self-serve plans and titles its own pricing page "Business Phone System Plans Starting from $29/Month". That page lists "API access & workflows" as a plan feature, described as "Build custom workflows for your business with JustCall's open APIs. (up to 1,800 requests/hour)". The per-tier feature matrix is rendered client-side and did not fetch, so the exact plan floor for API access is not recorded here rather than guessed.

**API documentation**

No documentation URL recorded.

428 of 559 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/saaslabsco/justcall-mcp-server](https://github.com/saaslabsco/justcall-mcp-server)

**On GitHub**

No GitHub organisation could be tied to justcall.io with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

6 candidate accounts seen and rejected by the evidence rules: saaslabsco, justcallhq, Justcallmetn, justcallmeben1234, JustCallMeJo. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

No job tag on this entry.

288 of 559 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://developer.justcall.io/docs/mcp](https://developer.justcall.io/docs/mcp)
- [https://justcall.io/pricing/](https://justcall.io/pricing/)
- [https://github.com/saaslabsco/justcall-mcp-server](https://github.com/saaslabsco/justcall-mcp-server)

3 source URLs. Raw sources field, verbatim:

https://developer.justcall.io/docs/mcp, https://justcall.io/pricing/, https://github.com/saaslabsco/justcall-mcp-server

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.justcall.host/mcp returned HTTP 401 Unauthorized, confirming a live auth-gated server, and the endpoint is printed verbatim in JustCall's own developer documentation, which states "JustCall hosts a remote MCP server at https://mcp.justcall.host/mcp". Note the off-domain host: the server lives on justcall.host, not justcall.io, which is the same discovery trap as Dialpad's karehq.com. The vendor's own MCP doc page carries an "Updated 11 months ago" stamp, so it predates the current MCP specification revisions by a wide margin and the transport details should be re-verified before a bench test. The public GitHub repository is under the saaslabsco organisation, which is JustCall's parent company, so it is first-party rather than community. The docs frame the server partly as documentation access for AI code editors and partly as live account access, and the example prompts shown include sending an SMS, which means write access is in scope and an unattended agent can message real prospects.

**Provenance**

- **Entry id**: 02-justcall

- **Source file**: 02-engagement-outbound.md

- **Source line**: 542

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
