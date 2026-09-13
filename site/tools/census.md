# Census (now operates as "Fivetran Activations"): MCP server status, API access gate and what it does

> Was a standalone reverse-ETL tool for syncing warehouse data (Snowflake, BigQuery, etc.) into GTM tools like... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Census (now operates as "Fivetran Activations")

# Census (now operates as "Fivetran Activations")

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [getcensus.com (301-redirects to fivetran.com; docs.getcensus.com redirects to fivetran.com/docs/activations)](https://getcensus.com (301-redirects to fivetran.com; docs.getcensus.com redirects to fivetran.com/docs/activations)) · entry id 06-census · source 06-revops-infra.md line 289

**What it does**
Was a standalone reverse-ETL tool for syncing warehouse data (Snowflake, BigQuery, etc.) into GTM tools like Salesforce/HubSpot without code; the product now lives inside Fivetran as "Activations," same function.

**AI features, separated from automation with an AI label on it**
No standalone Census AI features exist anymore - the product no longer operates independently. See the Fivetran entry for the current AI/MCP surface.

**RevOps role**
Reverse-ETL layer - pushes warehouse-modeled data (scores, segments, enrichment) into CRM/marketing tools; now folded into Fivetran's broader EL(T)-plus-activation platform rather than a separate best-of-breed vendor.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: API key + secret via env vars (FIVETRAN_API_KEY, FIVETRAN_API_SECRET).

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official (via Fivetran, not Census-specific)

mcp_url, verbatim from the file:

https://github.com/fivetran/fivetran-mcp

- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

**What this server exposes**

- **Tools named**: 2
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: fivetran/fivetran-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **get_schema** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_endpoints** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 380 entries that record an official or community MCP server carry a harvested tool list. The other 261 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the Fivetran REST API, which now covers Activations, is available on all plans including the free trial.

**API documentation**

No documentation URL recorded.

528 of 784 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

**On GitHub**

No GitHub organisation could be tied to getcensus.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

6 candidate accounts seen and rejected by the evidence rules: fivetran, CENSUS, censusreporter, census-instrumentation, uscensusbureau. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: dead. Entry states the standalone product no longer operates and now lives inside Fivetran as Activations. Tags belong on Fivetran, which has sync-records-between-systems.

513 of 784 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.getcensus.com/](https://www.getcensus.com/)
- [https://docs.getcensus.com/](https://docs.getcensus.com/)
- [https://fivetran.com/docs/activations](https://fivetran.com/docs/activations)
- (confirmed 301 redirect to fivetran.com)
- (confirmed redirect to fivetran.com/docs/activations)

3 source URLs. Raw sources field, verbatim:

https://www.getcensus.com/ (confirmed 301 redirect to fivetran.com), https://docs.getcensus.com/ (confirmed redirect to fivetran.com/docs/activations), https://fivetran.com/docs/activations

**Notes, verbatim from the file**
This is worth flagging plainly - anyone still citing "Census" as an independent reverse-ETL vendor is out of date. getcensus.com, www.getcensus.com, and docs.getcensus.com all redirect to Fivetran domains, and fivetran.com/docs/activations describes exactly Census's old reverse-ETL product. No dated press release confirming the acquisition/merger was found (Fivetran's own newsroom listing doesn't show one) - the exact date is unknown, the redirect behavior is what's confirmed.

**Provenance**

- **Entry id**: 06-census

- **Source file**: 06-revops-infra.md

- **Source line**: 289

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
