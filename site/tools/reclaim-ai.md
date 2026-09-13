# Reclaim.ai: MCP server status, API access gate and what it does

> AI calendar app that auto-schedules tasks, habits, and focus time around a user's existing meetings,... Official MCP, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

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
CLI: reclaim-cli (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

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

- **Endpoint probe**: auth wall at every path, not proven a server
- **Endpoint URL**: [https://mcp.reclaim.ai](https://mcp.reclaim.ai)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL answered an auth challenge, but so did a path on that host which cannot exist, so the challenge proves a wall rather than a running MCP server.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.reclaim.ai (endpoint confirmed live - returns HTTP 401 Unauthorized, i.e. a real OAuth-gated server, not dead); Reclaim's pricing page also lists "Claude/Claude Code MCP support" and "Microsoft Copilot/Copilot Cowork MCP support" as features across tiers.

- [https://mcp.reclaim.ai](https://mcp.reclaim.ai)

**What this server exposes**

- **Tools named**: 6
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-12
- **Repo read**: universalamateur/reclaim-mcp-server
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **Issue** Solution evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **Method** Command evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **Profile** Tools evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **full** 40 evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **minimal** 20 evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **standard** 32 evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 337 entries that record an official or community MCP server carry a harvested tool list. The other 218 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: reclaim-cli
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
pip install reclaim-cli
```

quoted from [https://pypi.org/project/reclaim-cli/](https://pypi.org/project/reclaim-cli/) on 2026-09-12, via pypi, a third party source

Packages seen, with the version on 2026-09-12:

- [pypi: reclaim-cli 0.2.3, third party](https://pypi.org/project/reclaim-cli/)
- [pypi: reclaim-cli 0.2.3, third party](https://pypi.org/project/reclaim-cli/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown for general REST API tier-gating - a developer API-key settings page exists (app.reclaim.ai/settings/developer) suggesting broad availability, but no page found states whether API access itself is free-tier-eligible. Confirmed paid-gated: webhooks are Business/Enterprise-only per reclaim.ai/pricing (not on Lite/Starter). MCP support itself is listed as included across multiple pricing tiers.

391 of 694 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

494 of 694 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/universalamateur/reclaim-mcp-server](https://github.com/universalamateur/reclaim-mcp-server)

**On GitHub**

[github.com/reclaim-ai](https://github.com/reclaim-ai) tied to the vendor by rule 3, account website https://reclaim.ai has the vendor's domain, confidence strong

- **Public repositories**: 3, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2025-10-17

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [react-intercom-hook](https://github.com/reclaim-ai/react-intercom-hook) | other | React hook for Intercom.io | 12 | 2025-10-17 | v2.0.6 |
| [be-interview](https://github.com/reclaim-ai/be-interview) | other | Simple project for backend interview exercise | 0 | 2023-07-21 | |
| [reclaim-raycast-extension](https://github.com/reclaim-ai/reclaim-raycast-extension) | plugin or integration | | 0 | 2023-07-14 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 694 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
