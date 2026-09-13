# Cargo: MCP server status, API access gate and what it does

> A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Cargo

# Cargo

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24
CLI: cargo

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [getcargo.ai](https://getcargo.ai) · entry id 06-cargo · source 06-revops-infra.md line 195

**What it does**
A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment, scoring, routing, CRM sync - as code, run by AI agents.

**AI features, separated from automation with an AI label on it**
Genuinely agent-based - ships "Cargo Skills," 17 defined agent skills (sourcing, enrichment, scoring, research, routing) usable directly inside Claude Code, Codex, and Cursor, with autonomous execution for routine tasks and human-approval gates for nuanced decisions. Closer to a GTM-specific agent framework than point-and-click automation.

**RevOps role**
Positions itself as the connective/execution layer between fragmented sales, marketing, and finance tools - closer to a GTM automation warehouse-plus-agents than a point tool; integrates with a data warehouse rather than owning its own store.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown for the MCP layer specifically - docs confirm the capability but not its auth mechanism. Cargo's separate REST API (api.getcargo.io/v1) uses OAuth 2.0 with device-code and PKCE flows.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.getcargo.ai/](https://docs.getcargo.ai/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.getcargo.ai/ (defineMcpServer is a native, first-party part of Cargo's workspace/CDK framework; a dedicated /mcp docs page returned HTTP 405 rather than content)

- [https://docs.getcargo.ai/](https://docs.getcargo.ai/)

**What this server exposes**

What this server exposes is the customer's own workspace, not a fixed catalogue the vendor publishes. No tool list is the correct answer here rather than a gap, and the harvest recorded it as one.

Recorded by the harvest: the customer's own Cargo workflows become the tools

The count below still carries this entry on the unmeasured side, because there is no list to record. That is a different thing from a server nobody has read, and both are published rather than blended.

119 of the 239 entries that record an official or community MCP server carry a harvested tool list. The other 120 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: cargo
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @cargo-ai/cli
```

quoted from [https://docs.getcargo.ai/cli/overview](https://docs.getcargo.ai/cli/overview) on 2026-09-12, via npm

```
npx @cargo-ai/cli
```

quoted from [https://docs.getcargo.ai/cli/overview](https://docs.getcargo.ai/cli/overview) on 2026-09-12, via npx

Login or key hint seen on the page:

cargo-ai login --token
- [npm: @cargo-ai/cli 1.0.91](https://www.npmjs.com/package/@cargo-ai/cli)

Where it was documented:

- [https://docs.getcargo.ai/cli/overview](https://docs.getcargo.ai/cli/overview) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - a genuine self-serve free tier (100 credits/mo, no card required, CLI signup via email); paid tiers start at Starter $165/mo, with "no feature lock" suggesting API/CLI access isn't paywalled.

**API documentation**

No documentation URL recorded.

347 of 422 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/getcargohq](https://github.com/getcargohq)
- [https://github.com/getcargohq/cargo-skills](https://github.com/getcargohq/cargo-skills)

**On GitHub**

[github.com/getcargohq](https://github.com/getcargohq) tied to the vendor by rule 2, account name 'Cargo' equals the entry's display name, confidence check

- **Public repositories**: 5, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [gtm-skills](https://github.com/getcargohq/gtm-skills) | other | Standalone Cargo GTM agent skills - one job each. Find leads, enrich contacts, verify emails, track signals. | 3 | 2026-09-07 | |
| [cargo-skills](https://github.com/getcargohq/cargo-skills) | CLI | GTM engineering skills for AI coding agents - build lead lists, find & verify emails, waterfall enrichment, lead... | 17 | 2026-09-05 | |
| [cargo-manifest](https://github.com/getcargohq/cargo-manifest) | other | The software factory for go-to-market. An open-source monorepo holding your company context (ICP, personas, plays,... | 6 | 2026-09-03 | |
| [cargo-partner-skills](https://github.com/getcargohq/cargo-partner-skills) | other | | 0 | 2026-08-19 | |
| [dummy-integration](https://github.com/getcargohq/dummy-integration) | plugin or integration | | 2 | 2026-01-13 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Route an inbound lead](../jobs/route-inbound-lead.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 422 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.ycombinator.com/companies/cargo](https://www.ycombinator.com/companies/cargo)
- [https://www.getcargo.ai/](https://www.getcargo.ai/)
- [https://www.getcargo.ai/pricing](https://www.getcargo.ai/pricing)
- [https://docs.getcargo.ai/](https://docs.getcargo.ai/)
- [https://github.com/getcargohq](https://github.com/getcargohq)
- [https://github.com/getcargohq/cargo-skills](https://github.com/getcargohq/cargo-skills)

6 source URLs. Raw sources field, verbatim:

https://www.ycombinator.com/companies/cargo, https://www.getcargo.ai/, https://www.getcargo.ai/pricing, https://docs.getcargo.ai/, https://github.com/getcargohq, https://github.com/getcargohq/cargo-skills

**Notes, verbatim from the file**
DOMAIN CORRECTION - cargo.so does not resolve (DNS failure, confirmed by multiple direct fetch attempts). The real company matching this brief (YC S23, founders ex-Spendesk) is at getcargo.ai / getcargo.io. Cargo's GitHub org (github.com/getcargohq) has 5 public repos but no standalone "MCP server" repo - MCP is a feature inside the core product/docs, not a separate open-source connector. 2026-09-07: LAW 1 FLAG, NOT DOWNGRADED. What the official claim actually rests on: defineMcpServer inside Cargo's own CDK, a framework feature documented at docs.getcargo.ai, not a separate repo or a callable endpoint. The finder searched GitHub (owners getcargo, getcargo-ai, cargo-ai), npm, PyPI and the official registry and probed https://mcp.getcargo.ai/ and /mcp with no result. A human should decide whether official survives law 1. 2026-09-09 (P6-04 repo sweep): first-party repository recorded at https://github.com/getcargohq/cargo-skills, the org getcargohq, 17 stars, last push 2026-09-05. Its README names the hosted-MCP-server skill cargo-mcp and calls MCP the hosted server, the one surface that is not the CLI, so the repo documents and wires the hosted server rather than containing its source. No public server source was found.

**Provenance**

- **Entry id**: 06-cargo

- **Source file**: 06-revops-infra.md

- **Source line**: 195

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
