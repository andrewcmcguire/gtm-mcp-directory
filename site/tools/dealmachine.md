# DealMachine: MCP server status, API access gate and what it does

> Search and enrich US property, owner, people, and company data for sales and lead generation. Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
DealMachine

# DealMachine

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-12
CLI: dm

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [mcp.dealmachine.com](https://mcp.dealmachine.com) · entry id 01-dealmachine · source 01-data-enrichment.md line 4196

**What it does**
Search and enrich US property, owner, people, and company data for sales and lead generation.

**AI features, separated from automation with an AI label on it**
Not evidenced from fetched pages this pass; no AI feature claims recorded without a source URL.

**RevOps role**
Upstream contact/company data or enrichment utility feeding CRM and outbound tooling

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: not recorded

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-12 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/DealMachine/dealmachine-cli

- [https://github.com/DealMachine/dealmachine-cli](https://github.com/DealMachine/dealmachine-cli)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

138 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 603 are unmeasured, which is not the same as empty. Harvest last run 2026-09-15. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: dm
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-15

Install, as the source shows it:

```
npm install -g dealmachine
```

quoted from [https://www.npmjs.com/package/dealmachine](https://www.npmjs.com/package/dealmachine) on 2026-09-15, via npm

```
npm install -g @dealmachine/cli
```

quoted from [https://www.npmjs.com/package/@dealmachine/cli](https://www.npmjs.com/package/@dealmachine/cli) on 2026-09-15, via npm

```
npm install -g @dealmachine/dealmachine-cli
```

quoted from [https://www.npmjs.com/package/@dealmachine/dealmachine-cli](https://www.npmjs.com/package/@dealmachine/dealmachine-cli) on 2026-09-15, via npm

```
npm install -g dealmachine-cli
```

quoted from [https://www.npmjs.com/package/dealmachine-cli](https://www.npmjs.com/package/dealmachine-cli) on 2026-09-15, via npm

Packages seen, with the version on 2026-09-15:

- [npm: dealmachine 0.3.0](https://www.npmjs.com/package/dealmachine)
- [npm: @dealmachine/cli 0.3.0](https://www.npmjs.com/package/@dealmachine/cli)
- [npm: @dealmachine/dealmachine-cli 0.1.0](https://www.npmjs.com/package/@dealmachine/dealmachine-cli)
- [npm: dealmachine-cli 0.1.0](https://www.npmjs.com/package/dealmachine-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-15.

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

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/DealMachine/dealmachine-cli](https://github.com/DealMachine/dealmachine-cli)

**On GitHub**

No GitHub organisation could be tied to mcp.dealmachine.com with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://mcp.dealmachine.com](https://mcp.dealmachine.com)
- [https://mcp.dealmachine.com/mcp](https://mcp.dealmachine.com/mcp)
- [https://github.com/DealMachine/dealmachine-cli](https://github.com/DealMachine/dealmachine-cli)

3 source URLs. Raw sources field, verbatim:

https://mcp.dealmachine.com, https://mcp.dealmachine.com/mcp, https://github.com/DealMachine/dealmachine-cli

**Notes, verbatim from the file**
what_it_does used staging desc because homepage meta description was empty. API mentioned on https://mcp.dealmachine.com/mcp; pricing/gate not inferred from presence alone. mcp_status=community from official-mcp-registry listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave Q 2026-09-12.

**Provenance**

- **Entry id**: 01-dealmachine

- **Source file**: 01-data-enrichment.md

- **Source line**: 4196

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-15

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
