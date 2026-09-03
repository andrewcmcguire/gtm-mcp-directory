# ZoomInfo: MCP server status, API access gate and what it does

> A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web... Official MCP, Free to start. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
ZoomInfo

# ZoomInfo

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [zoominfo.com](https://zoominfo.com) · entry id 01-zoominfo · source 01-data-enrichment.md line 7

**What it does**
A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human researchers, used for prospecting, account research, and lead enrichment.

**AI features, separated from automation with an AI label on it**
ML is used for record matching/deduplication and lead scoring; "Copilot" is an AI assistant that summarizes accounts, prioritizes leads, and drafts outreach emails on top of the database. The core value (the data itself) is not AI-generated - the AI layer is a research/writing assistant bolted onto a traditional data product.

**RevOps role**
Upstream contact/company data source feeding CRM, enrichment, and outbound tooling; typically the "system of record" for firmographic/contact data in larger RevOps stacks

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth for user-level access, or client credentials for service accounts; no API keys stored by the client. A local mcp-remote bridge is used for stdio clients.

- **Parsed URLs**: 3 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-25 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.zoominfo.com/mcp (server card at https://gtm.ai/.well-known/mcp/server-card.json; plugin repo https://github.com/Zoominfo/zoominfo-mcp-plugin)

- [https://mcp.zoominfo.com/mcp](https://mcp.zoominfo.com/mcp)
- [https://gtm.ai/.well-known/mcp/server-card.json](https://gtm.ai/.well-known/mcp/server-card.json)
- [https://github.com/Zoominfo/zoominfo-mcp-plugin](https://github.com/Zoominfo/zoominfo-mcp-plugin)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (CHANGED 2026-08-25, see notes - the MCP/API path is now self-serve via GTM.AI; the classic seat-based ZoomInfo platform remains enterprise-only)

**API documentation**

[https://gtm.ai/docs](https://gtm.ai/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Zoominfo/zoominfo-mcp-plugin](https://github.com/Zoominfo/zoominfo-mcp-plugin)

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://gtm.ai/](https://gtm.ai/)
- [https://gtm.ai/pricing](https://gtm.ai/pricing)
- [https://gtm.ai/docs/mcp](https://gtm.ai/docs/mcp)
- [https://gtm.ai/docs/mcp/clients](https://gtm.ai/docs/mcp/clients)
- [https://gtm.ai/.well-known/mcp/server-card.json](https://gtm.ai/.well-known/mcp/server-card.json)
- [https://gtm.ai/llms.txt](https://gtm.ai/llms.txt)
- [https://www.businesswire.com/news/home/20260601055723/en/ZoomInfo-Launches-GTM.AI-the-Headless-GTM-Context-Layer-to-Ground-Every-AI-Agent-in-Verified-GTM-Data](https://www.businesswire.com/news/home/20260601055723/en/ZoomInfo-Launches-GTM.AI-the-Headless-GTM-Context-Layer-to-Ground-Every-AI-Agent-in-Verified-GTM-Data)
- [https://ir.zoominfo.com/news-releases/news-release-details/zoominfo-launches-gtmai-cli-bringing-verified-gtm-data-command/](https://ir.zoominfo.com/news-releases/news-release-details/zoominfo-launches-gtmai-cli-bringing-verified-gtm-data-command/)
- [https://github.com/Zoominfo/zoominfo-mcp-plugin](https://github.com/Zoominfo/zoominfo-mcp-plugin)
- [https://pipeline.zoominfo.com/operations/zoominfo-mcp-server](https://pipeline.zoominfo.com/operations/zoominfo-mcp-server)
- [https://www.cleanlist.ai/blog/2026-03-19-zoominfo-pricing-guide](https://www.cleanlist.ai/blog/2026-03-19-zoominfo-pricing-guide)

11 source URLs. Raw sources field, verbatim:

https://gtm.ai/, https://gtm.ai/pricing, https://gtm.ai/docs/mcp, https://gtm.ai/docs/mcp/clients, https://gtm.ai/.well-known/mcp/server-card.json, https://gtm.ai/llms.txt, https://www.businesswire.com/news/home/20260601055723/en/ZoomInfo-Launches-GTM.AI-the-Headless-GTM-Context-Layer-to-Ground-Every-AI-Agent-in-Verified-GTM-Data, https://ir.zoominfo.com/news-releases/news-release-details/zoominfo-launches-gtmai-cli-bringing-verified-gtm-data-command/, https://github.com/Zoominfo/zoominfo-mcp-plugin, https://pipeline.zoominfo.com/operations/zoominfo-mcp-server, https://www.cleanlist.ai/blog/2026-03-19-zoominfo-pricing-guide

**Notes, verbatim from the file**
MATERIAL CHANGE FOUND 2026-08-25, and it contradicts this directory's own headline finding that legacy incumbents are enterprise-gated. ZoomInfo launched GTM.AI (gtm.ai), a "headless GTM context layer," announced 2026-06-01, plus a GTM.AI CLI. The published pricing page states "one tier, no contract, no seat fees," 1,000 data credits plus 1,000 AI credits free to start with no credit card, then pay-as-you-go from a $20 minimum top-up at $0.10 per data credit (launch promo; $0.35 regular) and $0.05 per AI credit, charged once per record per year. Search, lookup, find-similar and GTM-context tools are documented as free to call; credits are consumed only on enrichment and AI research. The server card declares 22 tools (account_research, browse_audiences, browse_engagements, contact_research, conversation_intelligence, enrich_companies, enrich_company_signals, enrich_contacts, enrich_intent, enrich_news, enrich_scoops, find_recommended_contacts, find_similar_companies, find_similar_contacts, get_audience, gtm_context, lookup, search_companies, search_contacts, search_intent, search_scoops, update_gtm_context) at server version 3.0 over HTTP. gtm.ai also publishes /.well-known/agent-skills/index.json and /.well-known/api-catalog, which is the most agent-native discovery surface found anywhere in this directory. PRIOR STATE, kept on the record: as of 2026-08-24 this entry read api_gate enterprise-only, on the basis that no self-serve path existed and API access shipped inside annual contracts reportedly starting around $50K/year. That classic seat-based platform motion still exists; what changed is that a credit-metered self-serve door opened next to it. NOT VERIFIED THIS PASS: whether the free GTM.AI tier's data coverage matches a paid ZoomInfo seat, and whether "ZoomInfo Lite" (named in secondary sources as the permanent free tier) is the same thing as the GTM.AI free tier or a separate product. Both need a hands-on check before this is used on camera.

**Provenance**

- **Entry id**: 01-zoominfo

- **Source file**: 01-data-enrichment.md

- **Source line**: 7

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
