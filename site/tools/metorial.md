# Metorial: MCP server status, API access gate and what it does

> A hosted MCP gateway that gives AI agents/"AI employees" centralized, governed access to a company's SaaS... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Metorial

# Metorial

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [metorial.com](https://metorial.com) · entry id 07-metorial · source 07-mcp-infrastructure.md line 245

**What it does**
A hosted MCP gateway that gives AI agents/"AI employees" centralized, governed access to a company's SaaS tools (Google Workspace, Microsoft 365, GitHub, Jira, Slack, Teams, Stripe, Salesforce, Zendesk, and custom internal systems) through one integration point.

**AI features, separated from automation with an AI label on it**
none in Metorial itself - it is connector/governance infrastructure for agents built elsewhere.

**RevOps role**
An enterprise-governance-flavored alternative to Composio/Pipedream - pitched at companies that want a single audited chokepoint (with tracing and access policies) for every agent-to-SaaS connection, including Salesforce.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Fully custodial - Metorial stores and centrally manages OAuth tokens for every connected integration ("no tokens to manage" for the end user), with company login handled via SSO/SAML (Okta, Azure AD, Google Workspace) and each integration isolated from the others.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://metorial.com](https://metorial.com)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://metorial.com

- [https://metorial.com](https://metorial.com)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (Metorial Dev is free - 500K tool calls/mo, 2 team members, 10 provider integrations; Metorial Scale is $250/mo - 2.5M tool calls/mo, 20 team members, unlimited integrations; Enterprise is custom, adding on-prem deployment, SOC 2/GDPR, RBAC, and SSO/SAML)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://metorial.com](https://metorial.com)
- [https://metorial.com/pricing](https://metorial.com/pricing)

2 source URLs. Raw sources field, verbatim:

https://metorial.com, https://metorial.com/pricing

**Notes, verbatim from the file**
Metorial is explicitly and fully custodial of OAuth tokens across every connected app - the entire pitch is "no tokens to manage" because Metorial manages them centrally. That is a meaningfully bigger trust concentration than Zapier MCP (reuses Zapier's existing per-app OAuth) or Anthropic's directory (per-connector, third-party-operated) - worth flagging to anyone evaluating it for a Salesforce/finance-adjacent connection.

**Provenance**

- **Entry id**: 07-metorial

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 245

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
