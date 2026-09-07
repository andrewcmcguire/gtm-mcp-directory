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

Vendor: [usefulapi.io](https://usefulapi.io) · entry id 07-usefulapi-io · source 07-mcp-infrastructure.md line 407

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

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - every server page publishes the same two tiers, "Free 100 tool calls / month" and "Pro $9/mo" or "$90/yr", which is the cheapest paid tier of any gateway in this file.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/m190/usefulapi-mcp](https://github.com/m190/usefulapi-mcp)

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

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

- **Source line**: 407

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
