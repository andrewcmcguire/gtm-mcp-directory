# Zapier: MCP server status, API access gate and what it does

> A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Zapier

# Zapier

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07
CLI: zapier-platform

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [zapier.com](https://zapier.com) · entry id 06-zapier · source 06-revops-infra.md line 146

**What it does**
A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate agent product.

**AI features, separated from automation with an AI label on it**
Two distinct tiers. Classic Zaps are deterministic trigger-action automations - not AI. Zapier Agents are genuinely LLM-driven: built with a Copilot, they run autonomously ("on command and while you sleep"), reason over business context/documents, retry different approaches, and can escalate to a human - real agentic behavior, not relabeled workflow logic.

**RevOps role**
General-purpose integration/automation backbone connecting CRM, marketing, and sales tools; increasingly positioned as an agent-orchestration layer that can act across a RevOps stack, not just move data.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Reuses Zapier's existing 13+ year credential infrastructure - connect an AI client (Claude, ChatGPT, Cursor) through a guided ~5-minute flow that auto-imports app connections already authorized on the account; effectively OAuth/account-login-style rather than a bare API key.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://zapier.com/mcp](https://zapier.com/mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.zapier.com/api/v1/connect ; https://zapier.com/mcp (connection endpoint https://mcp.zapier.com) ; repo https://github.com/zapier/zapier-mcp

- [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect)
- [https://zapier.com/mcp](https://zapier.com/mcp)
- [https://mcp.zapier.com](https://mcp.zapier.com)
- [https://github.com/zapier/zapier-mcp](https://github.com/zapier/zapier-mcp)

**What this server exposes**

What this server exposes is the customer's own workspace, not a fixed catalogue the vendor publishes. No tool list is the correct answer here rather than a gap, and the harvest recorded it as one.

Recorded by the harvest: every tool is one of the customer's own connected Zaps

The count below still carries this entry on the unmeasured side, because there is no list to record. That is a different thing from a server nobody has read, and both are published rather than blended.

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-09. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: zapier-platform
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-09

Install, as the source shows it:

```
npx zapier
```

quoted from [https://zapier.com/sdk](https://zapier.com/sdk) on 2026-09-09, via npx

```
npm install -g zapier-platform-cli
```

quoted from [https://www.npmjs.com/package/zapier-platform-cli](https://www.npmjs.com/package/zapier-platform-cli) on 2026-09-09, via npm

```
npm install -g @zapier/zapier-sdk-cli
```

quoted from [https://www.npmjs.com/package/@zapier/zapier-sdk-cli](https://www.npmjs.com/package/@zapier/zapier-sdk-cli) on 2026-09-09, via npm

Login or key hint seen on the page:

handles auth

Packages seen, with the version on 2026-09-09:

- [npm: zapier-platform-cli 19.1.0](https://www.npmjs.com/package/zapier-platform-cli)
- [npm: @zapier/zapier-sdk-cli 0.82.0](https://www.npmjs.com/package/@zapier/zapier-sdk-cli)

Where it was documented:

- [https://zapier.com/sdk](https://zapier.com/sdk) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-09.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - MCP/AI-product access is included on all plans including Free (100 tasks/mo); each MCP action consumes 2 tasks from the normal quota.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/zapier/zapier-mcp](https://github.com/zapier/zapier-mcp)

**On GitHub**

[github.com/zapier](https://github.com/zapier) tied to the vendor by rule 2, account website https://zapier.com has the vendor's domain, confidence strong

- **Public repositories**: 82, forks excluded, as read on 2026-09-08
- **Mention MCP**: 5 of them
- **Look like CLIs**: 5 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [zapier-platform](https://github.com/zapier/zapier-platform) | CLI | The toolkit for you to build an integration on Zapier | 551 | 2026-09-08 | |
| [kubechecks](https://github.com/zapier/kubechecks) | infrastructure | Check your Kubernetes changes before they hit the cluster | 612 | 2026-09-02 | v3.4.0 |
| [connectors](https://github.com/zapier/connectors) | CLI | Connect your agent to the apps you already use - with or without Zapier. | 164 | 2026-08-25 | |
| [agent-skills](https://github.com/zapier/agent-skills) | other | Agent skills for working with Zapier, maintained by Zapier teams. Indexed by skills.sh. | 17 | 2026-08-25 | |
| [marketplace](https://github.com/zapier/marketplace) | CLI | Install Zapier in your coding agent via the Claude Code, Codex, and Copilot CLI marketplaces. | 13 | 2026-08-11 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://zapier.com/mcp](https://zapier.com/mcp)
- [https://zapier.com/agents](https://zapier.com/agents)
- [https://zapier.com/pricing](https://zapier.com/pricing)
- [https://github.com/zapier/zapier-mcp](https://github.com/zapier/zapier-mcp)
- [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect)

5 source URLs. Raw sources field, verbatim:

https://zapier.com/mcp, https://zapier.com/agents, https://zapier.com/pricing, https://github.com/zapier/zapier-mcp, https://mcp.zapier.com/api/v1/connect

**Notes, verbatim from the file**
Zapier's own stated scale claims (195,000+ MCP servers created, 4.6M+ tool calls, 250,000+ apps connected) are vendor-reported, not independently verified. 2026-09-07: GitHub org zapier, repo zapier-mcp, 405 stars: "Official plugin distribution for the hosted Zapier MCP server." The official registry carries com.zapier/mcp (DNS-verified zapier.com namespace) pointing at this repo with remote https://mcp.zapier.com/api/v1/connect, which returned 401 to an MCP initialize (https://github.com/zapier/zapier-mcp).

**Provenance**

- **Entry id**: 06-zapier

- **Source file**: 06-revops-infra.md

- **Source line**: 146

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-09

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
