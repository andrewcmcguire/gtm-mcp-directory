# DealHub (DealHub AI): MCP server status, API access gate and what it does

> CPQ (configure-price-quote) and quote-to-revenue platform generating guided, dynamic sales proposals with... Community MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
DealHub (DealHub AI)

# DealHub (DealHub AI)

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [dealhub.io](https://dealhub.io) · entry id 13-dealhub · source 13-proposals-deals.md line 71

**What it does**
CPQ (configure-price-quote) and quote-to-revenue platform generating guided, dynamic sales proposals with real-time pricing logic, plus optional CLM and subscription-billing modules.

**AI features, separated from automation with an AI label on it**
Markets itself as "DealHub AI" with AI-assisted deal guidance; specific model/methodology claims were not independently verified in the pages reviewed.

**RevOps role**
CPQ/quote-generation engine sitting upstream of the proposal itself, feeding live pricing into whatever document tool renders the final quote.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: unknown - stdio transport run locally against the customer's own DealHub instance per the npm description; credential mechanism not read

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-03, HTTP None

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-02. On 2026-09-03 no recorded MCP URL answered.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://www.pulsemcp.com/servers/vishvick-dealhub-admin (unofficial; registry entry io.github.vishvick/dealhub-admin, npm package dealhub-admin-mcp v1.0.1)

- [https://www.pulsemcp.com/servers/vishvick-dealhub-admin](https://www.pulsemcp.com/servers/vishvick-dealhub-admin)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only in practice. DealHub operates on a custom-quote-only pricing model with no published prices across all three tiers (CPQ+, CPQ+CLM, Quote-to-Revenue); the Pricing API and Callouts API for real-time pricing sync exist but are documented as integration features of a purchased platform, not a standalone self-serve developer product.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Generate a proposal or quote](../jobs/generate-proposal-or-quote.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://dealhub.io/pricing/](https://dealhub.io/pricing/)
- [https://developers.dealhub.io/docs/introduction-to-dealhub-apis](https://developers.dealhub.io/docs/introduction-to-dealhub-apis)
- [https://dealhub.io/blog/cpq/what-you-can-do-with-dealhub-api/](https://dealhub.io/blog/cpq/what-you-can-do-with-dealhub-api/)
- [https://salestools.club/apis/dealhub](https://salestools.club/apis/dealhub)
- [https://www.pulsemcp.com/servers/vishvick-dealhub-admin](https://www.pulsemcp.com/servers/vishvick-dealhub-admin)
- [https://registry.modelcontextprotocol.io/v0/servers?search=dealhub](https://registry.modelcontextprotocol.io/v0/servers?search=dealhub)
- [https://libraries.io/npm/dealhub-admin-mcp](https://libraries.io/npm/dealhub-admin-mcp)

7 source URLs. Raw sources field, verbatim:

https://dealhub.io/pricing/, https://developers.dealhub.io/docs/introduction-to-dealhub-apis, https://dealhub.io/blog/cpq/what-you-can-do-with-dealhub-api/, https://salestools.club/apis/dealhub, https://www.pulsemcp.com/servers/vishvick-dealhub-admin, https://registry.modelcontextprotocol.io/v0/servers?search=dealhub, https://libraries.io/npm/dealhub-admin-mcp

**Notes, verbatim from the file**
The salestools.club "MCP Config" listing is the only lead found - flagged for direct verification against DealHub's own developer docs before citing it as a settled fact either way. 2026-09-02: CHANGED unknown -> community (unofficial). A stdio MCP server 'dealhub-admin-mcp' (npm v1.0.1, published 2026-04-01, description 'Model Context Protocol (MCP) server for DealHub administrators. Manage versions through Claude and AI agents.', 7 tools) is listed in the official MCP registry as io.github.vishvick/dealhub-admin and on PulseMCP, which classes it as community and names the GitHub user vishvick as maintainer. The npm license line reads 'Copyright (c) 2026 DealHub', which hints at an insider author, but the linked repo github.com/vishvick/dealhub-admin-mcp returns 404, developers.dealhub.io and dealhub.io/llms.txt make no mention of MCP, and no DealHub-branded docs exist, so it does not meet the bar for official. Admin-only scope (versions and users), not CPQ quoting.

**Provenance**

- **Entry id**: 13-dealhub

- **Source file**: 13-proposals-deals.md

- **Source line**: 71

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
