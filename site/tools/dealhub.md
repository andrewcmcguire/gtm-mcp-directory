# DealHub (DealHub AI): MCP server status, API access gate and what it does

> CPQ (configure-price-quote) and quote-to-revenue platform generating guided, dynamic sales proposals with... MCP unknown, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
DealHub (DealHub AI)

# DealHub (DealHub AI)

[MCP unknown](../mcp/unknown.md)
[Enterprise only](../gates/enterprise-only.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [dealhub.io](https://dealhub.io) · entry id 13-dealhub · source 13-proposals-deals.md line 71

**What it does**
CPQ (configure-price-quote) and quote-to-revenue platform generating guided, dynamic sales proposals with real-time pricing logic, plus optional CLM and subscription-billing modules.

**AI features, separated from automation with an AI label on it**
Markets itself as "DealHub AI" with AI-assisted deal guidance; specific model/methodology claims were not independently verified in the pages reviewed.

**RevOps role**
CPQ/quote-generation engine sitting upstream of the proposal itself, feeding live pricing into whatever document tool renders the final quote.

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: unknown

- **Parsed URLs**: 0 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

a third-party directory (salestools.club/apis/dealhub) lists "DealHub API Documentation & MCP Config," implying some MCP configuration exists, but no official DealHub-branded MCP docs page or GitHub repo could be independently located to confirm - logged as unknown rather than community/official pending direct verification.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only in practice. DealHub operates on a custom-quote-only pricing model with no published prices across all three tiers (CPQ+, CPQ+CLM, Quote-to-Revenue); the Pricing API and Callouts API for real-time pricing sync exist but are documented as integration features of a purchased platform, not a standalone self-serve developer product.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Generate a proposal or quote](../jobs/generate-proposal-or-quote.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://dealhub.io/pricing/](https://dealhub.io/pricing/)
- [https://developers.dealhub.io/docs/introduction-to-dealhub-apis](https://developers.dealhub.io/docs/introduction-to-dealhub-apis)
- [https://dealhub.io/blog/cpq/what-you-can-do-with-dealhub-api/](https://dealhub.io/blog/cpq/what-you-can-do-with-dealhub-api/)
- [https://salestools.club/apis/dealhub](https://salestools.club/apis/dealhub)

4 source URLs. Raw sources field, verbatim:

https://dealhub.io/pricing/, https://developers.dealhub.io/docs/introduction-to-dealhub-apis, https://dealhub.io/blog/cpq/what-you-can-do-with-dealhub-api/, https://salestools.club/apis/dealhub

**Notes, verbatim from the file**
The salestools.club "MCP Config" listing is the only lead found - flagged for direct verification against DealHub's own developer docs before citing it as a settled fact either way.

**Provenance**

- **Entry id**: 13-dealhub

- **Source file**: 13-proposals-deals.md

- **Source line**: 71

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
