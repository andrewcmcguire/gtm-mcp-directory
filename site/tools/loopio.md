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
- **Docs URL**: [https://github.com/fredericboyer/loopio-mcp](https://github.com/fredericboyer/loopio-mcp)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-02. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/fredericboyer/loopio-mcp (unofficial)

- [https://github.com/fredericboyer/loopio-mcp](https://github.com/fredericboyer/loopio-mcp)

**What this server exposes**

- **Tools named**: 16
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-12
- **Repo read**: fredericboyer/loopio-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **LOOPIO_API_BASE_PATH** No evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **LOOPIO_AUTH_NAME_CLAIM** `name` evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **LOOPIO_AUTH_NAME_HEADER** `x-ms-client-principal-name` evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **LOOPIO_AUTH_PRINCIPAL_HEADER** `x-ms-client-principal` evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **LOOPIO_AUTH_ROLES_CLAIM** `roles` evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **LOOPIO_CLIENT_ID** Yes evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **LOOPIO_CLIENT_SECRET** Yes evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **LOOPIO_HOST** No evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **LOOPIO_HTTP_ALLOWED_HOSTS** `127.0.0.1:

,localhost:` evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface - **LOOPIO_HTTP_HOST** `0.0.0.0` evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface - **LOOPIO_HTTP_PORT** `3000` evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface - **LOOPIO_MAX_RESULTS** No evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface - **LOOPIO_READ_ONLY** No evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface - **LOOPIO_SCOPES** No evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface - **LOOPIO_TRUST_PROXY_AUTH** `false` evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface - **Variable** Required evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface119 of the 380 entries that record an official or community MCP server carry a harvested tool list. The other 261 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only. Loopio does not publish pricing; third-party procurement data (Vendr, aggregating 80+ verified purchases) puts entry pricing around $20,000/yr for the Foundations tier (10 seats), with typical ACVs of $15,000-$150,000+ depending on team size - a fully sales-led, quote-only model with no self-serve path or public API-pricing page found.

**API documentation**

No documentation URL recorded.

528 of 784 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/fredericboyer/loopio-mcp](https://github.com/fredericboyer/loopio-mcp)

**On GitHub**

No GitHub organisation could be tied to loopio.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

6 candidate accounts seen and rejected by the evidence rules: fredericboyer, Loopio-EPD, Avnio, loopio-app, Loopio-AI. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Draft an RFP or questionnaire response](../jobs/draft-rfp-response.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 784 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
