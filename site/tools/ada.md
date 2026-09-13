# Ada: MCP server status, API access gate and what it does

> Enterprise AI customer-experience platform (voice, chat, email) that automates inbound support and sales... Official MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Ada

# Ada

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [ada.cx](https://ada.cx) · entry id 14-ada · source 14-inbound-plg-chat.md line 65

**What it does**
Enterprise AI customer-experience platform (voice, chat, email) that automates inbound support and sales conversations end-to-end.

**AI features, separated from automation with an AI label on it**
Vendor claims multi-LLM orchestration, generative AI for complex resolution, and "Playbooks" for automating SOPs with agentic AI, citing an 84% automated resolution rate and 357% ROI - all vendor-stated figures, not independently verified.

**RevOps role**
Enterprise inbound AI agent platform for CX teams; notable in this category for having a real but narrow MCP server.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: none documented - connects over HTTP with no credential requirement described in the docs.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official (docs-only)

mcp_url, verbatim from the file:

https://docs.ada.cx/_mcp/server ; repo https://github.com/AdaSupport/ada-skills

- [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server)
- [https://github.com/AdaSupport/ada-skills](https://github.com/AdaSupport/ada-skills)

**What this server exposes**

- **Tools named**: 1
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **searchDocs** Search the documentation at https://docs.ada.cx. Returns relevant doc passages with source URLs. evidence: answered tools/list · calling it reads · required: query

119 of the 264 entries that record an official or community MCP server carry a harvested tool list. The other 145 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (/pricing is a demo-booking landing page with no tiers or prices; docs.ada.cx publishes a public API reference but states no plan or package requirement for access)

**API documentation**

No documentation URL recorded.

400 of 514 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/AdaSupport/ada-skills](https://github.com/AdaSupport/ada-skills)

**On GitHub**

No GitHub organisation could be tied to ada.cx with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: AdaCore, adafruit, SylphAI-Inc, adatechschool, ada-url. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 514 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.ada.cx](https://www.ada.cx)
- [https://docs.ada.cx](https://docs.ada.cx)
- [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server)
- [https://www.ada.cx/pricing/](https://www.ada.cx/pricing/)

4 source URLs. Raw sources field, verbatim:

https://www.ada.cx, https://docs.ada.cx, https://docs.ada.cx/_mcp/server, https://www.ada.cx/pricing/

**Notes, verbatim from the file**
IMPORTANT CAVEAT - Ada's MCP server exposes exactly one tool ("AI-powered search over the documentation") and only lets an AI client search Ada's own help docs; it is not an MCP for querying or acting on a customer's live Ada account data (conversations, contacts, etc.). Listed as official because the URL is real and vendor-hosted, but do not conflate this with a full product-data MCP like Intercom's or Pylon's. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.ada.cx/pricing/): /pricing is a demo-booking landing page with no tiers or prices; docs.ada.cx publishes a public API reference but states no plan or package requirement for access. 2026-09-07: https://docs.ada.cx/_mcp/server answered an MCP initialize with HTTP 200 and a jsonrpc result - a live, unauthenticated MCP server on the vendor domain (https://docs.ada.cx/_mcp/server). 2026-09-12 (P6-04 repo sweep): first-party repository recorded at https://github.com/AdaSupport/ada-skills - first-party agent skills for the Ada MCP Server, NOT the server source. Evidence: the org AdaSupport, whose GitHub profile name is Ada and whose profile site is ada.cx, the vendor domain on this entry, and whose repo description reads "Agent Skills for the Ada MCP Server".

**Provenance**

- **Entry id**: 14-ada

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 65

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
