# GTM MCP servers behind a third party connector platform: 7 tools, counted

> 7 of the 182 GTM tools with an MCP server use a third party connector platform's auth. The verbatim auth field for each one is printed beside it. Counted 2026-09-04.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / GTM MCP servers behind a third party connector platform

**List · 7 of 293**

## GTM MCP servers behind a third party connector platform

Auth is handled by a connector platform sitting between the agent and the vendor, so the credential lives with the platform rather than with either end. The bucket is a keyword match over the mcp_auth field, run at build time, and the verbatim field ships in the row beside it so you can check the parse yourself. Where the two disagree, the verbatim field is the fact and the bucket is the convenience.

| Tool | MCP status | Server URL | mcp_auth, verbatim | Gate |
|---|---|---|---|---|
| [Landbot](../tools/landbot.md)
landbot.io | [Community MCP](../mcp/community.md) | [https://composio.dev/toolkits/landbot](https://composio.dev/toolkits/landbot) +1 more | The operator's own Landbot API key stored with Composio; the Zapier connector rides Zapier's hosted auth at mcp.zapier.com. | [Free to start](../gates/free.md) |
| [Chatbase](../tools/chatbase.md)
chatbase.co | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/chatbase](https://zapier.com/mcp/chatbase) | Rides Zapier's hosted-connector auth at mcp.zapier.com, not a Chatbase-issued MCP credential. | [Paid, self-serve](../gates/paid.md) |
| [Klenty](../tools/klenty.md)
klenty.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/klenty](https://zapier.com/mcp/klenty) +1 more | Rides Zapier's hosted-connector auth at mcp.zapier.com (and Runbear's for the Slack connector), not a Klenty-issued MCP credential. | [Paid, self-serve](../gates/paid.md) |
| [Sendspark](../tools/sendspark.md)
sendspark.com | [Community MCP](../mcp/community.md) | [https://composio.dev/toolkits/sendspark](https://composio.dev/toolkits/sendspark) | API-key based - Composio's page states Sendspark requires the user's own API key, which Composio then stores/manages. | [Paid, self-serve](../gates/paid.md) |
| [Vidyard](../tools/vidyard.md)
vidyard.com | [Community MCP](../mcp/community.md) | [https://viasocket.com/mcp/vidyard](https://viasocket.com/mcp/vidyard) | Not documented in technical detail on the viaSocket listing ("built-in authentication"). Vidyard's own Video Agent REST API (separate from any MCP)... | [Paid, self-serve](../gates/paid.md) |
| [Weezly](../tools/weezly.md)
weezly.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/weezly](https://zapier.com/mcp/weezly) | Zapier-mediated connection. | [Paid, self-serve](../gates/paid.md) |
| [WorkRamp](../tools/workramp.md)
workramp.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/workramp](https://zapier.com/mcp/workramp) +1 more | Rides Zapier's/viaSocket's own hosted-connector auth (their MCP gateway at mcp.zapier.com), not a WorkRamp-issued credential. | [Enterprise only](../gates/enterprise-only.md) |

Counted 2026-09-04 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
