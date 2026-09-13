# Composio: MCP server status, API access gate and what it does

> A hosted integration/auth platform that lets AI agents and MCP clients call actions across 1,000+ SaaS apps... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Composio

# Composio

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07
CLI: composio

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [composio.dev](https://composio.dev) · entry id 07-composio · source 07-mcp-infrastructure.md line 11

**What it does**
A hosted integration/auth platform that lets AI agents and MCP clients call actions across 1,000+ SaaS apps (HubSpot, Slack, Gmail, GitHub, Notion, Stripe, and others) through Composio-managed OAuth.

**AI features, separated from automation with an AI label on it**
none in Composio itself - it is tool/auth plumbing that any LLM or agent framework (Claude, GPT, LangChain, CrewAI, or a raw MCP client) calls into. The "AI" is whichever agent is on the other end, not something Composio adds.

**RevOps role**
The connector layer a solo RevOps engineer reaches for instead of hand-building OAuth + API wrappers for a dozen GTM tools one at a time.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Composio brokers OAuth for each connected toolkit (HubSpot, Gmail, Slack, etc.) on the user's behalf, then gates the MCP endpoint itself with an x-api-key header (required by default for new orgs). MCP endpoint pattern is https://backend.composio.dev/v3/mcp/{server_id}?user_id={user_id}.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.composio.dev/docs/single-toolkit-mcp](https://docs.composio.dev/docs/single-toolkit-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://connect.composio.dev/mcp ; https://docs.composio.dev/docs/single-toolkit-mcp (redirect correction 2026-08-28: the address previously recorded here, docs.composio.dev/mcp/overview, 308s to this one and this one returns 200) ; repo https://github.com/ComposioHQ/GHMCP

- [https://connect.composio.dev/mcp](https://connect.composio.dev/mcp)
- [https://docs.composio.dev/docs/single-toolkit-mcp](https://docs.composio.dev/docs/single-toolkit-mcp)
- [https://github.com/ComposioHQ/GHMCP](https://github.com/ComposioHQ/GHMCP)

**What this server exposes**

- **Tools named**: 6
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: the customer's own workspace, not a fixed catalogue

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

Recorded by the harvest: a small fixed meta-tool set plus the customer's own connected toolkits

- **COMPOSIO_GET_TOOL_SCHEMAS** Retrieves schema definitions for specified tools to validate their input/output structure. evidence: in the vendor docs · calling it reads · required: tool_slugs · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **COMPOSIO_MANAGE_CONNECTIONS** Checks or connects toolkits by slug so the agent can authenticate before calling their tools. evidence: in the vendor docs · calling it reads · required: toolkits · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **COMPOSIO_MULTI_EXECUTE_TOOL** Executes multiple logically independent tools in parallel with consolidated response tracking. evidence: in the vendor docs · calling it reads · required: tools, tool_slug, arguments, sync_response_to_workbench · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **COMPOSIO_REMOTE_BASH_TOOL** Executes bash commands in a sandbox environment with a 3-minute execution limit. evidence: in the vendor docs · calling it reads · required: command · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **COMPOSIO_REMOTE_WORKBENCH** Executes Python code in a persistent remote Jupyter sandbox with state preservation across executions. evidence: in the vendor docs · calling it reads · required: code_to_execute · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **COMPOSIO_SEARCH_TOOLS** Processes structured English search queries to discover and return relevant tools from Composio's toolkit ecosystem in parallel. evidence: in the vendor docs · calling it reads · required: queries, session · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

119 of the 359 entries that record an official or community MCP server carry a harvested tool list. The other 240 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: composio
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
curl -fsSL https://composio.dev/install | bash
```

quoted from [https://composio.dev/cli](https://composio.dev/cli) on 2026-09-12, via shell

```
curl -fsSL https://composio.dev/install | sh
```

quoted from [https://docs.composio.dev/docs/cli](https://docs.composio.dev/docs/cli) on 2026-09-12, via shell

```
curl -fsSL https://composio.dev/install | sh -s -- @composio/cli@0.3.1
```

quoted from [https://docs.composio.dev/docs/cli](https://docs.composio.dev/docs/cli) on 2026-09-12, via shell

Login or key hint seen on the page:

composio login --agent

Subcommands seen with the binary:

dev, execute, generate, link, links, login, proxy, run, search, setup, start, upgrade

Where it was documented:

- [https://composio.dev/cli](https://composio.dev/cli) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (100K tool calls/mo, 50K trigger events/mo, unlimited connections on the Free plan, no credit card)

**API documentation**

No documentation URL recorded.

510 of 739 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/ComposioHQ/GHMCP](https://github.com/ComposioHQ/GHMCP)

**On GitHub**

[github.com/ComposioHQ](https://github.com/ComposioHQ) tied to the vendor by rule 2, account website https://composio.dev has the vendor's domain, confidence strong

- **Public repositories**: 14, forks excluded, as read on 2026-09-08
- **Mention MCP**: 4 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [composio](https://github.com/ComposioHQ/composio) | MCP server | Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you... | 30,092 | 2026-09-08 | @composio/cli@0.4.2-beta.384 |
| [logo-cdn](https://github.com/ComposioHQ/logo-cdn) | other | oss logo cdn of composio toolkits | 7 | 2026-09-08 | |
| [helm-charts](https://github.com/ComposioHQ/helm-charts) | infrastructure | Helm charts to deploy Composio | 2 | 2026-09-07 | r20260908_01 |
| [composio-base-py](https://github.com/ComposioHQ/composio-base-py) | SDK | | 3 | 2026-08-19 | v1.44.0 |
| [composio-plugin-openai](https://github.com/ComposioHQ/composio-plugin-openai) | plugin or integration | | 4 | 2026-08-11 | v0.2.3 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 739 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://composio.dev](https://composio.dev)
- [https://composio.dev/pricing](https://composio.dev/pricing)
- [https://docs.composio.dev/docs/single-toolkit-mcp](https://docs.composio.dev/docs/single-toolkit-mcp)
- [https://github.com/ComposioHQ/GHMCP](https://github.com/ComposioHQ/GHMCP)
- [https://connect.composio.dev/mcp](https://connect.composio.dev/mcp)

5 source URLs. Raw sources field, verbatim:

https://composio.dev, https://composio.dev/pricing, https://docs.composio.dev/docs/single-toolkit-mcp, https://github.com/ComposioHQ/GHMCP, https://connect.composio.dev/mcp

**Notes, verbatim from the file**
Composio holds the OAuth tokens for every connected toolkit - it is a custodial broker, not a pass-through. Pro tier ($29/mo) adds pay-as-you-scale overage at $0.0003/tool call; Enterprise adds SSO/SCIM and a KMS proxy for teams that don't want Composio holding raw tokens. 2026-09-07: GitHub org ComposioHQ; repo GHMCP holds the server.json registry manifest and a publish-mcp workflow, and its README reads "Composio MCP Server ... Composio is a remote, streamable-HTTP MCP server ... https://connect.composio.dev/mcp" (https://github.com/ComposioHQ/GHMCP).

**Provenance**

- **Entry id**: 07-composio

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 11

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
