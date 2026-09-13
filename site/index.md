# The GTM MCP Directory

> 784 GTM tools counted, 200 with an official MCP server. Which tools an agent can actually call, and which ones a solo operator can reach without a procurement cycle.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](llms.txt). The whole dataset: [directory.json](data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
**Agent Operator**

# The GTM MCP
Directory

Every GTM tool your agent can use, and which one does the job.

**784 tools** counted · **200 official MCP servers** · **8,507 tools those servers name** · generated **2026-09-12** by build_directory.py (phase 1) · reconciled against tools_recount.py

- **tools counted**: 784

- **official MCP servers**: 200

- **tools those servers name**: 8,507

- **community MCP**: 180

- **no MCP found**: 380

- **enterprise gated**: 79

- **solo reachable**: 168

- **bench tested**: 1

- **ship a CLI (official) as of 2026-09-12**: 55

Entry facts were pulled by hand: 71 on 2026-08-24, 22 on 2026-08-25, 121 on 2026-09-02, 15 on 2026-09-03, 107 on 2026-09-07, 448 on 2026-09-12. The generated date above is only the date this site was baked. Both dates ship because both rot. 768 of the 784 entries are unique products; 16 are the same product listed in a second category and counted once here.

The tool count is the capability layer, harvested 2026-09-12: 119 of the 380 entries that record an official or community MCP server have a harvested tool list, and it names 8,507 tools. 2,514 of those belong to the GTM tools themselves; 5,993 belong to one gateway that re-exposes other vendors and are counted apart. The remaining 261 servers are **unmeasured, not empty**: nobody has read their tool list yet, and their pages say exactly that. None of these tools has been called. Bench tested, meaning somebody actually ran it, is still 1 across the whole directory.

The command-line layer was harvested 2026-09-12 across vendor docs, npm, PyPI, Homebrew and GitHub: 55 of the 784 entries ship a CLI the vendor publishes, 37 have only a third party's, and 244 came back none found, which is a probe result on that date and not proof of absence. Each tool page quotes the install command with the URL it came from.

- [Search by capability](#search)

- [Install the MCP server](#install)

- [Every tool a server names](tools-index.md)

- [See the 200 official servers](mcp/official.md)

**Capability search**

## Ask for the job, not the category.

An agent does not want a data enrichment tool. It wants a person's title from a LinkedIn URL. Type the thing you are trying to do. This runs in your browser over a baked index: no backend, no query logging, and it keeps working with the network cable pulled out.

Search the directory

Official MCPCommunity MCPMCP unknownMCP not applicableNo MCP found
Free to startPaid, self-serveEnterprise leaningEnterprise onlyGate unknownGate not applicable
Ships a CLI

Ordering is fixed and published, never tuned and never purchasable. official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable. With a query typed, matches are banded by relevance first and the rule above breaks every tie. An exact name match pins to the top and nothing else is boosted. The filters above run over the 768 unique products, so their totals sit below the 784 entry totals used by the [MCP status](mcp/index.md) and [gate](gates/index.md) views. Both numbers are correct and the difference is the 16 cross listings.

**The inversion**

## The tools sold as agents are the least usable by agents.

MCP Layer is 125 of 130 reachable by an agent. Enablement & Coaching is 3 of 44. Gold is an official server, green is a community one. Every ratio below is read straight out of the category blocks in directory.json.

- [MCP Layer](categories/mcp-infrastructure.md)**125** of 130 reachable

- [Data & Enrichment](categories/data-enrichment.md)**66** of 121 reachable

- [Video Prospecting](categories/video-prospecting.md)**10** of 19 reachable

- [Community & Dark Social](categories/community-dark-social.md)**11** of 21 reachable

- [RevOps Infra](categories/revops-infra.md)**37** of 73 reachable

- [Conversation Intel](categories/conversation-intel.md)**21** of 42 reachable

- [Scheduling & Routing](categories/scheduling-routing.md)**7** of 16 reachable

- [Proposals & Deals](categories/proposals-deals.md)**10** of 23 reachable

- [Signals & Intent](categories/signals-intent-abm.md)**25** of 61 reachable

- [Engagement & Outbound](categories/engagement-outbound.md)**33** of 105 reachable

- [Inbound & PLG Chat](categories/inbound-plg-chat.md)**13** of 43 reachable

- [AI SDRs](categories/ai-sdr-agents.md)**12** of 44 reachable

- [Email Deliverability](categories/email-deliverability.md)**4** of 21 reachable

- [Forecasting & Revenue](categories/forecasting-revenue.md)**3** of 21 reachable

- [Enablement & Coaching](categories/enablement-coaching.md)**3** of 44 reachable

**Install the MCP server**

## Point your agent at the directory.

The server loads the baked file once at import and answers from memory. It makes zero outbound network requests, so it cannot be slow, cannot rate limit you, cannot cost anything, and cannot leak your query to a vendor. Everything network shaped happens in the weekly build.

```
{
 "mcpServers": {
 "gtm-directory": {
 "url": "https://andrewcmcguire.com/gtm-directory/api/mcp",
 "headers": {
 "Authorization": "Bearer gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
 }
 }
}
```

That is the hosted copy, live since 2026-09-08: streamable HTTP, no install, the same read-only server this page is built from, restarted on every publish. It needs a free key, and `gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` above is where yours goes. [Request a key](access/index.md). A work email address is approved automatically, usually within about ten minutes. The hosted copy records, per key, the number of calls and the date last used, and nothing else: no query text, no tool arguments, no IP log kept.

```
claude mcp add --transport http gtm-directory https://andrewcmcguire.com/gtm-directory/api/mcp --header "Authorization: Bearer gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

Same key, as one line for Claude Code. A client that only accepts a URL (claude.ai custom connectors) cannot send a header, so it uses the per-key URL instead:

```
{
 "mcpServers": {
 "gtm-directory": {
 "url": "https://andrewcmcguire.com/gtm-directory/api/mcp/k/gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
 }
}
```

Both forms also work on the fallback host `https://d1hkopq5aq852m.cloudfront.net/gtm-directory/api/mcp`. Some clients hit a Cloudflare 403 on the apex host today; if yours does, swap the host and keep the rest. If you would rather run it yourself, no key is needed, because the code and the data are public:

```
{
 "mcpServers": {
 "gtm-directory": {
 "command": "uvx",
 "args": [
 "gtm-mcp-directory"
 ]
 }
 }
}
```

The package is not on PyPI yet, so this block is the shape the install will take rather than a working one-liner today. The server source is real and public: it lives in the [gtm-mcp-directory](https://github.com/andrewcmcguire/gtm-mcp-directory) repo and runs from a checkout right now.

**What it answers**

### find_tools

Which tools can do X, and can your agent actually reach them. Filters on category, MCP status, access gate and tier, and states the ordering rule it used.

**What it answers**

### get_tool

Every field on one entry, sources in full, plus the cross reference when the same product is listed in a second category.

**What it answers**

### whats_mcpd

The stat block. 784 entries, 200 official, 180 community, 380 none found, and 1 bench tested, scoped to a category when you ask for one.

**What it answers**

### list_categories

The 15 category files with their counts, gates and source markdown, reconciled against tools_recount.py at build time.

**The weekly diff**

## Get the changelog by email.

Once a week: new entries, dead endpoints, gate changes, and every tool that moved between MCP statuses. Assembled from the machine output, never written from thin air.

PLACEHOLDER. The list runs on Kit and the form action is deliberately empty until that endpoint is set. No address is collected today and nothing is sent anywhere.

**Submit a tool**

## Listing is free. Placement is not for sale.

Anyone can submit a tool. Every submission is verified against public sources before it is listed, and the verification is the product. No vendor can pay to be listed, to rank higher, to be featured, or to soften a note. BENCH-TESTED cannot be bought at any price.

- [Open the submission form](https://github.com/andrewcmcguire/gtm-mcp-directory/issues/new?template=tool-submission.yml)

- [Read what happens next](submit.md)

The submission queue is a GitHub issue form on the public gtm-mcp-directory repo. It is open now, and every submission is verified before it lists.

**The questions**

## Answers, not opinions.

The questions people actually ask about GTM tools, MCP servers and agents, answered from this data with the numbers generated at build time and the date stamped on every one. No tool versus tool verdicts, because 1 tools here have been bench tested.

- [Learn](learn/index.md) - Definitions, data and how to. What an MCP server is, what a GTM engineer is, which tools an agent can use for free, how to connect an assistant to a CRM.

- [The lists](lists/index.md) - 200 official servers, 78 free tiers. The same entries cut the ways people ask for them: by MCP status, by gate, by auth type, by category.

- [By job](jobs/index.md) - 56 jobs, 10 families. What an agent actually asks for, phrased from the agent's side, with the tools tagged against each one.

- [The data](data.md) - directory.json, free, no key. The whole directory as one JSON file, plus llms.txt and a markdown twin of every page on this site.

**Honesty**

## 1 bench tested, and that number is on the front page.

Every entry is RESEARCHED: facts from public sources with URLs, no usage claims, nobody has run the tool. BENCH-TESTED means Andrew personally ran it on a stated date. There are 1 of those, the number is published rather than hidden, and it is the proof the tier means something. 481 entries carry an access gate of unknown, 528 have no documentation URL recorded, and the 23 thinly sourced entries are named on the methodology page rather than quietly padded.

- [How an entry is made](methodology.md)

- [Browse all 768 products](tools/index.md)
