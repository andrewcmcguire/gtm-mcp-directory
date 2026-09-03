# Airbyte: MCP server status, API access gate and what it does

> Open-source/cloud ELT platform with 600+ connectors moving data from SaaS tools and databases into... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Airbyte

# Airbyte

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [airbyte.com](https://airbyte.com) · entry id 06-airbyte · source 06-revops-infra.md line 323

**What it does**
Open-source/cloud ELT platform with 600+ connectors moving data from SaaS tools and databases into warehouses; increasingly positions itself as a context layer for AI agents via a hosted Context Store.

**AI features, separated from automation with an AI label on it**
A real, substantive "Agents" product line (app.airbyte.ai) using a Connect-Ask-Act model that lets agents query/act on connected data - not just a copilot bolt-on. Whether the core Connector Builder itself has natural-language-assisted connector generation was not confirmed either way and is left as unknown rather than guessed.

**RevOps role**
Upstream data-integration layer - gets GTM tool data (and 600+ other sources) into the warehouse, and now also positions as the retrieval/action layer for AI agents to reach across GTM systems directly.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Two-layer OAuth 2.0 - OAuth into the Airbyte account/org for the MCP server itself, plus separate OAuth or API-key auth per connected third-party service (Salesforce, HubSpot, GitHub, Stripe, etc.), entered in-browser, never in agent chat. Hosted endpoint: https://mcp.airbyte.ai/mcp.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://docs.airbyte.com/ai-agents/interfaces/mcp](https://docs.airbyte.com/ai-agents/interfaces/mcp)Probed**: 2026-08-25, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.airbyte.com/ai-agents/interfaces/mcp

- [https://docs.airbyte.com/ai-agents/interfaces/mcp](https://docs.airbyte.com/ai-agents/interfaces/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - Core (self-managed, open source) is always free; Cloud has a genuine self-serve $0/mo tier (1,000 Agent Operations/month); cheapest paid Standard tier starts at $10/mo.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://airbyte.com/](https://airbyte.com/)
- [https://airbyte.com/pricing](https://airbyte.com/pricing)
- [https://docs.airbyte.com/ai-agents/interfaces/mcp](https://docs.airbyte.com/ai-agents/interfaces/mcp)

3 source URLs. Raw sources field, verbatim:

https://airbyte.com/, https://airbyte.com/pricing, https://docs.airbyte.com/ai-agents/interfaces/mcp

**Notes, verbatim from the file**
One of the more clearly "official and productized" MCP implementations in this file - hosted, documented, and multi-client (Claude, ChatGPT, Cursor, VS Code, Codex).

**Provenance**

- **Entry id**: 06-airbyte

- **Source file**: 06-revops-infra.md

- **Source line**: 323

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
