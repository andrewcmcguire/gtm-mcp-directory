# Landbase: MCP server status, API access gate and what it does

> A GTM data platform that targets, qualifies, prioritizes, and enriches B2B accounts via AI agents using... No MCP found, Free to start. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
Landbase

# Landbase

[No MCP found](../mcp/none-found.md)
[Free to start](../gates/free.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.landbase.com](https://www.landbase.com) · entry id 04-landbase · source 04-ai-sdr-agents.md line 296

**What it does**
A GTM data platform that targets, qualifies, prioritizes, and enriches B2B accounts via AI agents using natural-language criteria, with continuous signal monitoring - it prepares audiences rather than writing/sending/booking itself.

**AI features, separated from automation with an AI label on it**
Natural-language account targeting and continuous re-qualification (no manual audience rebuilding) are the confirmed agentic pieces; this is a data/targeting layer, not an outreach-execution agent, despite "AI agents" framing.

**RevOps role**
Account targeting/enrichment layer that feeds an outbound execution tool (like the other entries in this category) rather than replacing one.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

The mcp_url field is empty on this entry. 17 of 293 entries are.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (free signup grants an instant API key with 1,000 credits and no credit card, plus $49 of free credits; paid credit packs start at $499/mo for 15,000 credits)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Build a target account list](../jobs/build-target-account-list.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.landbase.com](https://www.landbase.com)
- [https://www.landbase.com/pricing](https://www.landbase.com/pricing)

2 source URLs. Raw sources field, verbatim:

https://www.landbase.com, https://www.landbase.com/pricing

**Notes, verbatim from the file**
Worth a second look for the "MCP infrastructure" category (7) rather than just this one - the Claude Code/Codex CLI installer is an interesting adjacent-to-MCP integration pattern even though it isn't MCP itself. [api_gate 2026-08-25] Reclassified unknown -> free from the vendor's own page (https://www.landbase.com/pricing): free signup grants an instant API key with 1,000 credits and no credit card, plus $49 of free credits; paid credit packs start at $499/mo for 15,000 credits. 2026-09-02: re-checked. landbase.com has no llms.txt, https://www.landbase.com/docs/faq describes the landbase-cli, a Claude Code plugin with slash commands and API-key auth but no MCP server, the official MCP registry has no entry, and Landbase's own blog posts on Claude Code tooling describe CLI access rather than an MCP. none-found stands.

**Provenance**

- **Entry id**: 04-landbase

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 296

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
