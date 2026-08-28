# G2 Buyer Intent: MCP server status, API access gate and what it does

> Surfaces which companies are researching your product and your competitors on G2's review marketplace, plus... Official MCP, Enterprise only. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
G2 Buyer Intent

# G2 Buyer Intent

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [g2.com](https://g2.com) · entry id 05-g2-buyer-intent · source 05-signals-intent-abm.md line 615

**What it does**
Surfaces which companies are researching your product and your competitors on G2's review marketplace, plus the review and category data behind those signals.

**AI features, separated from automation with an AI label on it**
Intent scoring 0-100 derived from on-site research behaviour, competitive evaluation pattern detection, and review-derived market intelligence including switching patterns and NPS. The scoring is proprietary and unverified externally; the underlying data is behavioural telemetry, not AI.

**RevOps role**
Third-party review-site intent source, complementary to Bombora's co-op and 6sense's own network, and a common trigger for ABM plays and competitive-displacement outreach.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 Authorization Code with PKCE. You register an OAuth app in the G2 Developer Dashboard at https://my.g2.com/developers to get a client_id and client_secret and configure a localhost callback redirect URI. Scopes include openid, profile, buyer_intent.read, products.read, products.reviews.read, vendors.read plus research-board scopes. Cross-application token introspection must be enabled on the OAuth app or token validation against the MCP server fails.

- **Parsed URLs**: 3 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-25 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.g2.com/mcp (docs: https://documentation.g2.com/docs/g2-mcp-server; product page: https://sell.g2.com/g2-mcp)

- [https://mcp.g2.com/mcp](https://mcp.g2.com/mcp)
- [https://documentation.g2.com/docs/g2-mcp-server](https://documentation.g2.com/docs/g2-mcp-server)
- [https://sell.g2.com/g2-mcp](https://sell.g2.com/g2-mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

[https://documentation.g2.com/](https://documentation.g2.com/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://documentation.g2.com/docs/g2-mcp-server](https://documentation.g2.com/docs/g2-mcp-server)
- [https://sell.g2.com/g2-mcp](https://sell.g2.com/g2-mcp)
- [https://data.g2.com/api/docs](https://data.g2.com/api/docs)
- [https://partner.g2.com/developer](https://partner.g2.com/developer)
- [https://partnerhub.g2.com/](https://partnerhub.g2.com/)
- [https://sell.g2.com/resources/webinars/ai-agents-mcp-and-the-new-intent-stack](https://sell.g2.com/resources/webinars/ai-agents-mcp-and-the-new-intent-stack)

6 source URLs. Raw sources field, verbatim:

https://documentation.g2.com/docs/g2-mcp-server, https://sell.g2.com/g2-mcp, https://data.g2.com/api/docs, https://partner.g2.com/developer, https://partnerhub.g2.com/, https://sell.g2.com/resources/webinars/ai-agents-mcp-and-the-new-intent-stack

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep, closing the most glaring gap in this file: the directory covered Bombora's co-op and 6sense's own network but not the third-party intent source B2B software sellers cite most often. 23 tools documented, spanning product browsing, vendor management, review retrieval, buyer intent, competitive intelligence, research board management and category exploration. Named tools include browse_buyer_intent, browse_competitive_intelligence, list_standard_product_reviews, list_market_intelligence_product_reviews. api_gate is enterprise-only in practice: G2's own FAQ states "the data returned is limited by your current G2 subscription," and the MCP docs add that "additional G2 entitlements may be required for buyer intent data." Buyer Intent is a paid seller product with no published price and no self-serve path. G2 does operate a developer portal with a sandbox, so a developer can explore the shape of the API without live intent data, which is a genuinely useful middle state worth naming. G2 also lists partner surfaces where the MCP is pre-wired: Claude, ChatGPT, HubSpot (requires Breeze Agents access), Gong, AirOps, Profound, plus a beta directly inside my.G2. TWO G2 DOC URLS 404: sell.g2.com/pricing and documentation.g2.com/docs/g2-api-getting-started; the working entry points are the two given above.

**Provenance**

- **Entry id**: 05-g2-buyer-intent

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 615

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
