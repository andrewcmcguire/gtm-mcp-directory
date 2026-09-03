# lemlist: MCP server status, API access gate and what it does

> Multichannel sales engagement platform combining lead database/enrichment, email/LinkedIn/call/SMS... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
lemlist

# lemlist

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [lemlist.com](https://lemlist.com) · entry id 02-lemlist · source 02-engagement-outbound.md line 160

**What it does**
Multichannel sales engagement platform combining lead database/enrichment, email/LinkedIn/call/SMS sequencing, and a unified inbox.

**AI features, separated from automation with an AI label on it**
"lemAgent" and "Intent Signal Agents" research prospects, act on trigger events, and generate personalized copy - genuinely AI per vendor description. "Data Enrichment Agents" synthesize third-party data. Lead filtering, sequencing workflows, and email warmup (lemwarm) are plain automation, explicitly distinguished from the agent features by the vendor itself.

**RevOps role**
Multichannel outbound sequencing and lead-enrichment layer, increasingly agent-augmented for personalization and trigger-based outreach.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (browser-based PKCE flow, recommended) or API key via X-API-Key header

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://developer.lemlist.com/mcp/setup](https://developer.lemlist.com/mcp/setup)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developer.lemlist.com/mcp/setup (endpoint https://app.lemlist.com/mcp)

- [https://developer.lemlist.com/mcp/setup](https://developer.lemlist.com/mcp/setup)
- [https://app.lemlist.com/mcp](https://app.lemlist.com/mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developer.lemlist.com/mcp/setup](https://developer.lemlist.com/mcp/setup)
- [https://www.lemlist.com/pricing](https://www.lemlist.com/pricing)
- [http://help.lemlist.com/en/articles/4452791-lemlist-plans-and-pricing-overview](http://help.lemlist.com/en/articles/4452791-lemlist-plans-and-pricing-overview)
- [https://developer.lemlist.com/api-reference/endpoints/enrich/enrich-data.md](https://developer.lemlist.com/api-reference/endpoints/enrich/enrich-data.md)

4 source URLs. Raw sources field, verbatim:

https://developer.lemlist.com/mcp/setup, https://www.lemlist.com/pricing, http://help.lemlist.com/en/articles/4452791-lemlist-plans-and-pricing-overview, https://developer.lemlist.com/api-reference/endpoints/enrich/enrich-data.md

**Notes, verbatim from the file**
One of the more clearly first-party, well-documented MCP implementations in this category - dual OAuth/API-key auth, 40+ documented actions. "Advanced API access" is explicitly called out as an Enterprise-tier ("Outreach Scale," 5+ seats, annual billing) feature; standard-tier API availability is not clearly documented, so treat access as paid/enterprise-leaning. 2026-09-03: vendor docs state the Enrich Data endpoint (POST /enrich) accepts firstName, lastName and companyName or companyDomain with a linkedinEnrichment flag ("Run LinkedIn enrichment") and its sample response returns linkedinUrl (https://developer.lemlist.com/api-reference/endpoints/enrich/enrich-data.md); no MCP tool name and no unit price are stated there.

**Provenance**

- **Entry id**: 02-lemlist

- **Source file**: 02-engagement-outbound.md

- **Source line**: 160

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
