# Company pages (Why Now account cards)

> 3 Why Now account cards in The GTM MCP Directory company-v1 scaffold. Honesty badges and tool counts come from directory.json. Data baked 2026-09-26.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) / Companies

**Scaffold**

## Why Now account cards.

3 company records in the SteadyBase company-v1 shape, emitted at `/gtm-directory/companies/{slug}/`. Each page is an account card (identity, family, why_now, executives, mcp_package_hint) plus a directory overlay. MCP honesty badges and tool counts are copied from directory.json. why_now abstains when there is no verbatim quote with a receipt. company-v1 executives stay empty without a filing roster. The enrichment sidecar may add a cited about blurb, a LinkedIn company URL, public-roster executives, GitHub MCP repos, and how_mcp_published prose tied to the directory badge. family stays empty without EX-21 proof.

This is not the same surface as [Vendors](../vendors/index.md), which groups every product by vendor domain. It is also not [/companies/](https://andrewcmcguire.com/companies/) on the apex, which is earnings-call briefs. Public-company intel source of record is fin45 / GTM Signals Postgres. Read `directory/product/companies/COMPANY_PAGES.md` before adding a record.

| legal_name | domain | ticker | Honesty badge | Linked tools | Last enriched |
|---|---|---|---|---|---|
| [Clay](clay/) | clay.com | null | Official MCP | 1 | 2026-09-21 |
| [Exa](exa/) | exa.ai | null | Official MCP | 1 | 2026-09-21 |
| [HubSpot](hubspot/) | hubspot.com | HUBS | Official MCP | 2 | 2026-09-21 |
