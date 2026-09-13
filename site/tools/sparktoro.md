# SparkToro: MCP server status, API access gate and what it does

> Audience-research tool that shows what a defined audience (by keyword, website, social account, or podcast)... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
SparkToro

# SparkToro

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://sparktoro.com](https://sparktoro.com) · entry id 15-sparktoro · source 15-community-dark-social.md line 64

**What it does**
Audience-research tool that shows what a defined audience (by keyword, website, social account, or podcast) reads, watches, listens to, and follows, by combining social-graph, search, and web-crawl data.

**AI features, separated from automation with an AI label on it**
Vendor markets an "AI-powered audience research" framing, but the underlying product is an aggregation/ranking engine over crawled affinity data rather than a disclosed ML/LLM model; the MCP layer adds genuine LLM-native querying via the connected client, not a SparkToro-owned model.

**RevOps role**
Audience/attention-mapping layer for GTM and content targeting - tells an operator where a target audience actually spends attention, complementary to (not competing with) the mention-monitoring tools elsewhere in this file.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (one-click sign-in with an existing SparkToro account); documented to work with Claude Desktop, Claude Code, Cursor, and ChatGPT.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://sparktoro.com/mcp](https://sparktoro.com/mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://sparktoro.com/mcp ; docs: https://sparktoro.com/mcp/docs

- [https://sparktoro.com/mcp](https://sparktoro.com/mcp)
- [https://sparktoro.com/mcp/docs](https://sparktoro.com/mcp/docs)

**What this server exposes**

- **Tools named**: 1
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-12
- **Repo read**: SparkToro/status
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **URL** Status evidence: in a README table · calling it reads

119 of the 303 entries that record an official or community MCP server carry a harvested tool list. The other 184 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (mixed) - the MCP server requires an active paid subscription (Personal $50/mo, Business $150/mo, or Agency $300/mo); the separate REST API is pay-as-you-go credit bundles with no subscription required, and the API docs themselves are free to read without a key.

**API documentation**

No documentation URL recorded.

449 of 604 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/SparkToro/status](https://github.com/SparkToro/status)

**On GitHub**

[github.com/SparkToro](https://github.com/SparkToro) tied to the vendor by rule 1, account website https://sparktoro.com has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [status](https://github.com/SparkToro/status) | MCP server | Live and historical status for SparkToro app, public API, and MCP server (Upptime) | 0 | 2026-09-08 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: no-job-fits. Audience attention mapping. Not account research, not mention monitoring. Candidate new job: map-audience-attention.

333 of 604 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://sparktoro.com/mcp](https://sparktoro.com/mcp)
- [https://sparktoro.com/mcp/docs](https://sparktoro.com/mcp/docs)
- [https://sparktoro.com/api](https://sparktoro.com/api)
- [https://sparktoro.com/api/pricing](https://sparktoro.com/api/pricing)
- [https://sparktoro.com/pricing](https://sparktoro.com/pricing)
- [https://github.com/SparkToro/status](https://github.com/SparkToro/status)

6 source URLs. Raw sources field, verbatim:

https://sparktoro.com/mcp, https://sparktoro.com/mcp/docs, https://sparktoro.com/api, https://sparktoro.com/api/pricing, https://sparktoro.com/pricing, https://github.com/SparkToro/status

**Notes, verbatim from the file**
A public status page (github.com/SparkToro/status, built on Upptime) tracks live uptime for "SparkToro app, public API, and MCP server" - an unusually transparent, solo-operator-friendly touch rare in this category. The $0/mo free tier covers the core research product but does not include MCP access.

**Provenance**

- **Entry id**: 15-sparktoro

- **Source file**: 15-community-dark-social.md

- **Source line**: 64

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
