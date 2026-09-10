# Prospeo: MCP server status, API access gate and what it does

> A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given... Official MCP, Free to start. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Prospeo

# Prospeo

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03
CLI: prospeo (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [prospeo.io](https://prospeo.io) · entry id 01-prospeo · source 01-data-enrichment.md line 198

**What it does**
A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given person or domain and returns basic firmographic data (headcount, industry, tech stack) for companies; also supports filtered people/company search.

**AI features, separated from automation with an AI label on it**
No credible AI capability surfaced in sources reviewed. Core mechanism is database lookup, email-pattern generation, domain search, and SMTP-based verification - a plain enrichment/lookup tool, not an AI-driven one, despite the modern positioning common in this category.

**RevOps role**
Email/phone finder and person+company search layer, most often plugged into Clay waterfalls (Clay-managed account billed at 2 credits/enriched cell) or used directly as a fallback provider alongside other finders.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 for the hosted server (auto-handled by Claude.ai/Desktop via the MCP directory); local/self-hosted setup uses an API key via PROSPEO_API_KEY env var or X-KEY header

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/prospeo-v2/prospeo-mcp-server

- [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server)

**What this server exposes**

- **Tools named**: 8
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-10
- **Repo read**: prospeo-v2/prospeo-mcp-server
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **bulk_enrich_company** Enrich up to 25 companies in ONE call - the canonical lookup tool when you already have a list of company names/domains (CRM exports, account lists, competitor maps). evidence: in the server source · calling it reads

- **bulk_enrich_person** Enrich up to 25 people in ONE call - the canonical follow-up to search_person. evidence: in the server source · calling it reads

- **enrich_company** Enrich a company - return its full profile (headcount, industry, revenue, tech stack, funding, social links, HQ phone). evidence: in the server source · calling it reads

- **enrich_person** Enrich a SINGLE person - return their full profile with verified email and/or mobile, job history, and current company. evidence: in the server source · calling it reads

- **get_account_info** Check your Prospeo account status - credits remaining, plan name, renewal date, and team size. evidence: in the server source · calling it reads

- **search_company** Search Prospeo evidence: in the server source · calling it reads

- **search_person** Search Prospeo evidence: in the server source · calling it reads

- **search_suggestions** Resolve canonical filter values BEFORE building a search. Free - no credit cost. evidence: in the server source · calling it reads

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-10. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: prospeo
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-10

Install, as the source shows it:

```
npm install -g prospeo-cli
```

quoted from [https://www.npmjs.com/package/prospeo-cli](https://www.npmjs.com/package/prospeo-cli) on 2026-09-10, via npm, a third party source

Packages seen, with the version on 2026-09-10:

- [npm: prospeo-cli 0.2.0, third party](https://www.npmjs.com/package/prospeo-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-10.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Meerkats-Ai/prospeo-mcp-server](https://github.com/Meerkats-Ai/prospeo-mcp-server)
- [https://github.com/orchidautomation/prospeo-mcp](https://github.com/orchidautomation/prospeo-mcp)
- [https://github.com/prospeo-v2](https://github.com/prospeo-v2)
- [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server)

**On GitHub**

[github.com/prospeo-v2](https://github.com/prospeo-v2) tied to the vendor by rule 1, account website prospeo.io has the vendor's domain, confidence strong

- **Public repositories**: 2, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-07-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server) | MCP server | MCP Server for integrating Prospeo API. | 0 | 2026-07-03 | |
| [n8n-nodes-prospeo](https://github.com/prospeo-v2/n8n-nodes-prospeo) | plugin or integration | n8n integration for Prospeo | 0 | 2026-01-29 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server)
- [https://github.com/prospeo-v2](https://github.com/prospeo-v2)
- [https://github.com/orchidautomation/prospeo-mcp](https://github.com/orchidautomation/prospeo-mcp)
- [https://github.com/Meerkats-Ai/prospeo-mcp-server](https://github.com/Meerkats-Ai/prospeo-mcp-server)
- [https://fullenrich.com/content/prospeo-pricing](https://fullenrich.com/content/prospeo-pricing)
- [https://www.xpay.sh/saas-pricing/prospeo-io/](https://www.xpay.sh/saas-pricing/prospeo-io/)
- [https://www.clay.com/integrations/data-provider/prospeo](https://www.clay.com/integrations/data-provider/prospeo)
- [https://university.clay.com/docs/prospeo-integration-overview](https://university.clay.com/docs/prospeo-integration-overview)
- [https://prospeo.io/api-docs/enrich-person](https://prospeo.io/api-docs/enrich-person)
- [https://prospeo.io/api-docs/mcp](https://prospeo.io/api-docs/mcp)

10 source URLs. Raw sources field, verbatim:

https://github.com/prospeo-v2/prospeo-mcp-server, https://github.com/prospeo-v2, https://github.com/orchidautomation/prospeo-mcp, https://github.com/Meerkats-Ai/prospeo-mcp-server, https://fullenrich.com/content/prospeo-pricing, https://www.xpay.sh/saas-pricing/prospeo-io/, https://www.clay.com/integrations/data-provider/prospeo, https://university.clay.com/docs/prospeo-integration-overview, https://prospeo.io/api-docs/enrich-person, https://prospeo.io/api-docs/mcp

**Notes, verbatim from the file**
Confirmed as a Clay "data provider" (native waterfall integration), a separate integration surface from the MCP. Besides the official prospeo-v2 MCP repo, at least two unofficial community MCP wrappers exist (orchidautomation/prospeo-mcp, Meerkats-Ai/prospeo-mcp-server), both hitting the same public API. Pricing sources conflict slightly: most describe a self-serve free plan (100 credits/mo) plus paid plans from $39-49/mo, but one third-party source claimed the public pricing page pushes visitors to a sales-contact form - flagged as a discrepancy, not resolved. 2026-09-03: vendor docs state the Enrich Person API (POST /enrich-person) accepts first name + last name + a company identifier (name/website/LinkedIn URL) and returns linkedin_url, described as "The person's public LinkedIn URL" (https://prospeo.io/api-docs/enrich-person); MCP tool enrich_person is listed in the MCP docs, described there as returning professional email and/or mobile (https://prospeo.io/api-docs/mcp); the enrich page states 1 credit per email found and no charge if no match is found.

**Provenance**

- **Entry id**: 01-prospeo

- **Source file**: 01-data-enrichment.md

- **Source line**: 198

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-10

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
