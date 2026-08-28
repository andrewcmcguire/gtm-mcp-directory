# Brandwatch: MCP server status, API access gate and what it does

> Enterprise consumer-intelligence and social-listening suite spanning social media management, influencer... Community MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
Brandwatch

# Brandwatch

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.brandwatch.com](https://www.brandwatch.com) · entry id 15-brandwatch · source 15-community-dark-social.md line 178

**What it does**
Enterprise consumer-intelligence and social-listening suite spanning social media management, influencer marketing, search/GenAI-mention monitoring, and analyst-backed media intelligence.

**AI features, separated from automation with an AI label on it**
Branded "Iris AI" - vendor markets it as "advanced proprietary and generative AI" for trend discovery and decision-making; no methodology disclosed publicly, so treat as an unverified vendor claim, consistent with this directory's general skepticism toward suite-wide "AI" branding.

**RevOps role**
Enterprise-tier consumer/social intelligence, the closest peer to Meltwater/Talkwalker in this file, now with an unofficial but real community MCP bridge.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: unknown - the third-party server's description states it interfaces with "the Brandwatch Consumer Research, Data Upload and Analysis APIs," hosted on Cloudflare Workers; specific auth handling was not confirmed from the repo listing alone.

- **Parsed URLs**: 1 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/ambo-sk/mcp-brandwatch

- [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (inferred) - no public self-serve pricing; the site routes only to "Book a meeting" / demo requests.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch)

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.brandwatch.com](https://www.brandwatch.com)
- [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch)

2 source URLs. Raw sources field, verbatim:

https://www.brandwatch.com, https://github.com/ambo-sk/mcp-brandwatch

**Notes, verbatim from the file**
The community MCP server is third-party (author ambo-sk, no visible Brandwatch affiliation in available metadata) and quite new (~20 days old as of this research) - worth a follow-up check on maintenance/reliability before recommending it in a live segment.

**Provenance**

- **Entry id**: 15-brandwatch

- **Source file**: 15-community-dark-social.md

- **Source line**: 178

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
