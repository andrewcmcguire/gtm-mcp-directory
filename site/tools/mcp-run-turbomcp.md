# mcp.run / TurboMCP: MCP server status, API access gate and what it does

> An enterprise self-hosted MCP gateway and management platform  - a trusted, admin-curated registry plus... Official MCP, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
mcp.run / TurboMCP

# mcp.run / TurboMCP

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [turbomcp.ai (mcp.run now 301-redirects here)](https://turbomcp.ai (mcp.run now 301-redirects here)) · entry id 07-mcp-run-turbomcp · source 07-mcp-infrastructure.md line 75

**What it does**
An enterprise self-hosted MCP gateway and management platform - a trusted, admin-curated registry plus RBAC-controlled deployment of MCP servers across a team's own infrastructure (K8s, PaaS, VMs).

**AI features, separated from automation with an AI label on it**
none - this is a gateway/governance layer for MCP traffic, not an AI product.

**RevOps role**
Relevant to a RevOps/IT team that wants centralized control over which MCP servers its agents can reach, rather than an individual operator's connector of choice.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Integrates with a team's own OIDC-compatible identity provider; handles OAuth and Dynamic Client Registration for the servers it fronts.

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official (this is infrastructure for running/gating other servers' MCP endpoints, not a single server itself)

mcp_url, verbatim from the file:

https://turbomcp.ai

- [https://turbomcp.ai](https://turbomcp.ai)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown (pricing not disclosed on the fetched page)

83 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Discover MCP servers](../jobs/discover-mcp-servers.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.mcp.run](https://www.mcp.run)
- [https://turbomcp.ai](https://turbomcp.ai)
- (redirects to turbomcp.ai, confirmed 301)

2 source URLs. Raw sources field, verbatim:

https://www.mcp.run (redirects to turbomcp.ai, confirmed 301), https://turbomcp.ai

**Notes, verbatim from the file**
mcp.run - originally a lightweight community MCP server registry - now redirects permanently to TurboMCP, an enterprise self-hosted gateway product. The fetched TurboMCP page does not mention its mcp.run history, so the nature/terms of that transition are unconfirmed; flagged as a gap rather than guessed.

**Provenance**

- **Entry id**: 07-mcp-run-turbomcp

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 75

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
