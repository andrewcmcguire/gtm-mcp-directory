# Talkwalker (rebranded: Lumen by Talkwalker): MCP server status, API access gate and what it does

> Enterprise social-listening and media-monitoring platform tracking social, digital, and AI-channel... Official MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
Talkwalker (rebranded: Lumen by Talkwalker)

# Talkwalker (rebranded: Lumen by Talkwalker)

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.talkwalker.com](https://www.talkwalker.com) · entry id 15-talkwalker · source 15-community-dark-social.md line 292

**What it does**
Enterprise social-listening and media-monitoring platform tracking social, digital, and AI-channel conversations for brand benchmarking and trend/consumer-insight detection.

**AI features, separated from automation with an AI label on it**
References "AI channels" as part of what it monitors (i.e., tracking mentions inside AI chat surfaces) but does not name or describe a specific proprietary AI model on its current marketing pages.

**RevOps role**
Enterprise media-intelligence peer to Brandwatch/Meltwater, notable mainly for its ownership consolidation into Hootsuite (see notes).

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Sign in with a Hootsuite workspace when prompted; the Hootsuite MCP page says authorization is one-time.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.hootsuite.com/integrations/mcp](https://www.hootsuite.com/integrations/mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.hootsuite.com/integrations/mcp (the Lumen server, endpoint https://mcp.hootsuite.com/lumen, published by parent company Hootsuite)

- [https://www.hootsuite.com/integrations/mcp](https://www.hootsuite.com/integrations/mcp)
- [https://mcp.hootsuite.com/lumen](https://mcp.hootsuite.com/lumen)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (inferred) - no public self-serve pricing; the site routes only to "Request a custom demo."

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

- [https://www.talkwalker.com](https://www.talkwalker.com)
- [https://www.hootsuite.com/integrations/mcp](https://www.hootsuite.com/integrations/mcp)

2 source URLs. Raw sources field, verbatim:

https://www.talkwalker.com, https://www.hootsuite.com/integrations/mcp

**Notes, verbatim from the file**
Talkwalker has rebranded as "Lumen by Talkwalker" as part of a stated consolidation with Hootsuite ("bring Hootsuite and Talkwalker closer together") - worth noting for anyone still searching under the old standalone "Talkwalker" name. Checked GitHub - no MCP server found. 2026-09-02: mcp_status none-found -> official. talkwalker.com still states "Talkwalker is now Lumen by Talkwalker", and Hootsuite's MCP page https://www.hootsuite.com/integrations/mcp lists four servers including Lumen ("Insights and listening": track mentions and sentiment, find influencers, summarize competitive intel) at mcp.hootsuite.com/lumen, which answered 405 to a HEAD request today (alive; MCP endpoints reject non-POST). Caveats recorded honestly: the Hootsuite page names the server Lumen without the Talkwalker suffix, talkwalker.com itself has no MCP mention, app.talkwalker.com/app/mcp returned 404, and the official MCP registry has no talkwalker entry. The claim is first-party through the parent company, not through talkwalker.com.

**Provenance**

- **Entry id**: 15-talkwalker

- **Source file**: 15-community-dark-social.md

- **Source line**: 292

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
