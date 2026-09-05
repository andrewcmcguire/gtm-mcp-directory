# Brand24: MCP server status, API access gate and what it does

> Tracks brand/keyword mentions across social media, news, blogs, forums, podcasts, and review sites, then... Official MCP, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
Brand24

# Brand24

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://brand24.com](https://brand24.com) · entry id 15-brand24 · source 15-community-dark-social.md line 140

**What it does**
Tracks brand/keyword mentions across social media, news, blogs, forums, podcasts, and review sites, then scores sentiment and surfaces coverage spikes and influencer reach.

**AI features, separated from automation with an AI label on it**
"AI Insights" (recommendations), "AI Topics" (trend identification), "Events Detection" (spike recognition), and a newer "AI Visibility module" tracking brand representation inside AI platforms - all vendor-described; sentiment scoring itself is a long-standing, largely rules/ML-hybrid capability across this whole category, not a novel claim specific to Brand24.

**RevOps role**
Mid-market social-listening layer positioned below Brandwatch/Meltwater on price, feeding brand-mention and sentiment data into marketing/comms workflows.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth; the help article states "MCP access is available to Brand24 subscribers. The data available in MCP reflects what's in your active projects."

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://help.brand24.com/en/articles/13011375-brand24-mcp](https://help.brand24.com/en/articles/13011375-brand24-mcp)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://help.brand24.com/en/articles/13011375-brand24-mcp (endpoint https://mcp.brand24.com/v1/mcp)

- [https://help.brand24.com/en/articles/13011375-brand24-mcp](https://help.brand24.com/en/articles/13011375-brand24-mcp)
- [https://mcp.brand24.com/v1/mcp](https://mcp.brand24.com/v1/mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, and gated further - API access is a flat "extra fee" of $99 layered on top of any paid plan (Individual $199/mo up to Business $699/mo, Enterprise from $1,499/yr custom); there is no free API tier.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://brand24.com/pricing/](https://brand24.com/pricing/)
- [https://help.brand24.com/en/articles/13011375-brand24-mcp](https://help.brand24.com/en/articles/13011375-brand24-mcp)
- [https://updates.brand24.com/brand24-mcp-enhance-chatgpt-claude-or-any-other-ai-agent-with-insights-from-your-projects-329207](https://updates.brand24.com/brand24-mcp-enhance-chatgpt-claude-or-any-other-ai-agent-with-insights-from-your-projects-329207)

3 source URLs. Raw sources field, verbatim:

https://brand24.com/pricing/, https://help.brand24.com/en/articles/13011375-brand24-mcp, https://updates.brand24.com/brand24-mcp-enhance-chatgpt-claude-or-any-other-ai-agent-with-insights-from-your-projects-329207

**Notes, verbatim from the file**
Checked GitHub and PulseMCP for "brand24" - no MCP server found under either official or community listings. 2026-09-02: mcp_status none-found -> official. Brand24's own help center article "Brand24 MCP" (dated 2026-02-27) documents a remote server at https://mcp.brand24.com/v1/mcp with OAuth, for ChatGPT, Claude, Gemini or any MCP-compatible agent, returning project summaries, key events, discussion topics, influencer statistics and source insights; a changelog post and a ChatGPT app built on the same MCP corroborate it. https://brand24.com/llms.txt has no MCP mention and the official MCP registry has no brand24 entry, which is why the 2026-08-24 pass missed it. Requires a paid Brand24 subscription; api_gate unchanged.

**Provenance**

- **Entry id**: 15-brand24

- **Source file**: 15-community-dark-social.md

- **Source line**: 140

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
