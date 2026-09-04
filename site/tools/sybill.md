# Sybill: MCP server status, API access gate and what it does

> AI sales assistant that analyzes call recordings, emails, and CRM data to produce deal insights, call... Official MCP, Enterprise leaning. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Sybill

# Sybill

[Official MCP](../mcp/official.md)
[Enterprise leaning](../gates/enterprise-leaning.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [sybill.ai](https://sybill.ai) · entry id 03-sybill · source 03-conversation-intel.md line 239

**What it does**
AI sales assistant that analyzes call recordings, emails, and CRM data to produce deal insights, call summaries, and behavioral/sentiment reads on prospects.

**AI features, separated from automation with an AI label on it**
Conversational Q&A over calls, deals, people, and companies; deal-insight generation; auto-generated summaries. Vendor also markets "real-time risk intelligence" and behavioral-analysis claims that are vendor copy and were not independently verified here.

**RevOps role**
Chat-first conversation-intelligence layer aimed at individual AEs, with a still-experimental developer surface.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Browser-based sign-in / OAuth on first connection from an MCP client such as Claude Desktop.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.sybill.ai/docs/mcp.html (server https://mcp.sybill.ai/mcp)

- [https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html)
- [https://mcp.sybill.ai/mcp](https://mcp.sybill.ai/mcp)

**Access gate**

- **Gate bucket**: Enterprise leaning

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-leaning (API and MCP access appear only on Business at $90/user/mo and Enterprise; Free and Pro carry neither, and the Business CTA is book-a-demo rather than a self-serve checkout)

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search across recorded calls](../jobs/search-call-library.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html)
- [https://api.sybill.ai/docs/introduction.html](https://api.sybill.ai/docs/introduction.html)
- [https://www.sybill.ai/pricing](https://www.sybill.ai/pricing)
- [https://help.sybill.ai/en/articles/15384825-sybill-ai-credits-guide-pricing-overview](https://help.sybill.ai/en/articles/15384825-sybill-ai-credits-guide-pricing-overview)

4 source URLs. Raw sources field, verbatim:

https://api.sybill.ai/docs/mcp.html, https://api.sybill.ai/docs/introduction.html, https://www.sybill.ai/pricing, https://help.sybill.ai/en/articles/15384825-sybill-ai-credits-guide-pricing-overview

**Notes, verbatim from the file**
None. [api_gate 2026-08-25] Reclassified unknown -> enterprise-leaning from the vendor's own page (https://www.sybill.ai/pricing): API and MCP access appear only on Business at $90/user/mo and Enterprise; Free and Pro carry neither, and the Business CTA is book-a-demo rather than a self-serve checkout.

**Provenance**

- **Entry id**: 03-sybill

- **Source file**: 03-conversation-intel.md

- **Source line**: 239

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
