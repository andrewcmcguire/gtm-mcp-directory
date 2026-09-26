# HubSpot: Why Now account card in The GTM MCP Directory

> HubSpot Why Now account card in The GTM MCP Directory. Honesty badge official, 2 linked directory products. Last enriched 2026-09-21. Data baked 2026-09-26.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../../llms.txt). The whole dataset: [directory.json](../../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../../index.md) /
[Companies](../../companies/index.md) /
HubSpot

# HubSpot

[Official MCP](../../mcp/official.md) · HUBS · Why Now account card · Last enriched 2026-09-21 · Data baked 2026-09-26

Why Now account card · [hubspot.com](https://hubspot.com) · [Public company earnings brief (HUBS)](https://andrewcmcguire.com/companies/hubspot/) · slug hubspot

[RevOps Infra](../../categories/revops-infra.md) · [AI SDRs](../../categories/ai-sdr-agents.md) · [Read CRM records](../../jobs/read-crm-records.md) · [Write CRM records](../../jobs/write-crm-records.md) · [Run an email sequence](../../jobs/run-email-sequence.md) · [Draft personalized outreach](../../jobs/draft-personalized-outreach.md)

Honesty badge and every tool count on this page are copied from [directory.json](../../data.md) at build time. Authored company JSON cannot override them. Public-company intel source of record is fin45 / GTM Signals Postgres, not this repo.

**about**

Helping Millions of Organizations Grow Better

receipt: [https://www.hubspot.com/company](https://www.hubspot.com/company) · as_of 2026-09-21 · Vendor about page, mission heading. Verbatim.

**why_now**

why_now abstains. No verbatim public quote with a resolvable receipt is on this record. Empty is honest; it is not a missing scoop.

why_now needs a verbatim quote and a resolvable receipt_url. Abstain (empty array) if the quote is weak or unpublished.

**Identity**

- **account_id**: null (unissued here)
- **legal_name**: HubSpot
- **ticker**: HUBS
- **cik**: 0001404655
- **domain**: [hubspot.com](https://hubspot.com)
- **linkedin_company_url**: [https://www.linkedin.com/company/hubspot](https://www.linkedin.com/company/hubspot)
- **entry_point_account_id**: null (abstain: no proved parent id, no self id)

account_id is a feed value only. This repo does not mint acc_ from the slug. entry_point_account_id is the proved parent id, else this record's account_id, else null. Never a tenant go-after id. linkedin_company_url is copied from identity.linkedin_url only when that URL is a LinkedIn company or school page. The enrichment sidecar may supply that URL with a receipt; --apply-identity copies it here when this field is null.

**family**

family is empty. parent_account_id is null. subsidiaries is empty. No EX-21 proved nodes are on this record.

entry_point_account_id: null. family.subsidiaries takes EX-21 proved nodes only. Do not guess children. parent_account_id is proved parent only.

**executives (filing roster)**

executives is empty. Filing-roster and licensed sources only. No email. No phone. Empty is not a claim this company has no officers.

**executives (public roster)**

| name | role | roster source | as_of |
|---|---|---|---|
| [Yamini Rangan](https://www.hubspot.com/company/management/yamini-rangan) | Chief Executive Officer | [vendor management roster](https://www.hubspot.com/company/management) | 2026-09-21 |
| Dharmesh Shah | Co-Founder, CTO | [vendor management roster](https://www.hubspot.com/company/management) | 2026-09-21 |
| Duncan Lennox | Chief Product & Technology Officer | [vendor management roster](https://www.hubspot.com/company/management) | 2026-09-21 |
| Kate Bueker | Chief Financial Officer | [vendor management roster](https://www.hubspot.com/company/management) | 2026-09-21 |
| Erika Fisher | Chief Legal Officer | [vendor management roster](https://www.hubspot.com/company/management) | 2026-09-21 |
| Helen Russell | Chief People Officer | [vendor management roster](https://www.hubspot.com/company/management) | 2026-09-21 |
| Kipp Bodnar | Chief Marketing Officer | [vendor management roster](https://www.hubspot.com/company/management) | 2026-09-21 |
| Jon Dick | Chief Customer Officer | [vendor management roster](https://www.hubspot.com/company/management) | 2026-09-21 |

Public roster only. No email. No phone. profile_url is a public bio, not a contact. company-v1.executives stays the filing-roster field and may still be empty.

**github (MCP-relevant)**

- **org**: [HubSpot](https://github.com/HubSpot)
- **website**: http://product.hubspot.com/

receipt: [https://github.com/HubSpot](https://github.com/HubSpot) · as_of 2026-09-08 · Resolved in github_orgs.json for 01-clearbit / hubspot.com (rule 3, website match).

| repo | party | relevance | as_of |
|---|---|---|---|
| [HubSpot/hubspot-mcp-plugins](https://github.com/HubSpot/hubspot-mcp-plugins) | first-party | First-party repo on the HubSpot org. Directory notes (2026-09-09) say it holds Claude Code client configuration for the HubSpot MCP server, not the server source. | 2026-09-09 |

community repos stay community. They never become official. Tool counts stay on directory.json.

**how_mcp_published**

Directory honesty badge is official. That badge is copied from linked canonical entries (06-hubspot official, 04-hubspot-breeze none-found). HubSpot publishes two first-party MCP surfaces on its developer docs: a hosted Remote MCP server for CRM read/write, and a local Developer MCP server via the HubSpot CLI. The directory connect URL is https://developers.hubspot.com/ai-tools/mcp. The first-party GitHub repo HubSpot/hubspot-mcp-plugins is client configuration, not server source. HubSpot/mcp-server was an empty repository on 2026-09-09 and is not treated as a source. Community HubSpot MCP servers exist and are not this official surface. This sidecar does not invent a tool count.

Directory honesty badge on this sidecar: official. This prose cannot invent official or a tool count.

| kind | url | note |
|---|---|---|
| vendor-docs | [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp) | Primary directory mcp_url on 06-hubspot. |
| hosted-endpoint | [https://mcp.hubspot.com](https://mcp.hubspot.com) | Named on the vendor docs as the Remote MCP host. Not a status and not a count. |
| first-party-repo | [https://github.com/HubSpot/hubspot-mcp-plugins](https://github.com/HubSpot/hubspot-mcp-plugins) | Client configuration, not server source. |
| directory-entry | [https://andrewcmcguire.com/gtm-directory/tools/hubspot](https://andrewcmcguire.com/gtm-directory/tools/hubspot) | Honesty and tool counts live on the directory entry. |

receipt: [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp) · as_of 2026-09-21

receipt: [https://github.com/HubSpot/hubspot-mcp-plugins](https://github.com/HubSpot/hubspot-mcp-plugins) · as_of 2026-09-09 · Recorded on directory entry 06-hubspot notes.

**mcp_package_hint**

- **slug**: hubspot
- **page_url**: [https://andrewcmcguire.com/gtm-directory/companies/hubspot/](https://andrewcmcguire.com/gtm-directory/companies/hubspot/)
- **listing_url**: [https://andrewcmcguire.com/gtm-directory/tools/hubspot](https://andrewcmcguire.com/gtm-directory/tools/hubspot)
- **mcp_url**: [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp)
- **ticker**: HUBS
- **domain**: hubspot.com

Locator only: slug, page_url, listing_url, mcp_url, plus ticker and domain when present. This is not an MCP status and not a tool count.

**Directory facts that beat this file**

| Product | MCP status | Tools catalogued | Endpoint probe | last_checked |
|---|---|---|---|---|
| [HubSpot](../../tools/hubspot.md) | Official MCP | 25 named, harvested 2026-09-26, evidence docs | did not answer | 2026-08-24 |
| [HubSpot Breeze (AI Prospecting Agent)](../../tools/hubspot-breeze.md) | No MCP found | not measured (0 means not measured, not zero tools) | n/a | 2026-09-02 |

Company honesty_badge is the strongest mcp_status_bucket among linked canonical directory entries, in order official, community, unknown, none-found. n-a is ignored. Mixed products stay visible on the page; the badge does not hide a none-found sibling. Derived badge for this page: official. A catalogued tool is a name a server published. Nobody has called it unless tier is BENCH-TESTED. 1 of 1,252 directory entries are bench tested.

**tools in the directory, 2**

### [HubSpot](../../tools/hubspot.md)

An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform.

[Official MCP](../../mcp/official.md)
[Free to start](../../gates/free.md)
[RevOps Infra](../../categories/revops-infra.md)
RESEARCHED

- **Directory id**: 06-hubspot

- **Tools catalogued**: 25 named, harvested 2026-09-26, evidence docs

- **Endpoint probe**: did not answer

- **last_checked**: 2026-08-24

- **MCP URL on the entry**: [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp)

### [HubSpot Breeze (AI Prospecting Agent)](../../tools/hubspot-breeze.md)

Monitors accounts for buying signals (funding, leadership changes, site visits) via integrated data providers (ZoomInfo, Apollo, Surfe, Seamless), identifies decision-makers, and drafts personalized outreach emails in a rep's voice; can send with human review...

[No MCP found](../../mcp/none-found.md)
[Paid, self-serve](../../gates/paid.md)
[AI SDRs](../../categories/ai-sdr-agents.md)
RESEARCHED

- **Directory id**: 04-hubspot-breeze

- **Tools catalogued**: not measured (0 means not measured, not zero tools)

- **Endpoint probe**: n/a

- **last_checked**: 2026-09-02

- **MCP URL on the entry**: no MCP URL on the entry

Product rollup by domain: [vendor page](../../vendors/hubspot-com.md) (existing /vendors/ surface, not this company record).

**provenance**

- **last_enriched**: 2026-09-21
- **source_of_record**: fin45 / GTM Signals Postgres for public-company intel; directory.json for MCP honesty
- **enrichment_scope**: company-level

legal_name and domain from directory entries 06-hubspot and 04-hubspot-breeze. ticker HUBS from the existing PUBLIC_COMPANIES map. cik 0001404655 from SEC EDGAR. linkedin_company_url from HubSpot's own docs handle example company/hubspot. mcp_package_hint.mcp_url copied from 06-hubspot. account_id, family, why_now, and company-v1 executives are unissued or empty. Public-roster executives live in the enrichment sidecar. No EX-21 nodes. No acc_ minted from slug.

Enrichment is company-level only. No tenant book, no ICP, no go-after, no contact harvest.

**What this page does not claim**

This is a Why Now account card, not a Scoops or ZoomInfo clone. It does not invent an official MCP server. It does not invent a tool count. It does not carry tenant book, ICP, go-after, email, or phone. Job tags on the linked entries mean the vendor says the product does that job. 1 of 1,252 directory entries are bench tested. Enrichment sidecar fields are receipt-gated and may be empty.

URL: `/gtm-directory/companies/hubspot/`. Schema: company-v1 plus enrichment-v1. Last enriched 2026-09-21. Data baked 2026-09-26 by build_directory.py (phase 1).

Why Now account card plus enrichment sidecar. Empty why_now is an abstain, not a missing scoop. Empty company-v1 executives means no filing-roster harvest. Public management-roster names are on enrichment/hubspot.json.
