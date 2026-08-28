# Apollo.io Sequences (Emailer Campaigns): MCP server status, API access gate and what it does

> Apollo's outbound-sequencing feature - multi-step, multi-channel (email/call/task) cadences that enroll... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Apollo.io Sequences (Emailer Campaigns)

# Apollo.io Sequences (Emailer Campaigns)

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [apollo.io](https://apollo.io) · entry id 02-apollo-io-sequences · source 02-engagement-outbound.md line 464

**What it does**
Apollo's outbound-sequencing feature - multi-step, multi-channel (email/call/task) cadences that enroll contacts pulled from Apollo's prospecting database and track send/reply state.

**AI features, separated from automation with an AI label on it**
No sequence-specific AI capability was independently verified beyond standard automation (step sequencing, contact-state tracking to prevent double-sends). Apollo's separate "AI Assistant"/"AI Research" features (documented under its data-enrichment entry) are account-level, not sequence-specific.

**RevOps role**
Execution/engagement module inside Apollo's core platform - same product surface as its prospecting/enrichment tool but a distinct API namespace for enrolling and managing cadences.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (Apollo.io sign-in/authorization flow; no API key required for this MCP)

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/apolloio/apollo-mcp-plugin (hosted server at https://mcp.apollo.io/mcp; listed in the official MCP Registry)

- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)
- [https://mcp.apollo.io/mcp](https://mcp.apollo.io/mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.apollo.io/developers](https://www.apollo.io/developers)
- [https://www.apollo.io/pricing](https://www.apollo.io/pricing)
- [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin)

3 source URLs. Raw sources field, verbatim:

https://www.apollo.io/developers, https://www.apollo.io/pricing, https://github.com/apolloio/apollo-mcp-plugin

**Notes, verbatim from the file**
Included here as its own entry (rather than folded into Apollo's data-enrichment listing) because it has a genuinely distinct API surface: POST /api/v1/emailer_campaigns to create a sequence and POST /api/v1/emailer_campaigns/{id}/add_contact_ids to enroll contacts, separate from the prospecting/enrichment endpoints. The official MCP server explicitly treats "outreach sequence workflows" as a separate capability group from prospecting/enrichment. Apollo's pricing page states API access generally is offered on "Custom" (negotiated/enterprise) plans; sequences are usable in-app on all tiers, but programmatic API access to them is enterprise-gated.

**Provenance**

- **Entry id**: 02-apollo-io-sequences

- **Source file**: 02-engagement-outbound.md

- **Source line**: 464

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
