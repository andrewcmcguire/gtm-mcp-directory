# Claude / Anthropic MCP Connector Directory: MCP server status, API access gate and what it does

> Anthropic's own curated, in-product directory of MCP connectors that Claude users can browse and... MCP not applicable, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Claude / Anthropic MCP Connector Directory

# Claude / Anthropic MCP Connector Directory

[MCP not applicable](../mcp/n-a.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [claude.com/partners/mcp](https://claude.com/partners/mcp) · entry id 07-claude-anthropic-mcp-connector-directory · source 07-mcp-infrastructure.md line 198

**What it does**
Anthropic's own curated, in-product directory of MCP connectors that Claude users can browse and one-click-connect to, filterable by use case (sales, marketing, data, etc.) and by capability (read / read-write / interactive).

**AI features, separated from automation with an AI label on it**
none in the directory itself - it is a discovery/connection UI inside Claude, not an AI feature; the AI is Claude, using whichever connector you authorize.

**RevOps role**
The most mainstream on-ramp for a non-engineer GTM user to connect Claude directly to their stack; listed connectors during this check included CRM/sales tools (ActiveCampaign, Apollo.io, Affinity), analytics, and productivity apps, filterable by "sales" use case.

**MCP server**

- **Status bucket**: MCP not applicable

- **Auth**: Per-connector OAuth - Claude shows the requested scopes at connect time and lets the user limit or deny them; connectors are built and maintained by third-party developers against the MCP spec, with Anthropic publishing separate MCP Directory Terms and Policies for listed providers.

- **Parsed URLs**: 1 found in the mcp_url field

An MCP server is not a meaningful question for this entry. The status was established on 2026-08-24.

mcp_status, verbatim from the file:

n/a (this is Anthropic's own directory, not a single vendor's MCP)

mcp_url, verbatim from the file:

https://claude.com/connectors (redirect correction 2026-08-28: the address previously recorded here, www.claude.com/partners/mcp, 301s to claude.com/partners/mcp, which 301s again to this one; this one returns 200)

- [https://claude.com/connectors](https://claude.com/connectors)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (custom/remote connectors: Free plan is limited to one custom connector; Pro, Max, Team, and Enterprise get unlimited custom connectors - no separate paid tier just to use the directory)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Discover MCP servers](../jobs/discover-mcp-servers.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://claude.com/connectors](https://claude.com/connectors)
- [https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

2 source URLs. Raw sources field, verbatim:

https://claude.com/connectors, https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp

**Notes, verbatim from the file**
Because each connector is built and operated by its own third-party developer (not Anthropic), the trust/auth posture varies connector-by-connector - Anthropic's role here is curation and the OAuth consent screen, not custody of your credentials.

**Provenance**

- **Entry id**: 07-claude-anthropic-mcp-connector-directory

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 198

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
