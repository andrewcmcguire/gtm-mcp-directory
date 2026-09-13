# Clearbit Reveal (rebranded: HubSpot Breeze Intelligence): MCP server status, API access gate and what it does

> Identifies companies visiting a website via IP-to-company matching, then enriches contact/company CRM records... No MCP found, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Clearbit Reveal (rebranded: HubSpot Breeze Intelligence)

# Clearbit Reveal (rebranded: HubSpot Breeze Intelligence)

[No MCP found](../mcp/none-found.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://clearbit.com (redirects into hubspot.com)](https://clearbit.com (redirects into hubspot.com)) · entry id 05-clearbit-reveal · source 05-signals-intent-abm.md line 356

**What it does**
Identifies companies visiting a website via IP-to-company matching, then enriches contact/company CRM records with firmographic data (employee count, revenue, tech stack, location) and surfaces buying-intent signals like pricing-page visits.

**AI features, separated from automation with an AI label on it**
No disclosed AI/ML claims found for the core identification/enrichment engine on current vendor pages - classic IP-database matching plus rules-based enrichment. HubSpot's broader "Breeze" branding implies AI, but Breeze Intelligence's own visitor-ID/enrichment mechanism is not described as AI-driven.

**RevOps role**
Visitor ID + firmographic enrichment + basic intent signal layer, now embedded inside the HubSpot CRM/Breeze ecosystem rather than sold as a standalone point solution.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 1 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

none - HubSpot has a general-purpose "HubSpot MCP Client" (docs: https://knowledge.hubspot.com/integrations/customize-breeze-agents-with-hubspot-mcp-client) letting Breeze Agents pull data from third-party connectors, but that documentation makes no mention of Breeze Intelligence/Clearbit visitor data being exposed through it.

- [https://knowledge.hubspot.com/integrations/customize-breeze-agents-with-hubspot-mcp-client](https://knowledge.hubspot.com/integrations/customize-breeze-agents-with-hubspot-mcp-client)

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/clearbit](https://github.com/clearbit) tied to the vendor by rule 3, account website https://clearbit.com has the vendor's domain, confidence strong

- **Public repositories**: 16, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-06-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [clearbit-slack](https://github.com/clearbit/clearbit-slack) | other | Clearbit enrichment data in a Slack channel | 37 | 2026-06-03 | |
| [clearbit-eslint-rules](https://github.com/clearbit/clearbit-eslint-rules) | plugin or integration | Some custom eslint rules as an eslint plugin | 0 | 2026-03-29 | |
| [team-review-action](https://github.com/clearbit/team-review-action) | infrastructure | github actions that makes sure PRs are approved by team members before merged | 0 | 2025-02-18 | |
| [check-PR-description-action](https://github.com/clearbit/check-PR-description-action) | infrastructure | github action that checks if the description is present and different from the template for the repo | 0 | 2025-02-14 | |
| [omniauth-clearbit](https://github.com/clearbit/omniauth-clearbit) | plugin or integration | OmniAuth integration for Clearbit | 1 | 2025-01-10 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 649 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://clearbit.com/](https://clearbit.com/)
- [https://www.hubspot.com/products/clearbit](https://www.hubspot.com/products/clearbit)
- [https://knowledge.hubspot.com/integrations/customize-breeze-agents-with-hubspot-mcp-client](https://knowledge.hubspot.com/integrations/customize-breeze-agents-with-hubspot-mcp-client)
- [https://knowledge.hubspot.com/account-management/understand-hubspot-credits-and-billing](https://knowledge.hubspot.com/account-management/understand-hubspot-credits-and-billing)
- [https://developers.hubspot.com/mcp](https://developers.hubspot.com/mcp)

5 source URLs. Raw sources field, verbatim:

https://clearbit.com/, https://www.hubspot.com/products/clearbit, https://knowledge.hubspot.com/integrations/customize-breeze-agents-with-hubspot-mcp-client, https://knowledge.hubspot.com/account-management/understand-hubspot-credits-and-billing, https://developers.hubspot.com/mcp

**Notes, verbatim from the file**
Clearbit is no longer sold standalone ("working hard to integrate Clearbit services into the HubSpot platform" per vendor copy); the independent Clearbit self-serve API appears discontinued post-acquisition. Breeze Intelligence runs on unified "HubSpot Credits" (migrated from Breeze Credits June 2025) purchasable self-serve, but only inside an existing HubSpot account - no independent signup path exists anymore. 2026-09-02: re-checked hubspot.com/llms.txt (no MCP mention) and developers.hubspot.com/mcp (HubSpot's MCP server at mcp.hubspot.com, OAuth 2.0); those docs make no mention of Breeze Intelligence, Clearbit, Reveal or visitor identification. No MCP server found for this product.

**Provenance**

- **Entry id**: 05-clearbit-reveal

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 356

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
