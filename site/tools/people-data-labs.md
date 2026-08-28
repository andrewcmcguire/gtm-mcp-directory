# People Data Labs: MCP server status, API access gate and what it does

> A raw person/company data API that returns profile records (name, job history, education, skills, social... Community MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
People Data Labs

# People Data Labs

[Community MCP](../mcp/community.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.peopledatalabs.com](https://www.peopledatalabs.com) · entry id 01-people-data-labs · source 01-data-enrichment.md line 122

**What it does**
A raw person/company data API that returns profile records (name, job history, education, skills, social handles, contact fields) matched by identifiers like email, name, or LinkedIn URL, plus SQL-style bulk search over its dataset.

**AI features, separated from automation with an AI label on it**
Uses match-confidence/"likelihood" scoring for identity resolution (i.e., probabilistic record matching) and describes some fraud-detection scoring as AI-driven; this is largely statistical matching/scoring rather than generative AI. Vendor and third-party pages use "AI-powered" broadly, but the verifiable functionality is data lookup plus a confidence score.

**RevOps role**
Bulk/programmatic person and company enrichment feeding a CRM, data warehouse, or downstream identity-resolution pipeline; commonly used as a raw-data backend rather than a polished GTM tool.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: api key (PDL_API_KEY environment variable)

- **Parsed URLs**: 1 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/phxdev1/peopledatalabs-mcp

- [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp)

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

- [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp)

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Reverse-look-up a person from an email](../jobs/reverse-lookup-person-from-email.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://support.peopledatalabs.com/hc/en-us/articles/25794271805211-Pricing-credits](https://support.peopledatalabs.com/hc/en-us/articles/25794271805211-Pricing-credits)
- [https://nubela.co/blog/people-data-labs-pricing/](https://nubela.co/blog/people-data-labs-pricing/)
- [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp)
- [https://glama.ai/mcp/servers/phxdev1/peopledatalabs-mcp](https://glama.ai/mcp/servers/phxdev1/peopledatalabs-mcp)
- [https://saleshive.com/vendors/peopledatalabs](https://saleshive.com/vendors/peopledatalabs)

5 source URLs. Raw sources field, verbatim:

https://support.peopledatalabs.com/hc/en-us/articles/25794271805211-Pricing-credits, https://nubela.co/blog/people-data-labs-pricing/, https://github.com/phxdev1/peopledatalabs-mcp, https://glama.ai/mcp/servers/phxdev1/peopledatalabs-mcp, https://saleshive.com/vendors/peopledatalabs

**Notes, verbatim from the file**
Free plan is $0/mo, no credit card required, up to 100 records/month, but contact fields (email/phone) return only as true/false flags, not actual values, on the free tier. Self-serve Pro plan starts ~$98/mo (350 records) with full contact field access, tiered per-credit pricing (~$0.25-$0.28/credit for Person data), and a separate $0.55/credit Person Identify API. The MCP server found (github.com/phxdev1/peopledatalabs-mcp) is a third-party/community project, not published by People Data Labs itself - no official PDL-run MCP was found.

**Provenance**

- **Entry id**: 01-people-data-labs

- **Source file**: 01-data-enrichment.md

- **Source line**: 122

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
