# Make: MCP server status, API access gate and what it does

> A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Make

# Make

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [make.com](https://make.com) · entry id 06-make · source 06-revops-infra.md line 164

**What it does**
A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent and natural-language-build features layered on top.

**AI features, separated from automation with an AI label on it**
Make AI Agents genuinely use an LLM to reason, choose what to do next, and trigger real workflows, and can analyze unstructured text/documents - but Make's own docs frame agents as operating "alongside deterministic logic, not instead of it," built/debugged inside the same visual scenario canvas with manual approvals or hard stops available. Closer to LLM-reasoning-nodes embedded in classic automation than a fully autonomous runtime. "Maia by Make" is a separate natural-language scenario builder (LLM-assisted authoring, not autonomous execution).

**RevOps role**
Same class as Zapier - integration/orchestration layer for a GTM stack; ships both an MCP Server (expose Make scenarios as tools to Claude/ChatGPT/Cursor) and an MCP Client (let Make scenarios consume external MCP servers), a more complete two-way implementation than most competitors here.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Two supported methods - OAuth via Make's cloud (endpoint mcp.make.com) or an MCP Token generated from the user's Make profile, sent as a Bearer token to a per-zone stateless-HTTP endpoint (SSE transport also supported).

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://developers.make.com/mcp-server](https://developers.make.com/mcp-server)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developers.make.com/mcp-server

- [https://developers.make.com/mcp-server](https://developers.make.com/mcp-server)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid for full access - scenario-run tools are available on all plans including Free, but management tools require a paid plan (Core, from $12/mo).

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.make.com/en/pricing](https://www.make.com/en/pricing)
- [https://www.make.com/en/ai-agents](https://www.make.com/en/ai-agents)
- [https://developers.make.com/mcp-server](https://developers.make.com/mcp-server)

3 source URLs. Raw sources field, verbatim:

https://www.make.com/en/pricing, https://www.make.com/en/ai-agents, https://developers.make.com/mcp-server

**Notes, verbatim from the file**
none

**Provenance**

- **Entry id**: 06-make

- **Source file**: 06-revops-infra.md

- **Source line**: 164

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
