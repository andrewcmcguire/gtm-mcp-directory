# Loopio: MCP server status, API access gate and what it does

> RFP/RFI response-management platform with a searchable content library, AI-assisted answer drafting, and... Community MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
Loopio

# Loopio

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [loopio.com](https://loopio.com) · entry id 13-loopio · source 13-proposals-deals.md line 128

**What it does**
RFP/RFI response-management platform with a searchable content library, AI-assisted answer drafting, and collaborative proposal workflows for larger bid teams.

**AI features, separated from automation with an AI label on it**
Markets "AI RFP Software with a Competitive Edge" - AI-assisted content retrieval and drafting from the response library is the core claimed capability; independent verification of the underlying model was not found.

**RevOps role**
RFP/RFI response system of record for larger proposal teams, the incumbent Loopio competes against in this file (Responsive, Arphie) increasingly via AI-drafting speed and MCP access rather than content-library size alone.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: OAuth2 client credentials (Client ID and Secret from the Loopio admin panel) against the Loopio Data API v2, per the repo README; runs locally over stdio

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/fredericboyer/loopio-mcp](https://github.com/fredericboyer/loopio-mcp)Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-02. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/fredericboyer/loopio-mcp (unofficial)

- [https://github.com/fredericboyer/loopio-mcp](https://github.com/fredericboyer/loopio-mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only. Loopio does not publish pricing; third-party procurement data (Vendr, aggregating 80+ verified purchases) puts entry pricing around $20,000/yr for the Foundations tier (10 seats), with typical ACVs of $15,000-$150,000+ depending on team size - a fully sales-led, quote-only model with no self-serve path or public API-pricing page found.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/fredericboyer/loopio-mcp](https://github.com/fredericboyer/loopio-mcp)

**Jobs it can do**

- [Draft an RFP or questionnaire response](../jobs/draft-rfp-response.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://loopio.com/pricing/](https://loopio.com/pricing/)
- [https://www.vendr.com/marketplace/loopio](https://www.vendr.com/marketplace/loopio)
- [https://autorfp.ai/blog/loopio-pricing](https://autorfp.ai/blog/loopio-pricing)
- [https://loopio.com/](https://loopio.com/)
- [https://github.com/fredericboyer/loopio-mcp](https://github.com/fredericboyer/loopio-mcp)
- [https://lobehub.com/mcp/fredericboyer-loopio-mcp](https://lobehub.com/mcp/fredericboyer-loopio-mcp)
- [https://loopio.com/platform/integrations/](https://loopio.com/platform/integrations/)

7 source URLs. Raw sources field, verbatim:

https://loopio.com/pricing/, https://www.vendr.com/marketplace/loopio, https://autorfp.ai/blog/loopio-pricing, https://loopio.com/, https://github.com/fredericboyer/loopio-mcp, https://lobehub.com/mcp/fredericboyer-loopio-mcp, https://loopio.com/platform/integrations/

**Notes, verbatim from the file**
No MCP reference found in this research - a notable contrast to Responsive and Arphie, its two closest direct competitors in this file, both of which shipped official MCP servers. 2026-09-02: CHANGED none-found -> community (unofficial). github.com/fredericboyer/loopio-mcp is a local stdio MCP server exposing the Loopio Data API v2 to Claude Desktop and Claude Code (search, read, write and delete library entries, manage RFP projects; read-only by default with writes opt-in). Its README states: 'Unofficial. This is an independent, community-built project. It is not affiliated with, endorsed by, or supported by Loopio Inc.' A second unofficial build (matthewrbonner/loopio-mcp-ec2) is listed on LobeHub. Loopio's own loopio.com/llms.txt (404), the platform/integrations page and the MCP registry carry nothing, so no official server.

**Provenance**

- **Entry id**: 13-loopio

- **Source file**: 13-proposals-deals.md

- **Source line**: 128

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
