# Copy.ai (GTM AI Platform): MCP server status, API access gate and what it does

> Pivoted from an AI copywriting tool to a workflow-building platform ("Copy Agents") that automates GTM tasks... Community MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
Copy.ai (GTM AI Platform)

# Copy.ai (GTM AI Platform)

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.copy.ai](https://www.copy.ai) · entry id 04-copy-ai · source 04-ai-sdr-agents.md line 144

**What it does**
Pivoted from an AI copywriting tool to a workflow-building platform ("Copy Agents") that automates GTM tasks - prospecting/lead research, inbound enrichment, content generation, deal analysis - via user-built AI workflows with guardrails.

**AI features, separated from automation with an AI label on it**
Explicitly positions itself against "unconstrained AI agents," emphasizing structured, guardrailed automation (its "Actions"/"Tables" building blocks) over freeform autonomy - a rare case of a vendor being modest about its own agentic-ness rather than overselling it.

**RevOps role**
Workflow/automation layer that can be pointed at prospecting, content, or deal-analysis tasks depending on configuration - more of a builder toolkit than a packaged "AI SDR."

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: API key via COPY_AI_API_KEY environment variable

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/anhuaxiang/copy-ai-mcp](https://github.com/anhuaxiang/copy-ai-mcp)Probed**: 2026-09-03, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/anhuaxiang/copy-ai-mcp

- [https://github.com/anhuaxiang/copy-ai-mcp](https://github.com/anhuaxiang/copy-ai-mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (API Access and Bulk Workflow Runs appear only in the Enterprise custom-pricing tier; the self-serve $29/mo Chat plan and the $1,000 to $3,000/mo Growth, Expansion and Scale tiers do not list API access)

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/anhuaxiang/copy-ai-mcp](https://github.com/anhuaxiang/copy-ai-mcp)

**Jobs it can do**

- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.copy.ai](https://www.copy.ai)
- [https://github.com/anhuaxiang/copy-ai-mcp](https://github.com/anhuaxiang/copy-ai-mcp)
- [https://www.copy.ai/pricing](https://www.copy.ai/pricing)

3 source URLs. Raw sources field, verbatim:

https://www.copy.ai, https://github.com/anhuaxiang/copy-ai-mcp, https://www.copy.ai/pricing

**Notes, verbatim from the file**
The community MCP repo is very thin - 1 star, 3 commits, 0 forks/issues - treat as experimental, not production-ready. No official Copy.ai MCP found. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.copy.ai/pricing): API Access and Bulk Workflow Runs appear only in the Enterprise custom-pricing tier; the self-serve $29/mo Chat plan and the $1,000 to $3,000/mo Growth, Expansion and Scale tiers do not list API access.

**Provenance**

- **Entry id**: 04-copy-ai

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 144

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
