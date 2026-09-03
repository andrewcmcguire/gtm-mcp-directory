# LeanData: MCP server status, API access gate and what it does

> GTM lead-routing/orchestration platform for Salesforce-centric revenue teams - routes leads, signals, and... MCP unknown, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
LeanData

# LeanData

[MCP unknown](../mcp/unknown.md)
[Enterprise only](../gates/enterprise-only.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [leandata.com](https://leandata.com) · entry id 10-leandata · source 10-scheduling-routing.md line 198

**What it does**
GTM lead-routing/orchestration platform for Salesforce-centric revenue teams - routes leads, signals, and buying-group activity to the right rep/queue across the customer lifecycle, plus a scheduling add-on (BookIt).

**AI features, separated from automation with an AI label on it**
Vendor markets "AI-assisted routing," an "AI SDR routing" capability, and a "LeanData AI" platform component, plus positions itself as "the backbone for AI-ready infrastructure" for GTM agents - these are vendor-stated capabilities with no independent technical breakdown found distinguishing genuine ML-driven routing decisions from LeanData's historically rules/workflow-engine-based core product.

**RevOps role**
Internal inbound-lead-routing/orchestration layer sitting in front of Salesforce, deciding who a lead or signal goes to and triggering the right next action (including handing off to BookIt for scheduling).

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: vendor-stated only, from the release post: "handled through Salesforce OAuth for admins and reps, and through a one-time code option for external partners or agents"; no docs page confirms this.

- **Parsed URLs**: 1 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

n/a (the only first-party surface is the Q2 2026 release post, https://www.leandata.com/blog/leandata-q2-2026-release-audit-logs-best-fit-assignment-bookit-mcp/, which publishes no endpoint or docs)

- [https://www.leandata.com/blog/leandata-q2-2026-release-audit-logs-best-fit-assignment-bookit-mcp/](https://www.leandata.com/blog/leandata-q2-2026-release-audit-logs-best-fit-assignment-bookit-mcp/)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only - pricing page confirms no free tier ("Setup and onboarding are tailored and billed separately for all packages"); three custom-quoted editions (Standard/Advanced/Premium) plus BookIt Scheduling and Buying Groups as separate paid add-ons; no transparent self-serve pricing found.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Route an inbound lead](../jobs/route-inbound-lead.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://leandata.com](https://leandata.com)
- [https://leandata.com/platform/pricing/](https://leandata.com/platform/pricing/)
- [https://docs.leandata.com](https://docs.leandata.com)
- [https://www.leandata.com/blog/leandata-q2-2026-release-audit-logs-best-fit-assignment-bookit-mcp/](https://www.leandata.com/blog/leandata-q2-2026-release-audit-logs-best-fit-assignment-bookit-mcp/)

4 source URLs. Raw sources field, verbatim:

https://leandata.com, https://leandata.com/platform/pricing/, https://docs.leandata.com, https://www.leandata.com/blog/leandata-q2-2026-release-audit-logs-best-fit-assignment-bookit-mcp/

**Notes, verbatim from the file**
LeanData's own homepage references a "BookIt MCP (Model Context Protocol server)" tied to a "Q2 2026 release," but no dedicated MCP docs page, repo, or endpoint could be located - docs.leandata.com search returned nothing and leandata.com/platform/bookit/ 404'd. This is a real, sourced mention of an MCP claim without a verifiable URL, so per this directory's law (an MCP claim requires a URL) it is recorded as mcp_status: unknown rather than official - worth a manual re-check once LeanData's Q2 2026 release material is more discoverable. 2026-09-02: re-checked, mcp_status stays unknown. The release material is discoverable now: https://www.leandata.com/blog/leandata-q2-2026-release-audit-logs-best-fit-assignment-bookit-mcp/ (May 21, 2026) says "The BookIt MCP server exposes scheduling functionality through a standard interface that any MCP-compatible AI client can connect to", with separate admin and rep capabilities and Salesforce OAuth plus a one-time code for external agents. It still publishes no endpoint, docs page, or setup guide, and the official MCP registry has no leandata or bookit entry, so a described-but-not-connectable server stays unknown under law 1.

**Provenance**

- **Entry id**: 10-leandata

- **Source file**: 10-scheduling-routing.md

- **Source line**: 198

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
