# Looker: MCP server status, API access gate and what it does

> Google Cloud's governed BI platform (LookML semantic model, explores, Looks, dashboards, embedded analytics)... Official MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Looker

# Looker

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [cloud.google.com/looker](https://cloud.google.com/looker) · entry id 06-looker · source 06-revops-infra.md line 687

**What it does**
Google Cloud's governed BI platform (LookML semantic model, explores, Looks, dashboards, embedded analytics) that sits on top of a warehouse; two first-party MCP routes exist, a local MCP Toolbox prebuilt server and a Looker-managed remote server in preview.

**AI features, separated from automation with an AI label on it**
The semantic layer is the value: the vendor's pitch is that an agent asks in business terms and "Looker generates the correct, optimized SQL". The MCP tools are metadata and query (get_models, get_explores, get_dimensions, get_measures, query, query_sql, run_look, make_dashboard, plus LookML authoring tools); Gemini-in-Looker features were not assessed.

**RevOps role**
The governed reporting layer above the warehouse in larger RevOps stacks; the MCP is the first sanctioned way for an agent to query the semantic model instead of scraping dashboards.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: The managed server uses OAuth 2.1 and an admin "must manually register AI agents as OAuth clients via the API Explorer"; all tools are "disabled by default" until an admin enables them, and "An AI agent cannot access data or models that the authenticated user is not authorized to see." The Toolbox route uses Looker API credentials in the LOOKER_BASE_URL, LOOKER_CLIENT_ID and LOOKER_CLIENT_SECRET environment variables and needs "MCP Toolbox version V1.0.0 or later".

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.cloud.google.com/looker/docs/mcp (Looker-managed server, preview, served at LOOKER_INSTANCE_URL/mcp per instance; local route: https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox using https://github.com/googleapis/mcp-toolbox run as "./toolbox --stdio --prebuilt looker"; launch post: https://cloud.google.com/blog/products/business-intelligence/introducing-looker-mcp-server)

- [https://docs.cloud.google.com/looker/docs/mcp](https://docs.cloud.google.com/looker/docs/mcp)
- [https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox](https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox)
- [https://github.com/googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)
- [https://cloud.google.com/blog/products/business-intelligence/introducing-looker-mcp-server](https://cloud.google.com/blog/products/business-intelligence/introducing-looker-mcp-server)

**What this server exposes**

- **Tools named**: 3
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-08
- **Repo read**: googleapis/mcp-toolbox
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **apply-spec-tool** a test description evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **example_tool** some description evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **my-tool** my tool description evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-08 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only - the pricing page states Looker (Google Cloud core) offers three platform editions (Standard "for small organizations or teams with fewer than 50 users" with "up to 1,000 query-based API calls per month", Enterprise with "up to 100,000 query-based API calls per month", and Embed), each on an "Annual commitment" with the cost cell reading "Call sales. Work with sales to identify a solution that works for you." No self-serve purchase and no published price.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)

**On GitHub**

[github.com/looker-open-source](https://github.com/looker-open-source) tied to the vendor by rule 3, account website https://cloud.google.com/looker has the vendor's domain, confidence strong

- **Public repositories**: 86, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 3 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [viz-report-table-marketplace-open-source](https://github.com/looker-open-source/viz-report-table-marketplace-open-source) | other | | 17 | 2026-09-07 | v1.1.4 |
| [viz-force_directed_graph-marketplace](https://github.com/looker-open-source/viz-force_directed_graph-marketplace) | other | | 7 | 2026-09-07 | |
| [app-lookml-diagram](https://github.com/looker-open-source/app-lookml-diagram) | plugin or integration | An "ERD for LookML". Now available for download on the Looker Marketplace. | 23 | 2026-09-07 | v2.0.9 |
| [app-data-dictionary](https://github.com/looker-open-source/app-data-dictionary) | app | | 14 | 2026-09-07 | v2.1.3 |
| [extension-gen-ai](https://github.com/looker-open-source/extension-gen-ai) | plugin or integration | Looker Extension GenAI - using LLMs to make exploration easier and getting dashboard insights | 94 | 2026-09-05 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://docs.cloud.google.com/looker/docs/mcp](https://docs.cloud.google.com/looker/docs/mcp)
- [https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox](https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox)
- [https://cloud.google.com/blog/products/business-intelligence/introducing-looker-mcp-server](https://cloud.google.com/blog/products/business-intelligence/introducing-looker-mcp-server)
- [https://cloud.google.com/looker/pricing](https://cloud.google.com/looker/pricing)
- [https://github.com/googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)

5 source URLs. Raw sources field, verbatim:

https://docs.cloud.google.com/looker/docs/mcp, https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox, https://cloud.google.com/blog/products/business-intelligence/introducing-looker-mcp-server, https://cloud.google.com/looker/pricing, https://github.com/googleapis/mcp-toolbox

**Notes, verbatim from the file**
No initialize POST was made on 2026-09-07: the managed server lives at each customer's own Looker instance URL (there is no shared Google host to probe) and the Toolbox route is a locally run binary, so this entry rests on documentation and repository evidence, not a probed endpoint. The managed server is in preview "for Looker (Google Cloud core) and Looker (original) instances" and "Customer-hosted (on-premise) instances are not supported for this preview". The Toolbox docs warn "Prebuilt tools are pre-1.0, so expect some tool changes between versions." The candidate row pointed only at the August 2025 launch post; the two documentation pages recorded here are the current routes. The API-call caps in the edition list (1,000 query-based calls a month on Standard) will bind an agent long before a human notices them.

**Provenance**

- **Entry id**: 06-looker

- **Source file**: 06-revops-infra.md

- **Source line**: 687

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
