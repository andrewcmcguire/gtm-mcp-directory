# Klavis AI: MCP server status, API access gate and what it does

> Primarily an AI-agent training-data company - it builds "live environments for training AI agents"... Official MCP, Gate unknown. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Klavis AI

# Klavis AI

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [klavis.ai](https://klavis.ai) · entry id 07-klavis-ai · source 07-mcp-infrastructure.md line 219

**What it does**
Primarily an AI-agent training-data company - it builds "live environments for training AI agents" (long-horizon coding tasks and agentic tool-use scenarios), and separately mentions "production MCP servers" and "600+ real tools and SaaS apps" as part of that training-data infrastructure.

**AI features, separated from automation with an AI label on it**
The product itself generates training/eval data for frontier model development (dockerized coding environments, programmatic verification, reward signals) - it is not positioned, in what was found, as a live GTM connector layer the way Composio/Pipedream/Metorial are.

**RevOps role**
Unclear fit for a solo GTM operator based on what's public - reads as an AI-lab infrastructure vendor (agent training data) rather than a connector service a RevOps team would wire into a live workflow. Flagging this mismatch explicitly rather than assuming it belongs alongside Composio/Pipedream.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Klavis API key as an HTTP Bearer token on the management API that creates a per-user Strata server (https://www.klavis.ai/docs/api-reference/strata/create.md); the response returns a strataServerUrl to connect to plus per-integration OAuth and API-key setup URLs for the downstream apps. The hosted endpoint answered 401 to an unauthenticated request today.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-02 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.klavis.ai/docs/concepts/strata.md (first-party docs for the hosted Strata server; endpoint https://strata.klavis.ai/mcp/ per the official registry entry ai.klavis/strata; source at https://github.com/Klavis-AI/klavis, Apache-2.0)

- [https://www.klavis.ai/docs/concepts/strata.md](https://www.klavis.ai/docs/concepts/strata.md)
- [https://strata.klavis.ai/mcp/](https://strata.klavis.ai/mcp/)
- [https://github.com/Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown - pricing page referenced but not disclosed in the fetched content

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: unclear. The entry states the product is agent-training-data infrastructure and explicitly flags the mismatch with Composio/Pipedream. proxy-tool-calls-to-saas is plausible from the "600+ real tools" line and unsupported by everything else on the page.

22 of 293 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.klavis.ai](https://www.klavis.ai)
- [https://klavis.ai/pricing](https://klavis.ai/pricing)
- [https://www.klavis.ai/docs/quickstart.md](https://www.klavis.ai/docs/quickstart.md)
- [https://www.klavis.ai/docs/concepts/strata.md](https://www.klavis.ai/docs/concepts/strata.md)
- [https://www.klavis.ai/docs/api-reference/strata/create.md](https://www.klavis.ai/docs/api-reference/strata/create.md)
- [https://github.com/Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)
- [https://registry.modelcontextprotocol.io/v0/servers?search=klavis](https://registry.modelcontextprotocol.io/v0/servers?search=klavis)
- (fetched; no pricing figures returned)

7 source URLs. Raw sources field, verbatim:

https://www.klavis.ai, https://klavis.ai/pricing (fetched; no pricing figures returned), https://www.klavis.ai/docs/quickstart.md, https://www.klavis.ai/docs/concepts/strata.md, https://www.klavis.ai/docs/api-reference/strata/create.md, https://github.com/Klavis-AI/klavis, https://registry.modelcontextprotocol.io/v0/servers?search=klavis

**Notes, verbatim from the file**
Included per the research brief's seed list, but the public-facing material found positions Klavis as an AI-agent training/eval company first, not a GTM-facing hosted-MCP aggregator - treat any "GTM connector" framing of Klavis with caution until a clearer product page is found. [api_gate 2026-08-25] Re-checked and left unknown, honestly: the quickstart says to create an account and get the API key from klavis.ai/home/api-keys, so keys are self-serve with no sales call and an open-source self-hosted path exists - but klavis.ai/pricing is client-rendered and returned only nav and footer to a plain fetch, so whether a free tier or a paid plan backs those keys is unverified and the free-versus-paid split stays unknown. Checked against https://www.klavis.ai/docs/quickstart.md. 2026-09-02: mcp_status none-found -> official. Klavis publishes a hosted MCP server, Strata, documented at https://www.klavis.ai/docs/concepts/strata.md ("One MCP server for AI agents to use tools progressively at any scale") with a create endpoint at https://www.klavis.ai/docs/api-reference/strata/create.md; the official MCP registry lists ai.klavis/strata with the remote https://strata.klavis.ai/mcp/ (401 today, alive and auth-gated); and the GitHub repo https://github.com/Klavis-AI/klavis describes "MCP integration platforms that let AI agents use tools reliably at any scale" with 100+ prebuilt integrations with OAuth support, cloud-hosted or self-hosted. That softens the caution above: Klavis is a usable MCP integration layer as well as a training-data vendor. Pricing is still unpublished to a plain fetch, so api_gate stays unknown.

**Provenance**

- **Entry id**: 07-klavis-ai

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 219

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
