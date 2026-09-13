# Help Scout: MCP server status, API access gate and what it does

> A shared inbox, live chat and knowledge-base product for customer-facing teams, with an MCP server that gives... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Help Scout

# Help Scout

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [helpscout.com](https://helpscout.com) · entry id 14-help-scout · source 14-inbound-plg-chat.md line 313

**What it does**
A shared inbox, live chat and knowledge-base product for customer-facing teams, with an MCP server that gives an AI agent read access to conversations, customers, organisations, reporting and Docs content, each teammate connecting under their own credentials and permissions.

**AI features, separated from automation with an AI label on it**
The product ships an AI inbox assistant, AI drafts and an AI Answers resolution feature on its paid tiers. The MCP server is deliberately not one of them: it is read-only for new connections, so the intelligence is entirely on the client side.

**RevOps role**
Inbound support and success inbox for SMB and mid-market teams, and, through a read-only MCP surface, a way to let an agent answer questions about customer history and support load without any ability to write into the queue.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The vendor's article states the connector registers itself, so the OAuth client ID and secret fields in the AI client are left empty, and warns explicitly that a Help Scout App ID and secret from My Apps are for the REST API and "won't work for the connector".

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.helpscout.net/mcp (docs: https://docs.helpscout.com/article/1779-connect-your-ai-agent-with-help-scout-to-search-conversations-and-pull-reports)

- [https://mcp.helpscout.net/mcp](https://mcp.helpscout.net/mcp)
- [https://docs.helpscout.com/article/1779-connect-your-ai-agent-with-help-scout-to-search-conversations-and-pull-reports](https://docs.helpscout.com/article/1779-connect-your-ai-agent-with-help-scout-to-search-conversations-and-pull-reports)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 380 entries that record an official or community MCP server carry a harvested tool list. The other 261 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's own article states "Your Help Scout account must have API access, which is included on the Standard, Plus, and Pro plans", and adds that report tools require Plus or Pro because the reporting API is not available on Standard. Published self-serve prices are Standard $25, Plus $45 and Pro $75 per user per month, with Pro routed to "Book a Demo"; a Free tier exists but does not carry API access and therefore cannot reach the MCP server.

**API documentation**

No documentation URL recorded.

528 of 784 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/helpscout](https://github.com/helpscout) tied to the vendor by rule 3, account website https://developer.helpscout.com has the vendor's domain, confidence strong

- **Public repositories**: 132, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 4 of them
- **Latest push**: 2026-08-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [app-template](https://github.com/helpscout/app-template) | docs or examples | Help Scout Developer Platform App Template | 14 | 2026-08-03 | |
| [helpscout-api-php-laravel](https://github.com/helpscout/helpscout-api-php-laravel) | API client | Service Provider and Facade for using the Help Scout API with Laravel and Lumen applications. | 9 | 2026-07-24 | 2.1.4 |
| [fe-yam-site](https://github.com/helpscout/fe-yam-site) | app | 🥔 Front-end Engineering: Hiring Project (Design Team) | 0 | 2026-06-23 | |
| [helpscout-api-php](https://github.com/helpscout/helpscout-api-php) | SDK | PHP Wrapper for the Help Scout API | 102 | 2026-06-15 | 3.10.3 |
| [beacon-ios-sdk](https://github.com/helpscout/beacon-ios-sdk) | SDK | The Beacon iOS SDK | 23 | 2026-04-27 | 4.1.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

513 of 784 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://docs.helpscout.com/article/1779-connect-your-ai-agent-with-help-scout-to-search-conversations-and-pull-reports](https://docs.helpscout.com/article/1779-connect-your-ai-agent-with-help-scout-to-search-conversations-and-pull-reports)
- [https://www.helpscout.com/pricing/](https://www.helpscout.com/pricing/)
- [https://mcp.helpscout.net/mcp](https://mcp.helpscout.net/mcp)

3 source URLs. Raw sources field, verbatim:

https://docs.helpscout.com/article/1779-connect-your-ai-agent-with-help-scout-to-search-conversations-and-pull-reports, https://www.helpscout.com/pricing/, https://mcp.helpscout.net/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.helpscout.net/mcp returned HTTP 401 with {"error":"invalid_token","error_description":"No authorization provided"}, confirming a live auth-gated server, and the endpoint is printed in Help Scout's own help-centre article. Note the domain: helpscout.net, not helpscout.com, which is a discovery trap for anyone checking only the marketing domain. TWO PLAN GATES STACK INSIDE ONE PRODUCT and both are documented by the vendor: Standard and above reaches the server at all, but the report tools return nothing on Standard because the reporting API is not included there, so an agent on a Standard plan will silently get an empty answer to a reporting question rather than an error a user can act on. Access is stated to be read-only for new connections with writes on the roadmap, so this is currently the safest inbox in this file to hand an unsupervised agent. The article also records a client-side gate that has nothing to do with Help Scout: on Claude Team and Enterprise only an Owner can add a custom connector, and on ChatGPT Business and Enterprise a workspace admin must enable Developer mode first. Help Scout was not listed in Claude's connector directory as of the article's own text, so it is added as a custom connector by URL. 2026-09-07: https://mcp.helpscout.net/mcp returned 401 to an MCP initialize POST. helpscout.net is Help Scout's own domain (https://mcp.helpscout.net/mcp).

**Provenance**

- **Entry id**: 14-help-scout

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 313

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
