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

Vendor: [cloud.google.com/bigquery](https://cloud.google.com/bigquery) · entry id 06-google-bigquery · source 06-revops-infra.md line 619

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

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - Google's free-tier list gives BigQuery "1 TiB of querying per month" and "10 GiB of storage per month" at no charge, and the MCP docs state "The BigQuery MCP server doesn't have its own quotas" and "there is no limit on the number of calls", with usage "still subject to the quotas enforced by the APIs called by the MCP server tools". Query and storage beyond the free tier are billed at standard BigQuery rates.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

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

- **Source line**: 619

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
