# Expandi: MCP server status, API access gate and what it does

> Cloud-based LinkedIn (+ email) outreach automation tool that runs connection/message sequences from a... MCP unknown, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Expandi

# Expandi

[MCP unknown](../mcp/unknown.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [expandi.io](https://expandi.io) · entry id 02-expandi · source 02-engagement-outbound.md line 369

**What it does**
Cloud-based LinkedIn (+ email) outreach automation tool that runs connection/message sequences from a dedicated cloud IP per LinkedIn account.

**AI features, separated from automation with an AI label on it**
none-found - no distinct AI-labeled feature surfaced on the pricing page; personalization is template/variable-based, and media personalization runs through a third-party Senspark video/GIF integration rather than proprietary AI.

**RevOps role**
LinkedIn (+email) sequence-execution tool integrating into a stack only via webhooks/Zapier, since no public API was found.

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: n/a

- **Parsed URLs**: 1 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

n/a (vendor names an "Expandi MCP" on https://expandi.io/pricing/ but publishes no endpoint or docs; expandi.io/mcp/ returned 404 on 2026-09-02)

- [https://expandi.io/pricing/](https://expandi.io/pricing/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (one self-serve plan only, Business at $99/mo or $79/mo annual, and the help centre documents webhooks plus a reversed-webhook API endpoint with no plan restriction stated; the pricing page itself never mentions API)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://expandi.io/pricing/](https://expandi.io/pricing/)
- [https://www.salesforge.ai/directory/sales-tools/expandi](https://www.salesforge.ai/directory/sales-tools/expandi)

2 source URLs. Raw sources field, verbatim:

https://expandi.io/pricing/, https://www.salesforge.ai/directory/sales-tools/expandi

**Notes, verbatim from the file**
Multiple independent sources state Expandi has no public API, only webhook/Zapier/CRM connectors (HubSpot, Salesforce, Pipedrive). Base plan is $99/mo (or $79/mo annual) per LinkedIn account with no free tier. Subject to the same LinkedIn User Agreement automation restrictions as all tools in this section. [api_gate 2026-08-25] Reclassified unknown -> paid from the vendor's own page (https://expandi.io/pricing/): one self-serve plan only, Business at $99/mo or $79/mo annual, and the help centre documents webhooks plus a reversed-webhook API endpoint with no plan restriction stated; the pricing page itself never mentions API. 2026-09-02: mcp_status none-found -> unknown. The vendor's own pricing page https://expandi.io/pricing/ now says "Both offers include a 90 minute build session and early access to Expandi MCP" inside a Back to Pipeline promo running to September 21. That is a first-party mention of a server with no docs, endpoint, or setup page (expandi.io/mcp/ 404, zero official-registry hits), so under law 1 it records as unknown, not official.

**Provenance**

- **Entry id**: 02-expandi

- **Source file**: 02-engagement-outbound.md

- **Source line**: 369

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
