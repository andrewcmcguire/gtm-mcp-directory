# Microsoft Dynamics 365 Sales: MCP server status, API access gate and what it does

> Microsoft's enterprise CRM for sales, built on Dataverse and the Power Platform, covering leads,... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Microsoft Dynamics 365 Sales

# Microsoft Dynamics 365 Sales

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [microsoft.com/dynamics-365](https://microsoft.com/dynamics-365) · entry id 06-microsoft-dynamics-365-sales · source 06-revops-infra.md line 531

**What it does**
Microsoft's enterprise CRM for sales, built on Dataverse and the Power Platform, covering leads, opportunities, accounts and forecasting, with a first-party MCP server that lets Copilot Studio agents and other MCP clients qualify leads, research opportunities and read and write Dataverse records.

**AI features, separated from automation with an AI label on it**
Substantial and native: Copilot inside Dynamics writes summaries and email drafts, and Microsoft ships named agents (Sales Qualification, Sales Opportunity, Sales Research, and Sales Close in preview) that run on Copilot Credits. The MCP server is the interface that lets an outside agent reach the same data, not itself an AI feature.

**RevOps role**
System of record for Microsoft-standardised enterprise sales orgs, and through MCP the point at which an external agent can read and write the pipeline directly rather than through a middleware sync.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: enterprise gate. Microsoft Entra identity; the documented prerequisites are admin permissions in Dynamics 365 Sales, admin permissions in Copilot Studio, an environment-level allowance for non-Copilot-Studio MCP clients to reach the Dataverse MCP server, and enough Copilot Studio credits to cover the tool calls.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://agent365.svc.cloud.microsoft/mcp/environments//servers/msdyn_SalesMCPServer for the Sales server, plus https:///api/mcp for the Dataverse server (docs: https://learn.microsoft.com/en-us/dynamics365/sales/connect-agents-to-model-context-protocol)

- [https://agent365.svc.cloud.microsoft/mcp/environments/](https://agent365.svc.cloud.microsoft/mcp/environments/)
- [https://learn.microsoft.com/en-us/dynamics365/sales/connect-agents-to-model-context-protocol](https://learn.microsoft.com/en-us/dynamics365/sales/connect-agents-to-model-context-protocol)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 106 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - Microsoft publishes per-seat prices with a self-serve "Buy now" path for the two lower tiers: Dynamics 365 Sales Professional at "$65.00 user/month, paid yearly" and Sales Enterprise Edition at "$105.00 user/month, paid yearly", with Sales Premium at "$150.00 user/month, paid yearly" routed to "Contact us". The MCP path costs more than a licence, because it additionally consumes Copilot Studio credits per tool call and requires tenant admin rights the buyer may not hold.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/microsoft](https://github.com/microsoft) tied to the vendor by rule 3, account website https://opensource.microsoft.com has the vendor's domain, confidence strong

- **Public repositories**: 148, forks excluded, as read on 2026-09-08
- **Mention MCP**: 4 of them
- **Look like CLIs**: 8 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [winget-pkgs](https://github.com/microsoft/winget-pkgs) | other | The Microsoft community Windows Package Manager manifest repository | 11,059 | 2026-09-08 | |
| [aspire](https://github.com/microsoft/aspire) | other | Aspire is the tool for code-first, extensible, observable dev and deploy. | 6,290 | 2026-09-08 | v13.5.3 |
| [LakeBench](https://github.com/microsoft/LakeBench) | other | A multi-modal Python library for benchmarking lakehouse engines and ELT scenarios, supporting both industry-standard... | 52 | 2026-09-08 | v1.2.0 |
| [playwright](https://github.com/microsoft/playwright) | other | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single... | 95,815 | 2026-09-08 | v1.63.0 |
| [vscode](https://github.com/microsoft/vscode) | other | Visual Studio Code | 191,494 | 2026-09-08 | 1.136.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://learn.microsoft.com/en-us/dynamics365/sales/connect-agents-to-model-context-protocol](https://learn.microsoft.com/en-us/dynamics365/sales/connect-agents-to-model-context-protocol)
- [https://www.microsoft.com/en-us/dynamics-365/products/sales/pricing](https://www.microsoft.com/en-us/dynamics-365/products/sales/pricing)

2 source URLs. Raw sources field, verbatim:

https://learn.microsoft.com/en-us/dynamics365/sales/connect-agents-to-model-context-protocol, https://www.microsoft.com/en-us/dynamics-365/products/sales/pricing

**Notes, verbatim from the file**
Verified 2026-09-07 from Microsoft Learn. The endpoints are tenant-specific templates, not a shared host, so there is nothing to probe without an environment ID and this entry carries no liveness probe result; that is a property of the design, not a gap in the research. The single most useful line for this directory's readers is in Microsoft's own prerequisites: "Claude Desktop isn't supported at this time." A Microsoft-shaped MCP server that the most widely used MCP client cannot reach is the sharpest available illustration of MCP support being a spectrum rather than a yes or no. The docs give a working mcp.json example pairing both servers, and note that CRUD on Dataverse records requires connecting the Dataverse MCP server as well as the Sales one, so an agent needs two connections to do what a rep does in one screen. Copilot Credit consumption is per tool and documented in a separate Microsoft rate table, so cost scales with agent chattiness rather than with seats. 2026-09-07: the Agent 365 endpoint is per-tenant and templated (https://agent365.svc.cloud.microsoft/mcp/environments/<EnvironmentID>/servers/msdyn_SalesMCPServer), so no capability harvest can ever enumerate its tools without a customer EnvironmentID. The route itself is confirmed real (HTTP 400 with an MCP-shaped error to a probe carrying a placeholder environment id). DO NOT RE-INVESTIGATE: this entry is permanently unharvestable from outside a tenant.

**Provenance**

- **Entry id**: 06-microsoft-dynamics-365-sales

- **Source file**: 06-revops-infra.md

- **Source line**: 531

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
