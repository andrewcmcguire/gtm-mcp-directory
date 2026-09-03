# PhantomBuster: MCP server status, API access gate and what it does

> General browser-automation/data-extraction platform ("Phantoms") that runs cloud scripts to scrape and act on... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
PhantomBuster

# PhantomBuster

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [phantombuster.com](https://phantombuster.com) · entry id 02-phantombuster · source 02-engagement-outbound.md line 407

**What it does**
General browser-automation/data-extraction platform ("Phantoms") that runs cloud scripts to scrape and act on LinkedIn and other web platforms - widely used as a LinkedIn outbound backbone rather than a purpose-built sequencer.

**AI features, separated from automation with an AI label on it**
Vendor-stated AI add-ons: an "AI LinkedIn Message Writer" (GPT-based drafting), an "AI LinkedIn Profile Enricher" (structures scraped data), and an "AI LinkedIn Post Responder" (comment suggestions) - metered AI-credit features layered on a core scraping/automation engine that is itself not AI.

**RevOps role**
Data-extraction/scraping and light-automation backbone many other engagement tools (and Clay) sit on top of; general-purpose rather than LinkedIn-native.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - first connection redirects to PhantomBuster sign-in/authorization, then workspace selection.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server)Probed**: 2026-08-25, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://hub.phantombuster.com/docs/mcp-server (hosted at mcp.phantombuster.com); community alternative at https://github.com/globodai-group/mcp-phantombuster

- [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server)
- [https://github.com/globodai-group/mcp-phantombuster](https://github.com/globodai-group/mcp-phantombuster)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/globodai-group/mcp-phantombuster](https://github.com/globodai-group/mcp-phantombuster)

**Jobs it can do**

- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server)
- [https://lagrowthmachine.com/phantombuster-pricing/](https://lagrowthmachine.com/phantombuster-pricing/)
- [https://github.com/globodai-group/mcp-phantombuster](https://github.com/globodai-group/mcp-phantombuster)

3 source URLs. Raw sources field, verbatim:

https://hub.phantombuster.com/docs/mcp-server, https://lagrowthmachine.com/phantombuster-pricing/, https://github.com/globodai-group/mcp-phantombuster

**Notes, verbatim from the file**
Documented REST API available starting on the entry paid plan (~$56/mo Starter, 20 execution hours/mo); no enterprise-only gate found. Because it operates via scraping/headless browser automation, it sits squarely inside activity LinkedIn's User Agreement prohibits.

**Provenance**

- **Entry id**: 02-phantombuster

- **Source file**: 02-engagement-outbound.md

- **Source line**: 407

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
