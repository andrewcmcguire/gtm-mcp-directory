# Clari: MCP server status, API access gate and what it does

> Revenue operations platform that aggregates CRM, activity, and conversation data into pipeline inspection,... Official MCP, Enterprise leaning. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Clari

# Clari

[Official MCP](../mcp/official.md)
[Enterprise leaning](../gates/enterprise-leaning.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [clari.com](https://clari.com) · entry id 03-clari · source 03-conversation-intel.md line 30

**What it does**
Revenue operations platform that aggregates CRM, activity, and conversation data into pipeline inspection, forecasting, and deal-execution workflows.

**AI features, separated from automation with an AI label on it**
"Revenue AI Agents" for automated deal inspection and forecast automation are the genuinely AI-branded pieces; most of the rest of the platform is workflow/analytics orchestration over activity data rather than independently-verified ML.

**RevOps role**
Forecasting / pipeline-inspection layer sitting above conversation-intelligence tools like Clari Copilot or Gong.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown / not disclosed publicly

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/](https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/ (no public technical docs or repo found - the announcement points to a sales/Champions-Hub contact, not open docs)

- [https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/](https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/)

**Access gate**

- **Gate bucket**: Enterprise leaning

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-leaning, not self-serve. Clari's core v4 API requires a paid subscription plus a support ticket to have Clari enable a feature flag on the account - it is not something a solo operator can turn on themselves. The MCP server announcement is likewise framed as a sales conversation, not a signup page.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Clari (+ Salesloft agents)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: Official MCP

- **Gate there**: Enterprise only

- **Source**: 04-ai-sdr-agents.md line 258

- **Canonical page**: [Clari](../tools/clari.md)

What that listing says it does: Primarily a revenue-intelligence/forecasting platform (deal inspection, pipeline forecasting) with an AI Copilot for conversation coaching; following Clari's merger with Salesloft, the combined product line adds "Revenue AI Agents" for deal inspection/forecast automation and (via Salesloft) outbound execution.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/](https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/)
- [https://www.salesloft.com/innovation/feature-releases/spring-2026-product-update](https://www.salesloft.com/innovation/feature-releases/spring-2026-product-update)
- [https://community.clari.com/product-q-a-6/clari-api-all-you-need-to-know-556](https://community.clari.com/product-q-a-6/clari-api-all-you-need-to-know-556)
- [https://community.clari.com/general-q-a-7/using-clari-api-1542](https://community.clari.com/general-q-a-7/using-clari-api-1542)

4 source URLs. Raw sources field, verbatim:

https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/, https://www.salesloft.com/innovation/feature-releases/spring-2026-product-update, https://community.clari.com/product-q-a-6/clari-api-all-you-need-to-know-556, https://community.clari.com/general-q-a-7/using-clari-api-1542

**Notes, verbatim from the file**
This April 2026 MCP server is a joint Clari + Salesloft product (the two appear to have combined go-to-market) - separate from the Clari Copilot conversation-intelligence product below.

**Provenance**

- **Entry id**: 03-clari

- **Source file**: 03-conversation-intel.md

- **Source line**: 30

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
