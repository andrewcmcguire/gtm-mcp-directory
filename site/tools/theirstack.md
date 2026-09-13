# TheirStack: MCP server status, API access gate and what it does

> Tracks 233M+ job postings across 195+ countries and 33,000+ technologies to detect hiring signals,... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
TheirStack

# TheirStack

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://theirstack.com](https://theirstack.com) · entry id 05-theirstack · source 05-signals-intent-abm.md line 544

**What it does**
Tracks 233M+ job postings across 195+ countries and 33,000+ technologies to detect hiring signals, technographic footprint, and buying-intent signals (job-posting keywords implying a company has or needs a specific type of software).

**AI features, separated from automation with an AI label on it**
Primarily rules/keyword-based signal detection (job posting text matched to technology/problem keywords) - data aggregation, not core ML. Three separate MCP servers are an LLM-agent access layer over the same structured datasets, not a new detection method.

**RevOps role**
Hiring/technographic/intent signal feed used to build outbound target lists based on what companies are hiring for or which tech-stack gaps they have.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - page references a "How does authentication work?" FAQ but the answer wasn't visible in the fetched content; requires free signup/login to use.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://theirstack.com/en/job-posting-mcp](https://theirstack.com/en/job-posting-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.theirstack.com/mcp/ ; https://theirstack.com/en/job-posting-mcp (also technographics-mcp and buying-intent-mcp at the same domain)

- [https://api.theirstack.com/mcp/](https://api.theirstack.com/mcp/)
- [https://theirstack.com/en/job-posting-mcp](https://theirstack.com/en/job-posting-mcp)

**What this server exposes**

- **Tools named**: 3
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

The harvest recorded this server against the cross listing **TheirStack** in Data & Enrichment. It is the same server, so the list is shown here rather than left blank.

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **search_companies** The search_companies tool lets you find companies that use a particular technology, filtered by location, size, or industry. evidence: in the vendor docs · calling it reads

- **search_jobs** Find jobs by title, location, salary, seniority, technology, or any combination evidence: in the vendor docs · calling it reads

- **technographics** Your AI assistant calls the technographics tool to get any company's full technology stack, categorized by type, with detection dates and confidence signals. evidence: in the vendor docs · calling it reads

119 of the 415 entries that record an official or community MCP server carry a harvested tool list. The other 296 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited)

**API documentation**

No documentation URL recorded.

582 of 884 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to theirstack.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

1 candidate account seen and rejected by the evidence rules: TheirStack. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Scrape job postings](../jobs/scrape-job-postings.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 884 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: TheirStack

- **Category**: [Data & Enrichment](../categories/data-enrichment.md)

- **MCP status there**: Official MCP

- **Gate there**: Free to start

- **Source**: 01-data-enrichment.md line 483

- **Canonical page**: [TheirStack](../tools/theirstack.md)

What that listing says it does: A job-postings and technographic-data API that tracks live job listings and the tech stack/hiring signals behind them across 195 countries (claims 223M+ jobs, 352K+ sources), queryable for GTM timing/intent signals.

16 of the 884 entries are cross listed like this. They are why the entry count is 884 and the unique product count is 868. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://theirstack.com/](https://theirstack.com/)
- [https://theirstack.com/en/pricing](https://theirstack.com/en/pricing)
- [https://theirstack.com/en/job-posting-mcp](https://theirstack.com/en/job-posting-mcp)
- [https://api.theirstack.com/mcp/](https://api.theirstack.com/mcp/)

4 source URLs. Raw sources field, verbatim:

https://theirstack.com/, https://theirstack.com/en/pricing, https://theirstack.com/en/job-posting-mcp, https://api.theirstack.com/mcp/

**Notes, verbatim from the file**
Free trial plus credit-based pricing from $49/mo (API credits) up to $5,500/mo; one-time credit packs $109-$999; a full "talk to sales" enterprise tier exists for the complete datasets. Three separate MCP servers (jobs, technographics, buying intent) rather than one unified server - see Sweep notes for MCP-of-the-Week candidacy. 2026-09-07: Same first-party endpoint as the other TheirStack entry: DNS-verified registry namespace com.theirstack, 401 invalid_token to an MCP initialize on the trailing-slash path (https://api.theirstack.com/mcp/).

**Provenance**

- **Entry id**: 05-theirstack

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 544

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
