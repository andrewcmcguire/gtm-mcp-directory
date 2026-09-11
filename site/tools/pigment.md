# Pigment: MCP server status, API access gate and what it does

> AI-native enterprise business-planning (EPM) platform used across finance, sales, HR, and supply chain;... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Forecasting & Revenue](../categories/forecasting-revenue.md) /
Pigment

# Pigment

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Forecasting & Revenue](../categories/forecasting-revenue.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [pigment.com](https://pigment.com) · entry id 12-pigment · source 12-forecasting-revenue.md line 188

**What it does**
AI-native enterprise business-planning (EPM) platform used across finance, sales, HR, and supply chain; GTM-relevant use cases include capacity, territory, and quota planning and revenue-growth-management scenario modeling.

**AI features, separated from automation with an AI label on it**
A genuine ML "Predictions" feature trained on historical data plus external variables (promotions, marketing spend, seasonality) generates statistical forecasts embedded in models - distinct from Pigment's separate agentic layer (Modeler Agent, Analyst Agent, and a not-yet-shipped Planner Agent), which is LLM-workflow automation for building/analyzing plans rather than the forecasting engine itself.

**RevOps role**
Enterprise capacity/territory/quota-planning layer, notable for one of the more substantive official MCP implementations in this category (real read access to live planning metrics, not just a chat wrapper) despite fully enterprise-gated pricing.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: A workspace admin enables MCP under Settings > Integrations, generating a per-workspace endpoint; individual users then connect with their existing Pigment login/permissions (no separate MCP-specific key). Only Number/Integer/Boolean-type Metrics are queryable via MCP; admins can wall off sensitive data Blocks from AI/MCP access.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://www.pigment.com/ai/mcp-server](https://www.pigment.com/ai/mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.pigment.com/ai/mcp-server (developed in partnership with Anthropic); setup docs at https://kb.pigment.com/docs/mcp-server-1

- [https://www.pigment.com/ai/mcp-server](https://www.pigment.com/ai/mcp-server)
- [https://kb.pigment.com/docs/mcp-server-1](https://kb.pigment.com/docs/mcp-server-1)

**What this server exposes**

- **Tools named**: 6
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-11
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **get_ai_metrics** List AI-enabled Metrics in an Application. Returns Metric IDs and names. evidence: in the vendor docs · calling it reads · required: Application ID

- **get_applications** List all Pigment applications the user can access, with their ID, name, and description. evidence: in the vendor docs · calling it reads

- **get_metric_description** Get the structure of a Metric: name, data type, description, Dimensions (with sample Items), and Scenarios. evidence: in the vendor docs · calling it reads · required: Metric ID

- **get_organization_info** Get information about the current organization (Workspace): ID and name. evidence: in the vendor docs · calling it reads

- **query_data** Retrieve data from a single Metric using a natural-language query. One Metric per call. evidence: in the vendor docs · calling it reads · required: Metric ID

- **search** Scan and understand the entire Application logic. Advanced mode only; exposes Block metadata. evidence: in the vendor docs · calling it reads

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only in practice - no public pricing page exists (pigment.com/pricing 404s); every path leads to "Request a demo." MCP access additionally requires Pigment AI to be activated first, an extra gate on top of the base enterprise contract.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/gopigment](https://github.com/gopigment) tied to the vendor by rule 3, account website https://engineering.pigment.com/ has the vendor's domain, confidence strong

- **Public repositories**: 2, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [ai-plugins](https://github.com/gopigment/ai-plugins) | plugin or integration | Pigment plugins for AI | 18 | 2026-09-07 | |
| [protobuf-experiment](https://github.com/gopigment/protobuf-experiment) | other | A temporary fork to experiment a change | 0 | 2024-09-30 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Model a revenue plan](../jobs/model-revenue-plan.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.pigment.com](https://www.pigment.com)
- [https://www.pigment.com/ai/mcp-server](https://www.pigment.com/ai/mcp-server)
- [https://kb.pigment.com/docs/mcp-server-1](https://kb.pigment.com/docs/mcp-server-1)
- [https://www.pigment.com/use-case/revenue-growth-management](https://www.pigment.com/use-case/revenue-growth-management)
- [https://www.pigment.com/ai-info-about-pigment](https://www.pigment.com/ai-info-about-pigment)
- [https://www.pulsemcp.com/servers?q=pigment](https://www.pulsemcp.com/servers?q=pigment)

6 source URLs. Raw sources field, verbatim:

https://www.pigment.com, https://www.pigment.com/ai/mcp-server, https://kb.pigment.com/docs/mcp-server-1, https://www.pigment.com/use-case/revenue-growth-management, https://www.pigment.com/ai-info-about-pigment, https://www.pulsemcp.com/servers?q=pigment

**Notes, verbatim from the file**
Gong is a named Pigment customer using it for GTM capacity/RevOps planning - a useful "who actually uses this" data point given Gong's own entry elsewhere in this directory.

**Provenance**

- **Entry id**: 12-pigment

- **Source file**: 12-forecasting-revenue.md

- **Source line**: 188

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
