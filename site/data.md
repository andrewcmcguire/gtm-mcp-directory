# The data: directory.json, published in full

> The whole GTM MCP Directory as JSON: 293 entries, 147 official MCP servers, 827 job tags, every source URL. Free, no key, no signup. Baked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](llms.txt). The whole dataset: [directory.json](data/directory.json).*

---
[Directory](index.md) / The data

**The data endpoint**

## The whole directory, as one JSON file.

No key, no signup, no rate limit, no tracking. The same file the site is generated from, the same file the MCP server reads, published as it is. If you are an agent, start here. If you are a person building something, this is the fastest path to it.

- [directory.json](data/directory.json)

- [build_report.json](data/build_report.json)

- [search-index.json](search-index.json)

- [llms.txt](llms.txt)

- **entries**: 293
277

**unique products**

147

**official MCP servers**

827

**job tags**

1,149

**source URLs**

0

**bench tested**

**The files**

| File | Bytes | What it is |
|---|---|---|
| [data/directory.json](data/directory.json) | 1,223,763 | Every entry with every field, the 15 category blocks, the closed 55 job vocabulary with its per job counts, the duplicate groups, and the counts block the whole site renders from. |
| [data/build_report.json](data/build_report.json) | 42,980 | The counting authority's report: per file reconciliation, field coverage, every place this build is thin, and the 28 entries the tagging pass flagged for human review. |
| [search-index.json](search-index.json) | 282,189 | One compact record per unique product, which is what the on page search runs over. |
| [llms.txt](llms.txt) | text | The map, for agents and crawlers. Every section of the site with a one line description. |

**Every field on an entry**

| Field | What it holds |
|---|---|
| id | the entry id, stable across builds, prefixed with its category number |
| name / vendor_url / vendor_domain | the product and where it lives |
| what_it_does | one plain sentence, rewritten. Vendor copy never ships as the description |
| ai_features | what the AI actually does, separated from automation with an AI label on it |
| mcp_status / mcp_status_bucket | the verbatim field and the normalised bucket |
| mcp_url / mcp_urls | verbatim, and every URL parsed out of it |
| mcp_auth | verbatim. The sentence that decides your security review |
| api_gate / api_gate_bucket | verbatim, and the normalised bucket |
| jobs / jobs_tagged_by / jobs_tagged_on | tags from the closed 55 job vocabulary, and who tagged them when |
| tier / last_checked | RESEARCHED or BENCH-TESTED, and the date the facts were pulled |
| sources / source_urls / source_annotations | verbatim, and the URLs parsed out of it |
| canonical / canonical_id / also_listed_in | the 16 deliberate cross listings and where each one belongs |
| source_file / source_line | the exact line of the source markdown this entry came from |
| github_* / docs_digest / submission | present on every entry, null on every entry. Nothing has been measured for them |

**How to read it without getting it wrong**

**Two counts exist and both are correct.** 293 entries, 277 unique products. The difference is 16 products deliberately listed in two categories. Filter on `canonical` for products, count everything for entries.

**Buckets are normalised, verbatim fields are not.** Every bucket has a matching raw field beside it. When they disagree, the raw field is the fact.

**Every date means something different.** `last_checked` is when a human pulled that entry's facts. `generated_on` is only when this file was baked. `jobs_tagged_on` is when the tags were written. Do not use one for another.

**A job tag is not a test.** A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Null means unmeasured, not zero.** Every github_* field and docs_digest is null on all 293 entries because the rail that would fill them has not run.

**Terms**

Use it. Attribution to The GTM MCP Directory with a link is the only ask, and it is an ask rather than a licence trap. The data is free because it is more useful when other operators correct it, and a correction is the most valuable thing anyone can send. There is no key to request, no quota, and nothing about you is logged by this site because there is no backend to log it.

Facts about third party products are recorded from those vendors' own public sources with URLs, and every entry names them. If you are a vendor and something here is wrong, [the correction path is the same one everybody else uses](submit.md).

**Provenance**

- **Baked**: 2026-09-02

- **By**: build_directory.py (phase 1)

- **Schema version**: 1.1

- **Reconciled against tools_recount.py Network calls during the build 0 Content sha256**: 45943543d879a85fe4386a9d...

The canonical base URL used by the sitemap, the canonical tags and llms.txt is https://andrewcmcguire.com/gtm-directory, live at that address since 2026-08-27. See the [methodology page](methodology.md).
