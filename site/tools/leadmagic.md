# LeadMagic: MCP server status, API access gate and what it does

> A B2B contact/company data API and CLI that finds and validates work emails, mobile numbers, and... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
LeadMagic

# LeadMagic

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://leadmagic.io](https://leadmagic.io) · entry id 01-leadmagic · source 01-data-enrichment.md line 179

**What it does**
A B2B contact/company data API and CLI that finds and validates work emails, mobile numbers, and social-to-email matches, plus company/job/ad-intelligence lookups, billing only for successful (valid) results.

**AI features, separated from automation with an AI label on it**
No substantive AI/ML claimed for the core lookup functions; "accuracy" and "confidence score" outputs are from SMTP/MX validation logic, not generative or learned models. Marketing framing as an "AI agent" data API mainly reflects that it is built to be consumed by AI agents/MCP clients, not that its enrichment itself uses AI.

**RevOps role**
Point enrichment/verification step (single lookups or bulk CSV) feeding a sequencer or CRM; positioned as a lightweight, developer-first alternative to larger enrichment suites.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key for local/self-hosted install (LEADMAGIC_API_KEY env var); OAuth Bearer token (Clerk-issued) for the hosted remote MCP - hosted version does not accept static API keys

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/LeadMagic/leadmagic-mcp (hosted endpoint: https://mcp.leadmagic.io/mcp)

- [https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp)
- [https://mcp.leadmagic.io/mcp](https://mcp.leadmagic.io/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp)

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Scrape job postings](../jobs/scrape-job-postings.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://leadmagic.io/pricing](https://leadmagic.io/pricing)
- [https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp)
- [https://mcp.leadmagic.io/](https://mcp.leadmagic.io/)
- [https://leadmagic.io/solutions/mcp](https://leadmagic.io/solutions/mcp)
- [https://www.pulsemcp.com/servers/leadmagic-smartlead](https://www.pulsemcp.com/servers/leadmagic-smartlead)
- [https://syncgtm.com/blog/leadmagic-review](https://syncgtm.com/blog/leadmagic-review)
- [https://coldemailkit.com/tools/leadmagic](https://coldemailkit.com/tools/leadmagic)

7 source URLs. Raw sources field, verbatim:

https://leadmagic.io/pricing, https://github.com/LeadMagic/leadmagic-mcp, https://mcp.leadmagic.io/, https://leadmagic.io/solutions/mcp, https://www.pulsemcp.com/servers/leadmagic-smartlead, https://syncgtm.com/blog/leadmagic-review, https://coldemailkit.com/tools/leadmagic

**Notes, verbatim from the file**
Fully self-serve, credit-based, no seats/contracts: Basic $59.99/mo (2,500 credits) up through Ultimate $799.99/mo (100,000 credits); credits deduct only on successful/valid results ($0.008/credit baseline, 1 credit/email, 5 credits/mobile). Every plan reportedly includes full API, CLI, and MCP access from a shared credit pool. Independent reviews report email-finding accuracy noticeably lower (~75-85%) than the vendor's claimed 97%, worth flagging for buyers relying on the vendor number.

**Provenance**

- **Entry id**: 01-leadmagic

- **Source file**: 01-data-enrichment.md

- **Source line**: 179

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
