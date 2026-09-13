# ZoomInfo: MCP server status, API access gate and what it does

> A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web... Official MCP, Free to start. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
ZoomInfo

# ZoomInfo

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-03
CLI: gtm

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [zoominfo.com](https://zoominfo.com) · entry id 01-zoominfo · source 01-data-enrichment.md line 7

**What it does**
A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human researchers, used for prospecting, account research, and lead enrichment.

**AI features, separated from automation with an AI label on it**
ML is used for record matching/deduplication and lead scoring; "Copilot" is an AI assistant that summarizes accounts, prioritizes leads, and drafts outreach emails on top of the database. The core value (the data itself) is not AI-generated - the AI layer is a research/writing assistant bolted onto a traditional data product.

**RevOps role**
Upstream contact/company data source feeding CRM, enrichment, and outbound tooling; typically the "system of record" for firmographic/contact data in larger RevOps stacks

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth for user-level access, or client credentials for service accounts; no API keys stored by the client. A local mcp-remote bridge is used for stdio clients.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL**: [https://mcp.zoominfo.com/mcp](https://mcp.zoominfo.com/mcp)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-04 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.zoominfo.com/mcp (server card at https://gtm.ai/.well-known/mcp/server-card.json; plugin repo https://github.com/Zoominfo/zoominfo-mcp-plugin)

- [https://mcp.zoominfo.com/mcp](https://mcp.zoominfo.com/mcp)
- [https://gtm.ai/.well-known/mcp/server-card.json](https://gtm.ai/.well-known/mcp/server-card.json)
- [https://github.com/Zoominfo/zoominfo-mcp-plugin](https://github.com/Zoominfo/zoominfo-mcp-plugin)

**What this server exposes**

- **Tools named**: 17
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-12
- **Repo read**: Zoominfo/zoominfo-mcp-plugin
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **Path** Purpose evidence: in a README table · calling it reads

- **Skill** Description evidence: in a README table · calling it reads

- **account-research** Produce an account intelligence brief with firmographics, relationship context, intent, news, and next actions evidence: in a README table · calling it reads

- **build-list** Build targeted account or contact lists from natural-language criteria evidence: in a README table · calling it reads

- **buying-committee** Map decision-makers, influencers, champions, and coverage gaps at a target account evidence: in a README table · calling it reads

- **competitor-analysis** Create fact-led competitor briefs using ZoomInfo data plus public context evidence: in a README table · calling it writes

- **enrich-company** Look up company profiles, firmographics, financials, structure, and growth signals evidence: in a README table · calling it reads

- **enrich-contact** Look up professional contact profiles, title, department, contact data, and accuracy signals evidence: in a README table · calling it reads

- **find-similar** Find lookalike companies or contacts based on a reference account or person evidence: in a README table · calling it reads

- **mcp.json** MCP server registration (Cursor) evidence: in a README table · calling it reads

- **meeting-prep** Prepare for upcoming calls with account, attendee, relationship, and talking-point context evidence: in a README table · calling it reads

- **personalize-email** Draft outreach grounded in account, contact, intent, and trigger signals evidence: in a README table · calling it reads

- **recommend-contacts** Get AI-ranked contact recommendations at a target company evidence: in a README table · calling it reads

- **score-accounts** Prioritize accounts by ICP fit, intent, trigger signals, and explainable scoring evidence: in a README table · calling it reads

- **score-leads** Rank inbound leads by fit, urgency, verified contact data, and recommended action evidence: in a README table · calling it reads

- **tam-sizer** Size a market or territory and produce a reusable ICP filter set evidence: in a README table · calling it writes

- **tech-stack-snapshot** Summarize detected technologies, displacement angles, and integration plays evidence: in a README table · calling it reads

119 of the 521 entries that record an official or community MCP server carry a harvested tool list. The other 402 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: gtm
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @zoominfo/gtm-ai-cli
```

quoted from [https://gtm.ai/docs/cli](https://gtm.ai/docs/cli) on 2026-09-12, via npm

```
brew install zoominfo/gtm-ai/gtm-ai-cli
```

quoted from [https://gtm.ai/docs/cli](https://gtm.ai/docs/cli) on 2026-09-12, via brew

Login or key hint seen on the page:

gtm auth

Subcommands seen with the binary:

auth, cli, companies, contacts

Packages seen, with the version on 2026-09-12:

- [npm: @zoominfo/gtm-ai-cli 1.1.0](https://www.npmjs.com/package/@zoominfo/gtm-ai-cli)

Where it was documented:

- [https://gtm.ai/docs/cli](https://gtm.ai/docs/cli) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (CHANGED 2026-08-25, see notes - the MCP/API path is now self-serve via GTM.AI; the classic seat-based ZoomInfo platform remains enterprise-only)

**API documentation**

[https://gtm.ai/docs](https://gtm.ai/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Zoominfo/zoominfo-mcp-plugin](https://github.com/Zoominfo/zoominfo-mcp-plugin)

**On GitHub**

[github.com/Zoominfo](https://github.com/Zoominfo) tied to the vendor by rule 1, account website https://www.zoominfo.com has the vendor's domain, confidence strong

- **Public repositories**: 8, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [zoominfo-mcp-plugin](https://github.com/Zoominfo/zoominfo-mcp-plugin) | MCP server | ZoomInfo MCP plugin | 7 | 2026-09-03 | |
| [n8n-nodes-zoominfo](https://github.com/Zoominfo/n8n-nodes-zoominfo) | plugin or integration | n8n community node for the ZoomInfo GTM API | 0 | 2026-09-02 | v1.0.0 |
| [gtm-ai-cli](https://github.com/Zoominfo/gtm-ai-cli) | CLI | A command-line tool for searching ZoomInfo's go-to-market data | 1 | 2026-08-30 | v1.1.0 |
| [homebrew-gtm-ai](https://github.com/Zoominfo/homebrew-gtm-ai) | infrastructure | Homebrew tap for gtm-ai formulae | 0 | 2026-08-26 | |
| [api-auth-java-client](https://github.com/Zoominfo/api-auth-java-client) | SDK | Zoominfo API's Java Authentication Client | 2 | 2026-06-30 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 1,032 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://gtm.ai/](https://gtm.ai/)
- [https://gtm.ai/pricing](https://gtm.ai/pricing)
- [https://gtm.ai/docs/mcp](https://gtm.ai/docs/mcp)
- [https://gtm.ai/docs/mcp/clients](https://gtm.ai/docs/mcp/clients)
- [https://gtm.ai/.well-known/mcp/server-card.json](https://gtm.ai/.well-known/mcp/server-card.json)
- [https://gtm.ai/llms.txt](https://gtm.ai/llms.txt)
- [https://www.businesswire.com/news/home/20260601055723/en/ZoomInfo-Launches-GTM.AI-the-Headless-GTM-Context-Layer-to-Ground-Every-AI-Agent-in-Verified-GTM-Data](https://www.businesswire.com/news/home/20260601055723/en/ZoomInfo-Launches-GTM.AI-the-Headless-GTM-Context-Layer-to-Ground-Every-AI-Agent-in-Verified-GTM-Data)
- [https://ir.zoominfo.com/news-releases/news-release-details/zoominfo-launches-gtmai-cli-bringing-verified-gtm-data-command/](https://ir.zoominfo.com/news-releases/news-release-details/zoominfo-launches-gtmai-cli-bringing-verified-gtm-data-command/)
- [https://github.com/Zoominfo/zoominfo-mcp-plugin](https://github.com/Zoominfo/zoominfo-mcp-plugin)
- [https://pipeline.zoominfo.com/operations/zoominfo-mcp-server](https://pipeline.zoominfo.com/operations/zoominfo-mcp-server)
- [https://www.cleanlist.ai/blog/2026-03-19-zoominfo-pricing-guide](https://www.cleanlist.ai/blog/2026-03-19-zoominfo-pricing-guide)
- [https://gtm.ai/content/docs/mcp/tools/enrich-contacts.md](https://gtm.ai/content/docs/mcp/tools/enrich-contacts.md)

12 source URLs. Raw sources field, verbatim:

https://gtm.ai/, https://gtm.ai/pricing, https://gtm.ai/docs/mcp, https://gtm.ai/docs/mcp/clients, https://gtm.ai/.well-known/mcp/server-card.json, https://gtm.ai/llms.txt, https://www.businesswire.com/news/home/20260601055723/en/ZoomInfo-Launches-GTM.AI-the-Headless-GTM-Context-Layer-to-Ground-Every-AI-Agent-in-Verified-GTM-Data, https://ir.zoominfo.com/news-releases/news-release-details/zoominfo-launches-gtmai-cli-bringing-verified-gtm-data-command/, https://github.com/Zoominfo/zoominfo-mcp-plugin, https://pipeline.zoominfo.com/operations/zoominfo-mcp-server, https://www.cleanlist.ai/blog/2026-03-19-zoominfo-pricing-guide, https://gtm.ai/content/docs/mcp/tools/enrich-contacts.md

**Notes, verbatim from the file**
MATERIAL CHANGE FOUND 2026-08-25, and it contradicts this directory's own headline finding that legacy incumbents are enterprise-gated. ZoomInfo launched GTM.AI (gtm.ai), a "headless GTM context layer," announced 2026-06-01, plus a GTM.AI CLI. The published pricing page states "one tier, no contract, no seat fees," 1,000 data credits plus 1,000 AI credits free to start with no credit card, then pay-as-you-go from a $20 minimum top-up at $0.10 per data credit (launch promo; $0.35 regular) and $0.05 per AI credit, charged once per record per year. Search, lookup, find-similar and GTM-context tools are documented as free to call; credits are consumed only on enrichment and AI research. The server card declares 22 tools (account_research, browse_audiences, browse_engagements, contact_research, conversation_intelligence, enrich_companies, enrich_company_signals, enrich_contacts, enrich_intent, enrich_news, enrich_scoops, find_recommended_contacts, find_similar_companies, find_similar_contacts, get_audience, gtm_context, lookup, search_companies, search_contacts, search_intent, search_scoops, update_gtm_context) at server version 3.0 over HTTP. gtm.ai also publishes /.well-known/agent-skills/index.json and /.well-known/api-catalog, which is the most agent-native discovery surface found anywhere in this directory. PRIOR STATE, kept on the record: as of 2026-08-24 this entry read api_gate enterprise-only, on the basis that no self-serve path existed and API access shipped inside annual contracts reportedly starting around $50K/year. That classic seat-based platform motion still exists; what changed is that a credit-metered self-serve door opened next to it. NOT VERIFIED THIS PASS: whether the free GTM.AI tier's data coverage matches a paid ZoomInfo seat, and whether "ZoomInfo Lite" (named in secondary sources as the permanent free tier) is the same thing as the GTM.AI free tier or a separate product. Both need a hands-on check before this is used on camera. 2026-09-03: vendor docs state the GTM.AI MCP tool Enrich Contacts accepts "a name paired with company context, an email address, or a ZoomInfo contact ID" and returns a LinkedIn URL among its fields, subject to package entitlements (https://gtm.ai/content/docs/mcp/tools/enrich-contacts.md); the docs state one bulk data credit per new contact, with re-enrichment within 12 months free.

**Provenance**

- **Entry id**: 01-zoominfo

- **Source file**: 01-data-enrichment.md

- **Source line**: 7

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
