# Mailreach: MCP server status, API access gate and what it does

> Email warmup and deliverability platform - automates inbox-to-inbox warmup conversations, tracks a "Heat... No MCP found, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Mailreach

# Mailreach

[No MCP found](../mcp/none-found.md)
[Paid, self-serve](../gates/paid.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [mailreach.co](https://mailreach.co) · entry id 09-mailreach · source 09-email-deliverability.md line 7

**What it does**
Email warmup and deliverability platform - automates inbox-to-inbox warmup conversations, tracks a "Heat Score" reputation metric, and monitors blacklist/authentication status across Gmail, Outlook, and any SMTP provider.

**AI features, separated from automation with an AI label on it**
No AI-specific capability confirmed in sourced pages; the warmup mechanic (automated send/open/reply cycles between real inboxes) and reputation scoring read as rules-based automation and monitoring, not model-driven - treat as plain automation absent further evidence.

**RevOps role**
Deliverability-maintenance layer that runs continuously behind an outbound sending tool (Instantly, Smartlead, a raw SMTP account) rather than being invoked directly in a sales workflow.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - API access appears bundled into the paid service (no free tier found); pricing starts at $25/mo per mailbox ($20/mo billed annually).

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Warm up an inbox](../jobs/warm-up-inbox.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.mailreach.co/email-warmup-api](https://www.mailreach.co/email-warmup-api)
- [https://docs.mailreach.co/api](https://docs.mailreach.co/api)
- [https://www.trustradius.com/products/mailreach/pricing](https://www.trustradius.com/products/mailreach/pricing)
- [https://emailwarmup.com/blog/email-deliverability-tools/mailreach-review/](https://emailwarmup.com/blog/email-deliverability-tools/mailreach-review/)

4 source URLs. Raw sources field, verbatim:

https://www.mailreach.co/email-warmup-api, https://docs.mailreach.co/api, https://www.trustradius.com/products/mailreach/pricing, https://emailwarmup.com/blog/email-deliverability-tools/mailreach-review/

**Notes, verbatim from the file**
One of the longer-established warmup vendors in this category (frequently cited as an "original") but no MCP server, GitHub repo, or registry listing (mcp.so/glama.ai/pulsemcp.com) was found for it.

**Provenance**

- **Entry id**: 09-mailreach

- **Source file**: 09-email-deliverability.md

- **Source line**: 7

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
