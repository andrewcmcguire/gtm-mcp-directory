# Derrick: MCP server status, API access gate and what it does

> A credit-metered B2B enrichment engine sold primarily as a Google Sheets add-on, plus a REST API and a hosted... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Derrick

# Derrick

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [derrick-app.com](https://derrick-app.com) · entry id 01-derrick · source 01-data-enrichment.md line 758

**What it does**
A credit-metered B2B enrichment engine sold primarily as a Google Sheets add-on, plus a REST API and a hosted MCP server, covering email finding, mobile phone finding, LinkedIn profile lookup, company firmographics, website technology detection and the French SIRET company registry.

**AI features, separated from automation with an AI label on it**
Thin. A "Leads from a Prompt" feature turns a natural-language ICP description into rows, and the MCP server lets an assistant pick which lookup to run; the lookups themselves are multi-source deterministic API waterfalls, not model inference.

**RevOps role**
A cheap, credit-priced enrichment provider for a solo operator or small team, used either inside a spreadsheet or as one leg of a waterfall behind an agent, with unusually deep French and EU registry coverage.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key. The vendor's page states the MCP installs without credentials but every tool call needs a Derrick API key, passed as an Authorization Bearer header or entered when the client first prompts; the key is generated in the Google Sheets add-on under Settings then API access.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://app1.derrick-app.com/mcp (docs: https://derrick-app.com/mcp; the same page advertises a server card at /.well-known/mcp/server-card.json) ; repo https://github.com/DerrickAppOrg/derrick-mcp

- [https://app1.derrick-app.com/mcp](https://app1.derrick-app.com/mcp)
- [https://derrick-app.com/mcp](https://derrick-app.com/mcp)
- [https://github.com/DerrickAppOrg/derrick-mcp](https://github.com/DerrickAppOrg/derrick-mcp)

**What this server exposes**

- **Tools named**: 5
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-08
- **Repo read**: DerrickAppOrg/derrick-mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **derrick_account** No description was recorded with the name. evidence: in the server source · calling it reads

- **derrick_configure** No description was recorded with the name. evidence: in the server source · calling it reads

- **derrick_credits** No description was recorded with the name. evidence: in the server source · calling it reads

- **derrick_help** No description was recorded with the name. evidence: in the server source · calling it reads

- **derrick_upgrade** No description was recorded with the name. evidence: in the server source · calling it reads

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-08 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's MCP page states that API keys "unlock from the PLUS plan" and prices that plan at 47.5 euros per month. The same page contradicts itself twice in the surrounding copy, and both contradictions are recorded in notes rather than resolved by guesswork.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/DerrickAppOrg/derrick-mcp](https://github.com/DerrickAppOrg/derrick-mcp)

**On GitHub**

[github.com/DerrickAppOrg](https://github.com/DerrickAppOrg) tied to the vendor by rule 1, the directory already classed this repo first-party and its owner is an Organization, confidence strong

- **Public repositories**: 2, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-07-16

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [derrick-outbound-plugin](https://github.com/DerrickAppOrg/derrick-outbound-plugin) | plugin or integration | | 0 | 2026-07-16 | |
| [derrick-mcp](https://github.com/DerrickAppOrg/derrick-mcp) | MCP server | | 0 | 2026-07-12 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://derrick-app.com/mcp](https://derrick-app.com/mcp)
- [https://app1.derrick-app.com/mcp](https://app1.derrick-app.com/mcp)
- [https://derrick-app.com/](https://derrick-app.com/)
- [https://github.com/DerrickAppOrg/derrick-mcp](https://github.com/DerrickAppOrg/derrick-mcp)

4 source URLs. Raw sources field, verbatim:

https://derrick-app.com/mcp, https://app1.derrick-app.com/mcp, https://derrick-app.com/, https://github.com/DerrickAppOrg/derrick-mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://app1.derrick-app.com/mcp returned HTTP 401 with {"error":"invalid_token","error_description":"Missing Authorization header"}, confirming a live auth-gated server. DEFECT ON THE VENDOR'S OWN PAGE, recorded rather than resolved: derrick-app.com/mcp states three different things about the plan floor in three places. Its FAQ says keys "unlock from the PLUS plan (47.5 euros/mo)"; a call-to-action block earlier on the same page says "MCP access from Standard (20 euros/mo)"; and a third line renders an unsubstituted template variable, reading "API access unlocks from the ${API_UNLOCK_TIER} plan". The FAQ figure was taken as the api_gate value because it is the most specific and sits in the section that answers the question directly, but a solo operator should confirm with support before purchase. The page also publishes per-tool credit costs (find_email 5, find_phone 150, enrich_profile 1, verify_email 1, search 1 per result) and states 100 credits per month are free to start, so a phone number costs thirty times an enrichment on the same balance and an unattended agent can drain a plan quickly. 2026-09-07: GitHub org DerrickAppOrg; README "# Derrick MCP Server ... B2B data enrichment tools for any MCP-compatible AI client"; tree contains src/server.ts and src/tools.ts. npm package derrick-mcp is published by user derrick_app and points at this repo (https://github.com/DerrickAppOrg/derrick-mcp).

**Provenance**

- **Entry id**: 01-derrick

- **Source file**: 01-data-enrichment.md

- **Source line**: 758

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
