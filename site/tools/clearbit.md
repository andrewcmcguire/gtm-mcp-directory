# Clearbit (now HubSpot Breeze Intelligence): MCP server status, API access gate and what it does

> A firmographic/contact data lookup service that fills in company and contact fields (size, industry, revenue,... No MCP found, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Clearbit (now HubSpot Breeze Intelligence)

# Clearbit (now HubSpot Breeze Intelligence)

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.hubspot.com/products/breeze/intelligence](https://www.hubspot.com/products/breeze/intelligence) · entry id 01-clearbit · source 01-data-enrichment.md line 103

**What it does**
A firmographic/contact data lookup service that fills in company and contact fields (size, industry, revenue, location, social profiles, etc.) from a third-party data pool; formerly sold as a standalone API, now sold only as an add-on inside the HubSpot CRM.

**AI features, separated from automation with an AI label on it**
Marketed as an "AI" feature of HubSpot's Breeze suite, but the core function is database lookup/matching against pre-aggregated firmographic and web data (i.e., automated enrichment, not generative or predictive AI). No independent evidence of model-based inference beyond standard matching/scoring.

**RevOps role**
Contact/company record enrichment and lead scoring input inside HubSpot CRM; no longer usable as a standalone enrichment layer outside HubSpot.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: not recorded

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

The mcp_url field is empty on this entry. 344 of 834 entries are.

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

555 of 834 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/HubSpot](https://github.com/HubSpot) tied to the vendor by rule 3, account website http://product.hubspot.com/ has the vendor's domain, confidence strong

- **Public repositories**: 99, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 5 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [HubSpot-public-api-spec-collection](https://github.com/HubSpot/HubSpot-public-api-spec-collection) | API client | | 45 | 2026-09-08 | |
| [agent-cli-skills](https://github.com/HubSpot/agent-cli-skills) | CLI | | 23 | 2026-09-08 | |
| [hubspot-project-components](https://github.com/HubSpot/hubspot-project-components) | docs or examples | Provides sample components for HubSpot projects. | 25 | 2026-09-08 | 2.3.0 |
| [hubspot-cms-vscode](https://github.com/HubSpot/hubspot-cms-vscode) | plugin or integration | A HubL language extension for the Visual Studio Code IDE, allowing for :rocket: fast local HubSpot CMS Platform... | 75 | 2026-09-08 | v1.7.5 |
| [boomslang](https://github.com/HubSpot/boomslang) | other | Python, but Java | 6 | 2026-09-08 | build-cfcfca4ac2ca188e3acd2a3abe8bed21bc281917 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 834 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.lead411.com/clearbit-pricing/](https://www.lead411.com/clearbit-pricing/)
- [https://derrick-app.com/en/pricing-clearbit-2/](https://derrick-app.com/en/pricing-clearbit-2/)
- [https://www.eesel.ai/blog/how-much-is-breeze-intelligence](https://www.eesel.ai/blog/how-much-is-breeze-intelligence)
- [https://community.hubspot.com/t5/Clearbit/Breeze-Intelligence/m-p/1143555](https://community.hubspot.com/t5/Clearbit/Breeze-Intelligence/m-p/1143555)
- [https://skrapp.io/blog/clearbit/](https://skrapp.io/blog/clearbit/)
- [https://salesmotion.io/blog/clearbit-alternatives-hubspot-acquisition](https://salesmotion.io/blog/clearbit-alternatives-hubspot-acquisition)
- [https://developers.hubspot.com/mcp](https://developers.hubspot.com/mcp)

7 source URLs. Raw sources field, verbatim:

https://www.lead411.com/clearbit-pricing/, https://derrick-app.com/en/pricing-clearbit-2/, https://www.eesel.ai/blog/how-much-is-breeze-intelligence, https://community.hubspot.com/t5/Clearbit/Breeze-Intelligence/m-p/1143555, https://skrapp.io/blog/clearbit/, https://salesmotion.io/blog/clearbit-alternatives-hubspot-acquisition, https://developers.hubspot.com/mcp

**Notes, verbatim from the file**
HubSpot acquired Clearbit (completed ~Dec 2024) and folded it into "Breeze Intelligence." The standalone Clearbit Enrichment API has been deprecated/closed to new customers - there is no independent API signup anymore. Access requires a paid HubSpot subscription (min. reported cost ~$75/mo combining HubSpot Starter + credits) plus HubSpot Credits for enrichment (~$0.01/credit per multiple sources); large-scale external use requires an Enterprise HubSpot contract negotiated with sales. No phone-number enrichment. No MCP server found for either legacy Clearbit or Breeze Intelligence - only generic third-party HubSpot-CRM MCP servers (unrelated to enrichment) were found. 2026-09-02: re-checked hubspot.com/llms.txt (no MCP mention) and HubSpot's MCP docs at developers.hubspot.com/mcp (endpoint mcp.hubspot.com, OAuth 2.0); those docs describe CRM access and make no mention of Breeze Intelligence, Clearbit or enrichment, so no MCP server found for this product.

**Provenance**

- **Entry id**: 01-clearbit

- **Source file**: 01-data-enrichment.md

- **Source line**: 103

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
