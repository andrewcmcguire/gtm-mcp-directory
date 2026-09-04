# Bombora (Company Surge): MCP server status, API access gate and what it does

> Detects which companies are actively researching specific B2B topics by aggregating content-consumption data... No MCP found, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Bombora (Company Surge)

# Bombora (Company Surge)

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://bombora.com](https://bombora.com) · entry id 05-bombora · source 05-signals-intent-abm.md line 63

**What it does**
Detects which companies are actively researching specific B2B topics by aggregating content-consumption data (article reads, downloads) across a co-op of 5,000+ B2B publisher sites, then measures spikes in a company's topic-research volume relative to its own baseline.

**AI features, separated from automation with an AI label on it**
Vendor states it uses BERT-based ML to map content to topics/intent semantically rather than keyword matching, and holds patents on measuring intent-change via ML - one of the more credible "real ML" claims in the category, though it's still fundamentally a scored data-aggregation product, not an agent.

**RevOps role**
Upstream intent-data supplier - consumed as a feed inside other ABM/intent platforms (6sense, Demandbase, Warmly all integrate it) rather than used as a standalone tool.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

none

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://bombora.com/products/company-surge/](https://bombora.com/products/company-surge/)
- [https://pipeline.zoominfo.com/sales/bombora-pricing](https://pipeline.zoominfo.com/sales/bombora-pricing)
- [https://www.docket.io/resources/research/bombora-pricing](https://www.docket.io/resources/research/bombora-pricing)
- [https://www.g2.com/products/bombora-company-surge/pricing](https://www.g2.com/products/bombora-company-surge/pricing)
- [https://marketbetter.ai/blog/bombora-pricing-breakdown-2026/](https://marketbetter.ai/blog/bombora-pricing-breakdown-2026/)

5 source URLs. Raw sources field, verbatim:

https://bombora.com/products/company-surge/, https://pipeline.zoominfo.com/sales/bombora-pricing, https://www.docket.io/resources/research/bombora-pricing, https://www.g2.com/products/bombora-company-surge/pricing, https://marketbetter.ai/blog/bombora-pricing-breakdown-2026/

**Notes, verbatim from the file**
Searched "Bombora MCP server/github" plus mcp.so/glama.ai/pulsemcp.com - nothing found. Sales-led, custom-quote pricing; third-party writeups peg entry contracts around $25-30K/yr with API access as a $5-20K/yr add-on. Company-level only, no individual researcher identification, weekly refresh. 2026-09-02: re-checked bombora.com/llms.txt (404) and web search; the only hit, 'bombora-wp-mcp' on apis.io, resolves to WordPress MCP tooling unrelated to Bombora the intent vendor. No MCP server found.

**Provenance**

- **Entry id**: 05-bombora

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 63

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
