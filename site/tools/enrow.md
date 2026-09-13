# Enrow: MCP server status, API access gate and what it does

> Finds and verifies work email addresses and direct phone numbers from a name plus company domain or a... Official MCP, Free to start. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Enrow

# Enrow

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [enrow.io](https://enrow.io) · entry id 01-enrow · source 01-data-enrichment.md line 659

**What it does**
Finds and verifies work email addresses and direct phone numbers from a name plus company domain or a LinkedIn URL, charging only when it returns a verified result.

**AI features, separated from automation with an AI label on it**
Essentially none, and to Enrow's credit they mostly do not claim otherwise; their own API page carries no AI claims at all. The mechanism is pattern generation plus SMTP and catch-all verification plus waterfall sourcing, which is deterministic infrastructure. Catch-all verification infers deliverability where SMTP gives no answer, which is usually statistical heuristics rather than a model. Third-party directory listings describe "cutting-edge artificial intelligence", but that is aggregator copy, not vendor copy. The genuinely modern thing here is the MCP server, which is distribution, not intelligence.

**RevOps role**
Cheap pay-per-result waterfall endpoint for email and phone discovery, dropped into enrichment pipelines or agent workflows where you want per-record cost rather than a seat licence.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key. ENROW_API_KEY env var for stdio, or an Authorization Bearer / x-enrow-api-key header for remote HTTP.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/EnrowAPI/enrow-mcp](https://github.com/EnrowAPI/enrow-mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/EnrowAPI/enrow-mcp (npm @enrow/mcp; listing: https://www.pulsemcp.com/servers?q=enrow)

- [https://github.com/EnrowAPI/enrow-mcp](https://github.com/EnrowAPI/enrow-mcp)
- [https://www.pulsemcp.com/servers?q=enrow](https://www.pulsemcp.com/servers?q=enrow)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 437 entries that record an official or community MCP server carry a harvested tool list. The other 318 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

[https://docs.enrow.io/](https://docs.enrow.io/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/EnrowAPI/enrow-mcp](https://github.com/EnrowAPI/enrow-mcp)

**On GitHub**

[github.com/EnrowAPI](https://github.com/EnrowAPI) tied to the vendor by rule 1, account website enrow.io has the vendor's domain, confidence strong

- **Public repositories**: 41, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-07-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [enrow-mcp](https://github.com/EnrowAPI/enrow-mcp) | MCP server | MCP server for the Enrow API - use email finder, verifier, and phone finder from any AI assistant | 1 | 2026-07-08 | |
| [phone-finder-swift](https://github.com/EnrowAPI/phone-finder-swift) | SDK | Find mobile phone numbers from LinkedIn or name + company - Swift library powered by Enrow | 0 | 2026-04-06 | |
| [phone-finder-java](https://github.com/EnrowAPI/phone-finder-java) | SDK | Find mobile phone numbers from LinkedIn or name + company - Java library powered by Enrow | 0 | 2026-04-06 | |
| [phone-finder-rust](https://github.com/EnrowAPI/phone-finder-rust) | SDK | Find mobile phone numbers from LinkedIn or name + company - Rust library powered by Enrow | 0 | 2026-04-06 | |
| [phone-finder-php](https://github.com/EnrowAPI/phone-finder-php) | SDK | Find mobile phone numbers from LinkedIn or name + company - PHP library powered by Enrow | 0 | 2026-04-06 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 934 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://enrow.io/en/pricing](https://enrow.io/en/pricing)
- [https://enrow.io/en/api](https://enrow.io/en/api)
- [https://docs.enrow.io/](https://docs.enrow.io/)
- [https://docs.enrow.io/authentication](https://docs.enrow.io/authentication)
- [https://github.com/EnrowAPI/enrow-mcp](https://github.com/EnrowAPI/enrow-mcp)
- [https://www.pulsemcp.com/servers?q=enrow](https://www.pulsemcp.com/servers?q=enrow)

6 source URLs. Raw sources field, verbatim:

https://enrow.io/en/pricing, https://enrow.io/en/api, https://docs.enrow.io/, https://docs.enrow.io/authentication, https://github.com/EnrowAPI/enrow-mcp, https://www.pulsemcp.com/servers?q=enrow

**Notes, verbatim from the file**
Added 2026-08-25, closing a named warm lead from this file's previous sweep notes. THE CLEANEST api_gate IN THIS WHOLE SWEEP, and a strong contrast piece against the enterprise-gated incumbents in the same file. Free 50 credits with no card at app.enrow.io/signup. Start $17/mo (1,000 credits), Pro $87/mo (10,000), Scale $397/mo (50,000), Custom $1,000+/mo. Published unit economics: email finder $0.017 down to $0.00794, email verifier $0.00425 down to $0.00198, phone finder $0.68 down to $0.32. Credit consumption: 1 per email found, 0.25 per email verified, 50 per phone found. Credits roll over, unlimited team members on Pro and above, API and MCP on all tiers, key copied from the dashboard with no sales call. Auth is x-api-key; endpoints are async with webhook delivery. The MCP is vendor-owned under the EnrowAPI GitHub org and classified as an official provider on PulseMCP with a 2026-07-09 release date, roughly 12 tools, but the repo is young at roughly 9 commits, so treat maintenance as light. Paris, France, founded 2023, bootstrapped with no disclosed funding, which is a durability note rather than a death signal. Where docs.enrow.io and the marketing API page disagree on endpoint path strings, trust the docs. The homepage claim of "less than 45% bounce rates" is almost certainly a vendor typo; do not quote it as a quality stat.

**Provenance**

- **Entry id**: 01-enrow

- **Source file**: 01-data-enrichment.md

- **Source line**: 659

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
