# Email Deliverability: 13 tools, 4 with an official MCP server

> Inbox-placement testing, warmup, and DNS-authentication (SPF/DKIM/DMARC) tooling that keeps... 13 tools counted, 4 with an official MCP server and 2 free to start.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[By category](index.md) / Email Deliverability

**09 · email-deliverability**

## Email Deliverability

Inbox-placement testing, warmup, and DNS-authentication (SPF/DKIM/DMARC) tooling that keeps cold-outbound infrastructure out of spam. Standing risk worth flagging once here rather than per entry: automated warmup - seed inboxes auto-opening/replying/starring your mail to fake engagement - sits in real tension with mailbox-provider ToS. Google banned automated email warm-up services for Gmail accounts in a January 2023 policy change, and Google/Yahoo/Microsoft jointly enforce bulk-sender rules (sub-0.3% spam complaints, sub-2% bounce) as of May 2025; GMass shut its own warm-up feature down as a result. Several vendors below (InboxAlly explicitly) market themselves as the safer alternative to network-based/bot-driven warmup for exactly this reason.

- **entries in this file**: 13

- **Official MCP**: 4
- **MCP unknown**: 1
- **No MCP found**: 8

- **Free to start**: 2
- **Paid, self-serve**: 10
- **Gate unknown**: 1

Source file: 09-email-deliverability.md · content sha256 5a4c85e11fb5bcde... · counts reconciled against tools_recount.py at build time.

- [The 4 with an MCP server](../lists/mcp-email-deliverability.md)

- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)
- [Check inbox placement](../jobs/check-inbox-placement.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

- [Allegrow](../tools/allegrow.md) allegrow.co B2B email verification and deliverability platform - resolves catch-all/secure-email-gateway addresses that legacy verifiers mark "unknown," sends warm-up email to real B2B accounts, and runs hourly... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Infraforge](../tools/infraforge.md) infraforge.ai Private cold-email infrastructure platform (part of the same Salesforge "Forge Stack" as Mailforge) offering dedicated IPs, automated DNS setup, and pre-warmed domains for high-volume senders who want more... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Maildoso](../tools/maildoso.md) maildoso.ai Cold-outreach mailbox and domain infrastructure provider - sells pre-configured SMTP mailboxes and Google Workspace accounts (with SPF/DKIM/DMARC already set up) built specifically for cold email sending,... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Mailforge](../tools/mailforge.md) mailforge.ai Shared cold-email infrastructure platform (part of the Salesforge "Forge Stack") - automates workspace setup, domain purchase/checks, mailbox creation, DNS records, forwarding, and domain masking for... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [GlockApps](../tools/glockapps.md) glockapps.com Email deliverability testing and monitoring platform - Inbox Insight sends a test email to real seed accounts across 60+ providers (Gmail, Yahoo, Outlook, Apple Mail, AOL, etc.) and reports exact... [MCP unknown](../mcp/unknown.md) · [Paid, self-serve](../gates/paid.md)

- [Scaledmail](../tools/scaledmail.md) scaledmail.com Cold-email infrastructure provider - sets up sending domains, configures DNS authentication (SPF/DKIM/DMARC) from day one, and rotates inboxes so outbound sequences land in the primary tab. [No MCP found](../mcp/none-found.md) · [Free to start](../gates/free.md)

- [Warmup Inbox](../tools/warmup-inbox.md) warmupinbox.com Email warmup and deliverability platform running a network of 30,000+ real inboxes that exchange natural-looking email (opens, replies, stars) with a customer's connected accounts to build sender reputation. [No MCP found](../mcp/none-found.md) · [Free to start](../gates/free.md)

- [Hypertide](../tools/hypertide.md) hypertide.io Automated cold-email infrastructure provider - high-deliverability Microsoft Entra/Google mailboxes with dedicated domains/IPs per order, pre-configured SPF/DKIM/DMARC, set up in 4-6 hours (vendor claims fully... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [InboxAlly](../tools/inboxally.md) inboxally.com Email warmup and reputation-repair service that adds real seed inboxes into a customer's actual campaigns; those seed accounts perform browser-level engagement (open, read, reply, mark important, move out of... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [MailGenius](../tools/mailgenius.md) mailgenius.com Free/paid email deliverability and spam-testing tool - checks SPF/DKIM/DMARC authentication, scans blacklists, previews inbox rendering across Gmail/Outlook, and scores spam likelihood. [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [Mailreach](../tools/mailreach.md) mailreach.co Email warmup and deliverability platform - automates inbox-to-inbox warmup conversations, tracks a "Heat Score" reputation metric, and monitors blacklist/authentication status across Gmail, Outlook, and any... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [Warmy.io](../tools/warmy-io.md) warmy.io Email warmup and deliverability platform with an "AI-driven engagement engine" - customizable warm-up topic/language selection, works across Gmail, Outlook, Zoho, and Amazon SES, with a real-time... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [Folderly](../tools/folderly.md) folderly.com Email deliverability platform combining a spam/inbox-placement test, ongoing deliverability monitoring, technical DNS setup, and spam-trigger content review for B2B outbound teams. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)
