# Close (Close CRM): MCP server status, API access gate and what it does

> A sales CRM built for inside-sales teams with built-in calling, email, and SMS alongside pipeline/lead... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Close (Close CRM)

# Close (Close CRM)

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [close.com](https://close.com) · entry id 06-close · source 06-revops-infra.md line 99

**What it does**
A sales CRM built for inside-sales teams with built-in calling, email, and SMS alongside pipeline/lead management - a communications-plus-CRM combo rather than a pure system of record.

**AI features, separated from automation with an AI label on it**
Close's pricing page reportedly references an "AI Sales Agent" but this was not independently verified against a primary product page in this pass - flagged as under-researched rather than asserted. The MCP server itself is connectivity (create leads, log calls, send SMS, manage tasks), not an AI feature.

**RevOps role**
SMB/startup sales CRM often chosen for native calling/SMS; its MCP server pitches "run ops tasks via Claude" as a differentiator for small sales teams without dedicated RevOps engineering.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Dual - OAuth 2.0 with Dynamic Client Registration (recommended; used by Claude, ChatGPT, Cursor) or API-key auth via custom headers (Close-API-Key, Close-Scope). Three scope tiers: mcp.read, mcp.write_safe, mcp.write_destructive.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://help.close.com/integrations/close-mcp-server](https://help.close.com/integrations/close-mcp-server)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://help.close.com/integrations/close-mcp-server (redirect correction 2026-08-28: the address previously recorded here, help.close.com/docs/mcp-server, 308s to this one and this one returns 200. Endpoint: https://mcp.close.com/mcp)

- [https://help.close.com/integrations/close-mcp-server](https://help.close.com/integrations/close-mcp-server)
- [https://mcp.close.com/mcp](https://mcp.close.com/mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - no free tier; API access is included on every paid plan starting at Solo (~$19/user/mo standard). No enterprise-sales gate, but a subscription is required.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Place an outbound call](../jobs/place-outbound-call.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://help.close.com/integrations/close-mcp-server](https://help.close.com/integrations/close-mcp-server)
- [https://help.close.com/llms.txt](https://help.close.com/llms.txt)

2 source URLs. Raw sources field, verbatim:

https://help.close.com/integrations/close-mcp-server, https://help.close.com/llms.txt

**Notes, verbatim from the file**
Supports HTTP Streamable transport and integrates with Claude (web/desktop/code), ChatGPT, Cursor, VS Code, and n8n per its own docs. A separate community CLI tool (bcharleson/close-crm-cli) also exists and is unofficial.

**Provenance**

- **Entry id**: 06-close

- **Source file**: 06-revops-infra.md

- **Source line**: 99

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
