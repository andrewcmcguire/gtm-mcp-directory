# Clay: MCP server status, API access gate and what it does

> A spreadsheet-style workflow/orchestration tool that runs lead and company records through "waterfall"... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Clay

# Clay

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [clay.com](https://clay.com) · entry id 01-clay · source 01-data-enrichment.md line 46

**What it does**
A spreadsheet-style workflow/orchestration tool that runs lead and company records through "waterfall" lookups across 100-200+ third-party data providers (Apollo, Lusha, Clearbit, etc.) and chains automation steps ("recipes") to build, enrich, and route prospect lists into a CRM or sequencer.

**AI features, separated from automation with an AI label on it**
"Claygent" is a genuine LLM agent that can browse the web and do open-ended research inside a workflow step (e.g., "find this company's funding stage"), plus an AI formula/code generator for building enrichment logic. This is real AI for the unstructured-research steps; the waterfall/enrichment core is deterministic API-calling across vendors, not AI itself.

**RevOps role**
Sits between raw data vendors and the CRM/outbound stack as the enrichment-orchestration layer a RevOps team builds once and reps or automations call into

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Session cookie - the same token used to log into app.clay.com in-browser, which grants full account access (tables, records, enrichments, CRM integrations, credits), not a scoped API key

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.clay.com/mcp](https://www.clay.com/mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.clay.com/mcp (docs: https://university.clay.com/docs/mcp-settings)

- [https://www.clay.com/mcp](https://www.clay.com/mcp)
- [https://university.clay.com/docs/mcp-settings](https://university.clay.com/docs/mcp-settings)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/shanefirek/clay-mcp-public](https://github.com/shanefirek/clay-mcp-public)

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Build a target account list](../jobs/build-target-account-list.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.clay.com/mcp](https://www.clay.com/mcp)
- [https://university.clay.com/docs/mcp-settings](https://university.clay.com/docs/mcp-settings)
- [https://github.com/shanefirek/clay-mcp-public](https://github.com/shanefirek/clay-mcp-public)
- [https://www.landbase.com/blog/clay-pricing](https://www.landbase.com/blog/clay-pricing)
- [https://www.warmly.ai/p/blog/clay-pricing](https://www.warmly.ai/p/blog/clay-pricing)
- [https://michaelsaruggia.com/blog/clay-pricing-change-2026](https://michaelsaruggia.com/blog/clay-pricing-change-2026)
- [https://www.clay.com/integrations/action/find-a-persons-linkedin-via-name-and-company-smarte](https://www.clay.com/integrations/action/find-a-persons-linkedin-via-name-and-company-smarte)

7 source URLs. Raw sources field, verbatim:

https://www.clay.com/mcp, https://university.clay.com/docs/mcp-settings, https://github.com/shanefirek/clay-mcp-public, https://www.landbase.com/blog/clay-pricing, https://www.warmly.ai/p/blog/clay-pricing, https://michaelsaruggia.com/blog/clay-pricing-change-2026, https://www.clay.com/integrations/action/find-a-persons-linkedin-via-name-and-company-smarte

**Notes, verbatim from the file**
Self-serve plans exist (Free, Launch ~$185/mo, Growth ~$495/mo as of the March 2026 repricing) with a dual Data Credits / Actions system, so a solo operator can get in without sales - but real usage costs scale fast via credit top-ups (50% premium) and this pricing structure changed substantially in March 2026. A separate 73-tool community MCP (github.com/shanefirek/clay-mcp-public) also exists. Caution: "Clay" the personal-CRM app (clay.earth, github.com/mesh/clay-mcp) is an unrelated product with its own MCP - do not confuse it with Clay.com in this directory. 2026-09-03: Clay's integration catalog lists the action "Find a Person's LinkedIn via Name and Company with SMARTe", described as "This action enables users to find a person's LinkedIn profile using their name and company", returning Contact Social URL and billed by Clay Credits or Bring Your Own Account with no unit cost stated (https://www.clay.com/integrations/action/find-a-persons-linkedin-via-name-and-company-smarte); the Clay MCP docs list People Search, Company Search and Functions and name no LinkedIn-finder tool (https://university.clay.com/docs/mcp-settings).

**Provenance**

- **Entry id**: 01-clay

- **Source file**: 01-data-enrichment.md

- **Source line**: 46

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
