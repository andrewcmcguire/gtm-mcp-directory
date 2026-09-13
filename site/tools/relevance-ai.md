# Relevance AI: MCP server status, API access gate and what it does

> A platform for building and deploying specialist AI agents (research/enrichment, outbound prospecting,... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
Relevance AI

# Relevance AI

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-09-07
CLI: relevanceai

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://relevanceai.com](https://relevanceai.com) · entry id 04-relevance-ai · source 04-ai-sdr-agents.md line 163

**What it does**
A platform for building and deploying specialist AI agents (research/enrichment, outbound prospecting, meeting scheduling, deal review, proposal building) that teams configure and progress toward autonomous ("L3 Autopilot") operation.

**AI features, separated from automation with an AI label on it**
Genuinely a build-your-own-agent platform rather than a single packaged persona - the agentic depth depends entirely on what the operator configures; the "96.4% eval pass rate" and "L3 Autopilot" framing are vendor-reported metrics, not independently verified.

**RevOps role**
Agent-building layer that can sit anywhere in the stack depending on configuration - closer to infrastructure than a packaged point solution.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (tokens may expire after inactivity; re-auth via login flow); Viewer/Chat project roles get restricted read-only access automatically

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins](https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.relevanceai.com/ ; https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins (redirect correction 2026-08-28: the address previously recorded here, relevanceai.com/docs/integrations/mcp/programmatic-gtm/introduction, 308s to this one and this one returns 200)

- [https://mcp.relevanceai.com/](https://mcp.relevanceai.com/)
- [https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins](https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 471 entries that record an official or community MCP server carry a harvested tool list. The other 352 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: relevanceai
- **Status**: official CLI, first party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
pip install relevanceai
```

quoted from [https://pypi.org/project/relevanceai/](https://pypi.org/project/relevanceai/) on 2026-09-12, via pypi

Packages seen, with the version on 2026-09-12:

- [pypi: relevanceai 10.2.2](https://pypi.org/project/relevanceai/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the MCP server and Claude Code plugin are free to connect; usage (agent runs, tool executions) bills against the operator's Relevance AI plan

**API documentation**

No documentation URL recorded.

629 of 982 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/RelevanceAI/cc-plugin](https://github.com/RelevanceAI/cc-plugin)

**On GitHub**

[github.com/RelevanceAI](https://github.com/RelevanceAI) tied to the vendor by rule 3, account website https://relevanceai.com has the vendor's domain, confidence strong

- **Public repositories**: 39, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 3 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [relevance-docs](https://github.com/RelevanceAI/relevance-docs) | docs or examples | | 3 | 2026-09-08 | |
| [content-cdn](https://github.com/RelevanceAI/content-cdn) | other | | 2 | 2026-09-08 | |
| [arg-releases](https://github.com/RelevanceAI/arg-releases) | CLI | Public release artifacts for the arg CLI (binary distribution only; source lives in the private monorepo) | 0 | 2026-08-24 | v0.3.19 |
| [cc-plugin](https://github.com/RelevanceAI/cc-plugin) | plugin or integration | RelevanceAI Claude Code plugin (Skills + MCP) | 1 | 2026-07-27 | |
| [homebrew-tap](https://github.com/RelevanceAI/homebrew-tap) | CLI | Homebrew tap for the arg CLI. Run: brew tap relevanceai/tap | 0 | 2026-05-14 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: thin. Tagged nothing. It is a build-your-own-agent platform and the entry says the agentic depth depends entirely on what the operator configures. Its listed specialist agents (prospecting, scheduling, deal review, proposal building) would each be a tag, but tagging a builder with its example templates would inflate the supply count for six jobs at once.

711 of 982 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://relevanceai.com](https://relevanceai.com)
- [https://marketplace.relevanceai.com/](https://marketplace.relevanceai.com/)
- [https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins](https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins)
- [https://mcp.relevanceai.com/](https://mcp.relevanceai.com/)
- [https://github.com/RelevanceAI/cc-plugin](https://github.com/RelevanceAI/cc-plugin)

5 source URLs. Raw sources field, verbatim:

https://relevanceai.com, https://marketplace.relevanceai.com/, https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins, https://mcp.relevanceai.com/, https://github.com/RelevanceAI/cc-plugin

**Notes, verbatim from the file**
The seed list named this tool's SDR agent "Bosh" - that name could not be found anywhere on the current site or marketplace (agent templates found instead: "Outbound Prospector," "Sales Researcher," "Perfect 5 Leads," etc.). Either renamed, deprecated, or misremembered - flag as unconfirmed. This is one of the very few tools in this category with a confirmed, solo-operator-accessible official MCP - a strong bench-test candidate. 2026-09-07: https://mcp.relevanceai.com/ returned 401 {"error":"invalid_token","error_description":"Missing Authorization header"} to an MCP initialize POST (https://mcp.relevanceai.com/). 2026-09-09 (P6-04 repo sweep): first-party repository recorded at https://github.com/RelevanceAI/cc-plugin, the org RelevanceAI (profile site relevanceai.com), last push 2026-07-27. It is NOT the server source: the README describes a Claude Code plugin of skills plus MCP wiring for Relevance AI. The npm package @relevanceai/relevanceai-mcp-server exists under the vendor's own scope but declares no repository, so no public server source was found.

**Provenance**

- **Entry id**: 04-relevance-ai

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 163

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
