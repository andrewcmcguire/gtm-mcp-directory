# Email Deliverability tools with MCP servers: 4 of 13, counted

> 4 of the 13 email deliverability tools in The GTM MCP Directory have an MCP server: 4 official and 0 community. The server URL, auth model and access gate for each. Counted 2026-09-04.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / Email Deliverability tools with an MCP server

**List · 4 of 293**

## Email Deliverability tools with an MCP server

Inbox-placement testing, warmup, and DNS-authentication (SPF/DKIM/DMARC) tooling that keeps cold-outbound infrastructure out of spam. Standing risk worth flagging once here rather than per entry: automated warmup - seed inboxes auto-opening/replying/starring your mail to fake engagement - sits in real tension with mailbox-provider ToS. Google banned automated email warm-up services for Gmail accounts in a January 2023 policy change, and Google/Yahoo/Microsoft jointly enforce bulk-sender rules (sub-0.3% spam complaints, sub-2% bounce) as of May 2025; GMass shut its own warm-up feature down as a result. Several vendors below (InboxAlly explicitly) market themselves as the safer alternative to network-based/bot-driven warmup for exactly this reason. 4 of 13 entries in this category are reachable by an agent: 4 through a server the vendor maintains and 0 through one somebody else built. The category is tagged most often with Warm up an inbox. [See the full category page](../categories/email-deliverability.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Allegrow](../tools/allegrow.md)
allegrow.co | [Official MCP](../mcp/official.md) | [https://www.allegrow.co/knowledge-base/claude-email-...](https://www.allegrow.co/knowledge-base/claude-email-mcp) | OAuth
OAuth - connects through Claude's standard connector authorization flow; user logs into... | [Paid, self-serve](../gates/paid.md) |
| [Infraforge](../tools/infraforge.md)
infraforge.ai | [Official MCP](../mcp/official.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) | API key
API key, generated from the Infraforge/Salesforge dashboard. | [Paid, self-serve](../gates/paid.md) |
| [Maildoso](../tools/maildoso.md)
maildoso.ai | [Official MCP](../mcp/official.md) | [https://maildoso.ai/](https://maildoso.ai/) | Auth not recorded
unknown - described only as "API and MCP access" bundled into every plan, without a... | [Paid, self-serve](../gates/paid.md) |
| [Mailforge](../tools/mailforge.md)
mailforge.ai | [Official MCP](../mcp/official.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) | API key
API key, generated from the Mailforge dashboard. | [Paid, self-serve](../gates/paid.md) |

### The other 9 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [GlockApps](../tools/glockapps.md)
glockapps.com | [MCP unknown](../mcp/unknown.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Scaledmail](../tools/scaledmail.md)
scaledmail.com | [No MCP found](../mcp/none-found.md) | [Free to start](../gates/free.md) | 2026-09-02 |
| [Warmup Inbox](../tools/warmup-inbox.md)
warmupinbox.com | [No MCP found](../mcp/none-found.md) | [Free to start](../gates/free.md) | 2026-09-02 |
| [Hypertide](../tools/hypertide.md)
hypertide.io | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [InboxAlly](../tools/inboxally.md)
inboxally.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [MailGenius](../tools/mailgenius.md)
mailgenius.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Mailreach](../tools/mailreach.md)
mailreach.co | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Warmy.io](../tools/warmy-io.md)
warmy.io | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Folderly](../tools/folderly.md)
folderly.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-02 |

### What this category is asked for

The jobs most often tagged on the 13 tagged entries in this category.

- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)
- [Check inbox placement](../jobs/check-inbox-placement.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

Counted 2026-09-04 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
