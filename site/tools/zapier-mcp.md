# Zapier MCP: MCP server status, API access gate and what it does

> Zapier's own MCP endpoint, letting Claude, ChatGPT, Cursor, and other MCP clients trigger the same 9,000+ app... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Zapier MCP

# Zapier MCP

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07
CLI: zapier-platform

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [zapier.com/mcp](https://zapier.com/mcp) · entry id 07-zapier-mcp · source 07-mcp-infrastructure.md line 57

**What it does**
Zapier's own MCP endpoint, letting Claude, ChatGPT, Cursor, and other MCP clients trigger the same 9,000+ app actions Zapier already exposes to its classic trigger-action Zaps.

**AI features, separated from automation with an AI label on it**
none in the MCP layer itself - it reuses Zapier's existing (non-AI) action library. Zapier's separate "Zapier Agents" product is where genuine LLM-driven autonomous behavior lives; MCP is a new door into the same rules-based action catalog.

**RevOps role**
The broadest reach-into-anything connector for a RevOps stack already standardized on Zapier - claims 9,000+ connectable apps including Salesforce, HubSpot, Gmail, and Slack.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Uses Zapier's existing decade-old app-connection/OAuth infrastructure - you authorize apps the same way you would for a normal Zap, then expose selected actions to the MCP client.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://mcp.zapier.com/login?redirectTo=%2Fmcp](https://mcp.zapier.com/login?redirectTo=%2Fmcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.zapier.com/api/v1/connect ; https://mcp.zapier.com/login?redirectTo=%2Fmcp (redirect correction 2026-08-28: the bare address previously recorded here, mcp.zapier.com, 307s to /mcp and then to this signed-in console URL, which returns 200. It is an auth wall, not documentation; the public documentation for the same server is https://zapier.com/mcp) ; repo https://github.com/zapier/zapier-mcp

- [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect)
- [https://mcp.zapier.com/login?redirectTo=%2Fmcp](https://mcp.zapier.com/login?redirectTo=%2Fmcp)
- [https://zapier.com/mcp](https://zapier.com/mcp)
- [https://github.com/zapier/zapier-mcp](https://github.com/zapier/zapier-mcp)

**What this server exposes**

- **Tools named**: 15
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: the customer's own workspace, not a fixed catalogue

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

Recorded by the harvest: every tool is one of the customer's own connected Zaps

- **auto_provision_mcp** Automatically provisions tools from your existing Zapier connections. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **create_zapier_skill** Creates new reusable workflows. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **delete_zapier_skill** Removes skills. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **disable_zapier_action** Removes an action you no longer need. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **discover_zapier_actions** Searches for apps and actions available to add. evidence: in the vendor docs · calling it writes · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **enable_zapier_action** Enables a specific action as a callable tool. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **execute_zapier_read_action** Runs search and lookup operations. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **execute_zapier_write_action** Runs create, send, or update operations. evidence: in the vendor docs · calling it writes · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **get_configuration_url** Returns the URL to your Zapier MCP configuration page. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **get_zapier_skill** Retrieves a specific skill by name. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **inspect_zapier_actions** Lists your enabled actions with what you need to run them. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **list_zapier_skills** Lists saved workflow instructions. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **send_feedback** Sends feedback to Zapier. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **update_zapier_skill** Modifies existing skills. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **write_code_action** Generates custom code when built-in actions do not fit. Exposed on some servers only. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

119 of the 415 entries that record an official or community MCP server carry a harvested tool list. The other 296 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: zapier-platform
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npx zapier
```

quoted from [https://zapier.com/sdk](https://zapier.com/sdk) on 2026-09-12, via npx

```
npm install -g zapier-platform-cli
```

quoted from [https://www.npmjs.com/package/zapier-platform-cli](https://www.npmjs.com/package/zapier-platform-cli) on 2026-09-12, via npm

```
npm install -g @zapier/zapier-sdk-cli
```

quoted from [https://www.npmjs.com/package/@zapier/zapier-sdk-cli](https://www.npmjs.com/package/@zapier/zapier-sdk-cli) on 2026-09-12, via npm

Login or key hint seen on the page:

handles auth

Packages seen, with the version on 2026-09-12:

- [npm: zapier-platform-cli 19.1.0](https://www.npmjs.com/package/zapier-platform-cli)
- [npm: @zapier/zapier-sdk-cli 0.83.1](https://www.npmjs.com/package/@zapier/zapier-sdk-cli)

Where it was documented:

- [https://zapier.com/sdk](https://zapier.com/sdk) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (bundled into existing Zapier plans; each MCP tool call consumes 2 tasks from the account's standard task quota - no separate SKU)

**API documentation**

No documentation URL recorded.

582 of 884 entries are in the same position. Blank is legal and it is published as blank.

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

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 884 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://zapier.com/mcp](https://zapier.com/mcp)
- [https://mcp.zapier.com/login?redirectTo=%2Fmcp](https://mcp.zapier.com/login?redirectTo=%2Fmcp)
- [https://github.com/zapier/zapier-mcp](https://github.com/zapier/zapier-mcp)
- [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect)

4 source URLs. Raw sources field, verbatim:

https://zapier.com/mcp, https://mcp.zapier.com/login?redirectTo=%2Fmcp, https://github.com/zapier/zapier-mcp, https://mcp.zapier.com/api/v1/connect

**Notes, verbatim from the file**
Because MCP calls draw from the same task pool as regular Zaps, a chatty agent can burn a plan's task quota fast - worth watching before pointing a high-frequency agent at it. 2026-09-07: Same first-party artifact as the Zapier entry: zapier/zapier-mcp (405 stars), registry com.zapier/mcp, remote https://mcp.zapier.com/api/v1/connect returning 401 to an MCP initialize (https://github.com/zapier/zapier-mcp).

**Provenance**

- **Entry id**: 07-zapier-mcp

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 57

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
