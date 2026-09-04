# Dropcontact: MCP server status, API access gate and what it does

> A France-based, GDPR-oriented contact enrichment and email-finding/verification service that takes a name... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Dropcontact

# Dropcontact

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [dropcontact.com](https://dropcontact.com) · entry id 01-dropcontact · source 01-data-enrichment.md line 236

**What it does**
A France-based, GDPR-oriented contact enrichment and email-finding/verification service that takes a name plus company (name, domain, or LinkedIn URL) and returns a verified professional email plus cleaned company data, with batch processing of up to 250 contacts at once.

**AI features, separated from automation with an AI label on it**
No strong AI claims found; the vendor's own positioning centers on "triple verification" and data-matching/deduplication logic rather than AI/ML. Treat as automation and rules-based verification, not AI-branded.

**RevOps role**
GDPR-conscious contact enrichment/verification layer for CRM hygiene and list-building; also a widely-used Clay waterfall step (Clay-managed account billed at 2 credits/enriched cell, with a 24h auto-update toggle).

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Hosted server at mcp.dropcontact.com/mcp/, supporting OAuth (recommended, browser-based) or a Dropcontact API token/key passed via headers; also usable through the npx mcp-remote bridge for clients without native remote-MCP support

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.dropcontact.com/mcp-dropcontact](https://www.dropcontact.com/mcp-dropcontact)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.dropcontact.com/mcp-dropcontact

- [https://www.dropcontact.com/mcp-dropcontact](https://www.dropcontact.com/mcp-dropcontact)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.dropcontact.com/mcp-dropcontact](https://www.dropcontact.com/mcp-dropcontact)
- [https://developer.dropcontact.com](https://developer.dropcontact.com)
- [https://www.dropcontact.com/pricing](https://www.dropcontact.com/pricing)
- [https://www.clay.com/integrations/data-provider/dropcontact](https://www.clay.com/integrations/data-provider/dropcontact)
- [https://university.clay.com/docs/dropcontact-integration-overview](https://university.clay.com/docs/dropcontact-integration-overview)
- [https://www.dropcontact.com/help/clay-integration](https://www.dropcontact.com/help/clay-integration)
- [https://support.dropcontact.com/article/237-how-to-use-the-dropcontact-api-key](https://support.dropcontact.com/article/237-how-to-use-the-dropcontact-api-key)
- [https://developer.dropcontact.com/](https://developer.dropcontact.com/)

8 source URLs. Raw sources field, verbatim:

https://www.dropcontact.com/mcp-dropcontact, https://developer.dropcontact.com, https://www.dropcontact.com/pricing, https://www.clay.com/integrations/data-provider/dropcontact, https://university.clay.com/docs/dropcontact-integration-overview, https://www.dropcontact.com/help/clay-integration, https://support.dropcontact.com/article/237-how-to-use-the-dropcontact-api-key, https://developer.dropcontact.com/

**Notes, verbatim from the file**
Dropcontact is a clear "official, vendor-built" MCP - it has its own product page and a centrally hosted MCP endpoint at mcp.dropcontact.com, distinct from (and in addition to) its long-standing Clay data-provider integration. API & MCP access is bundled starting at the Starter tier (EUR 79/mo, ~500 credits/mo) and up; there is no persistent free API tier, only a "50 free emails" signup incentive. Pricing model is pay-on-success (1 credit = 1 email found or verified; credit refunded if nothing found). Lower tiers reportedly throttle API requests to ~100/min, which can bottleneck heavy Clay/n8n automation. 2026-09-03: vendor docs state the enrich endpoint (POST /v1/enrich/all) accepts "first_name + last_name + company (or full_name + company)" and its response includes a linkedin field with a linkedin.com/in/ example (https://developer.dropcontact.com/); no MCP tool name is stated there; the docs state a credit is charged only if a verified email is returned.

**Provenance**

- **Entry id**: 01-dropcontact

- **Source file**: 01-data-enrichment.md

- **Source line**: 236

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
