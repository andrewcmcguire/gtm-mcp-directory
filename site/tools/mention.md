# Mention: MCP server status, API access gate and what it does

> Monitors web and social mentions across a claimed 1 billion+ sources in real time, layering sentiment/reach... Community MCP, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

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

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

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
- **Docs URL**: [https://github.com/MaelitoP/mention-mcp-server](https://github.com/MaelitoP/mention-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-02. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/MaelitoP/mention-mcp-server (third-party; not published by Mention)

- [https://github.com/MaelitoP/mention-mcp-server](https://github.com/MaelitoP/mention-mcp-server)

**What this server exposes**

- **Tools named**: 13
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-13
- **Repo read**: MaelitoP/mention-mcp-server
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **build-boolean-query** Generate a valid Boolean query string using Boolean operators, quoted terms, proximity, and field selectors evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_advanced_alert** Create a new advanced monitoring alert with boolean query syntax. Advanced alerts use complex query strings with boolean operators like AND, OR, NOT. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_basic_alert** Create a new basic monitoring alert. Basic alerts use simple keyword matching with included_keywords, required_keywords, and excluded_keywords arrays. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **fetch_alert_stats** Retrieve comprehensive statistics for one or more alerts including mentions per interval, tones, influencers, geographical data, and reach metrics. Supports flexible date ranges, filtering, and aggregation options. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **fetch_mentions** Retrieve mentions associated with a specific alert. Supports various filters like source, folder, tone, countries, languages, and advanced search queries. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_account_info** Get current account information including subscription plan, account ID, and capabilities. This tool should be called first to understand account limitations and determine which alert creation tools are available. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_alert** Get detailed information about a specific alert by its ID. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_app_data** Get application configuration data including available languages, countries, sources, colors, and other metadata needed for creating alerts. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **instructions** What the Boolean query should match, e.g., evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_alerts** List all monitoring alerts for the current account with pagination support. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **pause_alert** Temporarily pause monitoring for a specific alert. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **unpause_alert** Resume monitoring for a previously paused alert. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_alert** Update an existing alert with new criteria or settings. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-13. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-13 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - "API access for custom integrations" is listed as part of the top-tier Company plan; exact dollar pricing was not visible on the fetched pricing page (rendered as placeholders, likely region/currency-gated), so treat pricing as unconfirmed beyond "top-tier plan only."

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/MaelitoP/mention-mcp-server](https://github.com/MaelitoP/mention-mcp-server)

**On GitHub**

[github.com/mentionapp](https://github.com/mentionapp) tied to the vendor by rule 3, account website https://mention.com has the vendor's domain, confidence strong

- **Public repositories**: 9, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2025-09-25

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [retry](https://github.com/mentionapp/retry) | other | Retry is a PHP library for retrying operations with customizable backoff, jitter, and support for both synchronous and... | 13 | 2025-09-25 | 1.0 |
| [fast-doctrine-paginator](https://github.com/mentionapp/fast-doctrine-paginator) | other | Fast Doctrine paginator suitable for batching, infinite scrolling, GraphQL/Relay | 19 | 2023-12-06 | 2.0.0 |
| [paginator](https://github.com/mentionapp/paginator) | other | Pagination base | 0 | 2023-12-06 | 2.0.0 |
| [kebab](https://github.com/mentionapp/kebab) | other | Wrappers around the PHP standard library focused on safety and testability | 16 | 2023-11-28 | 1.4.2 |
| [yoed](https://github.com/mentionapp/yoed) | other | YO hub | 10 | 2023-10-10 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-13

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
