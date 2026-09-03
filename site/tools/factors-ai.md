# Factors.ai: MCP server status, API access gate and what it does

> De-anonymizes website visitors and tracks named-account behavior (page visits, LinkedIn/Google ad engagement,... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Factors.ai

# Factors.ai

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.factors.ai](https://www.factors.ai) · entry id 05-factors-ai · source 05-signals-intent-abm.md line 331

**What it does**
De-anonymizes website visitors and tracks named-account behavior (page visits, LinkedIn/Google ad engagement, email/content engagement, third-party intent research signals) to identify in-market accounts and specific contacts.

**AI features, separated from automation with an AI label on it**
"Scout Agent" is a genuine AI copilot/LLM layer grounded in account data (chat-based Q&A, account research). Predictive account scoring is more conventional scoring/ranking on engagement signals - model details aren't disclosed, so treat "predictive" as scored/ranked data rather than confirmed deep ML.

**RevOps role**
Account-level intent + engagement tracking with an AI copilot (Scout) for research/attribution, exposed to external AI clients via MCP.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Personal access token (generated in Settings > AI Features), used via Claude custom connector or a local Python 3.11+ package.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://help.factors.ai/en/articles/14705206-factors-mcp](https://help.factors.ai/en/articles/14705206-factors-mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://help.factors.ai/en/articles/14705206-factors-mcp

- [https://help.factors.ai/en/articles/14705206-factors-mcp](https://help.factors.ai/en/articles/14705206-factors-mcp)

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

- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.factors.ai/](https://www.factors.ai/)
- [https://www.factors.ai/pricing](https://www.factors.ai/pricing)
- [https://help.factors.ai/en/articles/14705206-factors-mcp](https://help.factors.ai/en/articles/14705206-factors-mcp)
- [https://www.factors.ai/mcp](https://www.factors.ai/mcp)

4 source URLs. Raw sources field, verbatim:

https://www.factors.ai/, https://www.factors.ai/pricing, https://help.factors.ai/en/articles/14705206-factors-mcp, https://www.factors.ai/mcp

**Notes, verbatim from the file**
Lite tier is free/self-serve (2-minute setup, no card) but is visitor-ID/traffic-analysis only. MCP/Scout Agent access requires "AI Features," gated behind paid plans (Basic $6K/yr, Growth $20K/yr, Enterprise $30K+/yr) that require booking a demo rather than self-serve checkout.

**Provenance**

- **Entry id**: 05-factors-ai

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 331

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
