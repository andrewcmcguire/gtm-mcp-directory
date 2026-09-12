# HeyReach: MCP server status, API access gate and what it does

> Cloud-based LinkedIn outreach automation platform for agencies/sales teams running multi-account connection,... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
HeyReach

# HeyReach

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07
CLI: heyreach (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [heyreach.io](https://heyreach.io) · entry id 02-heyreach · source 02-engagement-outbound.md line 350

**What it does**
Cloud-based LinkedIn outreach automation platform for agencies/sales teams running multi-account connection, messaging, and inbox campaigns from unlimited LinkedIn accounts.

**AI features, separated from automation with an AI label on it**
AI filters, message personalization, and message-optimization suggestions bundled in the paid plan - applied LLM copy generation/scoring layered on top of rule-based sequencing, not a novel capability.

**RevOps role**
LinkedIn multi-account outbound execution layer, downstream of list-building/enrichment tools and upstream of CRM via API/webhooks.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: workspace-scoped "MCP key" + connection URL (API-key-style, not OAuth)

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://www.heyreach.io/mcp](https://www.heyreach.io/mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.heyreach.io/mcp ; https://www.heyreach.io/mcp ; setup docs at https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools

- [https://mcp.heyreach.io/mcp](https://mcp.heyreach.io/mcp)
- [https://www.heyreach.io/mcp](https://www.heyreach.io/mcp)
- [https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools](https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools)

**What this server exposes**

- **Tools named**: 8
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **CreateCampaign** spin up a fully configured campaign in draft evidence: in the vendor docs · calling it reads

- **CreateCampaignFromTemplate** clone an existing campaign instead of starting cold evidence: in the vendor docs · calling it reads

- **GetCampaignSequence** pull the campaign's full workflow tree evidence: in the vendor docs · calling it reads

- **StartCampaign** activate a draft and send it live evidence: in the vendor docs · calling it writes

- **UpdateCampaignAccounts** swap the assigned LinkedIn accounts evidence: in the vendor docs · calling it reads

- **UpdateCampaignSchedule** set the time window, active days, and timezone evidence: in the vendor docs · calling it writes

- **UpdateCampaignSequence** create or replace the entire workflow sequence evidence: in the vendor docs · calling it writes

- **UpdateCampaignSettings** change name, lead list, and exclusions evidence: in the vendor docs · calling it reads

119 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 106 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: heyreach
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g heyreach-cli
```

quoted from [https://www.npmjs.com/package/heyreach-cli](https://www.npmjs.com/package/heyreach-cli) on 2026-09-12, via npm, a third party source

Packages seen, with the version on 2026-09-12:

- [npm: heyreach-cli 0.2.2, third party](https://www.npmjs.com/package/heyreach-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/HeyReach](https://github.com/HeyReach) tied to the vendor by rule 3, account website https://heyreach.io has the vendor's domain, confidence strong

- **Public repositories**: 4, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [HeyReach-CLI-releases](https://github.com/HeyReach/HeyReach-CLI-releases) | CLI | | 5 | 2026-09-07 | v1.0.2 |
| [heyreach-scoop](https://github.com/HeyReach/heyreach-scoop) | other | | 0 | 2026-05-12 | |
| [homebrew-heyreach](https://github.com/HeyReach/homebrew-heyreach) | infrastructure | | 0 | 2026-05-12 | |
| [n8n-nodes-heyreach](https://github.com/HeyReach/n8n-nodes-heyreach) | plugin or integration | HeyReach n8n community node | 0 | 2025-10-04 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.heyreach.io/pricing](https://www.heyreach.io/pricing)
- [https://www.heyreach.io/mcp](https://www.heyreach.io/mcp)
- [https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools](https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools)
- [https://www.heyreach.io/blog/campaign-api](https://www.heyreach.io/blog/campaign-api)
- [https://mcp.heyreach.io/mcp](https://mcp.heyreach.io/mcp)

5 source URLs. Raw sources field, verbatim:

https://www.heyreach.io/pricing, https://www.heyreach.io/mcp, https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools, https://www.heyreach.io/blog/campaign-api, https://mcp.heyreach.io/mcp

**Notes, verbatim from the file**
No permanent free tier (14-day trial only); cheapest paid plan is Growth at $79/mo/sender, with API and MCP included. A third-party/unofficial MCP repo (github.com/bcharleson/heyreach-mcp) predates and duplicates the official one - don't conflate them. Like all LinkedIn automation tools, this operates against LinkedIn's User Agreement, which prohibits third-party bots/automation (linkedin.com/help/linkedin/answer/a1341387). 2026-09-07: https://mcp.heyreach.io/mcp returned 401 to an MCP initialize POST while a control path on the same host (https://mcp.heyreach.io/zzznotamcp) returned 404, so /mcp is a real distinct route and not a blanket auth wall (https://mcp.heyreach.io/mcp).

**Provenance**

- **Entry id**: 02-heyreach

- **Source file**: 02-engagement-outbound.md

- **Source line**: 350

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
