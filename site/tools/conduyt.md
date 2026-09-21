# Conduyt: MCP server status, API access gate and what it does

> The CRM built for teams that move fast. Pipeline, messaging, and data. No middleman. Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Conduyt

# Conduyt

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-12
CLI: conduyt

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [conduyt.app](https://conduyt.app) · entry id 07-conduyt · source 07-mcp-infrastructure.md line 918

**What it does**
The CRM built for teams that move fast. Pipeline, messaging, and data. No middleman.

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

140 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 601 are unmeasured, which is not the same as empty. Harvest last run 2026-09-18. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: conduyt
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-18

Install, as the source shows it:

```
npx -y @mvanhorn/printing-press
```

quoted from [https://conduyt.app/docs](https://conduyt.app/docs) on 2026-09-18, via npx

```
npm install -g conduyt
```

quoted from [https://www.npmjs.com/package/conduyt](https://www.npmjs.com/package/conduyt) on 2026-09-18, via npm

Login or key hint seen on the page:

curl -H "Authorization: Bearer YOUR_API_KEY" \

Subcommands seen with the binary:

contacts, deals, doctor, insights

Packages seen, with the version on 2026-09-18:

- [npm: conduyt 1.49.0](https://www.npmjs.com/package/conduyt)

Where it was documented:

- [https://conduyt.app/docs](https://conduyt.app/docs) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-18.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

[https://conduyt.app/docs](https://conduyt.app/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to conduyt.app with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://conduyt.app](https://conduyt.app)
- [https://conduyt.app/docs](https://conduyt.app/docs)
- [https://conduyt.app/developers](https://conduyt.app/developers)
- [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm)

4 source URLs. Raw sources field, verbatim:

https://conduyt.app, https://conduyt.app/docs, https://conduyt.app/developers, https://www.npmjs.com/search?q=mcp%20crm

**Notes, verbatim from the file**
API mentioned on https://conduyt.app/developers; pricing/gate not inferred from presence alone. mcp_status=community from discovery source npm-mcp-gtm; mcp_url is the listed package/repo URL, not an official vendor MCP claim. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave D 2026-09-12: canonical name Conduyt (draft listed as conduyt-mcp).

**Provenance**

- **Entry id**: 07-conduyt

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 918

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-20

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
