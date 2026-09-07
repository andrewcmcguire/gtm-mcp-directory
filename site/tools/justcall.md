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

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - JustCall publishes self-serve plans and titles its own pricing page "Business Phone System Plans Starting from $29/Month". That page lists "API access & workflows" as a plan feature, described as "Build custom workflows for your business with JustCall's open APIs. (up to 1,800 requests/hour)". The per-tier feature matrix is rendered client-side and did not fetch, so the exact plan floor for API access is not recorded here rather than guessed.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/saaslabsco/justcall-mcp-server](https://github.com/saaslabsco/justcall-mcp-server)

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

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

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
