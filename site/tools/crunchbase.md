# Crunchbase: MCP server status, API access gate and what it does

> A private-company database covering company profiles, funding rounds, investors, people and acquisitions,... Official MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Crunchbase

# Crunchbase

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07
CLI: crunchbase-cli (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [crunchbase.com](https://crunchbase.com) · entry id 01-crunchbase · source 01-data-enrichment.md line 739

**What it does**
A private-company database covering company profiles, funding rounds, investors, people and acquisitions, sold as a web product, a REST API and, since 2026, a first-party MCP server that exposes the same data to AI assistants.

**AI features, separated from automation with an AI label on it**
Crunchbase's own layer is predictive rather than generative: it publishes funding, growth, acquisition and IPO predictions plus Heat and Growth scores derived from its signal set, and the vendor states 15M+ private company predictions are refreshed weekly. The MCP server adds LLM-native access to that data (expert tools that translate plain language into a Crunchbase search, plus structured lookup and list tools), but the reasoning is done by the client model, not by Crunchbase.

**RevOps role**
Upstream firmographic and funding-signal source for account research, ICP definition and territory planning, feeding lists into the CRM or an enrichment layer rather than sitting in the outbound path itself.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.1. The user signs in with their normal Crunchbase account in the AI client's browser flow; Crunchbase then checks that the account holds an MCP seat before the connection completes.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.crunchbase.com (docs: https://data.crunchbase.com/docs/mcp-overview and https://about.crunchbase.com/products/crunchbase-mcp)

- [https://mcp.crunchbase.com](https://mcp.crunchbase.com)
- [https://data.crunchbase.com/docs/mcp-overview](https://data.crunchbase.com/docs/mcp-overview)
- [https://about.crunchbase.com/products/crunchbase-mcp](https://about.crunchbase.com/products/crunchbase-mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 471 entries that record an official or community MCP server carry a harvested tool list. The other 352 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: crunchbase-cli
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g crunchbase-cli
```

quoted from [https://www.npmjs.com/package/crunchbase-cli](https://www.npmjs.com/package/crunchbase-cli) on 2026-09-12, via npm, a third party source

Packages seen, with the version on 2026-09-12:

- [npm: crunchbase-cli 1.0.0, third party](https://www.npmjs.com/package/crunchbase-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only - the vendor's own MCP overview states "MCP is purchased per workspace and access is assigned per user as an MCP seat by your workspace admin" and directs new buyers to "contact your account team to add MCP to your workspace"; the Crunchbase API product page publishes no price and every call to action on it is "Talk to Sales". Crunchbase Pro is separately self-serve, but a Pro subscription is not stated to include an MCP seat.

**API documentation**

No documentation URL recorded.

629 of 982 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/crunchbase](https://github.com/crunchbase) tied to the vendor by rule 3, account website https://www.crunchbase.com has the vendor's domain, confidence strong

- **Public repositories**: 0, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: not recorded

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

711 of 982 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://data.crunchbase.com/docs/mcp-overview](https://data.crunchbase.com/docs/mcp-overview)
- [https://data.crunchbase.com/docs/getting-started-with-mcp.md](https://data.crunchbase.com/docs/getting-started-with-mcp.md)
- [https://data.crunchbase.com/docs/connecting-ai-tools.md](https://data.crunchbase.com/docs/connecting-ai-tools.md)
- [https://about.crunchbase.com/products/crunchbase-mcp](https://about.crunchbase.com/products/crunchbase-mcp)
- [https://about.crunchbase.com/products/crunchbase-api](https://about.crunchbase.com/products/crunchbase-api)
- [https://about.crunchbase.com/products/crunchbase-pro](https://about.crunchbase.com/products/crunchbase-pro)
- [https://mcp.crunchbase.com](https://mcp.crunchbase.com)

7 source URLs. Raw sources field, verbatim:

https://data.crunchbase.com/docs/mcp-overview, https://data.crunchbase.com/docs/getting-started-with-mcp.md, https://data.crunchbase.com/docs/connecting-ai-tools.md, https://about.crunchbase.com/products/crunchbase-mcp, https://about.crunchbase.com/products/crunchbase-api, https://about.crunchbase.com/products/crunchbase-pro, https://mcp.crunchbase.com

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.crunchbase.com returned HTTP 401, which confirms a live auth-gated server at that address. The endpoint is not printed on the marketing page; it comes from the vendor's own Connecting AI Tools doc, which gives the bare host with no path plus a Claude Code one-liner (claude mcp add --transport http --scope user crunchbase https://mcp.crunchbase.com). Docs state the server exposes both expert tools (plain-language question answering and query translation) and structured tools (entity lookup, explicit search, list creation and management), and claim that "Everything available through the Crunchbase API is available through the MCP server". Two gates stack here and should not be conflated: the AI-client side is cheap (the docs state the connector can be added "even if you are on a free Claude plan") while the Crunchbase side requires a purchased MCP seat. The docs also state that data access for applications built on the MCP server differs from individual seat access and routes to the account team. Cross-reference: this vendor is also a funding-signal source and 05-signals-intent-abm.md could reasonably cross-list it; 01 is treated as canonical. 2026-09-07: https://mcp.crunchbase.com is on the vendor domain and returned 401 to an MCP initialize POST (https://mcp.crunchbase.com).

**Provenance**

- **Entry id**: 01-crunchbase

- **Source file**: 01-data-enrichment.md

- **Source line**: 739

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
