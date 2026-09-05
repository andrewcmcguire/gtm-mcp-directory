# Cal.com: MCP server status, API access gate and what it does

> Open-source scheduling infrastructure - booking pages, event types, and a scheduling API/platform - offered... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
Cal.com

# Cal.com

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [cal.com](https://cal.com) · entry id 10-cal-com · source 10-scheduling-routing.md line 26

**What it does**
Open-source scheduling infrastructure - booking pages, event types, and a scheduling API/platform - offered both as a free, self-hostable open-source product and as hosted SaaS.

**AI features, separated from automation with an AI label on it**
No distinct AI-driven scheduling-optimization or LLM feature was independently verified on the core product. The MCP server itself is a connectivity feature (translates natural-language requests like "what bookings do I have this week" into structured booking/event-type API calls) rather than an AI capability of the product itself.

**RevOps role**
Same category role as Calendly (prospect-facing meeting-booking layer) but positioned as the open-source, developer-controlled alternative - appeals to GTM engineers who want to self-host or avoid vendor lock-in.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Two paths. Hosted server (mcp.cal.com) uses OAuth 2.1 - "your client handles the authorization flow automatically," no API key needed. Self-hosted/local server uses a Cal.com API key generated at Settings -> Developer -> API Keys, passed via a CAL_API_KEY environment variable, run over stdio with Node.js (npx @calcom/cal-mcp@latest).

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/calcom/cal-mcp](https://github.com/calcom/cal-mcp)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/calcom/cal-mcp (repo self-describes as "the official MCP server for cal.com"); docs at https://cal.com/docs/mcp-server; also hosted at mcp.cal.com

- [https://github.com/calcom/cal-mcp](https://github.com/calcom/cal-mcp)
- [https://cal.com/docs/mcp-server](https://cal.com/docs/mcp-server)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - Cal.com's Free plan has "no usage limits" and includes 100+ app integrations; API-key generation is a self-serve account setting in documentation found, not gated behind a paid tier. Cal.com is also open-source and self-hostable via Docker - a genuinely free path Calendly does not offer. Caveat: "Custom APIs" / "Additional APIs" language appears in the Teams ($12/user/mo) and Organizations ($28/user/mo) plan marketing copy, suggesting some advanced API surface (Platform/Orgs-prefixed endpoints) is tier-gated even though basic API-key access is not.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/calcom/cal-mcp](https://github.com/calcom/cal-mcp)
- [https://github.com/calcom/cal-mcp/blob/main/README.md](https://github.com/calcom/cal-mcp/blob/main/README.md)

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/calcom/cal-mcp](https://github.com/calcom/cal-mcp)
- [https://github.com/calcom/cal-mcp/blob/main/README.md](https://github.com/calcom/cal-mcp/blob/main/README.md)
- [https://cal.com/docs/mcp-server](https://cal.com/docs/mcp-server)
- [https://cal.com/pricing](https://cal.com/pricing)
- [https://cal.com/docs/api-reference/v2/introduction](https://cal.com/docs/api-reference/v2/introduction)
- [https://www.pulsemcp.com/servers/aiwerk-cal-com](https://www.pulsemcp.com/servers/aiwerk-cal-com)
- [https://www.pulsemcp.com/servers/calcom-calendar](https://www.pulsemcp.com/servers/calcom-calendar)

7 source URLs. Raw sources field, verbatim:

https://github.com/calcom/cal-mcp, https://github.com/calcom/cal-mcp/blob/main/README.md, https://cal.com/docs/mcp-server, https://cal.com/pricing, https://cal.com/docs/api-reference/v2/introduction, https://www.pulsemcp.com/servers/aiwerk-cal-com, https://www.pulsemcp.com/servers/calcom-calendar

**Notes, verbatim from the file**
8 MCP tools enabled by default (getBooking, getBookings, createBooking, rescheduleBooking, cancelBooking, getEventTypes, getEventTypeById, updateEventType, deleteEventType); a --all-tools flag exposes the full Cal.com API surface. Repo flags itself as under active/rapid development ("features and APIs subject to rapid changes"). Distinct from at least four community-built Cal.com MCP servers also found on GitHub/PulseMCP (mnicole-dev/calcom-mcp-server, Danielpeter-99/calcom-mcp, bcharleson/calcom-cli, mumunha/cal_dot_com_mcpserver, listed on PulseMCP as "Cal.com AIWerk" and "Cal.com Calendar") - do not confuse those community projects with the official calcom/cal-mcp repo.

**Provenance**

- **Entry id**: 10-cal-com

- **Source file**: 10-scheduling-routing.md

- **Source line**: 26

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
