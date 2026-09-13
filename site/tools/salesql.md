# SalesQL: MCP server status, API access gate and what it does

> A LinkedIn-first contact database and browser extension that returns verified work emails and mobile numbers,... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
SalesQL

# SalesQL

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [salesql.com](https://salesql.com) · entry id 01-salesql · source 01-data-enrichment.md line 815

**What it does**
A LinkedIn-first contact database and browser extension that returns verified work emails and mobile numbers, with bulk CSV enrichment, an email verifier, a REST API and an MCP server that exposes search and enrichment to an AI client.

**AI features, separated from automation with an AI label on it**
Marketed as "AI Search" for the prospecting query builder; the reveal and verification steps are deterministic lookups against the database plus a verifier, not model inference. The MCP server's own framing is the notable part: search returns masked contacts for free and credits are spent only on the records the user chooses to reveal.

**RevOps role**
A low-cost contact-detail provider for LinkedIn-sourced prospecting, usable directly by a rep in the browser or as one provider inside a waterfall behind an agent.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The vendor's docs record "Auth OAuth 2.1" with an MCP key as the fallback for clients that cannot carry the OAuth flow.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.salesql.com/mcp (docs: https://salesql.com/docs/mcp; product page: https://salesql.com/mcp)

- [https://mcp.salesql.com/mcp](https://mcp.salesql.com/mcp)
- [https://salesql.com/docs/mcp](https://salesql.com/docs/mcp)
- [https://salesql.com/mcp](https://salesql.com/mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 380 entries that record an official or community MCP server carry a harvested tool list. The other 261 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's MCP page states "MCP access on the Professional and Organization plans", and the pricing table shows API absent on Free ($0/month, 50 credits) and Basic ($39/month, 2,000 credits) and present on Professional ($79/month, 5,000 API calls/day) and Organization ($119/month, 20,000 API calls/day).

**API documentation**

No documentation URL recorded.

528 of 784 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/salesql/claude-plugin](https://github.com/salesql/claude-plugin)

**On GitHub**

[github.com/salesql](https://github.com/salesql) tied to the vendor by rule 3, account website salesql.com has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-08-25

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [claude-plugin](https://github.com/salesql/claude-plugin) | MCP server | Official SalesQL plugin for Claude Code. connect the SalesQL MCP server and prospect, enrich and reveal B2B contacts... | 0 | 2026-08-25 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

513 of 784 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://salesql.com/mcp](https://salesql.com/mcp)
- [https://salesql.com/docs/mcp](https://salesql.com/docs/mcp)
- [https://salesql.com/pricing](https://salesql.com/pricing)
- [https://salesql.com/](https://salesql.com/)
- [https://mcp.salesql.com/mcp](https://mcp.salesql.com/mcp)
- [https://github.com/salesql/claude-plugin](https://github.com/salesql/claude-plugin)

6 source URLs. Raw sources field, verbatim:

https://salesql.com/mcp, https://salesql.com/docs/mcp, https://salesql.com/pricing, https://salesql.com/, https://mcp.salesql.com/mcp, https://github.com/salesql/claude-plugin

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.salesql.com/mcp returned HTTP 401 with an invalid_token error, confirming a live auth-gated server, and the endpoint, transport (Streamable HTTP) and auth model are all printed on the vendor's own docs page rather than inferred. Named tools seen on the vendor pages include search_people, enrich_person and enrich_person_bulk, the last documented as accepting up to 100 profiles in one call. The free-search, paid-reveal split deserves a line in any write-up: it is the inverse of the usual MCP failure mode, where an agent burns credits exploring. The MCP shares one credit balance with the REST API, so an agent and a script compete for the same pool. Vendor claims of 800,000+ users and a 4.8 average across 917 reviews are marketing figures and are recorded as claims, not findings. 2026-09-07: Official MCP registry carries com.salesql/salesql (DNS-verified salesql.com namespace) with remote https://mcp.salesql.com/mcp; that URL returned 401 to an MCP initialize (https://mcp.salesql.com/mcp). 2026-09-09 (P6-04 repo sweep): first-party repository recorded at https://github.com/salesql/claude-plugin, the org salesql (profile site salesql.com), last push 2026-08-25. It is NOT the server source. Its README reads "Official SalesQL plugin for Claude Code" and it wires the hosted SalesQL MCP server; the server itself is closed and hosted at the endpoint in mcp_url, which the official registry entry com.salesql/salesql (DNS-verified salesql.com namespace) also lists as a remote with no repository field. No public server source was found.

**Provenance**

- **Entry id**: 01-salesql

- **Source file**: 01-data-enrichment.md

- **Source line**: 815

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
