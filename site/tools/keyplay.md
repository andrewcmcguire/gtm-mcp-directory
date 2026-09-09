# Keyplay: MCP server status, API access gate and what it does

> Builds a mathematical ICP model from a company's existing best customers, then scores and ranks a universe of... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Keyplay

# Keyplay

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://keyplay.io](https://keyplay.io) · entry id 05-keyplay · source 05-signals-intent-abm.md line 259

**What it does**
Builds a mathematical ICP model from a company's existing best customers, then scores and ranks a universe of target accounts against that model using 750+ pre-built "signals" (hiring velocity, tech stack, industry category) plus custom web-scraped signals.

**AI features, separated from automation with an AI label on it**
"AI Lookalikes" (nearest-neighbor-style account similarity scoring against the ICP model) is the closest thing to genuine ML - vendor-described, not independently verified. The bulk of the product (750+ standard signals, custom signal composition) is data aggregation and rules/scoring, not ML.

**RevOps role**
Account selection / ICP modeling and continuous re-scoring layer, sitting upstream of outbound rather than detecting real-time triggers.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth for Claude.ai and Claude Desktop, API key for Claude Code, per the vendor's docs

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.keyplay.io/en/articles/13643214-keyplay-mcp](https://docs.keyplay.io/en/articles/13643214-keyplay-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.keyplay.io/mcp ; https://docs.keyplay.io/en/articles/13643214-keyplay-mcp (endpoint https://api.keyplay.io/mcp, streamable HTTP)

- [https://api.keyplay.io/mcp](https://api.keyplay.io/mcp)
- [https://docs.keyplay.io/en/articles/13643214-keyplay-mcp](https://docs.keyplay.io/en/articles/13643214-keyplay-mcp)

**What this server exposes**

- **Tools named**: 6
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-09
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **filter_accounts** Filter and browse millions of accounts using criteria evidence: in the vendor docs · calling it reads

- **get_account_data** Get detailed enrichment data for a specific account by ID evidence: in the vendor docs · calling it reads

- **list_filter_options** Discover valid IDs for use with filter_accounts evidence: in the vendor docs · calling it reads

- **search_accounts** Look up a specific company by name, domain, or LinkedIn URL evidence: in the vendor docs · calling it reads

- **switch_customer** Set the active workspace for the current OAuth/SSO session evidence: in the vendor docs · calling it writes

- **whoami** Get current MCP authentication and customer context evidence: in the vendor docs · calling it reads

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-09. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-09 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to keyplay.io with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

3 candidate accounts seen and rejected by the evidence rules: JASPERKEYPLAY, keyplay-io, keyplayersolution. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Build a target account list](../jobs/build-target-account-list.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://keyplay.io/pricing/](https://keyplay.io/pricing/)
- [https://keyplay.io/product/](https://keyplay.io/product/)
- [https://www.salesforge.ai/directory/sales-tools/keyplay](https://www.salesforge.ai/directory/sales-tools/keyplay)
- [https://syncgtm.com/blog/keyplay-review](https://syncgtm.com/blog/keyplay-review)
- [https://docs.keyplay.io/en/articles/13643214-keyplay-mcp](https://docs.keyplay.io/en/articles/13643214-keyplay-mcp)
- [https://adamgtm.com/brand/keyplay/](https://adamgtm.com/brand/keyplay/)
- [https://api.keyplay.io/mcp](https://api.keyplay.io/mcp)

7 source URLs. Raw sources field, verbatim:

https://keyplay.io/pricing/, https://keyplay.io/product/, https://www.salesforge.ai/directory/sales-tools/keyplay, https://syncgtm.com/blog/keyplay-review, https://docs.keyplay.io/en/articles/13643214-keyplay-mcp, https://adamgtm.com/brand/keyplay/, https://api.keyplay.io/mcp

**Notes, verbatim from the file**
No MCP found on GitHub, mcp.so, glama.ai, or pulsemcp.com. A free "List Builder" tier exists (25 credits, 750+ signals, CSV export) - genuinely solo-operator-accessible at $0 - but ICP-modeling and Enrichment API access sit behind paid tiers ($18-20K/yr "Growth," custom "Scale"). Keyplay's own homepage indicates it has joined a company called Inflection ("the B2B marketing platform where agents actually execute"); this ownership transition could not be independently verified beyond Keyplay's own site copy, so flag as unconfirmed. 2026-09-02: CHANGED none-found -> official. Keyplay's own help center documents a remote MCP at https://api.keyplay.io/mcp (install: claude mcp add keyplay --transport http https://api.keyplay.io/mcp) with OAuth for Claude.ai and Claude Desktop or an API key for Claude Code. Tools documented: search_accounts, get_account_data, filter_accounts, list_filter_options, plus whoami and switch_customer; five guided prompts: analyze_customers, define_icp, concept_campaign, build_target_list, write_account_brief. The docs page does not state which plan includes it. Pointer came from adamgtm.com (run by Keyplay co-founder Adam Schoenfeld), which states it shipped February 2026 ahead of the Inflection acquisition; the acquisition is now confirmed by a merger announcement on Keyplay's own homepage. keyplay.io/llms.txt, keyplay.io/mcp and the MCP registry carry nothing, so the help-center article is the only receipt. 2026-09-07: https://api.keyplay.io/mcp returned 401 to an MCP initialize POST (https://api.keyplay.io/mcp).

**Provenance**

- **Entry id**: 05-keyplay

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 259

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-09

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
