# Fivetran: MCP server status, API access gate and what it does

> Managed ELT pipeline platform; for GTM purposes, the relevant piece is its... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Fivetran

# Fivetran

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24
CLI: fivetran-cli (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [fivetran.com](https://fivetran.com) · entry id 06-fivetran · source 06-revops-infra.md line 357

**What it does**
Managed ELT pipeline platform; for GTM purposes, the relevant piece is its Salesforce/HubSpot/Marketo/Outreach/Salesloft/Gong/Zendesk connectors that land CRM and GTM-tool data in a warehouse, plus (post-Census) its "Activations" reverse-ETL product for pushing data back out to those same tools.

**AI features, separated from automation with an AI label on it**
Mostly plain data pipeline - the AI positioning is largely about being "AI-ready" infrastructure for downstream agents rather than AI inside the product itself. The one genuinely agentic piece is the official MCP server, which lets an AI assistant query/manage connections conversationally - that is real, not just marketing.

**RevOps role**
Core data-plumbing layer of a RevOps stack - lands CRM/marketing/sales-engagement data into the warehouse and, via Activations, pushes it back out so it can be modeled and reused across GTM tools.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: API key + API secret via env vars, generated from the Fivetran dashboard. Scoped permission tiers (read / read-write / read-write-delete) with a configurable disallowed-actions carve-out; confirms with the user before write/delete operations.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/fivetran/fivetran-mcp

- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

**What this server exposes**

- **Tools named**: 2
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: fivetran/fivetran-mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **get_schema** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_endpoints** No description was recorded with the name. evidence: in the server source · calling it reads

119 of the 359 entries that record an official or community MCP server carry a harvested tool list. The other 240 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: fivetran-cli
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
pip install fivetran-cli
```

quoted from [https://pypi.org/project/fivetran-cli/](https://pypi.org/project/fivetran-cli/) on 2026-09-12, via pypi, a third party source

Packages seen, with the version on 2026-09-12:

- [pypi: fivetran-cli 0.1.13, third party](https://pypi.org/project/fivetran-cli/)
- [pypi: fivetran-cli 0.1.13, third party](https://pypi.org/project/fivetran-cli/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the REST API is available on all Fivetran plans including the free trial; the Free plan is self-serve (500K MAR/mo for connections, 3,500 MAR for activations, 5,000 MMR for transformations, no payment info required).

**API documentation**

No documentation URL recorded.

510 of 739 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

**On GitHub**

[github.com/fivetran](https://github.com/fivetran) tied to the vendor by rule 1, account website https://fivetran.com has the vendor's domain, confidence strong

- **Public repositories**: 144, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [fivetran_sdk_tools](https://github.com/fivetran/fivetran_sdk_tools) | SDK | Local testing tools for Partner SDK and Connector SDK | 0 | 2026-09-08 | 2.26.0908.001 |
| [great_expectations](https://github.com/fivetran/great_expectations) | other | Always know what to expect from your data. | 11,776 | 2026-09-08 | 1.22.0 |
| [community_connectors](https://github.com/fivetran/community_connectors) | SDK | Fivetran Connector SDK Connectors Catalog | 85 | 2026-09-08 | |
| [connector_sdk](https://github.com/fivetran/connector_sdk) | SDK | Build custom connectors on Fivetran's platform | 133 | 2026-09-07 | |
| [dbt_openai](https://github.com/fivetran/dbt_openai) | other | | 0 | 2026-09-04 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 739 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.fivetran.com/](https://www.fivetran.com/)
- [https://www.fivetran.com/pricing](https://www.fivetran.com/pricing)
- [https://fivetran.com/docs/activations](https://fivetran.com/docs/activations)
- [https://fivetran.com/docs/connectors/applications](https://fivetran.com/docs/connectors/applications)
- [https://fivetran.com/docs/rest-api](https://fivetran.com/docs/rest-api)
- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

6 source URLs. Raw sources field, verbatim:

https://www.fivetran.com/, https://www.fivetran.com/pricing, https://fivetran.com/docs/activations, https://fivetran.com/docs/connectors/applications, https://fivetran.com/docs/rest-api, https://github.com/fivetran/fivetran-mcp

**Notes, verbatim from the file**
Confirmed GTM-relevant connectors include Salesforce, HubSpot, Pipedrive, Copper, Close, Marketo, Pardot, Braze, Klaviyo, Outreach, Salesloft, Apollo, Reply.io, Zendesk, Intercom, Freshdesk, Help Scout, LinkedIn Ad Analytics, Google Ads, and Gong. See the Census entry above - that product now lives inside Fivetran as Activations.

**Provenance**

- **Entry id**: 06-fivetran

- **Source file**: 06-revops-infra.md

- **Source line**: 357

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
