# Pipedream MCP: MCP server status, API access gate and what it does

> Pipedream's existing workflow/integration platform re-exposed as hosted MCP servers, giving an MCP client... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Pipedream MCP

# Pipedream MCP

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [pipedream.com](https://pipedream.com) · entry id 07-pipedream-mcp · source 07-mcp-infrastructure.md line 35

**What it does**
Pipedream's existing workflow/integration platform re-exposed as hosted MCP servers, giving an MCP client access to 3,000+ connected apps and 10,000+ pre-built tools via Pipedream Connect.

**AI features, separated from automation with an AI label on it**
none in Pipedream itself - same pattern as Composio, it is connector infrastructure an external LLM/agent calls into, not a model or agent of its own.

**RevOps role**
Same slot as Composio - a hosted connector layer, notable for breadth (3,000+ apps) rather than GTM-specific depth.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth/API-key credentials for each underlying app are stored by Pipedream and isolated per end user; Pipedream states credentials are "never exposed to AI models or client-side code" and all calls route server-side through its infrastructure.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://mcp.pipedream.com](https://mcp.pipedream.com)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.pipedream.com

- [https://mcp.pipedream.com](https://mcp.pipedream.com)

**What this server exposes**

- **Tools named**: 1
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: the customer's own workspace, not a fixed catalogue

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

Recorded by the harvest: the tools are the customer's own connected accounts and actions

- **CONFIGURE_COMPONENT** Retrieve configuration values for dynamic properties of a component. evidence: in the vendor docs · calling it reads · required: key, propName · read off pipedream, an aggregator wrapping the vendor's API rather than the vendor's own server

119 of the 415 entries that record an official or community MCP server carry a harvested tool list. The other 296 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (free for personal use and development; a paid plan is required once you deploy to production)

**API documentation**

No documentation URL recorded.

582 of 884 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/PipedreamHQ/mcp-chat](https://github.com/PipedreamHQ/mcp-chat)

**On GitHub**

[github.com/PipedreamHQ](https://github.com/PipedreamHQ) tied to the vendor by rule 3, account website https://pipedream.com has the vendor's domain, confidence strong

- **Public repositories**: 24, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [pipedream](https://github.com/PipedreamHQ/pipedream) | CLI | Connect APIs, remarkably fast. Free for developers. | 11,680 | 2026-09-08 | |
| [pipedream-sdk-java](https://github.com/PipedreamHQ/pipedream-sdk-java) | SDK | Java SDK for Pipedream | 2 | 2026-09-03 | v2.1.3 |
| [pipedream-sdk-python](https://github.com/PipedreamHQ/pipedream-sdk-python) | SDK | Python SDK for Pipedream | 14 | 2026-09-03 | v2.1.20 |
| [pipedream-sdk-typescript](https://github.com/PipedreamHQ/pipedream-sdk-typescript) | SDK | TypeScript SDK for Pipedream | 9 | 2026-09-03 | v3.1.6 |
| [pipedream-connect-examples](https://github.com/PipedreamHQ/pipedream-connect-examples) | docs or examples | Collection of example apps showcasing the pipedream SDKs. Learn more https://pipedream.com/docs/connect. | 28 | 2026-08-20 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 884 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://mcp.pipedream.com](https://mcp.pipedream.com)
- [https://pipedream.com/docs/connect/mcp](https://pipedream.com/docs/connect/mcp)
- [https://github.com/PipedreamHQ/mcp-chat](https://github.com/PipedreamHQ/mcp-chat)

3 source URLs. Raw sources field, verbatim:

https://mcp.pipedream.com, https://pipedream.com/docs/connect/mcp, https://github.com/PipedreamHQ/mcp-chat

**Notes, verbatim from the file**
Pipedream is custodial like Composio - it stores end-user credentials server-side rather than passing them through. Could not confirm exact production-tier pricing numbers in this pass (pricing docs page 404'd); marked unknown rather than guessed. GTM apps (Salesforce, HubSpot) were not explicitly named in the fetched docs, only implied by the "3,000+ apps" breadth claim. 2026-09-09 (P6-04 repo sweep): first-party repository recorded at https://github.com/PipedreamHQ/mcp-chat, the org PipedreamHQ (profile site pipedream.com), 192 stars, last push 2026-05-08. It is NOT the server source: the README describes an open-source reference chat app built on Pipedream's MCP server. The npm package @pipedream/mcp ("Pipedream stdio and SSE MCP servers") declares no repository, and a contents read of the PipedreamHQ/pipedream monorepo on 2026-09-09 found no modelcontextprotocol directory under the root or under packages/, so no public server source was found.

**Provenance**

- **Entry id**: 07-pipedream-mcp

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 35

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
