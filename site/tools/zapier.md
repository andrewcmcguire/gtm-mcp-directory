# Zapier: MCP server status, API access gate and what it does

> A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Zapier

# Zapier

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [zapier.com](https://zapier.com) · entry id 06-zapier · source 06-revops-infra.md line 142

**What it does**
A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate agent product.

**AI features, separated from automation with an AI label on it**
Two distinct tiers. Classic Zaps are deterministic trigger-action automations - not AI. Zapier Agents are genuinely LLM-driven: built with a Copilot, they run autonomously ("on command and while you sleep"), reason over business context/documents, retry different approaches, and can escalate to a human - real agentic behavior, not relabeled workflow logic.

**RevOps role**
General-purpose integration/automation backbone connecting CRM, marketing, and sales tools; increasingly positioned as an agent-orchestration layer that can act across a RevOps stack, not just move data.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Reuses Zapier's existing 13+ year credential infrastructure - connect an AI client (Claude, ChatGPT, Cursor) through a guided ~5-minute flow that auto-imports app connections already authorized on the account; effectively OAuth/account-login-style rather than a bare API key.

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://zapier.com/mcp (connection endpoint https://mcp.zapier.com)

- [https://zapier.com/mcp](https://zapier.com/mcp)
- [https://mcp.zapier.com](https://mcp.zapier.com)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - MCP/AI-product access is included on all plans including Free (100 tasks/mo); each MCP action consumes 2 tasks from the normal quota.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://zapier.com/mcp](https://zapier.com/mcp)
- [https://zapier.com/agents](https://zapier.com/agents)
- [https://zapier.com/pricing](https://zapier.com/pricing)

3 source URLs. Raw sources field, verbatim:

https://zapier.com/mcp, https://zapier.com/agents, https://zapier.com/pricing

**Notes, verbatim from the file**
Zapier's own stated scale claims (195,000+ MCP servers created, 4.6M+ tool calls, 250,000+ apps connected) are vendor-reported, not independently verified.

**Provenance**

- **Entry id**: 06-zapier

- **Source file**: 06-revops-infra.md

- **Source line**: 142

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
