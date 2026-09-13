# PandaDoc: MCP server status, API access gate and what it does

> Document builder/e-signature platform for proposals, quotes, and contracts, with AI-assisted content... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
PandaDoc

# PandaDoc

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-09-07
CLI: pandadoc (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [pandadoc.com](https://pandadoc.com) · entry id 13-pandadoc · source 13-proposals-deals.md line 14

**What it does**
Document builder/e-signature platform for proposals, quotes, and contracts, with AI-assisted content generation and CRM-linked workflows.

**AI features, separated from automation with an AI label on it**
AI-assisted document drafting and content suggestions inside the editor; the MCP server itself is an access/automation layer (search, create-from-template, send-and-track), not a new AI capability in itself.

**RevOps role**
Proposal/quote/e-signature system of record, one of the more genuinely solo-operator-accessible tools in this category on both API and MCP access.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - remote hosted server, add the server URL to an MCP client (Claude Desktop, Claude Code, Cursor, VS Code, Gemini, etc.) and authenticate via OAuth.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.pandadoc.com/v1/mcp ; https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server ; hosted remote server at https://mcp.pandadoc.com/v1/mcp ; repo https://github.com/PandaDoc/mcp-server-guide

- [https://mcp.pandadoc.com/v1/mcp](https://mcp.pandadoc.com/v1/mcp)
- [https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server)
- [https://github.com/PandaDoc/mcp-server-guide](https://github.com/PandaDoc/mcp-server-guide)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: pandadoc
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
pip install pandadoc
```

quoted from [https://pypi.org/project/pandadoc/](https://pypi.org/project/pandadoc/) on 2026-09-12, via pypi, a third party source

Packages seen, with the version on 2026-09-12:

- [pypi: pandadoc 0.1.0, third party](https://pypi.org/project/pandadoc/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited). PandaDoc's Free plan now includes API access with both a sandbox and production API key at signup (60 documents/year, 5 templates, sandbox docs watermarked and limited to your own domain) - sources conflict on whether production API access requires a paid/Enterprise plan, so treat the free-tier claim as probable-but-recently-changed rather than fully certain; verify current terms before publishing.

**API documentation**

No documentation URL recorded.

428 of 559 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/PandaDoc/mcp-server-guide](https://github.com/PandaDoc/mcp-server-guide)

**On GitHub**

[github.com/PandaDoc](https://github.com/PandaDoc) tied to the vendor by rule 2, account website https://pandadoc.com has the vendor's domain, confidence strong

- **Public repositories**: 16, forks excluded, as read on 2026-09-08
- **Mention MCP**: 3 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [pandadoc-openapi-specification](https://github.com/PandaDoc/pandadoc-openapi-specification) | API client | | 6 | 2026-09-08 | v7.27.1 |
| [design-engineer-interview-200826-dry-run](https://github.com/PandaDoc/design-engineer-interview-200826-dry-run) | other | | 0 | 2026-08-20 | |
| [mcp-server-guide](https://github.com/PandaDoc/mcp-server-guide) | MCP server | Where to start to use PandaDoc MCP server | 2 | 2026-08-20 | v1.0.0 |
| [design-engineer-interview-170826](https://github.com/PandaDoc/design-engineer-interview-170826) | other | | 0 | 2026-08-17 | |
| [property-agreement-templates](https://github.com/PandaDoc/property-agreement-templates) | docs or examples | Free property and real estate agreement templates - residential and commercial leases, rental agreements,... | 0 | 2026-07-22 | v1.0.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Generate a proposal or quote](../jobs/generate-proposal-or-quote.md)
- [Send a document for signature](../jobs/send-document-for-signature.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 559 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server)
- [https://www.usecarly.com/blog/pandadoc-mcp/](https://www.usecarly.com/blog/pandadoc-mcp/)
- [https://www.pandadoc.com/blog/pandadoc-free-plan-api/](https://www.pandadoc.com/blog/pandadoc-free-plan-api/)
- [https://www.pandadoc.com/api/pricing/](https://www.pandadoc.com/api/pricing/)
- [https://www.pulsemcp.com/servers/dazanza-pandadoc](https://www.pulsemcp.com/servers/dazanza-pandadoc)
- [https://github.com/PandaDoc/mcp-server-guide](https://github.com/PandaDoc/mcp-server-guide)
- [https://mcp.pandadoc.com/v1/mcp](https://mcp.pandadoc.com/v1/mcp)

7 source URLs. Raw sources field, verbatim:

https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server, https://www.usecarly.com/blog/pandadoc-mcp/, https://www.pandadoc.com/blog/pandadoc-free-plan-api/, https://www.pandadoc.com/api/pricing/, https://www.pulsemcp.com/servers/dazanza-pandadoc, https://github.com/PandaDoc/mcp-server-guide, https://mcp.pandadoc.com/v1/mcp

**Notes, verbatim from the file**
PulseMCP also lists a third-party community server (dazanza-pandadoc) - prefer the official hosted one (mcp.pandadoc.com) documented on PandaDoc's own developer site. 2026-09-07: GitHub org PandaDoc (homepage developers.pandadoc.com). Repo mcp-server-guide holds server.json / mcp.json / .mcp.json - the registry and client manifests - and the official registry carries com.pandadoc.mcp/mcp (DNS-verified pandadoc.com namespace) pointing at this repo with remote https://mcp.pandadoc.com/v1/mcp, which returned 401 to an MCP initialize (https://github.com/PandaDoc/mcp-server-guide).

**Provenance**

- **Entry id**: 13-pandadoc

- **Source file**: 13-proposals-deals.md

- **Source line**: 14

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
