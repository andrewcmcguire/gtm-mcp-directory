# Snitcher: MCP server status, API access gate and what it does

> Identifies anonymous website visitor companies via IP-to-company database matching, tracks on-site behavior... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Snitcher

# Snitcher

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.snitcher.com](https://www.snitcher.com) · entry id 05-snitcher · source 05-signals-intent-abm.md line 424

**What it does**
Identifies anonymous website visitor companies via IP-to-company database matching, tracks on-site behavior (pages viewed, session length, return visits) via an embedded tracking script, and surfaces "hot lead" alerts plus verified contacts.

**AI features, separated from automation with an AI label on it**
No explicit AI/ML claims found for the core detection engine - detection is deterministic IP-to-company matching plus rules-based intent/behavior scoring (e.g., pricing-page-visit alerts). Any "AI" references on the site point to customer logos, not Snitcher's own technology.

**RevOps role**
Visitor ID + real-time intent alerting (e.g., Slack ping when a target account hits the pricing page) + contact reveal, with a native MCP integration.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - vendor changelog points to docs.snitcher.com for authentication specifics, not independently confirmed.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.snitcher.com/changelog/point-claude-at-snitcher/](https://www.snitcher.com/changelog/point-claude-at-snitcher/)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.snitcher.com/changelog/point-claude-at-snitcher/

- [https://www.snitcher.com/changelog/point-claude-at-snitcher/](https://www.snitcher.com/changelog/point-claude-at-snitcher/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Find a work email address](../jobs/find-work-email.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.snitcher.com/](https://www.snitcher.com/)
- [https://www.snitcher.com/pricing](https://www.snitcher.com/pricing)
- [https://www.snitcher.com/changelog/point-claude-at-snitcher/](https://www.snitcher.com/changelog/point-claude-at-snitcher/)

3 source URLs. Raw sources field, verbatim:

https://www.snitcher.com/, https://www.snitcher.com/pricing, https://www.snitcher.com/changelog/point-claude-at-snitcher/

**Notes, verbatim from the file**
Self-serve throughout ("Start for free"), 14-day trial, no card required. Volume-tiered pricing $49/mo (0-50 companies identified) up to $529/mo (4,001-5,000 companies); a discounted "Startup Program" requires contacting sales. Changelog dated June 26, 2026 - a recent addition, part of a broader 2026 wave of visitor-ID vendors bolting on MCP servers.

**Provenance**

- **Entry id**: 05-snitcher

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 424

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
