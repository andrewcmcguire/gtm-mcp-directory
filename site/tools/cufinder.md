# CUFinder: MCP server status, API access gate and what it does

> A credit-based B2B data lookup service where you feed in a company name, domain, LinkedIn URL, or person and... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
CUFinder

# CUFinder

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [cufinder.io](https://cufinder.io) · entry id 01-cufinder · source 01-data-enrichment.md line 719

**What it does**
A credit-based B2B data lookup service where you feed in a company name, domain, LinkedIn URL, or person and get back an enriched company or contact record including verified emails, through a web app or roughly 40 individual API endpoints.

**AI features, separated from automation with an AI label on it**
The weakest AI story in this sweep, and the docs are honest about it even while the homepage is not. CUFinder's own API documentation describes no AI features at all, only enrichment, verification, confidence scoring, matching and normalisation, which are classic deterministic data operations. The marketing site's "AI verification" is one classification stage in a five-stage pipeline. The genuinely AI-adjacent thing CUFinder ships is the MCP server itself, which is plumbing letting somebody else's AI call CUFinder, not AI that CUFinder built. Calling this an AI product is a stretch.

**RevOps role**
Cheap self-serve per-credit enrichment and lookup API for filling gaps in CRM records and building lists without a sales cycle.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key from the CUFinder dashboard under Account Settings then API Dashboard. Streamable HTTP transport, explicitly stated by the vendor.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.cufinder.io/mcp](https://mcp.cufinder.io/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.cufinder.io/mcp (docs: https://apidoc.cufinder.io/mcp/introduction)

- [https://mcp.cufinder.io/mcp](https://mcp.cufinder.io/mcp)
- [https://apidoc.cufinder.io/mcp/introduction](https://apidoc.cufinder.io/mcp/introduction)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://apidoc.cufinder.io/](https://apidoc.cufinder.io/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://cufinder.io/pricing](https://cufinder.io/pricing)
- [https://apidoc.cufinder.io/apis](https://apidoc.cufinder.io/apis)
- [https://apidoc.cufinder.io/mcp/introduction](https://apidoc.cufinder.io/mcp/introduction)
- [https://mcpservers.org/servers/mcpdoc-cufinder-io-introduction](https://mcpservers.org/servers/mcpdoc-cufinder-io-introduction)
- [https://apidoc.cufinder.io/apis/person-enrichment.md](https://apidoc.cufinder.io/apis/person-enrichment.md)

5 source URLs. Raw sources field, verbatim:

https://cufinder.io/pricing, https://apidoc.cufinder.io/apis, https://apidoc.cufinder.io/mcp/introduction, https://mcpservers.org/servers/mcpdoc-cufinder-io-introduction, https://apidoc.cufinder.io/apis/person-enrichment.md

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. Fully self-serve with no sales call for standard tiers. Free plan 15 credits with no card. Lite $49/mo (1,000 credits), Standard $129/mo (3,000), Pro $299/mo (10,000, marked most popular), Premium $449/mo (20,000), roughly 30% off annual, plus a custom enterprise tier that does require sales. All tiers include unlimited teammates at no per-seat cost, which is a real differentiator against Lead411's per-seat model in the same file. Credits are consumed only on successful returns. Roughly 40 endpoints: 22 company APIs, 6 contact APIs, 5 general normalisers, 1 jobs API. CAVEAT: the MCP docs say the remote server is "available on paid plans starting from Growth" but no tier called Growth exists on the current pricing page (Lite/Standard/Pro/Premium). That is stale doc naming; the safe read is that MCP needs a paid plan and probably starts at Lite $49/mo. A third-party source claims a 50-credit free tier while the vendor page says 15; trust 15. LEGACY NAME TRACE: Software Advice still profiles it under the old "Company URL Finder" listing, which is where the name came from, and the old docs host mcpdoc.cufinder.io now 301-redirects to apidoc.cufinder.io. Database size claims of 1B+ profiles and 85M companies are vendor copy, unverified. NOT VERIFIED: the REST API auth header format could not be confirmed from the docs. 2026-09-03: vendor docs state the Person Enrichment API takes full_name and company ("The person's company, domain, name, or LinkedIn URL") and returns social.linkedin_url, at "Credit usage is 10 credits per request" (https://apidoc.cufinder.io/apis/person-enrichment.md); the MCP introduction names no tools and states a free tier of 50 credits/month (https://apidoc.cufinder.io/mcp/introduction).

**Provenance**

- **Entry id**: 01-cufinder

- **Source file**: 01-data-enrichment.md

- **Source line**: 719

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
