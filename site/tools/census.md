# Census (now operates as "Fivetran Activations"): MCP server status, API access gate and what it does

> Was a standalone reverse-ETL tool for syncing warehouse data (Snowflake, BigQuery, etc.) into GTM tools like... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

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

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [getcensus.com (301-redirects to fivetran.com; docs.getcensus.com redirects to fivetran.com/docs/activations)](https://getcensus.com (301-redirects to fivetran.com; docs.getcensus.com redirects to fivetran.com/docs/activations)) · entry id 06-census · source 06-revops-infra.md line 278

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

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official (via Fivetran, not Census-specific)

mcp_url, verbatim from the file:

https://github.com/fivetran/fivetran-mcp

- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the Fivetran REST API, which now covers Activations, is available on all plans including the free trial.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp)

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: dead. Entry states the standalone product no longer operates and now lives inside Fivetran as Activations. Tags belong on Fivetran, which has sync-records-between-systems.

22 of 293 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

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

- **Source line**: 278

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
