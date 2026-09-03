# Prospeo: MCP server status, API access gate and what it does

> A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Prospeo

# Prospeo

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [prospeo.io](https://prospeo.io) · entry id 01-prospeo · source 01-data-enrichment.md line 198

**What it does**
A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given person or domain and returns basic firmographic data (headcount, industry, tech stack) for companies; also supports filtered people/company search.

**AI features, separated from automation with an AI label on it**
No credible AI capability surfaced in sources reviewed. Core mechanism is database lookup, email-pattern generation, domain search, and SMTP-based verification - a plain enrichment/lookup tool, not an AI-driven one, despite the modern positioning common in this category.

**RevOps role**
Email/phone finder and person+company search layer, most often plugged into Clay waterfalls (Clay-managed account billed at 2 credits/enriched cell) or used directly as a fallback provider alongside other finders.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 for the hosted server (auto-handled by Claude.ai/Desktop via the MCP directory); local/self-hosted setup uses an API key via PROSPEO_API_KEY env var or X-KEY header

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/prospeo-v2/prospeo-mcp-server

- [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Meerkats-Ai/prospeo-mcp-server](https://github.com/Meerkats-Ai/prospeo-mcp-server)
- [https://github.com/orchidautomation/prospeo-mcp](https://github.com/orchidautomation/prospeo-mcp)
- [https://github.com/prospeo-v2](https://github.com/prospeo-v2)
- [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server)

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

- [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server)
- [https://github.com/prospeo-v2](https://github.com/prospeo-v2)
- [https://github.com/orchidautomation/prospeo-mcp](https://github.com/orchidautomation/prospeo-mcp)
- [https://github.com/Meerkats-Ai/prospeo-mcp-server](https://github.com/Meerkats-Ai/prospeo-mcp-server)
- [https://fullenrich.com/content/prospeo-pricing](https://fullenrich.com/content/prospeo-pricing)
- [https://www.xpay.sh/saas-pricing/prospeo-io/](https://www.xpay.sh/saas-pricing/prospeo-io/)
- [https://www.clay.com/integrations/data-provider/prospeo](https://www.clay.com/integrations/data-provider/prospeo)
- [https://university.clay.com/docs/prospeo-integration-overview](https://university.clay.com/docs/prospeo-integration-overview)

8 source URLs. Raw sources field, verbatim:

https://github.com/prospeo-v2/prospeo-mcp-server, https://github.com/prospeo-v2, https://github.com/orchidautomation/prospeo-mcp, https://github.com/Meerkats-Ai/prospeo-mcp-server, https://fullenrich.com/content/prospeo-pricing, https://www.xpay.sh/saas-pricing/prospeo-io/, https://www.clay.com/integrations/data-provider/prospeo, https://university.clay.com/docs/prospeo-integration-overview

**Notes, verbatim from the file**
Confirmed as a Clay "data provider" (native waterfall integration), a separate integration surface from the MCP. Besides the official prospeo-v2 MCP repo, at least two unofficial community MCP wrappers exist (orchidautomation/prospeo-mcp, Meerkats-Ai/prospeo-mcp-server), both hitting the same public API. Pricing sources conflict slightly: most describe a self-serve free plan (100 credits/mo) plus paid plans from $39-49/mo, but one third-party source claimed the public pricing page pushes visitors to a sales-contact form - flagged as a discrepancy, not resolved.

**Provenance**

- **Entry id**: 01-prospeo

- **Source file**: 01-data-enrichment.md

- **Source line**: 198

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
