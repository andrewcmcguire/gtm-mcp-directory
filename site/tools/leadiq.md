# LeadIQ: MCP server status, API access gate and what it does

> A B2B contact and company database with a Chrome extension for prospecting on LinkedIn and Sales Navigator,... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
LeadIQ

# LeadIQ

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [leadiq.com](https://leadiq.com) · entry id 01-leadiq · source 01-data-enrichment.md line 796

**What it does**
A B2B contact and company database with a Chrome extension for prospecting on LinkedIn and Sales Navigator, CRM enrichment, and champion-tracking (job-change) alerts, now also reachable as a verified Claude connector so prospect search and enrichment can be run from a chat.

**AI features, separated from automation with an AI label on it**
"Lando" is the vendor's named AI agent and an AI writing assistant drafts outreach; the MCP layer adds natural-language search over the database. The core reveal-a-contact function is a credit-billed database lookup, not model output.

**RevOps role**
Contact-data and job-change-signal source feeding the CRM and the sequencer, typically the SDR's in-browser prospecting tool rather than a batch enrichment backend.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The vendor's page states the connector is added from the AI client's connector directory and the user then signs in with LeadIQ credentials to authorize; no API key is entered into the client.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.leadiq.com/mcp (product page: https://leadiq.com/leadiq-mcp)

- [https://mcp.leadiq.com/mcp](https://mcp.leadiq.com/mcp)
- [https://leadiq.com/leadiq-mcp](https://leadiq.com/leadiq-mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

120 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 105 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's own MCP page states "You'll need an active LeadIQ paid subscription to use this integration" and, on cost, that "Credit consumption works the same as in the LeadIQ app." A free tier of the core product exists (the site's primary call to action is "Start free") but it is not stated to reach the MCP.

**API documentation**

No documentation URL recorded.

328 of 374 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/leadiq](https://github.com/leadiq) tied to the vendor by rule 3, account website leadiq.com has the vendor's domain, confidence strong

- **Public repositories**: 4, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-06-30

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [api-samples](https://github.com/leadiq/api-samples) | docs or examples | | 0 | 2026-06-30 | |
| [dataiq-api-specs](https://github.com/leadiq/dataiq-api-specs) | API client | LeadIQ Contact Search APIs | 3 | 2021-07-09 | |
| [sttp-play](https://github.com/leadiq/sttp-play) | other | Play based backends and json packages for STTP | 0 | 2018-10-26 | |
| [apollo-link-defer](https://github.com/leadiq/apollo-link-defer) | other | Interface for creating asynchronous links. | 18 | 2018-08-15 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

103 of 374 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://leadiq.com/leadiq-mcp](https://leadiq.com/leadiq-mcp)
- [https://leadiq.com/pricing](https://leadiq.com/pricing)
- [https://mcp.leadiq.com/mcp](https://mcp.leadiq.com/mcp)

3 source URLs. Raw sources field, verbatim:

https://leadiq.com/leadiq-mcp, https://leadiq.com/pricing, https://mcp.leadiq.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.leadiq.com/mcp returned HTTP 401 with {"code":"unauthorized","message":"Authentication required"}, confirming a live auth-gated server. The endpoint is not printed on the vendor page, which is written for a non-technical buyer and routes entirely through the Claude connector directory; the address above came from the candidate research and was confirmed by probe rather than by vendor text, and that distinction matters if the vendor moves it. LeadIQ describes itself as a "Verified Connector" in Anthropic's directory, which is a review of security, reliability and compatibility, not a statement about data quality. The pricing page renders its tier table client-side and the fetch on this date returned only surrounding copy, so no per-plan price is recorded here; the paid-subscription requirement is quoted from the MCP page's own FAQ instead. Credits are consumed per company lookup or contact enrichment exactly as in the app, so an agent left to loop can spend a plan's credits with no human in the path. 2026-09-07: https://mcp.leadiq.com/mcp returned 401 to an MCP initialize POST (https://mcp.leadiq.com/mcp).

**Provenance**

- **Entry id**: 01-leadiq

- **Source file**: 01-data-enrichment.md

- **Source line**: 796

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
