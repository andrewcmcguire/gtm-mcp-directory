# usefulapi.io: MCP server status, API access gate and what it does

> A hosted catalogue of 146 single-application MCP servers, one per SaaS product, each on its own subdomain,... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
usefulapi.io

# usefulapi.io

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [usefulapi.io](https://usefulapi.io) · entry id 07-usefulapi-io · source 07-mcp-infrastructure.md line 409

**What it does**
A hosted catalogue of 146 single-application MCP servers, one per SaaS product, each on its own subdomain, wrapping that product's public REST API as a named tool list with per-tool read and write labels and the underlying REST call documented against each tool.

**AI features, separated from automation with an AI label on it**
None. It is a wrapper host, and unusually transparent about it: each tool's description names the exact upstream REST endpoint it calls, so the mapping between an MCP tool and a vendor API route is legible before connecting.

**RevOps role**
A stopgap for the long tail: it puts an agent in front of a GTM tool that has shipped no MCP server of its own, at a price where trying it costs nothing, and its per-tool REST mapping makes it a useful reference even for someone who never connects it.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: per-application OAuth. The setup instructions add the subdomain as a custom connector and the user then authenticates with the wrapped vendor when prompted, so usefulapi brokers the connection rather than taking an API key up front.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official (usefulapi's own servers; not endorsed by the wrapped vendors)

mcp_url, verbatim from the file:

https://pipedrive.usefulapi.io/mcp ; https://.usefulapi.io/mcp, one subdomain per application, listed at https://usefulapi.io/ with a page per server such as https://usefulapi.io/aircall ; repo https://github.com/m190/usefulapi-mcp

- [https://pipedrive.usefulapi.io/mcp](https://pipedrive.usefulapi.io/mcp)
- [https://usefulapi.io/](https://usefulapi.io/)
- [https://usefulapi.io/aircall](https://usefulapi.io/aircall)
- [https://github.com/m190/usefulapi-mcp](https://github.com/m190/usefulapi-mcp)

**What this server exposes**

- **Tools named**: 20
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-12
- **Repo read**: m190/usefulapi-mcp
- **Whose repo**: third-party
- **Catalogue shape**: the customer's own workspace, not a fixed catalogue

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

Recorded by the harvest: a gateway that generates an MCP server per wrapped vendor API

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **Server** Category evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **pipedrive_add_note** Add a note, linked to at least one of a deal/person/organization/lead. `content` is required (HTML or plain text). Uses v1 (v2 has no notes endpoint). Pipedrive REST: POST /api/v1/notes. evidence: answered tools/list · calling it writes · required: content

- **pipedrive_create_activity** Create a new activity (task/event). `subject` is required; link it to a deal/person/org and set type/date/time as needed. Pipedrive REST: POST /api/v2/activities. evidence: answered tools/list · calling it writes · required: subject

- **pipedrive_create_deal** Create a new deal. `title` is required; link it to a person/org/pipeline/stage/owner as needed. Pipedrive REST: POST /api/v2/deals. evidence: answered tools/list · calling it writes · required: title

- **pipedrive_create_person** Create a new person (contact). `name` is required; `email`/`phone` are convenience strings mapped to Pipedrive's structured emails/phones arrays. Pipedrive REST: POST /api/v2/persons. evidence: answered tools/list · calling it writes · required: name

- **pipedrive_get_current_user** Get the authenticated user's profile (name, email, company, locale, timezone). Pipedrive REST: GET /api/v1/users/me. evidence: answered tools/list · calling it reads

- **pipedrive_get_deal** Get a single deal by its id. Pipedrive REST: GET /api/v2/deals/{id}. evidence: answered tools/list · calling it reads · required: id

- **pipedrive_get_organization** Get a single organization by its id. Pipedrive REST: GET /api/v2/organizations/{id}. evidence: answered tools/list · calling it reads · required: id

- **pipedrive_get_person** Get a single person (contact) by its id. Pipedrive REST: GET /api/v2/persons/{id}. evidence: answered tools/list · calling it reads · required: id

- **pipedrive_list_activities** List activities (tasks/events), optionally filtered by filter/owner/deal/person/org/done/updated_since. Pipedrive REST: GET /api/v2/activities. evidence: answered tools/list · calling it reads

- **pipedrive_list_deals** List deals, optionally filtered by filter/owner/person/org/pipeline/stage/status and sorted. Pipedrive REST: GET /api/v2/deals. evidence: answered tools/list · calling it reads

- **pipedrive_list_notes** List notes, optionally filtered by user/deal/person/org/lead. Uses v1 (v2 has no notes endpoint) with start+limit pagination. Pipedrive REST: GET /api/v1/notes. evidence: answered tools/list · calling it reads

- **pipedrive_list_organizations** List organizations, optionally filtered by filter/owner and sorted. Pipedrive REST: GET /api/v2/organizations. evidence: answered tools/list · calling it reads

- **pipedrive_list_persons** List persons (contacts), optionally filtered by filter/owner/org and sorted. Pipedrive REST: GET /api/v2/persons. evidence: answered tools/list · calling it reads

- **pipedrive_list_pipelines** List all pipelines. Pipedrive REST: GET /api/v2/pipelines. evidence: answered tools/list · calling it reads

- **pipedrive_list_stages** List stages, optionally restricted to a single pipeline. Pipedrive REST: GET /api/v2/stages. evidence: answered tools/list · calling it reads

- **pipedrive_search_deals** Search deals by term across selected fields. Pipedrive REST: GET /api/v2/deals/search. evidence: answered tools/list · calling it reads · required: term

- **pipedrive_search_items** Global search across multiple item types (deals, persons, organizations, products, leads, files, etc.). Pipedrive REST: GET /api/v2/itemSearch. evidence: answered tools/list · calling it reads · required: term

- **pipedrive_search_organizations** Search organizations by term across selected fields. Pipedrive REST: GET /api/v2/organizations/search. evidence: answered tools/list · calling it reads · required: term

- **pipedrive_search_persons** Search persons (contacts) by term across selected fields. Pipedrive REST: GET /api/v2/persons/search. evidence: answered tools/list · calling it reads · required: term

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - every server page publishes the same two tiers, "Free 100 tool calls / month" and "Pro $9/mo" or "$90/yr", which is the cheapest paid tier of any gateway in this file.

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/m190/usefulapi-mcp](https://github.com/m190/usefulapi-mcp)

**On GitHub**

No GitHub organisation could be tied to usefulapi.io with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

1 candidate account seen and rejected by the evidence rules: m190. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

No job tag on this entry.

378 of 649 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://usefulapi.io/](https://usefulapi.io/)
- [https://usefulapi.io/aircall](https://usefulapi.io/aircall)
- [https://pipedrive.usefulapi.io/mcp](https://pipedrive.usefulapi.io/mcp)
- [https://github.com/m190/usefulapi-mcp](https://github.com/m190/usefulapi-mcp)

4 source URLs. Raw sources field, verbatim:

https://usefulapi.io/, https://usefulapi.io/aircall, https://pipedrive.usefulapi.io/mcp, https://github.com/m190/usefulapi-mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://pipedrive.usefulapi.io/mcp returned HTTP 200 with a full initialize result, serverInfo name "pipedrive-mcp" version 1.0.0, protocol 2025-06-18, so the servers are live and the initialize handshake is open even though tool calls require the user's own vendor authorisation. RECLASSIFIED FROM THE CANDIDATE ROW for the same reason as Pipeworx: the research filed it "third-party wrapper (community)", which describes its relationship to the wrapped vendors correctly, but the servers are usefulapi's own first-party product, so mcp_status is official with the qualifier carried in the value itself. THE CAVEAT IS THE ENTRY: none of the wrapped vendors endorses these servers, the wrapped vendor's own terms of service still govern the API calls underneath, and connecting one means a third party sits in the OAuth path to a system of record. GTM-relevant servers seen in the catalogue include Aircall (27 tools), Pipedrive, Mixpanel, Chargebee, Zendesk and Groove HQ. The Aircall server page is a good worked example of the transparency: every tool names its upstream call, for instance aircall_search_calls documented as "Aircall REST: GET /calls/search". Compare against 02-engagement-outbound.md's Aircall entry, where the only servers found were community ones, and note that this host is one of them. 2026-09-07: The repo is the usefulapi portal and server catalogue: README "usefulapi - Hosted MCP servers for the tools you already use ... Portal: https://usefulapi.io", with servers/<app>/server.json for each hosted server (https://github.com/m190/usefulapi-mcp).

**Provenance**

- **Entry id**: 07-usefulapi-io

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 409

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
