# StackOne: MCP server status, API access gate and what it does

> A unified-API vendor that publishes a stated 518 managed MCP servers exposing 31,928 tools across HR, CRM, IT... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
StackOne

# StackOne

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [stackone.com](https://stackone.com) · entry id 07-stackone · source 07-mcp-infrastructure.md line 383

**What it does**
A unified-API vendor that publishes a stated 518 managed MCP servers exposing 31,928 tools across HR, CRM, IT and finance applications, reachable through one endpoint with per-account routing, plus dynamic tool discovery so an agent loads only the tools a task needs.

**AI features, separated from automation with an AI label on it**
Two that are more than plumbing, both vendor-claimed: a reinforcement-learning-trained tool-discovery layer the vendor says cuts context by 460 times, and a prompt-injection defence it claims detects hijacked tools at 88.7% accuracy before they reach the agent. Neither was independently verified; both are recorded as vendor claims.

**RevOps role**
The connector layer for a team that wants one governed endpoint in front of many GTM systems rather than a separate server per vendor, and the only layer in this group that publishes a searchable per-application MCP server directory.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Basic authentication plus a per-account identifier, with StackOne brokering OAuth, API keys and token refresh to each connected application on the customer's behalf.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.stackone.com/mcp ; https://api.stackone.com/mcp?x-account-id= (product page: https://www.stackone.com/platform/mcp/)

- [https://mcp.stackone.com/mcp](https://mcp.stackone.com/mcp)
- [https://api.stackone.com/mcp?x-account-id=](https://api.stackone.com/mcp?x-account-id=)
- [https://www.stackone.com/platform/mcp/](https://www.stackone.com/platform/mcp/)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the vendor's pricing page publishes a "Starter" Gateway tier at "Free" including "1,000 credits / seat / month", where the page states "one tool call or API call costs 1 credit", with an OEM track and enterprise deployment routed to "Book Demo".

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

- [https://www.stackone.com/platform/mcp/](https://www.stackone.com/platform/mcp/)
- [https://www.stackone.com/pricing/](https://www.stackone.com/pricing/)
- [https://api.stackone.com/mcp](https://api.stackone.com/mcp)
- [https://docs.stackone.com/mcp](https://docs.stackone.com/mcp)
- [https://mcp.stackone.com/mcp](https://mcp.stackone.com/mcp)

5 source URLs. Raw sources field, verbatim:

https://www.stackone.com/platform/mcp/, https://www.stackone.com/pricing/, https://api.stackone.com/mcp, https://docs.stackone.com/mcp, https://mcp.stackone.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://api.stackone.com/mcp returned HTTP 401 with {"statusCode":401,"message":"Unauthorized"}, confirming a live auth-gated server. NAME COLLISION INSIDE ONE VENDOR, worth recording because it will catch an automated verifier: https://docs.stackone.com/mcp is also a live MCP server, but it is a Mintlify documentation server whose tools are search_stackone and query_docs_filesystem_stackone over StackOne's own docs, and it is read-only and scoped to published site content. It is not the unified-API server and must not be recorded as the product endpoint. The vendor's positioning line is a direct swipe at this directory's own subject matter and is quotable: "First-party MCPs weren't built for production. StackOne's are." GTM connectors the research surfaced on StackOne include Salesloft, JustCall, Dialpad, Help Scout, RingCentral and Aircall, which means several vendors in this directory can be reached either directly or through StackOne, and a buyer should compare rather than assume the wrapper is worse. Vendor also advertises automated creation of new MCP servers, which would make the 518 figure a moving number. 2026-09-07: Official MCP registry carries com.stackone/mcp (DNS-verified stackone.com namespace) with remote https://mcp.stackone.com/mcp; that URL returned 401 to an MCP initialize, as did https://api.stackone.com/mcp (https://mcp.stackone.com/mcp).

**Provenance**

- **Entry id**: 07-stackone

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 383

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
