# Retool: MCP server status, API access gate and what it does

> A low-code platform for building internal tools/dashboards/admin panels on top of databases and APIs; in a... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Retool

# Retool

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [retool.com](https://retool.com) · entry id 06-retool · source 06-revops-infra.md line 392

**What it does**
A low-code platform for building internal tools/dashboards/admin panels on top of databases and APIs; in a GTM context, used to build custom RevOps tooling - lead-routing consoles, deal-desk approval apps, data-correction UIs - on top of the warehouse/CRM.

**AI features, separated from automation with an AI label on it**
Real natural-language app-building ("prompt full-stack apps on your live production data," context-aware @mention editing), AI Workflows (chains AI calls with data/business logic, one-click RAG), and "AI Agents" framed as production-ready automations with audit trails - more than a chat-copilot bolt-on, but claims like "AI Agents handle customer support" should be read as marketing framing until seen in practice.

**RevOps role**
The app layer for RevOps - builds custom internal UIs on top of the warehouse/CRM for workflows off-the-shelf tools don't cover (approval flows, override consoles, ops dashboards).

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0. Endpoint pattern https:///mcp over HTTP.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://retool.com/blog/retool-mcp-server](https://retool.com/blog/retool-mcp-server)Probed**: 2026-08-25, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official (public beta)

mcp_url, verbatim from the file:

https://retool.com/blog/retool-mcp-server

- [https://retool.com/blog/retool-mcp-server](https://retool.com/blog/retool-mcp-server)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the Free plan is self-serve with no sales conversation (unlimited apps, 500 workflow runs/mo, up to 5 users); cheapest paid Team plan is $10/mo per builder, annual.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Query a data warehouse](../jobs/query-data-warehouse.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://retool.com/pricing](https://retool.com/pricing)
- [https://retool.com/products/ai](https://retool.com/products/ai)
- [https://retool.com/blog/retool-mcp-server](https://retool.com/blog/retool-mcp-server)

3 source URLs. Raw sources field, verbatim:

https://retool.com/pricing, https://retool.com/products/ai, https://retool.com/blog/retool-mcp-server

**Notes, verbatim from the file**
The MCP server manages apps/workflows/users (build/edit/deploy apps, run queries, bulk user invites, access audits, resource enumeration) - an admin/dev-ops-facing MCP rather than an end-user data MCP. Available to both cloud and self-hosted customers per the announcement.

**Provenance**

- **Entry id**: 06-retool

- **Source file**: 06-revops-infra.md

- **Source line**: 392

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
