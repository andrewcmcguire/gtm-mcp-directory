# Syften: MCP server status, API access gate and what it does

> Monitors Reddit, Hacker News, X/Twitter, Bluesky, Mastodon, GitHub, YouTube, Slack communities, and general... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
Syften

# Syften

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://syften.com](https://syften.com) · entry id 15-syften · source 15-community-dark-social.md line 83

**What it does**
Monitors Reddit, Hacker News, X/Twitter, Bluesky, Mastodon, GitHub, YouTube, Slack communities, and general web/forum sources for keyword mentions, delivering alerts via email, Slack, RSS, webhook, or API.

**AI features, separated from automation with an AI label on it**
"AI filtering" suppresses spammy/duplicate/weak-match results (vendor-described noise reduction, no model specifics disclosed); vendor also states onboarding is automated by having the system "research your company" to seed initial filters - unverified beyond vendor copy.

**RevOps role**
Reddit/HN/forum-native "dark social" mention-monitoring layer, positioned as a lighter-weight, solo-operator-priced alternative to enterprise social-listening suites like Brandwatch or Meltwater.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Community server presumably authenticates with a Syften API key (matching Syften's own API auth model); not independently confirmed for this specific repo.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/syntax-syndicate/social-listening](https://github.com/syntax-syndicate/social-listening)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/syntax-syndicate/social-listening (third-party MCP server built against Syften's data; not a vendor-published repo)

- [https://github.com/syntax-syndicate/social-listening](https://github.com/syntax-syndicate/social-listening)

**What this server exposes**

- **Tools named**: 9
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: syntax-syndicate/social-listening
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **analyze_trends** Analyze mention trends over time evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **backfill_month** Backfill mentions for a specific month evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **configure_ai_filter** Configure AI filtering settings evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_ai_filtered_mentions** Get mentions that have been processed by AI filtering evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_top_sources** Get top mention sources/authors evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_webhook_status** Check webhook configuration and health evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **nlp_prompt** Process a natural language prompt to interact with the social listening tools evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **setup_webhook** Configure webhook endpoint for real-time updates evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **sync_latest** Sync new mentions since last update evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 380 entries that record an official or community MCP server carry a harvested tool list. The other 261 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - API access ships from the Standard tier ($49.95/mo); the Entry tier ($29.95/mo) has no API. Webhooks and Syften's own vendor-marketed "MCP support" are gated to Syften PRO ($119.95/mo).

**API documentation**

No documentation URL recorded.

528 of 784 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/dancolta/subscope](https://github.com/dancolta/subscope)
- [https://github.com/syntax-syndicate/social-listening](https://github.com/syntax-syndicate/social-listening)

**On GitHub**

[github.com/syften](https://github.com/syften) tied to the vendor by rule 3, account website https://syften.com has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-07-30

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [syften-examples](https://github.com/syften/syften-examples) | docs or examples | Syften API usage examples | 3 | 2026-07-30 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 784 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://syften.com](https://syften.com)
- [https://syften.com/pricing](https://syften.com/pricing)
- [https://github.com/syntax-syndicate/social-listening](https://github.com/syntax-syndicate/social-listening)
- [https://github.com/dancolta/subscope](https://github.com/dancolta/subscope)

4 source URLs. Raw sources field, verbatim:

https://syften.com, https://syften.com/pricing, https://github.com/syntax-syndicate/social-listening, https://github.com/dancolta/subscope

**Notes, verbatim from the file**
Syften's own pricing page advertises "MCP support" as a named PRO-tier feature, implying a first-party server, but no public vendor docs page or repo URL could be located during this research (both syften.com/mcp and syften.com/docs returned 404) - so mcp_status is logged as community, backed only by the third-party repo in hand, per the hard law that an MCP claim requires a URL. Re-check for an official server before the next directory pass. A second, unrelated Reddit-monitoring tool (dancolta/subscope, a free Claude Code plugin reading public RSS feeds) also surfaced during this search - not Syften-specific, but a relevant adjacent tool for the same use case.

**Provenance**

- **Entry id**: 15-syften

- **Source file**: 15-community-dark-social.md

- **Source line**: 83

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
