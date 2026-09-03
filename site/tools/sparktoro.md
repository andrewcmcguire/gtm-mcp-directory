# SparkToro: MCP server status, API access gate and what it does

> Audience-research tool that shows what a defined audience (by keyword, website, social account, or podcast)... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

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

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

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

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://sparktoro.com/mcp ; docs: https://sparktoro.com/mcp/docs

- [https://sparktoro.com/mcp](https://sparktoro.com/mcp)
- [https://sparktoro.com/mcp/docs](https://sparktoro.com/mcp/docs)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (mixed) - the MCP server requires an active paid subscription (Personal $50/mo, Business $150/mo, or Agency $300/mo); the separate REST API is pay-as-you-go credit bundles with no subscription required, and the API docs themselves are free to read without a key.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/SparkToro/status](https://github.com/SparkToro/status)

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: no-job-fits. Audience attention mapping. Not account research, not mention monitoring. Candidate new job: map-audience-attention.

22 of 293 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

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

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
