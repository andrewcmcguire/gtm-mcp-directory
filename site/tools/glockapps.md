# GlockApps: MCP server status, API access gate and what it does

> Email deliverability testing and monitoring platform - Inbox Insight sends a test email to real seed accounts... MCP unknown, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
GlockApps

# GlockApps

[MCP unknown](../mcp/unknown.md)
[Paid, self-serve](../gates/paid.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [glockapps.com](https://glockapps.com) · entry id 09-glockapps · source 09-email-deliverability.md line 216

**What it does**
Email deliverability testing and monitoring platform - Inbox Insight sends a test email to real seed accounts across 60+ providers (Gmail, Yahoo, Outlook, Apple Mail, AOL, etc.) and reports exact inbox/spam/promotions placement, plus authentication diagnostics and blacklist monitoring.

**AI features, separated from automation with an AI label on it**
No AI-specific capability confirmed; placement testing (seed-account network) and authentication checks read as measurement/monitoring automation, not model-driven - treat as plain automation.

**RevOps role**
Pre-send and ongoing deliverability-diagnosis layer, one of the longest-running "know your inbox placement" tools in the category (blog dates its founding narrative back years before most of this file's entrants).

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: OAuth 2.1 per the vendor's llms.txt ('OAuth 2.1: the API key stays on the GlockApps account and is never shared'); unverified, no reachable setup page

- **Parsed URLs**: 3 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

none that answers - the vendor's own https://glockapps.com/llms.txt links https://glockapps.com/mcp/ and https://glockapps.com/mcp-setup/, both HTTP 404 on fetch 2026-09-02

- [https://glockapps.com/llms.txt](https://glockapps.com/llms.txt)
- [https://glockapps.com/mcp/](https://glockapps.com/mcp/)
- [https://glockapps.com/mcp-setup/](https://glockapps.com/mcp-setup/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - API access is included only on the Growth plan tier, not the base/free tier.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Check inbox placement](../jobs/check-inbox-placement.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://glockapps.com/](https://glockapps.com/)
- [https://glockapps.com/tutorials/test-inbox-placement-and-test-spam-score/](https://glockapps.com/tutorials/test-inbox-placement-and-test-spam-score/)
- [https://frontdeskreview.com/software/email-deliverability/glockapps/](https://frontdeskreview.com/software/email-deliverability/glockapps/)
- [https://glockapps.com/blog/know-your-inbox-placement/](https://glockapps.com/blog/know-your-inbox-placement/)
- [https://glockapps.com/llms.txt](https://glockapps.com/llms.txt)

5 source URLs. Raw sources field, verbatim:

https://glockapps.com/, https://glockapps.com/tutorials/test-inbox-placement-and-test-spam-score/, https://frontdeskreview.com/software/email-deliverability/glockapps/, https://glockapps.com/blog/know-your-inbox-placement/, https://glockapps.com/llms.txt

**Notes, verbatim from the file**
No MCP server, GitHub repo, or registry listing found for GlockApps specifically. Integrates with Mailchimp, ActiveCampaign, HubSpot, SendGrid, and Mailgun per vendor site. 2026-09-02: CHANGED none-found -> unknown. GlockApps' own https://glockapps.com/llms.txt now carries the lines 'Remote MCP connector for Claude, ChatGPT and any MCP-compatible client', 'Start inbox placement tests and read results from inside an AI assistant' and 'OAuth 2.1: the API key stays on the GlockApps account and is never shared', pointing at glockapps.com/mcp/ and an 'MCP Setup Guide' at glockapps.com/mcp-setup/. Both linked pages returned HTTP 404 to fetch, the help-center search for mcp returns nothing, and the MCP registry has no glockapps entry, so this is a first-party claim without a URL that answers. Re-fetch /mcp/ with a browser next pass; if it answers, this flips to official.

**Provenance**

- **Entry id**: 09-glockapps

- **Source file**: 09-email-deliverability.md

- **Source line**: 216

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
