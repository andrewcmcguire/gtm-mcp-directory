# GTM Signals: MCP server status, API access gate and what it does

> Turns what public companies say about themselves into queryable buying signals, one row per dated public... Official MCP, Gate unknown. Checked 2026-09-14.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
GTM Signals

# GTM Signals

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-14

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://andrewcmcguire.com/gtmsignals/](https://andrewcmcguire.com/gtmsignals/) · entry id 05-gtm-signals · source 05-signals-intent-abm.md line 1974

**What it does**
Turns what public companies say about themselves into queryable buying signals, one row per dated public statement (earnings call, SEC filing, investor deck slide, IR statement, job posting), each carrying a verbatim quote and an https link to the source it came from, across 7,034 companies with a page each and a cross-company search index over 95,304 signals.

**AI features, separated from automation with an AI label on it**
The extraction and classification of statements into lanes (cost, expansion, headcount, leadership_change, guidance and others) is model-assisted; the search index itself is exact lowercased token match with no stemming and no synonyms, and the MCP is an interface over already-computed rows, not a new signal source. Nothing is inferred on a company's behalf and no signal is published without a resolvable source URL.

**RevOps role**
Upstream signal source. Answers "which companies just said something that matters" and "what has this company said, with the receipt", feeding account prioritisation and outreach timing rather than replacing a CRM.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key, sent as `Authorization: Bearer gtms_...`. Streamable HTTP, stateless, protocol version 2025-06-18. The descriptor at https://mcp.gtmsignals.co/.well-known/mcp.json is readable with no key and lists every tool with its input schema.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-14 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.gtmsignals.co/mcp

- [https://mcp.gtmsignals.co/mcp](https://mcp.gtmsignals.co/mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

140 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 601 are unmeasured, which is not the same as empty. Harvest last run 2026-09-26. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-26 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown - the gate is a key, issued by hand on request (email andrew@andrewcmcguire.com). There is no self-serve signup and no public page states a price, so whether that key is free or paid is recorded as unknown rather than guessed. Two of the data surfaces behind the tools need no key at all: the public company directory and the cross-company signal index.

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

[https://andrewcmcguire.com/gtmsignals/mcp/](https://andrewcmcguire.com/gtmsignals/mcp/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to andrewcmcguire.com with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://andrewcmcguire.com/gtmsignals/mcp/](https://andrewcmcguire.com/gtmsignals/mcp/)
- [https://mcp.gtmsignals.co/.well-known/mcp.json](https://mcp.gtmsignals.co/.well-known/mcp.json)
- [https://andrewcmcguire.com/gtmsignals/](https://andrewcmcguire.com/gtmsignals/)
- [https://api.gtmsignals.co/v1/enrich/openapi.json](https://api.gtmsignals.co/v1/enrich/openapi.json)
- [https://s3.us-east-2.amazonaws.com/navan.andrewcmcguire.com/app/company/index.json](https://s3.us-east-2.amazonaws.com/navan.andrewcmcguire.com/app/company/index.json)

5 source URLs. Raw sources field, verbatim:

https://andrewcmcguire.com/gtmsignals/mcp/, https://mcp.gtmsignals.co/.well-known/mcp.json, https://andrewcmcguire.com/gtmsignals/, https://api.gtmsignals.co/v1/enrich/openapi.json, https://s3.us-east-2.amazonaws.com/navan.andrewcmcguire.com/app/company/index.json

**Notes, verbatim from the file**
| DISCLOSURE: this is the directory owner's own product. It is listed under the same rules as every other entry, RESEARCHED tier, no ranking and no comparison, and every claim carries a public URL. 20 tools on an ordinary key, read from the descriptor on 2026-09-14. Four public-directory tools, no board needed and the same answer for every key: find_companies, get_company, company_why_now, company_signals. Two cross-company search tools on the same public index: search_company_signals, list_lanes. The rest are scoped to the calling key's own account board: resolve_entity, get_account, get_signals, whats_changed, whats_new, upcoming_calls, upcoming_calendar, next_earnings_call, get_actions, get_contacts, get_priorities, search_signals, plus research_company and search_content which are neither board scoped nor public directory. A private-company lane of four further tools is listed only for keys that own it. A REST API exists at https://api.gtmsignals.co with the same bearer key. Only /v1/enrich publishes a machine-readable spec; the other routes are documented in prose on the docs page above. /v1/ask was out of service on 2026-09-14. A status page is documented at https://andrewcmcguire.com/gtmsignals/status/ and returned 404 when this entry was written on 2026-09-14, so it is recorded here as documented, not as live. 2026-09-14 (Andrew): vendor_url points at the apex home because the product's original domain now redirects there; the MCP endpoint stays on mcp.gtmsignals.co.

**Provenance**

- **Entry id**: 05-gtm-signals

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 1974

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-14

- **Data baked**: 2026-09-26

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
