# Allegrow: MCP server status, API access gate and what it does

> B2B email verification and deliverability platform - resolves catch-all/secure-email-gateway addresses that... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Allegrow

# Allegrow

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [allegrow.co](https://allegrow.co) · entry id 09-allegrow · source 09-email-deliverability.md line 102

**What it does**
B2B email verification and deliverability platform - resolves catch-all/secure-email-gateway addresses that legacy verifiers mark "unknown," sends warm-up email to real B2B accounts, and runs hourly SPF/DKIM/DMARC checks with a "Safety Net" that auto-pauses sends to addresses likely to mark mail as spam.

**AI features, separated from automation with an AI label on it**
No AI-specific model capability confirmed in sourced pages; the differentiator (resolving catch-all/SEG addresses, hourly authentication monitoring, automatic send-pausing) is rules-based verification and monitoring logic, not disclosed as model-driven.

**RevOps role**
Email-verification-plus-deliverability layer aimed at list hygiene before and during outbound sends, with warm-up as a secondary feature rather than its primary product.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - connects through Claude's standard connector authorization flow; user logs into their Allegrow account and grants access explicitly (no manual API key copying).

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://www.allegrow.co/knowledge-base/claude-email-mcp](https://www.allegrow.co/knowledge-base/claude-email-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.allegrow.co/mcp ; https://www.allegrow.co/knowledge-base/claude-email-mcp

- [https://mcp.allegrow.co/mcp](https://mcp.allegrow.co/mcp)
- [https://www.allegrow.co/knowledge-base/claude-email-mcp](https://www.allegrow.co/knowledge-base/claude-email-mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 471 entries that record an official or community MCP server carry a harvested tool list. The other 352 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - credit-based model (one credit per unique address verified); a 14-day free trial covers up to 1,000 contacts, full pricing not published.

**API documentation**

No documentation URL recorded.

629 of 982 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to allegrow.co with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

1 candidate account seen and rejected by the evidence rules: AllegrowBiotech. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 982 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.allegrow.co/knowledge-base/claude-email-mcp](https://www.allegrow.co/knowledge-base/claude-email-mcp)
- [https://www.allegrow.co/knowledge-base/complete-guide-to-email-warm-up-tools-which-increase-sender-reputation](https://www.allegrow.co/knowledge-base/complete-guide-to-email-warm-up-tools-which-increase-sender-reputation)
- [https://emailwarmup.com/blog/email-deliverability-tools/allegrow-review/](https://emailwarmup.com/blog/email-deliverability-tools/allegrow-review/)
- [https://mcp.allegrow.co/mcp](https://mcp.allegrow.co/mcp)

4 source URLs. Raw sources field, verbatim:

https://www.allegrow.co/knowledge-base/claude-email-mcp, https://www.allegrow.co/knowledge-base/complete-guide-to-email-warm-up-tools-which-increase-sender-reputation, https://emailwarmup.com/blog/email-deliverability-tools/allegrow-review/, https://mcp.allegrow.co/mcp

**Notes, verbatim from the file**
Vendor-published on Allegrow's own domain and listed in Claude's connector directory (claude.ai/directory/allegrow) - clears this schema's bar for "official" since Allegrow built and documents it themselves. Worth noting Claude's own directory UI labels it a "community connector" (meaning it passed Anthropic's automated review but isn't Anthropic-verified) - a different axis than this schema's official/community distinction, which tracks who built the server, not who verified it. 2026-09-07: https://mcp.allegrow.co/mcp returned 401 {"error":"unauthorized"} to an MCP initialize POST, on a vendor-owned mcp. subdomain (https://mcp.allegrow.co/mcp).

**Provenance**

- **Entry id**: 09-allegrow

- **Source file**: 09-email-deliverability.md

- **Source line**: 102

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
