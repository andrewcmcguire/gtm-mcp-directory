# Arphie: MCP server status, API access gate and what it does

> AI-native RFP/RFx/security-questionnaire response software, positioned as a faster-drafting... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
Arphie

# Arphie

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [arphie.ai](https://arphie.ai) · entry id 13-arphie · source 13-proposals-deals.md line 204

**What it does**
AI-native RFP/RFx/security-questionnaire response software, positioned as a faster-drafting alternative/competitor to Loopio and Responsive.

**AI features, separated from automation with an AI label on it**
Core product is explicitly AI-drafting-first (auto-answering RFP/questionnaire content from a knowledge base) - the category's newer, "AI-native" entrant rather than an established platform with AI bolted on; depth of the underlying model not independently verified.

**RevOps role**
AI-native RFP response layer, direct competitor to Loopio and Responsive, differentiated mainly on drafting speed and a transparently usage-priced MCP tier.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown

- **Parsed URLs**: 0 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

referenced via pricing/product pages describing an "Arphie MCP" plan; no distinct standalone MCP docs URL or GitHub repo was independently located beyond the pricing mention - treat with the same caution as DealHub's entry above, logged as official on the strength of a specific named, priced product line rather than a confirmed public technical spec.

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, usage-based for MCP specifically. Core RFP platform uses "concurrent project-based" custom pricing (charges scale with how many RFPs/questionnaires are active at once, not per-seat) with no published rate card. The MCP plan specifically is priced at $50/month plus $0.05 per answered question - notably the same $50/mo base as Responsive's MCP pricing, suggesting a shared MCP-hosting/billing pattern across RFP vendors worth investigating further.

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/Arphie-AI](https://github.com/Arphie-AI) tied to the vendor by rule 3, account website arphie.ai has the vendor's domain, confidence strong

- **Public repositories**: 0, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: not recorded

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Draft an RFP or questionnaire response](../jobs/draft-rfp-response.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 649 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.arphie.ai/](https://www.arphie.ai/)
- [https://autorfp.ai/blog/arphie-pricing](https://autorfp.ai/blog/arphie-pricing)
- [https://www.arphie.ai/blog/best-ai-tools-rfx-response-automation-software](https://www.arphie.ai/blog/best-ai-tools-rfx-response-automation-software)

3 source URLs. Raw sources field, verbatim:

https://www.arphie.ai/, https://autorfp.ai/blog/arphie-pricing, https://www.arphie.ai/blog/best-ai-tools-rfx-response-automation-software

**Notes, verbatim from the file**
FLAG: the "$50/mo + per-answer usage" MCP pricing pattern appearing identically at both Responsive and Arphie (two direct competitors) is worth a dedicated follow-up - either a coincidence, a category-wide pricing convention, or both vendors reselling the same underlying MCP-hosting infrastructure. 2026-09-07: LAW 1 FLAG, NOT DOWNGRADED. A repo finder searched GitHub ("Arphie mcp", owners arphie and arphie-ai), npm, PyPI and the official MCP registry and found nothing, and probes of https://mcp.arphie.ai/ and https://mcp.arphie.ai/mcp did not answer an MCP initialize. What the official claim actually rests on: a pricing-tier mention on the vendor site, with no standalone MCP docs page - the finder called it the weakest official claim in the set. A human should decide whether it survives law 1. 2026-09-12 (P6-04 repo sweep): LAW 1 FLAG RE-CHECKED, STILL STANDS, STATUS DELIBERATELY NOT CHANGED because that decision was already handed to a human. Measured today: the vendor's own GitHub org is Arphie-AI, first-party on profile-site evidence (its profile site is arphie.ai), and it has 0 public repositories. The official MCP registry returns 0 servers for the search "arphie". A GitHub repository search for "arphie" returns only third-party work (xinxuxin/arphie, api-evangelist/arphie, heywood-dev/arphie-customer-health and similar), none of it Arphie's own. So there is still no URL of any kind behind this official claim, and this remains the only entry in the directory carrying official with nothing parseable in mcp_url. Under SCHEMA law 1 that reads unknown rather than official, and the change is a human's to make, not this pass's.

**Provenance**

- **Entry id**: 13-arphie

- **Source file**: 13-proposals-deals.md

- **Source line**: 204

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
