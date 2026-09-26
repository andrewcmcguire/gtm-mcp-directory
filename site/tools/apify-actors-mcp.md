# Apify Actors MCP: MCP server status, API access gate and what it does

> Connect Claude, Cursor, and your AI agents with thousands of web scraping and automation tools. Run Actors,... Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Apify Actors MCP

# Apify Actors MCP

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-12
CLI: actor

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [mcp.apify.com](https://mcp.apify.com) · entry id 07-apify-actors-mcp · source 07-mcp-infrastructure.md line 2530

**What it does**
Connect Claude, Cursor, and your AI agents with thousands of web scraping and automation tools. Run Actors, access results, and search Apify documentation.

**AI features, separated from automation with an AI label on it**
Homepage copy mentions AI/ML-related terms; specific AI feature list not independently verified beyond that mention this pass. See sources.

**RevOps role**
MCP server/client or agent-tooling infrastructure

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: not recorded

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-12 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://www.npmjs.com/search?q=mcp%20crm

- [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

140 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 601 are unmeasured, which is not the same as empty. Harvest last run 2026-09-26. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: actor
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-26

Install, as the source shows it:

```
npm install -g apify-cli
```

quoted from [https://www.npmjs.com/package/apify-cli](https://www.npmjs.com/package/apify-cli) on 2026-09-26, via npm

```
brew install apify-cli
```

quoted from [https://formulae.brew.sh/formula/apify-cli](https://formulae.brew.sh/formula/apify-cli) on 2026-09-26, via brew

Packages seen, with the version on 2026-09-26:

- [npm: apify-cli 1.10.0](https://www.npmjs.com/package/apify-cli)
- [brew: apify-cli 1.10.0](https://formulae.brew.sh/formula/apify-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-26.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

727 of 1252 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to mcp.apify.com with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://mcp.apify.com](https://mcp.apify.com)
- [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm)

2 source URLs. Raw sources field, verbatim:

https://mcp.apify.com, https://www.npmjs.com/search?q=mcp%20crm

**Notes, verbatim from the file**
mcp_status=community from discovery source npm-mcp-gtm; mcp_url is the listed package/repo URL, not an official vendor MCP claim. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave J 2026-09-12: canonical name Apify Actors MCP (draft listed as @apify/actors-mcp-server).

**Provenance**

- **Entry id**: 07-apify-actors-mcp

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 2530

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-26

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
