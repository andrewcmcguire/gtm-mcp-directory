# Google BigQuery: MCP server status, API access gate and what it does

> Google Cloud's serverless data warehouse, where many RevOps teams land CRM, product and billing data for... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Google BigQuery

# Google BigQuery

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [cloud.google.com/bigquery](https://cloud.google.com/bigquery) · entry id 06-google-bigquery · source 06-revops-infra.md line 621

**What it does**
Google Cloud's serverless data warehouse, where many RevOps teams land CRM, product and billing data for modelling and reporting; a first-party remote MCP server exposes dataset and table metadata and SQL execution to agents.

**AI features, separated from automation with an AI label on it**
The warehouse is infrastructure; Google's AI layer (Gemini in BigQuery, data insights) sits alongside it and was not assessed here. The MCP server is connectivity: execute_sql, execute_sql_readonly, list_dataset_ids, list_table_ids, get_dataset_info and get_table_info per the vendor docs.

**RevOps role**
The warehouse under a RevOps stack; the MCP lets an agent read schema and run SQL against the same tables dbt, Hightouch and Census operate on, with IAM deciding what it can see.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The docs state the server uses the "OAuth 2.0 protocol with IAM for authentication and authorization", supports "all Google Cloud identities" and requires the scope https://www.googleapis.com/auth/bigquery; the client sends a Google access token as a Bearer header.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://bigquery.googleapis.com/mcp (docs: https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp)

- [https://bigquery.googleapis.com/mcp](https://bigquery.googleapis.com/mcp)
- [https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp](https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp)

**What this server exposes**

- **Tools named**: 8
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **cancel_job** Cancel a running BigQuery job. Use this tool to cancel a query job that is currently executing (i.e. returned `job_complete: false` with a `job_id` from `execute_sql` or `execute_sql_readonly`). Specify the `job_id` to abort. evidence: answered tools/list · calling it reads · required: jobId, projectId

- **execute_sql** Run a SQL query in the project and return the result. Prefer the `execute_sql_readonly` tool if possible. This tool can execute any query that bigquery supports including: * SQL Queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, e evidence: answered tools/list · calling it reads · required: projectId, query

- **execute_sql_readonly** Run a read-only SQL query in the project and return the result. Prefer this tool over `execute_sql` if possible. This tool is restricted to only `SELECT` statements. `INSERT`, `UPDATE`, and `DELETE` statements and stored procedures aren't evidence: answered tools/list · calling it reads · required: projectId, query

- **get_dataset_info** Get metadata information about a BigQuery dataset or BigLake namespace. evidence: answered tools/list · calling it reads · required: datasetId, projectId

- **get_query_results** Get the results of a BigQuery SQL query job. Use this tool ONLY when: 1. A previous `execute_sql` or `execute_sql_readonly` call returned `job_complete: false` with a `job_id` (poll with this tool until `job_complete: true`), OR 2. You evidence: answered tools/list · calling it reads · required: jobId, projectId

- **get_table_info** Get metadata information about a BigQuery table or BigLake table. evidence: answered tools/list · calling it reads · required: datasetId, projectId, tableId

- **list_dataset_ids** List BigQuery dataset IDs and BigLake namespaces in a Google Cloud project. Supports pagination. Use `page_size` to limit results and `page_token` to retrieve next page. evidence: answered tools/list · calling it reads · required: projectId

- **list_table_ids** List table ids in a BigQuery dataset or BigLake namespace. Supports pagination. Use `page_size` to limit results and `page_token` to retrieve next page. evidence: answered tools/list · calling it reads · required: datasetId, projectId

119 of the 471 entries that record an official or community MCP server carry a harvested tool list. The other 352 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - Google's free-tier list gives BigQuery "1 TiB of querying per month" and "10 GiB of storage per month" at no charge, and the MCP docs state "The BigQuery MCP server doesn't have its own quotas" and "there is no limit on the number of calls", with usage "still subject to the quotas enforced by the APIs called by the MCP server tools". Query and storage beyond the free tier are billed at standard BigQuery rates.

**API documentation**

No documentation URL recorded.

629 of 982 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform) tied to the vendor by rule 3, account website https://cloud.google.com has the vendor's domain, confidence strong

- **Public repositories**: 150, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 4 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [DataflowTemplates](https://github.com/GoogleCloudPlatform/DataflowTemplates) | other | Cloud Dataflow Google-provided templates for solving in-Cloud data tasks | 1,311 | 2026-09-08 | 2026-09-01-00_RC00 |
| [composer-airflow](https://github.com/GoogleCloudPlatform/composer-airflow) | other | | 38 | 2026-09-08 | |
| [spring-cloud-gcp](https://github.com/GoogleCloudPlatform/spring-cloud-gcp) | other | New home for Spring Cloud GCP development starting with version 2.0. | 551 | 2026-09-08 | v8.1.1 |
| [PerfKitBenchmarker](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker) | other | PerfKit Benchmarker (PKB) contains a set of benchmarks to measure and compare cloud offerings. The benchmarks use... | 2,010 | 2026-09-08 | v1.15.1 |
| [opentelemetry-operations-collector](https://github.com/GoogleCloudPlatform/opentelemetry-operations-collector) | other | | 83 | 2026-09-08 | v0.159.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

711 of 982 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp](https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp)
- [https://docs.cloud.google.com/free/docs/free-cloud-features](https://docs.cloud.google.com/free/docs/free-cloud-features)
- [https://cloud.google.com/bigquery/pricing](https://cloud.google.com/bigquery/pricing)
- [https://bigquery.googleapis.com/mcp](https://bigquery.googleapis.com/mcp)

4 source URLs. Raw sources field, verbatim:

https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp, https://docs.cloud.google.com/free/docs/free-cloud-features, https://cloud.google.com/bigquery/pricing, https://bigquery.googleapis.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://bigquery.googleapis.com/mcp with no token returned HTTP 200 with a JSON-RPC result, serverInfo name "StatelessServer" version "ESF" (protocolVersion 2025-03-26); the control POST to /zzz-not-a-route returned 404. Initialize is open and IAM is enforced per tool call. Google's cloud documentation moved from cloud.google.com to docs.cloud.google.com with 301 redirects on this date; the entry records the destination URLs. Snowflake, the other warehouse in this file, is the natural comparison: both now ship a first-party MCP, and BigQuery's is reachable on a free-tier project with no contract. 2026-09-07: https://bigquery.googleapis.com/mcp returned 200 with a JSON-RPC initialize result to an MCP initialize POST (https://bigquery.googleapis.com/mcp).

**Provenance**

- **Entry id**: 06-google-bigquery

- **Source file**: 06-revops-infra.md

- **Source line**: 621

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
