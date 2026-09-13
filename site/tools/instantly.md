# Instantly: MCP server status, API access gate and what it does

> Cold email sending platform providing mailbox infrastructure, warmup, deliverability management, sequencing,... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Instantly

# Instantly

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [instantly.ai](https://instantly.ai) · entry id 02-instantly · source 02-engagement-outbound.md line 122

**What it does**
Cold email sending platform providing mailbox infrastructure, warmup, deliverability management, sequencing, and lead sourcing.

**AI features, separated from automation with an AI label on it**
Vendor markets "AI Sales Agent," "AI Reply Agent," "AI SDR Agent," and a "Copilot / WARP Mode" that finds leads, writes copy, and builds campaigns from a prompt - genuinely LLM-generated copy/campaign assembly. Email warmup, sender rotation, and sequencing logic are plain rules-based automation despite adjacent AI marketing.

**RevOps role**
Outbound email sending, deliverability, and warmup infrastructure layer feeding sequencing data to CRM/enrichment tools upstream.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (generated in Instantly Settings > Integrations > API Keys)

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: auth wall at every path, not proven a server
- **Endpoint URL**: [https://mcp.instantly.ai/mcp](https://mcp.instantly.ai/mcp)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL answered an auth challenge, but so did a path on that host which cannot exist, so the challenge proves a wall rather than a running MCP server.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.instantly.ai/mcp ; community alternative at https://github.com/bcharleson/Instantly-MCP

- [https://mcp.instantly.ai/mcp](https://mcp.instantly.ai/mcp)
- [https://github.com/bcharleson/Instantly-MCP](https://github.com/bcharleson/Instantly-MCP)

**What this server exposes**

- **Tools named**: 1
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: bcharleson/Instantly-MCP
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **get_server_info** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 303 entries that record an official or community MCP server carry a harvested tool list. The other 184 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

449 of 604 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/bcharleson/Instantly-MCP](https://github.com/bcharleson/Instantly-MCP)

**On GitHub**

No GitHub organisation could be tied to instantly.ai with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

6 candidate accounts seen and rejected by the evidence rules: bcharleson, replit, netlify, Fission-AI, loopholelabs. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 604 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://instantly.ai/new-pages/pricing](https://instantly.ai/new-pages/pricing)
- [https://instantly.ai/blog/instantly-mcp-server-connect-your-ai-assistant-directly-to-your-cold-email-platform/](https://instantly.ai/blog/instantly-mcp-server-connect-your-ai-assistant-directly-to-your-cold-email-platform/)
- [https://github.com/bcharleson/Instantly-MCP](https://github.com/bcharleson/Instantly-MCP)
- [https://developer.instantly.ai/](https://developer.instantly.ai/)

4 source URLs. Raw sources field, verbatim:

https://instantly.ai/new-pages/pricing, https://instantly.ai/blog/instantly-mcp-server-connect-your-ai-assistant-directly-to-your-cold-email-platform/, https://github.com/bcharleson/Instantly-MCP, https://developer.instantly.ai/

**Notes, verbatim from the file**
Full API+webhook access is gated to the Hypergrowth tier ($97/mo) and above, not the base Growth plan ($37/mo). A live 401 response at mcp.instantly.ai/mcp plus a third-party writeup confirm the official remote server, alongside an older, separate community implementation.

**Provenance**

- **Entry id**: 02-instantly

- **Source file**: 02-engagement-outbound.md

- **Source line**: 122

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
