# Salesloft: MCP server status, API access gate and what it does

> Sales engagement platform (merged with Clari in Dec 2025) for multichannel outbound cadences, call/email... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Salesloft

# Salesloft

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [salesloft.com](https://salesloft.com) · entry id 02-salesloft · source 02-engagement-outbound.md line 26

**What it does**
Sales engagement platform (merged with Clari in Dec 2025) for multichannel outbound cadences, call/email execution, and rep activity tracking that feeds forecasting.

**AI features, separated from automation with an AI label on it**
Vendor-named features include "Conductor AI" (analyzes buyer signals, automates next-best actions), "Rhythm with AI Prioritization," "Deal Intelligence," conversation intelligence on calls, "AI Email Agents," and "AI Forecast." No breakdown of which are genuinely model-driven vs. rules-based automation is published - treat as vendor-stated.

**RevOps role**
Core outbound execution and, post-Clari-merger, forecasting layer - increasingly positioned as "the context layer AI agents pull live revenue data from."

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown exact flow - vendor press material describes it as natively listed in Claude's connector directory "with no custom setup required," implying a managed OAuth connector, but the precise auth mechanics were not documented in sourced pages.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server](https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server ; https://www.salesloft.com/company/newsroom/salesloft-mcp-server-revenue-data-ai-ecosystem

- [https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server](https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server)
- [https://www.salesloft.com/company/newsroom/salesloft-mcp-server-revenue-data-ai-ecosystem](https://www.salesloft.com/company/newsroom/salesloft-mcp-server-revenue-data-ai-ecosystem)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (developer docs say customers need API keys to reach the API with no tier condition stated, but the pricing page publishes no prices or plan names and routes everything to contact-us)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developers.salesloft.com/](https://developers.salesloft.com/)
- [https://www.salesloft.com/company/newsroom/salesloft-mcp-server-revenue-data-ai-ecosystem](https://www.salesloft.com/company/newsroom/salesloft-mcp-server-revenue-data-ai-ecosystem)
- [https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server](https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server)
- [https://champions.salesloft.com/product-updates/august-2026-release-notes-605](https://champions.salesloft.com/product-updates/august-2026-release-notes-605)
- [https://www.vendr.com/marketplace/salesloft](https://www.vendr.com/marketplace/salesloft)
- [https://www.salesloft.com/pricing](https://www.salesloft.com/pricing)

6 source URLs. Raw sources field, verbatim:

https://developers.salesloft.com/, https://www.salesloft.com/company/newsroom/salesloft-mcp-server-revenue-data-ai-ecosystem, https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server, https://champions.salesloft.com/product-updates/august-2026-release-notes-605, https://www.vendr.com/marketplace/salesloft, https://www.salesloft.com/pricing

**Notes, verbatim from the file**
One of the most aggressive MCP rollouts researched in this category - initial launch April 2026, expanded July 2026 after the Clari-Salesloft merger, ChatGPT custom connector added August 2026. Vendr lists list pricing around $125-165/user/month, implying API/MCP access rides on a paid seat rather than being free-standing. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.salesloft.com/pricing): developer docs say customers need API keys to reach the API with no tier condition stated, but the pricing page publishes no prices or plan names and routes everything to contact-us.

**Provenance**

- **Entry id**: 02-salesloft

- **Source file**: 02-engagement-outbound.md

- **Source line**: 26

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
