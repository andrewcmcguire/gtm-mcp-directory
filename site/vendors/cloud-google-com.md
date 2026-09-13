# Google: products, MCP servers and connect URLs, one vendor page

> Google (cloud.google.com): 2 products in The GTM MCP Directory, 2 with an official MCP server, 0 answering a live handshake, 11 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Google

# Google

2 products in the directory
2 official MCP servers
0 live handshakes
Data baked 2026-09-12

Vendor domain: [cloud.google.com](https://cloud.google.com) · [Public company brief (GOOG)](https://andrewcmcguire.com/companies/alphabet/) · vendor page id cloud-google-com

**The rollup**

- **Products**: 2, facts checked by hand 2026-09-07

- **Official MCP servers**: 2 of 2, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 2

- **Live handshake**: 0 of 2 answered an MCP initialize, 0 probed, no date

- **Repo local**: 0 of 2: a server you install and run yourself

- **Docs only**: 0 of 2: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 11 named across 2 measured servers, harvested 2026-09-11

- **Bench tested**: 0 of 2 here, 1 of 374 across the directory

- **Ships a CLI**: 0 of 2 official, 0 community only, 2 none found, harvested 2026-09-11

- **GitHub organisation**: [github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform), [github.com/looker-open-source](https://github.com/looker-open-source), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 2**

### [Google BigQuery](../tools/google-bigquery.md)

Google Cloud's serverless data warehouse, where many RevOps teams land CRM, product and billing data for modelling and reporting; a first-party remote MCP server exposes dataset and table metadata and SQL execution to agents.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: not probed yet, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: 8 named, harvested 2026-09-11, catalogue fixed

- **last_checked**: 2026-09-07

### [Looker](../tools/looker.md)

Google Cloud's governed BI platform (LookML semantic model, explores, Looks, dashboards, embedded analytics) that sits on top of a warehouse; two first-party MCP routes exist, a local MCP Toolbox prebuilt server and a Looker-managed remote server in preview.

[Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: not probed yet, not probed

- **Connect URL**: no connect URL recorded

- **Tools catalogued**: 3 named, harvested 2026-09-11, catalogue fixed

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 2 free to start, a solo operator gets API access without talking to anyone. 1 of 2 enterprise only, API access needs a contract.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

No job tag on any product of this vendor.

An empty list means nobody has tagged these entries, not that the tools do nothing.

**Connect URLs**

No product of this vendor records an MCP endpoint or docs URL that the probe could classify.

**Command line**

No CLI found for any product of this vendor by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**On GitHub**

### github.com/GoogleCloudPlatform

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

### github.com/looker-open-source

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

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 374 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 2 products are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
