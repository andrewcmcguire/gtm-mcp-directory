# Wiza: MCP server status, API access gate and what it does

> Pulls verified work emails and mobile numbers for people found on LinkedIn or Sales Navigator and exports... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Wiza

# Wiza

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [wiza.co](https://wiza.co) · entry id 01-wiza · source 01-data-enrichment.md line 619

**What it does**
Pulls verified work emails and mobile numbers for people found on LinkedIn or Sales Navigator and exports them to CSV or a CRM.

**AI features, separated from automation with an AI label on it**
One genuine AI surface, "AI Research" / AI Columns, which takes a natural-language question about a company or contact, scans the public web, and returns a structured answer plus a reasoning string as a filterable column. Everything else, the 850M-contact database, the Chrome extension, the SMTP deliverability check, is a database with a filter and a mail-server ping. Wiza does not disclose which model powers AI Research.

**RevOps role**
Top-of-funnel contact acquisition sitting between Sales Navigator and the CRM or sequencer, with an optional LLM research column for ICP qualification.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.1 with PKCE for clients that support it, otherwise a static bearer token in the Authorization header using a Wiza API key. Streamable HTTP transport.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.wiza.co/mcp](https://mcp.wiza.co/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.wiza.co/mcp (docs: https://mcp.wiza.co/usage.html; announced at https://feedback.wiza.co/changelog/wiza-mcp)

- [https://mcp.wiza.co/mcp](https://mcp.wiza.co/mcp)
- [https://mcp.wiza.co/usage.html](https://mcp.wiza.co/usage.html)
- [https://feedback.wiza.co/changelog/wiza-mcp](https://feedback.wiza.co/changelog/wiza-mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://docs.wiza.co/](https://docs.wiza.co/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://wiza.co/pricing](https://wiza.co/pricing)
- [https://docs.wiza.co/](https://docs.wiza.co/)
- [https://mcp.wiza.co/usage.html](https://mcp.wiza.co/usage.html)
- [https://feedback.wiza.co/changelog/wiza-mcp](https://feedback.wiza.co/changelog/wiza-mcp)
- [https://wiza.co/ai-research](https://wiza.co/ai-research)
- [https://docs.wiza.co/api-reference/individual-reveals/start-individual-reveal](https://docs.wiza.co/api-reference/individual-reveals/start-individual-reveal)
- [https://docs.wiza.co/overview/data-dictionary.md](https://docs.wiza.co/overview/data-dictionary.md)

7 source URLs. Raw sources field, verbatim:

https://wiza.co/pricing, https://docs.wiza.co/, https://mcp.wiza.co/usage.html, https://feedback.wiza.co/changelog/wiza-mcp, https://wiza.co/ai-research, https://docs.wiza.co/api-reference/individual-reveals/start-individual-reveal, https://docs.wiza.co/overview/data-dictionary.md

**Notes, verbatim from the file**
Added 2026-08-25, closing a named warm lead from this file's previous sweep notes. Self-serve tiers are Free $0 (20 valid emails, 5 phones), Starter $49/mo, Email $99/mo, Email + Phone $199/mo, with annual at $990/yr and $1,990/yr. UNRESOLVED CONTRADICTION worth flagging to readers: "API access" appears on the pricing page only under the custom-priced, 3+ seat, annual Team plan, which means a sales call, while the MCP changelog says the server "is available today for all Wiza users" and needs only "a Wiza API key". Neither docs page states a plan requirement. Settling this needs an account, so api_gate is recorded as paid on the pricing page's authority. Documented MCP tools: enrich_contact, enrich_company, get_credits, search_companies, search_prospects. 2026-09-03: vendor docs state an individual reveal (POST /api/individual_reveals) takes full_name plus company or domain ("You can provide a name, company, and domain, or an email, or a LinkedIn profile URL") and the result carries the Profile Details fields of the data dictionary, which include Profile URL (https://docs.wiza.co/api-reference/individual-reveals/start-individual-reveal, https://docs.wiza.co/overview/data-dictionary.md); MCP tool enrich_contact is described as enriching "using a LinkedIn URL, email, or name plus company/domain" (https://mcp.wiza.co/usage.html); no per-lookup price is stated on those pages.

**Provenance**

- **Entry id**: 01-wiza

- **Source file**: 01-data-enrichment.md

- **Source line**: 619

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
