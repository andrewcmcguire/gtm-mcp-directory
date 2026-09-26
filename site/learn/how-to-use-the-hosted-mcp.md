# How to use the hosted MCP: tools and data, no model on the backend

> The hosted /api/mcp path is a tools and data API. It has no backend LLM and no model selection. The model is always your MCP client's model, including LM Studio. Baked 2026-09-26: 1,252 entries, 201 official MCP servers.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I use the hosted GTM MCP Directory?

**The short answer**

The hosted /api/mcp path is a tools and data MCP server. It has no backend LLM and no model selection. The model is always the MCP client's model: Cursor, Claude Desktop, Claude Code, LM Studio, or another MCP host. Request a free gtmd_ key, add the URL with a Bearer header or the per-key URL, then ask in natural language. A local install of the same server needs no key.

> **Who runs the model**: The hosted `/api/mcp` path has no backend LLM and no model selection. The model is always the MCP client's model: Cursor, Claude Desktop, Claude Code, LM Studio, or another MCP host. Powerhouse and LM Studio factory jobs are an internal workstation path, not this runtime.

## What this is, and what it is not

This is a **tools and directory data API**. The hosted copy at `/gtm-directory/api/mcp` exposes the same eleven read-only tools as the public Python package. It answers from a baked `directory.json` and it makes zero outbound requests. It is not a chat model, not an assistant, and not a hosted LLM.

It has **no backend LLM** and **no model selection**. It does not host a model, does not pick a model, and does not switch models based on your query. The model is always the MCP client's model. When you type a question, that client model chooses a tool, fills the arguments, and reads the result. If the model invents a tool name or a count, that is the client's mistake, not a fact this server produced. Ask it to quote the honesty block and the bake date.

## Where it runs

The public site and the JSON live on AWS: object storage behind CloudFront. The MCP API is the same read-only server, reached at the apex path `https://andrewcmcguire.com/gtm-directory/api/mcp` and at the CloudFront fallback `https://d1hkopq5aq852m.cloudfront.net/gtm-directory/api/mcp`. Some clients hit a Cloudflare 403 on the apex host today. If yours does, swap the host and keep the rest of the URL and the key exactly as they are.

The hosted copy needs a free key. A key looks like `gtmd_` followed by 32 characters. Request one at [/access/](../access/index.md). A work email address is approved automatically, usually within about ten minutes. The local install needs no key because the code and the data are public. The [data endpoint](../data/directory.json) needs no key either.

## How to connect

Any client that supports headers (Cursor, Claude Desktop, Claude Code) sends `Authorization: Bearer gtmd_...`. Replace the placeholder with your key.

### Cursor and Claude Desktop

Paste this into the client's MCP settings. Cursor: Settings, MCP, add a server. Claude Desktop: edit `claude_desktop_config.json` and restart.

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

### Claude Code

