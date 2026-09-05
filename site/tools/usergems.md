# UserGems: MCP server status, API access gate and what it does

> Tracks job changes of known contacts (past customers/champions moving to new companies) plus 30+ other native... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
UserGems

# UserGems

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.usergems.com](https://www.usergems.com) · entry id 05-usergems · source 05-signals-intent-abm.md line 87

**What it does**
Tracks job changes of known contacts (past customers/champions moving to new companies) plus 30+ other native signals (new hires, promotions, funding, website visits, M&A) sourced from LinkedIn-style data providers and a customer's own CRM history, to surface warm outbound opportunities.

**AI features, separated from automation with an AI label on it**
Core job-change/hire tracking is rules-based data monitoring and matching, not ML. A newer "Research Agent" for open-ended custom signal discovery is the more genuinely AI-native piece (LLM-agent layer); be skeptical of "AI-powered" framing applied to the core product.

**RevOps role**
Champion/relationship-tracking layer triggering warm outbound when known contacts change jobs, feeding sales engagement tools and CRM.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - connects inside Claude/ChatGPT per the product page, but the exact auth mechanism (OAuth vs. API key) isn't disclosed publicly.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.usergems.com/product/mcp](https://www.usergems.com/product/mcp)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.usergems.com/product/mcp

- [https://www.usergems.com/product/mcp](https://www.usergems.com/product/mcp)

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
- [Track job changes](../jobs/track-job-changes.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.usergems.com/product/mcp](https://www.usergems.com/product/mcp)
- [https://www.usergems.com/](https://www.usergems.com/)
- [https://www.vendr.com/marketplace/usergems](https://www.vendr.com/marketplace/usergems)
- [https://www.keepsync.io/post/usergems-pricing-worth-30k-year-cheaper-alternatives](https://www.keepsync.io/post/usergems-pricing-worth-30k-year-cheaper-alternatives)
- [https://salesmotion.io/blog/usergems-pricing](https://salesmotion.io/blog/usergems-pricing)

5 source URLs. Raw sources field, verbatim:

https://www.usergems.com/product/mcp, https://www.usergems.com/, https://www.vendr.com/marketplace/usergems, https://www.keepsync.io/post/usergems-pricing-worth-30k-year-cheaper-alternatives, https://salesmotion.io/blog/usergems-pricing

**Notes, verbatim from the file**
No public pricing page - third-party trackers (Vendr, Keepsync, Salesmotion) report tiers from ~$33K/yr to ~$120K/yr plus a $3-10K implementation fee; treat as market-observed, not vendor-confirmed. No self-serve signup found.

**Provenance**

- **Entry id**: 05-usergems

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 87

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
