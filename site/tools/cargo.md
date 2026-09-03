# Cargo: MCP server status, API access gate and what it does

> A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Cargo

# Cargo

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [getcargo.ai](https://getcargo.ai) · entry id 06-cargo · source 06-revops-infra.md line 186

**What it does**
A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment, scoring, routing, CRM sync - as code, run by AI agents.

**AI features, separated from automation with an AI label on it**
Genuinely agent-based - ships "Cargo Skills," 17 defined agent skills (sourcing, enrichment, scoring, research, routing) usable directly inside Claude Code, Codex, and Cursor, with autonomous execution for routine tasks and human-approval gates for nuanced decisions. Closer to a GTM-specific agent framework than point-and-click automation.

**RevOps role**
Positions itself as the connective/execution layer between fragmented sales, marketing, and finance tools - closer to a GTM automation warehouse-plus-agents than a point tool; integrates with a data warehouse rather than owning its own store.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown for the MCP layer specifically - docs confirm the capability but not its auth mechanism. Cargo's separate REST API (api.getcargo.io/v1) uses OAuth 2.0 with device-code and PKCE flows.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://docs.getcargo.ai/](https://docs.getcargo.ai/)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.getcargo.ai/ (defineMcpServer is a native, first-party part of Cargo's workspace/CDK framework; a dedicated /mcp docs page returned HTTP 405 rather than content)

- [https://docs.getcargo.ai/](https://docs.getcargo.ai/)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - a genuine self-serve free tier (100 credits/mo, no card required, CLI signup via email); paid tiers start at Starter $165/mo, with "no feature lock" suggesting API/CLI access isn't paywalled.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/getcargohq](https://github.com/getcargohq)

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Route an inbound lead](../jobs/route-inbound-lead.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.ycombinator.com/companies/cargo](https://www.ycombinator.com/companies/cargo)
- [https://www.getcargo.ai/](https://www.getcargo.ai/)
- [https://www.getcargo.ai/pricing](https://www.getcargo.ai/pricing)
- [https://docs.getcargo.ai/](https://docs.getcargo.ai/)
- [https://github.com/getcargohq](https://github.com/getcargohq)

5 source URLs. Raw sources field, verbatim:

https://www.ycombinator.com/companies/cargo, https://www.getcargo.ai/, https://www.getcargo.ai/pricing, https://docs.getcargo.ai/, https://github.com/getcargohq

**Notes, verbatim from the file**
DOMAIN CORRECTION - cargo.so does not resolve (DNS failure, confirmed by multiple direct fetch attempts). The real company matching this brief (YC S23, founders ex-Spendesk) is at getcargo.ai / getcargo.io. Cargo's GitHub org (github.com/getcargohq) has 5 public repos but no standalone "MCP server" repo - MCP is a feature inside the core product/docs, not a separate open-source connector.

**Provenance**

- **Entry id**: 06-cargo

- **Source file**: 06-revops-infra.md

- **Source line**: 186

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
