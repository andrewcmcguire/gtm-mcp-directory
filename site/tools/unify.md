# Unify: MCP server status, API access gate and what it does

> A hybrid signals-plus-agent platform: AI agents build targeted account/prospect lists from 40+ data sources,... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
Unify

# Unify

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.unifygtm.com](https://www.unifygtm.com) · entry id 04-unify · source 04-ai-sdr-agents.md line 106

**What it does**
A hybrid signals-plus-agent platform: AI agents build targeted account/prospect lists from 40+ data sources, write personalized outbound copy, and run multi-channel sequences triggered by intent signals ("plays").

**AI features, separated from automation with an AI label on it**
List-building from combined signals (job changes, funding, hiring, web visits, tech stack) and copywriting are AI-driven; "your agent knows your CRM, your data, and how you sell" is vendor copy for a chat-based orchestration layer, not verified as autonomous end-to-end execution.

**RevOps role**
Combined signals-intent + outbound-execution layer - overlaps with both category 4 and category 5 (signals-intent-abm) in this directory.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Auth0 browser sign-in (auth.unifygtm.com); MCP caches the session cookie (~30-day life) rather than a refresh token - no password or key ever passed to the MCP client

- **Parsed URLs**: 1 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/footcarts/unify-mcp

- [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, self-serve for the app (Free/$0, Base $20/seat/mo, Pro $60/seat/mo); "Open API + webhooks" is gated to the custom-priced Business tier only

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp)

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Build a target account list](../jobs/build-target-account-list.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.unifygtm.com](https://www.unifygtm.com)
- [https://www.unifygtm.com/pricing](https://www.unifygtm.com/pricing)
- [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp)

3 source URLs. Raw sources field, verbatim:

https://www.unifygtm.com, https://www.unifygtm.com/pricing, https://github.com/footcarts/unify-mcp

**Notes, verbatim from the file**
The MCP is an unaffiliated, community-maintained repo (0 stars, ~12 commits as of this check) - functional-looking but not vendor-backed; don't represent it as official to a reader. Official API is enterprise-gated even though the app itself is self-serve down to $0.

**Provenance**

- **Entry id**: 04-unify

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 106

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
