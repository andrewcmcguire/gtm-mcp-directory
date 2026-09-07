# Dialpad: MCP server status, API access gate and what it does

> An AI-native business communications platform covering cloud phone, contact centre, SMS and meetings, with an... Official MCP, Enterprise leaning. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Dialpad

# Dialpad

[Official MCP](../mcp/official.md)
[Enterprise leaning](../gates/enterprise-leaning.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [dialpad.com](https://dialpad.com) · entry id 02-dialpad · source 02-engagement-outbound.md line 523

**What it does**
An AI-native business communications platform covering cloud phone, contact centre, SMS and meetings, with an MCP server that exposes the Dialpad Public API surface (calls, contacts, call centres, coaching teams, transcripts) as tools an assistant can call.

**AI features, separated from automation with an AI label on it**
Real and central to the product: live transcription, AI recaps, sentiment analysis, AI scorecards and live coaching are all first-party features rather than bolt-ons, and the MCP server's read tools return that AI-derived call data (transcripts, action items) rather than only raw call metadata.

**RevOps role**
The dialer and conversation-capture layer of an outbound stack, and, via MCP, a way for an agent to read call outcomes and transcripts and act on them without a separate conversation-intelligence tool in the middle.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The docs state the server is hosted by Dialpad, supports Dynamic Client Registration so clients register themselves on first connect, acts on the signed-in user's behalf within their existing permissions, and holds sessions for 24 hours before prompting a fresh sign-in. The docs are explicit that "there are no API keys, service accounts, or admin setup steps involved", which contradicts the marketing page.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp-public.us.karehq.com/mcp for United States tenants and https://mcp-public.eu.karehq.com/mcp for Europe (docs: https://developers.dialpad.com/docs/dialpad-mcp-server; marketing page: https://www.dialpad.com/mcp/)

- [https://mcp-public.us.karehq.com/mcp](https://mcp-public.us.karehq.com/mcp)
- [https://mcp-public.eu.karehq.com/mcp](https://mcp-public.eu.karehq.com/mcp)
- [https://developers.dialpad.com/docs/dialpad-mcp-server](https://developers.dialpad.com/docs/dialpad-mcp-server)
- [https://www.dialpad.com/mcp/](https://www.dialpad.com/mcp/)

**Access gate**

- **Gate bucket**: Enterprise leaning

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-leaning - the MCP server is gated by an Early Access Program, not by a price. The vendor's developer docs carry the banner "This is an Early Access Program feature. Please contact your Customer Success Manager to request access", and add that if the company is not enrolled the calls fail with HTTP 403. Dialpad's own pricing page renders its per-seat tiers client-side and the fetch on this date returned only the AI Agent tab, whose pricing is conversation-based and routed to "Talk to sales".

**API documentation**

No documentation URL recorded.

289 of 318 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

47 of 318 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://developers.dialpad.com/docs/dialpad-mcp-server](https://developers.dialpad.com/docs/dialpad-mcp-server)
- [https://www.dialpad.com/mcp/](https://www.dialpad.com/mcp/)
- [https://www.dialpad.com/pricing/](https://www.dialpad.com/pricing/)
- [https://mcp-public.us.karehq.com/mcp](https://mcp-public.us.karehq.com/mcp)

4 source URLs. Raw sources field, verbatim:

https://developers.dialpad.com/docs/dialpad-mcp-server, https://www.dialpad.com/mcp/, https://www.dialpad.com/pricing/, https://mcp-public.us.karehq.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp-public.us.karehq.com/mcp returned HTTP 401 with {"detail":"Authorization header missing or invalid format."}, confirming a live auth-gated server. TWO CORRECTIONS TO THE CANDIDATE ROW, both material. First, the endpoint is not on a dialpad.com host at all: mcp.dialpad.com does not resolve (DNS failure on this date), and the documented server URLs are on karehq.com, a domain Dialpad acquired with Kare Knowledgeware. An operator checking only dialpad.com would conclude no server exists. Second, the marketing page at dialpad.com/mcp shows an API key (dp_...) in its illustrations and claims "100+ pre-built actions", while the developer docs state OAuth with no API keys and count "36 tools are exposed by the Dialpad MCP Server today". Where the two disagree the developer docs are treated as authoritative and both figures are recorded. Tool groups documented: Calls, Call Centers, Coaching Teams, Contacts, Departments and Offices, and more. The tools are built out of the Dialpad Public APIs, so MCP reach equals API reach. 2026-09-07: Both regional endpoints answered 401 to an MCP initialize POST: https://mcp-public.us.karehq.com/mcp and https://mcp-public.eu.karehq.com/mcp. karehq.com is Dialpad-operated (Kare was acquired by Dialpad) (https://mcp-public.us.karehq.com/mcp).

**Provenance**

- **Entry id**: 02-dialpad

- **Source file**: 02-engagement-outbound.md

- **Source line**: 523

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
