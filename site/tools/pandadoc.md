# PandaDoc: MCP server status, API access gate and what it does

> Document builder/e-signature platform for proposals, quotes, and contracts, with AI-assisted content... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
PandaDoc

# PandaDoc

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [pandadoc.com](https://pandadoc.com) · entry id 13-pandadoc · source 13-proposals-deals.md line 14

**What it does**
Document builder/e-signature platform for proposals, quotes, and contracts, with AI-assisted content generation and CRM-linked workflows.

**AI features, separated from automation with an AI label on it**
AI-assisted document drafting and content suggestions inside the editor; the MCP server itself is an access/automation layer (search, create-from-template, send-and-track), not a new AI capability in itself.

**RevOps role**
Proposal/quote/e-signature system of record, one of the more genuinely solo-operator-accessible tools in this category on both API and MCP access.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - remote hosted server, add the server URL to an MCP client (Claude Desktop, Claude Code, Cursor, VS Code, Gemini, etc.) and authenticate via OAuth.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server ; hosted remote server at https://mcp.pandadoc.com/v1/mcp

- [https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server)
- [https://mcp.pandadoc.com/v1/mcp](https://mcp.pandadoc.com/v1/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited). PandaDoc's Free plan now includes API access with both a sandbox and production API key at signup (60 documents/year, 5 templates, sandbox docs watermarked and limited to your own domain) - sources conflict on whether production API access requires a paid/Enterprise plan, so treat the free-tier claim as probable-but-recently-changed rather than fully certain; verify current terms before publishing.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Generate a proposal or quote](../jobs/generate-proposal-or-quote.md)
- [Send a document for signature](../jobs/send-document-for-signature.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server)
- [https://www.usecarly.com/blog/pandadoc-mcp/](https://www.usecarly.com/blog/pandadoc-mcp/)
- [https://www.pandadoc.com/blog/pandadoc-free-plan-api/](https://www.pandadoc.com/blog/pandadoc-free-plan-api/)
- [https://www.pandadoc.com/api/pricing/](https://www.pandadoc.com/api/pricing/)
- [https://www.pulsemcp.com/servers/dazanza-pandadoc](https://www.pulsemcp.com/servers/dazanza-pandadoc)

5 source URLs. Raw sources field, verbatim:

https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server, https://www.usecarly.com/blog/pandadoc-mcp/, https://www.pandadoc.com/blog/pandadoc-free-plan-api/, https://www.pandadoc.com/api/pricing/, https://www.pulsemcp.com/servers/dazanza-pandadoc

**Notes, verbatim from the file**
PulseMCP also lists a third-party community server (dazanza-pandadoc) - prefer the official hosted one (mcp.pandadoc.com) documented on PandaDoc's own developer site.

**Provenance**

- **Entry id**: 13-pandadoc

- **Source file**: 13-proposals-deals.md

- **Source line**: 14

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
