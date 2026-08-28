# Community MCP servers: 21 GTM tools with a third party server

> Go to market tools where a working MCP server exists but somebody other than the vendor built it. Counted 2026-08-28 across 293 directory entries.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / The 21 GTM tools with a community MCP server

**List · 21 of 293**

## The 21 GTM tools with a community MCP server

A community server is a real server. It is also a server that can be abandoned without the vendor noticing, which is the single most useful thing to know before you write one into a workflow. The repo health rail that would date stamp each one has not been run, so no staleness claim is made here.

| Tool | Category | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Fathom](../tools/fathom.md)
fathom.video | [Conversation Intel](../categories/conversation-intel.md) | [https://github.com/trevorwelch/fathom-video-mcp](https://github.com/trevorwelch/fathom-video-mcp) +2 more | API key
Community servers authenticate with a Fathom API key (FATHOM_API_KEY environment... | [Free to start](../gates/free.md) |
| [Loom](../tools/loom.md)
loom.com | [Video Prospecting](../categories/video-prospecting.md) | [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom) +2 more | API key
karbassi/mcp-loom uses Loom's undocumented internal GraphQL API via a browser session... | [Free to start](../gates/free.md) |
| [People Data Labs](../tools/people-data-labs.md)
peopledatalabs.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp) | API key
api key (PDL_API_KEY environment variable) | [Free to start](../gates/free.md) |
| [Bonjoro](../tools/bonjoro.md)
bonjoro.com | [Video Prospecting](../categories/video-prospecting.md) | [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro) | OAuth
Rides a Zapier account connection (OAuth to Zapier, which holds the Bonjoro-side... | [Paid, self-serve](../gates/paid.md) |
| [Clari Copilot](../tools/clari-copilot.md)
clari.com | [Conversation Intel](../categories/conversation-intel.md) | [https://www.scalekit.com/connectors/claricopilot](https://www.scalekit.com/connectors/claricopilot) +1 more | OAuth or an API key
Scalekit-hosted connector uses per-user delegated OAuth-style authorization in Scalekit's... | [Paid, self-serve](../gates/paid.md) |
| [Motion](../tools/motion.md)
usemotion.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp) | API key
API key (MOTION_API_KEY from Motion Settings -> API), per community repos. Rate limits... | [Paid, self-serve](../gates/paid.md) |
| [Overloop](../tools/overloop.md)
overloop.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp) | API key
api key via OVERLOOP_API_KEY environment variable | [Paid, self-serve](../gates/paid.md) |
| [SavvyCal](../tools/savvycal.md)
savvycal.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server) | API key
API key (SAVVYCAL_API_KEY env var, a personal access token from SavvyCal's Developer... | [Paid, self-serve](../gates/paid.md) |
| [Sendspark](../tools/sendspark.md)
sendspark.com | [Video Prospecting](../categories/video-prospecting.md) | [https://composio.dev/toolkits/sendspark](https://composio.dev/toolkits/sendspark) | Third party platform auth
API-key based - Composio's page states Sendspark requires the user's own API key, which... | [Paid, self-serve](../gates/paid.md) |
| [Smartlead](../tools/smartlead.md)
smartlead.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server) +1 more | API key
api key | [Paid, self-serve](../gates/paid.md) |
| [Syften](../tools/syften.md)
syften.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://github.com/syntax-syndicate/social-listening](https://github.com/syntax-syndicate/social-listening) | API key
Community server presumably authenticates with a Syften API key (matching Syften's own... | [Paid, self-serve](../gates/paid.md) |
| [Trigify (Trigify.io)](../tools/trigify.md)
trigify.io | [Signals & Intent](../categories/signals-intent-abm.md) | [https://github.com/bcharleson/trigify-cli](https://github.com/bcharleson/trigify-cli) | API key
api key (from app.trigify.io/settings; via `trigify login --api-key`, env var... | [Paid, self-serve](../gates/paid.md) |
| [Unify](../tools/unify.md)
unifygtm.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp) | Auth not recorded
Auth0 browser sign-in (auth.unifygtm.com); MCP caches the session cookie (~30-day life)... | [Paid, self-serve](../gates/paid.md) |
| [UpLead](../tools/uplead.md)
uplead.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://zapier.com/mcp/uplead](https://zapier.com/mcp/uplead) +1 more | OAuth or an API key
Handled through the Zapier/Pipedream platform's own connector auth (API key entered into... | [Paid, self-serve](../gates/paid.md) |
| [Vidyard](../tools/vidyard.md)
vidyard.com | [Video Prospecting](../categories/video-prospecting.md) | [https://viasocket.com/mcp/vidyard](https://viasocket.com/mcp/vidyard) | Third party platform auth
Not documented in technical detail on the viaSocket listing ("built-in authentication").... | [Paid, self-serve](../gates/paid.md) |
| [Weezly](../tools/weezly.md)
weezly.com | [Video Prospecting](../categories/video-prospecting.md) | [https://zapier.com/mcp/weezly](https://zapier.com/mcp/weezly) | Third party platform auth
Zapier-mediated connection. | [Paid, self-serve](../gates/paid.md) |
| [BombBomb](../tools/bombbomb.md)
bombbomb.com | [Video Prospecting](../categories/video-prospecting.md) | [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom) | OAuth or an API key
Rides Zapier's own OAuth/API-key connection to BombBomb; not a native BombBomb MCP auth... | [Enterprise only](../gates/enterprise-only.md) |
| [Brandwatch](../tools/brandwatch.md)
brandwatch.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch) | Auth not recorded
unknown - the third-party server's description states it interfaces with "the Brandwatch... | [Enterprise only](../gates/enterprise-only.md) |
| [Copy.ai (GTM AI Platform)](../tools/copy-ai.md)
copy.ai | [AI SDRs](../categories/ai-sdr-agents.md) | [https://github.com/anhuaxiang/copy-ai-mcp](https://github.com/anhuaxiang/copy-ai-mcp) | API key
API key via COPY_AI_API_KEY environment variable | [Enterprise only](../gates/enterprise-only.md) |
| [Jiminny](../tools/jiminny.md)
jiminny.com | [Conversation Intel](../categories/conversation-intel.md) | [https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp](https://glama.ai/mcp/servers/fzheng0222/jiminny-mcp) +1 more | OAuth or an API key
Community server: JIMINNY_TOKEN API token. Zapier's hosted connector uses Zapier's own... | [Enterprise only](../gates/enterprise-only.md) |
| [WorkRamp](../tools/workramp.md)
workramp.com | [Enablement & Coaching](../categories/enablement-coaching.md) | [https://zapier.com/mcp/workramp](https://zapier.com/mcp/workramp) +1 more | Third party platform auth
Rides Zapier's/viaSocket's own hosted-connector auth (their MCP gateway at... | [Enterprise only](../gates/enterprise-only.md) |

Counted 2026-08-28 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
