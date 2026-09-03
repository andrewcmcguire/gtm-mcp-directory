# Superblocks: MCP server status, API access gate and what it does

> A platform for building - and more distinctively, governing - AI-generated internal apps: lets business teams... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Superblocks

# Superblocks

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [superblocks.com](https://superblocks.com) · entry id 06-superblocks · source 06-revops-infra.md line 414

**What it does**
A platform for building - and more distinctively, governing - AI-generated internal apps: lets business teams build apps (including importing prototypes from Claude, Lovable, or Replit) while giving IT/Security a control layer over integrations, permissions, and auditing.

**AI features, separated from automation with an AI label on it**
A "Clark AI agent" for app development plus prototype-import from AI coding tools; the more unique angle is AI-app governance (usage monitoring, permission auditing, threat detection across AI-built apps) rather than Superblocks itself being a novel generative engine - much of the "AI" framing here is about controlling other tools' AI output.

**RevOps role**
Adjacent to Retool - an internal-app builder, but positioned specifically as the IT/security control plane for a world where GTM/ops teams are building their own AI-assisted apps; not itself a core data-pipeline tool.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - the announcement doesn't specify the auth method; the feature is Enterprise-only, implying an admin/OAuth-gated setup, but this isn't documented in what was found.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://superblocks.com/blog/superblocks-mcp](https://superblocks.com/blog/superblocks-mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://superblocks.com/blog/superblocks-mcp

- [https://superblocks.com/blog/superblocks-mcp](https://superblocks.com/blog/superblocks-mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - no free tier; cheapest self-serve entry is the Teams plan at $100/mo annual with a 14-day free trial. The MCP feature itself is Enterprise-exclusive, so a solo operator can use the base product self-serve but cannot reach the MCP capability without an enterprise plan.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: no-job-fits. Internal-app building and AI-app governance. run-automation-workflow is not what it does and there is no app-builder job.

22 of 293 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://superblocks.com/](https://superblocks.com/)
- [https://superblocks.com/pricing](https://superblocks.com/pricing)
- [https://superblocks.com/blog/superblocks-mcp](https://superblocks.com/blog/superblocks-mcp)

3 source URLs. Raw sources field, verbatim:

https://superblocks.com/, https://superblocks.com/pricing, https://superblocks.com/blog/superblocks-mcp

**Notes, verbatim from the file**
Superblocks MCP is a different category of MCP than the rest of this file - it isn't "connect an AI agent to move/query GTM data," it's "give IT admins programmatic visibility and control over every AI-built app, integration, and permission in the org" (identify malicious packages, detect unusual write patterns, alert on permission changes, correlate audit logs to builders).

**Provenance**

- **Entry id**: 06-superblocks

- **Source file**: 06-revops-infra.md

- **Source line**: 414

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
