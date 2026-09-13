# SavvyCal: MCP server status, API access gate and what it does

> Prospect-facing scheduling/booking-page tool (Calendly competitor) built around letting invitees overlay... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
SavvyCal

# SavvyCal

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [savvycal.com](https://savvycal.com) · entry id 10-savvycal · source 10-scheduling-routing.md line 179

**What it does**
Prospect-facing scheduling/booking-page tool (Calendly competitor) built around letting invitees overlay their own calendar on the organizer's availability, with Collective/Round-Robin/Group team-scheduling modes.

**AI features, separated from automation with an AI label on it**
No AI features found or marketed on the vendor's public pages - this is classic rules-based calendar automation (buffers, meeting limits, time-blocking, branded booking links), not an AI product.

**RevOps role**
Same prospect-facing booking-link role as Calendly/Cal.com, positioned as a UX-differentiated alternative (calendar-overlay booking flow).

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: API key (SAVVYCAL_API_KEY env var, a personal access token from SavvyCal's Developer Settings). MIT-licensed repo, not explicitly disclaiming official/unofficial status but built by a third-party GitHub account, not SavvyCal's own org.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/arturkoter/savvycal-mcp-server

- [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server)

**What this server exposes**

- **Tools named**: 1
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: arturkoter/savvycal-mcp-server
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **savvycal_get_current_user** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 337 entries that record an official or community MCP server carry a harvested tool list. The other 218 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - SavvyCal has a genuine free tier for the product itself ("kick the tires for free"), but "API & Webhooks" appears only in the Premium tier ($17/user/mo) feature list, not Basic ($10/user/mo) - API access is gated above both the free tier and the entry paid tier.

**API documentation**

No documentation URL recorded.

494 of 694 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server)

**On GitHub**

[github.com/svycal](https://github.com/svycal) tied to the vendor by rule 3, account website https://savvycal.com has the vendor's domain, confidence strong

- **Public repositories**: 18, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-02

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [mjml-editor](https://github.com/svycal/mjml-editor) | other | A React MJML template editor | 1 | 2026-09-02 | @savvycal/mjml-editor@0.9.1 |
| [zonex](https://github.com/svycal/zonex) | other | An Elixir library for compiling enriched time zone information | 10 | 2026-09-01 | v0.7.1 |
| [appointments-js-archive](https://github.com/svycal/appointments-js-archive) | infrastructure | Scheduling infrastructure by SavvyCal | 2 | 2026-08-28 | @savvycal/appointments-react-query@2.0.1 |
| [enact](https://github.com/svycal/enact) | other | A thin, behaviour-based action layer for application write operations. | 1 | 2026-08-24 | v0.1.0 |
| [calendar](https://github.com/svycal/calendar) | other | A React calendar component | 2 | 2026-08-22 | @savvycal/calendar@0.10.2 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Read calendar availability](../jobs/read-calendar-availability.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 694 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://savvycal.com](https://savvycal.com)
- [https://savvycal.com/pricing](https://savvycal.com/pricing)
- [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server)

3 source URLs. Raw sources field, verbatim:

https://savvycal.com, https://savvycal.com/pricing, https://github.com/arturkoter/savvycal-mcp-server

**Notes, verbatim from the file**
developers.savvycal.com exists as a dedicated dev-docs section but detailed content wasn't retrievable in this research pass.

**Provenance**

- **Entry id**: 10-savvycal

- **Source file**: 10-scheduling-routing.md

- **Source line**: 179

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
