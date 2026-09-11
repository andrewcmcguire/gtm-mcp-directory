# Typeform: MCP server status, API access gate and what it does

> An online form and survey builder (conversational one-question-at-a-time forms, quizzes, lead-capture forms)... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Typeform

# Typeform

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [typeform.com](https://typeform.com) · entry id 14-typeform · source 14-inbound-plg-chat.md line 333

**What it does**
An online form and survey builder (conversational one-question-at-a-time forms, quizzes, lead-capture forms) with logic, integrations, webhooks and a REST API, widely used as the top-of-funnel intake form.

**AI features, separated from automation with an AI label on it**
AI shows up in form generation and response insights inside the product; the MCP server exposes forms, automations, contacts and insights tool groups (forms-*, automations-*, contacts-*, insights-*). The form engine itself is not AI.

**RevOps role**
The inbound intake form under a lead-routing and enrichment flow; the MCP lets an agent build the form, read responses and drive automations.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The docs state "Authorization is OAuth 2.0, and your client is prompted on first connect." EU-hosted accounts use different endpoints, and a hosted connector needs its redirect domain allowlisted first.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.typeform.com/mcp (docs: https://www.typeform.com/developers/get-started/mcp/; plan gating: https://www.typeform.com/developers/mcp/plans/)

- [https://api.typeform.com/mcp](https://api.typeform.com/mcp)
- [https://www.typeform.com/developers/get-started/mcp/](https://www.typeform.com/developers/get-started/mcp/)
- [https://www.typeform.com/developers/mcp/plans/](https://www.typeform.com/developers/mcp/plans/)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

120 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 105 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the pricing page lists a Free plan, Basic $28/month, Plus $56/month, Business $91/month, Growth Flow $266/month, Talent $119/month and Enterprise custom; the MCP plans page states "Every account sees the same tool list, so tools/list is stable and safe to cache" and "Access to the underlying features is subject to their availability in the account's subscription plan, and is enforced when a tool is called." Webhooks are listed as unavailable on Free and Basic. Recorded as paid because the working tool surface follows the paid plan even though the connection itself is open to every account.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/Typeform](https://github.com/Typeform) tied to the vendor by rule 3, account website https://www.typeform.com has the vendor's domain, confidence strong

- **Public repositories**: 22, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [js-api-client](https://github.com/Typeform/js-api-client) | SDK | Typeform API js client | 85 | 2026-09-07 | v2.10.4 |
| [ci-standard-checks](https://github.com/Typeform/ci-standard-checks) | other | Standard Checks for Typeform repos | 2 | 2026-09-06 | v1.31.5-beta.1 |
| [.github](https://github.com/Typeform/.github) | other | DEPRECATED: Use .github-private/ instead! Only accepts edits of existing workflows. | 4 | 2026-09-06 | v1.55.0 |
| [eslint-config-typeform](https://github.com/Typeform/eslint-config-typeform) | other | ESLint configuration for Typeform front-end projects | 0 | 2026-09-06 | v7.0.20 |
| [embed](https://github.com/Typeform/embed) | app | Library to embed Typeforms in your website | 319 | 2026-09-06 | @typeform/embed-v6.0.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.typeform.com/developers/get-started/mcp/](https://www.typeform.com/developers/get-started/mcp/)
- [https://www.typeform.com/developers/mcp/plans/](https://www.typeform.com/developers/mcp/plans/)
- [https://www.typeform.com/pricing/](https://www.typeform.com/pricing/)
- [https://api.typeform.com/mcp](https://api.typeform.com/mcp)

4 source URLs. Raw sources field, verbatim:

https://www.typeform.com/developers/get-started/mcp/, https://www.typeform.com/developers/mcp/plans/, https://www.typeform.com/pricing/, https://api.typeform.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://api.typeform.com/mcp returned HTTP 401 with JSON reading "not authorized"; the control POST to /zzz-not-a-route returned 404 with a JSON body reading "Endpoint not found". Live first-party auth-gated server. The plan-gating design (stable tool list, per-call enforcement, and the docs' instruction to "Branch on the top-level code, never on the prose") is the clearest published pattern in this directory for how a vendor hides plan limits inside an MCP: the connector works on every plan and the tool call fails on the wrong one, the same failure shape Vayne documents in 01-data-enrichment.md. 2026-09-07: https://api.typeform.com/mcp returned 401 to an MCP initialize POST (https://api.typeform.com/mcp).

**Provenance**

- **Entry id**: 14-typeform

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 333

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
