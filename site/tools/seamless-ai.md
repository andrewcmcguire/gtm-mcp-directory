# Seamless.AI: MCP server status, API access gate and what it does

> A B2B contact and company database/prospecting tool that lets users search and pull emails, phone numbers,... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Seamless.AI

# Seamless.AI

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [seamless.ai](https://seamless.ai) · entry id 01-seamless-ai · source 01-data-enrichment.md line 312

**What it does**
A B2B contact and company database/prospecting tool that lets users search and pull emails, phone numbers, and firmographic data from a claimed 1.9B+ contact / 121M+ company index, plus basic list-building, outreach/campaign sending, and CRM sync.

**AI features, separated from automation with an AI label on it**
Marketed heavily as "AI-powered," but the core function - matching a target list against a contact database and returning emails/phones - is lookup plus data-matching/verification, not generative AI. The new MCP server adds a real LLM-agent layer (natural-language prompts driving search/enrichment/campaign actions), and there's an "AI research" account-summarization feature - that layer is genuine LLM use; the underlying contact data itself is a traditional scraped/aggregated database.

**RevOps role**
Top-of-funnel prospecting/contact-discovery source - used to build target lists and pull direct-dial/email data before handoff to outreach tooling; both raw API and (per docs) MCP access are gated behind account-level enablement tied to higher tiers.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.1 or API key; docs state "MCP access must be enabled on your account" - i.e. gated per-account, contact admin/support to turn on

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://docs.seamless.ai/mcp-docs](https://docs.seamless.ai/mcp-docs)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.seamless.ai/mcp-docs (hosted endpoint https://mcp.seamless.ai/mcp)

- [https://docs.seamless.ai/mcp-docs](https://docs.seamless.ai/mcp-docs)
- [https://mcp.seamless.ai/mcp](https://mcp.seamless.ai/mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Build a target account list](../jobs/build-target-account-list.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Run an email sequence](../jobs/run-email-sequence.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://docs.seamless.ai/mcp-docs](https://docs.seamless.ai/mcp-docs)
- [https://seamless.ai/customers/blog/products/seamless-mcp-server](https://seamless.ai/customers/blog/products/seamless-mcp-server)
- [https://www.prweb.com/releases/seamlessais-new-mcp-server-takes-you-from-prompt-to-closed-won-deal-302839077.html](https://www.prweb.com/releases/seamlessais-new-mcp-server-takes-you-from-prompt-to-closed-won-deal-302839077.html)
- [https://salesintel.io/blog/seamless-ai-pricing/](https://salesintel.io/blog/seamless-ai-pricing/)
- [https://www.spendhound.com/marketplace/seamlessai-pricing](https://www.spendhound.com/marketplace/seamlessai-pricing)
- [https://www.cleanlist.ai/blog/2026-03-19-seamless-ai-pricing-guide](https://www.cleanlist.ai/blog/2026-03-19-seamless-ai-pricing-guide)

6 source URLs. Raw sources field, verbatim:

https://docs.seamless.ai/mcp-docs, https://seamless.ai/customers/blog/products/seamless-mcp-server, https://www.prweb.com/releases/seamlessais-new-mcp-server-takes-you-from-prompt-to-closed-won-deal-302839077.html, https://salesintel.io/blog/seamless-ai-pricing/, https://www.spendhound.com/marketplace/seamlessai-pricing, https://www.cleanlist.ai/blog/2026-03-19-seamless-ai-pricing-guide

**Notes, verbatim from the file**
Multiple independent pricing breakdowns put raw API access on Seamless's Enterprise tier only, with quoted contracts roughly $20k-$100k/year depending on seats/volume; consumer-facing Free/Basic/Pro plans are seat-and-credit based with no documented self-serve API key. Treat "MCP access must be enabled on your account" as effectively the same enterprise gate.

**Provenance**

- **Entry id**: 01-seamless-ai

- **Source file**: 01-data-enrichment.md

- **Source line**: 312

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
