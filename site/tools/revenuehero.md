# RevenueHero: MCP server status, API access gate and what it does

> Instant meeting-scheduling and inbound-lead-routing tool that qualifies web-form leads against CRM data and... Official MCP, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
RevenueHero

# RevenueHero

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [revenuehero.io](https://revenuehero.io) · entry id 10-revenuehero · source 10-scheduling-routing.md line 84

**What it does**
Instant meeting-scheduling and inbound-lead-routing tool that qualifies web-form leads against CRM data and books them directly onto the right rep's calendar without a redirect.

**AI features, separated from automation with an AI label on it**
No genuine ML/AI capability independently found on public pages - routing is described purely in terms of round-robin/custom distribution rules and CRM-based qualification logic; no predictive scoring, send-time optimization, or NLP claims found. This is a rules-based routing/scheduling tool despite category adjacency to AI-branded competitors.

**RevOps role**
Inbound lead-routing plus instant meeting booking, positioned as a leaner/cheaper Chili Piper alternative for the same form-to-meeting conversion category.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Per-customer router token over an SSE endpoint, manually provisioned by RevenueHero - not a self-serve API-key flow.

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.revenuehero.io/resources/tales-of-ops (vendor's own case-study page - the only public documentation found; describes a live MCP server RevenueHero's own engineering team provisions per customer over an SSE endpoint with a router token and system prompt)

- [https://www.revenuehero.io/resources/tales-of-ops](https://www.revenuehero.io/resources/tales-of-ops)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown/enterprise-leaning - no public developer/API docs were found (help.revenuehero.io covers webhooks, JS events, and workflows only); the MCP server is obtainable only by contacting RevenueHero directly. The product itself is self-serve and tiered (Inbound Essentials ~$79/mo + $25-35/user; Enterprise ~$79/mo + $35-45/user; Lite $15/user; 14-day free trial, no perpetual free tier), but MCP access specifically is white-glove, not a plan checkbox.

83 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/revenuehero/sdk](https://github.com/revenuehero/sdk)

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)
- [Route an inbound lead](../jobs/route-inbound-lead.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.revenuehero.io/resources/tales-of-ops](https://www.revenuehero.io/resources/tales-of-ops)
- [https://www.revenuehero.io/pricing](https://www.revenuehero.io/pricing)
- [https://help.revenuehero.io/home/get-started](https://help.revenuehero.io/home/get-started)
- [https://help.revenuehero.io/llms.txt](https://help.revenuehero.io/llms.txt)
- [https://github.com/revenuehero/sdk](https://github.com/revenuehero/sdk)

5 source URLs. Raw sources field, verbatim:

https://www.revenuehero.io/resources/tales-of-ops, https://www.revenuehero.io/pricing, https://help.revenuehero.io/home/get-started, https://help.revenuehero.io/llms.txt, https://github.com/revenuehero/sdk

**Notes, verbatim from the file**
Do not confuse with RevenueCat (an unrelated in-app-subscriptions product) - a frequent search-namesake collision. A public SDK exists on GitHub (github.com/revenuehero/sdk, AGPL-3.0) but its purpose/API surface could not be confirmed from its README in this pass.

**Provenance**

- **Entry id**: 10-revenuehero

- **Source file**: 10-scheduling-routing.md

- **Source line**: 84

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
