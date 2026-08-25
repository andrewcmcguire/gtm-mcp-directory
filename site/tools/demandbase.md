# Demandbase (Demandbase One): MCP server status, API access gate and what it does

> Identifies and scores in-market B2B accounts by combining IP/website deanonymization, a global... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Demandbase (Demandbase One)

# Demandbase (Demandbase One)

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.demandbase.com](https://www.demandbase.com) · entry id 05-demandbase · source 05-signals-intent-abm.md line 38

**What it does**
Identifies and scores in-market B2B accounts by combining IP/website deanonymization, a global firmographic/technographic database, and intent-signal ingestion, rolling this into "Buying Group" and account-level engagement data inside a customer's own tenant.

**AI features, separated from automation with an AI label on it**
Vendor markets "Demandbase AI" for buying-group prioritization ("most likely to convert") but public pages don't disclose whether this is a distinct trained model or a scored aggregation of intent+firmographic data - treat with skepticism. The MCP's natural-language query layer is an interface, not a new signal.

**RevOps role**
Enterprise ABM platform - account intelligence and buying-group orchestration feeding CRM, ad platforms, and sales engagement tools.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - the account-team-gated support article that likely covers this returned HTTP 403 and could not be read; docs confirm the MCP is read-only against a customer's own tenant.

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developer.demandbase.com/docs/mcp ; https://learn.demandbase.com/setting-up-and-using-demandbase-mcp

- [https://developer.demandbase.com/docs/mcp](https://developer.demandbase.com/docs/mcp)
- [https://learn.demandbase.com/setting-up-and-using-demandbase-mcp](https://learn.demandbase.com/setting-up-and-using-demandbase-mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://developer.demandbase.com/docs/mcp](https://developer.demandbase.com/docs/mcp)
- [https://learn.demandbase.com/setting-up-and-using-demandbase-mcp](https://learn.demandbase.com/setting-up-and-using-demandbase-mcp)
- [https://developer.demandbase.com/docs/instructions](https://developer.demandbase.com/docs/instructions)
- [https://www.demandbase.com/products/data/api-integration/](https://www.demandbase.com/products/data/api-integration/)
- [https://support.demandbase.com/hc/en-us/articles/38999526296603-Generate-and-Manage-API-Key-Sets](https://support.demandbase.com/hc/en-us/articles/38999526296603-Generate-and-Manage-API-Key-Sets)
- [https://www.demandbase.com/pricing/](https://www.demandbase.com/pricing/)

6 source URLs. Raw sources field, verbatim:

https://developer.demandbase.com/docs/mcp, https://learn.demandbase.com/setting-up-and-using-demandbase-mcp, https://developer.demandbase.com/docs/instructions, https://www.demandbase.com/products/data/api-integration/, https://support.demandbase.com/hc/en-us/articles/38999526296603-Generate-and-Manage-API-Key-Sets, https://www.demandbase.com/pricing/

**Notes, verbatim from the file**
B2B API and Export API require the customer's account team to enable them even on an existing paid contract - not bundled by default. MCP requires an existing Demandbase One tenant, so it isn't independently usable.

**Provenance**

- **Entry id**: 05-demandbase

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 38

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
