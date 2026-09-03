# Highspot: MCP server status, API access gate and what it does

> Sales enablement platform (content management, training) that has added a genuine call-recording and... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Highspot

# Highspot

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [highspot.com](https://highspot.com) · entry id 03-highspot · source 03-conversation-intel.md line 353

**What it does**
Sales enablement platform (content management, training) that has added a genuine call-recording and conversation-intelligence module on top of its core content product.

**AI features, separated from automation with an AI label on it**
Highspot Copilot uses generative AI plus conversation intelligence to score sales skills and deliver real-time coaching feedback from actual call recordings; call summaries, action items, and objection tracking are pulled from real calls via Highspot's acquisition of Nova.ai, now integrated natively into its codebase. This is genuine call-analysis AI, not just content recommendation - which is why it clears the bar for inclusion in this category.

**RevOps role**
Enablement-plus-conversation-intelligence hub, positioned to feed content, coaching, and call data to external AI agents via MCP.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - product page describes agent-to-agent access via OpenAI, Anthropic, and Microsoft Copilot integrations but does not detail the underlying auth mechanism.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.highspot.com/product/mcp-server/](https://www.highspot.com/product/mcp-server/)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.highspot.com/product/mcp-server/

- [https://www.highspot.com/product/mcp-server/](https://www.highspot.com/product/mcp-server/)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (inferred). Highspot has no public self-serve pricing; sales enablement platforms of this class are sold via enterprise contract only in every source reviewed.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Retrieve sales content](../jobs/retrieve-sales-content.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.highspot.com/product/mcp-server/](https://www.highspot.com/product/mcp-server/)
- [https://www.highspot.com/product/conversation-intelligence-software/](https://www.highspot.com/product/conversation-intelligence-software/)
- [https://www.highspot.com/blog/what-is-conversation-intelligence/](https://www.highspot.com/blog/what-is-conversation-intelligence/)
- [https://www.highspot.com/blog/discover-highspot-powering-impactful-buyer-engagement-with-ai-driven-insights/](https://www.highspot.com/blog/discover-highspot-powering-impactful-buyer-engagement-with-ai-driven-insights/)

4 source URLs. Raw sources field, verbatim:

https://www.highspot.com/product/mcp-server/, https://www.highspot.com/product/conversation-intelligence-software/, https://www.highspot.com/blog/what-is-conversation-intelligence/, https://www.highspot.com/blog/discover-highspot-powering-impactful-buyer-engagement-with-ai-driven-insights/

**Notes, verbatim from the file**
Included per the schema's conditional instruction ("only if they have real conversation-AI") - Highspot qualifies via its Nova.ai-powered Conversation Intelligence module.

**Provenance**

- **Entry id**: 03-highspot

- **Source file**: 03-conversation-intel.md

- **Source line**: 353

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
