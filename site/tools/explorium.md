# Explorium: MCP server status, API access gate and what it does

> Aggregates roughly 50 third-party data sources into one API/platform for business and prospect lookup... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Explorium

# Explorium

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [explorium.ai](https://explorium.ai) · entry id 01-explorium · source 01-data-enrichment.md line 464

**What it does**
Aggregates roughly 50 third-party data sources into one API/platform for business and prospect lookup (firmographics, contacts, technographics, business events), claiming coverage of 150M+ companies and 800M+ contacts.

**AI features, separated from automation with an AI label on it**
Branded as "AgentSource" for AI agents - the MCP exposes self-describing tools an agent can call at runtime to decide what data it needs and chain lookups; the underlying enrichment/matching is standard multi-source aggregation, not a novel AI model.

**RevOps role**
Multi-source aggregation layer for agent-driven enrichment - an alternative to hand-building a waterfall across several point providers.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.explorium.ai/mcp/ (also listed at https://glama.ai/mcp/servers/explorium-ai/mcp-explorium)

- [https://www.explorium.ai/mcp/](https://www.explorium.ai/mcp/)
- [https://glama.ai/mcp/servers/explorium-ai/mcp-explorium](https://glama.ai/mcp/servers/explorium-ai/mcp-explorium)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (the API key is assigned automatically when a subscription package is purchased; cheapest self-serve package is Starter at $99.99 for 2,500 credits, and the $0 100-credit trial is not stated to include a key)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Detect a funding or news event](../jobs/detect-funding-or-news-event.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.explorium.ai/mcp/](https://www.explorium.ai/mcp/)
- [https://glama.ai/mcp/servers/explorium-ai/mcp-explorium](https://glama.ai/mcp/servers/explorium-ai/mcp-explorium)
- [https://www.explorium.ai/building-ai-agents/how-to-add-b2b-data-enrichment-to-a-claude-code-agent-step-by-step/](https://www.explorium.ai/building-ai-agents/how-to-add-b2b-data-enrichment-to-a-claude-code-agent-step-by-step/)
- [https://developers.explorium.ai/reference/setup/getting_your_api_key](https://developers.explorium.ai/reference/setup/getting_your_api_key)

4 source URLs. Raw sources field, verbatim:

https://www.explorium.ai/mcp/, https://glama.ai/mcp/servers/explorium-ai/mcp-explorium, https://www.explorium.ai/building-ai-agents/how-to-add-b2b-data-enrichment-to-a-claude-code-agent-step-by-step/, https://developers.explorium.ai/reference/setup/getting_your_api_key

**Notes, verbatim from the file**
Coverage-size claims (150M companies / 800M contacts) are vendor-stated and not independently verified. Vendor content implies self-serve sign-up/trial for the MCP and API, but an explicit self-serve-vs-sales-gated pricing page could not be confirmed, so api_gate is left unknown rather than guessed. [api_gate 2026-08-25] Reclassified unknown -> paid from the vendor's own page (https://developers.explorium.ai/reference/setup/getting_your_api_key): the API key is assigned automatically when a subscription package is purchased; cheapest self-serve package is Starter at $99.99 for 2,500 credits, and the $0 100-credit trial is not stated to include a key.

**Provenance**

- **Entry id**: 01-explorium

- **Source file**: 01-data-enrichment.md

- **Source line**: 464

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
