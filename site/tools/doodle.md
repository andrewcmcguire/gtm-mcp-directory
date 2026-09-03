# Doodle: MCP server status, API access gate and what it does

> General-purpose group-scheduling tool - polls for finding a time that works across many participants, sign-up... No MCP found, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
Doodle

# Doodle

[No MCP found](../mcp/none-found.md)
[Gate unknown](../gates/unknown.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [doodle.com](https://doodle.com) · entry id 10-doodle · source 10-scheduling-routing.md line 255

**What it does**
General-purpose group-scheduling tool - polls for finding a time that works across many participants, sign-up sheets, and 1:1 booking pages - used more broadly than GTM specifically (events, recruiting, ops) but present in some sales/CS booking stacks.

**AI features, separated from automation with an AI label on it**
Markets "agentic calendar orchestration" and "preference-aware scheduling" that "learns team patterns over time," but no model details, technical documentation, or independent verification were found - treat as unverified vendor marketing language layered on what is historically a poll/booking-page product.

**RevOps role**
The least GTM-native tool in this file - more useful for internal/cross-team group scheduling and events than prospect-facing sales booking; included for completeness since it surfaced during discovery.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown - a paid "Premium" tier exists alongside a free option, but specific API-access gating was not found on public pages in this pass.

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://doodle.com](https://doodle.com)
- [https://www.pulsemcp.com](https://www.pulsemcp.com)
- [https://doodle.com/en/premium/](https://doodle.com/en/premium/)
- searched "doodle" scheduling
- zero relevant results

3 source URLs. Raw sources field, verbatim:

https://doodle.com, https://www.pulsemcp.com (searched "doodle" scheduling, zero relevant results), https://doodle.com/en/premium/

**Notes, verbatim from the file**
Swiss company; SOC 2/GDPR/CCPA/HIPAA compliance claimed on its homepage. Included as a discovery item rather than a core recommendation - see Sweep notes. [api_gate 2026-08-25] Re-checked and left unknown, honestly: pricing is published (Free $0, Pro and Team per seat billed annually, Enterprise from $15,000/year) but no tier mentions API access, doodle.com/en/api returns 404, developers.doodle.com 302-redirects to the marketing homepage, and no API or Developers link exists in nav or footer. Checked against https://doodle.com/en/premium/.

**Provenance**

- **Entry id**: 10-doodle

- **Source file**: 10-scheduling-routing.md

- **Source line**: 255

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
