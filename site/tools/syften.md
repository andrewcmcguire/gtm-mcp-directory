# Syften: MCP server status, API access gate and what it does

> Monitors Reddit, Hacker News, X/Twitter, Bluesky, Mastodon, GitHub, YouTube, Slack communities, and general... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

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

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

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

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/syntax-syndicate/social-listening (third-party MCP server built against Syften's data; not a vendor-published repo)

- [https://github.com/syntax-syndicate/social-listening](https://github.com/syntax-syndicate/social-listening)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - API access ships from the Standard tier ($49.95/mo); the Entry tier ($29.95/mo) has no API. Webhooks and Syften's own vendor-marketed "MCP support" are gated to Syften PRO ($119.95/mo).

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/dancolta/subscope](https://github.com/dancolta/subscope)
- [https://github.com/syntax-syndicate/social-listening](https://github.com/syntax-syndicate/social-listening)

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

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

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
