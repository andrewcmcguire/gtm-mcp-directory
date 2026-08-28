# Hunter.io: MCP server status, API access gate and what it does

> An email-finding and verification tool - given a name, domain, or company, it locates likely professional... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Hunter.io

# Hunter.io

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [hunter.io](https://hunter.io) · entry id 01-hunter-io · source 01-data-enrichment.md line 350

**What it does**
An email-finding and verification tool - given a name, domain, or company, it locates likely professional email addresses (via domain pattern-matching and web-crawled data) and verifies deliverability; also offers bulk domain search and a separate higher-volume "Data Platform" API for larger-scale lookups.

**AI features, separated from automation with an AI label on it**
Primarily deterministic pattern-matching (common email formats per domain) plus web crawling and deliverability checks (SMTP/syntax verification) - this is data engineering, not AI/ML in any meaningful sense. Notably, Hunter does not prominently market itself as "AI-powered," which is more honest than most competitors in this category.

**RevOps role**
Email-finding/verification utility typically plugged in downstream of a contact-discovery tool (or run directly against a domain list) to fill in or validate email addresses before outreach; also used for domain-wide email-pattern discovery.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (HUNTER_API_KEY)

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://hunter.io/api-documentation#mcp (an earlier open-source repo, github.com/hunter-io/hunter-mcp, is superseded by this hosted remote MCP server)

- [https://hunter.io/api-documentation#mcp](https://hunter.io/api-documentation#mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/hunter-io/hunter-mcp](https://github.com/hunter-io/hunter-mcp)

**Jobs it can do**

- [Find a work email address](../jobs/find-work-email.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://github.com/hunter-io/hunter-mcp](https://github.com/hunter-io/hunter-mcp)
- [https://hunter.io/pricing](https://hunter.io/pricing)
- [https://hunter.io/api](https://hunter.io/api)
- [https://fullenrich.com/content/hunter-io-pricing](https://fullenrich.com/content/hunter-io-pricing)
- [https://www.g2.com/products/hunter/pricing](https://www.g2.com/products/hunter/pricing)

5 source URLs. Raw sources field, verbatim:

https://github.com/hunter-io/hunter-mcp, https://hunter.io/pricing, https://hunter.io/api, https://fullenrich.com/content/hunter-io-pricing, https://www.g2.com/products/hunter/pricing

**Notes, verbatim from the file**
The Free tier ($0/mo, 25 searches + 50 verifications/month) includes API access per Hunter's own feature-comparison table, making it one of the few tools here with genuinely self-serve, no-cost API access (rate/volume-limited). Paid tiers: Starter (~$34-49/mo), Growth (~$104-149/mo), Scale (~$209-299/mo depending on annual/monthly billing), Enterprise custom. A separate higher-volume "Data Platform" API product uses credit packages starting around $6,500.

**Provenance**

- **Entry id**: 01-hunter-io

- **Source file**: 01-data-enrichment.md

- **Source line**: 350

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
