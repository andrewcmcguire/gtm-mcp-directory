# Vainu: MCP server status, API access gate and what it does

> Sells a licensed database of roughly 5M Nordic registered companies with 700+ fields and around 9M... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Vainu

# Vainu

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [vainu.com](https://vainu.com) · entry id 01-vainu · source 01-data-enrichment.md line 699

**What it does**
Sells a licensed database of roughly 5M Nordic registered companies with 700+ fields and around 9M decision-maker contacts, plus scraped and classified trigger events, delivered into a CRM, an API, or Excel.

**AI features, separated from automation with an AI label on it**
A genuinely mixed picture, and the mix is the point. Real ML: event classification, where they scrape news, job postings, company sites and registries then use models to tag events into categories (M&A, funding, hiring, expansion) and resolve them to the right company entity, which is a real NLP problem. Real LLM: the "Vainu Enrichment Agent" runs user-written prompts over Vainu records at list scale to produce fit scores and summaries, which is a wrapper over their own data rather than proprietary model work. Not AI: the 700-field company record, financial statements, registry data, CRM sync and prospecting alerts, which are a licensed and scraped database with a scheduler. "AI-ready company data" is marketing for "structured data an LLM can read".

**RevOps role**
Nordic-market CRM enrichment and data-hygiene backbone with trigger-event alerting bolted on, for teams whose ICP is Finland, Sweden, Norway or Denmark.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 with PKCE, scoped to existing Vainu permissions, but NOT enabled by default. The vendor help centre says it "isn't automatically available to all users" and you must ask a CS manager or email customersuccess@vainu.io.

- **Parsed URLs**: 3 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-25 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.vainu.ai/mcp (announcement: https://www.vainu.com/blog/product-updates/vainu-mcp/; docs: https://help.vainu.app/en/articles/612044-vainu-mcp)

- [https://mcp.vainu.ai/mcp](https://mcp.vainu.ai/mcp)
- [https://www.vainu.com/blog/product-updates/vainu-mcp/](https://www.vainu.com/blog/product-updates/vainu-mcp/)
- [https://help.vainu.app/en/articles/612044-vainu-mcp](https://help.vainu.app/en/articles/612044-vainu-mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://developers.vainu.com/docs](https://developers.vainu.com/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.vainu.com/pricing/](https://www.vainu.com/pricing/)
- [https://www.vainu.com/delivery-methods/api/](https://www.vainu.com/delivery-methods/api/)
- [https://www.vainu.com/blog/product-updates/vainu-mcp/](https://www.vainu.com/blog/product-updates/vainu-mcp/)
- [https://help.vainu.app/en/articles/612044-vainu-mcp](https://help.vainu.app/en/articles/612044-vainu-mcp)
- [https://developers.vainu.com/docs](https://developers.vainu.com/docs)

5 source URLs. Raw sources field, verbatim:

https://www.vainu.com/pricing/, https://www.vainu.com/delivery-methods/api/, https://www.vainu.com/blog/product-updates/vainu-mcp/, https://help.vainu.app/en/articles/612044-vainu-mcp, https://developers.vainu.com/docs

**Notes, verbatim from the file**
Added 2026-08-25, closing a named warm lead from this file's previous sweep notes. CATEGORY CALL: this belongs in data-enrichment, not signals-intent-abm. The centre of gravity, the pricing, and the plan names ("Vainu for Prospecting", "Vainu for CRM", "Vainu for Data") are all about getting company records into a CRM and keeping them fresh, and the delivery methods (API, SFTP, CSV, CRM connector) are enrichment plumbing. The signal layer is real (AI-tagged trigger events; get_event_types_reference is a first-class MCP tool) but rides on the database. Critically it is NOT intent data in the Bombora or 6sense sense: no third-party bid stream, no content-consumption intent, no ABM ad layer, no de-anonymisation. RARE FOR THIS CATEGORY: published list prices. Prospecting from EUR 3,500/yr plus EUR 200 onboarding, CRM from EUR 4,200/yr plus EUR 750 onboarding, Data custom, all 12-month auto-renewing with 60-day cancellation notice. API is on all three tiers so it is not tier-gated, but there is no free developer tier and no card-swipe path to a production key; the route in is a trial-request form. Coverage is Nordic-first and weak outside it. Not acquired: an independent Finnish company since 2013, last confirmed outside capital a EUR 4M Round2 Capital growth investment in 2021. MCP tools: search_companies, get_company_context, query_organizations (VQL), document_search, get_event_types_reference, list_organization_fields. NOT VERIFIED: whether a trial token is self-generatable; developers.vainu.com/docs/getting-started returned thin or 404 content.

**Provenance**

- **Entry id**: 01-vainu

- **Source file**: 01-data-enrichment.md

- **Source line**: 699

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
