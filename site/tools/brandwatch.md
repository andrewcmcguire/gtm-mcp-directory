# Brandwatch: MCP server status, API access gate and what it does

> Enterprise consumer-intelligence and social-listening suite spanning social media management, influencer... Community MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

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

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

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

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/ambo-sk/mcp-brandwatch

- [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch)

**What this server exposes**

- **Tools named**: 7
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: ambo-sk/mcp-brandwatch
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **analysis_query** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **analysis_result** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **brandwatch_request** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chart** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_mentions** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_projects** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_queries** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (inferred) - no public self-serve pricing; the site routes only to "Book a meeting" / demo requests.

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch)

**On GitHub**

[github.com/brandwatch](https://github.com/brandwatch) tied to the vendor by rule 3, account website https://brandwatch.com has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-06-17

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [.github](https://github.com/brandwatch/.github) | docs or examples | A special repo with templates and docs for the whole org | 0 | 2026-06-17 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 649 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
