# Metorial: MCP server status, API access gate and what it does

> A hosted MCP gateway that gives AI agents/"AI employees" centralized, governed access to a company's SaaS... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Metorial

# Metorial

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07
CLI: metorial

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [metorial.com](https://metorial.com) · entry id 07-metorial · source 07-mcp-infrastructure.md line 250

**What it does**
A hosted MCP gateway that gives AI agents/"AI employees" centralized, governed access to a company's SaaS tools (Google Workspace, Microsoft 365, GitHub, Jira, Slack, Teams, Stripe, Salesforce, Zendesk, and custom internal systems) through one integration point.

**AI features, separated from automation with an AI label on it**
none in Metorial itself - it is connector/governance infrastructure for agents built elsewhere.

**RevOps role**
An enterprise-governance-flavored alternative to Composio/Pipedream - pitched at companies that want a single audited chokepoint (with tracing and access policies) for every agent-to-SaaS connection, including Salesforce.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Fully custodial - Metorial stores and centrally manages OAuth tokens for every connected integration ("no tokens to manage" for the end user), with company login handled via SSO/SAML (Okta, Azure AD, Google Workspace) and each integration isolated from the others.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://metorial.com](https://metorial.com)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/metorial/metorial ; https://metorial.com

- [https://github.com/metorial/metorial](https://github.com/metorial/metorial)
- [https://metorial.com](https://metorial.com)

**What this server exposes**

- **Tools named**: 9
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-11
- **Repo read**: metorial/metorial
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **Anthropic** `@metorial/anthropic` evidence: in a README table · calling it reads

- **DeepSeek** `@metorial/deepseek` evidence: in a README table · calling it reads

- **LangChain** `@metorial/langchain` evidence: in a README table · calling it reads

- **Mistral** `@metorial/mistral` evidence: in a README table · calling it reads

- **OpenAI** `@metorial/openai` evidence: in a README table · calling it reads

- **Provider** TypeScript adapter evidence: in a README table · calling it reads

- **PydanticAI** - evidence: in a README table · calling it reads

- **TogetherAI** `@metorial/togetherai` evidence: in a README table · calling it reads

- **XAI** `@metorial/xai` evidence: in a README table · calling it reads

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: metorial
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-11

Install, as the source shows it:

```
npm install -g @metorial/cli
```

quoted from [https://metorial.com/cli](https://metorial.com/cli) on 2026-09-11, via npm

Login or key hint seen on the page:

Easy setup

Where it was documented:

- [https://metorial.com/cli](https://metorial.com/cli) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-11.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (Metorial Dev is free - 500K tool calls/mo, 2 team members, 10 provider integrations; Metorial Scale is $250/mo - 2.5M tool calls/mo, 20 team members, unlimited integrations; Enterprise is custom, adding on-prem deployment, SOC 2/GDPR, RBAC, and SSO/SAML)

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/metorial/metorial](https://github.com/metorial/metorial)

**On GitHub**

[github.com/metorial](https://github.com/metorial) tied to the vendor by rule 1, account website https://metorial.com has the vendor's domain, confidence strong

- **Public repositories**: 35, forks excluded, as read on 2026-09-08
- **Mention MCP**: 8 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [metorial-platform](https://github.com/metorial/metorial-platform) | MCP server | The engine powering hundreds of thousands of MCP connections 🤖 🔥 | 221 | 2026-09-08 | |
| [metorial](https://github.com/metorial/metorial) | CLI | Connect any AI model to 1200+ integrations (MCP, CLI, API) | 3,351 | 2026-09-08 | |
| [outpost](https://github.com/metorial/outpost) | other | A trusted proxy and anonymization system for Metorial | 1 | 2026-09-03 | |
| [object-storage](https://github.com/metorial/object-storage) | other | A lightweight and universal object storage service. | 4 | 2026-08-26 | |
| [metorial-python](https://github.com/metorial/metorial-python) | SDK | Official Python SDK for the Metorial API 🐍 📡 | 11 | 2026-08-14 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://metorial.com](https://metorial.com)
- [https://metorial.com/pricing](https://metorial.com/pricing)
- [https://github.com/metorial/metorial](https://github.com/metorial/metorial)

3 source URLs. Raw sources field, verbatim:

https://metorial.com, https://metorial.com/pricing, https://github.com/metorial/metorial

**Notes, verbatim from the file**
Metorial is explicitly and fully custodial of OAuth tokens across every connected app - the entire pitch is "no tokens to manage" because Metorial manages them centrally. That is a meaningfully bigger trust concentration than Zapier MCP (reuses Zapier's existing per-app OAuth) or Anthropic's directory (per-connector, third-party-operated) - worth flagging to anyone evaluating it for a Salesforce/finance-adjacent connection. 2026-09-07: GitHub org metorial (homepage metorial.com), repo metorial, 3,351 stars, pushed 2026-09-07 (https://github.com/metorial/metorial).

**Provenance**

- **Entry id**: 07-metorial

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 250

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
