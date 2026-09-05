# Infraforge: MCP server status, API access gate and what it does

> Private cold-email infrastructure platform (part of the same Salesforge "Forge Stack" as Mailforge) offering... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Infraforge

# Infraforge

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [infraforge.ai](https://infraforge.ai) · entry id 09-infraforge · source 09-email-deliverability.md line 159

**What it does**
Private cold-email infrastructure platform (part of the same Salesforge "Forge Stack" as Mailforge) offering dedicated IPs, automated DNS setup, and pre-warmed domains for high-volume senders who want more control than shared infrastructure.

**AI features, separated from automation with an AI label on it**
No AI-specific capability confirmed; dedicated-IP provisioning and automated DNS/warmup setup read as infrastructure automation, not model-driven.

**RevOps role**
Dedicated-IP cold-email infrastructure layer for teams that have outgrown shared mailbox providers (Maildoso, Mailforge) and need isolated reputation per domain/IP.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: API key, generated from the Infraforge/Salesforge dashboard.

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

paid - pricing starts around $40/month for 10 mailboxes per third-party review; no free tier found.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.infraforge.ai/](https://www.infraforge.ai/)
- [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp)
- [https://www.infraforge.ai/blog/scaling-cold-outreach-with-email-apis](https://www.infraforge.ai/blog/scaling-cold-outreach-with-email-apis)
- [https://www.mailforge.ai/blog/hypertide-review](https://www.mailforge.ai/blog/hypertide-review)

4 source URLs. Raw sources field, verbatim:

https://www.infraforge.ai/, https://mcp.salesforge.ai/mcp, https://www.infraforge.ai/blog/scaling-cold-outreach-with-email-apis, https://www.mailforge.ai/blog/hypertide-review

**Notes, verbatim from the file**
Shares the same official MCP endpoint as Mailforge (see that entry) - one connection surfaces both tools plus four siblings. Cross-shop this against Hypertide and Scaledmail below; all three sell some version of "dedicated, pre-warmed cold-email infrastructure," but only the Forge Stack (Mailforge/Infraforge) has a confirmed official MCP.

**Provenance**

- **Entry id**: 09-infraforge

- **Source file**: 09-email-deliverability.md

- **Source line**: 159

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
