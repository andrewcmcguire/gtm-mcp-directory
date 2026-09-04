# RB2B: MCP server status, API access gate and what it does

> Deanonymizes B2B website traffic by matching visitor IP/device identifiers and first/third-party data against... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
RB2B

# RB2B

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.rb2b.com](https://www.rb2b.com) · entry id 05-rb2b · source 05-signals-intent-abm.md line 159

**What it does**
Deanonymizes B2B website traffic by matching visitor IP/device identifiers and first/third-party data against a contact database to reveal the specific US-based person (name, LinkedIn, email) browsing the site, plus company-level ID globally.

**AI features, separated from automation with an AI label on it**
No AI/ML claims found - presented as identity-resolution/probabilistic data matching, not predictive scoring or LLM work. This is aggregation and matching, not AI.

**RevOps role**
Top-of-funnel intent capture, turning anonymous website traffic into named, contactable leads for SDR follow-up and Slack alerting.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://registry.npmjs.org/@rb2b/rb2b-apis-mcp](https://registry.npmjs.org/@rb2b/rb2b-apis-mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://registry.npmjs.org/@rb2b/rb2b-apis-mcp (re-verified 200 on 2026-08-28, latest 1.1.7 published 2026-04-13. The only live first-party receipt; corrected that day off a dead receipt, see notes.)

- [https://registry.npmjs.org/@rb2b/rb2b-apis-mcp](https://registry.npmjs.org/@rb2b/rb2b-apis-mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Find a work email address](../jobs/find-work-email.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.rb2b.com/](https://www.rb2b.com/)
- [https://www.rb2b.com/power-your-product](https://www.rb2b.com/power-your-product)
- [https://www.warmly.ai/p/blog/rb2b-pricing](https://www.warmly.ai/p/blog/rb2b-pricing)
- [https://salestools.club/apis/rb2b](https://salestools.club/apis/rb2b)
- [https://registry.npmjs.org/@rb2b/rb2b-apis-mcp](https://registry.npmjs.org/@rb2b/rb2b-apis-mcp)

5 source URLs. Raw sources field, verbatim:

https://www.rb2b.com/, https://www.rb2b.com/power-your-product, https://www.warmly.ai/p/blog/rb2b-pricing, https://salestools.club/apis/rb2b, https://registry.npmjs.org/@rb2b/rb2b-apis-mcp

**Notes, verbatim from the file**
2026-08-28 link-rot correction. The GitHub repo published as this entry's mcp_url until today, github.com/robbclarke/RB2B-APIs-MCP, 404d on 2026-08-27 and is gone. It is named here rather than left in the mcp_url field so the published page does not carry a link to a 404. The npm package's own homepage and repository fields still point at that dead repo. The npm package it shipped from is still live and installable. mcp_status stays official on that basis, but it is the weakest official claim in this file and needs a re-verification pass: RB2B's own docs host (docs.rb2b.com) now 302s to an /inactive path that returns 401, so there is no vendor documentation surface left to confirm against. Sources conflict on MCP status - a third-party directory (salestools.club) says "Not available," but the npm package's maintainer email (robb@retention.com) matches RB2B's parent company Retention.com, a strong signal it's founder-maintained rather than a random fork; not confirmed via RB2B's own docs site. A separate OEM/API program runs $5,000/mo base + $0.10/resolution above 50,000/mo - enterprise-leaning for that tier specifically. Person-level ID is US-only.

**Provenance**

- **Entry id**: 05-rb2b

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 159

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
