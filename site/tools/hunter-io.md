# Hunter.io: MCP server status, API access gate and what it does

> An email-finding and verification tool - given a name, domain, or company, it locates likely professional... Official MCP, Free to start. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Hunter.io

# Hunter.io

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [hunter.io](https://hunter.io) · entry id 01-hunter-io · source 01-data-enrichment.md line 350

**What it does**
An email-finding and verification tool - given a name, domain, or company, it locates likely professional email addresses (via domain pattern-matching and web-crawled data) and verifies deliverability; also offers bulk domain search and a separate higher-volume "Data Platform" API for larger-scale lookups.

**AI features, separated from automation with an AI label on it**
Primarily deterministic pattern-matching (common email formats per domain) plus web crawling and deliverability checks (SMTP/syntax verification) - this is data engineering, not AI/ML in any meaningful sense. Notably, Hunter does not prominently market itself as "AI-powered," which is more honest than most competitors in this category.

**RevOps role**
Email-finding/verification utility typically plugged in downstream of a contact-discovery tool (or run directly against a domain list) to fill in or validate email addresses before outreach; also used for domain-wide email-pattern discovery.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (HUNTER_API_KEY)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://hunter.io/api-documentation#mcp](https://hunter.io/api-documentation#mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://hunter.io/api-documentation#mcp (an earlier open-source repo, github.com/hunter-io/hunter-mcp, is superseded by this hosted remote MCP server)

- [https://hunter.io/api-documentation#mcp](https://hunter.io/api-documentation#mcp)

**What this server exposes**

- **Tools named**: 6
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: hunter-io/hunter-mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **create_lead** No description was recorded with the name. evidence: in the server source · calling it reads

- **domain_search** No description was recorded with the name. evidence: in the server source · calling it reads

- **email_finder** No description was recorded with the name. evidence: in the server source · calling it reads

- **email_verifier** No description was recorded with the name. evidence: in the server source · calling it reads

- **enrich_company** No description was recorded with the name. evidence: in the server source · calling it reads

- **enrich_email** No description was recorded with the name. evidence: in the server source · calling it reads

119 of the 251 entries that record an official or community MCP server carry a harvested tool list. The other 132 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

374 of 468 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/hunter-io/hunter-mcp](https://github.com/hunter-io/hunter-mcp)

**On GitHub**

[github.com/hunter-io](https://github.com/hunter-io) tied to the vendor by rule 1, account website https://hunter.io has the vendor's domain, confidence strong

- **Public repositories**: 14, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-01

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [claude-plugin](https://github.com/hunter-io/claude-plugin) | plugin or integration | Hunter plugin for Claude - find and verify professional email addresses, search contacts by domain, and enrich company... | 9 | 2026-09-01 | |
| [chatgpt-mcp](https://github.com/hunter-io/chatgpt-mcp) | MCP server | Hunter MCP server for ChatGPT - company discovery, enrichment, and lead management. | 7 | 2026-09-01 | |
| [cursor-plugin](https://github.com/hunter-io/cursor-plugin) | plugin or integration | | 0 | 2026-09-01 | |
| [geonames](https://github.com/hunter-io/geonames) | other | | 1 | 2026-09-01 | v0.2.0 |
| [baseimage-ruby](https://github.com/hunter-io/baseimage-ruby) | SDK | Base Docker image for Hunter's Rails applications | 0 | 2026-07-14 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 468 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/hunter-io/hunter-mcp](https://github.com/hunter-io/hunter-mcp)
- [https://hunter.io/pricing](https://hunter.io/pricing)
- [https://hunter.io/api](https://hunter.io/api)
- [https://fullenrich.com/content/hunter-io-pricing](https://fullenrich.com/content/hunter-io-pricing)
- [https://www.g2.com/products/hunter/pricing](https://www.g2.com/products/hunter/pricing)
- [https://hunter.io/api-documentation/v2](https://hunter.io/api-documentation/v2)

6 source URLs. Raw sources field, verbatim:

https://github.com/hunter-io/hunter-mcp, https://hunter.io/pricing, https://hunter.io/api, https://fullenrich.com/content/hunter-io-pricing, https://www.g2.com/products/hunter/pricing, https://hunter.io/api-documentation/v2

**Notes, verbatim from the file**
The Free tier ($0/mo, 25 searches + 50 verifications/month) includes API access per Hunter's own feature-comparison table, making it one of the few tools here with genuinely self-serve, no-cost API access (rate/volume-limited). Paid tiers: Starter (~$34-49/mo), Growth (~$104-149/mo), Scale (~$209-299/mo depending on annual/monthly billing), Enterprise custom. A separate higher-volume "Data Platform" API product uses credit packages starting around $6,500. 2026-09-03: vendor docs state the Email Finder endpoint "finds the most likely email address from a domain name, a first name and a last name" and its response includes linkedin_url (https://hunter.io/api-documentation/v2); no MCP tool name is stated on that page; the docs state no credit is charged if no email is found, and the pricing page states the Free plan includes 50 credits per month (https://hunter.io/pricing).

**Provenance**

- **Entry id**: 01-hunter-io

- **Source file**: 01-data-enrichment.md

- **Source line**: 350

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
