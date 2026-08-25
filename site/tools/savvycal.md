# SavvyCal: MCP server status, API access gate and what it does

> Prospect-facing scheduling/booking-page tool (Calendly competitor) built around letting invitees overlay... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
SavvyCal

# SavvyCal

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [savvycal.com](https://savvycal.com) · entry id 10-savvycal · source 10-scheduling-routing.md line 179

**What it does**
Prospect-facing scheduling/booking-page tool (Calendly competitor) built around letting invitees overlay their own calendar on the organizer's availability, with Collective/Round-Robin/Group team-scheduling modes.

**AI features, separated from automation with an AI label on it**
No AI features found or marketed on the vendor's public pages - this is classic rules-based calendar automation (buffers, meeting limits, time-blocking, branded booking links), not an AI product.

**RevOps role**
Same prospect-facing booking-link role as Calendly/Cal.com, positioned as a UX-differentiated alternative (calendar-overlay booking flow).

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: API key (SAVVYCAL_API_KEY env var, a personal access token from SavvyCal's Developer Settings). MIT-licensed repo, not explicitly disclaiming official/unofficial status but built by a third-party GitHub account, not SavvyCal's own org.

- **Parsed URLs**: 1 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/arturkoter/savvycal-mcp-server

- [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - SavvyCal has a genuine free tier for the product itself ("kick the tires for free"), but "API & Webhooks" appears only in the Premium tier ($17/user/mo) feature list, not Basic ($10/user/mo) - API access is gated above both the free tier and the entry paid tier.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server)

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://savvycal.com](https://savvycal.com)
- [https://savvycal.com/pricing](https://savvycal.com/pricing)
- [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server)

3 source URLs. Raw sources field, verbatim:

https://savvycal.com, https://savvycal.com/pricing, https://github.com/arturkoter/savvycal-mcp-server

**Notes, verbatim from the file**
developers.savvycal.com exists as a dedicated dev-docs section but detailed content wasn't retrievable in this research pass.

**Provenance**

- **Entry id**: 10-savvycal

- **Source file**: 10-scheduling-routing.md

- **Source line**: 179

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
