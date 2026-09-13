# Mixmax: MCP server status, API access gate and what it does

> Gmail-native sales engagement layer that runs email sequences, tracking, calendaring and meeting notes from... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Mixmax

# Mixmax

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [mixmax.com](https://mixmax.com) · entry id 02-mixmax · source 02-engagement-outbound.md line 483

**What it does**
Gmail-native sales engagement layer that runs email sequences, tracking, calendaring and meeting notes from inside the inbox.

**AI features, separated from automation with an AI label on it**
"Meeting Copilot" records and summarises calls into topics and action items; AI sequence and email drafting plus reply assistance. The sequencing, tracking and scheduling engine itself is automation, not AI.

**RevOps role**
Inbox-side sequencing and meeting-scheduling layer for AE and CS teams that live in Gmail rather than in a full Outreach or Salesloft deployment.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 authorization code flow, scoped to the connecting user's account. Read-only.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: auth wall at every path, not proven a server
- **Endpoint URL**: [https://mcp.mixmax.com/mcp](https://mcp.mixmax.com/mcp)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-04 the recorded URL answered an auth challenge, but so did a path on that host which cannot exist, so the challenge proves a wall rather than a running MCP server.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.mixmax.com/mcp (docs: https://success.mixmax.com/en/articles/14298142-mixmax-mcp-server; vendor guide: https://www.mixmax.com/mcp-server-guide)

- [https://mcp.mixmax.com/mcp](https://mcp.mixmax.com/mcp)
- [https://success.mixmax.com/en/articles/14298142-mixmax-mcp-server](https://success.mixmax.com/en/articles/14298142-mixmax-mcp-server)
- [https://www.mixmax.com/mcp-server-guide](https://www.mixmax.com/mcp-server-guide)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 380 entries that record an official or community MCP server carry a harvested tool list. The other 261 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. Two separate gates, and the split is the useful fact. The MCP server is free to every Mixmax customer including the $0 Free plan per the vendor help doc, but meeting data requires the Meeting Copilot product ($29/user/mo annual, $34 monthly). The REST API is a higher gate: Mixmax's own pricing page includes "Mixmax API" only on Engagement Copilot ($49/mo annual), Mixmax Suite ($89/mo annual) and Mixmax for Teams. A third-party review states API is restricted to annual Growth+/Enterprise plans, which does not match the current published plan names, so trust the pricing page.

**API documentation**

[https://developer.mixmax.com/reference/getting-started-with-the-api](https://developer.mixmax.com/reference/getting-started-with-the-api)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/mixmaxhq](https://github.com/mixmaxhq) tied to the vendor by rule 3, account website https://www.mixmax.com/engineering has the vendor's domain, confidence strong

- **Public repositories**: 105, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-01

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [email-setup](https://github.com/mixmaxhq/email-setup) | other | Collection of utilities for checking email configuration settings. | 2 | 2026-09-01 | v1.1.2 |
| [eslint-config-mixmax](https://github.com/mixmaxhq/eslint-config-mixmax) | other | Mixmax's JS linter configuration. | 1 | 2026-08-19 | v6.0.1 |
| [custody-probe](https://github.com/mixmaxhq/custody-probe) | other | Report the state of child processes to custody. | 0 | 2026-07-10 | |
| [aws-instance-metadata](https://github.com/mixmaxhq/aws-instance-metadata) | other | | 2 | 2026-07-10 | v2.1.3 |
| [check-dependencies-except-peer](https://github.com/mixmaxhq/check-dependencies-except-peer) | other | Ensure that your package-lock matches your package and is self-consistent, and ignore missing peerDependencies | 1 | 2026-07-10 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Book a meeting](../jobs/book-a-meeting.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 784 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://success.mixmax.com/en/articles/14298142-mixmax-mcp-server](https://success.mixmax.com/en/articles/14298142-mixmax-mcp-server)
- [https://www.mixmax.com/mcp-server-guide](https://www.mixmax.com/mcp-server-guide)
- [https://www.mixmax.com/pricing](https://www.mixmax.com/pricing)
- [https://developer.mixmax.com/](https://developer.mixmax.com/)
- [https://success.mixmax.com/en/articles/11643056-mixmax-rest-api](https://success.mixmax.com/en/articles/11643056-mixmax-rest-api)

5 source URLs. Raw sources field, verbatim:

https://success.mixmax.com/en/articles/14298142-mixmax-mcp-server, https://www.mixmax.com/mcp-server-guide, https://www.mixmax.com/pricing, https://developer.mixmax.com/, https://success.mixmax.com/en/articles/11643056-mixmax-rest-api

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep, closing a real structural gap: this file previously had no Gmail-native incumbent at all despite covering the full pure-play sequencer market. NOTABLE LIMIT: all MCP tools are read-only today. The vendor doc explicitly states action capabilities (sequence enrollment, sending, template management) are "on the roadmap" and not shipped, so an agent can report on sequences but cannot run them. Two tool groups exist: Meetings (calendar search, AI summaries, assistant settings) and Sequences (list sequences, stage detail, open/click/reply/bounce rates, enrollment checks, daily send volume, validation). The MCP-free-but-API-paid split is unusual enough to be worth a segment on its own: the agent door is cheaper than the developer door.

**Provenance**

- **Entry id**: 02-mixmax

- **Source file**: 02-engagement-outbound.md

- **Source line**: 483

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
