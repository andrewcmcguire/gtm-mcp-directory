# Kixie: MCP server status, API access gate and what it does

> Sales engagement / power-dialer platform (PowerCall) with multi-line parallel dialing, local-presence... No MCP found, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Kixie

# Kixie

[No MCP found](../mcp/none-found.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [kixie.com](https://kixie.com) · entry id 02-kixie · source 02-engagement-outbound.md line 84

**What it does**
Sales engagement / power-dialer platform (PowerCall) with multi-line parallel dialing, local-presence calling, and CRM-embedded calling/texting.

**AI features, separated from automation with an AI label on it**
Genuinely AI: "AI Human Voice Detection" that distinguishes a live person from a recording/voicemail to auto-connect reps, and "Kixie AI Insights" for reporting/analytics. Plain automation: the multi-line PowerDialer itself, ConnectionBoost local presence, and CRM activity logging.

**RevOps role**
Outbound/inbound calling and texting layer embedded directly into CRMs, competing more with dialer add-ons than full engagement suites.

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

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (Developer API is ticked on all three plans including the entry Professional tier and signup is self-serve with no card, but Kixie no longer publishes dollar prices and notes each account reaches different APIs by product level)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Place an outbound call](../jobs/place-outbound-call.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.kixie.com/developer/custom-crm-integration/](https://www.kixie.com/developer/custom-crm-integration/)
- [https://www.kixie.com/features/kixie-powercall/](https://www.kixie.com/features/kixie-powercall/)
- [https://www.kixie.com/sales-blog/claude-dialer-integration-with-kixie-for-ai-powered-outreach/](https://www.kixie.com/sales-blog/claude-dialer-integration-with-kixie-for-ai-powered-outreach/)
- [https://www.kixie.com/pricing/](https://www.kixie.com/pricing/)

4 source URLs. Raw sources field, verbatim:

https://www.kixie.com/developer/custom-crm-integration/, https://www.kixie.com/features/kixie-powercall/, https://www.kixie.com/sales-blog/claude-dialer-integration-with-kixie-for-ai-powered-outreach/, https://www.kixie.com/pricing/

**Notes, verbatim from the file**
A Kixie blog post titled "Claude Dialer Integration With Kixie for AI-Powered Outreach" describes MCP only as a DIY architectural pattern a developer could build on top of Kixie's existing API-key REST endpoints - it is not a published MCP server. No real implementation found on GitHub, mcp.so, glama.ai, or pulsemcp.com. Kixie has a documented API with apikey-based webhooks, but no pricing tier for it was found. [api_gate 2026-08-25] Reclassified unknown -> paid from the vendor's own page (https://www.kixie.com/pricing/): Developer API is ticked on all three plans including the entry Professional tier and signup is self-serve with no card, but Kixie no longer publishes dollar prices and notes each account reaches different APIs by product level.

**Provenance**

- **Entry id**: 02-kixie

- **Source file**: 02-engagement-outbound.md

- **Source line**: 84

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
