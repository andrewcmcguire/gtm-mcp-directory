# Saleshandy: MCP server status, API access gate and what it does

> A cold-email outreach platform with sequences, sender rotation, email warm-up and deliverability tooling,... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Saleshandy

# Saleshandy

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [saleshandy.com](https://saleshandy.com) · entry id 02-saleshandy · source 02-engagement-outbound.md line 580

**What it does**
A cold-email outreach platform with sequences, sender rotation, email warm-up and deliverability tooling, plus a Lead Finder contact database, exposed to AI clients through an MCP server that can create sequences, add prospects, verify addresses and read campaign and sender-health stats.

**AI features, separated from automation with an AI label on it**
An "AI Sequence Copilot" drafts and optimises sequences and an AI prospect-enrichment feature is sold alongside; the sending, rotation and warm-up machinery is deterministic infrastructure. The MCP server's own pitch is execution without the UI rather than added intelligence.

**RevOps role**
The sending layer of a cold-outbound stack, and one of the few in this category where an agent can build and launch a sequence end to end rather than only reading results.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth, with an api key fallback. The developer docs state "Saleshandy MCP uses OAuth for authentication - no API key needed for most clients" and document a key path for clients that cannot carry OAuth, generated at my.saleshandy.com under Settings then API Key and shown only once.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.saleshandy.com/mcp (docs: https://developer.saleshandy.com/api-reference/mcp; product page: https://www.saleshandy.com/mcp)

- [https://mcp.saleshandy.com/mcp](https://mcp.saleshandy.com/mcp)
- [https://developer.saleshandy.com/api-reference/mcp](https://developer.saleshandy.com/api-reference/mcp)
- [https://www.saleshandy.com/mcp](https://www.saleshandy.com/mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - published self-serve tiers are Starter $34/month, Pro $76/month and Scale $149/month billed annually, each with a 7-day free trial, and the pricing page's feature list includes a row reading "MCP and CLI: Connect AI assistants, ChatGPT, Claude, Gemini, and more, to Saleshandy via the Model Context Protocol (MCP)" alongside "Platform API access: Push and pull data programmatically with the REST API." The per-tier ticks for those two rows are rendered client-side and did not fetch, so the plan floor is not recorded here.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://developer.saleshandy.com/api-reference/mcp](https://developer.saleshandy.com/api-reference/mcp)
- [https://www.saleshandy.com/mcp](https://www.saleshandy.com/mcp)
- [https://www.saleshandy.com/pricing/](https://www.saleshandy.com/pricing/)
- [https://mcp.saleshandy.com/mcp](https://mcp.saleshandy.com/mcp)

4 source URLs. Raw sources field, verbatim:

https://developer.saleshandy.com/api-reference/mcp, https://www.saleshandy.com/mcp, https://www.saleshandy.com/pricing/, https://mcp.saleshandy.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.saleshandy.com/mcp returned HTTP 401 with {"jsonrpc":"2.0","error":{"code":-32001,"message":"Authentication required. Use an API key or OAuth Bearer token."}}, which confirms a live auth-gated server and confirms both auth paths in one response. A second address, https://api.saleshandy.com/mcp, returned HTTP 406 with a content-type complaint rather than 404, so it exists but is not the documented entry point; the documented endpoint is the mcp.saleshandy.com one and that is what is recorded. WRITE ACCESS IS THE POINT AND THE RISK: the vendor's own copy is "Create sequences, add prospects, verify email addresses, and track performances, all without launching the app", so an agent with this connected can start real cold email against real people. Anyone bench-testing this should use a throwaway sending domain. Saleshandy also publishes an MCP CLI, listed in its own footer navigation next to "Model Context Protocol", which is a second surface worth checking. The MCP marketing page offers a 7-day free trial with no credit card, which is the cheapest hands-on path found in this category on this date. 2026-09-07: https://mcp.saleshandy.com/mcp returned 401 to an MCP initialize POST (https://mcp.saleshandy.com/mcp).

**Provenance**

- **Entry id**: 02-saleshandy

- **Source file**: 02-engagement-outbound.md

- **Source line**: 580

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
