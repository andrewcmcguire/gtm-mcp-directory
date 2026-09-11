# Snitcher: MCP server status, API access gate and what it does

> Identifies anonymous website visitor companies via IP-to-company database matching, tracks on-site behavior... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Snitcher

# Snitcher

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.snitcher.com](https://www.snitcher.com) · entry id 05-snitcher · source 05-signals-intent-abm.md line 426

**What it does**
Identifies anonymous website visitor companies via IP-to-company database matching, tracks on-site behavior (pages viewed, session length, return visits) via an embedded tracking script, and surfaces "hot lead" alerts plus verified contacts.

**AI features, separated from automation with an AI label on it**
No explicit AI/ML claims found for the core detection engine - detection is deterministic IP-to-company matching plus rules-based intent/behavior scoring (e.g., pricing-page-visit alerts). Any "AI" references on the site point to customer logos, not Snitcher's own technology.

**RevOps role**
Visitor ID + real-time intent alerting (e.g., Slack ping when a target account hits the pricing page) + contact reveal, with a native MCP integration.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - vendor changelog points to docs.snitcher.com for authentication specifics, not independently confirmed.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://www.snitcher.com/changelog/point-claude-at-snitcher/](https://www.snitcher.com/changelog/point-claude-at-snitcher/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://app.snitcher.com/mcp/snitcher ; https://www.snitcher.com/changelog/point-claude-at-snitcher/

- [https://app.snitcher.com/mcp/snitcher](https://app.snitcher.com/mcp/snitcher)
- [https://www.snitcher.com/changelog/point-claude-at-snitcher/](https://www.snitcher.com/changelog/point-claude-at-snitcher/)

**What this server exposes**

- **Tools named**: 35
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-11
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **add-tag-to-organisation** Add a tag to a company (by tag name or UUID) evidence: in the vendor docs · calling it writes

- **capture-mcp-feedback** Send feedback about the MCP server, feature requests, bugs, or friction evidence: in the vendor docs · calling it writes

- **create-custom-field** Create a custom field definition on companies evidence: in the vendor docs · calling it writes

- **create-persona** Create a buyer persona with filters evidence: in the vendor docs · calling it writes

- **create-segment** Create a segment from filter groups and conditions evidence: in the vendor docs · calling it writes

- **create-tag** Create a new tag in a workspace evidence: in the vendor docs · calling it writes

- **delete-custom-field** Archive (soft-delete) a custom field. Reversible evidence: in the vendor docs · calling it writes

- **get-organisation** Full details of a company: profile, tags, segments, technologies, CRM data, and visit stats evidence: in the vendor docs · calling it reads

- **get-organisation-activities** Session-by-session activity: page views, duration, referrer, location, and visitor details evidence: in the vendor docs · calling it reads

- **get-organisation-buyer-personas** Show which buyer personas match a company, with associated contacts evidence: in the vendor docs · calling it reads

- **get-organisation-engagement** Engagement over a time period: total sessions, timeline, unique visitors evidence: in the vendor docs · calling it reads

- **get-organisation-insights** Key insights: unique visitors, pageview stats, most popular pages, and top traffic sources evidence: in the vendor docs · calling it reads

- **get-organisation-people** Contacts at a company with titles, departments, seniority, LinkedIn, and email availability evidence: in the vendor docs · calling it reads

- **get-usage** Current identification usage and credit balance against plan limits evidence: in the vendor docs · calling it reads

- **get-workspace** Get a workspace's name, URL, plan status, usage limits, and tags evidence: in the vendor docs · calling it reads

- **list-buyer-personas** List buyer personas and their filter definitions evidence: in the vendor docs · calling it reads

- **list-contacts** List people at a company with names, titles, departments, seniority, and email status evidence: in the vendor docs · calling it reads

- **list-custom-fields** List custom field definitions for companies in a workspace evidence: in the vendor docs · calling it reads

- **list-filter-options** Discover valid values for a filter attribute evidence: in the vendor docs · calling it reads

- **list-organisations** List identified companies, filtered by segment, date range, or name search evidence: in the vendor docs · calling it reads

- **list-segments** List segments with their filter definitions and matching company counts evidence: in the vendor docs · calling it reads

- **list-sessions** List visits for a company: pages viewed, duration, referrer, location evidence: in the vendor docs · calling it reads

- **list-tags** List all tags with their UUIDs, names, and colors evidence: in the vendor docs · calling it reads

- **list-tracking-scripts** List tracking scripts for a workspace with IDs, types, and active status evidence: in the vendor docs · calling it reads

- **list-workspaces** List all workspaces you have access to evidence: in the vendor docs · calling it reads

- **remove-tag-from-organisation** Remove a tag from a company evidence: in the vendor docs · calling it writes

- **reveal-contact-email** Reveal a contact's email address. Consumes 1 email reveal credit evidence: in the vendor docs · calling it reads

- **set-organisation-custom-field** Set or clear a custom field value on a company evidence: in the vendor docs · calling it writes

- **share-to-slack** Share a company to a Slack channel or user evidence: in the vendor docs · calling it reads

- **share-to-teams** Share a company to a Microsoft Teams channel evidence: in the vendor docs · calling it reads

- **sync-to-crm** Push a company to a connected CRM (HubSpot, Salesforce, Pipedrive, Zoho, Dynamics, or Attio) evidence: in the vendor docs · calling it writes

- **update-custom-field** Update a custom field's name or description evidence: in the vendor docs · calling it writes

- **update-organisation-notes** Replace the notes on a company with new text evidence: in the vendor docs · calling it writes

- **update-persona** Update a persona's name and/or filters evidence: in the vendor docs · calling it writes

- **update-segment** Replace a segment's filter definition evidence: in the vendor docs · calling it writes

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to snitcher.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

2 candidate accounts seen and rejected by the evidence rules: Snitcher, snitcher-app. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Find a work email address](../jobs/find-work-email.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.snitcher.com/](https://www.snitcher.com/)
- [https://www.snitcher.com/pricing](https://www.snitcher.com/pricing)
- [https://www.snitcher.com/changelog/point-claude-at-snitcher/](https://www.snitcher.com/changelog/point-claude-at-snitcher/)
- [https://app.snitcher.com/mcp/snitcher](https://app.snitcher.com/mcp/snitcher)

4 source URLs. Raw sources field, verbatim:

https://www.snitcher.com/, https://www.snitcher.com/pricing, https://www.snitcher.com/changelog/point-claude-at-snitcher/, https://app.snitcher.com/mcp/snitcher

**Notes, verbatim from the file**
Self-serve throughout ("Start for free"), 14-day trial, no card required. Volume-tiered pricing $49/mo (0-50 companies identified) up to $529/mo (4,001-5,000 companies); a discounted "Startup Program" requires contacting sales. Changelog dated June 26, 2026 - a recent addition, part of a broader 2026 wave of visitor-ID vendors bolting on MCP servers. 2026-09-07: Official MCP registry carries com.snitcher/snitcher (DNS-verified snitcher.com namespace) with remote https://app.snitcher.com/mcp/snitcher; that URL returned 401 to an MCP initialize (https://app.snitcher.com/mcp/snitcher).

**Provenance**

- **Entry id**: 05-snitcher

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 426

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
