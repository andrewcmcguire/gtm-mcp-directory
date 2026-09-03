# Lead411: MCP server status, API access gate and what it does

> A B2B contact and company database with verified emails, direct dials, and growth/intent triggers, queryable... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Lead411

# Lead411

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [lead411.com](https://lead411.com) · entry id 01-lead411 · source 01-data-enrichment.md line 559

**What it does**
A B2B contact and company database with verified emails, direct dials, and growth/intent triggers, queryable by search or by an enrichment API.

**AI features, separated from automation with an AI label on it**
Not established from public sources. The MCP exposes database search and enrichment endpoints; no generative AI capability is documented on the vendor site.

**RevOps role**
Contact and firmographic source feeding list building and CRM enrichment, positioned as a cheaper substitute for Apollo or ZoomInfo.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key via X-API-KEY header. TRANSPORT IS DISPUTED: the official registry record says SSE, PulseMCP says Streamable HTTP. Verify at connect time.

- **Parsed URLs**: 4 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-25 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.lead411.com/mcp (vendor page: https://www.lead411.com/zoominfo-mcp-server/; registry record: https://registry.modelcontextprotocol.io/v0/servers?search=lead411, namespace io.github.kunal-lead411/lead411; mirror listing: https://www.pulsemcp.com/servers/lead411)

- [https://mcp.lead411.com/mcp](https://mcp.lead411.com/mcp)
- [https://www.lead411.com/zoominfo-mcp-server/](https://www.lead411.com/zoominfo-mcp-server/)
- [https://registry.modelcontextprotocol.io/v0/servers?search=lead411](https://registry.modelcontextprotocol.io/v0/servers?search=lead411)
- [https://www.pulsemcp.com/servers/lead411](https://www.pulsemcp.com/servers/lead411)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://api.lead411.com/v1/docs/](https://api.lead411.com/v1/docs/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://registry.modelcontextprotocol.io/v0/servers?search=lead411](https://registry.modelcontextprotocol.io/v0/servers?search=lead411)
- [https://www.pulsemcp.com/servers/lead411](https://www.pulsemcp.com/servers/lead411)
- [https://www.lead411.com/](https://www.lead411.com/)
- [https://api.lead411.com/v1/docs/](https://api.lead411.com/v1/docs/)

4 source URLs. Raw sources field, verbatim:

https://registry.modelcontextprotocol.io/v0/servers?search=lead411, https://www.pulsemcp.com/servers/lead411, https://www.lead411.com/, https://api.lead411.com/v1/docs/

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. OFFICIAL STATUS, AND HOW IT WAS SETTLED, because the process is the point. The MCP registry record is published under the namespace io.github.kunal-lead411, which proves control of that GitHub account and nothing more; registry namespace verification does NOT establish that a publisher speaks for lead411.com, so on registry evidence alone this would have been scored community. It was upgraded to official only after a page on the vendor's own domain was found that names the product in the vendor's own words: https://www.lead411.com/zoominfo-mcp-server/ states "The Lead411 MCP Server allows you to take the entire Lead411 dataset of b2b contacts and companies and add it within your own tools or platform." That is first-party attestation. Treat "official" here as registry-attested plus vendor-acknowledged rather than vendor-documented, because Lead411 publishes no setup docs, no tool list and no auth instructions on its own domain, which is unusual for an official server. THE API GATE IS THE USEFUL FACT: it is explicitly one tier up. Pilot Light free trial $0 for 7 days with 50 exports; Spark $49/mo or $490/yr with API NOT included; Ignite from $150/mo or $1,500/yr WITH API included, roughly 500 successful API requests at the entry point; Blaze enterprise custom quote. So the cheapest route to the API is $150/mo, a 3x jump. Intent data requires annual billing, and the intent feed is a third-party Bombora co-op feed rather than Lead411's own. The AI Search Assistant (natural language to boolean filters) sits on Ignite and Blaze only. MCP is priced separately and sales-gated: the vendor's own page says only "Pricing is based on company size, number of customers, etc. Talk to us." The REST API uses a different scheme entirely: a JWT obtained by POSTing username and password to /v1/authenticate_user, roughly 40+ endpoints. A third-party MCPBundles proxy wrapper also exists at mcp.mcpbundles.com/bundle/lead411-bundle; that is not vendor-hosted, use the official endpoint. LIVE PROBE 2026-08-25: the registry-listed bare host https://mcp.lead411.com returns 404 at the root and at /sse, but https://mcp.lead411.com/mcp returns HTTP 401, which confirms a live auth-gated endpoint at that path. The mcp_url above is corrected to the path that actually answers; the registry record's bare host would not have connected. LIVE PROBE 2026-08-25: the registry-listed bare host https://mcp.lead411.com returns 404 at the root and at /sse, but https://mcp.lead411.com/mcp returns HTTP 401, which confirms a live auth-gated endpoint at that path. The mcp_url above is corrected to the path that actually answers; the registry record's bare host would not have connected.

**Provenance**

- **Entry id**: 01-lead411

- **Source file**: 01-data-enrichment.md

- **Source line**: 559

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
