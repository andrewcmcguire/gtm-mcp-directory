# The Swarm: MCP server status, API access gate and what it does

> A professional data and relationship-intelligence platform (500M+ profiles, 50M+ companies) whose... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
The Swarm

# The Swarm

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [theswarm.com](https://theswarm.com) · entry id 01-the-swarm · source 01-data-enrichment.md line 540

**What it does**
A professional data and relationship-intelligence platform (500M+ profiles, 50M+ companies) whose differentiator is network mapping - warm-introduction paths, shared work history, education, and investor connections across a team's or partner org's combined network - plus job-change and funding signals, via REST API and a Network Mapper API.

**AI features, separated from automation with an AI label on it**
Not independently assessed in this pass - the docs describe relationship-graph mapping and signal data; no explicit LLM/ML methodology claims were evaluated.

**RevOps role**
Relationship-intelligence layer over the account list - who on the team or in partner networks can open a door into a target account - feeding targeting and warm outreach rather than cold contact lookup.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth via personal Swarm login (native Claude and ChatGPT app connectors) or team API key via x-api-key header for any MCP client supporting custom headers

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-25 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://bee.theswarm.com/mcp (docs: https://docs.theswarm.com)

- [https://bee.theswarm.com/mcp](https://bee.theswarm.com/mcp)
- [https://docs.theswarm.com](https://docs.theswarm.com)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Discover warm intro paths](../jobs/discover-warm-intro-paths.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://docs.theswarm.com/docs/getting-started/introduction](https://docs.theswarm.com/docs/getting-started/introduction)
- [https://docs.theswarm.com/docs/mcp/overview](https://docs.theswarm.com/docs/mcp/overview)

2 source URLs. Raw sources field, verbatim:

https://docs.theswarm.com/docs/getting-started/introduction, https://docs.theswarm.com/docs/mcp/overview

**Notes, verbatim from the file**
MCP is read-only, respects workspace permissions, credit-based at 1 credit per successful search (empty searches free), available to Owner/Admin/Contributor roles. No public pricing; sales-led. Cross-reference - Commsor was folded into The Swarm's "Go-to-Network" product line (see the Commsor entry in 15-community-dark-social.md). Entry added 2026-08-25 from Drew's pointer; a fuller verification pass belongs to the coverage sweep.

**Provenance**

- **Entry id**: 01-the-swarm

- **Source file**: 01-data-enrichment.md

- **Source line**: 540

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
