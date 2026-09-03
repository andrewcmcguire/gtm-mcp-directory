# TheirStack: MCP server status, API access gate and what it does

> Tracks 233M+ job postings across 195+ countries and 33,000+ technologies to detect hiring signals,... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
TheirStack

# TheirStack

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://theirstack.com](https://theirstack.com) · entry id 05-theirstack · source 05-signals-intent-abm.md line 539

**What it does**
Tracks 233M+ job postings across 195+ countries and 33,000+ technologies to detect hiring signals, technographic footprint, and buying-intent signals (job-posting keywords implying a company has or needs a specific type of software).

**AI features, separated from automation with an AI label on it**
Primarily rules/keyword-based signal detection (job posting text matched to technology/problem keywords) - data aggregation, not core ML. Three separate MCP servers are an LLM-agent access layer over the same structured datasets, not a new detection method.

**RevOps role**
Hiring/technographic/intent signal feed used to build outbound target lists based on what companies are hiring for or which tech-stack gaps they have.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - page references a "How does authentication work?" FAQ but the answer wasn't visible in the fetched content; requires free signup/login to use.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://theirstack.com/en/job-posting-mcp](https://theirstack.com/en/job-posting-mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://theirstack.com/en/job-posting-mcp (also technographics-mcp and buying-intent-mcp at the same domain)

- [https://theirstack.com/en/job-posting-mcp](https://theirstack.com/en/job-posting-mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Scrape job postings](../jobs/scrape-job-postings.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: TheirStack

- **Category**: [Data & Enrichment](../categories/data-enrichment.md)

- **MCP status there**: Official MCP

- **Gate there**: Free to start

- **Source**: 01-data-enrichment.md line 483

- **Canonical page**: [TheirStack](../tools/theirstack.md)

What that listing says it does: A job-postings and technographic-data API that tracks live job listings and the tech stack/hiring signals behind them across 195 countries (claims 223M+ jobs, 352K+ sources), queryable for GTM timing/intent signals.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://theirstack.com/](https://theirstack.com/)
- [https://theirstack.com/en/pricing](https://theirstack.com/en/pricing)
- [https://theirstack.com/en/job-posting-mcp](https://theirstack.com/en/job-posting-mcp)

3 source URLs. Raw sources field, verbatim:

https://theirstack.com/, https://theirstack.com/en/pricing, https://theirstack.com/en/job-posting-mcp

**Notes, verbatim from the file**
Free trial plus credit-based pricing from $49/mo (API credits) up to $5,500/mo; one-time credit packs $109-$999; a full "talk to sales" enterprise tier exists for the complete datasets. Three separate MCP servers (jobs, technographics, buying intent) rather than one unified server - see Sweep notes for MCP-of-the-Week candidacy.

**Provenance**

- **Entry id**: 05-theirstack

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 539

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
