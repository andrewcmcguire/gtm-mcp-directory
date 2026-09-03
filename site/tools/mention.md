# Mention: MCP server status, API access gate and what it does

> Monitors web and social mentions across a claimed 1 billion+ sources in real time, layering sentiment/reach... Community MCP, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
Mention

# Mention

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://mention.com](https://mention.com) · entry id 15-mention · source 15-community-dark-social.md line 273

**What it does**
Monitors web and social mentions across a claimed 1 billion+ sources in real time, layering sentiment/reach analytics and a unified social inbox on top of the monitoring feed.

**AI features, separated from automation with an AI label on it**
"AI tools" for content generation (caption/bio/tweet generators) are the concretely-described AI feature; monitoring and sentiment analysis themselves are presented as standard aggregation and scoring rather than a named proprietary model.

**RevOps role**
General-purpose social/web mention monitoring with a social-management layer bolted on - broader and more marketing-team-oriented than the Reddit/HN-specific tools (Syften, F5Bot) elsewhere in this file.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Mention API key via the MCP_MENTION_API_KEY environment variable

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/MaelitoP/mention-mcp-server](https://github.com/MaelitoP/mention-mcp-server)Probed**: 2026-09-03, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/MaelitoP/mention-mcp-server (third-party; not published by Mention)

- [https://github.com/MaelitoP/mention-mcp-server](https://github.com/MaelitoP/mention-mcp-server)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - "API access for custom integrations" is listed as part of the top-tier Company plan; exact dollar pricing was not visible on the fetched pricing page (rendered as placeholders, likely region/currency-gated), so treat pricing as unconfirmed beyond "top-tier plan only."

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/MaelitoP/mention-mcp-server](https://github.com/MaelitoP/mention-mcp-server)

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://mention.com/en/](https://mention.com/en/)
- [https://mention.com/en/pricing/](https://mention.com/en/pricing/)
- [https://github.com/MaelitoP/mention-mcp-server](https://github.com/MaelitoP/mention-mcp-server)

3 source URLs. Raw sources field, verbatim:

https://mention.com/en/, https://mention.com/en/pricing/, https://github.com/MaelitoP/mention-mcp-server

**Notes, verbatim from the file**
Checked GitHub for "mention.com mcp" - no repositories found. The "1 billion+ sources" figure is vendor copy, not independently verified. Pricing page did not render dollar figures during this research; flagged as thin rather than guessed at. 2026-09-02: mcp_status none-found -> community. A third-party TypeScript server, github.com/MaelitoP/mention-mcp-server (0 stars, 34 commits, MIT licence, no stated Mention.com affiliation), wraps the Mention API with 11 tools for alerts, mentions and statistics and is listed on mcp.so and LobeHub. mention.com has no llms.txt and the official MCP registry has no entry, so no official server; unofficial and thin, treat as experimental.

**Provenance**

- **Entry id**: 15-mention

- **Source file**: 15-community-dark-social.md

- **Source line**: 273

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
