# StackOne: MCP server status, API access gate and what it does

> A unified-API vendor that publishes a stated 518 managed MCP servers exposing 31,928 tools across HR, CRM, IT... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
StackOne

# StackOne

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07
CLI: stackone

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [stackone.com](https://stackone.com) · entry id 07-stackone · source 07-mcp-infrastructure.md line 384

**What it does**
A unified-API vendor that publishes a stated 518 managed MCP servers exposing 31,928 tools across HR, CRM, IT and finance applications, reachable through one endpoint with per-account routing, plus dynamic tool discovery so an agent loads only the tools a task needs.

**AI features, separated from automation with an AI label on it**
Two that are more than plumbing, both vendor-claimed: a reinforcement-learning-trained tool-discovery layer the vendor says cuts context by 460 times, and a prompt-injection defence it claims detects hijacked tools at 88.7% accuracy before they reach the agent. Neither was independently verified; both are recorded as vendor claims.

**RevOps role**
The connector layer for a team that wants one governed endpoint in front of many GTM systems rather than a separate server per vendor, and the only layer in this group that publishes a searchable per-application MCP server directory.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Basic authentication plus a per-account identifier, with StackOne brokering OAuth, API keys and token refresh to each connected application on the customer's behalf.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.stackone.com/mcp ; https://api.stackone.com/mcp?x-account-id= (product page: https://www.stackone.com/platform/mcp/)

- [https://mcp.stackone.com/mcp](https://mcp.stackone.com/mcp)
- [https://api.stackone.com/mcp?x-account-id=](https://api.stackone.com/mcp?x-account-id=)
- [https://www.stackone.com/platform/mcp/](https://www.stackone.com/platform/mcp/)

**What this server exposes**

What this server exposes is the customer's own workspace, not a fixed catalogue the vendor publishes. No tool list is the correct answer here rather than a gap, and the harvest recorded it as one.

Recorded by the harvest: a unified API gateway; its tools are the vendors it wraps, not its own

The count below still carries this entry on the unmeasured side, because there is no list to record. That is a different thing from a server nobody has read, and both are published rather than blended.

119 of the 264 entries that record an official or community MCP server carry a harvested tool list. The other 145 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: stackone
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @stackone/cli
```

quoted from [https://www.npmjs.com/package/@stackone/cli](https://www.npmjs.com/package/@stackone/cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @stackone/cli 1.47.3](https://www.npmjs.com/package/@stackone/cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the vendor's pricing page publishes a "Starter" Gateway tier at "Free" including "1,000 credits / seat / month", where the page states "one tool call or API call costs 1 credit", with an OEM track and enterprise deployment routed to "Book Demo".

**API documentation**

No documentation URL recorded.

400 of 514 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/StackOneHQ/stackone-plugin](https://github.com/StackOneHQ/stackone-plugin)

**On GitHub**

[github.com/StackOneHQ](https://github.com/StackOneHQ) tied to the vendor by rule 3, account website https://stackone.com has the vendor's domain, confidence strong

- **Public repositories**: 34, forks excluded, as read on 2026-09-08
- **Mention MCP**: 4 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [stack-nudge](https://github.com/StackOneHQ/stack-nudge) | other | | 24 | 2026-09-08 | v1.32.0 |
| [stackvox](https://github.com/StackOneHQ/stackvox) | CLI | Offline Kokoro-82M text-to-speech for Python - library, CLI, and a unix-socket daemon for ~13ms speech from shell... | 3 | 2026-09-08 | v0.12.0 |
| [defender](https://github.com/StackOneHQ/defender) | CLI | Open source prompt injection protection for Agents calling tools (via MCP, CLI or direct function calling). Detect and... | 120 | 2026-09-08 | defender-v0.8.2 |
| [hub](https://github.com/StackOneHQ/hub) | plugin or integration | Embeddable Integration Hub components | 1 | 2026-09-08 | hub-v1.11.2 |
| [agent-plugins](https://github.com/StackOneHQ/agent-plugins) | plugin or integration | StackOne agent skills - installable via npx skills add stackonehq/agent-plugins-marketplace | 3 | 2026-09-07 | stackone-agent-plugins-v3.2.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

243 of 514 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.stackone.com/platform/mcp/](https://www.stackone.com/platform/mcp/)
- [https://www.stackone.com/pricing/](https://www.stackone.com/pricing/)
- [https://api.stackone.com/mcp](https://api.stackone.com/mcp)
- [https://docs.stackone.com/mcp](https://docs.stackone.com/mcp)
- [https://mcp.stackone.com/mcp](https://mcp.stackone.com/mcp)
- [https://github.com/StackOneHQ/stackone-plugin](https://github.com/StackOneHQ/stackone-plugin)

6 source URLs. Raw sources field, verbatim:

https://www.stackone.com/platform/mcp/, https://www.stackone.com/pricing/, https://api.stackone.com/mcp, https://docs.stackone.com/mcp, https://mcp.stackone.com/mcp, https://github.com/StackOneHQ/stackone-plugin

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://api.stackone.com/mcp returned HTTP 401 with {"statusCode":401,"message":"Unauthorized"}, confirming a live auth-gated server. NAME COLLISION INSIDE ONE VENDOR, worth recording because it will catch an automated verifier: https://docs.stackone.com/mcp is also a live MCP server, but it is a Mintlify documentation server whose tools are search_stackone and query_docs_filesystem_stackone over StackOne's own docs, and it is read-only and scoped to published site content. It is not the unified-API server and must not be recorded as the product endpoint. The vendor's positioning line is a direct swipe at this directory's own subject matter and is quotable: "First-party MCPs weren't built for production. StackOne's are." GTM connectors the research surfaced on StackOne include Salesloft, JustCall, Dialpad, Help Scout, RingCentral and Aircall, which means several vendors in this directory can be reached either directly or through StackOne, and a buyer should compare rather than assume the wrapper is worse. Vendor also advertises automated creation of new MCP servers, which would make the 518 figure a moving number. 2026-09-07: Official MCP registry carries com.stackone/mcp (DNS-verified stackone.com namespace) with remote https://mcp.stackone.com/mcp; that URL returned 401 to an MCP initialize, as did https://api.stackone.com/mcp (https://mcp.stackone.com/mcp). 2026-09-09 (P6-04 repo sweep): first-party repository recorded at https://github.com/StackOneHQ/stackone-plugin, the org StackOneHQ (profile site stackone.com), homepage docs.stackone.com, last push 2026-08-22. It is NOT the server source: the README says the plugin connects an agent to StackOne's HOSTED MCP server. The official registry entry com.stackone/mcp (DNS-verified stackone.com namespace) lists only the remote https://mcp.stackone.com/mcp and no repository, so no public server source was found.

**Provenance**

- **Entry id**: 07-stackone

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 384

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
