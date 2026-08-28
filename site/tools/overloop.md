# Overloop: MCP server status, API access gate and what it does

> Sales engagement and lead-gen platform for finding, verifying, and contacting B2B prospects via automated... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Overloop

# Overloop

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [overloop.com](https://overloop.com) · entry id 02-overloop · source 02-engagement-outbound.md line 331

**What it does**
Sales engagement and lead-gen platform for finding, verifying, and contacting B2B prospects via automated email and LinkedIn campaigns.

**AI features, separated from automation with an AI label on it**
Vendor claims an "AI engine" that builds multichannel campaigns, analyzes a prospect's website/social profiles to write "ultra-personalized" cold emails, drafts contextual follow-ups from thread history, and personalizes LinkedIn connection requests - plausible LLM-based personalization per vendor description, not independently verified.

**RevOps role**
Multichannel outbound sequencing/lead-gen layer, now organizationally tied to Sortlist (a B2B agency-matching marketplace).

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: api key via OVERLOOP_API_KEY environment variable

- **Parsed URLs**: 1 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/sortlist/overloop-mcp

- [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp)

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

- [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp)

**Jobs it can do**

- [Find a work email address](../jobs/find-work-email.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://overloop.com/pricing](https://overloop.com/pricing)
- [https://overloop.com/](https://overloop.com/)
- [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp)

3 source URLs. Raw sources field, verbatim:

https://overloop.com/pricing, https://overloop.com/, https://github.com/sortlist/overloop-mcp

**Notes, verbatim from the file**
Formerly Prospect.io. REST API is available at the Growth tier ($99/user/mo) and above, not Starter ($69/user/mo). The only known MCP server lives under github.com/sortlist (not Overloop's own org) and carries a beta notice - consistent with signs the product now operates under Sortlist; flagged as a business-continuity consideration, not a confirmed shutdown.

**Provenance**

- **Entry id**: 02-overloop

- **Source file**: 02-engagement-outbound.md

- **Source line**: 331

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
