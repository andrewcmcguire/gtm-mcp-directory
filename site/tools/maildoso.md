# Maildoso: MCP server status, API access gate and what it does

> Cold-outreach mailbox and domain infrastructure provider  - sells pre-configured SMTP mailboxes and Google... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Maildoso

# Maildoso

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [maildoso.ai](https://maildoso.ai) · entry id 09-maildoso · source 09-email-deliverability.md line 121

**What it does**
Cold-outreach mailbox and domain infrastructure provider - sells pre-configured SMTP mailboxes and Google Workspace accounts (with SPF/DKIM/DMARC already set up) built specifically for cold email sending, starting at $0.49/mailbox.

**AI features, separated from automation with an AI label on it**
No AI-specific capability confirmed; "self-healing mailboxes" and IP rotation read as automated infrastructure management, not model-driven - treat as plain automation.

**RevOps role**
Cold-email-infrastructure layer (domains + mailboxes + DNS) that outbound sequencers (Instantly, Smartlead) send through - a direct competitor to Mailforge/Infraforge/Scaledmail/Hypertide below.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - described only as "API and MCP access" bundled into every plan, without a documented auth mechanism in sourced pages.

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://maildoso.ai/ (see "resources/api" section; no separate dedicated MCP docs page was found)

- [https://maildoso.ai/](https://maildoso.ai/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - bundled into paid mailbox plans (starting $0.49/mailbox up to $499/mo for 1,000 mailboxes); no free tier.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://maildoso.ai/](https://maildoso.ai/)
- [https://maildoso.ai/blog/recommendations/cold-email-infrastructure-scale-safely](https://maildoso.ai/blog/recommendations/cold-email-infrastructure-scale-safely)
- [https://maildoso.ai/blog/tools/zapmail](https://maildoso.ai/blog/tools/zapmail)

3 source URLs. Raw sources field, verbatim:

https://maildoso.ai/, https://maildoso.ai/blog/recommendations/cold-email-infrastructure-scale-safely, https://maildoso.ai/blog/tools/zapmail

**Notes, verbatim from the file**
Do not confuse with the similarly-named "Mailforge" (a separate company, part of the Salesforge/"Forge Stack" family - see next entries). Maildoso's own homepage states "Every plan includes ... API and MCP access," a first-party claim, but no dedicated technical documentation page for the MCP server specifically (setup, tool list, transport) was independently located - treat the mcp_url as the best-available vendor page, not a confirmed docs endpoint.

**Provenance**

- **Entry id**: 09-maildoso

- **Source file**: 09-email-deliverability.md

- **Source line**: 121

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
