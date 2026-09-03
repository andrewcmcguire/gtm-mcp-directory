# Snov.io: MCP server status, API access gate and what it does

> A B2B prospecting and outreach platform - finds and verifies emails/contacts, enriches company and contact... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Snov.io

# Snov.io

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [snov.io](https://snov.io) · entry id 01-snov-io · source 01-data-enrichment.md line 369

**What it does**
A B2B prospecting and outreach platform - finds and verifies emails/contacts, enriches company and contact records, manages prospect lists and a lightweight CRM, and runs email drip campaigns plus LinkedIn outreach actions.

**AI features, separated from automation with an AI label on it**
Mostly rule-based lookup, verification, and workflow automation (email finder, email warmup, drip sequencing) - not AI/ML in the underlying data. The 2026 MCP launch adds a genuine LLM-agent layer (natural-language commands driving 100+ underlying actions), but the core prospecting/enrichment data itself is aggregated/verified contact data, not AI-generated.

**RevOps role**
Mid-funnel prospecting/enrichment plus lightweight outreach execution (find contact -> verify -> add to campaign) - positioned as an all-in-one alternative to stitching together a separate finder, verifier, and sequencer.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - user reviews and approves the connection through their Snov.io account; no raw API key is shared with the AI assistant

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.snov.io/mcp](https://mcp.snov.io/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.snov.io/mcp (product page https://snov.io/mcp)

- [https://mcp.snov.io/mcp](https://mcp.snov.io/mcp)
- [https://snov.io/mcp](https://snov.io/mcp)

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

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://snov.io/mcp](https://snov.io/mcp)
- [https://snov.io/knowledgebase/how-to-use-snov-io-mcp-with-your-ai-assistant/](https://snov.io/knowledgebase/how-to-use-snov-io-mcp-with-your-ai-assistant/)
- [https://snov.io/pricing](https://snov.io/pricing)
- [https://snov.io/knowledgebase/faq-pricing-plans/](https://snov.io/knowledgebase/faq-pricing-plans/)
- [https://www.bookyourdata.com/blog/snov-io-pricing](https://www.bookyourdata.com/blog/snov-io-pricing)
- [https://www.saleshandy.com/blog/snovio-pricing/](https://www.saleshandy.com/blog/snovio-pricing/)

6 source URLs. Raw sources field, verbatim:

https://snov.io/mcp, https://snov.io/knowledgebase/how-to-use-snov-io-mcp-with-your-ai-assistant/, https://snov.io/pricing, https://snov.io/knowledgebase/faq-pricing-plans/, https://www.bookyourdata.com/blog/snov-io-pricing, https://www.saleshandy.com/blog/snovio-pricing/

**Notes, verbatim from the file**
REST API/webhook access is available "on all premium plans" starting at Starter ($39/mo, self-serve signup); the free Trial plan has API access locked. Snov.io states MCP access itself "is available across all plans, including the free Trial" - so MCP access is broader than raw API-key access, even though the underlying API is paid-tier only.

**Provenance**

- **Entry id**: 01-snov-io

- **Source file**: 01-data-enrichment.md

- **Source line**: 369

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
