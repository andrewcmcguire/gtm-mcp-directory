# Snowflake (Cortex AI, as GTM/RevOps warehouse layer): MCP server status, API access gate and what it does

> Cloud data warehouse that acts as the central store where GTM data (CRM, product usage, marketing, support)... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Snowflake (Cortex AI, as GTM/RevOps warehouse layer)

# Snowflake (Cortex AI, as GTM/RevOps warehouse layer)

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07
CLI: snowflake-cli

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [snowflake.com](https://snowflake.com) · entry id 06-snowflake · source 06-revops-infra.md line 382

**What it does**
Cloud data warehouse that acts as the central store where GTM data (CRM, product usage, marketing, support) gets modeled and joined; increasingly the platform other reverse-ETL tools (Hightouch, Fivetran Activations) and app tools (Retool, Superblocks) sit on top of.

**AI features, separated from automation with an AI label on it**
Genuinely substantial - Cortex Analyst (natural-language-to-SQL, GA), Cortex Search (semantic/unstructured search for RAG), Cortex AI Functions/AISQL (multimodal text/image/audio via SQL), native serverless access to Claude/Llama/Mistral model endpoints, and Cortex Agents (orchestration across structured and unstructured data). Newer, less-established additions - "Snowflake CoWork" (personal work agent) and "Snowflake CoCo" (AI coding agent) - are flagged as less proven than the Cortex core.

**RevOps role**
The warehouse/data layer everything else in a modern RevOps stack reads from or writes to - the source-of-truth GTM data model sits here, with Cortex increasingly used to let RevOps ask natural-language questions of that data directly.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Snowflake OAuth 2.0 by default, or External OAuth (Okta, Microsoft Entra ID); hardcoded PATs/tokens are explicitly discouraged. Exposes Cortex Agent, Cortex Analyst (semantic views only), Cortex Search, read-only SQL execution, and custom UDF/stored-procedure tools, capped at 50 tools per server.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp ; deprecated predecessor repo https://github.com/Snowflake-Labs/mcp

- [https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)
- [https://github.com/Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp)

**What this server exposes**

- **Tools named**: 24
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: Snowflake-Labs/mcp
- **Whose repo**: first-party
- **Catalogue shape**: the customer's own workspace, not a fixed catalogue

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

Recorded by the harvest: Cortex names tool TYPES (CORTEX_AGENT_RUN, SYSTEM_EXECUTE_SQL) that a customer binds to their own tool names in YAML

- **cortex_agent** No description was recorded with the name. evidence: in the server source · calling it reads

- **cortex_analyst** No description was recorded with the name. evidence: in the server source · calling it reads

- **cortex_search** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_object** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_or_alter_object** No description was recorded with the name. evidence: in the server source · calling it reads

- **describe_object** No description was recorded with the name. evidence: in the server source · calling it reads

- **describe_semantic_view** Describe a semantic view. evidence: in the server source · calling it reads

- **describe_semantic_view_tool** No description was recorded with the name. evidence: in the server source · calling it reads

- **drop_object** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_semantic_view_ddl** Get the DDL for a semantic view. evidence: in the server source · calling it reads

- **get_semantic_view_ddl_tool** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_objects** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_semantic_views** List all semantic views in the account, database, or schema. evidence: in the server source · calling it reads

- **list_semantic_views_tool** No description was recorded with the name. evidence: in the server source · calling it reads

- **query_semantic_view** No description was recorded with the name. evidence: in the server source · calling it reads

- **query_semantic_view_tool** No description was recorded with the name. evidence: in the server source · calling it reads

- **run_query_tool** No description was recorded with the name. evidence: in the server source · calling it reads

- **run_snowflake_query** No description was recorded with the name. evidence: in the server source · calling it reads

- **show_semantic_dimensions** Show all semantic dimensions in the account, database, or schema. evidence: in the server source · calling it reads

- **show_semantic_dimensions_tool** No description was recorded with the name. evidence: in the server source · calling it reads

- **show_semantic_metrics** Show all semantic metrics in the account, database, or schema. evidence: in the server source · calling it reads

- **show_semantic_metrics_tool** No description was recorded with the name. evidence: in the server source · calling it reads

- **write_semantic_view_query_tool** No description was recorded with the name. evidence: in the server source · calling it reads

- **write_semantic_view_tool** No description was recorded with the name. evidence: in the server source · calling it reads

119 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 106 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: snowflake-cli
- **Status**: official CLI, first party
- **Strongest evidence**: brew
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
brew install snowflake-cli
```

quoted from [https://formulae.brew.sh/formula/snowflake-cli](https://formulae.brew.sh/formula/snowflake-cli) on 2026-09-12, via brew

Packages seen, with the version on 2026-09-12:

- [pypi: snowflake-cli 3.27.0, third party](https://pypi.org/project/snowflake-cli/)
- [pypi: snowflakecli 0.4.4, third party](https://pypi.org/project/snowflakecli/)
- [pypi: snowflake-cli 3.27.0, third party](https://pypi.org/project/snowflake-cli/)
- [brew: snowflake-cli 3.27.0](https://formulae.brew.sh/formula/snowflake-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - a 30-day self-serve trial requires no payment info; Cortex AI functions are capped at roughly 10 credits/day on trial without a payment method attached.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp)

**On GitHub**

[github.com/Snowflake-Labs](https://github.com/Snowflake-Labs) tied to the vendor by rule 1, account website https://developers.snowflake.com/ has the vendor's domain, confidence strong

- **Public repositories**: 125, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 4 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [sfquickstarts](https://github.com/Snowflake-Labs/sfquickstarts) | other | Follow along with our tutorials to get you up and running with Snowflake. | 17 | 2026-09-08 | |
| [pg_lake](https://github.com/Snowflake-Labs/pg_lake) | other | pg_lake: Postgres with Iceberg and data lake access | 1,637 | 2026-09-08 | v3.5.0 |
| [coco-skills](https://github.com/Snowflake-Labs/coco-skills) | CLI | This is a curated collection of Agent Skills for Cortex Code ("CoCo") - Snowflake's CLI for building with AI. | 29 | 2026-09-08 | |
| [swt-tokyo-2026-coco](https://github.com/Snowflake-Labs/swt-tokyo-2026-coco) | other | | 0 | 2026-09-08 | |
| [sfguide-create-a-route-optimisation-and-vehicle-route-plan-simulator](https://github.com/Snowflake-Labs/sfguide-create-a-route-optimisation-and-vehicle-route-plan-simulator) | other | | 12 | 2026-09-08 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Query a data warehouse](../jobs/query-data-warehouse.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.snowflake.com/en/data-cloud/cortex/](https://www.snowflake.com/en/data-cloud/cortex/)
- [https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)
- [https://docs.snowflake.com/en/user-guide/admin-trial-account](https://docs.snowflake.com/en/user-guide/admin-trial-account)
- [https://github.com/Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp)

4 source URLs. Raw sources field, verbatim:

https://www.snowflake.com/en/data-cloud/cortex/, https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp, https://docs.snowflake.com/en/user-guide/admin-trial-account, https://github.com/Snowflake-Labs/mcp

**Notes, verbatim from the file**
The community github.com/Snowflake-Labs/mcp repo is explicitly deprecated - its README states "This project is deprecated and no longer maintained. Please migrate to the official Snowflake MCP Server," linking to the docs.snowflake.com URL above. Do not cite Snowflake-Labs/mcp as current; the officially-supported, Snowflake-managed MCP server is the one at docs.snowflake.com (GA, but not supported in government regions). 2026-09-07: the vendor now marks this repo DEPRECATED - the README of https://github.com/Snowflake-Labs/mcp reads "[DEPRECATED] ... migrate to the official Snowflake MCP Server" and points at docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp, which is the replacement and is already the primary mcp_url recorded here. The repo is still a real server (mcp_server_snowflake/ with cortex_services, object_manager and query_manager tools, PyPI snowflake-labs-mcp) and is recorded because the successor is an in-account managed server with no public repo and no public endpoint, so the deprecated repo is the only harvestable artifact. mcp_status left at official on the strength of the current vendor docs page, not the deprecated repo.

**Provenance**

- **Entry id**: 06-snowflake

- **Source file**: 06-revops-infra.md

- **Source line**: 382

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
