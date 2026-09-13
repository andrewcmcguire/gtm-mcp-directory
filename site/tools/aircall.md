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
CLI: aircall (community)

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

**What this server exposes**

- **Tools named**: 81
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-12
- **Repo read**: themobilefirstco/aircall-mcp-server
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **aircall_add_call_comment** Add a comment / note to a call. Aircall REST: POST /calls/{id}/comments. evidence: answered tools/list · calling it writes · required: id, content

- **aircall_add_campaign_numbers** Add numbers to campaign evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_add_comment** Add comment to call evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_add_email** Add email to contact evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_add_phone** Add phone to contact evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_add_tags** Tag a call evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_add_user_to_team** Add user to team evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_archive_call** Archive a call evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_check_availability** Check user availability evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_create_campaign** Create campaign evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_create_config** Enable SMS on number evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_create_contact** Create a new contact in the shared address book. Aircall typically requires at least one of first_name / last_name / company_name. Aircall REST: POST /contacts. evidence: answered tools/list · calling it writes

- **aircall_create_tag** Create new tag evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_create_team** Create new team evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_create_user** Create new user evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_create_webhook** Create webhook evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_delete_campaign** Delete campaign evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_delete_config** Disable SMS evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_delete_contact** Delete contact evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_delete_email** Delete email evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_delete_tag** Delete tag evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_delete_team** Delete team evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_delete_user** Delete user evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_delete_webhook** Delete webhook evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_dial** Open dialer with number evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_disable_integration** Disable integration evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_enable_integration** Enable integration evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_action_items** Get detected action items evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_call** Get a single call by id. Aircall REST: GET /calls/{id}. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_call_action_items** Get the AI-extracted action items / follow-ups from a call (Aircall AI Voice feature). Aircall REST: GET /calls/{id}/action_items. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_call_sentiments** Get the AI-generated sentiment analysis of a call (Aircall AI Voice feature). Aircall REST: GET /calls/{id}/sentiments. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_call_summary** Get the AI-generated summary of a call (Aircall AI Voice feature). Aircall REST: GET /calls/{id}/summary. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_call_topics** Get the AI-detected topics of a call (Aircall AI Voice feature). Aircall REST: GET /calls/{id}/topics. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_call_transcription** Get the AI-generated transcription of a call (Aircall AI Voice feature). Aircall REST: GET /calls/{id}/transcription. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_campaign** Get campaign details evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_campaign_numbers** List campaign numbers evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_company** Get details of the authenticated Aircall company (name, plan, usage). Aircall REST: GET /company. evidence: answered tools/list · calling it reads

- **aircall_get_config** Get SMS config evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_contact** Get a single contact by id. Aircall REST: GET /contacts/{id}. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_number** Get a single phone number by id. Aircall REST: GET /numbers/{id}. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_realtime_transcript** Get live transcription evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_registration_status** Get registration status evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_sentiments** Get sentiment analysis evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_summary** Get AI-generated call summary evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_tag** Get a single tag by id. Aircall REST: GET /tags/{id}. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_team** Get a single team by id. Aircall REST: GET /teams/{id}. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_topics** Get topics discussed evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_transcript** Get call transcription evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_user** Get a single user (agent) by id. Aircall REST: GET /users/{id}. evidence: answered tools/list · calling it reads · required: id

- **aircall_get_user_numbers** Get user's numbers evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_get_webhook** Get webhook details evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_list_availabilities** List all availabilities evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_list_calls** List calls, optionally filtered by a creation-date window and ordered. Aircall REST: GET /calls. evidence: answered tools/list · calling it reads

- **aircall_list_campaigns** List campaigns evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_list_contacts** List contacts in the shared address book, optionally by creation-date window and order. Aircall REST: GET /contacts. evidence: answered tools/list · calling it reads

- **aircall_list_integrations** List integrations evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_list_messages** List SMS messages evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_list_numbers** List the phone numbers owned by the company (id, name, digits, country). Aircall REST: GET /numbers. evidence: answered tools/list · calling it reads

- **aircall_list_tags** List the company's call tags (id, name, color). Aircall REST: GET /tags. evidence: answered tools/list · calling it reads

- **aircall_list_teams** List the company's teams and their members. Aircall REST: GET /teams. evidence: answered tools/list · calling it reads

- **aircall_list_users** List users (agents) in the Aircall company (id, name, email, availability). Aircall REST: GET /users. evidence: answered tools/list · calling it reads

- **aircall_list_webhooks** List webhooks evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_pause_recording** Pause call recording evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_ping** Health check - verify the API is reachable and the credentials are valid. Aircall REST: GET /ping. evidence: answered tools/list · calling it reads

- **aircall_remove_campaign_number** Remove number evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_remove_user_from_team** Remove user from team evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_resume_recording** Resume call recording evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_search_calls** Search calls by a free-text term (e.g. phone number, tag, direction). Aircall REST: GET /calls/search. evidence: answered tools/list · calling it reads

- **aircall_search_contacts** Search contacts by a free-text term (e.g. name, phone number, email). Aircall REST: GET /contacts/search. evidence: answered tools/list · calling it reads

- **aircall_send_agent_message** Reply in conversation evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_send_message** Send SMS evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_start_call** Initiate outbound call evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_tag_call** Apply tags to a call by tag id (get ids from aircall_list_tags). Aircall REST: POST /calls/{id}/tags. evidence: answered tools/list · calling it writes · required: id, tag_ids

- **aircall_transfer_call** Transfer active call evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_update_contact** Update fields on an existing contact. Only provided fields are changed. Aircall REST: PUT /contacts/{id}. evidence: answered tools/list · calling it writes · required: id

- **aircall_update_messages** Update audio messages evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_update_number** Update number config evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_update_phone** Update phone number evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_update_tag** Update tag evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_update_user** Update user evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **aircall_update_webhook** Update webhook evidence: in a README table · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: aircall
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g aircall-cli
```

quoted from [https://www.npmjs.com/package/aircall-cli](https://www.npmjs.com/package/aircall-cli) on 2026-09-12, via npm, a third party source

Packages seen, with the version on 2026-09-12:

- [npm: aircall-cli 0.2.0, third party](https://www.npmjs.com/package/aircall-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's pricing page lists "250+ integrations and API access" on the Essentials plan, the entry tier, with the dollar amounts not rendered on the page on this date; the Custom plan carries a 25-licence minimum and "Access to API developer support". No free plan.

**API documentation**

No documentation URL recorded.

428 of 559 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/themobilefirstco/aircall-mcp-server](https://github.com/themobilefirstco/aircall-mcp-server)

**On GitHub**

[github.com/aircall](https://github.com/aircall) tied to the vendor by rule 3, account website https://aircall.io has the vendor's domain, confidence strong

- **Public repositories**: 18, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-05-26

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [aircall-everywhere](https://github.com/aircall/aircall-everywhere) | SDK | SDK to embed and communicate to Aircall phone in any web page | 39 | 2026-05-26 | v2.0.6 |
| [aircall-infosecmanager-takehome-submission-template](https://github.com/aircall/aircall-infosecmanager-takehome-submission-template) | docs or examples | Template for candidates to clone to submit their take home exercise deliverables | 0 | 2026-01-12 | |
| [frontend-hiring-test](https://github.com/aircall/frontend-hiring-test) | app | | 46 | 2025-12-15 | |
| [ios-test](https://github.com/aircall/ios-test) | other | | 0 | 2024-02-23 | |
| [backend-test-5](https://github.com/aircall/backend-test-5) | other | | 5 | 2023-01-19 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

288 of 559 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
