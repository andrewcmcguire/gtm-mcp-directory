# Octave: MCP server status, API access gate and what it does

> A GTM context engine that stores a company's ICP, personas, positioning, competitors, proof points, and... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Octave

# Octave

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [octavehq.com](https://octavehq.com) · entry id 06-octave · source 06-revops-infra.md line 435

**What it does**
A GTM context engine that stores a company's ICP, personas, positioning, competitors, proof points, and objections as one structured model, then serves that model to sequences, scripts, and AI agents at runtime through an API and an MCP server so every tool uses the same current messaging.

**AI features, separated from automation with an AI label on it**
Genuinely agentic in parts - an ICP Agent that revises the model from call, email, and deal data, and Managed Agents that run prospect research, qualification, and sequence drafting. Messaging Studio and Motion Builder are LLM generation grounded on the stored Context Graph rather than free generation. The distribution layer itself (resolving context at runtime and pushing updates to connected tools) is plumbing, not AI. All capability claims are vendor-stated.

**RevOps role**
The context and messaging layer underneath the rest of the stack; it does not send, dial, or route, it supplies the ICP and positioning that the tools which do those things read from at runtime.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Browser OAuth. Per the vendor's Claude Code setup doc you add the server with "claude mcp add octave-myWorkspace --transport http https://mcp.octavehq.com/mcp?ctx=YOUR_CONTEXT" then run /mcp and "Select the Octave server and authenticate via your browser." No API key header path is documented for the MCP. The separate REST API v2 uses a different scheme, an API key passed in an "Api key" header, issued from app.octavehq.com.

- **Parsed URLs**: 4 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-25 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.octavehq.com/mcp/overview (endpoint: https://mcp.octavehq.com/mcp?ctx=, HTTP transport, one connection per workspace; vendor capability page: https://www.octavehq.com/capabilities/mcp; Claude Code plugin source: https://github.com/octavehq/lfgtm)

- [https://docs.octavehq.com/mcp/overview](https://docs.octavehq.com/mcp/overview)
- [https://mcp.octavehq.com/mcp?ctx=](https://mcp.octavehq.com/mcp?ctx=)
- [https://www.octavehq.com/capabilities/mcp](https://www.octavehq.com/capabilities/mcp)
- [https://github.com/octavehq/lfgtm](https://github.com/octavehq/lfgtm)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. A Base plan exists at no cost but is capped (2 workspaces, 1 offering, limited elements, playbooks, and generation) and does not list API or MCP access. MCP, API, CLI/SDK, and the Claude Code plugin are listed under Octave Ultra, which starts at $1,500/month billed annually. Signup is self-serve with a free trial, so a solo operator can reach the product without a sales call, but not the MCP or API tier.

**API documentation**

[https://docs.octavehq.com/](https://docs.octavehq.com/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/octavehq/lfgtm](https://github.com/octavehq/lfgtm)

**Jobs it can do**

- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Retrieve sales content](../jobs/retrieve-sales-content.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://octavehq.com](https://octavehq.com)
- [https://www.octavehq.com/capabilities/mcp](https://www.octavehq.com/capabilities/mcp)
- [https://www.octavehq.com/capabilities/api](https://www.octavehq.com/capabilities/api)
- [https://www.octavehq.com/pricing](https://www.octavehq.com/pricing)
- [https://docs.octavehq.com/](https://docs.octavehq.com/)
- [https://docs.octavehq.com/mcp/overview](https://docs.octavehq.com/mcp/overview)
- [https://docs.octavehq.com/mcp/claude-code](https://docs.octavehq.com/mcp/claude-code)
- [https://docs.octavehq.com/llms.txt](https://docs.octavehq.com/llms.txt)
- [https://github.com/octavehq/lfgtm](https://github.com/octavehq/lfgtm)
- [https://learn.octavehq.com/](https://learn.octavehq.com/)
- [https://www.pulsemcp.com/servers?q=octave](https://www.pulsemcp.com/servers?q=octave)

11 source URLs. Raw sources field, verbatim:

https://octavehq.com, https://www.octavehq.com/capabilities/mcp, https://www.octavehq.com/capabilities/api, https://www.octavehq.com/pricing, https://docs.octavehq.com/, https://docs.octavehq.com/mcp/overview, https://docs.octavehq.com/mcp/claude-code, https://docs.octavehq.com/llms.txt, https://github.com/octavehq/lfgtm, https://learn.octavehq.com/, https://www.pulsemcp.com/servers?q=octave

**Notes, verbatim from the file**
Added 2026-08-25 to close a known directory gap (Octave was missing entirely). MCP docs are split across /mcp/overview, /mcp/available-tools, /mcp/claude-code, /mcp/claude-desktop, /mcp/cursor, /mcp/other-editors. The REST API v2 base is https://api.octavehq.com/api/v2/ with an OpenAPI spec at https://docs.octavehq.com/v2-api-reference/openapi.json. IMPORTANT METHOD NOTE: Octave is not listed on PulseMCP (0 results) or Glama. The server is distributed through vendor docs and the octavehq/lfgtm Claude Code plugin, not through registries, so a registry-absence check produces a false negative here. This is direct evidence that a registry-only sweep will miss official servers, and it is the reason the ongoing coverage mechanism cannot be registry diffing alone. NAME COLLISION WARNING: github.com/elevanaltd/octave-mcp and the mcpmarket.com "Octave" server are unrelated (the OCTAVE token-compression protocol and GNU Octave script execution respectively); do not cite either as this vendor's MCP. CATEGORY CALL: filed in revops-infra because Octave's own framing is that it is the layer other tools and agents read from, and the product surface backs that up (MCP server, REST API, CLI/SDK, Claude Code plugin, with the Context Graph as the artifact). It has no sender, dialer, or inbox, which rules out 02; its Managed Agents are outputs of the context model rather than a standalone AI rep with a quota, which is what 04 is for.

**Provenance**

- **Entry id**: 06-octave

- **Source file**: 06-revops-infra.md

- **Source line**: 435

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
