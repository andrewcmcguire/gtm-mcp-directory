# MailGenius: MCP server status, API access gate and what it does

> Free/paid email deliverability and spam-testing tool - checks SPF/DKIM/DMARC authentication, scans... No MCP found, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
MailGenius

# MailGenius

[No MCP found](../mcp/none-found.md)
[Paid, self-serve](../gates/paid.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [mailgenius.com](https://mailgenius.com) · entry id 09-mailgenius · source 09-email-deliverability.md line 83

**What it does**
Free/paid email deliverability and spam-testing tool - checks SPF/DKIM/DMARC authentication, scans blacklists, previews inbox rendering across Gmail/Outlook, and scores spam likelihood.

**AI features, separated from automation with an AI label on it**
No AI-specific capability confirmed; diagnostic checks (authentication records, header analysis, spam-trigger content scan) read as rules-based testing, not model-driven - treat as plain automation.

**RevOps role**
Pre-send deliverability-testing layer, typically run before a cold-email campaign launches rather than continuously in the background like a warmup tool.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - a whitelabel/API tier exists but requires applying for access (mailgenius.com/api-application), not self-serve signup.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Check inbox placement](../jobs/check-inbox-placement.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.mailgenius.com/](https://www.mailgenius.com/)
- [https://www.mailgenius.com/api-application/](https://www.mailgenius.com/api-application/)
- [https://mcp.pipedream.com/app/mailgenius](https://mcp.pipedream.com/app/mailgenius)
- [https://coldiq.com/tools/mailgenius](https://coldiq.com/tools/mailgenius)

4 source URLs. Raw sources field, verbatim:

https://www.mailgenius.com/, https://www.mailgenius.com/api-application/, https://mcp.pipedream.com/app/mailgenius, https://coldiq.com/tools/mailgenius

**Notes, verbatim from the file**
A "MailGenius MCP Server" listing exists at mcp.pipedream.com/app/mailgenius, but Pipedream is a generic workflow-automation platform that auto-generates MCP wrappers around thousands of apps' APIs - it is not a MailGenius-published or dedicated community server, so this is marked none-found per this directory's convention (consistent with how Zapier-MCP-only listings are treated elsewhere in this file and the wider directory).

**Provenance**

- **Entry id**: 09-mailgenius

- **Source file**: 09-email-deliverability.md

- **Source line**: 83

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
