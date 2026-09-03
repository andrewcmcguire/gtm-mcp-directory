# Default: MCP server status, API access gate and what it does

> An inbound go-to-market platform unifying revenue-stack data (a "Tables" data layer) with AI-agent-built... MCP unknown, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Default

# Default

[MCP unknown](../mcp/unknown.md)
[Enterprise only](../gates/enterprise-only.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [default.com](https://default.com) · entry id 06-default · source 06-revops-infra.md line 210

**What it does**
An inbound go-to-market platform unifying revenue-stack data (a "Tables" data layer) with AI-agent-built workflows for lead routing, qualification, and meeting scheduling.

**AI features, separated from automation with an AI label on it**
"Dot" is an AI assistant/agent that turns plain-language requests into working GTM systems, with agent-built workflows reviewed/approved by humans before deployment, and agents that can schedule meetings. The workflow builder also has discrete "AI Routing" and "AI Prompt" nodes for AI-driven decisions inside otherwise deterministic workflows - a hybrid pattern similar to Make's.

**RevOps role**
Sits at inbound lead routing/qualification - where marketing-generated leads get scored, matched to reps/territories, and booked; pitched as an agentic replacement for legacy lead-routing tools.

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: unknown - not documented anywhere found (checked default.com, default.com/product, docs.default.com, default.com/solutions/default-mcp).

- **Parsed URLs**: 1 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

n/a (marketing pages only: https://www.default.com/solutions/default-mcp names a Default MCP but publishes no endpoint, auth, or setup docs, and docs.default.com has no MCP article)

- [https://www.default.com/solutions/default-mcp](https://www.default.com/solutions/default-mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (no pricing is published and the only CTA is book-a-demo; the site describes Native Access in beta as MCP access to data and tools for every agent, so programmatic access exists but is reachable only through sales)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Book a meeting](../jobs/book-a-meeting.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Route an inbound lead](../jobs/route-inbound-lead.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Default

- **Category**: [Scheduling & Routing](../categories/scheduling-routing.md)

- **MCP status there**: MCP unknown

- **Gate there**: Enterprise only

- **Source**: 10-scheduling-routing.md line 65

- **Canonical page**: [Default](../tools/default.md)

What that listing says it does: "Agentic GTM infrastructure" platform unifying CRM, website-form, and enrichment data into one identity-resolved model, with lead routing, scheduling, enrichment, and workflow automation built on top.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.default.com](https://www.default.com)
- [https://www.default.com/product](https://www.default.com/product)
- [https://docs.default.com](https://docs.default.com)
- [https://www.default.com/solutions/default-mcp](https://www.default.com/solutions/default-mcp)

4 source URLs. Raw sources field, verbatim:

https://www.default.com, https://www.default.com/product, https://docs.default.com, https://www.default.com/solutions/default-mcp

**Notes, verbatim from the file**
Confirmed this is default.com the lead-routing SaaS, not a generic dev-tooling reference. The MCP claim is real but labeled "In beta" on the homepage with no dedicated docs/repo page found - treat as early/unstable. Marked official rather than none-found because the vendor's own page explicitly names MCP with a linkable URL, satisfying the schema's "URL required" law, even though it isn't a full docs page. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.default.com/): no pricing is published and the only CTA is book-a-demo; the site describes Native Access in beta as MCP access to data and tools for every agent, so programmatic access exists but is reachable only through sales. 2026-09-02: mcp_status official -> unknown. Default's homepage now carries a "Default MCP" nav item ("Trigger workflows, run enrichment jobs, and pull audit logs from your terminal or your agents") and a dedicated marketing page, https://www.default.com/solutions/default-mcp ("The MCP for go-to-market ops"), which is more than the beta feature line cited before. But that page publishes no endpoint, auth method, setup guide, or client list; https://docs.default.com/ has no MCP article in any section; and the official MCP registry's default hits are all unrelated products. A marketing page that names a server without a connectable URL is not a receipt under law 1, so the earlier reasoning is retracted and the status is unknown until Default publishes docs.

**Provenance**

- **Entry id**: 06-default

- **Source file**: 06-revops-infra.md

- **Source line**: 210

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
