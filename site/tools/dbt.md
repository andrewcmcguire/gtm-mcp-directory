# dbt (dbt platform remote MCP): MCP server status, API access gate and what it does

> The transformation layer of the modern data stack: SQL models, tests and documentation compiled and run... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
dbt (dbt platform remote MCP)

# dbt (dbt platform remote MCP)

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07
CLI: dbt

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [getdbt.com](https://getdbt.com) · entry id 06-dbt · source 06-revops-infra.md line 642

**What it does**
The transformation layer of the modern data stack: SQL models, tests and documentation compiled and run against a warehouse, with a hosted "dbt platform" (formerly dbt Cloud) that adds scheduling, a Semantic Layer, a Catalog and a remote MCP server.

**AI features, separated from automation with an AI label on it**
dbt Copilot (AI-assisted model and test authoring) and the text_to_sql MCP tool are the AI surface; the docs state "Only text_to_sql consumes your dbt Copilot action allotment. Other MCP tools do not." The rest of the MCP is metadata, Semantic Layer queries and SQL execution.

**RevOps role**
The modelling layer between the warehouse and reverse-ETL; the MCP lets an agent read model lineage and metrics from the Semantic Layer and, with the right token, run SQL, instead of guessing at raw tables.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth (beta) or token. The docs state "OAuth lets you connect to the remote MCP server without copying API tokens into your MCP client" and limit OAuth to "Starter, Enterprise, or Enterprise+" accounts; token auth sends "Authorization: Token YOUR_DBT_ACCESS_TOKEN" (or Bearer) plus an x-dbt-prod-environment-id header, and "If you plan to use execute_sql with token-based auth, you must use a Personal Access Token (PAT)"; "Service tokens do not work for execute_sql".

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://YOUR_DBT_HOST_URL/api/ai/v1/mcp (per account, for example https://cloud.getdbt.com/api/ai/v1/mcp/; docs: https://docs.getdbt.com/docs/dbt-ai/setup-remote-mcp; open-source local server: https://github.com/dbt-labs/dbt-mcp)

- [https://YOUR_DBT_HOST_URL/api/ai/v1/mcp](https://YOUR_DBT_HOST_URL/api/ai/v1/mcp)
- [https://cloud.getdbt.com/api/ai/v1/mcp/](https://cloud.getdbt.com/api/ai/v1/mcp/)
- [https://docs.getdbt.com/docs/dbt-ai/setup-remote-mcp](https://docs.getdbt.com/docs/dbt-ai/setup-remote-mcp)
- [https://github.com/dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

120 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 105 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: dbt
- **Status**: official CLI, first party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-11

Install, as the source shows it:

```
pip install dbt
```

quoted from [https://pypi.org/project/dbt/](https://pypi.org/project/dbt/) on 2026-09-11, via pypi

Packages seen, with the version on 2026-09-11:

- [pypi: dbt 1.0.0.40.21](https://pypi.org/project/dbt/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-11.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the pricing page lists Developer as free (one seat, "3,000 successful models built per month", with no API access in its feature list), Starter at "$100 per user/month" whose feature list includes "API access", and Enterprise and Enterprise+ at custom pricing; the remote MCP's OAuth path is documented for Starter and above only.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp)

**On GitHub**

[github.com/dbt-labs](https://github.com/dbt-labs) tied to the vendor by rule 2, account website getdbt.com has the vendor's domain, confidence strong

- **Public repositories**: 120, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 6 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [dbt-core](https://github.com/dbt-labs/dbt-core) | other | dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to... | 13,790 | 2026-09-08 | v2.0.0-rc.2 |
| [docs.getdbt.com](https://github.com/dbt-labs/docs.getdbt.com) | docs or examples | The code behind docs.getdbt.com | 213 | 2026-09-08 | |
| [hub.getdbt.com-test](https://github.com/dbt-labs/hub.getdbt.com-test) | other | | 1 | 2026-09-08 | |
| [hubcap](https://github.com/dbt-labs/hubcap) | other | This app adds modules to the hubsite at hub.getdbt.com | 16 | 2026-09-08 | 0.1.0 |
| [dbt-mcp](https://github.com/dbt-labs/dbt-mcp) | MCP server | A MCP (Model Context Protocol) server for interacting with dbt. | 603 | 2026-09-08 | v2.3.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://docs.getdbt.com/docs/dbt-ai/setup-remote-mcp](https://docs.getdbt.com/docs/dbt-ai/setup-remote-mcp)
- [https://www.getdbt.com/pricing](https://www.getdbt.com/pricing)
- [https://github.com/dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp)
- [https://cloud.getdbt.com/api/ai/v1/mcp/](https://cloud.getdbt.com/api/ai/v1/mcp/)

4 source URLs. Raw sources field, verbatim:

https://docs.getdbt.com/docs/dbt-ai/setup-remote-mcp, https://www.getdbt.com/pricing, https://github.com/dbt-labs/dbt-mcp, https://cloud.getdbt.com/api/ai/v1/mcp/

**Notes, verbatim from the file**
Probed 2026-09-07: POST of an MCP initialize to https://cloud.getdbt.com/api/ai/v1/mcp/ returned HTTP 401 with an nginx "401 Authorization Required" page; the control POST to /zzz-not-a-route on cloud.getdbt.com returned 405 MethodNotAllowed from a storage front end. The two paths are handled by different layers and the 401 is specific to the API route, but the control did not return 404, so this is recorded as a live auth-gated server behind a non-standard control result. The endpoint is per account (the docs say to copy the "MCP Endpoint URL" from Account settings, Access URLs), which is why the entry carries the pattern and a representative host rather than a single canonical URL. The free Developer plan is real but its pricing card lists no API access, so a solo operator should expect the remote MCP to need Starter. 2026-09-07: https://cloud.getdbt.com/api/ai/v1/mcp/ returned 401 to an MCP initialize POST (https://cloud.getdbt.com/api/ai/v1/mcp/).

**Provenance**

- **Entry id**: 06-dbt

- **Source file**: 06-revops-infra.md

- **Source line**: 642

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
