# Waalaxy: MCP server status, API access gate and what it does

> Chrome-extension-based LinkedIn (+ email) prospecting tool that automates invitations, messages, and... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Waalaxy

# Waalaxy

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [waalaxy.com](https://waalaxy.com) · entry id 02-waalaxy · source 02-engagement-outbound.md line 426

**What it does**
Chrome-extension-based LinkedIn (+ email) prospecting tool that automates invitations, messages, and multi-step campaigns, with a built-in prospect finder.

**AI features, separated from automation with an AI label on it**
"AI Prospect Finder" finds ideal-client prospects without manual search building, and GPT-powered "AI message writing" drafts/optimizes outreach copy - both vendor-described LLM-generation features, not independently verified.

**RevOps role**
Entry-to-mid-tier LinkedIn+email outbound tool used mostly by individual operators/small teams; MCP access is plan-gated above the entry tier.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: user-based OAuth 2.1 via magic-link sign-in; vendor docs explicitly state bearer API keys are NOT supported by the MCP server (differs from the separate REST API).

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.waalaxy.com/mcp-server](https://docs.waalaxy.com/mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.waalaxy.com/mcp-server ; community/workaround alternative at https://github.com/globodai-group/mcp-server-waalaxy

- [https://docs.waalaxy.com/mcp-server](https://docs.waalaxy.com/mcp-server)
- [https://github.com/globodai-group/mcp-server-waalaxy](https://github.com/globodai-group/mcp-server-waalaxy)

**What this server exposes**

- **Tools named**: 6
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-11
- **Repo read**: globodai-group/mcp-server-waalaxy
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **close_session** Close browser session and clean up resources evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_analytics** Get account analytics and statistics evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_campaign_stats** Get statistics for a specific campaign evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_campaigns** Get all campaigns from Waalaxy evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_conversations** Get LinkedIn conversations from Waalaxy inbox evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_prospects** Get prospects from a campaign or list evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

120 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 105 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

328 of 374 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/globodai-group/mcp-server-waalaxy](https://github.com/globodai-group/mcp-server-waalaxy)

**On GitHub**

No GitHub organisation could be tied to waalaxy.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

1 candidate account seen and rejected by the evidence rules: globodai-group. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 374 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://docs.waalaxy.com/mcp-server](https://docs.waalaxy.com/mcp-server)
- [https://coldiq.com/tools/waalaxy](https://coldiq.com/tools/waalaxy)
- [https://github.com/globodai-group/mcp-server-waalaxy](https://github.com/globodai-group/mcp-server-waalaxy)

3 source URLs. Raw sources field, verbatim:

https://docs.waalaxy.com/mcp-server, https://coldiq.com/tools/waalaxy, https://github.com/globodai-group/mcp-server-waalaxy

**Notes, verbatim from the file**
MCP server access is restricted to the Advanced and Business plans, not the entry Pro plan. A third party built a Playwright-based unofficial MCP that logs into the Waalaxy web UI instead, specifically to work around that plan gate - a useful illustration of how a plan-gated official MCP spawns scraping-based workarounds. As a browser-extension tool automating invites/messages, it falls under LinkedIn's prohibited "bots/browser plugins" language.

**Provenance**

- **Entry id**: 02-waalaxy

- **Source file**: 02-engagement-outbound.md

- **Source line**: 426

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
