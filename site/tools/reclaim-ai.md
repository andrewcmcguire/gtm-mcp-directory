# Reclaim.ai: MCP server status, API access gate and what it does

> AI calendar app that auto-schedules tasks, habits, and focus time around a user's existing meetings,... Official MCP, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
Reclaim.ai

# Reclaim.ai

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [reclaim.ai](https://reclaim.ai) · entry id 10-reclaim-ai · source 10-scheduling-routing.md line 141

**What it does**
AI calendar app that auto-schedules tasks, habits, and focus time around a user's existing meetings, dynamically defending and rebalancing the calendar as things change.

**AI features, separated from automation with an AI label on it**
Genuine, well-established optimization algorithms - focus-time defense, habit scheduling (recurring flexible blocks), meeting-conflict/priority-based rescheduling, and task auto-scheduling, Reclaim's original non-LLM engine. Homepage markets these as "AI agents that schedule work, meetings, and life - automatically," which reads as marketing framing over the same optimization engine rather than evidence of new distinct LLM decisioning; no standalone LLM feature (e.g. natural-language chat scheduling) independently confirmed.

**RevOps role**
Personal/team calendar-optimization layer for an AE or rep - auto-schedules deep-work/prep time and habits around booked meetings; not prospect-facing.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (official hosted server). A separate unofficial/community server also exists (github.com/universalamateur/reclaim-mcp-server, explicitly marked "UNOFFICIAL & UNAFFILIATED"; also github.com/jj3ny/reclaim-mcp-server) using API-key auth via app.reclaim.ai/settings/developer.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.reclaim.ai](https://mcp.reclaim.ai)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.reclaim.ai (endpoint confirmed live - returns HTTP 401 Unauthorized, i.e. a real OAuth-gated server, not dead); Reclaim's pricing page also lists "Claude/Claude Code MCP support" and "Microsoft Copilot/Copilot Cowork MCP support" as features across tiers.

- [https://mcp.reclaim.ai](https://mcp.reclaim.ai)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown for general REST API tier-gating - a developer API-key settings page exists (app.reclaim.ai/settings/developer) suggesting broad availability, but no page found states whether API access itself is free-tier-eligible. Confirmed paid-gated: webhooks are Business/Enterprise-only per reclaim.ai/pricing (not on Lite/Starter). MCP support itself is listed as included across multiple pricing tiers.

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/universalamateur/reclaim-mcp-server](https://github.com/universalamateur/reclaim-mcp-server)

**Jobs it can do**

- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://reclaim.ai](https://reclaim.ai)
- [https://reclaim.ai/pricing](https://reclaim.ai/pricing)
- [https://mcp.reclaim.ai](https://mcp.reclaim.ai)
- [https://github.com/universalamateur/reclaim-mcp-server](https://github.com/universalamateur/reclaim-mcp-server)
- [https://erikmackinnon.com/tools/reclaim-mcp/](https://erikmackinnon.com/tools/reclaim-mcp/)
- [https://reclaim.ai/blog/dropbox-acquires-reclaim](https://reclaim.ai/blog/dropbox-acquires-reclaim)
- [https://www.geekwire.com/2024/dropbox-acquires-reclaim-a-calendar-app-that-uses-ai-scheduling-to-boost-productivity/](https://www.geekwire.com/2024/dropbox-acquires-reclaim-a-calendar-app-that-uses-ai-scheduling-to-boost-productivity/)

7 source URLs. Raw sources field, verbatim:

https://reclaim.ai, https://reclaim.ai/pricing, https://mcp.reclaim.ai, https://github.com/universalamateur/reclaim-mcp-server, https://erikmackinnon.com/tools/reclaim-mcp/, https://reclaim.ai/blog/dropbox-acquires-reclaim, https://www.geekwire.com/2024/dropbox-acquires-reclaim-a-calendar-app-that-uses-ai-scheduling-to-boost-productivity/

**Notes, verbatim from the file**
Acquired by Dropbox in August 2024 (~320,000 users / 43,000+ companies at acquisition; product continues operating independently under Dropbox per founders' statements). Following Clockwise's March 2026 shutdown (see below), Reclaim has been publicly positioned - including by Clockwise itself - as the recommended migration target, making it the practical category survivor. [api_gate 2026-08-25] Re-checked and left unknown, honestly: the pricing page states Business ($15/user/mo monthly) and Enterprise get unlimited integrations plus webhooks support versus limited integrations on the free Lite tier, but no REST API or API key is documented anywhere - developer.reclaim.ai does not resolve and /developers, /docs and /api all 404. Webhooks at Business are self-serve; a documented API is not published. Checked against https://reclaim.ai/pricing.

**Provenance**

- **Entry id**: 10-reclaim-ai

- **Source file**: 10-scheduling-routing.md

- **Source line**: 141

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
