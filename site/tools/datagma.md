# Datagma: MCP server status, API access gate and what it does

> An all-in-one B2B enrichment platform that finds work emails and verified mobile phone numbers, appends... No MCP found, Free to start. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Datagma

# Datagma

[No MCP found](../mcp/none-found.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [datagma.com](https://datagma.com) · entry id 01-datagma · source 01-data-enrichment.md line 255

**What it does**
An all-in-one B2B enrichment platform that finds work emails and verified mobile phone numbers, appends firmographic company data, and offers a Sales Navigator export/Chrome extension for pulling prospect data directly from LinkedIn.

**AI features, separated from automation with an AI label on it**
No specific AI capability documented in the sources reviewed (pricing, API, and Clay integration pages describe lookup/enrichment across multiple data sources, not an AI/ML process). Treat vendor "data intelligence" language as marketing framing over a conventional enrichment pipeline.

**RevOps role**
All-in-one enrichment layer (email/phone/company) used both standalone via API/Chrome extension and as one of several providers in a Clay waterfall (enrich person, enrich company, find email, find mobile, find profile, find employees).

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: not recorded

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

The mcp_url field is empty on this entry. 17 of 293 entries are.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://composio.dev/toolkits/datagma](https://composio.dev/toolkits/datagma)
- [https://datagma.com/pricing/](https://datagma.com/pricing/)
- [https://university.clay.com/docs/datagma-integration-overview](https://university.clay.com/docs/datagma-integration-overview)
- [https://datagma.com/api/](https://datagma.com/api/)

4 source URLs. Raw sources field, verbatim:

https://composio.dev/toolkits/datagma, https://datagma.com/pricing/, https://university.clay.com/docs/datagma-integration-overview, https://datagma.com/api/

**Notes, verbatim from the file**
No dedicated official or independently-maintained community MCP server was found on GitHub, mcp.so, glama.ai, or pulsemcp.com. Datagma only appears through Composio's generic multi-app "Tool Router," a no-code platform that wraps thousands of unrelated SaaS APIs uniformly - not counted as a genuine product-specific MCP. Datagma is a confirmed Clay enrichment provider. API access is unusually open: included on every tier including the Free plan (3 mobile lookups + 90 verified emails/month), with self-serve paid tiers at $39/$99/$249/mo (or ~20% less billed annually) and a custom Enterprise tier for larger volume. 2026-09-02: re-checked datagma.com/llms.txt (present, no MCP mention) and web search; only Composio and Runbear aggregator listings surface, no MCP server found.

**Provenance**

- **Entry id**: 01-datagma

- **Source file**: 01-data-enrichment.md

- **Source line**: 255

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
