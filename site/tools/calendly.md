# Calendly: MCP server status, API access gate and what it does

> Prospect-facing scheduling links and booking pages that let invitees book meetings directly onto a rep's... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
Calendly

# Calendly

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-09-07
CLI: calendly-axi (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [calendly.com](https://calendly.com) · entry id 10-calendly · source 10-scheduling-routing.md line 7

**What it does**
Prospect-facing scheduling links and booking pages that let invitees book meetings directly onto a rep's calendar based on defined availability rules.

**AI features, separated from automation with an AI label on it**
The core booking-page product is classic rules-based calendar automation (availability rules, buffers, round robin) - not AI. Calendly separately markets "Callie," an AI relationship-assistant feature (beta) - a genuinely different capability from booking automation, but described only in vendor's own material, unverified independently. The MCP server itself is not an AI feature; it is a structured API surface an AI agent calls to execute the same rules-based booking actions via natural language.

**RevOps role**
Prospect-facing meeting-booking layer - the "here's my link, pick a time" step at the top of a GTM funnel, usually paired with a routing/qualification layer upstream (Chili Piper, RevenueHero, LeanData).

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.1 Authorization Code + PKCE (S256) with Dynamic Client Registration (RFC 7591). Personal access tokens are not supported. Fully hosted by Calendly at mcp.calendly.com - no self-hosting option.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://developer.calendly.com/calendly-mcp-server](https://developer.calendly.com/calendly-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.calendly.com ; https://developer.calendly.com/calendly-mcp-server (hosted at https://mcp.calendly.com); announcement: https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450; vendor blog: https://calendly.com/blog/mcp-server

- [https://mcp.calendly.com](https://mcp.calendly.com)
- [https://developer.calendly.com/calendly-mcp-server](https://developer.calendly.com/calendly-mcp-server)
- [https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450](https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450)
- [https://calendly.com/blog/mcp-server](https://calendly.com/blog/mcp-server)

**What this server exposes**

- **Tools named**: 36
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-10
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **availability-get_user_availability_schedule** Get a schedule's details evidence: in the vendor docs · calling it writes

- **availability-list_user_availability_schedules** List user availability schedules evidence: in the vendor docs · calling it reads

- **availability-list_user_busy_times** List busy times within a range evidence: in the vendor docs · calling it reads

- **event_types-create_event_type** Create a new event type evidence: in the vendor docs · calling it writes

- **event_types-get_event_type** Retrieve event type details evidence: in the vendor docs · calling it reads

- **event_types-list_event_type_availability_schedule** List availability schedules evidence: in the vendor docs · calling it reads

- **event_types-list_event_type_available_times** List available time slots evidence: in the vendor docs · calling it reads

- **event_types-list_event_types** List event types for a user/org evidence: in the vendor docs · calling it reads

- **event_types-update_event_type** Update event type details evidence: in the vendor docs · calling it writes

- **event_types-update_event_type_availability_schedule** Update an availability schedule evidence: in the vendor docs · calling it writes

- **list_calendly_skills** List available Calendly skills evidence: in the vendor docs · calling it reads

- **load_calendly_skill** Retrieve a specific Calendly skill evidence: in the vendor docs · calling it reads

- **locations-list_user_meeting_locations** List a user's meeting locations evidence: in the vendor docs · calling it reads

- **meetings-cancel_event** Cancel a scheduled event evidence: in the vendor docs · calling it reads

- **meetings-create_invitee** Create a new booking (Scheduling API). Requires a paid Calendly plan evidence: in the vendor docs · calling it writes

- **meetings-create_invitee_no_show** Mark invitee as no-show evidence: in the vendor docs · calling it reads

- **meetings-delete_invitee_no_show** Remove no-show status evidence: in the vendor docs · calling it writes

- **meetings-get_event** Retrieve event details evidence: in the vendor docs · calling it reads

- **meetings-get_event_invitee** Get invitee details evidence: in the vendor docs · calling it reads

- **meetings-get_invitee_no_show** Get no-show details evidence: in the vendor docs · calling it reads

- **meetings-list_event_invitees** List invitees for an event evidence: in the vendor docs · calling it reads

- **meetings-list_events** List scheduled events evidence: in the vendor docs · calling it reads

- **organizations-create_organization_invitation** Invite a user evidence: in the vendor docs · calling it reads

- **organizations-get_organization** Retrieve org details evidence: in the vendor docs · calling it reads

- **organizations-get_organization_membership** Get membership details evidence: in the vendor docs · calling it reads

- **organizations-list_organization_invitations** List pending invitations evidence: in the vendor docs · calling it reads

- **organizations-list_organization_memberships** List organization members evidence: in the vendor docs · calling it reads

- **organizations-revoke_organization_invitation** Revoke an invitation evidence: in the vendor docs · calling it reads

- **routing_forms-get_routing_form** Get form details. Requires a Calendly Teams plan or higher evidence: in the vendor docs · calling it reads

- **routing_forms-get_routing_form_submission** Retrieve a submission. Requires a Calendly Teams plan or higher evidence: in the vendor docs · calling it reads

- **routing_forms-list_routing_form_submissions** List form submissions. Requires a Calendly Teams plan or higher evidence: in the vendor docs · calling it reads

- **routing_forms-list_routing_forms** List routing forms. Requires a Calendly Teams plan or higher evidence: in the vendor docs · calling it reads

- **scheduling_links-create_single_use_scheduling_link** Create a single-use scheduling link from existing event type evidence: in the vendor docs · calling it writes

- **shares-create_share** Create and customize single-use scheduling link from existing event type evidence: in the vendor docs · calling it writes

- **users-get_current_user** Get the authenticated user evidence: in the vendor docs · calling it reads

- **users-get_user** Get a specific user by UUID evidence: in the vendor docs · calling it reads

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-10. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: calendly-axi
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-10

Install, as the source shows it:

```
npm install -g calendly-axi
```

quoted from [https://www.npmjs.com/package/calendly-axi](https://www.npmjs.com/package/calendly-axi) on 2026-09-10, via npm, a third party source

```
npm install -g calendly-cli
```

quoted from [https://www.npmjs.com/package/calendly-cli](https://www.npmjs.com/package/calendly-cli) on 2026-09-10, via npm, a third party source

Packages seen, with the version on 2026-09-10:

- [npm: calendly-axi 1.2.0, third party](https://www.npmjs.com/package/calendly-axi)
- [npm: calendly-cli 1.0.5, third party](https://www.npmjs.com/package/calendly-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-10.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free for the MCP server specifically - Calendly's own blog states "you can use Calendly MCP on any Calendly plan, including the free tier." Nuance: broader/advanced REST API functionality (webhooks, deeper integrations) has historically required the paid Standard tier ($10/user/mo)+ per third-party pricing trackers, so "free" applies to MCP access, not necessarily every API capability.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/calendly](https://github.com/calendly) tied to the vendor by rule 3, account website https://calendly.com/ has the vendor's domain, confidence strong

- **Public repositories**: 6, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-03-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [buzzwordcrm](https://github.com/calendly/buzzwordcrm) | docs or examples | BuzzwordCRM is a sample application that demonstrates how to build applications using Calendly's v2 api. | 125 | 2026-03-03 | |
| [cypress_tictactoe](https://github.com/calendly/cypress_tictactoe) | other | | 0 | 2025-09-16 | |
| [gatsby-plugin-guru-export](https://github.com/calendly/gatsby-plugin-guru-export) | plugin or integration | | 0 | 2023-07-19 | |
| [gatsby-scroll-repro](https://github.com/calendly/gatsby-scroll-repro) | other | | 0 | 2023-06-05 | |
| [embed-demo](https://github.com/calendly/embed-demo) | docs or examples | | 1 | 2023-04-22 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developer.calendly.com/calendly-mcp-server](https://developer.calendly.com/calendly-mcp-server)
- [https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450](https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450)
- [https://calendly.com/blog/mcp-server](https://calendly.com/blog/mcp-server)
- [https://meetergo.com/en/magazine/calendly-plans](https://meetergo.com/en/magazine/calendly-plans)
- [https://www.cloudeagle.ai/blogs/calendly-pricing-guide](https://www.cloudeagle.ai/blogs/calendly-pricing-guide)
- [https://costbench.com/software/scheduling/calendly/](https://costbench.com/software/scheduling/calendly/)
- [https://mcp.calendly.com](https://mcp.calendly.com)

7 source URLs. Raw sources field, verbatim:

https://developer.calendly.com/calendly-mcp-server, https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450, https://calendly.com/blog/mcp-server, https://meetergo.com/en/magazine/calendly-plans, https://www.cloudeagle.ai/blogs/calendly-pricing-guide, https://costbench.com/software/scheduling/calendly/, https://mcp.calendly.com

**Notes, verbatim from the file**
MCP server released March 11, 2026 (community announcement date). First release "focused on scheduling workflows" (availability management, event-type config, meeting booking, link generation). Requires an MCP-compliant client supporting MCP 2025-03-26+ and streamable HTTP - ChatGPT's free tier doesn't support custom MCP connectors, so Calendly's MCP isn't reachable there without a paid ChatGPT plan. 2026-09-07: https://mcp.calendly.com returned 401 to an MCP initialize POST (https://mcp.calendly.com).

**Provenance**

- **Entry id**: 10-calendly

- **Source file**: 10-scheduling-routing.md

- **Source line**: 7

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-10

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
