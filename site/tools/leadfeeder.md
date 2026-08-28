# Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com): MCP server status, API access gate and what it does

> Identifies companies visiting a website via IP-to-company matching, tracks page-level visit behavior, and... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)

# Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.leadfeeder.com](https://www.leadfeeder.com) · entry id 05-leadfeeder · source 05-signals-intent-abm.md line 372

**What it does**
Identifies companies visiting a website via IP-to-company matching, tracks page-level visit behavior, and surfaces intent signals plus verified contact data for those companies.

**AI features, separated from automation with an AI label on it**
Core product is visitor ID + segmentation + contact enrichment - data aggregation and rules/filters, not confirmed ML/LLM, aside from the MCP-driven natural-language query layer (which uses the connecting LLM client, not a proprietary Leadfeeder model).

**RevOps role**
Website visitor identification + intent + contact enrichment, one of the more solo-operator-friendly, well-documented MCP integrations in this category.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - user signs in with their own Leadfeeder account; vendor states "No keys pasted in."

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.leadfeeder.com/features/mcp-server/ ; docs: https://docs.leadfeeder.com/api/public/connect-your-ai-tool-370534m0

- [https://www.leadfeeder.com/features/mcp-server/](https://www.leadfeeder.com/features/mcp-server/)
- [https://docs.leadfeeder.com/api/public/connect-your-ai-tool-370534m0](https://docs.leadfeeder.com/api/public/connect-your-ai-tool-370534m0)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/ever-works/awesome-mcp-servers/blob/master/details/leadfeeder-mcp-server.md](https://github.com/ever-works/awesome-mcp-servers/blob/master/details/leadfeeder-mcp-server.md)

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.leadfeeder.com/features/mcp-server/](https://www.leadfeeder.com/features/mcp-server/)
- [https://docs.leadfeeder.com/api/public/connect-your-ai-tool-370534m0](https://docs.leadfeeder.com/api/public/connect-your-ai-tool-370534m0)
- [https://www.leadfeeder.com/pricing/](https://www.leadfeeder.com/pricing/)
- [https://mcp.pipedream.com/app/leadfeeder](https://mcp.pipedream.com/app/leadfeeder)
- [https://github.com/ever-works/awesome-mcp-servers/blob/master/details/leadfeeder-mcp-server.md](https://github.com/ever-works/awesome-mcp-servers/blob/master/details/leadfeeder-mcp-server.md)

5 source URLs. Raw sources field, verbatim:

https://www.leadfeeder.com/features/mcp-server/, https://docs.leadfeeder.com/api/public/connect-your-ai-tool-370534m0, https://www.leadfeeder.com/pricing/, https://mcp.pipedream.com/app/leadfeeder, https://github.com/ever-works/awesome-mcp-servers/blob/master/details/leadfeeder-mcp-server.md

**Notes, verbatim from the file**
Permanently free "Lite" tier exists (unlimited users, last 100 identified companies/mo, 7-day visitor history, no card). Paid: Discover from €79/mo, Activate from €369/mo, Scale from €599/mo, all self-serve with 14-day trials; only "Enterprise" requires sales contact. MCP is explicitly labeled Beta by the vendor. A third-party Pipedream-hosted connector also exists as an alternative access path.

**Provenance**

- **Entry id**: 05-leadfeeder

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 372

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
