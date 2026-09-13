# Woodpecker: MCP server status, API access gate and what it does

> Cold email and LinkedIn outreach automation tool with inbox rotation, adaptive sending, and centralized reply... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Woodpecker

# Woodpecker

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07
CLI: woodpecker

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [woodpecker.co](https://woodpecker.co) · entry id 02-woodpecker · source 02-engagement-outbound.md line 198

**What it does**
Cold email and LinkedIn outreach automation tool with inbox rotation, adaptive sending, and centralized reply management.

**AI features, separated from automation with an AI label on it**
Vendor advertises an AI email writer (copy drafting) and AI interest-level detection that auto-sorts replies by engagement - both genuinely AI/LLM-adjacent but modest in scope versus competitors' "AI agent" claims. Inbox rotation and adaptive sending are plain automation.

**RevOps role**
Outbound email sequencing/deliverability layer; MCP access is bundled with API/webhook access as one paid add-on.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: hosted OAuth-style flow (Claude-specific) or self-hosted Docker setup using a Woodpecker API key

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://developers.woodpecker.co/docs/mcp/](https://developers.woodpecker.co/docs/mcp/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/Woodpeckerco/woodpecker-mcp-server ; https://developers.woodpecker.co/docs/mcp/ (Claude-specific setup at https://developers.woodpecker.co/docs/mcp/connect-claude/)

- [https://github.com/Woodpeckerco/woodpecker-mcp-server](https://github.com/Woodpeckerco/woodpecker-mcp-server)
- [https://developers.woodpecker.co/docs/mcp/](https://developers.woodpecker.co/docs/mcp/)
- [https://developers.woodpecker.co/docs/mcp/connect-claude/](https://developers.woodpecker.co/docs/mcp/connect-claude/)

**What this server exposes**

- **Tools named**: 34
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **addEmailStep** Add an email follow-up step to an existing campaign evidence: in the vendor docs · calling it writes · required: campaignId, parentId, versions, deliveryTimes

- **addLinkedinConnectionRequestStep** Add a LinkedIn connection request follow-up step to an existing campaign evidence: in the vendor docs · calling it writes · required: campaignId, parentId, linkedinAccountId

- **addLinkedinDirectMessageStep** Add a LinkedIn direct message follow-up step to an existing campaign evidence: in the vendor docs · calling it writes · required: campaignId, parentId, linkedinAccountId, bodyVersions

- **addLinkedinInMailMessageStep** Add a LinkedIn InMail message follow-up step to an existing campaign evidence: in the vendor docs · calling it writes · required: campaignId, parentId, linkedinAccountId, bodyVersions

- **addLinkedinProfileVisitStep** Add a LinkedIn profile visit follow-up step to an existing campaign evidence: in the vendor docs · calling it writes · required: campaignId, parentId, linkedinAccountId

- **addProspectsToCampaign** Bulk add prospects with full contact information and custom snippets evidence: in the vendor docs · calling it writes · required: campaignId, prospectsPayload

- **addProspectsToDatabase** Adds new prospects to your global prospect list without enrolling them in campaigns evidence: in the vendor docs · calling it reads · required: prospectsPayload

- **buildCampaignUrl** Generate Woodpecker app URL for campaign access evidence: in the vendor docs · calling it reads · required: campaignId

- **createEmailCampaign** Create a Woodpecker email campaign with one email step and minimal configuration evidence: in the vendor docs · calling it writes · required: timezone, dailyEnroll, emailAccountIds, versions, deliveryTimes

- **createLinkedinConnectionRequestCampaign** Create a Woodpecker LinkedIn campaign with one connection request step evidence: in the vendor docs · calling it writes · required: timezone, dailyEnroll, linkedinAccountId

- **createLinkedinDirectMessageCampaign** Create a Woodpecker LinkedIn campaign with one direct message step evidence: in the vendor docs · calling it writes · required: timezone, dailyEnroll, linkedinAccountId, bodyVersions

- **createLinkedinInMailMessageCampaign** Create a Woodpecker LinkedIn campaign with one InMail message step evidence: in the vendor docs · calling it writes · required: timezone, dailyEnroll, linkedinAccountId, bodyVersions

- **createLinkedinProfileVisitCampaign** Create a Woodpecker LinkedIn campaign with one profile visit step evidence: in the vendor docs · calling it writes · required: timezone, dailyEnroll, linkedinAccountId

- **deleteCampaign** Remove campaign entirely evidence: in the vendor docs · calling it writes · required: campaignId

- **deleteCampaignStep** Remove steps from campaigns evidence: in the vendor docs · calling it writes · required: campaignId, stepId

- **deleteProspects** Permanently deletes prospects from your database and/or specific campaigns evidence: in the vendor docs · calling it reads · required: prospectIds

- **listCampaigns** Retrieve campaigns with optional filtering by operational status evidence: in the vendor docs · calling it reads · required: pageNumber

- **listLinkedinAccounts** Retrieve available LinkedIn accounts for campaign assignment evidence: in the vendor docs · calling it reads · required: filter

- **listMailboxes** Retrieve available email accounts for campaign assignment evidence: in the vendor docs · calling it reads · required: filter

- **listProspectsInCampaign** Paginated retrieval of campaign prospects evidence: in the vendor docs · calling it reads · required: campaignId, pageNumber

- **listProspectsInDatabase** Lists prospects from your global prospect database (not tied to any specific campaign) evidence: in the vendor docs · calling it reads · required: pageNumber

- **makeCampaignEditable** Enable campaign modifications evidence: in the vendor docs · calling it reads · required: campaignId

- **pauseCampaign** Pause campaign evidence: in the vendor docs · calling it reads · required: campaignId

- **retrieveCampaignDetails** Get detailed campaign structure including all steps and configurations evidence: in the vendor docs · calling it reads · required: campaignId

- **retrieveCampaignStatistics** Fetch campaign performance metrics and analytics evidence: in the vendor docs · calling it reads · required: campaignId

- **runCampaign** Start campaign execution evidence: in the vendor docs · calling it writes · required: campaignId

- **searchProspects** Searches for prospects matching specific criteria across your entire database evidence: in the vendor docs · calling it reads · required: pageNumber

- **stopCampaign** Stop campaign evidence: in the vendor docs · calling it writes · required: campaignId

- **updateCampaignSettings** Modify campaign-wide configuration including naming, email accounts, and limits evidence: in the vendor docs · calling it reads · required: campaignId, name, emailAccountIds, timezone, dailyEnroll

- **updateCampaignStep** Modify step delivery times and scheduling evidence: in the vendor docs · calling it reads · required: campaignId, stepId, payload

- **updateEmailStepVersion** Update email content, subject lines, signatures and tracking settings evidence: in the vendor docs · calling it writes · required: campaignId, stepId, versionId, subject, message, signature, trackOpens

- **updateLinkedinStepVersion** Update LinkedIn connection request, direct message, or InMail content evidence: in the vendor docs · calling it writes · required: campaignId, stepId, versionId, message

- **updateProspectsInCampaign** Update existing prospect data (requires explicit user request) evidence: in the vendor docs · calling it writes · required: campaignId, prospectsPayload

- **updateProspectsInDatabase** Updates existing prospects in your global database or adds new ones if they do not exist evidence: in the vendor docs · calling it reads · required: prospectsPayload

119 of the 415 entries that record an official or community MCP server carry a harvested tool list. The other 296 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: woodpecker
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @woodpecker.co/cli
```

quoted from [https://www.npmjs.com/package/@woodpecker.co/cli](https://www.npmjs.com/package/@woodpecker.co/cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @woodpecker.co/cli 0.0.1](https://www.npmjs.com/package/@woodpecker.co/cli)
- [npm: @woodpecker-js/cli 0.1.0, third party](https://www.npmjs.com/package/@woodpecker-js/cli)
- [pypi: woodpecker 0.0.1, third party](https://pypi.org/project/woodpecker/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

582 of 884 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Woodpeckerco/woodpecker-mcp-server](https://github.com/Woodpeckerco/woodpecker-mcp-server)

**On GitHub**

[github.com/Woodpeckerco](https://github.com/Woodpeckerco) tied to the vendor by rule 2, account website https://woodpecker.co has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2025-07-29

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [woodpecker-mcp-server](https://github.com/Woodpeckerco/woodpecker-mcp-server) | MCP server | The Woodpecker MCP (Model Context Protocol) integration transforms cold email campaign management into a conversational... | 1 | 2025-07-29 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 884 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://woodpecker.co/pricing/](https://woodpecker.co/pricing/)
- [https://developers.woodpecker.co/docs/mcp/](https://developers.woodpecker.co/docs/mcp/)
- [https://github.com/Woodpeckerco/woodpecker-mcp-server](https://github.com/Woodpeckerco/woodpecker-mcp-server)

3 source URLs. Raw sources field, verbatim:

https://woodpecker.co/pricing/, https://developers.woodpecker.co/docs/mcp/, https://github.com/Woodpeckerco/woodpecker-mcp-server

**Notes, verbatim from the file**
"Integrations, API, webhooks, MCP, CLI" is a single $20/month add-on available on top of any pricing tier - not enterprise-gated. Notable discovery gap: this server did not surface via GitHub/glama.ai search (which returned an unrelated "Woodpecker CI" project) - only found by checking the vendor's own site directly. 2026-09-07: GitHub account Woodpeckerco; README: "The Woodpecker MCP (Model Context Protocol) integration transforms cold email campaign management into a conversational experience... connecting your AI assistant to Woodpecker's automation platform" - that is woodpecker.co the cold-email vendor, not Woodpecker CI (https://github.com/Woodpeckerco/woodpecker-mcp-server).

**Provenance**

- **Entry id**: 02-woodpecker

- **Source file**: 02-engagement-outbound.md

- **Source line**: 198

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
