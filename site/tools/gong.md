# Gong: MCP server status, API access gate and what it does

> Records, transcribes, and analyzes sales calls and emails, then rolls the signals into deal-risk scores,... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Gong

# Gong

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [gong.io](https://gong.io) · entry id 03-gong · source 03-conversation-intel.md line 11

**What it does**
Records, transcribes, and analyzes sales calls and emails, then rolls the signals into deal-risk scores, coaching data, and revenue forecasts.

**AI features, separated from automation with an AI label on it**
ML-based "Deal Likelihood Score" trained on 300+ engagement/CRM signals; risk-signal detection (engagement drop-off, competitor mentions, missing stakeholders); auto-populated coaching scorecards; natural-language "Ask Anything" query layer. Recording/transcription itself is standard ASR, not the differentiator.

**RevOps role**
Call-recording / conversation-intelligence system of record feeding deal-risk and coaching signals into CRM and forecasting.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Official MCP client+server ships as part of Gong's enterprise agent stack (used to connect Microsoft 365 Copilot, Salesforce, etc.); community servers use Gong REST API Basic auth (Access Key + Access Key Secret from the admin console).

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://help.gong.io/docs/about-gong-mcp](https://help.gong.io/docs/about-gong-mcp)Probed**: 2026-08-25, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://help.gong.io/docs/about-gong-mcp ; announcement: https://www.gong.io/press/gong-introduces-model-context-protocol-mcp-support-to-unify-enterprise-ai-agents-from-hubspot-microsoft-salesforce-and-others ; community example: https://github.com/cedricziel/gong-mcp

- [https://help.gong.io/docs/about-gong-mcp](https://help.gong.io/docs/about-gong-mcp)
- [https://www.gong.io/press/gong-introduces-model-context-protocol-mcp-support-to-unify-enterprise-ai-agents-from-hubspot-microsoft-salesforce-and-others](https://www.gong.io/press/gong-introduces-model-context-protocol-mcp-support-to-unify-enterprise-ai-agents-from-hubspot-microsoft-salesforce-and-others)
- [https://github.com/cedricziel/gong-mcp](https://github.com/cedricziel/gong-mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only in practice. Gong's own help doc says the API is "Available on: Any Gong plan," but there is no self-serve signup at all - every purchase runs through sales with a mandatory annual platform fee (commonly $25,000-$50,000+/yr for mid-market/enterprise, $5,000 minimum) and multi-year contracts. A solo operator cannot get an API key without becoming a paying enterprise customer first.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/cedricziel/gong-mcp](https://github.com/cedricziel/gong-mcp)

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Search across recorded calls](../jobs/search-call-library.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://help.gong.io/docs/about-gong-mcp](https://help.gong.io/docs/about-gong-mcp)
- [https://help.gong.io/docs/receive-access-to-the-api](https://help.gong.io/docs/receive-access-to-the-api)
- [https://www.gong.io/press/gong-introduces-model-context-protocol-mcp-support-to-unify-enterprise-ai-agents-from-hubspot-microsoft-salesforce-and-others](https://www.gong.io/press/gong-introduces-model-context-protocol-mcp-support-to-unify-enterprise-ai-agents-from-hubspot-microsoft-salesforce-and-others)
- [https://www.claap.io/blog/gong-api](https://www.claap.io/blog/gong-api)
- [https://github.com/cedricziel/gong-mcp](https://github.com/cedricziel/gong-mcp)

5 source URLs. Raw sources field, verbatim:

https://help.gong.io/docs/about-gong-mcp, https://help.gong.io/docs/receive-access-to-the-api, https://www.gong.io/press/gong-introduces-model-context-protocol-mcp-support-to-unify-enterprise-ai-agents-from-hubspot-microsoft-salesforce-and-others, https://www.claap.io/blog/gong-api, https://github.com/cedricziel/gong-mcp

**Notes, verbatim from the file**
The "Available on: Any Gong plan" language is real but misleading for a solo operator - there is no plan you can buy without a sales-led enterprise contract, so treat the API as enterprise-gated regardless of that wording.

**Provenance**

- **Entry id**: 03-gong

- **Source file**: 03-conversation-intel.md

- **Source line**: 11

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
