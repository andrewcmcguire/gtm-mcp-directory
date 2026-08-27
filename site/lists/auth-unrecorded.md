# GTM MCP servers with no auth model recorded: 26 tools, counted

> 26 of the 165 GTM tools with an MCP server use an auth model that is not recorded. The verbatim auth field for each one is printed beside it. Counted 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / GTM MCP servers with no auth model recorded

**List · 26 of 293**

## GTM MCP servers with no auth model recorded

The mcp_auth field on the entry is blank, or says unknown. Published as blank rather than guessed. The bucket is a keyword match over the mcp_auth field, run at build time, and the verbatim field ships in the row beside it so you can check the parse yourself. Where the two disagree, the verbatim field is the fact and the bucket is the convenience.

| Tool | MCP status | Server URL | mcp_auth, verbatim | Gate |
|---|---|---|---|---|
| [Common Paper](../tools/common-paper.md)
commonpaper.com | [Official MCP](../mcp/official.md) | [https://commonpaper.com/release-notes/common-paper-m...](https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/) +1 more | unknown - not detailed in the release-notes excerpt reviewed. | [Free to start](../gates/free.md) |
| [Crustdata](../tools/crustdata.md)
crustdata.com | [Official MCP](../mcp/official.md) | [https://crustdata.com/](https://crustdata.com/) | unknown | [Free to start](../gates/free.md) |
| [Hightouch](../tools/hightouch.md)
hightouch.com | [Official MCP](../mcp/official.md) | [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp) | Existing Hightouch workspace auth with role-based access control; however the MCP server itself "must be enabled by Hightouch - contact us to turn it... | [Free to start](../gates/free.md) |
| [TheirStack](../tools/theirstack.md)
theirstack.com | [Official MCP](../mcp/official.md) | [https://theirstack.com/en/job-posting-mcp](https://theirstack.com/en/job-posting-mcp) | unknown - page references a "How does authentication work?" FAQ but the answer wasn't visible in the fetched content; requires free signup/login to... | [Free to start](../gates/free.md) |
| [Amplemarket (Duo Copilot)](../tools/amplemarket.md)
amplemarket.com | [Official MCP](../mcp/official.md) | [https://knowledge.amplemarket.com/articles/802268531...](https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server) | Account sign-in (no API key needed) - "sign in with your Amplemarket account when prompted" | [Paid, self-serve](../gates/paid.md) |
| [Arphie](../tools/arphie.md)
arphie.ai | [Official MCP](../mcp/official.md) | referenced via pricing/product pages describing an "Arphie... | unknown | [Paid, self-serve](../gates/paid.md) |
| [Attention](../tools/attention.md)
attention.com | [Official MCP](../mcp/official.md) | [https://docs.attention.com/attention-mcp-server](https://docs.attention.com/attention-mcp-server) +1 more | unknown - not confirmed in the sources reviewed. | [Paid, self-serve](../gates/paid.md) |
| [Maildoso](../tools/maildoso.md)
maildoso.ai | [Official MCP](../mcp/official.md) | [https://maildoso.ai/](https://maildoso.ai/) | unknown - described only as "API and MCP access" bundled into every plan, without a documented auth mechanism in sourced pages. | [Paid, self-serve](../gates/paid.md) |
| [Ortto](../tools/ortto.md)
ortto.com | [Official MCP](../mcp/official.md) | [https://mcp-api-us.ortto.app/mcp](https://mcp-api-us.ortto.app/mcp) +1 more | A scoped JWT key created as an MCP data source inside the Ortto account, passed as a "jwt" query parameter on the URL. | [Paid, self-serve](../gates/paid.md) |
| [Responsive (formerly RFPIO)](../tools/responsive.md)
responsive.io | [Official MCP](../mcp/official.md) | [https://www.responsive.io/capability/mcp-server](https://www.responsive.io/capability/mcp-server) +2 more | unknown - not detailed in the sources reviewed. | [Paid, self-serve](../gates/paid.md) |
| [Salesforge (Agent Frank)](../tools/salesforge.md)
salesforge.ai | [Official MCP](../mcp/official.md) | [https://help.salesforge.ai/en/articles/10333582-sale...](https://help.salesforge.ai/en/articles/10333582-salesforge-mcp-server-connect-with-ai-assistants) | unknown specifics (help article confirms an official MCP server "to connect with AI assistants" alongside API and CLI access, but exact auth flow not... | [Paid, self-serve](../gates/paid.md) |
| [Snitcher](../tools/snitcher.md)
snitcher.com | [Official MCP](../mcp/official.md) | [https://www.snitcher.com/changelog/point-claude-at-s...](https://www.snitcher.com/changelog/point-claude-at-snitcher/) | unknown - vendor changelog points to docs.snitcher.com for authentication specifics, not independently confirmed. | [Paid, self-serve](../gates/paid.md) |
| [Sumble](../tools/sumble.md)
sumble.com | [Official MCP](../mcp/official.md) | [https://docs.sumble.com/pages/KLH6XuEHsUssUZW6C1i4](https://docs.sumble.com/pages/KLH6XuEHsUssUZW6C1i4) | unknown - not disclosed in the public docs excerpt available | [Paid, self-serve](../gates/paid.md) |
| [Clari](../tools/clari.md)
clari.com | [Official MCP](../mcp/official.md) | [https://www.clari.com/press/clari-salesloft-forecast...](https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/) | unknown / not disclosed publicly | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Ada](../tools/ada.md)
ada.cx | [Official MCP](../mcp/official.md) | [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server) | none documented - connects over HTTP with no credential requirement described in the docs. | [Enterprise only](../gates/enterprise-only.md) |
| [Allego](../tools/allego.md)
allego.com | [Official MCP](../mcp/official.md) | [https://www.allego.com/platform/integrations/](https://www.allego.com/platform/integrations/) | unknown - vendor material states the MCP server connects to Salesforce Einstein, Microsoft Copilot, and enterprise self-hosted copilots with... | [Enterprise only](../gates/enterprise-only.md) |
| [Clari (+ Salesloft agents)](../tools/clari.md)
clari.com | [Official MCP](../mcp/official.md) | [https://www.clari.com/press/clari-salesloft-forecast...](https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/) | unknown - announcement confirms an official MCP server (works with Claude, ChatGPT, Microsoft Copilot, Gemini, and Salesforce Agentforce) but does... | [Enterprise only](../gates/enterprise-only.md) |
| [Default](../tools/default.md)
default.com | [Official MCP](../mcp/official.md) | [https://www.default.com](https://www.default.com) | unknown - not documented anywhere found (checked default.com, default.com/product, docs.default.com). | [Enterprise only](../gates/enterprise-only.md) |
| [Demandbase (Demandbase One)](../tools/demandbase.md)
demandbase.com | [Official MCP](../mcp/official.md) | [https://developer.demandbase.com/docs/mcp](https://developer.demandbase.com/docs/mcp) +1 more | unknown - the account-team-gated support article that likely covers this returned HTTP 403 and could not be read; docs confirm the MCP is read-only... | [Enterprise only](../gates/enterprise-only.md) |
| [Gong](../tools/gong.md)
gong.io | [Official MCP](../mcp/official.md) | [https://help.gong.io/docs/about-gong-mcp](https://help.gong.io/docs/about-gong-mcp) +2 more | Official MCP client+server ships as part of Gong's enterprise agent stack (used to connect Microsoft 365 Copilot, Salesforce, etc.); community... | [Enterprise only](../gates/enterprise-only.md) |
| [Highspot](../tools/highspot.md)
highspot.com | [Official MCP](../mcp/official.md) | [https://www.highspot.com/product/mcp-server/](https://www.highspot.com/product/mcp-server/) | unknown - product page describes agent-to-agent access via OpenAI, Anthropic, and Microsoft Copilot integrations but does not detail the underlying... | [Enterprise only](../gates/enterprise-only.md) |
| [Ironclad](../tools/ironclad.md)
ironcladapp.com | [Official MCP](../mcp/official.md) | [https://support.ironcladapp.com/hc/en-us/articles/39...](https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server) +1 more | unknown - a single, static MCP endpoint per the support article; specific credential mechanism not detailed in the sources reviewed. | [Enterprise only](../gates/enterprise-only.md) |
| [Otter.ai](../tools/otter-ai.md)
otter.ai | [Official MCP](../mcp/official.md) | [https://help.otter.ai/hc/en-us/articles/352876075696...](https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server) +2 more | unknown - exact auth mechanism not confirmed in public sources; framed under "Otter for Enterprise" with a demo-request CTA. | [Enterprise only](../gates/enterprise-only.md) |
| [Pigment](../tools/pigment.md)
pigment.com | [Official MCP](../mcp/official.md) | [https://www.pigment.com/ai/mcp-server](https://www.pigment.com/ai/mcp-server) +1 more | A workspace admin enables MCP under Settings > Integrations, generating a per-workspace endpoint; individual users then connect with their existing... | [Enterprise only](../gates/enterprise-only.md) |
| [Unify](../tools/unify.md)
unifygtm.com | [Community MCP](../mcp/community.md) | [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp) | Auth0 browser sign-in (auth.unifygtm.com); MCP caches the session cookie (~30-day life) rather than a refresh token - no password or key ever passed... | [Paid, self-serve](../gates/paid.md) |
| [Brandwatch](../tools/brandwatch.md)
brandwatch.com | [Community MCP](../mcp/community.md) | [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch) | unknown - the third-party server's description states it interfaces with "the Brandwatch Consumer Research, Data Upload and Analysis APIs," hosted on... | [Enterprise only](../gates/enterprise-only.md) |

Counted 2026-08-25 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
