# CatchIntent: MCP server status, API access gate and what it does

> A B2B intent tool that monitors social and web sources for buying signals, ranks the people behind them by... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
CatchIntent

# CatchIntent

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [catchintent.com](https://catchintent.com) · entry id 05-catchintent · source 05-signals-intent-abm.md line 668

**What it does**
A B2B intent tool that monitors social and web sources for buying signals, ranks the people behind them by warmth, enriches the profiles and drafts personalised openers, then pushes leads to a CRM or outreach account.

**AI features, separated from automation with an AI label on it**
The vendor names "Bedrock-powered enrichment" to fill buyer profiles and AI-drafted openers matching brand voice; the signal detection itself is listening plus ranking. Its changelog frames the MCP server as the agent surface: "Connect Claude, Cursor, or any MCP-compatible AI tool to your CatchIntent workspace."

**RevOps role**
A signal-to-outreach layer for small teams: social-listening intent in, ranked warm leads with drafted openers out, feeding a CRM or a sequencer.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The vendor's MCP page states "One-time OAuth 2.1 authorization. Your MCP client opens a browser, you sign into CatchIntent, pick the workspace, and approve the requested scopes."

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://engine.catchintent.com/mcp (vendor page: https://catchintent.com/mcp; changelog v3.0.0 dated 2026-05-13: https://catchintent.com/changelog/)

- [https://engine.catchintent.com/mcp](https://engine.catchintent.com/mcp)
- [https://catchintent.com/mcp](https://catchintent.com/mcp)
- [https://catchintent.com/changelog/](https://catchintent.com/changelog/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's MCP page states "MCP access is included on every plan, Growth, Scale, and Enterprise. The free 7-day trial includes full MCP access." The pricing page lists Growth (1,000 leads/month), Scale (4,000 leads/month) and Enterprise (25,000+ leads/month) without dollar figures, plus a Done-for-You service "Starting at $1,999/mo, 3-month minimum"; "Card on file is required" for the trial. No free plan.

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

- [https://catchintent.com/mcp](https://catchintent.com/mcp)
- [https://catchintent.com/changelog/](https://catchintent.com/changelog/)
- [https://catchintent.com/pricing](https://catchintent.com/pricing)
- [https://engine.catchintent.com/mcp](https://engine.catchintent.com/mcp)

4 source URLs. Raw sources field, verbatim:

https://catchintent.com/mcp, https://catchintent.com/changelog/, https://catchintent.com/pricing, https://engine.catchintent.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://engine.catchintent.com/mcp with no credentials returned HTTP 200 with a JSON-RPC result, serverInfo name "catchintent" version "2.0.0"; the control POST to /zzz-not-a-route returned 404 with a JSON body reading "Cannot POST /zzz-not-a-route". Live first-party server; initialize is open and the OAuth gate sits at tool-call time. The vendor's own MCP page says "28+ typed tools across six surfaces" while the v3.0.0 changelog line says "27 typed tools"; both vendor figures are recorded as found, not reconciled. The pricing page publishes plan sizes but no plan prices, so the api_gate is paid on the vendor's own statement that every plan is paid, with the amount unknown. The catchintent.com/mcp page is not linked from the homepage; it was reached via the registry listing that named the endpoint. 2026-09-07: https://engine.catchintent.com/mcp returned 200 with a JSON-RPC initialize result to an MCP initialize POST (https://engine.catchintent.com/mcp).

**Provenance**

- **Entry id**: 05-catchintent

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 668

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
