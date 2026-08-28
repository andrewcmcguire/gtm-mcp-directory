# Crustdata: MCP server status, API access gate and what it does

> A real-time API for company and person firmographic/growth data (headcount trends, funding, tech stack, web... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Crustdata

# Crustdata

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [crustdata.com](https://crustdata.com) · entry id 01-crustdata · source 01-data-enrichment.md line 445

**What it does**
A real-time API for company and person firmographic/growth data (headcount trends, funding, tech stack, web traffic, social signals), positioned as infrastructure for time-sensitive GTM triggers and agent-built prospecting workflows.

**AI features, separated from automation with an AI label on it**
Markets itself as built "for AI agents" with Claude Code example workflows; the underlying capability is real-time data aggregation and API delivery, not a proprietary AI model - "AI-native" mostly describes agent-friendly API/MCP design, not novel enrichment intelligence.

**RevOps role**
Real-time firmographic/trigger-signal layer for outbound (funding events, headcount changes, tech-stack shifts), used alongside or as an alternative to Clay/PDL.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://crustdata.com/ (MCP referenced directly on the vendor homepage: "drop the whole graph into your agent with the MCP, in one line"; a dedicated MCP docs sub-page was not locatable under docs.crustdata.com)

- [https://crustdata.com/](https://crustdata.com/)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (free sandbox API key issued self-serve at signup, no credit card; paid usage is credit-based on top)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Crustdata

- **Category**: [Signals & Intent](../categories/signals-intent-abm.md)

- **MCP status there**: Official MCP

- **Gate there**: Paid, self-serve

- **Source**: 05-signals-intent-abm.md line 509

- **Canonical page**: [Crustdata](../tools/crustdata.md)

What that listing says it does: Aggregates real-time company and people data (250+ data points per company from 15+ sources - funding, headcount, web signals, social, reviews) plus a "Watcher API" for near-real-time hiring/funding/event alerts, covering 60M companies and 1B+ people.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://crustdata.com/](https://crustdata.com/)
- [https://docs.crustdata.com/general/pricing](https://docs.crustdata.com/general/pricing)
- [https://crustdata.com/blog/b2b-prospecting-workflow-claude-code](https://crustdata.com/blog/b2b-prospecting-workflow-claude-code)

3 source URLs. Raw sources field, verbatim:

https://crustdata.com/, https://docs.crustdata.com/general/pricing, https://crustdata.com/blog/b2b-prospecting-workflow-claude-code

**Notes, verbatim from the file**
MCP existence is confirmed on the vendor's own homepage, but the exact MCP-specific auth flow and a dedicated MCP docs URL could not be pinned down in this pass - mcp_auth and the precise api_gate are marked unknown rather than guessed. Web search/fetch and basic search+enrichment endpoints appear self-serve (free sandbox key referenced); live real-time Person and Company endpoints are explicitly plan-gated per docs.crustdata.com/general/pricing, with no full public price list and credits that expire after 6 months (up to 7 credits per enriched person profile). [api_gate 2026-08-25] Reclassified unknown -> free from the vendor's own page (https://crustdata.com/): free sandbox API key issued self-serve at signup, no credit card; paid usage is credit-based on top.

**Provenance**

- **Entry id**: 01-crustdata

- **Source file**: 01-data-enrichment.md

- **Source line**: 445

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
