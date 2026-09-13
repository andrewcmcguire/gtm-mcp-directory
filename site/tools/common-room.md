# Common Room: MCP server status, API access gate and what it does

> Aggregates buyer/community engagement signals - Slack, Discord, GitHub activity (stars, PRs, issues), product... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Common Room

# Common Room

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24
CLI: cr

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.commonroom.io](https://www.commonroom.io) · entry id 05-common-room · source 05-signals-intent-abm.md line 285

**What it does**
Aggregates buyer/community engagement signals - Slack, Discord, GitHub activity (stars, PRs, issues), product usage, and third-party intent data (Bombora integration) - across a company's community/product channels into unified contact and organization profiles.

**AI features, separated from automation with an AI label on it**
Primarily data aggregation and unification across many signal sources rather than an ML/predictive product. The MCP layer adds genuine LLM-native querying, but that intelligence comes from the connected AI client, not a proprietary Common Room model. No predictive-scoring ML claims found.

**RevOps role**
Community-led-growth and product-signal intelligence, especially for developer-tool/PLG companies tracking engagement across Slack/Discord/GitHub before a form-fill, feeding CRM enrichment.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth (OAuth 2.1, browser-based, tokens scoped to the user's own Common Room permissions)

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://www.commonroom.io/docs/using-common-room/mcp-server/](https://www.commonroom.io/docs/using-common-room/mcp-server/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.commonroom.io/docs/using-common-room/mcp-server/ ; community alternative: https://github.com/chris-trag/commonroom-mcp

- [https://www.commonroom.io/docs/using-common-room/mcp-server/](https://www.commonroom.io/docs/using-common-room/mcp-server/)
- [https://github.com/chris-trag/commonroom-mcp](https://github.com/chris-trag/commonroom-mcp)

**What this server exposes**

- **Tools named**: 15
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: chris-trag/commonroom-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **commonroom_add_activity** Add a new activity record to Common Room (blog post, webinar, conference talk, etc.) evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_add_user** Add or update a user profile in Common Room evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_activity_types** Get all available Common Room activity types (article, webinar, presentation, etc.) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_api_sources_url** Get URL for Common Room API sources configuration page evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_api_tokens_url** Get URL for Common Room API tokens configuration page evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_dashboard_urls** Get URLs for all Common Room dashboard sections (home, segments, search, contacts, etc.). Requires COMMONROOM_BASE_URL in .env file. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_member_activity_url** Get URL for individual Common Room member activity page (more detailed than overview) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_member_url** Get URL for individual Common Room member page evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_organization_url** Get URL for individual Common Room organization page evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_segment_url** Get URL for individual Common Room segment page evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_segments** Get all Common Room audience segments for targeting and analysis evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_sources_url** Get URL for Common Room sources configuration page evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_tags** Get all Common Room tags used for categorizing activities and users evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **commonroom_get_user** Get Common Room user profile and activity data by email address evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **test_tool** Test tool to verify MCP connection evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 437 entries that record an official or community MCP server carry a harvested tool list. The other 318 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: cr
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @commonroomio/cli
```

quoted from [https://www.npmjs.com/package/@commonroomio/cli](https://www.npmjs.com/package/@commonroomio/cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @commonroomio/cli 0.2.0](https://www.npmjs.com/package/@commonroomio/cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

604 of 934 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/chris-trag/commonroom-mcp](https://github.com/chris-trag/commonroom-mcp)

**On GitHub**

[github.com/common-room](https://github.com/common-room) tied to the vendor by rule 3, account website commonroom.io has the vendor's domain, confidence strong

- **Public repositories**: 5, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [cli-sample](https://github.com/common-room/cli-sample) | docs or examples | | 1 | 2026-09-08 | |
| [homebrew-tap](https://github.com/common-room/homebrew-tap) | infrastructure | | 0 | 2026-08-21 | |
| [hacker-news-integration](https://github.com/common-room/hacker-news-integration) | docs or examples | End to end working example that integrates Hacker News with Common Room. | 0 | 2026-05-28 | |
| [claude-plugin](https://github.com/common-room/claude-plugin) | plugin or integration | | 3 | 2026-02-19 | |
| [.github](https://github.com/common-room/.github) | other | | 0 | 2025-05-01 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 934 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Common Room

- **Category**: [Community & Dark Social](../categories/community-dark-social.md)

- **MCP status there**: Official MCP

- **Gate there**: Enterprise only

- **Source**: 15-community-dark-social.md line 7

- **Canonical page**: [Common Room](../tools/common-room.md)

What that listing says it does: See the full RESEARCHED entry in 05-signals-intent-abm.md (Common Room is filed there as its canonical home in this directory) - aggregates Slack, Discord, GitHub, product-usage, and third-party intent signals into unified contact/organization profiles.

16 of the 934 entries are cross listed like this. They are why the entry count is 934 and the unique product count is 918. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.commonroom.io/docs/using-common-room/mcp-server/](https://www.commonroom.io/docs/using-common-room/mcp-server/)
- [https://www.commonroom.io/product/mcp-server/](https://www.commonroom.io/product/mcp-server/)
- [https://github.com/chris-trag/commonroom-mcp](https://github.com/chris-trag/commonroom-mcp)
- [https://www.vendr.com/marketplace/common-room](https://www.vendr.com/marketplace/common-room)
- [https://marketbetter.ai/blog/common-room-pricing-breakdown-2026/](https://marketbetter.ai/blog/common-room-pricing-breakdown-2026/)
- [https://glama.ai/mcp/servers?query=common+room](https://glama.ai/mcp/servers?query=common+room)

6 source URLs. Raw sources field, verbatim:

https://www.commonroom.io/docs/using-common-room/mcp-server/, https://www.commonroom.io/product/mcp-server/, https://github.com/chris-trag/commonroom-mcp, https://www.vendr.com/marketplace/common-room, https://marketbetter.ai/blog/common-room-pricing-breakdown-2026/, https://glama.ai/mcp/servers?query=common+room

**Notes, verbatim from the file**
Official MCP exposes 4 tools (get_catalog, list_objects, create_object, update_object) and supports read AND write - more capable than a typical read-only intent MCP. No public self-serve pricing found; market data (Vendr) suggests Starter plans around $1,700/mo scaling to $30-60K/yr, quote-only.

**Provenance**

- **Entry id**: 05-common-room

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 285

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
