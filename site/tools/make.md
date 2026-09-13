# Make: MCP server status, API access gate and what it does

> A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent... Official MCP, Paid, self-serve. Checked 2026-09-07.

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
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [make.com](https://make.com) · entry id 06-make · source 06-revops-infra.md line 171

**What it does**
A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent and natural-language-build features layered on top.

**AI features, separated from automation with an AI label on it**
Make AI Agents genuinely use an LLM to reason, choose what to do next, and trigger real workflows, and can analyze unstructured text/documents - but Make's own docs frame agents as operating "alongside deterministic logic, not instead of it," built/debugged inside the same visual scenario canvas with manual approvals or hard stops available. Closer to LLM-reasoning-nodes embedded in classic automation than a fully autonomous runtime. "Maia by Make" is a separate natural-language scenario builder (LLM-assisted authoring, not autonomous execution).

**RevOps role**
Same class as Zapier - integration/orchestration layer for a GTM stack; ships both an MCP Server (expose Make scenarios as tools to Claude/ChatGPT/Cursor) and an MCP Client (let Make scenarios consume external MCP servers), a more complete two-way implementation than most competitors here.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Two supported methods - OAuth via Make's cloud (endpoint mcp.make.com) or an MCP Token generated from the user's Make profile, sent as a Bearer token to a per-zone stateless-HTTP endpoint (SSE transport also supported).

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://developers.make.com/mcp-server](https://developers.make.com/mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.make.com ; https://developers.make.com/mcp-server ; repo https://github.com/integromat/make-mcp-server

- [https://mcp.make.com](https://mcp.make.com)
- [https://developers.make.com/mcp-server](https://developers.make.com/mcp-server)
- [https://github.com/integromat/make-mcp-server](https://github.com/integromat/make-mcp-server)

**What this server exposes**

What this server exposes is the customer's own workspace, not a fixed catalogue the vendor publishes. No tool list is the correct answer here rather than a gap, and the harvest recorded it as one.

Recorded by the harvest: each customer's own Make scenarios become the tools

The count below still carries this entry on the unmeasured side, because there is no list to record. That is a different thing from a server nobody has read, and both are published rather than blended.

119 of the 264 entries that record an official or community MCP server carry a harvested tool list. The other 145 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid for full access - scenario-run tools are available on all plans including Free, but management tools require a paid plan (Core, from $12/mo).

**API documentation**

No documentation URL recorded.

400 of 514 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/integromat/make-mcp-server](https://github.com/integromat/make-mcp-server)

**On GitHub**

[github.com/integromat](https://github.com/integromat) tied to the vendor by rule 2, account website https://www.make.com has the vendor's domain, confidence strong

- **Public repositories**: 26, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [make-typescript-sdk](https://github.com/integromat/make-typescript-sdk) | SDK | Make TypeScript SDK | 14 | 2026-09-08 | v1.6.15 |
| [make-skills](https://github.com/integromat/make-skills) | other | Make Skills | 98 | 2026-09-07 | |
| [make-white-label-documentation](https://github.com/integromat/make-white-label-documentation) | docs or examples | Source of content for white label documentation in GitBook; https://developers.make.com/white-label-documentation | 0 | 2026-09-07 | |
| [make-forman-schema](https://github.com/integromat/make-forman-schema) | other | Make Forman Schema Tools | 0 | 2026-09-02 | v2.0.1 |
| [vscode-apps-sdk](https://github.com/integromat/vscode-apps-sdk) | SDK | Integromat Apps SDK plugin for Visual Studio Code | 51 | 2026-08-31 | 2.8.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 514 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.make.com/en/pricing](https://www.make.com/en/pricing)
- [https://www.make.com/en/ai-agents](https://www.make.com/en/ai-agents)
- [https://developers.make.com/mcp-server](https://developers.make.com/mcp-server)
- [https://github.com/integromat/make-mcp-server](https://github.com/integromat/make-mcp-server)
- [https://mcp.make.com](https://mcp.make.com)

5 source URLs. Raw sources field, verbatim:

https://www.make.com/en/pricing, https://www.make.com/en/ai-agents, https://developers.make.com/mcp-server, https://github.com/integromat/make-mcp-server, https://mcp.make.com

**Notes, verbatim from the file**
none. 2026-09-07: Integromat is Make's own GitHub org (Make was formerly Integromat). Repo make-mcp-server, 171 stars, README: "Make MCP Server (legacy) ... A Model Context Protocol server that enables Make scenarios to be utilized as tools by AI assistants," and it points at the newer cloud version at developers.make.com/mcp-server (https://github.com/integromat/make-mcp-server).

**Provenance**

- **Entry id**: 06-make

- **Source file**: 06-revops-infra.md

- **Source line**: 171

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
