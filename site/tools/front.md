# Front: MCP server status, API access gate and what it does

> A shared-inbox and customer-communication platform where email, SMS, social and chat land in team inboxes... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Front

# Front

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [front.com](https://front.com) · entry id 14-front · source 14-inbound-plg-chat.md line 294

**What it does**
A shared-inbox and customer-communication platform where email, SMS, social and chat land in team inboxes with assignment, internal comments and rules, and, since July 2026, an MCP server that lets an AI agent search and read conversations, draft and send replies, comment, tag and assign, all as a named teammate.

**AI features, separated from automation with an AI label on it**
Front sells three priced AI add-ons: Autopilot, an omnichannel AI agent billed per conversation, Copilot, a real-time agent assistant, and Smart QA and Smart CSAT for automated review and satisfaction inference. The MCP server is separate from all of them and adds no intelligence of its own; it hands the inbox to whichever model the customer already uses.

**RevOps role**
The shared inbox where inbound demand actually lands for many sales and success teams, and through MCP the first point in this category where an agent can triage, route and reply inside the human queue rather than in a separate bot lane.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.1 with PKCE, per teammate. Front's docs state the server does not support Dynamic Client Registration, so the AI client must be able to send a confidential OAuth client ID and secret, and warn that "Some popular AI assistants are currently not compatible." Scopes are read, write and send, and every tool call attributes to a specific Front teammate.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official (open beta)

mcp_url, verbatim from the file:

https://mcp.frontapp.com/mcp (docs: https://dev.frontapp.com/docs/mcp-server)

- [https://mcp.frontapp.com/mcp](https://mcp.frontapp.com/mcp)
- [https://dev.frontapp.com/docs/mcp-server](https://dev.frontapp.com/docs/mcp-server)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 264 entries that record an official or community MCP server carry a harvested tool list. The other 145 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - Front publishes self-serve per-seat pricing starting at Starter "$25 /seat/mo, up to 10 seats", then Professional at "$65 /seat/mo, up to 50 seats" and Enterprise at "$105 /seat/mo", with no free tier. The MCP server carries no separate price and its docs state of the open beta that "Everyone has access". A separate paid add-on exists for raising API rate limits, listed at "$200 per 100 API requests/min per month".

**API documentation**

No documentation URL recorded.

400 of 514 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to front.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: front, frontendmentorio, FrontendMasters, frontendbr, front-end-by-rimantas. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

No job tag on this entry.

243 of 514 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://dev.frontapp.com/docs/mcp-server](https://dev.frontapp.com/docs/mcp-server)
- [https://front.com/pricing](https://front.com/pricing)
- [https://mcp.frontapp.com/mcp](https://mcp.frontapp.com/mcp)

3 source URLs. Raw sources field, verbatim:

https://dev.frontapp.com/docs/mcp-server, https://front.com/pricing, https://mcp.frontapp.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.frontapp.com/mcp returned HTTP 401 with {"error":"Missing authentication token."}, confirming a live auth-gated server, and the endpoint, transport (Streamable HTTP), spec version (2025-11-25), auth model and scopes are all printed on Front's own developer page. THE MISSING DCR IS THE FINDING and is the sort of detail this directory exists to record: an official server that a large share of MCP clients cannot connect to, because Front requires a confidential client and says so plainly. A user who installs Front from an official client directory skips the developer-app setup; everyone else has to create a Front developer app under Settings, Company, Developer, add an OAuth feature and supply the client ID and secret. Write and send scopes mean an agent connected here can email real customers as a named teammate, so the per-teammate attribution model is a safety feature worth understanding before a bench test rather than after. Open beta status is the vendor's own label, quoted: "This feature is in open beta. Everyone has access, but bug fixes, improvements, and other details are still being worked on." 2026-09-07: https://mcp.frontapp.com/mcp returned 401 to an MCP initialize POST. frontapp.com is Front's own API domain (https://mcp.frontapp.com/mcp).

**Provenance**

- **Entry id**: 14-front

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 294

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
