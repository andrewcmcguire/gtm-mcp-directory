# Fiber AI: MCP server status, API access gate and what it does

> B2B search and enrichment APIs for finding companies and people by structured filters or natural language,... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Fiber AI

# Fiber AI

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [fiber.ai](https://fiber.ai) · entry id 01-fiber-ai · source 01-data-enrichment.md line 599

**What it does**
B2B search and enrichment APIs for finding companies and people by structured filters or natural language, then revealing work emails and phone numbers with live LinkedIn data.

**AI features, separated from automation with an AI label on it**
Natural-language intent parsing over the search filters, plus a shipped agent plugin carrying skills and personas. The data retrieval itself is API lookup, not generation.

**RevOps role**
Prospect discovery and contact-reveal layer for agent-run outbound and recruiting list building.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth via Clerk on the v3 endpoint; x-api-key header on the v2 and legacy endpoints.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.fiber.ai/mcp/v3](https://mcp.fiber.ai/mcp/v3)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.fiber.ai/mcp/v3 (vendor agent plugin: https://github.com/fiber-ai/fiber-ai-plugin; machine-readable docs: https://api.fiber.ai/llms.txt)

- [https://mcp.fiber.ai/mcp/v3](https://mcp.fiber.ai/mcp/v3)
- [https://github.com/fiber-ai/fiber-ai-plugin](https://github.com/fiber-ai/fiber-ai-plugin)
- [https://api.fiber.ai/llms.txt](https://api.fiber.ai/llms.txt)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://api.fiber.ai/docs](https://api.fiber.ai/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/fiber-ai/fiber-ai-plugin](https://github.com/fiber-ai/fiber-ai-plugin)

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://api.fiber.ai/llms.txt](https://api.fiber.ai/llms.txt)
- [https://github.com/fiber-ai/fiber-ai-plugin](https://github.com/fiber-ai/fiber-ai-plugin)
- [https://www.fiber.ai/](https://www.fiber.ai/)
- [https://api.fiber.ai/docs](https://api.fiber.ai/docs)

4 source URLs. Raw sources field, verbatim:

https://api.fiber.ai/llms.txt, https://github.com/fiber-ai/fiber-ai-plugin, https://www.fiber.ai/, https://api.fiber.ai/docs

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. Scored official because the plugin repo sits in the fiber-ai GitHub org and the docs are served from the vendor's own api.fiber.ai host. Runs on a credits model, and notably the vendor's own agent-facing docs instruct the agent to confirm spend before any chargeable call and to run a preflight cost estimate before audience enrichment, which is the most agent-aware cost-safety design found in this directory. Y Combinator company. NOT VERIFIED: public pricing is not posted, so per-credit cost is unknown and api_gate "paid" reflects the absence of any free tier rather than a confirmed price.

**Provenance**

- **Entry id**: 01-fiber-ai

- **Source file**: 01-data-enrichment.md

- **Source line**: 599

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
