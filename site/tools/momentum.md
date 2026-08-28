# Momentum: MCP server status, API access gate and what it does

> Turns sales call and CRM activity into automatic Slack deal-channel updates, deal-risk alerts, and CRM field... No MCP found, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Momentum

# Momentum

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [momentum.io](https://momentum.io) · entry id 03-momentum · source 03-conversation-intel.md line 163

**What it does**
Turns sales call and CRM activity into automatic Slack deal-channel updates, deal-risk alerts, and CRM field updates ("revenue orchestration").

**AI features, separated from automation with an AI label on it**
AI-based risk detection that parses calls, Slack threads, and CRM data for silence, negative sentiment, competitor mentions, and churn/blocker signals, plus AI-generated call summaries posted to Slack. Much of the orchestration itself (channel creation, routing) is rules/automation rather than AI.

**RevOps role**
Slack/CRM-facing deal-risk alerting layer sitting on top of call and pipeline data.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a for MCP. The REST API uses an X-API-Key header, and API access must first be enabled for the org by Momentum's support team.

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only in practice - API access requires contacting Momentum support to enable it before you can even create a key; no public self-serve pricing (third-party trackers cite plans starting around $828, quote-based).

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.momentum.io/](https://www.momentum.io/)
- [https://docs.momentum.io/api-access](https://docs.momentum.io/api-access)
- [https://www.momentum.io/pricing](https://www.momentum.io/pricing)
- [https://www.trustradius.com/products/dealmomentum/pricing](https://www.trustradius.com/products/dealmomentum/pricing)

4 source URLs. Raw sources field, verbatim:

https://www.momentum.io/, https://docs.momentum.io/api-access, https://www.momentum.io/pricing, https://www.trustradius.com/products/dealmomentum/pricing

**Notes, verbatim from the file**
A search for "Momentum MCP" surfaces an unrelated healthcare-sector company also branded "Momentum" (FHIR/Apple Health MCP servers) - not to be confused with momentum.io.

**Provenance**

- **Entry id**: 03-momentum

- **Source file**: 03-conversation-intel.md

- **Source line**: 163

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
