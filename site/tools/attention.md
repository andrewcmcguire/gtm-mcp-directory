# Attention: MCP server status, API access gate and what it does

> Captures, transcribes, and analyzes sales and customer conversations, automatically syncing structured... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Attention

# Attention

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [attention.com](https://attention.com) · entry id 03-attention · source 03-conversation-intel.md line 144

**What it does**
Captures, transcribes, and analyzes sales and customer conversations, automatically syncing structured insights to the CRM.

**AI features, separated from automation with an AI label on it**
AI-driven CRM auto-fill from calls, "AI sales agents" for follow-up automation, coaching workflows, sentiment/summary extraction, and searchable call snippets.

**RevOps role**
CRM-auto-write conversation-intelligence layer, marketed as an "AI agent platform" for sales conversations rather than a passive recorder.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth for end users, api key for programmatic access, per https://docs.attention.com/mcp/authentication read 2026-08-28.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.attention.com/mcp/overview](https://docs.attention.com/mcp/overview)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.attention.com/mcp/overview (re-verified 200 on 2026-08-28; corrected that day off a dead receipt, see notes. An unofficial community fork also exists: https://github.com/highgravitas/attention-mcp)

- [https://docs.attention.com/mcp/overview](https://docs.attention.com/mcp/overview)
- [https://github.com/highgravitas/attention-mcp](https://github.com/highgravitas/attention-mcp)

**What this server exposes**

- **Tools named**: 7
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-09
- **Repo read**: highgravitas/attention-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **ask_attention** Run Attention evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_conversation** Get full details and transcript for a specific Attention conversation by ID. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_scorecards_summary** Get per-criterion averages for a scorecard over a date range. Feeds weekly manager rollup. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_gi_history** List an org user evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_recent_conversations** List recent Attention conversations from the past N days. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_scorecards** List all scorecards configured for the organization (id, name, criteria). Call this first to pick a scorecard_id and criterion ids for create_scorecard_result. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_conversations** Search Attention for call recordings and transcripts. Use for sales calls, customer calls, and demos. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-09. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-09 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. No free plan; pricing runs roughly $100-$500/month per third-party trackers, with deeper API/security features reserved for a Contact-Sales Enterprise tier.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/highgravitas/attention-mcp](https://github.com/highgravitas/attention-mcp)

**On GitHub**

No GitHub organisation could be tied to attention.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

6 candidate accounts seen and rejected by the evidence rules: highgravitas, team-attention, AttentionX, buckaroo-it, attentiontech. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://docs.attention.com/mcp/overview](https://docs.attention.com/mcp/overview)
- [https://docs.attention.com/mcp/authentication](https://docs.attention.com/mcp/authentication)
- [https://docs.attention.com/llms.txt](https://docs.attention.com/llms.txt)
- [https://www.attention.com/](https://www.attention.com/)
- [https://coldiq.com/tools/attention](https://coldiq.com/tools/attention)
- [https://github.com/highgravitas/attention-mcp](https://github.com/highgravitas/attention-mcp)

6 source URLs. Raw sources field, verbatim:

https://docs.attention.com/mcp/overview, https://docs.attention.com/mcp/authentication, https://docs.attention.com/llms.txt, https://www.attention.com/, https://coldiq.com/tools/attention, https://github.com/highgravitas/attention-mcp

**Notes, verbatim from the file**
2026-08-28 link-rot correction. The mcp_url published until today, docs.attention.com/attention-mcp-server, 404d when re-checked on 2026-08-27. It is named here rather than left in the mcp_url field so the published page does not carry a link to a 404. The current first-party receipt was found in https://docs.attention.com/llms.txt, which indexes a full Attention MCP Server section, and both the overview and authentication pages return 200. mcp_status stays official on a live first-party URL, not on the old one.

**Provenance**

- **Entry id**: 03-attention

- **Source file**: 03-conversation-intel.md

- **Source line**: 144

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-09

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
