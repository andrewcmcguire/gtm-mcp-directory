# Sendspark: MCP server status, API access gate and what it does

> Purpose-built B2B outbound video-prospecting platform - record one video, and AI voice cloning plus dynamic... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Sendspark

# Sendspark

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [sendspark.com](https://sendspark.com) · entry id 08-sendspark · source 08-video-prospecting.md line 52

**What it does**
Purpose-built B2B outbound video-prospecting platform - record one video, and AI voice cloning plus dynamic personalization generate individualized versions per prospect at scale for cold/warm outreach sequences.

**AI features, separated from automation with an AI label on it**
Genuinely AI: voice cloning that inserts each recipient's name (correctly pronounced) spoken in the rep's own cloned voice across several languages; dynamic on-video backgrounds pulling in the prospect's website/LinkedIn; AI-personalized thumbnails. The "record once, merge into thousands" delivery mechanism itself is automation layered on that AI core. Vendor's "300% higher click-through" / "50% more meetings" figures not independently corroborated.

**RevOps role**
Personalization-at-scale layer for cold/warm outbound, plugging into HubSpot, HighLevel, Instantly, and sequence tools.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: API-key based - Composio's page states Sendspark requires the user's own API key, which Composio then stores/manages.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://composio.dev/toolkits/sendspark](https://composio.dev/toolkits/sendspark)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://composio.dev/toolkits/sendspark (third-party Composio-hosted toolkit, 9 tools: campaigns, prospects, webhooks, analytics)

- [https://composio.dev/toolkits/sendspark](https://composio.dev/toolkits/sendspark)

**What this server exposes**

- **Tools named**: 9
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **API Health Status** Tool to check the health status of the Sendspark API. evidence: in the vendor docs · calling it reads · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **Add Multiple Prospects to Dynamic Campaign** Tool to add multiple prospects to a dynamic campaign in bulk. evidence: in the vendor docs · calling it writes · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **Add Prospect to Dynamic Video Campaign** Tool to add a prospect to a dynamic video campaign. evidence: in the vendor docs · calling it writes · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **Create Dynamic Video Campaign V2** Tool to create a dynamic video campaign in a workspace. evidence: in the vendor docs · calling it writes · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **Delete Webhook** Delete a webhook by its unique ID. evidence: in the vendor docs · calling it writes · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **Get Dynamic Campaign by ID** Tool to retrieve details of a specific dynamic video campaign. evidence: in the vendor docs · calling it reads · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **Get Workspace Prospect Data by Email** Tool to retrieve prospect data by email in a dynamic campaign. evidence: in the vendor docs · calling it reads · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **List Dynamic Video Campaigns** Tool to list all dynamic video campaigns in a workspace. evidence: in the vendor docs · calling it reads · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

- **List Webhooks** Retrieves all configured webhooks for a Sendspark workspace. evidence: in the vendor docs · calling it reads · read off composio, an aggregator wrapping the vendor's API rather than the vendor's own server

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. REST API/webhooks are excluded from the entry Solo plan ($49/mo) and included starting at Growth ($99/mo, 3 seats); continues through Team ($299/mo) and Business ($699/mo).

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/sendspark](https://github.com/sendspark) tied to the vendor by rule 3, account website https://sendspark.com has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-08-28

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [docs](https://github.com/sendspark/docs) | docs or examples | | 0 | 2026-08-28 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 649 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.sendspark.com/](https://www.sendspark.com/)
- [https://www.sendspark.com/video-platform/ai-intros](https://www.sendspark.com/video-platform/ai-intros)
- [https://help.sendspark.com/en/articles/8554225-dynamic-videos-make-videos-with-ai-introductions](https://help.sendspark.com/en/articles/8554225-dynamic-videos-make-videos-with-ai-introductions)
- [https://www.sendspark.com/pricing-plans](https://www.sendspark.com/pricing-plans)
- [https://composio.dev/toolkits/sendspark](https://composio.dev/toolkits/sendspark)

5 source URLs. Raw sources field, verbatim:

https://www.sendspark.com/, https://www.sendspark.com/video-platform/ai-intros, https://help.sendspark.com/en/articles/8554225-dynamic-videos-make-videos-with-ai-introductions, https://www.sendspark.com/pricing-plans, https://composio.dev/toolkits/sendspark

**Notes, verbatim from the file**
Repeatedly cited across independent buyer-guide articles as a top Vidyard/BombBomb alternative for prospecting specifically - one of the strongest "purpose-built for prospecting" fits researched in this file. A GitHub repo named "ai-spark-mcp-server" surfaces in search but is an unrelated Apache Spark data-engineering tool - do not cite it for Sendspark.

**Provenance**

- **Entry id**: 08-sendspark

- **Source file**: 08-video-prospecting.md

- **Source line**: 52

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
