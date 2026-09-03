# Centralize: MCP server status, API access gate and what it does

> A relationship-intelligence and account-mapping tool that builds org charts and buying-committee maps for a... MCP unknown, Free to start. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Centralize

# Centralize

[MCP unknown](../mcp/unknown.md)
[Free to start](../gates/free.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [usecentralize.com](https://usecentralize.com) · entry id 05-centralize · source 05-signals-intent-abm.md line 575

**What it does**
A relationship-intelligence and account-mapping tool that builds org charts and buying-committee maps for a rep's accounts automatically from their own CRM, email, calendar, and call data, then flags coverage gaps and warm paths into the account.

**AI features, separated from automation with an AI label on it**
"Centra" is described as an AI account strategist that answers questions like "who actually owns the budget" and drafts prioritised outreach; the org-chart construction itself is entity resolution and graph-building over first-party comms data rather than generative AI. All capability claims are vendor-stated and were not independently verified.

**RevOps role**
Buying-committee and relationship map over the accounts a rep already owns; it consumes first-party comms data rather than selling third-party contact data, so it complements an enrichment vendor rather than replacing one.

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: unknown - no setup documentation found.

- **Parsed URLs**: 1 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-08-25.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

none locatable. The vendor's own pricing page lists "MCP access" as a named feature of the Pro tier ($49/user/month), which is a first-party claim that an MCP exists: https://www.usecentralize.com/pricing. But no server endpoint, docs page, or setup instructions could be found this pass. usecentralize.com/mcp and usecentralize.com/docs both return HTTP 404, the homepage does not mention MCP, and PulseMCP, Glama, Smithery, mcp.so and GitHub searches returned nothing. Per SCHEMA law 1 an MCP claim requires a URL, so this is recorded as unknown with the pricing page as the evidence of the claim, not as official.

- [https://www.usecentralize.com/pricing](https://www.usecentralize.com/pricing)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (for the base product). Free tier is $0/month with 5 standard accounts, automatic org charts and account maps, LinkedIn warm-connection sync, Chrome extension, and email and calendar integrations, with no credit card required and every new signup getting 30 days of Pro. Pro is $49/user/month and is the tier that carries MCP access, Centra, AI priorities and drafted outreach, 50 standard plus 5 smart accounts, and 1,000 email plus 100 phone enrichment credits. Enterprise is custom and adds the Salesforce integration, call-recorder and sequencer integrations, SSO and MFA. NOTE: no REST API is mentioned on any tier.

**API documentation**

[(none found - no docs, developers, or api subdomain or path resolves)]((none found - no docs, developers, or api subdomain or path resolves))

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Discover warm intro paths](../jobs/discover-warm-intro-paths.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.usecentralize.com/](https://www.usecentralize.com/)
- [https://www.usecentralize.com/pricing](https://www.usecentralize.com/pricing)
- [https://www.businesswire.com/news/home/20260729724558/en/Centralize-Raises-19M-Led-by-NEA-to-Bring-Relationship-Intelligence-to-the-Core-of-Enterprise-Sales](https://www.businesswire.com/news/home/20260729724558/en/Centralize-Raises-19M-Led-by-NEA-to-Bring-Relationship-Intelligence-to-the-Core-of-Enterprise-Sales)
- [https://www.ycombinator.com/launches/LUE-centralize-ai-powered-org-charts-for-enterprise-sales](https://www.ycombinator.com/launches/LUE-centralize-ai-powered-org-charts-for-enterprise-sales)

4 source URLs. Raw sources field, verbatim:

https://www.usecentralize.com/, https://www.usecentralize.com/pricing, https://www.businesswire.com/news/home/20260729724558/en/Centralize-Raises-19M-Led-by-NEA-to-Bring-Relationship-Intelligence-to-the-Core-of-Enterprise-Sales, https://www.ycombinator.com/launches/LUE-centralize-ai-powered-org-charts-for-enterprise-sales

**Notes, verbatim from the file**
Added 2026-08-25 from a direct pointer that Centralize had just launched a self-service product. Confirmed: Businesswire, dated 2026-07-29, reports $19M led by NEA with Salesforce Ventures, Y Combinator, 20SALES, Ritual Capital and Adverb Ventures participating, announced alongside a free tier that any seller can sign up for. Named integrations: Salesforce, Slack, Gmail, Outlook, Google Calendar, Notion, Gong. SOC 2 Type 2 per the release. THE INTERESTING FACT HERE, and it is a content beat: this is the first entry in the directory where a vendor SELLS "MCP access" as a line item on a public pricing page while publishing no server URL, no docs, and no registry listing. That is the inverse of the usual failure mode (a server that exists but is undiscoverable) and it is exactly the case the two-tier honesty rule exists to handle. Re-check on the next sweep; if a server URL appears, this flips to official. CROSS-REFERENCE: The Swarm (01-data-enrichment.md) covers the same warm-path job from the opposite direction, selling a 500M-profile third-party relationship graph rather than mapping the customer's own data.

**Provenance**

- **Entry id**: 05-centralize

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 575

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
