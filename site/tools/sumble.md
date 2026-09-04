# Sumble: MCP server status, API access gate and what it does

> Builds an account-intelligence knowledge graph by continuously scanning tens of millions of public sources... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Sumble

# Sumble

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://sumble.com](https://sumble.com) · entry id 05-sumble · source 05-signals-intent-abm.md line 469

**What it does**
Builds an account-intelligence knowledge graph by continuously scanning tens of millions of public sources (job boards, company sites, social media, regulatory filings) to map org structure, tech stack, and initiatives like cloud migrations or GenAI projects per company.

**AI features, separated from automation with an AI label on it**
Genuinely AI-driven - pairs a knowledge graph with an LLM to synthesize disparate signals into coherent account narratives, per vendor and TechCrunch coverage. Founded by Kaggle co-founders (Anthony Goldbloom, Ben Hamner), which lends some credibility, though the specifics remain vendor-described.

**RevOps role**
Account research / call-prep layer - LLM-driven account intelligence for reps prepping outbound or discovery calls.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - the MCP overview page documents one-click install from the Claude and ChatGPT app directories and a custom MCP connection for Cursor, Claude Code and Gemini CLI, but does not name the credential type on that page. Read 2026-08-28.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://docs.sumble.com/api/mcp](https://docs.sumble.com/api/mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.sumble.com/api/mcp (re-verified 200 on 2026-08-28; corrected that day off a dead receipt, see notes. Product overview at https://sumble.com/mcp)

- [https://docs.sumble.com/api/mcp](https://docs.sumble.com/api/mcp)
- [https://sumble.com/mcp](https://sumble.com/mcp)

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

- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://techcrunch.com/2025/10/22/sumble-emerges-from-stealth-with-38-5m-to-bring-ai-powered-context-to-sales-intelligence/](https://techcrunch.com/2025/10/22/sumble-emerges-from-stealth-with-38-5m-to-bring-ai-powered-context-to-sales-intelligence/)
- [https://sumble.com/](https://sumble.com/)
- [https://docs.sumble.com/api/mcp](https://docs.sumble.com/api/mcp)
- [https://sumble.com/llms.txt](https://sumble.com/llms.txt)
- [https://sumble.com/mcp](https://sumble.com/mcp)

5 source URLs. Raw sources field, verbatim:

https://techcrunch.com/2025/10/22/sumble-emerges-from-stealth-with-38-5m-to-bring-ai-powered-context-to-sales-intelligence/, https://sumble.com/, https://docs.sumble.com/api/mcp, https://sumble.com/llms.txt, https://sumble.com/mcp

**Notes, verbatim from the file**
2026-08-28 link-rot correction, and the lead paid off. The mcp_url published until today, docs.sumble.com/pages/KLH6XuEHsUssUZW6C1i4, 404d when re-checked on 2026-08-27. It is named here rather than left in the mcp_url field so the published page does not carry a link to a 404. https://sumble.com/llms.txt names the real current surface under a "For AI agents" heading, and both https://sumble.com/mcp and https://docs.sumble.com/api/mcp return 200. The server is alive and first-party, so mcp_status stays official rather than being downgraded. Emerged from stealth October 2025 with a $38.5M raise; knowledge graph covers ~2.6M companies. Self-serve 30-day free trial, no credit card required; specific paid pricing tiers not published.

**Provenance**

- **Entry id**: 05-sumble

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 469

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
