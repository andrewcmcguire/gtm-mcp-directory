# FullEnrich: MCP server status, API access gate and what it does

> A B2B contact-enrichment aggregator that runs a single lookup or bulk list through 15+ third-party data... Official MCP, Free to start. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
FullEnrich

# FullEnrich

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://fullenrich.com](https://fullenrich.com) · entry id 01-fullenrich · source 01-data-enrichment.md line 141

**What it does**
A B2B contact-enrichment aggregator that runs a single lookup or bulk list through 15+ third-party data vendors in a "waterfall" and returns the first verified work/personal email or mobile number found, charging only for hits.

**AI features, separated from automation with an AI label on it**
No meaningful AI/ML claimed beyond vendor orchestration logic; this is automation (parallel/sequential vendor waterfall + verification), not AI-based inference.

**RevOps role**
Waterfall contact enrichment step in outbound/prospecting workflows, typically sitting between a list-building tool (e.g., Sales Navigator export) and a sequencer/CRM.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth (browser sign-in to FullEnrich account; no manual API key needed)

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.fullenrich.com/mcp](https://mcp.fullenrich.com/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.fullenrich.com/mcp (setup docs: https://help.fullenrich.com/en/articles/14190120-mcp-server)

- [https://mcp.fullenrich.com/mcp](https://mcp.fullenrich.com/mcp)
- [https://help.fullenrich.com/en/articles/14190120-mcp-server](https://help.fullenrich.com/en/articles/14190120-mcp-server)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://fullenrich.com/pricing](https://fullenrich.com/pricing)
- [https://help.fullenrich.com/en/articles/14190120-mcp-server](https://help.fullenrich.com/en/articles/14190120-mcp-server)
- [https://help.fullenrich.com/en/articles/14595910-connect-fullenrich-mcp-to-claude](https://help.fullenrich.com/en/articles/14595910-connect-fullenrich-mcp-to-claude)
- [https://mcp.pipedream.com/app/fullenrich](https://mcp.pipedream.com/app/fullenrich)
- [https://coldiq.com/blog/fullenrich-pricing](https://coldiq.com/blog/fullenrich-pricing)
- [https://docs.fullenrich.com/api/v2/people/lookup/post.md](https://docs.fullenrich.com/api/v2/people/lookup/post.md)

6 source URLs. Raw sources field, verbatim:

https://fullenrich.com/pricing, https://help.fullenrich.com/en/articles/14190120-mcp-server, https://help.fullenrich.com/en/articles/14595910-connect-fullenrich-mcp-to-claude, https://mcp.pipedream.com/app/fullenrich, https://coldiq.com/blog/fullenrich-pricing, https://docs.fullenrich.com/api/v2/people/lookup/post.md

**Notes, verbatim from the file**
Free trial gives 50 credits, no credit card required, with API/MCP access included even on the free tier. Paid plan (Pro) is $55-69/mo (sources vary slightly) for ~1,000 credits/month; Enterprise is custom. Credits are charged only on verified finds (1 credit work email, 3 personal email, 10 mobile phone). The MCP server is confirmed official, built and hosted by FullEnrich itself, using OAuth rather than a static API key. 2026-09-03: vendor docs state the Look Up People endpoint (POST /people/lookup) looks up "a single person using their identifiers (professional network URL/ID, or full name combined with a company identifier)", taking person_name with company_domain or a company professional-network URL/ID, and returns social_profiles.professional_network.url with a linkedin.com/in/ example (https://docs.fullenrich.com/api/v2/people/lookup/post.md); the MCP setup page names no tools; the endpoint page says Search API pricing applies and states no unit price.

**Provenance**

- **Entry id**: 01-fullenrich

- **Source file**: 01-data-enrichment.md

- **Source line**: 141

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
