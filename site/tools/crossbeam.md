# Crossbeam: MCP server status, API access gate and what it does

> Compares your account list against your partners' account lists to surface overlaps, partner-shared contacts,... Official MCP, Enterprise only. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Crossbeam

# Crossbeam

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [crossbeam.com](https://crossbeam.com) · entry id 05-crossbeam · source 05-signals-intent-abm.md line 601

**What it does**
Compares your account list against your partners' account lists to surface overlaps, partner-shared contacts, and warm introduction paths for co-selling.

**AI features, separated from automation with an AI label on it**
The MCP is a read-only data surface, so the AI is whatever client is attached to it. Crossbeam's own product supplies partner recommendations and ecosystem scoring rather than generative AI.

**RevOps role**
Partner and ecosystem data layer feeding account prioritisation and co-sell routing; the "who already has a relationship here" question answered from partner data rather than from a purchased contact graph.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth with Crossbeam login credentials, with a permission consent screen at connect time.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.crossbeam.com/mcp](https://mcp.crossbeam.com/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.crossbeam.com/mcp (docs: https://www.crossbeam.com/what-is-crossbeam/crossbeam-mcp)

- [https://mcp.crossbeam.com/mcp](https://mcp.crossbeam.com/mcp)
- [https://www.crossbeam.com/what-is-crossbeam/crossbeam-mcp](https://www.crossbeam.com/what-is-crossbeam/crossbeam-mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

[https://developers.crossbeam.com/](https://developers.crossbeam.com/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Discover warm intro paths](../jobs/discover-warm-intro-paths.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.crossbeam.com/what-is-crossbeam/crossbeam-mcp](https://www.crossbeam.com/what-is-crossbeam/crossbeam-mcp)
- [https://help.crossbeam.com/en/articles/12601327-crossbeam-mcp-server-limited-availability](https://help.crossbeam.com/en/articles/12601327-crossbeam-mcp-server-limited-availability)
- [https://developers.mcp.crossbeam.com/](https://developers.mcp.crossbeam.com/)
- [https://developers.crossbeam.com/](https://developers.crossbeam.com/)

4 source URLs. Raw sources field, verbatim:

https://www.crossbeam.com/what-is-crossbeam/crossbeam-mcp, https://help.crossbeam.com/en/articles/12601327-crossbeam-mcp-server-limited-availability, https://developers.mcp.crossbeam.com/, https://developers.crossbeam.com/

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. MCP is in Limited Availability and restricted to Supernode and Enterprise customers only; Free and Connector plans are explicitly excluded, which is why api_gate is enterprise-only despite Crossbeam having a free product tier. All exposed tools are read-only per vendor docs. NOT VERIFIED: what the Supernode tier costs, which matters because it is the gate on the MCP. Partner-ecosystem data is a lane this directory did not previously cover at all.

**Provenance**

- **Entry id**: 05-crossbeam

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 601

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