```
claude mcp add --transport http gtm-directory https://andrewcmcguire.com/gtm-directory/api/mcp --header "Authorization: Bearer gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Clients that only take a URL

A claude.ai custom connector cannot send a header. Use the per-key URL, and treat that URL like the key it contains.

```
{
 "mcpServers": {
 "gtm-directory": {
 "url": "https://andrewcmcguire.com/gtm-directory/api/mcp/k/gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
 }
}
```

Both forms also work on the fallback host. The hosted copy records, per key, the number of calls and the date last used, and nothing else: no query text, no tool arguments, no IP log kept. Revoke a key by replying to the email it arrived in.

## LM Studio and other local models

LM Studio is a supported local client model path. You run a model in LM Studio. That model is the only model in the loop. Then you attach this directory as a remote MCP server. LM Studio uses the same `mcp.json` shape as Cursor (LM Studio 0.3.17 and later). The hosted `/api/mcp` path still has no backend LLM and no model selection.

- Load a model in LM Studio.

- Request a free `gtmd_` key at [/access/](../access/index.md).

- Add the directory as a remote MCP server. Send the key as `Authorization: Bearer gtmd_...`, or use the per-key URL `/api/mcp/k/gtmd_...` if the client only takes a URL.

- If the apex host returns 403, use `https://d1hkopq5aq852m.cloudfront.net/gtm-directory/api/mcp` and keep the path and the key the same.

- A local install of this server, attached from LM Studio over stdio, needs no key.

Paste this into LM Studio's `mcp.json` (same shape as Cursor). Replace the placeholder with your key:

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

If the apex host returns 403, use this CloudFront block instead. Path and key stay the same:

```
{
 "mcpServers": {
 "gtm-directory": {
 "url": "https://d1hkopq5aq852m.cloudfront.net/gtm-directory/api/mcp",
 "headers": {
 "Authorization": "Bearer gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
 }
 }
}
```

If the client only takes a URL, use the per-key form:

```
{
 "mcpServers": {
 "gtm-directory": {
 "url": "https://andrewcmcguire.com/gtm-directory/api/mcp/k/gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
 }
}
```

Powerhouse and any LM Studio factory jobs used internally to draft or harvest directory content are not the public product runtime. They do not run on `/api/mcp`, they do not select a model for visitors, and they are not required to query the hosted directory.

## The eleven tools, named exactly

Do not invent a twelfth. The server package is the authority.

| Tool | Question it answers |
|---|---|
| `find_tools` | Which tools claim a job, and by which interface (MCP, CLI) an agent can reach them |
| `get_tool` | One directory entry, every field, every source URL |
| `list_categories` | The 15 categories with counts and gates |
| `whats_mcpd` | How much of GTM an agent can reach, in numbers |
| `find_by_gate` | The access axis on its own: free, paid, enterprise, unknown |
| `get_docs_digest` | Structured facts from vendor API docs, when crawled |
| `get_server_tools` | What one MCP server actually exposes, with evidence |
| `get_install` | Both routes into one tool: the MCP endpoint and the CLI install commands |
| `whats_building` | What a vendor ships in public on GitHub, dated |
| `plan_stack` | A step by step shortlist for a multi-step GTM job |
| `list_jobs` | The closed capability vocabulary |

## What you can ask in natural language

Say the job in plain English. The client model maps that to a tool. These prompts are ones this directory can actually answer. Each line names the tool it should call. Two of them are site surfaces, not MCP tools, and the list says so.

- **I have a model loaded in LM Studio. Using only the GTM Directory tools, which official MCP servers can find a work email?**
 Maps to `find_tools` with a find-work-email job and `mcp_status=official`. The model is the one loaded in LM Studio. The hosted `/api/mcp` path does not select or run a model.

- **Show me free to start tools that have an MCP server a solo operator can actually reach.**
 Maps to `find_tools` with `mcp_status=official` (or community) and `gate=free` or `paid`. Solo reachable on this bake means an official or community server plus a free or paid self serve gate: 168 entries, counted 2026-09-26.

- **Look up HubSpot in the directory. What MCP status and access gate does it have?**
 Maps to `get_tool`. That is the directory entry, not the company page.

- **What tools does HubSpot's MCP server actually expose, and what is the evidence?**
 Maps to `get_server_tools`. A listed tool has not been called.

- **How do I install Clay's MCP and its CLI?**
 Maps to `get_install`. Every command is quoted from a source URL with a fetch date.

- **How much of GTM is agent reachable right now?**
 Maps to `whats_mcpd`. Quote the bake date with the numbers.

- **List the categories and how many official servers each has.**
 Maps to `list_categories`.

- **What jobs can I ask this directory about?**
 Maps to `list_jobs`. The vocabulary is closed on purpose.

- **Which tools need an enterprise contract just to get a key?**
 Maps to `find_by_gate` with `gate=enterprise-only`.

- **What do Exa's API docs actually say, as this directory crawled them?**
 Maps to `get_docs_digest`. If the docs have not been crawled, the tool says so rather than guessing.

- **What has Clay shipped in public on GitHub recently?**
 Maps to `whats_building`. Dated, or the field says it is unmeasured.

- **Plan a stack: find a LinkedIn URL from a name and company, get the work email, verify it.**
 Maps to `plan_stack`. A job tag means the vendor says the product does this. It is a reading order, not a benchmark.

- **Open HubSpot's company page in this directory.**
 Maps to a site page, not an MCP tool: [/companies/hubspot/](../companies/hubspot/index.md). Company pages are a small pilot. The current bake has three: HubSpot, Clay and Exa. There is no `get_company` tool.

- **What changed in the directory this week?**
 Maps to a site page, not an MCP tool: [/updates/](../updates/index.md), or the machine copies [feed.json](../updates/feed.json) and [atom.xml](../updates/atom.xml). There is no updates-feed tool on the server.

## Honesty vocabulary

Use these words the way this directory uses them, or the answer is wrong even if it sounds confident.

- **official** means the vendor ships and maintains the server itself. A wrapper from a third party integration platform is community, not official.

- **community** means somebody else built it. It can work. The failure mode is different: it can be abandoned without the vendor noticing.

- **none-found** is a statement about a search on a stated date, not a claim that no server exists. Every entry carries its own `last_checked` date.

- **unknown** is a legal answer and is published as unknown rather than guessed.

- **RESEARCHED** means facts from public sources with URLs. Nobody has run the tool. No usage claims.

- **BENCH-TESTED** means Andrew personally ran it on a stated date. It cannot be bought. This bake has 1 bench tested entry.

- **A job tag** means the vendor says the tool does this. It is not a test result.

**Never invent a count.** The live bake of 2026-09-26 has **1,252 entries** and **201 official** MCP servers (540 community, 487 none found, 15 unknown, 9 not applicable). If a later bake disagrees, quote that bake's `directory.json` instead. An undated number is a bug.

## Limits

- **Company pages are a small pilot.** Three account cards are live (HubSpot, Clay, Exa). They are Why Now cards, not a full account graph, and they are not MCP tools. Honesty badges and tool counts on those pages are copied from `directory.json`. A company page never invents official.

- **Harvest staging is not live promote.** New harvests stay staged. Nothing writes into the live category files or `directory.json` until it is reviewed. A staged candidate is not a listing.

- **No query text is logged.** Per the [access page](../access/index.md) policy, the hosted copy records, per key, the number of calls and the date last used, and nothing else: no query text, no tool arguments, no IP log kept.

- **The server does not call vendors for you.** It will not enrich a person, send an email, or write a CRM record. It tells you which tools claim those jobs and whether an agent can reach them.

## Sources

- [The GTM MCP Directory, request a key](../access/index.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site
- [The GTM MCP Directory, the counted data](../data.md) this site
- [The GTM MCP Directory, company pages (pilot)](../companies/index.md) this site
- [The GTM MCP Directory, updates feed](../updates/index.md) this site
- [Model Context Protocol, connect an MCP server to a client](https://modelcontextprotocol.io/quickstart/user) https://modelcontextprotocol.io/quickstart/user
- [LM Studio, Use MCP Servers](https://lmstudio.ai/docs/app/mcp) https://lmstudio.ai/docs/app/mcp

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-26. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [How do I add an MCP server to my AI client?](how-do-i-add-an-mcp-server-to-claude-desktop.md)
- [What is an MCP server?](what-is-an-mcp-server.md)
- [What is the difference between an official and a community MCP server?](official-vs-community-mcp-server.md)
- [What does agent ready mean for a GTM tool?](what-does-agent-ready-mean.md)

## In the directory

- [Request a key](../access/index.md)
- [Official servers](../lists/official-mcp-servers.md)
- [Company pages, the pilot](../companies/index.md)
- [Updates](../updates/index.md)
