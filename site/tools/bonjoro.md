# Bonjoro: MCP server status, API access gate and what it does

> Personalized 1:1 and 1:many video-messaging platform triggered by CRM events (new signup, first purchase,... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Bonjoro

# Bonjoro

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [bonjoro.com](https://bonjoro.com) · entry id 08-bonjoro · source 08-video-prospecting.md line 204

**What it does**
Personalized 1:1 and 1:many video-messaging platform triggered by CRM events (new signup, first purchase, deal-stage change), used across sales and customer-success teams.

**AI features, separated from automation with an AI label on it**
Primarily a recording/workflow-automation tool rather than AI-generation-heavy - no evidence found of generative-AI video personalization (voice cloning, AI avatars); personalization is human-recorded and CRM-triggered, not machine-generated.

**RevOps role**
Personalized-video triggers embedded in CRM lifecycle stages - a sales/customer-success crossover tool (50,000+ businesses claimed by vendor).

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Rides a Zapier account connection (OAuth to Zapier, which holds the Bonjoro-side connection).

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://zapier.com/mcp/bonjoro (Zapier's generic MCP gateway; no vendor-published first-party server found)

- [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro)

**What this server exposes**

- **Tools named**: 3
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **Create Task** Establishes a Bonjoro task requiring video recording via the platform. evidence: in the vendor docs · calling it writes · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **Message Templates** Lists available message templates. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **Workspaces** Lists available workspaces. evidence: in the vendor docs · calling it reads · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

119 of the 396 entries that record an official or community MCP server carry a harvested tool list. The other 277 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. REST API access is gated to the Grrrowth and Company/Enterprise plans ($79-399+/mo); Zapier/CRM integrations are available from the Free tier up, but the direct API is not.

**API documentation**

No documentation URL recorded.

555 of 834 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/Vimily](https://github.com/Vimily) tied to the vendor by rule 3, account website http://www.bonjoro.com has the vendor's domain, confidence strong

- **Public repositories**: 3, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-06-30

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [circleci-laravel](https://github.com/Vimily/circleci-laravel) | other | | 1 | 2026-06-30 | |
| [docker-php-dockerize](https://github.com/Vimily/docker-php-dockerize) | infrastructure | | 0 | 2021-02-22 | |
| [docker-nginx-dockerize](https://github.com/Vimily/docker-nginx-dockerize) | infrastructure | | 0 | 2018-11-21 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 834 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.bonjoro.com/](https://www.bonjoro.com/)
- [https://www.bonjoro.com/teams/customer-success](https://www.bonjoro.com/teams/customer-success)
- [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro)
- [https://www.bonjoro.com/pricing](https://www.bonjoro.com/pricing)

4 source URLs. Raw sources field, verbatim:

https://www.bonjoro.com/, https://www.bonjoro.com/teams/customer-success, https://zapier.com/mcp/bonjoro, https://www.bonjoro.com/pricing

**Notes, verbatim from the file**
Well-established (founded 2017); confirmed real and currently active.

**Provenance**

- **Entry id**: 08-bonjoro

- **Source file**: 08-video-prospecting.md

- **Source line**: 204

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
