# Mailforge: MCP server status, API access gate and what it does

> Shared cold-email infrastructure platform (part of the Salesforge "Forge Stack") - automates workspace setup,... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Mailforge

# Mailforge

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [mailforge.ai](https://mailforge.ai) · entry id 09-mailforge · source 09-email-deliverability.md line 140

**What it does**
Shared cold-email infrastructure platform (part of the Salesforge "Forge Stack") - automates workspace setup, domain purchase/checks, mailbox creation, DNS records, forwarding, and domain masking for high-volume outbound.

**AI features, separated from automation with an AI label on it**
No AI-specific capability confirmed; infrastructure automation (bulk domain/mailbox provisioning, DNS configuration) reads as rules-based automation, not model-driven.

**RevOps role**
Shared (non-dedicated-IP) cold-email infrastructure layer - the lower-cost counterpart to Infraforge's dedicated-IP offering within the same product family.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: API key, generated from the Mailforge dashboard.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp)Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.salesforge.ai/mcp

- [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - no free tier found; positioned for "scaling shared cold email infrastructure and bulk mailbox management."

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp)
- [https://www.mailforge.ai/blog/mailforge-api](https://www.mailforge.ai/blog/mailforge-api)
- [https://help.salesforge.ai/en/articles/10333582-salesforge-mcp-server-with-claude-for-cold-email-and-linkedin-outreach](https://help.salesforge.ai/en/articles/10333582-salesforge-mcp-server-with-claude-for-cold-email-and-linkedin-outreach)
- [https://www.salesforge.ai/blog/cold-email-mcp-server](https://www.salesforge.ai/blog/cold-email-mcp-server)

4 source URLs. Raw sources field, verbatim:

https://mcp.salesforge.ai/mcp, https://www.mailforge.ai/blog/mailforge-api, https://help.salesforge.ai/en/articles/10333582-salesforge-mcp-server-with-claude-for-cold-email-and-linkedin-outreach, https://www.salesforge.ai/blog/cold-email-mcp-server

**Notes, verbatim from the file**
One shared MCP endpoint (mcp.salesforge.ai/mcp) exposes Mailforge alongside five sibling products - Salesforge, Primeforge, Leadsforge, Infraforge, and Warmforge - as native tools in a single connection, set up in under 5 minutes per vendor docs. This is one of the more mature vendor-published MCP rollouts found in this entire file.

**Provenance**

- **Entry id**: 09-mailforge

- **Source file**: 09-email-deliverability.md

- **Source line**: 140

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
