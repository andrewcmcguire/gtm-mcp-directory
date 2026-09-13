# Nutshell CRM: MCP server status, API access gate and what it does

> An SMB CRM covering leads, companies, people, pipelines and activity reporting, with email and calendar sync... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Nutshell CRM

# Nutshell CRM

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [nutshell.com](https://nutshell.com) · entry id 06-nutshell-crm · source 06-revops-infra.md line 576

**What it does**
An SMB CRM covering leads, companies, people, pipelines and activity reporting, with email and calendar sync and built-in marketing tools, and a read-only MCP server that lets an assistant search that data and pull sales reports.

**AI features, separated from automation with an AI label on it**
The product sells AI outcomes metered per plan (AI lead recaps and next steps, an AI chatbot, AI email tooling). The MCP server adds none of its own and is explicitly read-only.

**RevOps role**
System of record for a small sales team, and a clean example of a CRM shipping a deliberately read-only MCP surface so an assistant can answer pipeline questions without being able to change anything.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The vendor's article instructs the user to add the server URL as a custom connector, then log in to Nutshell and approve access on a consent page; no API key is entered into the AI client.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://app.nutshell.com/mcp (docs: https://support.nutshell.com/en/articles/12631143-mcp-server)

- [https://app.nutshell.com/mcp](https://app.nutshell.com/mcp)
- [https://support.nutshell.com/en/articles/12631143-mcp-server](https://support.nutshell.com/en/articles/12631143-mcp-server)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-13. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-13 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - Nutshell's own MCP article states "MCP server integration is included with all Nutshell plans at no extra cost" and adds "There are no usage limits or hidden fees for MCP queries within Nutshell." There is no free Nutshell tier: the published plans start at $13 per user per month and run through $25, $42, $59 and $79, all with a self-serve "Try for free" trial and no seat minimums or maximums.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/nutshellcrm](https://github.com/nutshellcrm) tied to the vendor by rule 3, account website https://nutshell.com has the vendor's domain, confidence strong

- **Public repositories**: 6, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2025-06-13

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [eslint-config-nutshell](https://github.com/nutshellcrm/eslint-config-nutshell) | other | ESLint shareable config for the Nutshell JavaScript style guide | 1 | 2025-06-13 | v5.0.0 |
| [api-spec](https://github.com/nutshellcrm/api-spec) | API client | | 3 | 2023-09-14 | |
| [is](https://github.com/nutshellcrm/is) | other | | 0 | 2023-09-14 | |
| [nutshell-api-php](https://github.com/nutshellcrm/nutshell-api-php) | SDK | A lightweight JSON-RPC + CURL wrapper to access Nutshell CRM's API. | 22 | 2023-09-14 | |
| [hass-config](https://github.com/nutshellcrm/hass-config) | other | The config for the Nutshell Home Assistant instance | 0 | 2023-09-14 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://support.nutshell.com/en/articles/12631143-mcp-server](https://support.nutshell.com/en/articles/12631143-mcp-server)
- [https://www.nutshell.com/pricing](https://www.nutshell.com/pricing)
- [https://app.nutshell.com/mcp](https://app.nutshell.com/mcp)

3 source URLs. Raw sources field, verbatim:

https://support.nutshell.com/en/articles/12631143-mcp-server, https://www.nutshell.com/pricing, https://app.nutshell.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://app.nutshell.com/mcp returned HTTP 401 Authorization required, confirming a live auth-gated server. READ-ONLY BY DESIGN, and the vendor says so plainly: "The MCP server can only read your data and cannot make any changes to your Nutshell account." Documented tool coverage is search over leads, companies, people and users, plus pipelines, stages, outcomes, activity types, sources and channels, industries, markets and territories, and tags. That makes it the safest CRM MCP in this file to hand an unsupervised agent, and a useful counterexample to the assumption that an official CRM server means write access. Cost note worth carrying into any write-up: Nutshell charges nothing for MCP queries but the article points out the real bill lands on the AI side, saying "You'll only pay for your AI assistant subscription (ChatGPT Plus, Claude Pro)", and the connection instructions for both Claude and ChatGPT require a paid plan on those products. 2026-09-07: https://app.nutshell.com/mcp returned 401 to an MCP initialize POST (https://app.nutshell.com/mcp).

**Provenance**

- **Entry id**: 06-nutshell-crm

- **Source file**: 06-revops-infra.md

- **Source line**: 576

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-13

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
