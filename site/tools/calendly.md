# Calendly: MCP server status, API access gate and what it does

> Prospect-facing scheduling links and booking pages that let invitees book meetings directly onto a rep's... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
Calendly

# Calendly

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

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

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developer.calendly.com/calendly-mcp-server (hosted at https://mcp.calendly.com); announcement: https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450; vendor blog: https://calendly.com/blog/mcp-server

- [https://developer.calendly.com/calendly-mcp-server](https://developer.calendly.com/calendly-mcp-server)
- [https://mcp.calendly.com](https://mcp.calendly.com)
- [https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450](https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450)
- [https://calendly.com/blog/mcp-server](https://calendly.com/blog/mcp-server)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free for the MCP server specifically - Calendly's own blog states "you can use Calendly MCP on any Calendly plan, including the free tier." Nuance: broader/advanced REST API functionality (webhooks, deeper integrations) has historically required the paid Standard tier ($10/user/mo)+ per third-party pricing trackers, so "free" applies to MCP access, not necessarily every API capability.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://developer.calendly.com/calendly-mcp-server](https://developer.calendly.com/calendly-mcp-server)
- [https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450](https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450)
- [https://calendly.com/blog/mcp-server](https://calendly.com/blog/mcp-server)
- [https://meetergo.com/en/magazine/calendly-plans](https://meetergo.com/en/magazine/calendly-plans)
- [https://www.cloudeagle.ai/blogs/calendly-pricing-guide](https://www.cloudeagle.ai/blogs/calendly-pricing-guide)
- [https://costbench.com/software/scheduling/calendly/](https://costbench.com/software/scheduling/calendly/)

6 source URLs. Raw sources field, verbatim:

https://developer.calendly.com/calendly-mcp-server, https://community.calendly.com/developer-faq-62/announcing-the-calendly-mcp-server-5450, https://calendly.com/blog/mcp-server, https://meetergo.com/en/magazine/calendly-plans, https://www.cloudeagle.ai/blogs/calendly-pricing-guide, https://costbench.com/software/scheduling/calendly/

**Notes, verbatim from the file**
MCP server released March 11, 2026 (community announcement date). First release "focused on scheduling workflows" (availability management, event-type config, meeting booking, link generation). Requires an MCP-compliant client supporting MCP 2025-03-26+ and streamable HTTP - ChatGPT's free tier doesn't support custom MCP connectors, so Calendly's MCP isn't reachable there without a paid ChatGPT plan.

**Provenance**

- **Entry id**: 10-calendly

- **Source file**: 10-scheduling-routing.md

- **Source line**: 7

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
