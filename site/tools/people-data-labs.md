# People Data Labs: MCP server status, API access gate and what it does

> A raw person/company data API that returns profile records (name, job history, education, skills, social... Community MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
People Data Labs

# People Data Labs

[Community MCP](../mcp/community.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.peopledatalabs.com](https://www.peopledatalabs.com) · entry id 01-people-data-labs · source 01-data-enrichment.md line 122

**What it does**
A raw person/company data API that returns profile records (name, job history, education, skills, social handles, contact fields) matched by identifiers like email, name, or LinkedIn URL, plus SQL-style bulk search over its dataset.

**AI features, separated from automation with an AI label on it**
Uses match-confidence/"likelihood" scoring for identity resolution (i.e., probabilistic record matching) and describes some fraud-detection scoring as AI-driven; this is largely statistical matching/scoring rather than generative AI. Vendor and third-party pages use "AI-powered" broadly, but the verifiable functionality is data lookup plus a confidence score.

**RevOps role**
Bulk/programmatic person and company enrichment feeding a CRM, data warehouse, or downstream identity-resolution pipeline; commonly used as a raw-data backend rather than a polished GTM tool.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: api key (PDL_API_KEY environment variable)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/phxdev1/peopledatalabs-mcp

- [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp)

**What this server exposes**

- **Tools named**: 10
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-11
- **Repo read**: phxdev1/peopledatalabs-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **autocomplete** Get autocomplete suggestions for a partial query evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **bulk_person_enrich** Enrich multiple person profiles in a single request evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **enrich_company** Enrich a company profile with additional data evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **enrich_person** Enrich a person profile with additional data from People Data Labs evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_companies** Search for companies matching specific criteria evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_job_titles** Search for job titles matching specific criteria evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_locations** Search for locations matching specific criteria evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_people** Search for people matching specific criteria evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_schools** Search for schools matching specific criteria evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_skills** Search for skills matching specific criteria evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

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

- [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp)

**On GitHub**

[github.com/peopledatalabs](https://github.com/peopledatalabs) tied to the vendor by rule 3, account website https://www.peopledatalabs.com has the vendor's domain, confidence strong

- **Public repositories**: 7, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-08-24

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [peopledatalabs-go](https://github.com/peopledatalabs/peopledatalabs-go) | SDK | A Go client for the People Data Labs API | 7 | 2026-08-24 | v6.6.0 |
| [peopledatalabs-rust](https://github.com/peopledatalabs/peopledatalabs-rust) | SDK | A Rust client for the People Data Labs API | 1 | 2026-08-14 | v5.0.0 |
| [peopledatalabs-js](https://github.com/peopledatalabs/peopledatalabs-js) | SDK | A universal JS client with TypeScript support for the People Data Labs API | 26 | 2026-08-14 | v14.4.0 |
| [peopledatalabs-python](https://github.com/peopledatalabs/peopledatalabs-python) | SDK | A Python client for the People Data Labs API | 40 | 2026-06-04 | v6.4.13 |
| [peopledatalabs-ruby](https://github.com/peopledatalabs/peopledatalabs-ruby) | SDK | A Ruby client for the People Data Labs API | 5 | 2026-04-21 | v5.2.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Reverse-look-up a person from an email](../jobs/reverse-lookup-person-from-email.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://support.peopledatalabs.com/hc/en-us/articles/25794271805211-Pricing-credits](https://support.peopledatalabs.com/hc/en-us/articles/25794271805211-Pricing-credits)
- [https://nubela.co/blog/people-data-labs-pricing/](https://nubela.co/blog/people-data-labs-pricing/)
- [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp)
- [https://glama.ai/mcp/servers/phxdev1/peopledatalabs-mcp](https://glama.ai/mcp/servers/phxdev1/peopledatalabs-mcp)
- [https://saleshive.com/vendors/peopledatalabs](https://saleshive.com/vendors/peopledatalabs)

5 source URLs. Raw sources field, verbatim:

https://support.peopledatalabs.com/hc/en-us/articles/25794271805211-Pricing-credits, https://nubela.co/blog/people-data-labs-pricing/, https://github.com/phxdev1/peopledatalabs-mcp, https://glama.ai/mcp/servers/phxdev1/peopledatalabs-mcp, https://saleshive.com/vendors/peopledatalabs

**Notes, verbatim from the file**
Free plan is $0/mo, no credit card required, up to 100 records/month, but contact fields (email/phone) return only as true/false flags, not actual values, on the free tier. Self-serve Pro plan starts ~$98/mo (350 records) with full contact field access, tiered per-credit pricing (~$0.25-$0.28/credit for Person data), and a separate $0.55/credit Person Identify API. The MCP server found (github.com/phxdev1/peopledatalabs-mcp) is a third-party/community project, not published by People Data Labs itself - no official PDL-run MCP was found.

**Provenance**

- **Entry id**: 01-people-data-labs

- **Source file**: 01-data-enrichment.md

- **Source line**: 122

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
