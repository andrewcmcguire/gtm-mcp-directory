# Warmy.io: MCP server status, API access gate and what it does

> Email warmup and deliverability platform with an "AI-driven engagement engine" - customizable warm-up... No MCP found, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Warmy.io

# Warmy.io

[No MCP found](../mcp/none-found.md)
[Paid, self-serve](../gates/paid.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [warmy.io](https://warmy.io) · entry id 09-warmy-io · source 09-email-deliverability.md line 235

**What it does**
Email warmup and deliverability platform with an "AI-driven engagement engine" - customizable warm-up topic/language selection, works across Gmail, Outlook, Zoho, and Amazon SES, with a real-time webhook/Slack-connected API for adjusting warm-up speed, volume, and timing programmatically.

**AI features, separated from automation with an AI label on it**
Vendor markets the engagement engine as "AI-driven" and the warmup content as "fully personalized" per message - no independent breakdown of what is model-generated versus templated was found; treat as vendor-stated.

**RevOps role**
Deliverability-maintenance layer comparable to Mailreach/Warmup Inbox, differentiated on enterprise-sender topic/language customization and webhook-driven programmatic control.

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

paid - API is a distinct product tier ("Warmy API") rather than bundled into every plan by default, per the vendor's own product page.

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

- [https://www.warmy.io/product/api/](https://www.warmy.io/product/api/)
- [https://www.warmy.io/product/warm-up-email/](https://www.warmy.io/product/warm-up-email/)
- [https://www.warmy.io/blog/best-email-warmup-deliverability-tools-alternatives/](https://www.warmy.io/blog/best-email-warmup-deliverability-tools-alternatives/)

3 source URLs. Raw sources field, verbatim:

https://www.warmy.io/product/api/, https://www.warmy.io/product/warm-up-email/, https://www.warmy.io/blog/best-email-warmup-deliverability-tools-alternatives/

**Notes, verbatim from the file**
A search result mentioned a separate, apparently unrelated tool called "mailX" (a free SPF/DKIM/DMARC/blacklist checker) as having "API and MCP access" - that is a different product from Warmy.io and was not pursued further here since it fell outside this file's named seed list; flagged only to avoid future conflation. No MCP server found for Warmy.io itself.

**Provenance**

- **Entry id**: 09-warmy-io

- **Source file**: 09-email-deliverability.md

- **Source line**: 235

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
