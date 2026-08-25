# UpLead: MCP server status, API access gate and what it does

> A B2B contact database and prospecting tool (vendor claims 160M+ contacts, 95% data accuracy) for building... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
UpLead

# UpLead

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [uplead.com](https://uplead.com) · entry id 01-uplead · source 01-data-enrichment.md line 331

**What it does**
A B2B contact database and prospecting tool (vendor claims 160M+ contacts, 95% data accuracy) for building lead lists with verified emails, direct dials, and firmographic/technographic filters, with a browser extension and CRM integrations.

**AI features, separated from automation with an AI label on it**
No distinct AI/ML feature set found beyond standard match-and-verify logic (real-time email verification, intent-data overlays). Marketing emphasizes "accuracy" and "verified," not AI - functionally this is a traditional enrichment database rather than an AI product, despite appearing in "AI tools" roundups.

**RevOps role**
Prospecting/list-build and enrichment source; lower self-serve tiers cover manual search, CSV export, and a limited real-time Enrichment API, while full API/integration-building access requires the top custom-priced tier.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Handled through the Zapier/Pipedream platform's own connector auth (API key entered into that third-party platform), not a UpLead-native OAuth or API-key flow

- **Parsed URLs**: 2 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://zapier.com/mcp/uplead (also listed on Pipedream: https://mcp.pipedream.com/app/uplead)

- [https://zapier.com/mcp/uplead](https://zapier.com/mcp/uplead)
- [https://mcp.pipedream.com/app/uplead](https://mcp.pipedream.com/app/uplead)

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
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.uplead.com/pricing/](https://www.uplead.com/pricing/)
- [https://zapier.com/mcp/uplead](https://zapier.com/mcp/uplead)
- [https://mcp.pipedream.com/app/uplead](https://mcp.pipedream.com/app/uplead)
- [https://www.landbase.com/blog/uplead-pricing](https://www.landbase.com/blog/uplead-pricing)
- [https://www.cleanlist.ai/blog/2026-07-15-uplead-pricing-guide](https://www.cleanlist.ai/blog/2026-07-15-uplead-pricing-guide)

5 source URLs. Raw sources field, verbatim:

https://www.uplead.com/pricing/, https://zapier.com/mcp/uplead, https://mcp.pipedream.com/app/uplead, https://www.landbase.com/blog/uplead-pricing, https://www.cleanlist.ai/blog/2026-07-15-uplead-pricing-guide

**Notes, verbatim from the file**
No dedicated UpLead-built MCP server was found on github.com, mcp.so, glama.ai, or pulsemcp.com - the only "MCP" listings are generic Zapier/Pipedream action-wrapper connectors, so this is marked community/third-party, not an official protocol-native server. Pricing: Essentials ($99/mo billed monthly, ~$74/mo annual) and Plus ($199/mo, ~$149/mo annual) are self-serve and include a limited real-time "Enrichment API" (Plus adds a "Prospector Pro API" for search). Full/unrestricted API access is reserved for the Professional tier - annual-only, custom-priced, "Book a Demo" only, no self-serve checkout - functionally enterprise-gated for complete API use.

**Provenance**

- **Entry id**: 01-uplead

- **Source file**: 01-data-enrichment.md

- **Source line**: 331

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
