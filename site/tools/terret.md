# Terret (BoostUp): MCP server status, API access gate and what it does

> A revenue-intelligence platform ("answer-to-action" engine) that analyzes call recordings and deal data to... No MCP found, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
Terret (BoostUp)

# Terret (BoostUp)

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.terret.ai (login portal at app.boostup.ai)](https://www.terret.ai (login portal at app.boostup.ai)) · entry id 04-terret · source 04-ai-sdr-agents.md line 334

**What it does**
A revenue-intelligence platform ("answer-to-action" engine) that analyzes call recordings and deal data to find winning patterns, generates sales playbooks, and pushes pre-call briefs/deal alerts/suggested talk tracks to reps in Slack - with some automated outreach-sequence drafting.

**AI features, separated from automation with an AI label on it**
Pattern analysis across calls/deals and automatic playbook generation are the confirmed AI pieces; "self-configuring agents" is vendor copy not independently verified. This is much closer to conversation-intelligence + forecasting than to outbound AI-SDR execution.

**RevOps role**
Revenue-intelligence/forecasting layer (product suite includes Terret Nexus, Terret Forecast, Terret Conversation Intelligence) - arguably better filed under conversation-intel (category 3) than AI SDR agents.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

The mcp_url field is empty on this entry. 17 of 293 entries are.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (no pricing published anywhere - /pricing is a demo booking form offering a 48-hour proof of concept - and the site names no API, developer docs or access condition)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.terret.ai](https://www.terret.ai)
- [https://www.terret.ai/pricing](https://www.terret.ai/pricing)

2 source URLs. Raw sources field, verbatim:

https://www.terret.ai, https://www.terret.ai/pricing

**Notes, verbatim from the file**
SWEEP FLAG - the product's login portal is at app.boostup.ai, strongly indicating Terret is a rebrand (or sub-brand) of BoostUp, an established revenue-intelligence/forecasting vendor. Included because the seed list named it explicitly, but its category fit here is weak - it's not an outbound prospecting agent. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.terret.ai/pricing): no pricing published anywhere - /pricing is a demo booking form offering a 48-hour proof of concept - and the site names no API, developer docs or access condition. 2026-09-02: re-checked terret.ai (no llms.txt), the official MCP registry (no terret or boostup entry) and a web search; no MCP server found.

**Provenance**

- **Entry id**: 04-terret

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 334

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
