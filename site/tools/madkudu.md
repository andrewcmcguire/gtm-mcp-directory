# MadKudu: MCP server status, API access gate and what it does

> Historically a lead-scoring/qualification product; the vendor domain now redirects to HG Insights, and... Official MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
MadKudu

# MadKudu

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.madkudu.com (redirects to https://hginsights.com)](https://www.madkudu.com (redirects to https://hginsights.com)) · entry id 04-madkudu · source 04-ai-sdr-agents.md line 277

**What it does**
Historically a lead-scoring/qualification product; the vendor domain now redirects to HG Insights, and MadKudu appears folded into HG Insights' "HG Sales Copilot" (AI-automated scoring, account research, playbooks, personalized outreach sequences, signal-based engagement) at msi.madkudu.com.

**AI features, separated from automation with an AI label on it**
Could not independently verify current-state agentic depth beyond the HG Insights marketing description found via the redirect; the original standalone MadKudu lead-scoring product no longer appears to exist as an independent entity.

**RevOps role**
Formerly a lead-scoring layer between marketing/sales handoff; now positioned inside HG Insights' broader revenue-intelligence suite.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: MadKudu API key embedded in the endpoint path; the portal states "Please contact HG Insights or your account manager if you're interested in the MadKudu API".

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min](https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min (endpoints https://mcp.madkudu.com/YOUR_API_KEY/mcp for Streamable HTTP and https://mcp.madkudu.com/YOUR_API_KEY/sse for SSE clients such as Claude)

- [https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min](https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min)
- [https://mcp.madkudu.com/YOUR_API_KEY/mcp](https://mcp.madkudu.com/YOUR_API_KEY/mcp)
- [https://mcp.madkudu.com/YOUR_API_KEY/sse](https://mcp.madkudu.com/YOUR_API_KEY/sse)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (madkudu.com/pricing 301s to hginsights.com after the HG Insights acquisition and HG publishes no prices - platform and data-fabric pricing is by data consumption, seats and credits on quote, with no self-serve purchase path)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.madkudu.com](https://www.madkudu.com)
- [https://hginsights.com](https://hginsights.com)
- [https://hginsights.com/pricing](https://hginsights.com/pricing)
- [https://developers.madkudu.com/](https://developers.madkudu.com/)
- [https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min](https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min)

5 source URLs. Raw sources field, verbatim:

https://www.madkudu.com, https://hginsights.com, https://hginsights.com/pricing, https://developers.madkudu.com/, https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min

**Notes, verbatim from the file**
SWEEP FLAG - www.madkudu.com now 301-redirects to hginsights.com, and the login link is labeled "HG Sales Copilot" at msi.madkudu.com. Strong signal of an acquisition/absorption; could not find a dedicated public announcement confirming deal terms or date in this pass. Treat MadKudu as effectively discontinued as a standalone product. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://hginsights.com/pricing): madkudu.com/pricing 301s to hginsights.com after the HG Insights acquisition and HG publishes no prices - platform and data-fabric pricing is by data consumption, seats and credits on quote, with no self-serve purchase path. 2026-09-02: mcp_status none-found -> official. https://developers.madkudu.com/ ("HG Platform API", shorthand MadAPI and MadMCP) has a MadKudu MCP section (What is MadKudu MCP, First time using MCP, Install in AI platforms in 2min, MadMCP tools, Building AI Agents powered by MadKudu) and states "MCP is a new protocol to connect to AI tools like ChatGPT, Claude, Cursor, Dust, or your own GPT agents... The MCP server translates that into API calls to MadKudu." The install page gives the mcp.madkudu.com endpoints above. The key is gated behind HG Insights sales, so api_gate stays enterprise-only. hginsights.com/llms.txt has no MCP mention; the receipt lives on the MadKudu developer subdomain, which still operates under the MadKudu name post-acquisition.

**Provenance**

- **Entry id**: 04-madkudu

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 277

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
