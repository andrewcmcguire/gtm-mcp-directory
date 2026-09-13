# Meltwater: MCP server status, API access gate and what it does

> Media-intelligence and social-listening platform that consolidates news coverage, social conversations, and... Official MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
Meltwater

# Meltwater

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-09-02
CLI: generateJwk

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.meltwater.com](https://www.meltwater.com) · entry id 15-meltwater · source 15-community-dark-social.md line 197

**What it does**
Media-intelligence and social-listening platform that consolidates news coverage, social conversations, and AI-generated content into prioritized alerts and workflows for PR, comms, and marketing teams.

**AI features, separated from automation with an AI label on it**
Branded "Meltwater AI," including narrative-shift detection, AI-generated summaries/alerts, a "GenAI Lens" feature, and a "MIRA Studio" AI showcase - all vendor-described, with no independent verification of the underlying models found.

**RevOps role**
Enterprise PR/media-intelligence layer - the kind of incumbent the lighter-weight tools in this file (Syften, Brand24) position themselves against on price and self-serve access.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Meltwater API token today, "with OAuth 2.0 planned for later this year" per the vendor docs; access requires a Meltwater MCP package in the customer's subscription.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://developer.meltwater.com/guides/meltwater-mcp/overview/](https://developer.meltwater.com/guides/meltwater-mcp/overview/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developer.meltwater.com/guides/meltwater-mcp/overview/ (endpoint https://api.meltwater.com/v2/mcp)

- [https://developer.meltwater.com/guides/meltwater-mcp/overview/](https://developer.meltwater.com/guides/meltwater-mcp/overview/)
- [https://api.meltwater.com/v2/mcp](https://api.meltwater.com/v2/mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 264 entries that record an official or community MCP server carry a harvested tool list. The other 145 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: generateJwk
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @meltwater/jwk-converter-cli
```

quoted from [https://www.npmjs.com/package/@meltwater/jwk-converter-cli](https://www.npmjs.com/package/@meltwater/jwk-converter-cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @meltwater/jwk-converter-cli 1.0.0](https://www.npmjs.com/package/@meltwater/jwk-converter-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (inferred) - no public self-serve pricing; the site routes only to "Request a demo" / "Request Pricing."

**API documentation**

No documentation URL recorded.

400 of 514 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/danmeltwater/inception-volume-monitor](https://github.com/danmeltwater/inception-volume-monitor)
- [https://github.com/mcopelandmw/mira-api-demo](https://github.com/mcopelandmw/mira-api-demo)

**On GitHub**

[github.com/meltwater](https://github.com/meltwater) tied to the vendor by rule 3, account website https://underthehood.meltwater.com has the vendor's domain, confidence strong

- **Public repositories**: 20, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 3 of them
- **Latest push**: 2026-08-11

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [meltwater-plugins](https://github.com/meltwater/meltwater-plugins) | plugin or integration | Official Meltwater plugins for AI assistants and developer platforms. | 0 | 2026-08-11 | |
| [aws-configuration-fetcher](https://github.com/meltwater/aws-configuration-fetcher) | other | A simple system for gathering configuration from both SSM and Secrets Manager in AWS | 0 | 2026-08-03 | |
| [meltwater-api-examples](https://github.com/meltwater/meltwater-api-examples) | docs or examples | Example code for Meltwater API customers building their own solutions for PR & marketing use cases | 2 | 2026-07-14 | |
| [meltwater-killercoda](https://github.com/meltwater/meltwater-killercoda) | other | Meltwater Engineering's Public / Shared Training Center | 2 | 2026-06-26 | |
| [terraform-aws-asg-dns-handler](https://github.com/meltwater/terraform-aws-asg-dns-handler) | infrastructure | Terraform module for dynamically setting hostnames following a pattern on instances in AWS Auto Scaling Groups | 77 | 2026-06-25 | v2.1.8 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 514 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.meltwater.com](https://www.meltwater.com)
- [https://github.com/mcopelandmw/mira-api-demo](https://github.com/mcopelandmw/mira-api-demo)
- [https://github.com/danmeltwater/inception-volume-monitor](https://github.com/danmeltwater/inception-volume-monitor)
- [https://developer.meltwater.com/guides/meltwater-mcp/overview/](https://developer.meltwater.com/guides/meltwater-mcp/overview/)
- [https://developer.meltwater.com/guides/mira-api/overview/](https://developer.meltwater.com/guides/mira-api/overview/)

5 source URLs. Raw sources field, verbatim:

https://www.meltwater.com, https://github.com/mcopelandmw/mira-api-demo, https://github.com/danmeltwater/inception-volume-monitor, https://developer.meltwater.com/guides/meltwater-mcp/overview/, https://developer.meltwater.com/guides/mira-api/overview/

**Notes, verbatim from the file**
Two GitHub repos surfaced referencing Meltwater + MCP - mcopelandmw/mira-api-demo ("Mira API MCP Server Demo Guide for Meltwater Sales Teams") and danmeltwater/inception-volume-monitor (a personal API ingestion-volume monitor) - but both read as individual/internal artifacts rather than a vendor-published or customer-usable MCP server, so mcp_status is logged as none-found rather than community. Worth re-checking if Meltwater formalizes a real MCP server around its "MIRA Studio" AI product. 2026-09-02: mcp_status none-found -> official. Meltwater's developer portal now documents "Meltwater MCP" at https://api.meltwater.com/v2/mcp, authenticated with the Meltwater API token, exposing saved searches, tags, mentions, analytics and insights with tools discovered at runtime according to the products in the subscription, and states "Meltwater MCP is accessible to API customers if they have a Meltwater MCP package in their subscription." The portal also says the Mira API (the AI assistant layer) is exposed as a remote MCP server. https://www.meltwater.com/llms.txt is 404 and the official MCP registry has no entry, so this was found by web search. The two personal GitHub repos above are superseded as evidence.

**Provenance**

- **Entry id**: 15-meltwater

- **Source file**: 15-community-dark-social.md

- **Source line**: 197

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
