# Autobound: MCP server status, API access gate and what it does

> Generates personalised outbound email copy and openers from live buyer signals, and sells the underlying... Official MCP, Free to start. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Autobound

# Autobound

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [autobound.ai](https://autobound.ai) · entry id 02-autobound · source 02-engagement-outbound.md line 503

**What it does**
Generates personalised outbound email copy and openers from live buyer signals, and sells the underlying signal data as an API and MCP feed.

**AI features, separated from automation with an AI label on it**
Signal ranking plus generative copy from a claimed 700+ insight types and 35+ proprietary signal categories (job changes, funding, hiring, news, podcast and LinkedIn activity). The signal collection layer is data engineering; the ranking and content generation is the AI claim. Vendor copy is the only source for the "700+ insights" figure.

**RevOps role**
Personalisation and signal layer that sits underneath a sequencer (Outreach, Salesloft, Apollo) or feeds an agent directly, rather than sending mail itself.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key via an AUTOBOUND_API_KEY environment variable in the MCP client config.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.autobound.ai/integrations/mcp](https://www.autobound.ai/integrations/mcp)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.autobound.ai/integrations/mcp (npm package @autobound-ai/mcp-server, installed via npx -y @autobound-ai/mcp-server; announcement: https://www.autobound.ai/blog/announcing-autobounds-model-context-protocol-mcp)

- [https://www.autobound.ai/integrations/mcp](https://www.autobound.ai/integrations/mcp)
- [https://www.autobound.ai/blog/announcing-autobounds-model-context-protocol-mcp](https://www.autobound.ai/blog/announcing-autobounds-model-context-protocol-mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

[https://autobound-api.readme.io](https://autobound-api.readme.io)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.autobound.ai/integrations/mcp](https://www.autobound.ai/integrations/mcp)
- [https://www.autobound.ai/pricing](https://www.autobound.ai/pricing)
- [https://www.autobound.ai/platform/embedded-api](https://www.autobound.ai/platform/embedded-api)
- [https://www.autobound.ai/blog/announcing-autobounds-model-context-protocol-mcp](https://www.autobound.ai/blog/announcing-autobounds-model-context-protocol-mcp)
- [https://www.autobound.ai/blog/may-2026-product-update](https://www.autobound.ai/blog/may-2026-product-update)
- [https://autobound-api.readme.io/docs/introduction](https://autobound-api.readme.io/docs/introduction)
- [https://www.speakeasy.com/customers/autobound](https://www.speakeasy.com/customers/autobound)

7 source URLs. Raw sources field, verbatim:

https://www.autobound.ai/integrations/mcp, https://www.autobound.ai/pricing, https://www.autobound.ai/platform/embedded-api, https://www.autobound.ai/blog/announcing-autobounds-model-context-protocol-mcp, https://www.autobound.ai/blog/may-2026-product-update, https://autobound-api.readme.io/docs/introduction, https://www.speakeasy.com/customers/autobound

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. ONE OF THE VERY FEW VENDORS IN THIS ENTIRE DIRECTORY where a solo operator can get a real API key and a working MCP server in minutes with zero sales contact: signup grants 1,000 free credits with no credit card and no sales call per the vendor pricing page. Published paid tiers: Starter $19 (2,000 credits), Growth $49, Scale $149, Pro $499, Business $1,299, Enterprise $4,999. The pricing page states the REST API plus MCP server are included on every plan with no tier restriction. TWO VENDOR SELF-CONFLICTS to note: the Embedded API page tells developers to email Autobound to "get provisioned with an API key" while the pricing page shows self-serve, and the MCP page says 100 free credits while the pricing page says 1,000. Treat the pricing page as canonical for credits. Tool count is also inconsistent across vendor pages: the May 2026 update says 11 tools, the MCP integrations page says 14 (signal_search, company_enrich, contact_enrich, company_timeline, contact_timeline, signal_types, account_info plus bulk and monitoring tools). The MCP server itself is described as free and open source; you pay for credit consumption.

**Provenance**

- **Entry id**: 02-autobound

- **Source file**: 02-engagement-outbound.md

- **Source line**: 503

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
