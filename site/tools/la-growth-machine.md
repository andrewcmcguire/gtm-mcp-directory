# La Growth Machine: MCP server status, API access gate and what it does

> Multi-channel prospecting platform that sequences outreach across LinkedIn, email, Twitter/X, and voice... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
La Growth Machine

# La Growth Machine

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [lagrowthmachine.com](https://lagrowthmachine.com) · entry id 02-la-growth-machine · source 02-engagement-outbound.md line 388

**What it does**
Multi-channel prospecting platform that sequences outreach across LinkedIn, email, Twitter/X, and voice notes/calls from one campaign builder, with built-in lead enrichment.

**AI features, separated from automation with an AI label on it**
"Magic Messages" (Pro/Ultimate plans) auto-generates message copy; "AI Comment Automation" posts contextual comments on a prospect's LinkedIn activity pre-connection; the Ultimate plan adds AI-personalized voice notes. Vendor-stated LLM-generation features, not independently verified.

**RevOps role**
Multichannel (LinkedIn-centric) outbound execution + enrichment layer that can be driven conversationally via its own open-source MCP/Claude-skills bundle.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - no API key needed; first use opens a browser sign-in directly to the user's La Growth Machine account.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/LaGrowthMachine/gtm-system ; https://lagrowthmachine.com/mcp-server/

- [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system)
- [https://lagrowthmachine.com/mcp-server/](https://lagrowthmachine.com/mcp-server/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system)

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://lagrowthmachine.com/best-linkedin-automation-tools/](https://lagrowthmachine.com/best-linkedin-automation-tools/)
- [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system)
- [https://lagrowthmachine.com/mcp-server/](https://lagrowthmachine.com/mcp-server/)

3 source URLs. Raw sources field, verbatim:

https://lagrowthmachine.com/best-linkedin-automation-tools/, https://github.com/LaGrowthMachine/gtm-system, https://lagrowthmachine.com/mcp-server/

**Notes, verbatim from the file**
API, Zapier, and CRM integrations are vendor-stated as available only on upper-tier plans (base plan starts ~$70/mo/identity, which reportedly excludes API). Notably the most "agent-native" tool in this category - ships an open-source repo bundling both Claude skills and an MCP server together, more mature agent tooling than most competitors here.

**Provenance**

- **Entry id**: 02-la-growth-machine

- **Source file**: 02-engagement-outbound.md

- **Source line**: 388

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
