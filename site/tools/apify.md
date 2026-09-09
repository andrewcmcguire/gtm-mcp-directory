# Apify: MCP server status, API access gate and what it does

> A cloud platform for running "Actors" (hosted scrapers and automation programs, thousands of them in a public... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Apify

# Apify

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07
CLI: actor

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [apify.com](https://apify.com) · entry id 01-apify · source 01-data-enrichment.md line 892

**What it does**
A cloud platform for running "Actors" (hosted scrapers and automation programs, thousands of them in a public store) that extract web data such as LinkedIn posts, Google Maps listings, company sites and social feeds into datasets, with an API, scheduling and storage.

**AI features, separated from automation with an AI label on it**
The platform itself is scraping infrastructure, not AI. AI shows up as the MCP server (search Actors, call Actors and read datasets from an agent) and as individual store Actors that wrap LLM steps; the vendor's MCP docs describe Actor discovery, execution, documentation search and storage tools.

**RevOps role**
The list-building and scraping substrate under a GTM stack: run a store Actor for LinkedIn company posts, Google Maps leads or job boards on a schedule and hand the dataset to enrichment or a CRM.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth (recommended, browser sign-in) or an Apify API token as an Authorization Bearer header. The docs state "The Apify MCP server accepts requests without an API token when the tools query parameter contains only tools enabled for unauthenticated use" (discovery and docs); running Actors and reading storage require a token.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.apify.com (docs: https://docs.apify.com/platform/integrations/mcp; registry name com.apify/apify-mcp-server)

- [https://mcp.apify.com](https://mcp.apify.com)
- [https://docs.apify.com/platform/integrations/mcp](https://docs.apify.com/platform/integrations/mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-09. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: actor
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-09

Install, as the source shows it:

```
npm install -g apify-cli
```

quoted from [https://www.npmjs.com/package/apify-cli](https://www.npmjs.com/package/apify-cli) on 2026-09-09, via npm

```
brew install apify-cli
```

quoted from [https://formulae.brew.sh/formula/apify-cli](https://formulae.brew.sh/formula/apify-cli) on 2026-09-09, via brew

Packages seen, with the version on 2026-09-09:

- [npm: apify-cli 1.10.0](https://www.npmjs.com/package/apify-cli)
- [brew: apify-cli 1.10.0](https://formulae.brew.sh/formula/apify-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-09.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the pricing page lists Free at $0/month with "$5" of monthly prepaid platform usage and "No credit card is required", then Starter $19/month, Scale $199/month and Business $999/month. The Free plan "lets you use most of the features of the Apify platform, but with certain limits" (5 concurrent runs, rented Actors on trial only).

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/apify](https://github.com/apify) tied to the vendor by rule 3, account website https://apify.com/ has the vendor's domain, confidence strong

- **Public repositories**: 122, forks excluded, as read on 2026-09-08
- **Mention MCP**: 12 of them
- **Look like CLIs**: 3 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [agent-skills](https://github.com/apify/agent-skills) | other | Collection of Apify agent skills | 2,371 | 2026-09-08 | |
| [apify-evals](https://github.com/apify/apify-evals) | other | | 0 | 2026-09-08 | |
| [cgroups-sensor](https://github.com/apify/cgroups-sensor) | other | Utility functions to measure resource limits from cgroups in scenarios where psutils is not sufficient. | 0 | 2026-09-08 | |
| [actor-templates](https://github.com/apify/actor-templates) | docs or examples | This project is the :house: home of Apify Actor templates to help users quickly get started. Contributions welcome! | 60 | 2026-09-08 | |
| [apify-mcp-server](https://github.com/apify/apify-mcp-server) | MCP server | The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites,... | 6,380 | 2026-09-08 | v0.15.4 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://docs.apify.com/platform/integrations/mcp](https://docs.apify.com/platform/integrations/mcp)
- [https://apify.com/pricing](https://apify.com/pricing)
- [https://mcp.apify.com](https://mcp.apify.com)

3 source URLs. Raw sources field, verbatim:

https://docs.apify.com/platform/integrations/mcp, https://apify.com/pricing, https://mcp.apify.com

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.apify.com returned HTTP 401 with JSON reading "Missing or invalid access token. Pass an Apify API token in the Authorization: Bearer <token> header"; the control POST to /zzz-not-a-route returned 404 with a body that begins "There is nothing at route POST /zzz-not-a-route. This Model Context Protocol (MCP) server supports the Streamable HTTP transport", which is the server identifying itself on its own 404 page. Live first-party auth-gated server. STANDING CATEGORY RISK: many store Actors scrape LinkedIn and other sites whose terms prohibit automation; the account-ban and legal exposure sits with the operator, not the platform. The pricing page states free-plan usage credits "expire at the end of the billing cycle". 2026-09-07: https://mcp.apify.com returned 401 to an MCP initialize POST (https://mcp.apify.com).

**Provenance**

- **Entry id**: 01-apify

- **Source file**: 01-data-enrichment.md

- **Source line**: 892

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-09

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
