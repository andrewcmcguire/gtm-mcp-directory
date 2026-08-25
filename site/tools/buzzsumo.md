# BuzzSumo: MCP server status, API access gate and what it does

> Researches top-performing content and social engagement by topic, tracks brand/competitor mentions, and... No MCP found, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
BuzzSumo

# BuzzSumo

[No MCP found](../mcp/none-found.md)
[Paid, self-serve](../gates/paid.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://buzzsumo.com](https://buzzsumo.com) · entry id 15-buzzsumo · source 15-community-dark-social.md line 159

**What it does**
Researches top-performing content and social engagement by topic, tracks brand/competitor mentions, and surfaces influencers, built on a large historical index of article and social-share data.

**AI features, separated from automation with an AI label on it**
"Content Ideas Generator" and "Brief Generator" synthesize headlines/keywords/SERP data into content-ideation output - this reads as research aggregation surfaced through a generation UI, not a confirmed proprietary trained model; treat the "AI" framing skeptically.

**RevOps role**
Content/engagement research and influencer-discovery layer - more content-marketing-adjacent than a pure dark-social signal tool, but relevant to GTM engineers building content-driven outbound triggers.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

none

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, quote-only - an Account API (Alerts/Projects) and a Search API exist, but both are "not tied to specific pricing tiers" and require contacting sales for arrangement/pricing, on top of already-paid subscription tiers running $199-$999/mo.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://buzzsumo.com/pricing/](https://buzzsumo.com/pricing/)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 32 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://buzzsumo.com/pricing/

**Notes, verbatim from the file**
Checked GitHub and PulseMCP for "buzzsumo" - no MCP server found under either official or community listings. API pricing being separately quote-gated on top of an already-paid subscription is a meaningfully worse access story than most tools in this file.

**Provenance**

- **Entry id**: 15-buzzsumo

- **Source file**: 15-community-dark-social.md

- **Source line**: 159

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
