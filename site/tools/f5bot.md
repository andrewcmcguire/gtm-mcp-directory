# F5Bot: MCP server status, API access gate and what it does

> Monitors Reddit, Hacker News, and Lobsters for keyword mentions and sends email alerts within minutes of a... No MCP found, Free to start. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
F5Bot

# F5Bot

[No MCP found](../mcp/none-found.md)
[Free to start](../gates/free.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://f5bot.com](https://f5bot.com) · entry id 15-f5bot · source 15-community-dark-social.md line 102

**What it does**
Monitors Reddit, Hacker News, and Lobsters for keyword mentions and sends email alerts within minutes of a match.

**AI features, separated from automation with an AI label on it**
Now markets an "AI" option to "describe what you're looking for in natural language" and have AI evaluate each new discussion - a newer addition beyond exact-keyword matching, vendor-described and not independently verified; the core free service remains rules-based keyword alerting.

**RevOps role**
The lowest-friction entry point in this whole file - a genuinely free Reddit/HN keyword alert for solo operators, with paid tiers layered on top for filtering, AI evaluation, and API access.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

none

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited) - a $0/mo "free forever" tier exists with no credit card required, but "RSS & JSON feeds" and full programmatic API access are gated to the Gold tier ($49.99/mo); a Silver tier ($9.99/mo) adds "advanced filtering" without API access.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://f5bot.com](https://f5bot.com)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 14 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://f5bot.com

**Notes, verbatim from the file**
Worth flagging as a finding in itself: F5Bot has historically been known purely as a bare-bones free tool, but as of this research it now runs three tiers (Free/Silver $9.99/Gold $49.99) plus an AI-powered natural-language filtering option - a meaningfully different, more built-out product than its old reputation suggests, while still keeping a real free tier. No MCP found on GitHub or PulseMCP. 2026-09-02: re-checked https://f5bot.com (no MCP mention on the homepage, no llms.txt) and the official MCP registry (no entry); no MCP server found.

**Provenance**

- **Entry id**: 15-f5bot

- **Source file**: 15-community-dark-social.md

- **Source line**: 102

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
