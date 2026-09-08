# Fiber AI: MCP server status, API access gate and what it does

> B2B search and enrichment APIs for finding companies and people by structured filters or natural language,... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

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
- **Endpoint URL**: [https://mcp.fiber.ai/mcp/v3](https://mcp.fiber.ai/mcp/v3)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-04 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.fiber.ai/mcp/v3 (vendor agent plugin: https://github.com/fiber-ai/fiber-ai-plugin; machine-readable docs: https://api.fiber.ai/llms.txt)

- [https://mcp.fiber.ai/mcp/v3](https://mcp.fiber.ai/mcp/v3)
- [https://github.com/fiber-ai/fiber-ai-plugin](https://github.com/fiber-ai/fiber-ai-plugin)
- [https://api.fiber.ai/llms.txt](https://api.fiber.ai/llms.txt)

**What this server exposes**

- **Tools named**: 3
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-08
- **Repo read**: fiber-ai/fiber-ai-plugin
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **Endpoint** URL evidence: in a README table · calling it reads

- **Persona** Who it is evidence: in a README table · calling it reads

- **Skill** Trigger phrases evidence: in a README table · calling it reads

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-08 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

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

**On GitHub**

[github.com/fiber-ai](https://github.com/fiber-ai) tied to the vendor by rule 1, account website https://fiber.ai has the vendor's domain, confidence strong

- **Public repositories**: 5, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-01

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [typescript-sdk](https://github.com/fiber-ai/typescript-sdk) | SDK | Fiber AI TypeScript SDK for Node.js, Bun, etc. | 0 | 2026-09-01 | |
| [python-sdk](https://github.com/fiber-ai/python-sdk) | SDK | Fiber AI Python SDK | 0 | 2026-09-01 | v0.0.1 |
| [open-fiber](https://github.com/fiber-ai/open-fiber) | other | Open-source sales / recruiting UI built on Fiber APIs | 2 | 2026-08-20 | |
| [fiber-ai-plugin](https://github.com/fiber-ai/fiber-ai-plugin) | plugin or integration | MCP servers, skills, hooks, and slash commands into a single installable unit | 2 | 2026-06-24 | |
| [mcp](https://github.com/fiber-ai/mcp) | MCP server | Fiber MCP server | 0 | 2026-04-28 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
