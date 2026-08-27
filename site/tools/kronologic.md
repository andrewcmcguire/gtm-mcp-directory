# Kronologic: MCP server status, API access gate and what it does

> Automated meeting-booking platform that sends calendar invites directly (not just booking links) on a rep's... No MCP found, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
Kronologic

# Kronologic

[No MCP found](../mcp/none-found.md)
[Gate unknown](../gates/unknown.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [kronologic.com](https://kronologic.com) · entry id 10-kronologic · source 10-scheduling-routing.md line 103

**What it does**
Automated meeting-booking platform that sends calendar invites directly (not just booking links) on a rep's behalf and negotiates meeting times over email, aimed mainly at customer-expansion motions (renewals, upsells, reactivations) as well as inbound.

**AI features, separated from automation with an AI label on it**
Vendor claims the system reads reply emails, classifies intent (interested / not now / wrong person / question), and negotiates a time in natural language while staying calendar-aware - plausibly real NLP/intent classification, but no public detail on model type, training, or accuracy is disclosed; treat as an unverified vendor claim. Account-owner routing and availability-matching underneath is standard rules/calendar-API logic.

**RevOps role**
Calendar-invite-first meeting-booking automation, most differentiated for customer-success/expansion motions rather than net-new inbound routing.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown for a general API/developer surface (no API/webhook/SDK docs found anywhere on the site), but Kronologic is notably the only tool in this file with a genuine self-serve Free tier ($0/mo: booking page + Google Calendar + 2 meeting types) - though the AI "negotiation" features that differentiate it are gated to paid Pro ($15/seat/mo) and Team ($49/seat/mo) tiers.

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)
- [Route an inbound lead](../jobs/route-inbound-lead.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.kronologic.com/](https://www.kronologic.com/)
- [https://www.kronologic.com/pricing/](https://www.kronologic.com/pricing/)
- [https://www.kronologic.com/calendar-link-vs-kronologic](https://www.kronologic.com/calendar-link-vs-kronologic)

3 source URLs. Raw sources field, verbatim:

https://www.kronologic.com/, https://www.kronologic.com/pricing/, https://www.kronologic.com/calendar-link-vs-kronologic

**Notes, verbatim from the file**
Vendor domain redirects from kronologic.ai to kronologic.com (canonical). No MCP or public API surface found in any registry (mcp.so, glama.ai, pulsemcp.com) or on the vendor's own site after repeated targeted checks - a genuine gap, not a search failure. [api_gate 2026-08-25] Re-checked and left unknown, honestly: pricing is published (Free $0, Pro $15/seat/mo, Team $49/seat/mo, Enterprise custom) but no tier mentions API, kronologic.com/api returns 404, docs.kronologic.com does not resolve, and no API or Developers link appears in nav or footer. Checked against https://www.kronologic.com/pricing.

**Provenance**

- **Entry id**: 10-kronologic

- **Source file**: 10-scheduling-routing.md

- **Source line**: 103

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
