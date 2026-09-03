# Surfe: MCP server status, API access gate and what it does

> A Chrome extension plus API that pulls contacts and companies off LinkedIn, runs them through a multi-vendor... Official MCP, Enterprise only. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Surfe

# Surfe

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [surfe.com](https://surfe.com) · entry id 01-surfe · source 01-data-enrichment.md line 679

**What it does**
A Chrome extension plus API that pulls contacts and companies off LinkedIn, runs them through a multi-vendor waterfall to find verified emails and mobile numbers, and pushes the records into a CRM.

**AI features, separated from automation with an AI label on it**
Mostly not AI. The core is a waterfall chaining 15+ data providers, which is routing and dedupe logic. Genuinely LLM-shaped: the AI message generation on LinkedIn and an AI-guided daily shortlist that ranks accounts by ICP fit and recent events. The buying-signals feed (funding, hiring spikes, promotions, news) is event scraping plus filters marketed as AI, and the "AI Agents monitor sources around the clock" copy describes scheduled monitoring with no evidence of autonomous reasoning agents. Blunt version: the AI here is a message writer and a ranking layer bolted onto a data business.

**RevOps role**
LinkedIn-to-CRM capture and waterfall enrichment for SDR teams, with an API and MCP layer for programmatic enrichment and CRM hygiene.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Surfe API key, with a browser sign-in flow that exchanges the key for a managed token so it is entered once, or the key passed directly per call. Hosted remote server only, no public GitHub repo.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.eu.surfe.com/mcp](https://mcp.eu.surfe.com/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.eu.surfe.com/mcp (docs: https://developers.surfe.com/mcp)

- [https://mcp.eu.surfe.com/mcp](https://mcp.eu.surfe.com/mcp)
- [https://developers.surfe.com/mcp](https://developers.surfe.com/mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

[https://developers.surfe.com/](https://developers.surfe.com/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.surfe.com/pricing/](https://www.surfe.com/pricing/)
- [https://www.surfe.com/api/](https://www.surfe.com/api/)
- [https://developers.surfe.com/mcp](https://developers.surfe.com/mcp)
- [https://www.surfe.com/leadjet-becomes-surfe/](https://www.surfe.com/leadjet-becomes-surfe/)
- [https://intercom.help/surfe/en/articles/11681517-api-credits-quotas](https://intercom.help/surfe/en/articles/11681517-api-credits-quotas)
- [https://developers.surfe.com/public-015-create-people-bulk-enrichment](https://developers.surfe.com/public-015-create-people-bulk-enrichment)

6 source URLs. Raw sources field, verbatim:

https://www.surfe.com/pricing/, https://www.surfe.com/api/, https://developers.surfe.com/mcp, https://www.surfe.com/leadjet-becomes-surfe/, https://intercom.help/surfe/en/articles/11681517-api-credits-quotas, https://developers.surfe.com/public-015-create-people-bulk-enrichment

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. REBRAND: this was Leadjet, renamed to Surfe in October 2022 alongside a EUR 4M seed led by 360 Capital; Product Hunt still hosts it under the legacy /products/leadjet slug. Dating trap for researchers: the vendor's own rebrand post now carries a republished date of 2026-05-26, which is a content refresh, not the rebrand date. Paris-based, actively shipping, public roadmap at roadmap.surfe.com and release notes at releases.surfe.com. UNRESOLVED CONTRADICTION on api_gate: self-serve tiers are Free $0 (20 email finds, 5 mobile), Essential $49/mo or $39/mo annual, Pro $89/mo or $79/mo annual, Enterprise custom, and ONLY the Enterprise row lists "API (search and waterfall enrichment)", with the API product page publishing no API pricing and offering "Talk to partnerships". But the developer docs describe an apparently self-serve path with per-endpoint daily quotas from 200 results/day up to 50,000 profiles/day. Recorded as enterprise-only because that is what the vendor's own pricing table says; the docs may simply be ahead of the pricing page. Credits are consumed only on successful returns. Eight MCP tools across People, Companies and Account. NAMING TRAP: "Surfe MCP" searches are heavily polluted by SurferSEO, the Surfer waveform viewer, and various crypto "surf" servers, none of which are this vendor. 2026-09-03: vendor docs state the Enrich People endpoint (POST /v2/people/enrich) accepts firstName, lastName and companyName or companyDomain per person and "Set include.linkedInUrl to return additional profile data" (https://developers.surfe.com/public-015-create-people-bulk-enrichment); the MCP docs list people search and enrichment tools without naming them (https://developers.surfe.com/mcp); the docs state 1 email credit per email found and 1 mobile credit per mobile found, with no price stated for the LinkedIn URL.

**Provenance**

- **Entry id**: 01-surfe

- **Source file**: 01-data-enrichment.md

- **Source line**: 679

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
