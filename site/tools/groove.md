# Groove: MCP server status, API access gate and what it does

> Salesforce-native sales engagement and prospecting platform - multichannel outbound automation and activity... MCP unknown, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Groove

# Groove

[MCP unknown](../mcp/unknown.md)
[Enterprise only](../gates/enterprise-only.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [groove.co (product page now at clari.com/products/groove/)](https://groove.co (product page now at clari.com/products/groove/)) · entry id 02-groove · source 02-engagement-outbound.md line 103

**What it does**
Salesforce-native sales engagement and prospecting platform - multichannel outbound automation and activity capture - operated as a module of the Clari revenue platform since its 2023 acquisition.

**AI features, separated from automation with an AI label on it**
Vendor states "AI-powered automation and predictive insights" for journey-stage progression, AI email generation, and access to Clari's broader "Revenue AI Agents." No page found breaks down which are model-driven vs. workflow automation - vendor-stated only.

**RevOps role**
Outbound execution layer embedded in Salesforce, increasingly folded into Clari's forecasting stack - functionally overlapping with Salesloft inside the same parent company post-merger.

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (now a Clari product and Clari publishes no prices or tiers; the pricing page is a get-a-quote form and neither it nor the Groove product page mentions API access)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.clari.com/products/groove/](https://www.clari.com/products/groove/)
- [https://marketbetter.ai/blog/groove-clari-review-2026/](https://marketbetter.ai/blog/groove-clari-review-2026/)
- [https://www.getmaxiq.com/blog/clari-salesloft-merger-guide](https://www.getmaxiq.com/blog/clari-salesloft-merger-guide)
- [https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server](https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server)
- [https://www.clari.com/pricing/](https://www.clari.com/pricing/)
- [https://registry.modelcontextprotocol.io/v0/servers?search=groove](https://registry.modelcontextprotocol.io/v0/servers?search=groove)

6 source URLs. Raw sources field, verbatim:

https://www.clari.com/products/groove/, https://marketbetter.ai/blog/groove-clari-review-2026/, https://www.getmaxiq.com/blog/clari-salesloft-merger-guide, https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server, https://www.clari.com/pricing/, https://registry.modelcontextprotocol.io/v0/servers?search=groove

**Notes, verbatim from the file**
Clari (Groove's parent) launched an MCP server in 2026 described as covering "the full Clari + Salesloft platform," but no source explicitly confirmed Groove-specific actions/data are in scope, hence mcp_status: unknown rather than official. A "groove-mcp" GitHub repo exists but belongs to the unrelated Groove HQ support-ticketing product - do not cite it for this tool. Clari/Salesloft merged Dec 2025, creating direct product overlap between Groove and Salesloft worth flagging to anyone evaluating both. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.clari.com/pricing/): now a Clari product and Clari publishes no prices or tiers; the pricing page is a get-a-quote form and neither it nor the Groove product page mentions API access. 2026-09-02: re-checked, mcp_status stays unknown. The official MCP registry's only groove hit is io.usefulapi/groove-hq (remote groove-hq.usefulapi.io/mcp), a wrapper for the GrooveHQ support inbox, not Clari Groove - do not cite it. https://www.clari.com/products/groove/ has no MCP mention, and the Clari/Salesloft MCP press release describes live Salesloft and Clari pipeline, call and deal data without naming Groove. Nothing Groove-specific exists, but the parent's server may well expose Groove activity data, which is why this stays unknown rather than none-found.

**Provenance**

- **Entry id**: 02-groove

- **Source file**: 02-engagement-outbound.md

- **Source line**: 103

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
