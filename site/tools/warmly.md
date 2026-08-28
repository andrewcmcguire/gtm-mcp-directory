# Warmly (Warmly.ai): MCP server status, API access gate and what it does

> De-anonymizes website visitors at the person and company level from site traffic, and aggregates first-party... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Warmly (Warmly.ai)

# Warmly (Warmly.ai)

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.warmly.ai](https://www.warmly.ai) · entry id 05-warmly · source 05-signals-intent-abm.md line 135

**What it does**
De-anonymizes website visitors at the person and company level from site traffic, and aggregates first-party (web/product/CRM), second-party (social/job-change), and third-party (Bombora intent, keyword research) signals into a unified account/contact view.

**AI features, separated from automation with an AI label on it**
Mixed but partly genuine - an "AI chatbot" grounded in a proprietary "Context Graph" is a real conversational LLM layer. "ML Intent Scoring" and account tiering read more like scored/ranked aggregation of ingested signals (including licensed Bombora data) than a novel model; be more skeptical of that claim specifically.

**RevOps role**
Entry-level visitor-ID + intent aggregation - the lighter-weight, solo-operator-accessible alternative to 6sense/Demandbase in this category.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: MCP uses OAuth-based login (no manual key management); the separate REST API (opps-api.getwarmly.com) uses a per-organization API key.

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.warmly.ai/launches/warmly-mcp-and-api-are-live

- [https://www.warmly.ai/launches/warmly-mcp-and-api-are-live](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Warmly

- **Category**: [Data & Enrichment](../categories/data-enrichment.md)

- **MCP status there**: Official MCP

- **Gate there**: Free to start

- **Source**: 01-data-enrichment.md line 502

- **Canonical page**: [Warmly (Warmly.ai)](../tools/warmly.md)

What that listing says it does: A website-visitor de-anonymization and intent platform that identifies companies (and increasingly named individuals) visiting a customer's site from IP/behavioral signals, then enriches those visitor records with firmographic and contact data for follow-up.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.warmly.ai/launches/warmly-mcp-and-api-are-live](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live)
- [https://www.warmly.ai/p/resources/launches](https://www.warmly.ai/p/resources/launches)
- [https://opps-widget.getwarmly.com/pricing.html](https://opps-widget.getwarmly.com/pricing.html)
- [https://softwarefinder.com/customer-service-software/warmly](https://softwarefinder.com/customer-service-software/warmly)
- [https://www.leadpipe.com/blog/warmly-review-2026/](https://www.leadpipe.com/blog/warmly-review-2026/)

5 source URLs. Raw sources field, verbatim:

https://www.warmly.ai/launches/warmly-mcp-and-api-are-live, https://www.warmly.ai/p/resources/launches, https://opps-widget.getwarmly.com/pricing.html, https://softwarefinder.com/customer-service-software/warmly, https://www.leadpipe.com/blog/warmly-review-2026/

**Notes, verbatim from the file**
Free tier: 500 de-anonymized visitors/mo, limited Bombora intent, MCP included with 250 credits/mo, 60 req/min rate limit. Paid: Starter $99/mo, Growth $199/mo, Pro $499/mo, Enterprise custom. MCP tools are read-only (list_warm_visitors, list_warm_accounts, get_credits_remaining).

**Provenance**

- **Entry id**: 05-warmly

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 135

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
