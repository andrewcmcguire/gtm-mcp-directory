# HubSpot Breeze (AI Prospecting Agent): MCP server status, API access gate and what it does

> Monitors accounts for buying signals (funding, leadership changes, site visits) via integrated data providers... No MCP found, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
HubSpot Breeze (AI Prospecting Agent)

# HubSpot Breeze (AI Prospecting Agent)

[No MCP found](../mcp/none-found.md)
[Paid, self-serve](../gates/paid.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.hubspot.com/products/sales/ai-prospecting-agent](https://www.hubspot.com/products/sales/ai-prospecting-agent) · entry id 04-hubspot-breeze · source 04-ai-sdr-agents.md line 239

**What it does**
Monitors accounts for buying signals (funding, leadership changes, site visits) via integrated data providers (ZoomInfo, Apollo, Surfe, Seamless), identifies decision-makers, and drafts personalized outreach emails in a rep's voice; can send with human review or in a fully autonomous send mode. Does not book meetings itself - it hands off qualified leads to reps.

**AI features, separated from automation with an AI label on it**
Signal monitoring and voice-matched drafting are genuinely automated; the reviewed-vs-autonomous send toggle is a real, verifiable agentic feature (not just template automation) - this is one of the more precisely documented entries in the category.

**RevOps role**
Native prospecting layer for shops already on HubSpot Sales Hub - competes directly with standalone tools like AiSDR/Regie for HubSpot-native teams.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

The mcp_url field is empty on this entry. 17 of 293 entries are.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, bundled - included in Starter/Professional/Enterprise Sales Hub editions, billed per-lead ($1/lead recommended) against pooled "HubSpot Credits"; no separate subscription

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.hubspot.com/products/sales/ai-prospecting-agent](https://www.hubspot.com/products/sales/ai-prospecting-agent)
- [https://developers.hubspot.com/mcp](https://developers.hubspot.com/mcp)

2 source URLs. Raw sources field, verbatim:

https://www.hubspot.com/products/sales/ai-prospecting-agent, https://developers.hubspot.com/mcp

**Notes, verbatim from the file**
HubSpot has an official, platform-wide MCP server (OAuth 2.0/2.1, developers.hubspot.com/mcp) covering CRM objects (contacts, deals, engagements, etc.) - but nothing found confirming the Breeze Prospecting Agent specifically is exposed through it. Performance claims ("76% more qualified leads," "80% more meetings," "26% higher win rate") are vendor-reported and unsourced beyond the marketing page - mark as vendor-copy-only. 2026-09-02: re-checked https://developers.hubspot.com/mcp: it lists CRM objects, engagements, org context and marketing content and says tools will grow over time, but names no Breeze or prospecting-agent tool. The official MCP registry holds only third-party HubSpot servers. none-found stands for the Prospecting Agent specifically.

**Provenance**

- **Entry id**: 04-hubspot-breeze

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 239

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
