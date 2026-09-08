# Hex: MCP server status, API access gate and what it does

> A collaborative data workspace (SQL and Python notebooks, published apps, a conversational "Threads" analysis... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Hex

# Hex

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [hex.tech](https://hex.tech) · entry id 06-hex · source 06-revops-infra.md line 665

**What it does**
A collaborative data workspace (SQL and Python notebooks, published apps, a conversational "Threads" analysis mode) used by data and RevOps teams to answer questions on top of the warehouse.

**AI features, separated from automation with an AI label on it**
Hex's agent ("Threads") runs analyses from natural language, and the MCP server exposes exactly that surface: search projects, create a Thread, retrieve Thread results, continue a Thread. An MCP call therefore returns model-produced analysis, not raw table access.

**RevOps role**
The analysis layer above the warehouse for teams that have outgrown dashboards; the MCP lets an operator's assistant ask Hex's agent a question and read back the answer.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The docs state "Complete the OAuth flow to authorize access to your Hex workspace"; no token path is documented. "Hex MCP server is currently in beta."

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://app.hex.tech/mcp (docs: https://learn.hex.tech/docs/api-integrations/mcp-server; single-tenant and EU deployments use their own host)

- [https://app.hex.tech/mcp](https://app.hex.tech/mcp)
- [https://learn.hex.tech/docs/api-integrations/mcp-server](https://learn.hex.tech/docs/api-integrations/mcp-server)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the MCP docs state the server is "Available on the Team and Enterprise plans" only; the pricing page lists Community (free), Professional at "$36 per Editor/month", Team at "$75 per Editor/month" and Enterprise custom, with REST APIs from Professional up and an Observability API on Enterprise. "Anyone can try the Hex Team plan free for 14 days, no payment card required."

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

- [https://learn.hex.tech/docs/api-integrations/mcp-server](https://learn.hex.tech/docs/api-integrations/mcp-server)
- [https://hex.tech/pricing](https://hex.tech/pricing)
- [https://app.hex.tech/mcp](https://app.hex.tech/mcp)

3 source URLs. Raw sources field, verbatim:

https://learn.hex.tech/docs/api-integrations/mcp-server, https://hex.tech/pricing, https://app.hex.tech/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://app.hex.tech/mcp returned HTTP 401 with the text "Unauthorized"; the control POST to /zzz-not-a-route returned 404 with an Express-style "Cannot POST" page. Live first-party auth-gated server. The plan gate is unusually explicit for this directory: the vendor names the two plans that can use the MCP on the MCP page itself, which is the behaviour SCHEMA law 4 asks every vendor for. Team is $75 per editor per month, so the cheapest MCP-capable Hex seat is $900 a year. 2026-09-07: https://app.hex.tech/mcp returned 401 to an MCP initialize POST (https://app.hex.tech/mcp).

**Provenance**

- **Entry id**: 06-hex

- **Source file**: 06-revops-infra.md

- **Source line**: 665

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
