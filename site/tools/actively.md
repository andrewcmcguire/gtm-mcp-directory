# Actively: MCP server status, API access gate and what it does

> A sales platform that runs an always-on "per-account agent" for every account in a seller's book,... Official MCP, Gate unknown. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Actively

# Actively

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [actively.ai](https://actively.ai) · entry id 05-actively · source 05-signals-intent-abm.md line 691

**What it does**
A sales platform that runs an always-on "per-account agent" for every account in a seller's book, synthesising CRM data, call transcripts and external signals into account research, risk flags and recommended next actions for the rep.

**AI features, separated from automation with an AI label on it**
The whole product is the agent layer; the vendor states "Per-Account Agents work every account 24/7, guide your team on what to do next, and help them do it." The MCP server exposes the agents' stored memory and decisions (get_agent_memory, get_agent_decisions, search_agent_memory) rather than raw data, so what a client reads is model output about the account.

**RevOps role**
An account-intelligence layer above the CRM for mid-market and enterprise sales teams; the MCP lets a rep's own assistant read what the per-account agent already concluded.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The vendor docs state "MCP access uses OAuth 2.1 with WorkOS." Tools are read-only: "Public tools are read-only, non-destructive, idempotent, and closed-world." Tool list per the docs: lookup_accounts, get_recent_account_activity, get_agent_memory, get_agent_memory_sections, get_bulk_agent_memory, search_agent_memory, get_agent_decisions, get_agent_decisions_sections, get_bulk_agent_decisions, list_workflows, get_workflow_instructions.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://app.actively.ai/docs/mcp (the docs state the server is "available at /mcp on the Actively app domain", i.e. https://app.actively.ai/mcp; Claude connector listing: https://claude.com/connectors/actively)

- [https://app.actively.ai/docs/mcp](https://app.actively.ai/docs/mcp)
- [https://app.actively.ai/mcp](https://app.actively.ai/mcp)
- [https://claude.com/connectors/actively](https://claude.com/connectors/actively)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown - the vendor site publishes no pricing page and every path ends in "Request a demo"; the MCP docs name no plan condition. Recorded as unknown on purpose: the MCP is demonstrably real and the condition for getting an account is not published.

346 of 649 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/Actively](https://github.com/Actively) tied to the vendor by rule 3, account website https://actively.ai has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2018-02-02

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [frontend-developer-test](https://github.com/Actively/frontend-developer-test) | app | | 0 | 2018-02-02 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

378 of 649 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://app.actively.ai/docs/mcp](https://app.actively.ai/docs/mcp)
- [https://claude.com/connectors/actively](https://claude.com/connectors/actively)
- [https://actively.ai](https://actively.ai)

3 source URLs. Raw sources field, verbatim:

https://app.actively.ai/docs/mcp, https://claude.com/connectors/actively, https://actively.ai

**Notes, verbatim from the file**
Probed 2026-09-07: POST of an MCP initialize to https://app.actively.ai/mcp returned HTTP 307 with a JSON body redirecting to api.workos.com/user_management/authorize; the control POST to /zzz-not-a-route on the same host returned the same 307 to WorkOS. An identical redirect on both paths is an auth wall in front of the whole app domain, not proof that /mcp answers as an MCP server; the vendor's docs page is the evidence for the server and the endpoint is recorded on the docs' statement. The candidate row's proposed alternative was ai-sdr-agents; it lands in signals because the product's output is account intelligence for a human rep, not autonomous outreach. Listed in the Claude connector directory with "Capabilities: Read". 2026-09-07: https://app.actively.ai/mcp returned 307 to an MCP initialize POST (https://app.actively.ai/mcp).

**Provenance**

- **Entry id**: 05-actively

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 691

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
