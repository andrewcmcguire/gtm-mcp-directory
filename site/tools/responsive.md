# Responsive (formerly RFPIO): MCP server status, API access gate and what it does

> RFP, DDQ, and security-questionnaire response-management platform with an approved-content library... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
Responsive (formerly RFPIO)

# Responsive (formerly RFPIO)

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [responsive.io](https://responsive.io) · entry id 13-responsive · source 13-proposals-deals.md line 147

**What it does**
RFP, DDQ, and security-questionnaire response-management platform with an approved-content library ("Library") and AI-assisted drafting grounded in that governed content.

**AI features, separated from automation with an AI label on it**
MCP server explicitly grounds AI-generated draft responses in Responsive's approved Library content (with provenance/review metadata) rather than open generation - a genuinely governance-aware design distinct from a plain chatbot wrapper, though how the underlying retrieval/ranking works is not disclosed.

**RevOps role**
RFP/DDQ response layer for AI-agent workflows, notable for a rare, genuinely transparent usage-based MCP price sitting on top of an otherwise fully opaque enterprise platform.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - not detailed in the sources reviewed.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.responsive.io/capability/mcp-server](https://www.responsive.io/capability/mcp-server)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.responsive.io/capability/mcp-server ; help docs: https://help.responsive.io/en-US/responsive/article/duV3ckq5-using-responsive-mcp-server-with-generative-ai-tools ; Microsoft connector listing: https://learn.microsoft.com/en-us/connectors/responsivemcp/

- [https://www.responsive.io/capability/mcp-server](https://www.responsive.io/capability/mcp-server)
- [https://help.responsive.io/en-US/responsive/article/duV3ckq5-using-responsive-mcp-server-with-generative-ai-tools](https://help.responsive.io/en-US/responsive/article/duV3ckq5-using-responsive-mcp-server-with-generative-ai-tools)
- [https://learn.microsoft.com/en-us/connectors/responsivemcp/](https://learn.microsoft.com/en-us/connectors/responsivemcp/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, separately metered from the core platform. Responsive's main platform is fully sales-led/custom-quote (four plans: Lite, Emerging, Growth, Enterprise; average reported spend ~$13,955/yr per third-party trackers, no public rate card). The MCP product itself has transparent usage pricing: $50/month plus $5 per 100 AI-generated answers.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Draft an RFP or questionnaire response](../jobs/draft-rfp-response.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.responsive.io/capability/mcp-server](https://www.responsive.io/capability/mcp-server)
- [https://help.responsive.io/en-US/responsive/article/duV3ckq5-using-responsive-mcp-server-with-generative-ai-tools](https://help.responsive.io/en-US/responsive/article/duV3ckq5-using-responsive-mcp-server-with-generative-ai-tools)
- [https://autorfp.ai/blog/responsive-rfpio-pricing](https://autorfp.ai/blog/responsive-rfpio-pricing)
- [https://tribble.ai/blog/responsive-rfpio-review-pricing-features-limitations-2026/](https://tribble.ai/blog/responsive-rfpio-review-pricing-features-limitations-2026/)

4 source URLs. Raw sources field, verbatim:

https://www.responsive.io/capability/mcp-server, https://help.responsive.io/en-US/responsive/article/duV3ckq5-using-responsive-mcp-server-with-generative-ai-tools, https://autorfp.ai/blog/responsive-rfpio-pricing, https://tribble.ai/blog/responsive-rfpio-review-pricing-features-limitations-2026/

**Notes, verbatim from the file**
Verify current URL/branding before publishing - Responsive was formerly RFPIO; responsive.io is the confirmed current primary domain used in official MCP docs.

**Provenance**

- **Entry id**: 13-responsive

- **Source file**: 13-proposals-deals.md

- **Source line**: 147

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
