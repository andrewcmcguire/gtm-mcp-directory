# BombBomb: MCP server status, API access gate and what it does

> Asynchronous video-messaging platform for sales, real estate, and CX teams to record and send personalized... Community MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
BombBomb

# BombBomb

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [bombbomb.com](https://bombbomb.com) · entry id 08-bombbomb · source 08-video-prospecting.md line 71

**What it does**
Asynchronous video-messaging platform for sales, real estate, and CX teams to record and send personalized one-to-one videos via email/text/CRM with open and watch tracking.

**AI features, separated from automation with an AI label on it**
Vendor states (Copilot add-on, Core+Copilot/Enterprise plans only) AI audio/noise cleanup, AI-suggested talking points/scripts, AI-generated titles/subject lines, AI summaries, smart team assignment, and a patented "fallback video" auto-send when a rep misses their assignment. Base Core plan (no Copilot) is plain recording/sending/tracking with no AI. None of the AI claims independently verified beyond vendor pages.

**RevOps role**
Outbound/relationship-nurture layer - personalized video touches inside email/CRM sequences, especially real estate and SMB sales.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Rides Zapier's own OAuth/API-key connection to BombBomb; not a native BombBomb MCP auth flow.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://zapier.com/mcp/bombbombcom (Zapier's generic MCP gateway exposing any Zapier-connected app, not a BombBomb-authored server; no dedicated repo found on GitHub, mcp.so, glama.ai, or pulsemcp.com)

- [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom)

**What this server exposes**

- **Tools named**: 4
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **Add Contact To Drip** Add a contact into a drip. Will create a contact if one doesn't exist. evidence: in the vendor docs · calling it writes · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **Add Contact To List** Add a contact into a list. Will create a contact if one doesn't exist. evidence: in the vendor docs · calling it writes · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **New Contact** Add a contact to BombBomb. evidence: in the vendor docs · calling it writes · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

- **New Email To Contact** Send an email to a contact. evidence: in the vendor docs · calling it writes · read off zapier, an aggregator wrapping the vendor's API rather than the vendor's own server

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only. BombBomb has a public REST API (developer.bombbomb.com, SDKs for JS/Ruby/Go) but access is explicitly listed as an Enterprise-plan-only feature, not available on Core or Core+Copilot.

**API documentation**

No documentation URL recorded.

428 of 559 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/bombbomb](https://github.com/bombbomb) tied to the vendor by rule 3, account website https://bombbomb.com has the vendor's domain, confidence strong

- **Public repositories**: 16, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-05-04

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [terra](https://github.com/bombbomb/terra) | infrastructure | Terraform modules | 0 | 2026-05-04 | v0.0.8 |
| [OpenAPIBuilder](https://github.com/bombbomb/OpenAPIBuilder) | API client | Builds OpenAPI Client Libraries and pushes them to their respective Git Repos | 0 | 2026-03-03 | |
| [listen-server](https://github.com/bombbomb/listen-server) | other | A simple server that captures events and allows you to inspect them via JSON. | 0 | 2026-02-26 | |
| [mindfulness](https://github.com/bombbomb/mindfulness) | other | A simple interface for logging and metrics endpoints. | 1 | 2026-02-26 | |
| [kms-jwt](https://github.com/bombbomb/kms-jwt) | other | | 1 | 2025-06-16 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 559 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://bombbomb.com/pricing/](https://bombbomb.com/pricing/)
- [https://bombbomb.com/copilot/](https://bombbomb.com/copilot/)
- [https://support.bombbomb.com/hc/en-us/articles/36078323159437-What-s-Included-in-My-Plan-Core-vs-Core-Copilot-vs-Enterprise](https://support.bombbomb.com/hc/en-us/articles/36078323159437-What-s-Included-in-My-Plan-Core-vs-Core-Copilot-vs-Enterprise)
- [https://developer.bombbomb.com/](https://developer.bombbomb.com/)
- [https://support.bombbomb.com/hc/en-us/articles/39269877765773-How-to-Get-Started-with-the-BombBomb-API](https://support.bombbomb.com/hc/en-us/articles/39269877765773-How-to-Get-Started-with-the-BombBomb-API)
- [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom)

6 source URLs. Raw sources field, verbatim:

https://bombbomb.com/pricing/, https://bombbomb.com/copilot/, https://support.bombbomb.com/hc/en-us/articles/36078323159437-What-s-Included-in-My-Plan-Core-vs-Core-Copilot-vs-Enterprise, https://developer.bombbomb.com/, https://support.bombbomb.com/hc/en-us/articles/39269877765773-How-to-Get-Started-with-the-BombBomb-API, https://zapier.com/mcp/bombbombcom

**Notes, verbatim from the file**
Pricing varies slightly by source (Core ~$36-42/user/mo, Core+Copilot ~$56-70/user/mo) - treat as approximate. Recent vendor material also refers to the product as "BombBomb Engage," suggesting a platform refresh/rebrand in progress.

**Provenance**

- **Entry id**: 08-bombbomb

- **Source file**: 08-video-prospecting.md

- **Source line**: 71

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
